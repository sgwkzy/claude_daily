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
from .models import PipelineStats, VideoCandidate
from .summarizer import TranscriptSummarizer
from .transcript import TranscriptFetcher, compact_segments
from .x_poster import PostPayload

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class PipelineDeps:
    """1 記事処理が必要とする依存をまとめたコンテナ。"""

    root: Path
    settings: Settings
    transcript_fetcher: TranscriptFetcher
    summarizer: TranscriptSummarizer
    media: MediaManager
    header_generator: HeaderImageGenerator
    thumbnail_directions: list[str]
    dry_run: bool = False


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
                languages=[candidate.source_language, "ja", "en"],
                dry_run=deps.dry_run,
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

    # --- ヘッダー画像生成（失敗時はサムネイルにフォールバック）---
    header_path = image_dir / "header.png"
    header_context = HeaderContext(
        title=candidate.title,
        channel=candidate.channel,
        key_phrases=summary.keyPhrases,
        bullet_points=[item.text for item in summary.bulletPoints],
        section_headings=[section.heading for section in summary.sections],
    )
    try:
        generated_headers = []
        for index, direction in enumerate(deps.thumbnail_directions):
            is_primary = index == 0
            destination = header_path if is_primary else image_dir / f"header-{direction}.png"
            prompt_dump = (
                image_dir / f"header-{direction}.prompt.txt" if len(deps.thumbnail_directions) > 1 else None
            )
            generated_headers.append(
                deps.header_generator.generate(
                    thumbnail_path,
                    destination,
                    candidate.title,
                    dry_run=deps.dry_run,
                    direction=direction,
                    context=header_context,
                    prompt_dump_path=prompt_dump,
                )
            )
        if generated_headers and generated_headers[0] != header_path:
            header_path.write_bytes(generated_headers[0].read_bytes())
    except Exception as error:
        print(f"ヘッダー画像生成に失敗したためサムネイルを使用します: {candidate.video_id} / {error}")
        try:
            header_path.write_bytes(thumbnail_path.read_bytes())
        except Exception as fallback_error:
            stats.skipped_errors += 1
            stats.failed_header += 1
            print(f"ヘッダーのフォールバックにも失敗したためスキップします: {candidate.video_id} / {fallback_error}")
            logger.exception("Header fallback failed: video_id=%s", candidate.video_id)
            return None

    # --- 記事書き込み ---
    try:
        frontmatter = build_frontmatter(
            candidate=candidate,
            summary=summary,
            header_image=f"/images/{candidate.video_id}/{header_path.name}",
            hero_image=f"/images/{candidate.video_id}/{header_path.name}",
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
        slug=candidate.video_id.lower(),
        key_phrases=list(summary.keyPhrases),
    )
