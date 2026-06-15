from __future__ import annotations

import json


class TrendProposer:
    def __init__(self, api_key: str | None, model: str = "claude-sonnet-4-6") -> None:
        self.api_key = api_key
        self.model = model

    def propose(self, fixed_keywords: list[str], limit: int, dry_run: bool = False) -> list[str]:
        if dry_run:
            return ["AI agents", "developer tools", "breaking tech news"][:limit]
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY が設定されていません。")
        from .llm import anthropic_client

        client = anthropic_client(self.api_key)
        response = client.messages.create(
            model=self.model,
            max_tokens=300,
            temperature=0.2,
            system="あなたはYouTubeトレンド候補をJSONだけで返すアシスタントです。",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "既存キーワードと重複しにくい最近の話題を提案してください。"
                        f" 返却形式は {{\"keywords\":[\"...\"]}} のみ。既存: {', '.join(fixed_keywords)}"
                    ),
                }
            ],
        )
        text = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")
        payload = json.loads(text)
        keywords = payload.get("keywords", [])
        return [str(keyword) for keyword in keywords][:limit]
