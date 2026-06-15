from __future__ import annotations

from datetime import UTC, datetime

from .config import YoutubeConfig
from .models import VideoCandidate


def dedupe_and_rank(
    candidates: list[VideoCandidate],
    limit: int,
    youtube_config: YoutubeConfig | None = None,
) -> list[VideoCandidate]:
    """Dedupe candidates by videoId, drop Shorts and low-view items, rank by score.

    When `youtube_config` is provided, candidates with `view_count < min_view_count`
    or `duration_sec < min_duration_sec` (default 180s, intended to exclude YouTube
    Shorts) are removed before scoring. The parameter is optional for backward
    compatibility with older call sites and tests.
    """
    deduped: dict[str, VideoCandidate] = {}
    for candidate in candidates:
        existing = deduped.get(candidate.video_id)
        if existing is None:
            deduped[candidate.video_id] = candidate
            continue
        merged_keywords = sorted(set(existing.matched_keywords + candidate.matched_keywords))
        existing.matched_keywords = merged_keywords
        existing.proposed_by_llm = existing.proposed_by_llm or candidate.proposed_by_llm

    ranked = list(deduped.values())
    if youtube_config is not None:
        ranked = [
            c for c in ranked
            if c.view_count >= youtube_config.min_view_count
            and c.duration_sec >= youtube_config.min_duration_sec
        ]
    for candidate in ranked:
        candidate.score = score_candidate(candidate)
    return sorted(ranked, key=lambda item: item.score, reverse=True)[:limit]


def score_candidate(candidate: VideoCandidate, now: datetime | None = None) -> float:
    now = now or datetime.now(UTC)
    age_hours = max((now - candidate.published_at).total_seconds() / 3600, 1)
    freshness = 1 / age_hours
    return candidate.view_count + freshness * 100000

