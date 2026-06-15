from __future__ import annotations

import json

from .models import SummaryResult, TranscriptSegment


class TranscriptSummarizer:
    def __init__(self, api_key: str | None, model: str = "claude-sonnet-4-6") -> None:
        self.api_key = api_key
        self.model = model

    def summarize(self, title: str, segments: list[TranscriptSegment], dry_run: bool = False) -> SummaryResult:
        if dry_run:
            return _dummy_summary(segments)
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY が設定されていません。")
        from .llm import anthropic_client

        client = anthropic_client(self.api_key)
        transcript_text = "\n".join(f"[{segment.start}] {segment.text}" for segment in segments)
        response = client.messages.create(
            model=self.model,
            max_tokens=1600,
            temperature=0.2,
            system=(
                "あなたはYouTube字幕を日本語の構造化記事に要約するアシスタントです。"
                " 出力はJSONのみ。形式は "
                "{\"articleTitle\":\"...\","
                "\"bulletPoints\":[{\"time\":0,\"text\":\"...\"}],"
                "\"sections\":[{\"heading\":\"...\",\"time\":0,\"body\":\"...\"}],"
                "\"keyPhrases\":[\"...\"]}。"
                " articleTitleは必須。日本語の記事見出しで30〜50字程度。検索意図に沿った具体的な内容を含め、"
                "元動画タイトルの直訳・直写しは禁止。煽り表現は禁止。感嘆符は禁止。絵文字は禁止。"
                " bulletPointsは5〜8件、sectionsは3〜5件、timeは入力に存在する秒数を使うこと。"
            ),
            messages=[
                {
                    "role": "user",
                    "content": f"タイトル: {title}\n字幕:\n{transcript_text}",
                }
            ],
        )
        text = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")
        return SummaryResult.model_validate(json.loads(text))


def _dummy_summary(segments: list[TranscriptSegment]) -> SummaryResult:
    bullet_points = [
        {"time": 0, "text": "Claude Codeは「コードを書くLLM」ではなく「コードベースを操作するエージェント」として設計されている。"},
        {"time": 72, "text": "CLIから読み取り・編集・テスト実行・コミットまで一気通貫で進められる。"},
        {"time": 210, "text": "AGENTS.md / CLAUDE.md に前提知識を書いておくと出力品質が大きく変わる。"},
        {"time": 360, "text": "MCPで社内ツール（Slack / Notion / DB）を接続すると、調査と実装が同じ場所で完結する。"},
        {"time": 510, "text": "プラン承認モードと自動承認モードを場面で切り替えることで安全性とスピードを両立できる。"},
    ]
    sections = [
        {
            "heading": "Claude Codeをなぜ使うのか",
            "time": 0,
            "body": (
                "Claude Codeは単にコードを生成するアシスタントではなく、ターミナルからファイルを読み・書き換え・コマンドを実行する「コードベース操作エージェント」として設計されています。\n\n"
                "そのため、設計判断や調査からテスト実行、Git操作までを一連の流れとして任せられ、開発者は「何を作るか」に集中できるようになります。動画の冒頭ではこの設計思想と、従来のチャット型AIとの違いが整理されています。"
            ),
        },
        {
            "heading": "実装フロー：プロンプトの前にコンテキスト",
            "time": 72,
            "body": (
                "高品質な出力を得るための鍵は、毎回プロンプトを工夫することではなく、リポジトリ直下に置く AGENTS.md / CLAUDE.md に前提を書いておくことだと紹介されます。\n\n"
                "「使っているフレームワーク」「テストの走らせ方」「コミット規約」など、毎回説明したくない情報を集約しておくと、以降のセッションは短い指示だけで成立するようになります。"
            ),
        },
        {
            "heading": "MCPで社内ツールを接続する",
            "time": 360,
            "body": (
                "MCP（Model Context Protocol）を経由すると、Slackの会話履歴・Notionの仕様書・社内DBのスキーマなどに Claude から直接アクセスできます。\n\n"
                "「ドキュメントを開いてコピペしてプロンプトに貼る」というワークフローが不要になり、調査から実装まで同じセッションの中で完結する点が、エンジニアの体験を大きく変えると説明されています。"
            ),
        },
        {
            "heading": "運用：承認モードを使い分ける",
            "time": 510,
            "body": (
                "本番リポジトリで安心して使い続けるために、プラン承認モード（実行前に必ず確認）と自動承認モード（差分のみ事後確認）を場面で切り替えることが推奨されています。\n\n"
                "リファクタや実験的なタスクは自動承認で素早く回し、本番影響のある変更はプラン承認で慎重に進める、という運用例が紹介されました。"
            ),
        },
    ]
    return SummaryResult.model_validate(
        {
            "articleTitle": "Claude Codeをコードベース操作エージェントとして使いこなす実装フローとMCP連携",
            "bulletPoints": bullet_points,
            "sections": sections,
            "keyPhrases": ["Claude Code", "MCP", "AIエージェント", "開発フロー", "コンテキスト設計"],
        }
    )
