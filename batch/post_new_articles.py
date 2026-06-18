"""push で追加された記事を X に投稿するドライバ。GitHub Actions の post-x.yml から呼ぶ。"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from batch.x_poster import PostPayload, XPoster, post_articles_with_delay

logger = logging.getLogger(__name__)


def main(paths: list[str]) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    payloads: list[PostPayload] = []
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            logger.warning("ファイルが見つからないためスキップ: %s", path)
            continue
        frontmatter = _read_frontmatter(path)
        article_title = frontmatter.get("articleTitle") or frontmatter.get("title")
        slug = frontmatter.get("slug") or frontmatter.get("videoId")
        video_id = frontmatter.get("videoId")
        key_phrases = frontmatter.get("keyPhrases") or []
        if not article_title or not video_id or not slug:
            logger.warning("articleTitle/videoId/slug が無いためスキップ: %s", path)
            continue
        payloads.append(
            PostPayload(
                article_title=str(article_title),
                slug=str(slug).lower(),
                key_phrases=list(key_phrases),
                video_id=str(video_id),
            )
        )

    if not payloads:
        logger.info("投稿対象がないため終了")
        return 0

    poster = XPoster.from_env()
    if not poster.enabled:
        logger.warning("X 認証情報が未設定のため投稿スキップ")
        return 0

    posted = post_articles_with_delay(poster, payloads)
    logger.info("X 投稿結果: 成功 %d/%d 件", posted, len(payloads))
    return 0


def _read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    _, _, rest = text.partition("---\n")
    body, _, _ = rest.partition("\n---")
    return yaml.safe_load(body) or {}


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
