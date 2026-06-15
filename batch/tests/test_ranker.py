from datetime import UTC, datetime, timedelta

from batch.config import YoutubeConfig
from batch.models import VideoCandidate
from batch.ranker import dedupe_and_rank


def _make(video_id: str, view_count: int, duration_sec: int) -> VideoCandidate:
    return VideoCandidate.model_validate(
        {
            "videoId": video_id,
            "title": "t",
            "channel": "c",
            "channelId": "cid",
            "publishedAt": (datetime.now(UTC) - timedelta(hours=1)).isoformat(),
            "viewCount": view_count,
            "durationSec": duration_sec,
            "originalThumbnail": "https://example.com/a.webp",
            "sourceLanguage": "ja",
            "matchedKeywords": ["AI"],
            "proposedByLLM": False,
        }
    )


def test_filters_shorts_and_low_view_when_config_supplied() -> None:
    cfg = YoutubeConfig(min_view_count=5000, min_duration_sec=180)
    short_video = _make("short", view_count=999_999, duration_sec=45)
    low_view = _make("lowview", view_count=100, duration_sec=600)
    keeper = _make("keep", view_count=20_000, duration_sec=300)
    ranked = dedupe_and_rank([short_video, low_view, keeper], limit=5, youtube_config=cfg)
    assert [c.video_id for c in ranked] == ["keep"]


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

