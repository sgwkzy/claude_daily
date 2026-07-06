import sys
import types

from batch.transcript import TranscriptFetcher, _parse_vtt, compact_segments


def test_transcript_dry_run() -> None:
    fetcher = TranscriptFetcher()
    segments = fetcher.fetch("dummy", dry_run=True)
    assert len(segments) >= 3


def test_compact_segments() -> None:
    segments = TranscriptFetcher().fetch("dummy", dry_run=True) * 50
    compacted = compact_segments(segments, max_segments=12)
    assert len(compacted) == 12


def test_parse_vtt() -> None:
    content = """WEBVTT

00:00:01.000 --> 00:00:03.500
Hello <c.colorE5E5E5>world</c>

2
00:00:05.000 --> 00:00:07.000 align:start position:0%
Second line
continues here
"""
    segments = _parse_vtt(content)
    assert len(segments) == 2
    assert segments[0].start == 1
    assert segments[0].duration == 2
    assert segments[0].text == "Hello world"
    assert segments[1].text == "Second line continues here"


class _FakeSnippet:
    def __init__(self, text: str = "hello", start: int = 1, duration: int = 2) -> None:
        self.text = text
        self.start = start
        self.duration = duration


class _FakeTor:
    def __init__(self, ready: bool = True) -> None:
        self.ready = ready
        self.ensure_called = False

    def ensure(self, *_args, **_kwargs) -> bool:
        self.ensure_called = True
        return self.ready


def test_fetch_retries_with_tor_backed_api_on_ip_block(monkeypatch) -> None:
    class NoTranscriptFound(Exception):
        pass

    class TranscriptsDisabled(Exception):
        pass

    class IpBlocked(Exception):
        pass

    class RequestBlocked(Exception):
        pass

    proxy_configs = []

    class GenericProxyConfig:
        def __init__(self, http_url: str, https_url: str) -> None:
            self.http_url = http_url
            self.https_url = https_url
            proxy_configs.append(self)

    api_instances = []

    class YouTubeTranscriptApi:
        def __init__(self, proxy_config=None) -> None:
            self.proxy_config = proxy_config
            api_instances.append(self)

        def fetch(self, video_id: str, languages: list[str]):
            if self.proxy_config is None:
                raise IpBlocked("blocked")
            assert video_id == "video-1"
            assert languages == ["en", "ja"]
            return [_FakeSnippet("via tor")]

    api_module = types.ModuleType("youtube_transcript_api")
    api_module.NoTranscriptFound = NoTranscriptFound
    api_module.TranscriptsDisabled = TranscriptsDisabled
    api_module.YouTubeTranscriptApi = YouTubeTranscriptApi
    errors_module = types.ModuleType("youtube_transcript_api._errors")
    errors_module.IpBlocked = IpBlocked
    errors_module.RequestBlocked = RequestBlocked
    proxies_module = types.ModuleType("youtube_transcript_api.proxies")
    proxies_module.GenericProxyConfig = GenericProxyConfig
    monkeypatch.setitem(sys.modules, "youtube_transcript_api", api_module)
    monkeypatch.setitem(sys.modules, "youtube_transcript_api._errors", errors_module)
    monkeypatch.setitem(sys.modules, "youtube_transcript_api.proxies", proxies_module)

    tor = _FakeTor(ready=True)
    segments = TranscriptFetcher().fetch("video-1", languages=["en", "ja"], tor=tor)

    assert tor.ensure_called
    assert len(api_instances) == 2
    assert api_instances[0].proxy_config is None
    assert api_instances[1].proxy_config is proxy_configs[0]
    assert proxy_configs[0].http_url == "socks5://127.0.0.1:9050"
    assert proxy_configs[0].https_url == "socks5://127.0.0.1:9050"
    assert len(segments) == 1
    assert segments[0].text == "via tor"
