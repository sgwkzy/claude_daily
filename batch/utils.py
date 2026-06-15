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
