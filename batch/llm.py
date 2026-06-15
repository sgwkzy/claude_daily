"""LLM クライアント生成を一箇所に集約するファクトリ。

trend_proposer / summarizer がそれぞれ Anthropic クライアントを生成していたため共通化した。
重い依存を dry-run 時に読み込まないよう、import は関数内で遅延させている。
"""
from __future__ import annotations

import json
import re
from typing import Any


def anthropic_client(api_key: str) -> Any:
    from anthropic import Anthropic

    return Anthropic(api_key=api_key)


def parse_json_response(text: str) -> Any:
    """LLM 応答テキストを JSON として解析する。

    モデルが ```json ... ``` のコードフェンスで包む失敗モードに備えてフェンスを剥がし、
    解析失敗時は先頭をスニペット表示した ValueError を送出する。
    """
    cleaned = text.strip()
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", cleaned, re.DOTALL)
    if fence:
        cleaned = fence.group(1).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as error:
        raise ValueError(f"LLM レスポンスの JSON 解析に失敗しました: {cleaned[:200]}") from error
