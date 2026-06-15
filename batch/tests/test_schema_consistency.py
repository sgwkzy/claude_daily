"""batch/models.py の ArticleFrontmatter と site/src/content/config.ts の
zod スキーマがフィールド単位でドリフトしていないか検出する。

型レベルまでは突き合わせず「トップレベルのフィールド名集合が一致するか」を見る。
最も起きやすいドリフト（片側だけにフィールドを足す / 消す）を CI で捕まえる狙い。
JS ランタイムは不要で、config.ts を正規表現でパースする。
"""
from __future__ import annotations

import re
from pathlib import Path

from batch.models import ArticleFrontmatter

_REPO_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_TS = _REPO_ROOT / "site" / "src" / "content" / "config.ts"


def _zod_article_fields() -> set[str]:
    text = _CONFIG_TS.read_text(encoding="utf-8")
    marker = "schema: z.object({"
    start = text.index(marker) + len(marker)
    block = text[start:]
    # article スキーマ内には入れ子の `{` が無いため、最初の `})` で閉じる。
    block = block[: block.index("})")]
    return set(re.findall(r"^\s*(\w+):\s*z\.", block, re.MULTILINE))


def test_frontmatter_fields_match_astro_zod_schema() -> None:
    py_fields = set(ArticleFrontmatter.model_fields.keys())
    zod_fields = _zod_article_fields()
    assert zod_fields, "config.ts から zod フィールドを抽出できませんでした"
    assert py_fields == zod_fields, (
        "ArticleFrontmatter と config.ts のフィールドが不一致です。"
        f" python_only={sorted(py_fields - zod_fields)} ts_only={sorted(zod_fields - py_fields)}"
    )
