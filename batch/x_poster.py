from __future__ import annotations

import logging
import os
import random
import time
from dataclasses import dataclass

logger = logging.getLogger(__name__)

SITE_URL = "https://www.claude-daily.com"
BASE_TAGS = ["Claude", "Anthropic"]
TWEET_MAX = 280
URL_LENGTH = 23  # t.co 自動短縮の固定長
# 投稿本文の冒頭ヘッダー文言。空文字ならヘッダー行を出さない（現行運用）。
# 自動投稿を再有効化する際に文言を入れたい場合はここだけ変更する。
TWEET_HEADER = ""


@dataclass
class PostPayload:
    article_title: str
    slug: str
    key_phrases: list[str]


class XPoster:
    """X (Twitter) 投稿クライアント。資格情報が無い場合は no-op。"""

    def __init__(
        self,
        api_key: str | None,
        api_secret: str | None,
        access_token: str | None,
        access_token_secret: str | None,
    ) -> None:
        self._credentials_present = bool(api_key and api_secret and access_token and access_token_secret)
        self._api_key = api_key
        self._api_secret = api_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._client = None

    @classmethod
    def from_env(cls) -> "XPoster":
        return cls(
            api_key=os.getenv("X_API_KEY"),
            api_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
        )

    @property
    def enabled(self) -> bool:
        return self._credentials_present

    def _get_client(self):
        if self._client is None:
            import tweepy

            self._client = tweepy.Client(
                consumer_key=self._api_key,
                consumer_secret=self._api_secret,
                access_token=self._access_token,
                access_token_secret=self._access_token_secret,
            )
        return self._client

    def post(self, payload: PostPayload) -> bool:
        if not self._credentials_present:
            logger.warning("X 投稿スキップ: 認証情報が未設定 slug=%s", payload.slug)
            return False
        text = build_tweet_text(payload)
        try:
            client = self._get_client()
            response = client.create_tweet(text=text)
            tweet_id = getattr(getattr(response, "data", None), "get", lambda _k: None)("id") if response else None
            logger.info("X 投稿成功: slug=%s tweet_id=%s", payload.slug, tweet_id)
            return True
        except Exception as error:
            logger.exception("X 投稿失敗 (バッチ自体は継続): slug=%s error=%s", payload.slug, error)
            return False


def build_tweet_text(payload: PostPayload) -> str:
    """280字に収まるツイート本文を組み立てる。

    ``TWEET_HEADER`` が空のときは冒頭ヘッダー行を出さず、
    記事タイトル + ハッシュタグ + 記事URL の構成にする。
    """
    url = f"{SITE_URL}/articles/{payload.slug}/"
    hashtags = _build_hashtags(payload.key_phrases)

    # URL は t.co 短縮で 23 字固定として計算する。各ブロック間は空行 1 行を挟む。
    fixed_overhead = URL_LENGTH
    if TWEET_HEADER:
        fixed_overhead += len(TWEET_HEADER) + 2  # ヘッダー行 + 空行
    if hashtags:
        fixed_overhead += len(hashtags) + 2  # ハッシュタグ行 + 空行
    fixed_overhead += 2  # タイトル行と次ブロックの間の空行
    title_budget = TWEET_MAX - fixed_overhead
    title = payload.article_title
    if len(title) > title_budget:
        title = title[: max(title_budget - 1, 0)] + "…"

    parts: list[str] = []
    if TWEET_HEADER:
        parts.extend([TWEET_HEADER, ""])
    parts.extend([title, ""])
    if hashtags:
        parts.extend([hashtags, ""])
    parts.append(url)
    return "\n".join(parts)


def _build_hashtags(key_phrases: list[str]) -> str:
    tags = list(BASE_TAGS)
    for phrase in key_phrases:
        candidate = _to_hashtag(phrase)
        if candidate and candidate not in tags and len(tags) < 4:
            tags.append(candidate)
    return " ".join(f"#{tag}" for tag in tags)


def _to_hashtag(phrase: str) -> str | None:
    # 空白・記号を除いてハッシュタグ化。長すぎる句は除外。
    stripped = "".join(ch for ch in phrase if ch.isalnum())
    if not stripped or len(stripped) > 20:
        return None
    return stripped


def post_articles_with_delay(
    poster: XPoster,
    payloads: list[PostPayload],
    min_delay_sec: int = 3000,
    max_delay_sec: int = 4200,
) -> int:
    """新規作成記事を順次投稿する。投稿間に 50〜70 分のランダム待機を挟む。"""
    if not payloads:
        return 0
    if not poster.enabled:
        logger.warning("X 投稿スキップ: 認証情報が未設定のため %d 件すべて見送り", len(payloads))
        return 0
    success = 0
    for index, payload in enumerate(payloads):
        if index > 0:
            delay = random.randint(min_delay_sec, max_delay_sec)
            logger.info("X 投稿の次の間隔を待機: %d 秒", delay)
            time.sleep(delay)
        if poster.post(payload):
            success += 1
    return success
