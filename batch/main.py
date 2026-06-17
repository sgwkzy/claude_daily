from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from batch.config import ensure_directories, load_config
from batch.fetcher import YouTubeFetcher
from batch.header_image import HeaderImageGenerator
from batch.media import MediaManager
from batch.models import PipelineStats
from batch.pipeline import PipelineDeps, process_candidate
from batch.ranker import dedupe_and_rank
from batch.summarizer import TranscriptSummarizer
from batch.transcript import TranscriptFetcher
from batch.trend_proposer import TrendProposer
from batch.utils import unique_preserving_order
from batch.x_poster import PostPayload, XPoster, post_articles_with_delay


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
    parser.add_argument(
        "--no-x-post",
        action="store_true",
        help="新規記事の X 自動投稿をスキップします（ローカル検証向け）。",
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
    pending_x_posts: list[PostPayload] = []

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
    ranked = dedupe_and_rank(candidates, limit=limit, youtube_config=settings.youtube)

    deps = PipelineDeps(
        root=root,
        settings=settings,
        transcript_fetcher=transcript_fetcher,
        summarizer=summarizer,
        media=media,
        header_generator=header_generator,
        thumbnail_directions=thumbnail_directions,
        dry_run=args.dry_run,
    )

    for candidate in ranked:
        payload = process_candidate(candidate, deps, stats)
        if payload is not None:
            pending_x_posts.append(payload)

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
    logger.info(
        "Error breakdown failed_transcript=%s failed_summary=%s failed_media=%s failed_header=%s failed_write=%s",
        stats.failed_transcript,
        stats.failed_summary,
        stats.failed_media,
        stats.failed_header,
        stats.failed_write,
    )

    if pending_x_posts and not args.dry_run and not args.no_x_post:
        poster = XPoster.from_env()
        if poster.enabled:
            print(f"X への自動投稿を開始します: {len(pending_x_posts)} 件")
            posted = post_articles_with_delay(poster, pending_x_posts)
            print(f"X 投稿結果: 成功 {posted}/{len(pending_x_posts)} 件")
            logger.info("X posting finished posted=%s total=%s", posted, len(pending_x_posts))
        else:
            print("X 認証情報が未設定のため自動投稿をスキップしました。")
            logger.info("X posting skipped: credentials missing")
    elif pending_x_posts and (args.dry_run or args.no_x_post):
        logger.info("X posting skipped by flag: pending=%s", len(pending_x_posts))

    return 0


def _resolve_thumbnail_directions(cli_value: str | None, config_value: list[str]) -> list[str]:
    source = cli_value.split(",") if cli_value else config_value
    directions = [item.strip() for item in source if item.strip()]
    if not directions:
        return ["editorial-rebuild"]
    return unique_preserving_order(directions)


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
