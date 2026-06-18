from datetime import UTC, datetime
from pathlib import Path

from batch.article_writer import build_frontmatter, render_article, write_article
from batch.fetcher import YouTubeFetcher
from batch.config import load_config
from batch.summarizer import TranscriptSummarizer
from batch.transcript import TranscriptFetcher


def test_article_writer_roundtrip(tmp_path: Path) -> None:
    settings = load_config("batch/config.yaml")
    candidate = YouTubeFetcher(None, settings).fetch(["AI"], dry_run=True)[0]
    summary = TranscriptSummarizer(None).summarize("sample", TranscriptFetcher().fetch("x", dry_run=True), dry_run=True)
    frontmatter = build_frontmatter(candidate, summary, "/images/test/header.png", fetched_at=datetime.now(UTC))
    content = render_article(frontmatter)
    assert "videoId:" in content
    assert "slug:" in content
    assert "articleTitle:" in content
    assert "seoTitle:" in content
    assert "summary:" in content
    assert "heroImage: /images/test/header.png" in content
    target = write_article(frontmatter, tmp_path / "article.md")
    assert target.exists()
