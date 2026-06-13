from __future__ import annotations

from pathlib import Path

from batch.post_new_articles import _read_frontmatter


def test_read_frontmatter_parses_yaml(tmp_path: Path) -> None:
    article = tmp_path / "abc.md"
    article.write_text(
        "---\n"
        "videoId: ABC123\n"
        "title: Original Title\n"
        "articleTitle: 日本語の要約見出し\n"
        "keyPhrases:\n"
        "  - Claude\n"
        "  - MCP\n"
        "---\n"
        "本文\n",
        encoding="utf-8",
    )
    data = _read_frontmatter(article)
    assert data["videoId"] == "ABC123"
    assert data["articleTitle"] == "日本語の要約見出し"
    assert data["keyPhrases"] == ["Claude", "MCP"]


def test_read_frontmatter_returns_empty_when_no_frontmatter(tmp_path: Path) -> None:
    article = tmp_path / "x.md"
    article.write_text("本文のみ\n", encoding="utf-8")
    assert _read_frontmatter(article) == {}
