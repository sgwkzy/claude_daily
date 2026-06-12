from batch.config import load_config
from batch.fetcher import YouTubeFetcher, _parse_duration_seconds


def test_fetcher_dry_run() -> None:
    settings = load_config("batch/config.yaml")
    fetcher = YouTubeFetcher(api_key=None, settings=settings)
    items = fetcher.fetch(["AI"], dry_run=True)
    assert len(items) == 5
    assert all(item.video_id.startswith("dryrun-") for item in items)


def test_parse_duration_seconds() -> None:
    assert _parse_duration_seconds("PT7M3S") == 423
    assert _parse_duration_seconds("PT1H2M") == 3720

