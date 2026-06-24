"""日本語の要約（``SummaryResult``）を英語へ翻訳するステップ。

サイトを英語デフォルト＋日本語 `/jp/` の完全バイリンガルにするため、記事フロント
マターへ英語の表示テキストを追加する。要約と同じく JSON-only 方式で 1 回の LLM
呼び出しに収め、``time`` と ``image`` は言語非依存なので原文の値をそのまま流用する。
"""
from __future__ import annotations

from .models import ArticleSection, BulletPoint, SummaryResult


class SummaryTranslator:
    def __init__(self, api_key: str | None, model: str = "claude-sonnet-4-6") -> None:
        self.api_key = api_key
        self.model = model

    def translate(self, summary: SummaryResult, dry_run: bool = False) -> SummaryResult:
        """日本語の ``SummaryResult`` を英語の ``SummaryResult`` へ翻訳する。

        ``bulletPoints`` / ``sections`` の ``time`` と ``image`` は保持し、テキスト
        （``articleTitle`` / ``text`` / ``heading`` / ``body`` / ``keyPhrases``）のみ翻訳する。
        """
        if dry_run:
            return _dummy_translation(summary)
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY が設定されていません。")
        from .llm import anthropic_client, parse_json_response

        client = anthropic_client(self.api_key)
        payload = summary.model_dump(mode="json")
        import json as _json

        response = client.messages.create(
            model=self.model,
            max_tokens=2000,
            temperature=0.2,
            system=(
                "You translate a structured Japanese tech article into natural, fluent English."
                " Output JSON only, with exactly the same shape as the input: "
                "{\"articleTitle\":\"...\","
                "\"bulletPoints\":[{\"time\":0,\"text\":\"...\"}],"
                "\"sections\":[{\"heading\":\"...\",\"time\":0,\"image\":null,\"body\":\"...\"}],"
                "\"keyPhrases\":[\"...\"],"
                "\"editorial\":\"...\"}."
                " Translate `editorial` as well; keep it as an editorial commentary, not a summary."
                " Preserve every numeric `time` value and every `image` value exactly as given."
                " Keep the same number and order of bulletPoints and sections."
                " Preserve product and proper names (Claude, Claude Code, Anthropic, MCP, etc.)."
                " Write idiomatic English aimed at a US developer audience; keep technical nuance."
                " Do not exaggerate. No exclamation marks. No emoji."
            ),
            messages=[
                {
                    "role": "user",
                    "content": "Translate this article JSON to English:\n" + _json.dumps(payload, ensure_ascii=False),
                }
            ],
        )
        text = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")
        translated = SummaryResult.model_validate(parse_json_response(text))
        return _restore_invariants(summary, translated)


def _restore_invariants(source: SummaryResult, translated: SummaryResult) -> SummaryResult:
    """LLM が ``time`` / ``image`` を取りこぼしても原文の値で復元する。

    要素数がずれた場合は原文の構造を優先し、テキストだけ翻訳結果で上書きする。
    """
    bullet_points = [
        BulletPoint(time=src.time, text=dst.text if dst.text else src.text)
        for src, dst in zip(source.bulletPoints, translated.bulletPoints)
    ]
    sections = [
        ArticleSection(
            heading=dst.heading if dst.heading else src.heading,
            time=src.time,
            image=src.image,
            body=dst.body if dst.body else src.body,
        )
        for src, dst in zip(source.sections, translated.sections)
    ]
    key_phrases = translated.keyPhrases or source.keyPhrases
    return SummaryResult(
        articleTitle=translated.articleTitle or source.articleTitle,
        bulletPoints=bullet_points,
        sections=sections,
        keyPhrases=key_phrases,
        editorial=translated.editorial or source.editorial,
    )


def _dummy_translation(summary: SummaryResult) -> SummaryResult:
    """dry-run 用。LLM を呼ばずに英語っぽいダミーへ機械的に変換する。"""
    bullet_points = [
        BulletPoint(time=point.time, text=f"[EN] {point.text}") for point in summary.bulletPoints
    ]
    sections = [
        ArticleSection(
            heading=f"[EN] {section.heading}",
            time=section.time,
            image=section.image,
            body=f"[EN] {section.body}",
        )
        for section in summary.sections
    ]
    return SummaryResult(
        articleTitle=f"[EN] {summary.articleTitle}",
        bulletPoints=bullet_points,
        sections=sections,
        keyPhrases=[f"{phrase}" for phrase in summary.keyPhrases],
        editorial=f"[EN] {summary.editorial}" if summary.editorial else None,
    )
