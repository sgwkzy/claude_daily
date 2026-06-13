from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from batch.article_writer import build_frontmatter, write_article
from batch.config import ensure_directories, load_config
from batch.fetcher import YouTubeFetcher
from batch.header_image import HeaderContext, HeaderImageGenerator
from batch.media import MediaManager
from batch.models import PipelineStats
from batch.ranker import dedupe_and_rank
from batch.summarizer import TranscriptSummarizer
from batch.transcript import TranscriptFetcher, compact_segments
from batch.trend_proposer import TrendProposer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YouTube人気動画ポータルのバッチ処理を実行します。")
    parser.add_argument("--dry-run", action="store_true", help="API呼び出しを行わずダミーデータで動作確認します。")
    parser.add_argument("--limit", type=int, default=None, help="処理する動画本数を上書きします。")
    parser.add_argument("--config", default="batch/config.yaml", help="設定ファイルのパスを指定します。")
    parser.add_argument(
        "--thumbnail-directions",
        default=None,
        help="サムネイル方針をカンマ区切りで上書きします。例: source-first,source-explainer",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    settings = load_config(root / args.config)
    ensure_directories(root, settings)
    _configure_logging(root / settings.pipeline.temp_dir)

    api_keys = {
        "youtube": os.getenv("YOUTUBE_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "openai": os.getenv("OPENAI_API_KEY"),
    }
    limit = args.limit or settings.youtube.limit_total
    thumbnail_directions = _resolve_thumbnail_directions(args.thumbnail_directions, settings.prompts.thumbnail_directions)
    stats = PipelineStats()

    trend_proposer = TrendProposer(api_keys["anthropic"])
    fetcher = YouTubeFetcher(api_keys["youtube"], settings)
    transcript_fetcher = TranscriptFetcher()
    summarizer = TranscriptSummarizer(api_keys["anthropic"])
    media = MediaManager(root / settings.pipeline.temp_dir)
    header_generator = HeaderImageGenerator(api_keys["openai"], settings.prompts.header_style)
    logger = logging.getLogger(__name__)

    print("設定を読み込みました。")
    logger.info("Batch started dry_run=%s limit=%s config=%s", args.dry_run, limit, args.config)
    trend_keywords = trend_proposer.propose(
        fixed_keywords=settings.youtube.keywords,
        limit=settings.prompts.trend_limit,
        dry_run=args.dry_run,
    )
    print(f"提案キーワード: {', '.join(trend_keywords) if trend_keywords else 'なし'}")

    keywords = settings.youtube.keywords + trend_keywords
    candidates = fetcher.fetch(keywords=keywords, dry_run=args.dry_run)
    ranked = dedupe_and_rank(candidates, limit=limit)

    for candidate in ranked:
        stats.processed += 1
        article_path = root / settings.pipeline.output_articles_dir / f"{candidate.video_id}.md"
        if article_path.exists():
            stats.skipped_existing += 1
            print(f"既存記事のためスキップ: {candidate.video_id}")
            logger.info("Skipped existing article: video_id=%s", candidate.video_id)
            continue
        try:
            segments = compact_segments(
                transcript_fetcher.fetch(candidate.video_id, languages=[candidate.source_language, "ja", "en"], dry_run=args.dry_run)
            )
            if not segments:
                stats.skipped_transcript += 1
                print(f"字幕が取得できないためスキップ: {candidate.video_id}")
                logger.warning("Skipped due to missing transcript: video_id=%s", candidate.video_id)
                continue

            summary = summarizer.summarize(candidate.title, segments, dry_run=args.dry_run)
            image_dir = root / settings.pipeline.output_images_dir / candidate.video_id
            thumbnail_path = media.download_thumbnail(str(candidate.original_thumbnail), image_dir / "thumbnail.webp", dry_run=args.dry_run)
            video_path = media.download_video(candidate.video_id, dry_run=args.dry_run)
            for index, section in enumerate(summary.sections, start=1):
                frame_path = media.extract_frame(video_path, section.time, image_dir / f"scene-{index}.webp", dry_run=args.dry_run)
                if frame_path:
                    section.image = f"/images/{candidate.video_id}/{frame_path.name}"
            media.cleanup(video_path)

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
                for index, direction in enumerate(thumbnail_directions):
                    is_primary = index == 0
                    destination = header_path if is_primary else image_dir / f"header-{direction}.png"
                    prompt_dump = image_dir / f"header-{direction}.prompt.txt" if len(thumbnail_directions) > 1 else None
                    generated_headers.append(
                        header_generator.generate(
                            thumbnail_path,
                            destination,
                            candidate.title,
                            dry_run=args.dry_run,
                            direction=direction,
                            context=header_context,
                            prompt_dump_path=prompt_dump,
                        )
                    )
                if generated_headers and generated_headers[0] != header_path:
                    header_path.write_bytes(generated_headers[0].read_bytes())
            except Exception as error:
                print(f"ヘッダー画像生成に失敗したためサムネイルを使用します: {candidate.video_id} / {error}")
                header_path.write_bytes(thumbnail_path.read_bytes())

            frontmatter = build_frontmatter(
                candidate=candidate,
                summary=summary,
                header_image=f"/images/{candidate.video_id}/{header_path.name}",
                hero_image=f"/images/{candidate.video_id}/{header_path.name}",
            )
            write_article(frontmatter, article_path)
            stats.created += 1
            print(f"記事を生成しました: {article_path.relative_to(root)}")
            logger.info("Article created: video_id=%s article_path=%s", candidate.video_id, article_path)
        except Exception as error:
            stats.skipped_errors += 1
            print(f"動画処理でエラーが発生したためスキップします: {candidate.video_id} / {error}")
            logger.exception("Video processing failed: video_id=%s", candidate.video_id)
            continue

    print(
        "実行結果:"
        f" 処理候補={stats.processed}, 作成={stats.created}, 既存スキップ={stats.skipped_existing},"
        f" 字幕スキップ={stats.skipped_transcript}, エラー={stats.skipped_errors}"
    )
    logger.info(
        "Batch finished processed=%s created=%s skipped_existing=%s skipped_transcript=%s skipped_errors=%s",
        stats.processed,
        stats.created,
        stats.skipped_existing,
        stats.skipped_transcript,
        stats.skipped_errors,
    )
    return 0


def _resolve_thumbnail_directions(cli_value: str | None, config_value: list[str]) -> list[str]:
    source = cli_value.split(",") if cli_value else config_value
    directions = [item.strip() for item in source if item.strip()]
    if not directions:
        return ["source-explainer"]
    seen: list[str] = []
    for direction in directions:
        if direction not in seen:
            seen.append(direction)
    return seen


def _configure_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "batch.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path, encoding="utf-8"),
        ],
        force=True,
    )


if __name__ == "__main__":
    raise SystemExit(main())
