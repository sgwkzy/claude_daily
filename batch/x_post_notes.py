"""記事ごとの X 投稿用本文を Markdown ノートに書き出すヘルパ。

X 自動投稿を無効化している間、記事作成時にこのモジュールで投稿本文を生成し、
日付ごとの Markdown ファイルへ書き出す。ユーザーがそれを見て任意のタイミングで
手動投稿する。出力先（Obsidian vault 内のパス）は呼び出し側が渡す。
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from .x_poster import PostPayload, build_tweet_text


def render_post_notes(payloads: list[PostPayload], note_date: date) -> str:
    """日付ノートの Markdown 文字列を組み立てる。"""
    iso = note_date.isoformat()
    lines: list[str] = [
        "---",
        f"title: Claude Daily X投稿 {iso}",
        f"date: {iso}",
        "tags: [x-post, claude-daily]",
        "---",
        "",
        f"# Claude Daily X投稿 {iso}",
        "",
        "> 各記事の X 投稿本文。任意のタイミングでコードブロックの内容をコピーして手動投稿する。",
        "",
    ]
    for payload in payloads:
        lines.append(f"## {payload.article_title}")
        lines.append("")
        lines.append("```text")
        lines.append(build_tweet_text(payload))
        lines.append("```")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_post_notes(payloads: list[PostPayload], output_dir: Path, note_date: date) -> Path:
    """``output_dir/<YYYY-MM-DD>.md`` に投稿本文ノートを書き出す（既存は上書き）。"""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{note_date.isoformat()}.md"
    path.write_text(render_post_notes(payloads, note_date), encoding="utf-8")
    return path
