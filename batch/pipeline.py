"""1 記事分の処理を main() から分離したパイプライン本体。

main.py の ranked ループが肥大化していたため、1 件分の処理を
``process_candidate`` へ抽出した。挙動・標準出力・ログ文言は従来の main.py を踏襲し、
段階別に例外を捕捉して PipelineStats の失敗種別を記録できるようにしている。
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from .article_writer import build_frontmatter, write_article
from .config import Settings
from .header_image import HeaderContext, HeaderImageGenerator
from .media import MediaManager
from .models import PipelineStats, SummaryResult, VideoCandidate
from .summarizer import TranscriptSummarizer
from .transcript import TranscriptFetcher, compact_segments, preferred_languages
from .translator import SummaryTranslator
from .x_poster import PostPayload

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class PipelineDeps:
    """1 記事処理が必要とする依存をまとめたコンテナ。"""

    root: Path
    settings: Settings
    transcript_fetcher: TranscriptFetcher
    summarizer: TranscriptSummarizer
    translator: SummaryTranslator
    media: MediaManager
    header_generator: HeaderImageGenerator
    thumbnail_directions: list[str]
    dry_run: bool = False
    tor: object | None = None


def _header_context(candidate: VideoCandidate, summary: SummaryResult) -> HeaderContext:
    """要約（原文 or 翻訳）からヘッダー画像生成用のコンテキストを組み立てる。"""
    return HeaderContext(
        title=candidate.title,
        article_title=summary.articleTitle,
        channel=candidate.channel,
        category_label=candidate.matched_keywords[0] if candidate.matched_keywords else "",
        key_phrases=summary.keyPhrases,
        bullet_points=[item.text for item in summary.bulletPoints],
        section_headings=[section.heading for section in summary.sections],
    )


def _generate_header(
    deps: PipelineDeps,
    thumbnail_path: Path,
    destination: Path,
    candidate: VideoCandidate,
    direction: str,
    context: HeaderContext,
    *,
    language: str,
) -> bool:
    """1 言語分のヘッダー画像を生成する。失敗時はサムネイル流用へフォールバックする。

    生成・フォールバックの双方が失敗した場合のみ ``False`` を返す。
    """
    try:
        deps.header_generator.generate(
            thumbnail_path,
            destination,
            candidate.title,
            dry_run=deps.dry_run,
            direction=direction,
            context=context,
            language=language,
        )
        return True
    except Exception as error:
        print(
            f"ヘッダー画像生成({language})に失敗したためサムネイルを使用します: {candidate.video_id} / {error}"
        )
        try:
            destination.write_bytes(thumbnail_path.read_bytes())
            return True
        except Exception as fallback_error:
            print(
                f"ヘッダーのフォールバック({language})にも失敗しました: {candidate.video_id} / {fallback_error}"
            )
            return False


def process_candidate(
    candidate: VideoCandidate,
    deps: PipelineDeps,
    stats: PipelineStats,
) -> PostPayload | None:
    """1 件の動画候補を記事化する。

    成功時は X 投稿用の ``PostPayload`` を返し、スキップ・失敗時は ``None`` を返す。
    ``stats`` はこの関数内で更新する（processed / skipped_* / created / failed_*）。
    失敗は段階別に捕捉し、互換性のため ``skipped_errors`` は従来どおり総数として加算しつつ、
    ``failed_<stage>`` で内訳を残す。
    """
    stats.processed += 1
    article_path = deps.root / deps.settings.pipeline.output_articles_dir / f"{candidate.video_id}.md"
    if article_path.exists():
        stats.skipped_existing += 1
        print(f"既存記事のためスキップ: {candidate.video_id}")
        logger.info("Skipped existing article: video_id=%s", candidate.video_id)
        return None

    # --- 字幕取得 ---
    try:
        segments = compact_segments(
            deps.transcript_fetcher.fetch(
                candidate.video_id,
                languages=preferred_languages(candidate.title),
                dry_run=deps.dry_run,
                tor=deps.tor,
            )
        )
    except Exception as error:
        stats.skipped_errors += 1
        stats.failed_transcript += 1
        print(f"字幕取得でエラーが発生したためスキップします: {candidate.video_id} / {error}")
        logger.exception("Transcript fetch failed: video_id=%s", candidate.video_id)
        return None
    if not segments:
        stats.skipped_transcript += 1
        print(f"字幕が取得できないためスキップ: {candidate.video_id}")
        logger.warning("Skipped due to missing transcript: video_id=%s", candidate.video_id)
        return None

    # --- 要約 ---
    try:
        summary = deps.summarizer.summarize(candidate.title, segments, dry_run=deps.dry_run)
    except Exception as error:
        stats.skipped_errors += 1
        stats.failed_summary += 1
        print(f"要約でエラーが発生したためスキップします: {candidate.video_id} / {error}")
        logger.exception("Summarization failed: video_id=%s", candidate.video_id)
        return None

    image_dir = deps.root / deps.settings.pipeline.output_images_dir / candidate.video_id

    # --- メディア取得（サムネイル / 動画 / scene 抽出）---
    try:
        thumbnail_path = deps.media.download_thumbnail(
            str(candidate.original_thumbnail), image_dir / "thumbnail.webp", dry_run=deps.dry_run
        )
        video_path = deps.media.download_video(candidate.video_id, dry_run=deps.dry_run)
        for index, section in enumerate(summary.sections, start=1):
            frame_path = deps.media.extract_frame(
                video_path, section.time, image_dir / f"scene-{index}.webp", dry_run=deps.dry_run
            )
            if frame_path:
                section.image = f"/images/{candidate.video_id}/{frame_path.name}"
        deps.media.cleanup(video_path)
    except Exception as error:
        stats.skipped_errors += 1
        stats.failed_media += 1
        print(f"メディア取得でエラーが発生したためスキップします: {candidate.video_id} / {error}")
        logger.exception("Media processing failed: video_id=%s", candidate.video_id)
        return None

    # --- 英語翻訳（失敗してもログのみ。日本語記事は生成を続行する）---
    translation: SummaryResult | None
    try:
        translation = deps.translator.translate(summary, dry_run=deps.dry_run)
    except Exception as error:
        translation = None
        print(f"英訳に失敗したため日本語のみで記事化します: {candidate.video_id} / {error}")
        logger.exception("Translation failed: video_id=%s", candidate.video_id)

    # --- ヘッダー画像生成（日本語＝原文 / 英語＝翻訳、失敗時はサムネイルにフォールバック）---
    # 翻訳がある場合は en=header.png / ja=header.ja.png に分け、サイトは en を既定表示する。
    # 翻訳が無い場合は header.png 1 枚（日本語）に集約し、英語表示は日本語へフォールバックする。
    ja_header_path = image_dir / ("header.ja.png" if translation is not None else "header.png")
    en_header_path = image_dir / "header.png"
    primary_direction = deps.thumbnail_directions[0]
    ja_context = _header_context(candidate, summary)

    ja_ok = _generate_header(
        deps, thumbnail_path, ja_header_path, candidate, primary_direction, ja_context, language="ja"
    )
    if not ja_ok:
        stats.skipped_errors += 1
        stats.failed_header += 1
        print(f"ヘッダーのフォールバックにも失敗したためスキップします: {candidate.video_id}")
        logger.exception("Header fallback failed: video_id=%s", candidate.video_id)
        return None

    en_header_image: str | None = None
    if translation is not None:
        en_context = _header_context(candidate, translation)
        if _generate_header(
            deps, thumbnail_path, en_header_path, candidate, primary_direction, en_context, language="en"
        ):
            en_header_image = f"/images/{candidate.video_id}/{en_header_path.name}"
        else:
            print(f"英語ヘッダー画像を生成できなかったため日本語画像を流用します: {candidate.video_id}")

    # 比較用の追加方針（日本語のみ・opt-in）。primary 以外を任意出力する。
    for direction in deps.thumbnail_directions[1:]:
        try:
            deps.header_generator.generate(
                thumbnail_path,
                image_dir / f"header-{direction}.png",
                candidate.title,
                dry_run=deps.dry_run,
                direction=direction,
                context=ja_context,
                prompt_dump_path=image_dir / f"header-{direction}.prompt.txt",
                language="ja",
            )
        except Exception as error:
            print(f"比較用ヘッダー({direction})の生成に失敗しました: {candidate.video_id} / {error}")

    # --- 記事書き込み ---
    try:
        frontmatter = build_frontmatter(
            candidate=candidate,
            summary=summary,
            header_image=f"/images/{candidate.video_id}/{ja_header_path.name}",
            hero_image=f"/images/{candidate.video_id}/{ja_header_path.name}",
            translation=translation,
            en_header_image=en_header_image,
        )
        write_article(frontmatter, article_path)
    except Exception as error:
        stats.skipped_errors += 1
        stats.failed_write += 1
        print(f"記事書き込みでエラーが発生したためスキップします: {candidate.video_id} / {error}")
        logger.exception("Article write failed: video_id=%s", candidate.video_id)
        return None

    stats.created += 1
    print(f"記事を生成しました: {article_path.relative_to(deps.root)}")
    logger.info("Article created: video_id=%s article_path=%s", candidate.video_id, article_path)
    return PostPayload(
        article_title=summary.articleTitle,
        slug=frontmatter.slug or candidate.video_id.lower(),
        key_phrases=list(summary.keyPhrases),
        video_id=candidate.video_id,
    )
