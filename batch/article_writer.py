from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import yaml

from .models import ArticleFrontmatter, SummaryResult, VideoCandidate


def build_frontmatter(
    candidate: VideoCandidate,
    summary: SummaryResult,
    header_image: str,
    hero_image: str | None = None,
    fetched_at: datetime | None = None,
) -> ArticleFrontmatter:
    return ArticleFrontmatter(
        videoId=candidate.video_id,
        title=candidate.title,
        articleTitle=summary.articleTitle,
        channel=candidate.channel,
        channelId=candidate.channel_id,
        publishedAt=candidate.published_at,
        fetchedAt=fetched_at or datetime.now(UTC),
        originalThumbnail=candidate.original_thumbnail,
        headerImage=header_image,
        heroImage=hero_image or header_image,
        viewCount=candidate.view_count,
        durationSec=candidate.duration_sec,
        sourceLanguage=candidate.source_language,
        matchedKeywords=candidate.matched_keywords,
        proposedByLLM=candidate.proposed_by_llm,
        keyPhrases=summary.keyPhrases,
        bulletPoints=summary.bulletPoints,
        sections=summary.sections,
    )


def render_article(frontmatter: ArticleFrontmatter) -> str:
    body_lines = ["", "## ハイライト", ""]
    for point in frontmatter.bulletPoints:
        body_lines.append(f"- [{format_mmss(point.time)}] {point.text}")
    body_lines.extend(["", "## セクション", ""])
    for section in frontmatter.sections:
        body_lines.append(f"### {section.heading}")
        body_lines.append("")
        body_lines.append(f"- 時刻: {format_mmss(section.time)}")
        if section.image:
            body_lines.append(f"- 画像: {section.image}")
        body_lines.append("")
        body_lines.append(section.body)
        body_lines.append("")
    metadata = yaml.safe_dump(
        frontmatter.model_dump(mode="json"),
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip()
    return f"---\n{metadata}\n---\n" + "\n".join(body_lines).rstrip() + "\n"


def write_article(frontmatter: ArticleFrontmatter, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_article(frontmatter), encoding="utf-8")
    return output_path


def format_mmss(seconds: int) -> str:
    minutes, secs = divmod(max(seconds, 0), 60)
    return f"{minutes:02d}:{secs:02d}"
