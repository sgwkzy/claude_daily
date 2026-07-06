from __future__ import annotations

import logging
import os
import re
import subprocess
import tempfile
from pathlib import Path

from .models import TranscriptSegment
from .utils import contains_japanese, unique_preserving_order

logger = logging.getLogger(__name__)


def preferred_languages(title: str) -> list[str]:
    """タイトルが日本語中心なら ja を優先、それ以外は en を優先した字幕言語順を返す。

    グローバル版運用（非日本語チャンネルも候補に入る）に合わせ、元動画の言語傾向を
    タイトルから推定して字幕取得の試行順を決める。
    """
    return ["ja", "en"] if contains_japanese(title) else ["en", "ja"]


class TranscriptFetcher:
    def fetch(self, video_id: str, languages: list[str] | None = None, dry_run: bool = False, tor=None) -> list[TranscriptSegment]:
        if dry_run:
            return _dummy_segments()
        languages = languages or ["ja", "en"]
        if tor is None:
            from .tor_control import ManagedTor

            with ManagedTor() as owned_tor:
                return self._fetch_with_tor(video_id, languages, owned_tor)
        return self._fetch_with_tor(video_id, languages, tor)

    def _fetch_with_tor(self, video_id: str, languages: list[str], tor) -> list[TranscriptSegment]:
        try:
            from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled, YouTubeTranscriptApi
            from youtube_transcript_api._errors import IpBlocked, RequestBlocked
            from youtube_transcript_api.proxies import GenericProxyConfig

            api = YouTubeTranscriptApi()
            try:
                fetched = api.fetch(video_id, languages=languages)
                logger.info(
                    "Transcript fetched via youtube_transcript_api: video_id=%s languages=%s segments=%s",
                    video_id,
                    ",".join(languages),
                    len(fetched),
                )
            except NoTranscriptFound:
                # 希望言語(ja/en)が無くても、訳して要約できるので任意の言語の字幕を取得する。
                # グローバルな情報発信のため、利用可能ならどの言語でも率先して拾う。
                fetched = _fetch_any_available(api, video_id, languages)
                if fetched is None:
                    logger.info(
                        "Transcript unavailable in any language: video_id=%s preferred=%s",
                        video_id,
                        ",".join(languages),
                    )
                    return []
            except (IpBlocked, RequestBlocked) as error:
                logger.warning(
                    "Transcript fetch blocked via youtube_transcript_api, retrying through Tor: video_id=%s languages=%s error=%s",
                    video_id,
                    ",".join(languages),
                    error,
                )
                fetched = self._fetch_via_tor_api(
                    YouTubeTranscriptApi,
                    GenericProxyConfig,
                    video_id,
                    languages,
                    tor,
                )
                if fetched is None:
                    return _fetch_with_ytdlp(video_id, languages, tor=tor)
        except TranscriptsDisabled:
            logger.info(
                "Transcript unavailable via youtube_transcript_api: video_id=%s languages=%s reason=disabled",
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
            return _fetch_with_ytdlp(video_id, languages, tor=tor)
        return [
            TranscriptSegment(
                start=int(snippet.start),
                duration=int(snippet.duration),
                text=snippet.text.strip(),
            )
            for snippet in fetched
            if snippet.text.strip()
        ]

    def _fetch_via_tor_api(self, api_cls, proxy_config_cls, video_id: str, languages: list[str], tor):
        if not tor.ensure():
            logger.warning("Tor を起動できず、Tor経由の字幕再取得を断念しました。")
            return None

        proxy_config = proxy_config_cls(
            http_url="socks5://127.0.0.1:9050",
            https_url="socks5://127.0.0.1:9050",
        )
        api = api_cls(proxy_config=proxy_config)
        try:
            fetched = api.fetch(video_id, languages=languages)
            logger.info(
                "Transcript fetched via Tor-backed youtube_transcript_api: video_id=%s languages=%s segments=%s",
                video_id,
                ",".join(languages),
                len(fetched),
            )
            return fetched
        except Exception as error:
            try:
                from youtube_transcript_api import NoTranscriptFound

                if isinstance(error, NoTranscriptFound):
                    fetched = _fetch_any_available(api, video_id, languages)
                    if fetched is not None:
                        return fetched
            except Exception:
                pass
            logger.warning("Tor-backed transcript fetch failed: video_id=%s error=%s", video_id, error)
            return None


def _fetch_any_available(api, video_id: str, preferred: list[str]):
    """希望言語が無い場合に、利用可能な任意言語の字幕を1つ選んで取得する。

    手動作成字幕を優先し、次いで preferred の言語順、最後に残り全部の順で選ぶ。
    取得できなければ None を返す。
    """
    try:
        transcript_list = list(api.list(video_id))
    except Exception as error:
        logger.warning("Transcript list failed: video_id=%s error=%s", video_id, error)
        return None
    if not transcript_list:
        return None

    preferred_roots = [lang.split("-", 1)[0] for lang in preferred]

    def rank(transcript) -> tuple[int, int]:
        manual_rank = 1 if getattr(transcript, "is_generated", False) else 0
        root = str(getattr(transcript, "language_code", "")).split("-", 1)[0]
        lang_rank = preferred_roots.index(root) if root in preferred_roots else len(preferred_roots)
        return (manual_rank, lang_rank)

    chosen = sorted(transcript_list, key=rank)[0]
    logger.info(
        "Transcript fallback to available language: video_id=%s language=%s generated=%s",
        video_id,
        getattr(chosen, "language_code", "?"),
        getattr(chosen, "is_generated", "?"),
    )
    try:
        return chosen.fetch()
    except Exception as error:
        logger.warning("Transcript fetch of fallback language failed: video_id=%s error=%s", video_id, error)
        return None


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


def _fetch_with_ytdlp(video_id: str, languages: list[str], tor=None) -> list[TranscriptSegment]:
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
        if tor is not None and tor.ensure():
            command.extend(["--proxy", "socks5://127.0.0.1:9050"])
        cookies_from_browser = os.getenv("YTDLP_COOKIES_FROM_BROWSER", "").strip()
        cookies_path = os.getenv("YTDLP_COOKIES_PATH", "").strip()
        if cookies_from_browser:
            command.extend(["--cookies-from-browser", cookies_from_browser])
        elif cookies_path:
            command.extend(["--cookies", cookies_path])
        command.append(f"https://www.youtube.com/watch?v={video_id}")
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        subtitle_files = sorted(tmp_path.glob(f"{video_id}*.vtt"))
        # 希望言語のファイルを先に処理する（無ければ任意言語の字幕を使う）。
        preferred_roots = [lang.split("-", 1)[0] for lang in languages] + ["en", "ja"]

        def _lang_rank(path: Path) -> int:
            name = path.name.lower()
            for index, root in enumerate(preferred_roots):
                if f".{root}." in name or f".{root}-" in name:
                    return index
            return len(preferred_roots)

        subtitle_files.sort(key=_lang_rank)
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
    # 希望言語を先頭に置きつつ、訳して要約できるので最後に全言語を拾う。
    expanded.extend(["en", "ja", "all"])
    return unique_preserving_order(expanded)


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
