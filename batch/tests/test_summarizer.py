from batch.summarizer import TranscriptSummarizer
from batch.transcript import TranscriptFetcher


def test_summarizer_dry_run() -> None:
    summarizer = TranscriptSummarizer(api_key=None)
    segments = TranscriptFetcher().fetch("dummy", dry_run=True)
    result = summarizer.summarize("sample", segments, dry_run=True)
    assert len(result.sections) == 4
    assert result.keyPhrases

