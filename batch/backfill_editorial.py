"""既存記事に「編集部の視点」(editorial) を後付けするバックフィル。

AdSense「有用性の低いコンテンツ」対策として、各記事へ動画字幕には無いサイト独自の
論評ブロックを追加する。本文(editorial)は LLM コストを避けるため別途用意した
``editorials.json`` から読み込み、本スクリプトは純粋な注入のみを行う。

editorials.json の形式::

    { "<videoId>": { "ja": "...", "en": "..." }, ... }

トップレベル(日本語)へ ``editorial`` を、``en`` ブロックがあれば ``en.editorial`` を
設定して Markdown を書き戻す。既に editorial を持つ記事は ``--force`` 無しでスキップ。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from batch.article_writer import render_article
from batch.models import ArticleFrontmatter


def _split_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        raise ValueError("フロントマターが見つかりません。")
    end = text.index("\n---", 3)
    return yaml.safe_load(text[3:end].strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="既存記事に editorial を後付けします。")
    parser.add_argument("--data", default="batch/editorials.json", help="editorial 本文 JSON のパス。")
    parser.add_argument("--articles", default="site/src/content/articles", help="記事ディレクトリ。")
    parser.add_argument("--force", action="store_true", help="既存 editorial を上書きする。")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    data = json.loads((root / args.data).read_text(encoding="utf-8"))
    articles_dir = root / args.articles

    written = skipped = missing = 0
    for path in sorted(articles_dir.glob("*.md")):
        fm = ArticleFrontmatter.model_validate(_split_frontmatter(path.read_text(encoding="utf-8")))
        if fm.editorial and not args.force:
            skipped += 1
            continue
        entry = data.get(fm.videoId)
        if not entry or not entry.get("ja"):
            missing += 1
            print(f"editorial 未提供: {fm.videoId}")
            continue
        fm.editorial = entry["ja"].strip()
        if fm.en is not None and entry.get("en"):
            fm.en.editorial = entry["en"].strip()
        path.write_text(render_article(fm), encoding="utf-8")
        written += 1

    print(f"完了: 書込={written}, 既存スキップ={skipped}, 本文未提供={missing}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
