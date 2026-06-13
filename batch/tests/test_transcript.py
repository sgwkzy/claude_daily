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
