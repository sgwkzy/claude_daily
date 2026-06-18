from __future__ import annotations

from batch.x_poster import PostPayload, XPoster, build_tweet_text


def test_build_tweet_text_basic() -> None:
    payload = PostPayload(
        article_title="Claude Fable 5の安全設計と長文処理を読み解くAnthropic公式発表まとめ",
        slug="y9wz2pv404e",
        key_phrases=["Claude Fable 5", "安全設計", "長文処理"],
    )
    text = build_tweet_text(payload)
    # ヘッダーなし運用: 冒頭はタイトルから始まる
    assert not text.startswith("本日のClaude Daily更新")
    assert payload.article_title in text
    assert "https://www.claude-daily.com/articles/y9wz2pv404e/" in text
    assert "#Claude" in text and "#Anthropic" in text


def test_build_tweet_text_truncates_long_title() -> None:
    long_title = "あ" * 300
    payload = PostPayload(article_title=long_title, slug="abc", key_phrases=[])
    text = build_tweet_text(payload)
    # t.co 短縮を 23 字として概算した実効長で 280 以内
    effective = len(text) - len("https://www.claude-daily.com/articles/abc/") + 23
    assert effective <= 280
    assert "…" in text


def test_xposter_disabled_without_credentials() -> None:
    poster = XPoster(api_key=None, api_secret=None, access_token=None, access_token_secret=None)
    assert poster.enabled is False
    assert poster.post(PostPayload(article_title="t", slug="s", key_phrases=[])) is False
