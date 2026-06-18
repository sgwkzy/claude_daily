from __future__ import annotations

import re
import unicodedata

from .models import SummaryResult

ARTICLE_SLUG_MAX_LENGTH = 56
SEO_TITLE_MAX_LENGTH = 64
SUMMARY_MAX_LENGTH = 120


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def slugify_path_segment(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).strip().lower()
    normalized = re.sub(r"[\/\s]+", "-", normalized)
    chars = [char for char in normalized if char.isalnum() or char == "-"]
    collapsed = re.sub(r"-+", "-", "".join(chars))
    return collapsed.strip("-")


def trim_slug_segment(slug: str, max_length: int = ARTICLE_SLUG_MAX_LENGTH) -> str:
    if len(slug) <= max_length:
        return slug

    trimmed = slug[:max_length].rstrip("-")
    safe = trimmed[: trimmed.rfind("-")].rstrip("-") if "-" in trimmed else ""
    return safe if len(safe) >= int(max_length * 0.55) else trimmed


def build_article_slug(title: str, article_id: str, explicit_slug: str | None = None) -> str:
    normalized_id = article_id.strip().lower()
    if explicit_slug:
        return slugify_path_segment(explicit_slug) or normalized_id

    title_slug = trim_slug_segment(slugify_path_segment(title))
    return f"{title_slug}-{normalized_id}" if title_slug else normalized_id


def build_seo_title(article_title: str) -> str:
    title = normalize_whitespace(article_title)
    if len(title) <= SEO_TITLE_MAX_LENGTH:
        return title

    shortened = title[:SEO_TITLE_MAX_LENGTH].rstrip(" 、。・-")
    return shortened or title


def build_summary_text(summary: SummaryResult) -> str:
    candidates = [point.text for point in summary.bulletPoints]
    candidates.extend(section.body for section in summary.sections)

    for candidate in candidates:
        text = normalize_whitespace(candidate)
        if text:
            return _truncate_summary(text)

    return _truncate_summary(summary.articleTitle)


def _truncate_summary(text: str, max_length: int = SUMMARY_MAX_LENGTH) -> str:
    if len(text) <= max_length:
        return text

    shortened = text[:max_length].rstrip()
    for marker in ("。", "、", " - ", " "):
        index = shortened.rfind(marker)
        if index >= int(max_length * 0.55):
            shortened = shortened[:index].rstrip(" 、。-")
            break
    return (shortened or text[:max_length]).rstrip(" 、。-") + "…"
