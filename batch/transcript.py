from __future__ import annotations

import logging
import os
import re
import subprocess
import tempfile
from pathlib import Path

from .models import TranscriptSegment

logger = logging.getLogger(__name__)


class TranscriptFetcher:
    def fetch(self, video_id: str, languages: list[str] | None = None, dry_run: bool = False) -> list[TranscriptSegment]:
        if dry_run:
            return _dummy_segments()
        languages = languages or ["ja", "en"]
        try:
            from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled, YouTubeTranscriptApi

            fetched = YouTubeTranscriptApi().fetch(video_id, languages=languages)
            logger.info(
                "Transcript fetched via youtube_transcript_api: video_id=%s languages=%s segments=%s",
                video_id,
                ",".join(languages),
                len(fetched),
            )
        except (NoTranscriptFound, TranscriptsDisabled):
            logger.info(
                "Transcript unavailable via youtube_transcript_api: video_id=%s languages=%s reason=no_transcript",
                video_id,
                ",".join(languages),
            )
            return []
        except Exception as error:
            logger.warning(
                "Transcript fetch failed via youtube_transcript_api, falling back to yt-dlp: video_id=%s languages=%s error=%s",
                video_id,
                ",".join(languages),
                error,
            )
            return _fetch_with_ytdlp(video_id, languages)
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


def _fetch_with_ytdlp(video_id: str, languages: list[str]) -> list[TranscriptSegment]:
    if not _has_command("yt-dlp"):
        logger.warning("yt-dlp is not available for transcript fallback: video_id=%s", video_id)
        return []

    with tempfile.TemporaryDirectory(prefix="claude-daily-transcript-") as tmpdir:
        tmp_path = Path(tmpdir)
        command = [
            "yt-dlp",
            "--skip-download",
            "--ignore-no-formats-error",
            "--write-subs",
            "--write-auto-subs",
            "--sub-format",
            "vtt",
            "--sub-langs",
            ",".join(_expand_language_codes(languages)),
            "-o",
            str(tmp_path / "%(id)s.%(ext)s"),
        ]
        if _has_command("node"):
            command.extend(["--js-runtimes", "node"])
        cookies_from_browser = os.getenv("YTDLP_COOKIES_FROM_BROWSER", "").strip()
        cookies_path = os.getenv("YTDLP_COOKIES_PATH", "").strip()
        if cookies_from_browser:
            command.extend(["--cookies-from-browser", cookies_from_browser])
        elif cookies_path:
            command.extend(["--cookies", cookies_path])
        command.append(f"https://www.youtube.com/watch?v={video_id}")
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        subtitle_files = sorted(tmp_path.glob(f"{video_id}*.vtt"))
        if completed.returncode != 0 and not subtitle_files:
            stderr = completed.stderr.strip().replace("\n", " ")
            logger.warning(
                "yt-dlp transcript fallback failed: video_id=%s languages=%s returncode=%s stderr=%s",
                video_id,
                ",".join(languages),
                completed.returncode,
                stderr[:500],
            )
            return []

        for subtitle_file in subtitle_files:
            segments = _parse_vtt(subtitle_file.read_text(encoding="utf-8", errors="ignore"))
            if segments:
                logger.info(
                    "Transcript fetched via yt-dlp fallback: video_id=%s subtitle_file=%s segments=%s",
                    video_id,
                    subtitle_file.name,
                    len(segments),
                )
                return segments
        logger.warning("yt-dlp subtitle files were downloaded but no segments were parsed: video_id=%s", video_id)
    return []


def _expand_language_codes(languages: list[str]) -> list[str]:
    expanded: list[str] = []
    for language in languages:
        lang = language.strip()
        if not lang:
            continue
        expanded.append(lang)
        if "-" in lang:
            expanded.append(lang.split("-", 1)[0])
    expanded.extend(["en", "ja"])
    seen: list[str] = []
    for lang in expanded:
        if lang not in seen:
            seen.append(lang)
    return seen


def _has_command(command: str) -> bool:
    from shutil import which

    return which(command) is not None


def _parse_vtt(content: str) -> list[TranscriptSegment]:
    segments: list[TranscriptSegment] = []
    cue_lines: list[str] = []
    start = 0
    end = 0

    def flush() -> None:
        nonlocal cue_lines, start, end
        if not cue_lines:
            return
        text = re.sub(r"<[^>]+>", "", " ".join(line.strip() for line in cue_lines)).strip()
        text = re.sub(r"\s+", " ", text)
        if text:
            duration = max(end - start, 0)
            segments.append(TranscriptSegment(start=start, duration=duration, text=text))
        cue_lines = []
        start = 0
        end = 0

    for raw_line in content.splitlines():
        line = raw_line.strip("\ufeff").strip()
        if not line:
            flush()
            continue
        if line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if "-->" in line:
            flush()
            start_text, end_text = [part.strip() for part in line.split("-->", 1)]
            end_text = end_text.split(" ", 1)[0]
            start = _parse_vtt_timestamp(start_text)
            end = _parse_vtt_timestamp(end_text)
            continue
        if line.isdigit():
            continue
        cue_lines.append(line)

    flush()
    return segments


def _parse_vtt_timestamp(value: str) -> int:
    parts = value.replace(",", ".").split(":")
    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        hours = "0"
        minutes, seconds = parts
    else:
        return 0
    try:
        total = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    except ValueError:
        return 0
    return int(total)
