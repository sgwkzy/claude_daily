from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Iterable

from .config import Settings
from .models import VideoCandidate


class YouTubeFetcher:
    def __init__(self, api_key: str | None, settings: Settings) -> None:
        self.api_key = api_key
        self.settings = settings

    def fetch(self, keywords: Iterable[str], dry_run: bool = False) -> list[VideoCandidate]:
        if dry_run:
            return self._dummy_candidates(list(keywords))
        if not self.api_key:
            raise ValueError("YOUTUBE_API_KEY が設定されていません。")
        from googleapiclient.discovery import build

        service = build("youtube", "v3", developerKey=self.api_key)
        collected: list[VideoCandidate] = []
        published_after = (datetime.now(UTC) - timedelta(hours=self.settings.youtube.max_age_hours)).isoformat()

        for region in self.settings.youtube.effective_regions():
            for keyword in keywords:
                search_response = (
                    service.search()
                    .list(
                        part="snippet",
                        type="video",
                        q=keyword,
                        order="viewCount",
                        maxResults=self.settings.youtube.per_keyword_top_n,
                        publishedAfter=published_after,
                        regionCode=region,
                    )
                    .execute()
                )
                video_ids = [item["id"]["videoId"] for item in search_response.get("items", []) if item.get("id", {}).get("videoId")]
                if not video_ids:
                    continue
                videos_response = (
                    service.videos()
                    .list(part="snippet,statistics,contentDetails", id=",".join(video_ids))
                    .execute()
                )
                for item in videos_response.get("items", []):
                    collected.append(self._to_candidate(item, keyword))
        return collected

    def _to_candidate(self, item: dict, keyword: str) -> VideoCandidate:
        snippet = item["snippet"]
        statistics = item.get("statistics", {})
        return VideoCandidate.model_validate(
            {
                "videoId": item["id"],
                "title": snippet["title"],
                "channel": snippet["channelTitle"],
                "channelId": snippet["channelId"],
                "publishedAt": snippet["publishedAt"],
                "viewCount": int(statistics.get("viewCount", 0)),
                "durationSec": _parse_duration_seconds(item.get("contentDetails", {}).get("duration", "PT0S")),
                "originalThumbnail": _best_thumbnail(snippet.get("thumbnails", {})),
                "sourceLanguage": snippet.get("defaultAudioLanguage") or snippet.get("defaultLanguage") or "und",
                "matchedKeywords": [keyword],
                "proposedByLLM": False,
            }
        )

    def _dummy_candidates(self, keywords: list[str]) -> list[VideoCandidate]:
        base_keyword = keywords[0] if keywords else "Claude"
        now = datetime.now(UTC)
        today = now
        yesterday = now - timedelta(days=1)
        two_days_ago = now - timedelta(days=2)
        return [
            VideoCandidate.model_validate(
                {
                    "videoId": "dryrun-claude-code",
                    "title": "Claude Codeで開発フローを変える 実践ガイド",
                    "channel": "AI Dev Lounge",
                    "channelId": "demo-channel-1",
                    "publishedAt": today.isoformat(),
                    "viewCount": 184000,
                    "durationSec": 612,
                    "originalThumbnail": "https://example.com/thumb-claude-code.webp",
                    "sourceLanguage": "ja",
                    "matchedKeywords": [base_keyword, "Claude Code"],
                    "proposedByLLM": False,
                }
            ),
            VideoCandidate.model_validate(
                {
                    "videoId": "dryrun-mcp-overview",
                    "title": "MCPで広がるClaudeの可能性 — 接続先と設計の勘所",
                    "channel": "Anthropic JP Community",
                    "channelId": "demo-channel-2",
                    "publishedAt": today.isoformat(),
                    "viewCount": 96500,
                    "durationSec": 538,
                    "originalThumbnail": "https://example.com/thumb-mcp.webp",
                    "sourceLanguage": "ja",
                    "matchedKeywords": [base_keyword, "MCP"],
                    "proposedByLLM": True,
                }
            ),
            VideoCandidate.model_validate(
                {
                    "videoId": "dryrun-agents-md",
                    "title": "AGENTS.md と CLAUDE.md の書き方 完全版",
                    "channel": "AI Dev Lounge",
                    "channelId": "demo-channel-1",
                    "publishedAt": yesterday.isoformat(),
                    "viewCount": 132000,
                    "durationSec": 482,
                    "originalThumbnail": "https://example.com/thumb-agents.webp",
                    "sourceLanguage": "ja",
                    "matchedKeywords": [base_keyword, "Claude Code"],
                    "proposedByLLM": False,
                }
            ),
            VideoCandidate.model_validate(
                {
                    "videoId": "dryrun-subagents",
                    "title": "サブエージェントで仕事を分業する Claudeの使いこなし",
                    "channel": "Anthropic JP Community",
                    "channelId": "demo-channel-2",
                    "publishedAt": yesterday.isoformat(),
                    "viewCount": 78000,
                    "durationSec": 421,
                    "originalThumbnail": "https://example.com/thumb-subagents.webp",
                    "sourceLanguage": "ja",
                    "matchedKeywords": [base_keyword, "AIエージェント"],
                    "proposedByLLM": True,
                }
            ),
            VideoCandidate.model_validate(
                {
                    "videoId": "dryrun-prompting",
                    "title": "Claude向けプロンプト設計 5つの原則",
                    "channel": "AI Research Notes",
                    "channelId": "demo-channel-3",
                    "publishedAt": two_days_ago.isoformat(),
                    "viewCount": 54000,
                    "durationSec": 367,
                    "originalThumbnail": "https://example.com/thumb-prompting.webp",
                    "sourceLanguage": "ja",
                    "matchedKeywords": [base_keyword],
                    "proposedByLLM": False,
                }
            ),
        ]


def _best_thumbnail(thumbnails: dict) -> str:
    for key in ("maxres", "standard", "high", "medium", "default"):
        value = thumbnails.get(key)
        if value and value.get("url"):
            return value["url"]
    return "https://i.ytimg.com/vi/default/hqdefault.jpg"


def _parse_duration_seconds(duration: str) -> int:
    hours = minutes = seconds = 0
    if not duration.startswith("PT"):
        return 0
    token = duration[2:]
    number = ""
    for char in token:
        if char.isdigit():
            number += char
            continue
        if char == "H":
            hours = int(number or 0)
        elif char == "M":
            minutes = int(number or 0)
        elif char == "S":
            seconds = int(number or 0)
        number = ""
    return hours * 3600 + minutes * 60 + seconds
