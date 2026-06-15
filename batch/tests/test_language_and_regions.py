from batch.config import YoutubeConfig
from batch.transcript import preferred_languages
from batch.utils import contains_japanese


def test_contains_japanese() -> None:
    assert contains_japanese("Claude Code 完全入門")
    assert contains_japanese("カタカナ")
    assert contains_japanese("ひらがな")
    assert not contains_japanese("Introducing Claude Fable 5")
    assert not contains_japanese("MCP 101")  # 数字・英字のみ


def test_preferred_languages_japanese_title() -> None:
    assert preferred_languages("Claude Code 実践ガイド") == ["ja", "en"]


def test_preferred_languages_non_japanese_title() -> None:
    assert preferred_languages("Building agents with MCP") == ["en", "ja"]


def test_effective_regions_defaults_to_region_code() -> None:
    cfg = YoutubeConfig(region_code="JP")
    assert cfg.effective_regions() == ["JP"]


def test_effective_regions_uses_regions_when_present() -> None:
    cfg = YoutubeConfig(region_code="JP", regions=["JP", "US"])
    assert cfg.effective_regions() == ["JP", "US"]
