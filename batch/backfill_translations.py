"""既存記事に英語ブロック（`en`）と英語ヘッダー画像を後付けするバックフィル。

サイトを英語デフォルト + 日本語 `/jp/` の完全バイリンガルにするにあたり、
過去記事はトップレベル（日本語）しか持たない。本スクリプトは各記事 Markdown を読み、
未翻訳のものだけを対象に:

1. 日本語フロントマターから ``SummaryResult`` を組み立てて英訳する。
2. 既存の日本語ヘッダー画像 ``header.png`` を ``header.ja.png`` へ退避し、
   トップレベルの ``headerImage`` / ``heroImage`` をそちらへ向け直す。
3. 英語ヘッダー画像を新たに生成して ``header.png``（既定 = 英語）に置く。
4. ``en`` ブロックを追記して Markdown を書き戻す。

``--limit`` で分割実行でき、``en`` が既にある記事はスキップするため冪等に再実行できる。
LLM（翻訳）と画像生成 API のコストが記事数ぶん発生する点に注意。
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from batch.article_writer import build_translation, render_article
from batch.config import load_config
from batch.header_image import HeaderContext, HeaderImageGenerator
from batch.models import ArticleFrontmatter, SummaryResult
from batch.translator import SummaryTranslator


def _split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        raise ValueError("フロントマターが見つかりません。")
    end = text.index("\n---", 3)
    raw = text[3:end].strip()
    body = text[end + len("\n---") :]
    return yaml.safe_load(raw), body


def _summary_from_frontmatter(fm: ArticleFrontmatter) -> SummaryResult:
    return SummaryResult(
        articleTitle=fm.articleTitle or fm.title,
        bulletPoints=fm.bulletPoints,
        sections=fm.sections,
        keyPhrases=fm.keyPhrases or [fm.channel],
        editorial=fm.editorial,
    )


def _english_header_context(fm: ArticleFrontmatter, translation: SummaryResult) -> HeaderContext:
    return HeaderContext(
        title=fm.title,
        article_title=translation.articleTitle,
        channel=fm.channel,
        category_label=fm.matchedKeywords[0] if fm.matchedKeywords else "",
        key_phrases=translation.keyPhrases,
        bullet_points=[item.text for item in translation.bulletPoints],
        section_headings=[section.heading for section in translation.sections],
    )


def backfill_article(
    article_path: Path,
    *,
    images_root: Path,
    translator: SummaryTranslator,
    header_generator: HeaderImageGenerator,
    thumbnail_direction: str,
    dry_run: bool,
) -> bool:
    """1 記事をバックフィルする。翻訳済み（``en`` あり）なら False を返す。"""
    text = article_path.read_text(encoding="utf-8")
    data, _ = _split_frontmatter(text)
    if data.get("en"):
        return False

    fm = ArticleFrontmatter.model_validate(data)
    video_id = fm.videoId
    image_dir = images_root / video_id
    en_image = f"/images/{video_id}/header.png"
    ja_image = f"/images/{video_id}/header.ja.png"

    translation = translator.translate(_summary_from_frontmatter(fm), dry_run=dry_run)

    # 既存の日本語 header.png を header.ja.png へ退避してから英語版で上書きする。
    en_path = image_dir / "header.png"
    ja_path = image_dir / "header.ja.png"
    if not ja_path.exists():
        if en_path.exists():
            ja_path.write_bytes(en_path.read_bytes())
        elif dry_run:
            ja_path.parent.mkdir(parents=True, exist_ok=True)
            ja_path.write_bytes(b"placeholder")

    thumbnail = image_dir / "thumbnail.webp"
    source_image = thumbnail if thumbnail.exists() else en_path
    try:
        header_generator.generate(
            source_image,
            en_path,
            fm.title,
            dry_run=dry_run,
            direction=thumbnail_direction,
            context=_english_header_context(fm, translation),
            language="en",
        )
    except Exception as error:  # noqa: BLE001 - 失敗時は日本語画像を流用
        print(f"  英語ヘッダー生成に失敗、日本語画像を流用します: {video_id} / {error}")
        if ja_path.exists():
            en_path.write_bytes(ja_path.read_bytes())

    # トップレベル（日本語）画像を header.ja.png に向け直し、en ブロックを追記する。
    fm.headerImage = ja_image
    fm.heroImage = ja_image
    fm.en = build_translation(translation, en_image, en_image)

    article_path.write_text(render_article(fm), encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="既存記事に英語ブロックと英語ヘッダー画像を後付けします。")
    parser.add_argument("--limit", type=int, default=None, help="処理する記事本数の上限。")
    parser.add_argument("--dry-run", action="store_true", help="API を呼ばずプレースホルダで動作確認します。")
    parser.add_argument("--config", default="batch/config.yaml", help="設定ファイルのパス。")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    settings = load_config(root / args.config)
    articles_dir = root / settings.pipeline.output_articles_dir
    images_root = root / settings.pipeline.output_images_dir

    translator = SummaryTranslator(os.getenv("ANTHROPIC_API_KEY"))
    header_generator = HeaderImageGenerator(os.getenv("OPENAI_API_KEY"), settings.prompts.header_style)
    thumbnail_direction = settings.prompts.thumbnail_directions[0]

    article_paths = sorted(p for p in articles_dir.glob("*.md"))
    processed = 0
    skipped = 0
    for article_path in article_paths:
        if args.limit is not None and processed >= args.limit:
            break
        try:
            changed = backfill_article(
                article_path,
                images_root=images_root,
                translator=translator,
                header_generator=header_generator,
                thumbnail_direction=thumbnail_direction,
                dry_run=args.dry_run,
            )
        except Exception as error:  # noqa: BLE001 - 1 記事の失敗で全体を止めない
            print(f"スキップ（エラー）: {article_path.name} / {error}")
            continue
        if changed:
            processed += 1
            print(f"英語化しました: {article_path.relative_to(root)}")
        else:
            skipped += 1

    print(f"完了: 英語化={processed}, 既存スキップ={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
