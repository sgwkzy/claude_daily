from __future__ import annotations

from batch.article_metadata import build_article_slug, build_seo_title, build_summary_text
from batch.models import SummaryResult


def _make_summary() -> SummaryResult:
    return SummaryResult.model_validate(
        {
            "articleTitle": "Claude Codeをコードベース操作エージェントとして使いこなす実装フローとMCP連携",
            "bulletPoints": [
                {
                    "time": 0,
                    "text": "Claude Codeはコード生成だけでなく、既存リポジトリの調査、編集、テスト、コミットまで一気通貫で進められる。",
                }
            ],
            "sections": [
                {
                    "heading": "概要",
                    "time": 0,
                    "body": "Claude Codeの使い方を整理する本文です。",
                }
            ],
            "keyPhrases": ["Claude Code", "MCP"],
        }
    )


def test_build_article_slug_matches_site_style() -> None:
    slug = build_article_slug(
        "Claude Codeをコードベース操作エージェントとして使いこなす実装フローとMCP連携",
        "DryRun-Pipeline",
    )
    assert slug == "claude-codeをコードベース操作エージェントとして使いこなす実装フローとmcp連携-dryrun-pipeline"


def test_build_seo_title_trims_excess_length() -> None:
    seo_title = build_seo_title("A" * 80)
    assert len(seo_title) == 64


def test_build_summary_text_uses_first_bullet_point() -> None:
    summary = build_summary_text(_make_summary())
    assert summary.startswith("Claude Codeはコード生成だけでなく")
    assert len(summary) <= 121
