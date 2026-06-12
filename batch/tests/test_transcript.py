from batch.transcript import TranscriptFetcher, compact_segments


def test_transcript_dry_run() -> None:
    fetcher = TranscriptFetcher()
    segments = fetcher.fetch("dummy", dry_run=True)
    assert len(segments) >= 3


def test_compact_segments() -> None:
    segments = TranscriptFetcher().fetch("dummy", dry_run=True) * 50
    compacted = compact_segments(segments, max_segments=12)
    assert len(compacted) == 12

