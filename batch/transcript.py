from __future__ import annotations

from .models import TranscriptSegment


class TranscriptFetcher:
    def fetch(self, video_id: str, languages: list[str] | None = None, dry_run: bool = False) -> list[TranscriptSegment]:
        if dry_run:
            return _dummy_segments()
        languages = languages or ["ja", "en"]
        try:
            from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled, YouTubeTranscriptApi

            fetched = YouTubeTranscriptApi().fetch(video_id, languages=languages)
        except (NoTranscriptFound, TranscriptsDisabled):
            return []
        return [
            TranscriptSegment(
                start=int(snippet.start),
                duration=int(snippet.duration),
                text=snippet.text.strip(),
            )
            for snippet in fetched
            if snippet.text.strip()
        ]


def compact_segments(segments: list[TranscriptSegment], max_segments: int = 120) -> list[TranscriptSegment]:
    if len(segments) <= max_segments:
        return segments
    third = max_segments // 3
    return segments[:third] + segments[len(segments) // 2 - third // 2 : len(segments) // 2 + third // 2] + segments[-third:]


def _dummy_segments() -> list[TranscriptSegment]:
    return [
        TranscriptSegment(start=0, duration=18, text="今日はClaude Codeを使った開発フローのリアルを紹介します。"),
        TranscriptSegment(start=72, duration=24, text="Claude CodeはCLIから直接コードベースを読んで編集・テスト・コミットまで進められるのが最大の特徴です。"),
        TranscriptSegment(start=210, duration=26, text="プロンプトを書く前に、AGENTS.mdやCLAUDE.mdに前提を書いておくと精度が一段上がります。"),
        TranscriptSegment(start=360, duration=22, text="MCPを使えば社内のSlackやNotion、社内DBにもClaudeから直接アクセスできます。"),
        TranscriptSegment(start=510, duration=20, text="運用ではプラン承認モードと自動承認モードを使い分けるのがおすすめです。"),
    ]
