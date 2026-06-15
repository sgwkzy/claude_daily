import pytest

from batch.llm import parse_json_response


def test_parse_json_response_plain() -> None:
    assert parse_json_response('{"keywords": ["a", "b"]}') == {"keywords": ["a", "b"]}


def test_parse_json_response_strips_code_fence() -> None:
    text = '```json\n{"keywords": ["a"]}\n```'
    assert parse_json_response(text) == {"keywords": ["a"]}


def test_parse_json_response_raises_on_invalid() -> None:
    with pytest.raises(ValueError):
        parse_json_response("これはJSONではありません")
