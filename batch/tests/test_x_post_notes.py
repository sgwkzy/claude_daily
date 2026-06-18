from __future__ import annotations

from datetime import date

from batch.x_post_notes import render_post_notes, write_post_notes
from batch.x_poster import PostPayload


def _payloads() -> list[PostPayload]:
    return [
        PostPayload(
            article_title="Claude Fable 5の安全設計を読み解く",
            slug="claude-fable-5-y9wz",
            key_phrases=["Claude Fable 5", "安全設計"],
            video_id="Y9Wz2PV404E",
        ),
        PostPayload(
            article_title="Claude Code 完全入門",
            slug="claude-code-dkcl",
            key_phrases=["Claude Code"],
            video_id="DkClEbyXyq4",
        ),
    ]


def test_render_post_notes_contains_each_article() -> None:
    text = render_post_notes(_payloads(), date(2026, 6, 18))
    assert "# Claude Daily X投稿 2026-06-18" in text
    assert "## Claude Fable 5の安全設計を読み解く" in text
    assert "## Claude Code 完全入門" in text
    # ASCII の videoId ベース URL（日本語スラッグではない）
    assert "https://www.claude-daily.com/articles/y9wz2pv404e/" in text
    assert text.count("```text") == 2


def test_write_post_notes_creates_dated_file(tmp_path) -> None:
    out = write_post_notes(_payloads(), tmp_path / "Posts", date(2026, 6, 18))
    assert out.name == "2026-06-18.md"
    assert out.exists()
    assert "Claude Code 完全入門" in out.read_text(encoding="utf-8")
