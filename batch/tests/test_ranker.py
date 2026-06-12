from datetime import UTC, datetime, timedelta

from batch.models import VideoCandidate
from batch.ranker import dedupe_and_rank


def test_dedupe_and_rank_merges_keywords() -> None:
    now = datetime.now(UTC)
    candidate1 = VideoCandidate.model_validate(
        {
            "videoId": "abc",
            "title": "A",
            "channel": "C",
            "channelId": "cid",
            "publishedAt": (now - timedelta(hours=1)).isoformat(),
            "viewCount": 1000,
            "durationSec": 10,
            "originalThumbnail": "https://example.com/a.webp",
            "sourceLanguage": "ja",
            "matchedKeywords": ["AI"],
            "proposedByLLM": False,
        }
    )
    candidate2 = VideoCandidate.model_validate(
        {
            "videoId": "abc",
            "title": "A",
            "channel": "C",
            "channelId": "cid",
            "publishedAt": (now - timedelta(hours=2)).isoformat(),
            "viewCount": 2000,
            "durationSec": 10,
            "originalThumbnail": "https://example.com/a.webp",
            "sourceLanguage": "ja",
            "matchedKeywords": ["Claude"],
            "proposedByLLM": True,
        }
    )
    ranked = dedupe_and_rank([candidate1, candidate2], limit=5)
    assert len(ranked) == 1
    assert sorted(ranked[0].matched_keywords) == ["AI", "Claude"]
    assert ranked[0].proposed_by_llm is True

