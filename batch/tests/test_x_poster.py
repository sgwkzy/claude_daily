from __future__ import annotations

from batch.x_poster import UTM_SUFFIX, PostPayload, XPoster, build_tweet_text


def test_build_tweet_text_basic() -> None:
    payload = PostPayload(
        article_title="Claude Fable 5の安全設計と長文処理を読み解くAnthropic公式発表まとめ",
        slug="claude-fable-5-y9wz2pv404e",
        key_phrases=["Claude Fable 5", "安全設計", "長文処理"],
        video_id="Y9Wz2PV404E",
    )
    text = build_tweet_text(payload)
    # ヘッダーなし運用: 冒頭はタイトルから始まる
    assert not text.startswith("本日のClaude Daily更新")
    assert payload.article_title in text
    # 日本語スラッグではなく ASCII の videoId ベース URL を使う
    assert f"https://www.claude-daily.com/articles/y9wz2pv404e/{UTM_SUFFIX}" in text
    # GA4 で social 流入として分類させる UTM が付与されている
    assert "utm_source=x" in text
    assert "#Claude" in text and "#Anthropic" in text


def test_build_tweet_text_truncates_long_title() -> None:
    long_title = "あ" * 300
    payload = PostPayload(article_title=long_title, slug="abc", key_phrases=[])
    text = build_tweet_text(payload)
    # t.co 短縮を 23 字として概算した実効長で 280 以内（UTM 込みの URL 全体が短縮される）
    effective = len(text) - len(f"https://www.claude-daily.com/articles/abc/{UTM_SUFFIX}") + 23
    assert effective <= 280
    assert "…" in text


def test_xposter_disabled_without_credentials() -> None:
    poster = XPoster(api_key=None, api_secret=None, access_token=None, access_token_secret=None)
    assert poster.enabled is False
    assert poster.post(PostPayload(article_title="t", slug="s", key_phrases=[])) is False
