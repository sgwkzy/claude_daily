from __future__ import annotations

from typing import Iterable, TypeVar

T = TypeVar("T")


def unique_preserving_order(items: Iterable[T]) -> list[T]:
    """出現順を保ったまま重複を除いたリストを返す。"""
    seen: list[T] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def contains_japanese(text: str) -> bool:
    """ひらがな・カタカナ・CJK 統合漢字を 1 文字でも含めば True。"""
    for ch in text:
        code = ord(ch)
        if (
            0x3040 <= code <= 0x309F  # ひらがな
            or 0x30A0 <= code <= 0x30FF  # カタカナ
            or 0x4E00 <= code <= 0x9FFF  # CJK 統合漢字
        ):
            return True
    return False
