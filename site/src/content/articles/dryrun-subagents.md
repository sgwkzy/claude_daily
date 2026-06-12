---
videoId: dryrun-subagents
title: サブエージェントで仕事を分業する Claudeの使いこなし
channel: Anthropic JP Community
channelId: demo-channel-2
publishedAt: '2026-06-11T02:50:59.578188Z'
fetchedAt: '2026-06-12T02:51:01.978086Z'
originalThumbnail: https://example.com/thumb-subagents.webp
headerImage: /images/dryrun-subagents/header.webp
viewCount: 78000
durationSec: 421
sourceLanguage: ja
matchedKeywords:
- Claude
- AIエージェント
proposedByLLM: true
keyPhrases:
- Claude Code
- MCP
- AIエージェント
- 開発フロー
- コンテキスト設計
bulletPoints:
- time: 0
  text: Claude Codeは「コードを書くLLM」ではなく「コードベースを操作するエージェント」として設計されている。
- time: 72
  text: CLIから読み取り・編集・テスト実行・コミットまで一気通貫で進められる。
- time: 210
  text: AGENTS.md / CLAUDE.md に前提知識を書いておくと出力品質が大きく変わる。
- time: 360
  text: MCPで社内ツール（Slack / Notion / DB）を接続すると、調査と実装が同じ場所で完結する。
- time: 510
  text: プラン承認モードと自動承認モードを場面で切り替えることで安全性とスピードを両立できる。
sections:
- heading: Claude Codeをなぜ使うのか
  time: 0
  body: 'Claude Codeは単にコードを生成するアシスタントではなく、ターミナルからファイルを読み・書き換え・コマンドを実行する「コードベース操作エージェント」として設計されています。


    そのため、設計判断や調査からテスト実行、Git操作までを一連の流れとして任せられ、開発者は「何を作るか」に集中できるようになります。動画の冒頭ではこの設計思想と、従来のチャット型AIとの違いが整理されています。'
  image: /images/dryrun-subagents/scene-1.webp
- heading: 実装フロー：プロンプトの前にコンテキスト
  time: 72
  body: '高品質な出力を得るための鍵は、毎回プロンプトを工夫することではなく、リポジトリ直下に置く AGENTS.md / CLAUDE.md に前提を書いておくことだと紹介されます。


    「使っているフレームワーク」「テストの走らせ方」「コミット規約」など、毎回説明したくない情報を集約しておくと、以降のセッションは短い指示だけで成立するようになります。'
  image: /images/dryrun-subagents/scene-2.webp
- heading: MCPで社内ツールを接続する
  time: 360
  body: 'MCP（Model Context Protocol）を経由すると、Slackの会話履歴・Notionの仕様書・社内DBのスキーマなどに Claude
    から直接アクセスできます。


    「ドキュメントを開いてコピペしてプロンプトに貼る」というワークフローが不要になり、調査から実装まで同じセッションの中で完結する点が、エンジニアの体験を大きく変えると説明されています。'
  image: /images/dryrun-subagents/scene-3.webp
- heading: 運用：承認モードを使い分ける
  time: 510
  body: '本番リポジトリで安心して使い続けるために、プラン承認モード（実行前に必ず確認）と自動承認モード（差分のみ事後確認）を場面で切り替えることが推奨されています。


    リファクタや実験的なタスクは自動承認で素早く回し、本番影響のある変更はプラン承認で慎重に進める、という運用例が紹介されました。'
  image: /images/dryrun-subagents/scene-4.webp
---

## ハイライト

- [00:00] Claude Codeは「コードを書くLLM」ではなく「コードベースを操作するエージェント」として設計されている。
- [01:12] CLIから読み取り・編集・テスト実行・コミットまで一気通貫で進められる。
- [03:30] AGENTS.md / CLAUDE.md に前提知識を書いておくと出力品質が大きく変わる。
- [06:00] MCPで社内ツール（Slack / Notion / DB）を接続すると、調査と実装が同じ場所で完結する。
- [08:30] プラン承認モードと自動承認モードを場面で切り替えることで安全性とスピードを両立できる。

## セクション

### Claude Codeをなぜ使うのか

- 時刻: 00:00
- 画像: /images/dryrun-subagents/scene-1.webp

Claude Codeは単にコードを生成するアシスタントではなく、ターミナルからファイルを読み・書き換え・コマンドを実行する「コードベース操作エージェント」として設計されています。

そのため、設計判断や調査からテスト実行、Git操作までを一連の流れとして任せられ、開発者は「何を作るか」に集中できるようになります。動画の冒頭ではこの設計思想と、従来のチャット型AIとの違いが整理されています。

### 実装フロー：プロンプトの前にコンテキスト

- 時刻: 01:12
- 画像: /images/dryrun-subagents/scene-2.webp

高品質な出力を得るための鍵は、毎回プロンプトを工夫することではなく、リポジトリ直下に置く AGENTS.md / CLAUDE.md に前提を書いておくことだと紹介されます。

「使っているフレームワーク」「テストの走らせ方」「コミット規約」など、毎回説明したくない情報を集約しておくと、以降のセッションは短い指示だけで成立するようになります。

### MCPで社内ツールを接続する

- 時刻: 06:00
- 画像: /images/dryrun-subagents/scene-3.webp

MCP（Model Context Protocol）を経由すると、Slackの会話履歴・Notionの仕様書・社内DBのスキーマなどに Claude から直接アクセスできます。

「ドキュメントを開いてコピペしてプロンプトに貼る」というワークフローが不要になり、調査から実装まで同じセッションの中で完結する点が、エンジニアの体験を大きく変えると説明されています。

### 運用：承認モードを使い分ける

- 時刻: 08:30
- 画像: /images/dryrun-subagents/scene-4.webp

本番リポジトリで安心して使い続けるために、プラン承認モード（実行前に必ず確認）と自動承認モード（差分のみ事後確認）を場面で切り替えることが推奨されています。

リファクタや実験的なタスクは自動承認で素早く回し、本番影響のある変更はプラン承認で慎重に進める、という運用例が紹介されました。
