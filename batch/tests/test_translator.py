from batch.models import SummaryResult
from batch.translator import SummaryTranslator


def _sample_summary() -> SummaryResult:
    return SummaryResult.model_validate(
        {
            "articleTitle": "Claude Code の使い方",
            "bulletPoints": [
                {"time": 0, "text": "最初のポイント"},
                {"time": 120, "text": "次のポイント"},
            ],
            "sections": [
                {"heading": "導入", "time": 0, "image": "/images/x/scene-1.webp", "body": "本文1"},
                {"heading": "実装", "time": 120, "body": "本文2"},
            ],
            "keyPhrases": ["Claude Code", "MCP"],
        }
    )


def test_dummy_translation_preserves_time_and_image() -> None:
    summary = _sample_summary()
    translated = SummaryTranslator(api_key=None).translate(summary, dry_run=True)

    # time と image は言語非依存なので原文のまま保持される。
    assert [b.time for b in translated.bulletPoints] == [0, 120]
    assert translated.sections[0].time == 0
    assert translated.sections[0].image == "/images/x/scene-1.webp"
    assert translated.sections[1].image is None
    # テキストは英語化（ダミーでは [EN] 接頭辞）される。
    assert translated.articleTitle.startswith("[EN]")
    assert all(b.text.startswith("[EN]") for b in translated.bulletPoints)
    assert translated.keyPhrases == ["Claude Code", "MCP"]


def test_translate_requires_api_key_when_not_dry_run() -> None:
    summary = _sample_summary()
    try:
        SummaryTranslator(api_key=None).translate(summary, dry_run=False)
    except ValueError as error:
        assert "ANTHROPIC_API_KEY" in str(error)
    else:  # pragma: no cover
        raise AssertionError("API キー未設定時は ValueError を送出するべきです。")
