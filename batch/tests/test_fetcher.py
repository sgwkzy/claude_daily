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


class _FakeResponse:
    def __init__(self, payload: dict, status_code: int = 200) -> None:
        self._payload = payload
        self.status_code = status_code

    def json(self) -> dict:
        return self._payload


class _FakeTor:
    """ManagedTor のスタブ。ensure() が呼ばれたかと、その戻り値を制御する。"""

    def __init__(self, ready: bool = True) -> None:
        self.ready = ready
        self.ensure_called = False

    def ensure(self, *_args, **_kwargs) -> bool:
        self.ensure_called = True
        return self.ready


def test_call_falls_back_to_tor_on_network_error(monkeypatch) -> None:
    from batch import proxy_fetch

    settings = load_config("batch/config.yaml")
    fetcher = YouTubeFetcher(api_key="dummy-key", settings=settings)

    calls: list[str] = []

    def fake_proxy_fetch(url: str):
        calls.append(url)
        return _FakeResponse({"items": [{"ok": True}]})

    monkeypatch.setattr(proxy_fetch, "fetch", fake_proxy_fetch)
    tor = _FakeTor(ready=True)

    def primary():
        raise ConnectionError("boom")

    result = fetcher._call(primary, "https://example.com/search", {"q": "AI"}, tor)
    assert result == {"items": [{"ok": True}]}
    assert tor.ensure_called
    assert len(calls) == 1
    assert "key=dummy-key" in calls[0]


def test_call_gives_up_when_tor_unavailable(monkeypatch) -> None:
    from batch import proxy_fetch

    settings = load_config("batch/config.yaml")
    fetcher = YouTubeFetcher(api_key="dummy-key", settings=settings)

    monkeypatch.setattr(
        proxy_fetch, "fetch",
        lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("Tor 不可なら fetch を呼ばない")),
    )

    def primary():
        raise ConnectionError("boom")

    result = fetcher._call(primary, "https://example.com/search", {"q": "AI"}, _FakeTor(ready=False))
    assert result == {}


def test_call_skips_tor_on_success() -> None:
    settings = load_config("batch/config.yaml")
    fetcher = YouTubeFetcher(api_key="dummy-key", settings=settings)
    tor = _FakeTor(ready=True)

    result = fetcher._call(lambda: {"items": []}, "https://example.com/search", {"q": "AI"}, tor)
    assert result == {"items": []}
    assert not tor.ensure_called

