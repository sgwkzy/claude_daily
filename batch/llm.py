"""LLM クライアント生成を一箇所に集約するファクトリ。

trend_proposer / summarizer がそれぞれ Anthropic クライアントを生成していたため共通化した。
重い依存を dry-run 時に読み込まないよう、import は関数内で遅延させている。
"""
from __future__ import annotations

from typing import Any


def anthropic_client(api_key: str) -> Any:
    from anthropic import Anthropic

    return Anthropic(api_key=api_key)
