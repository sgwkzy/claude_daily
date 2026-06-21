from pathlib import Path

from batch.config import PipelineConfig, PromptConfig, Settings, YoutubeConfig
from batch.header_image import HeaderImageGenerator
from batch.media import MediaManager
from batch.models import PipelineStats, VideoCandidate
from batch.pipeline import PipelineDeps, process_candidate
from batch.summarizer import TranscriptSummarizer
from batch.transcript import TranscriptFetcher
from batch.translator import SummaryTranslator
from batch.x_poster import PostPayload


def _make_settings(root: Path) -> Settings:
    return Settings(
        youtube=YoutubeConfig(),
        pipeline=PipelineConfig(
            output_articles_dir="articles",
            output_images_dir="images",
            temp_dir="tmp",
        ),
        prompts=PromptConfig(),
    )


def _make_candidate() -> VideoCandidate:
    return VideoCandidate.model_validate(
        {
            "videoId": "dryrun-pipeline",
            "title": "Claude Code 実践ガイド",
            "channel": "AI Dev Lounge",
            "channelId": "cid",
            "publishedAt": "2026-06-15T00:00:00Z",
            "viewCount": 12345,
            "durationSec": 600,
            "originalThumbnail": "https://example.com/thumb.webp",
            "sourceLanguage": "ja",
            "matchedKeywords": ["Claude"],
            "proposedByLLM": False,
        }
    )


def _make_deps(root: Path) -> PipelineDeps:
    settings = _make_settings(root)
    return PipelineDeps(
        root=root,
        settings=settings,
        transcript_fetcher=TranscriptFetcher(),
        summarizer=TranscriptSummarizer(api_key=None),
        translator=SummaryTranslator(api_key=None),
        media=MediaManager(root / settings.pipeline.temp_dir),
        header_generator=HeaderImageGenerator(api_key=None, style_prompt="test style"),
        thumbnail_directions=["editorial-rebuild"],
        dry_run=True,
    )


def test_process_candidate_creates_article_and_returns_payload(tmp_path: Path) -> None:
    deps = _make_deps(tmp_path)
    stats = PipelineStats()
    candidate = _make_candidate()

    payload = process_candidate(candidate, deps, stats)

    assert isinstance(payload, PostPayload)
    assert payload.slug == "claude-codeをコードベース操作エージェントとして使いこなす実装フローとmcp連携-dryrun-pipeline"
    assert stats.created == 1
    assert stats.processed == 1
    assert stats.skipped_errors == 0

    article_path = tmp_path / "articles" / "dryrun-pipeline.md"
    assert article_path.exists()
    article_text = article_path.read_text(encoding="utf-8")
    assert "seoTitle:" in article_text
    assert "summary:" in article_text
    # 英語ブロックと日英 2 枚のヘッダー画像が生成される。
    assert "en:" in article_text
    en_header_path = tmp_path / "images" / "dryrun-pipeline" / "header.png"
    ja_header_path = tmp_path / "images" / "dryrun-pipeline" / "header.ja.png"
    assert en_header_path.exists()
    assert ja_header_path.exists()


def test_process_candidate_skips_existing(tmp_path: Path) -> None:
    deps = _make_deps(tmp_path)
    stats = PipelineStats()
    candidate = _make_candidate()
    article_path = tmp_path / "articles" / "dryrun-pipeline.md"
    article_path.parent.mkdir(parents=True, exist_ok=True)
    article_path.write_text("---\nvideoId: dryrun-pipeline\n---\n", encoding="utf-8")

    payload = process_candidate(candidate, deps, stats)

    assert payload is None
    assert stats.skipped_existing == 1
    assert stats.created == 0
