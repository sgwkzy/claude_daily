---
videoId: UMjeSU6C4qU
title: How I built an $80K/Mo mobile app with Claude Code (Full Vibe Code Tutorial)
slug: 月8万ドルの領収書トラッカーアプリをclaude-codeで構築ノーコードで実装する手順を公開-umjesu6c4qu
articleTitle: 月8万ドルの領収書トラッカーアプリをClaude Codeで構築：ノーコードで実装する手順を公開
seoTitle: 月8万ドルの領収書トラッカーアプリをClaude Codeで構築：ノーコードで実装する手順を公開
summary: App Store上の『領収書・経費管理』という小さなニッチ市場で、月4万〜8万ドルを売り上げるアプリが複数存在することを紹介する。
channel: Jason Lee
channelId: UCSm7riYU-NTWWFlG9XJBcRA
publishedAt: '2026-07-09T17:00:14Z'
fetchedAt: '2026-07-11T09:00:00.000000Z'
originalThumbnail: https://i.ytimg.com/vi/UMjeSU6C4qU/maxresdefault.jpg
headerImage: /images/UMjeSU6C4qU/header.ja.png
heroImage: /images/UMjeSU6C4qU/header.ja.png
viewCount: 31133
durationSec: 1565
sourceLanguage: en-US
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Claude Code
- Claude API
- Supabase
- MCP
- ノーコード開発
- 個人開発
bulletPoints:
- time: 0
  text: App Store上の『領収書・経費管理』という小さなニッチ市場で、月4万〜8万ドルを売り上げるアプリが複数存在することを紹介する。
- time: 33
  text: 動画では、この領収書トラッカーアプリをClaude Codeでゼロから構築し、アニメーションを加えたプレミアム版として一切コードを書かずに実装する手順を解説する。
- time: 745
  text: 構築にはClaudeのAPIを使い、レシート画像をスキャンしてデータ化する。API利用はサブスクリプションとは別料金で、事前にクレジットを購入する必要がある。
- time: 786
  text: APIキーをClaudeに渡す際は、チャットに直接貼り付けるとチャット履歴の漏洩時に流出するリスクがあるため、.envファイルに保存するよう注意喚起している。
- time: 799
  text: データベースにはSupabaseを採用し、MCPコネクタ経由でClaude Codeと接続する。
- time: 1503
  text: 実際にSupabaseのテーブルエディタを開き、Claude Codeが作成したレシート・カテゴリ・ユーザー情報のテーブル構造を確認できる。
sections:
- heading: 月8万ドルの『地味だが儲かる』ニッチアプリ
  time: 0
  body: 動画はApp Store内の会計カテゴリの小さなサブニッチである『領収書・経費トラッカー』に着目する。SimplyWiseなど、月6万〜8万ドルを売り上げるアプリが複数存在し、いずれも『物理的な領収書をスキャンする』という単一機能に特化している点を指摘。小さなカテゴリでも収益性の高いアプリが存在しうる好例として紹介した。
- heading: Claude APIとSupabaseで組み立てる実装手順
  time: 745
  body: '構築にあたっては、レシート画像をAIで解析するためにClaudeのAPIを使用する(OpenAIのAPIの方が安価だが、既にクレジットがあるためClaudeを選択したと説明)。API利用は月額サブスクリプションとは別課金のため、事前にクレジットを購入し、APIキーは漏洩防止のため.envファイルに保存するよう注意を促している。


    データベースにはSupabaseを採用し、領収書・カテゴリ・ユーザー情報などをMCPコネクタ経由でClaude Codeと接続。QuickBooksなど会計ソフトとの連携も視野に入れた設計とした。'
- heading: Supabase側でデータ構造を確認する
  time: 1503
  body: Supabaseの管理画面からテーブルエディタを開くと、Claude Codeが自動生成したreceiptsテーブルの中身(合計金額、内訳、クレジットカード情報、カテゴリなど)を直接確認できる。ユーザーごとに固有のデータとして保存される設計になっており、認証機能を追加すれば複数ユーザー対応のSaaSとしてもそのまま展開可能な構成になっている。
editorial: この動画が実践しているのは、Claude CodeとAPI、Supabase、MCPコネクタを組み合わせた『個人開発者向けフルスタック構築』の典型的なパターンだ。領収書スキャンという地味な機能に特化したニッチアプリが月数万ドル規模の収益を上げている事実は、AIによる実装コストの低下が、これまで参入障壁の高かった細分化市場を個人開発者にも開放しつつあることを示している。一方でAPIキーの.env管理を明示的に注意喚起している点は、AI駆動開発が広がるほどセキュリティ意識の基本を丁寧に伝える必要性が増している証左でもある。
en:
  articleTitle: 'Building an $80K/Month Receipt-Tracker App With Claude Code: A No-Code
    Build Walkthrough'
  seoTitle: 'Building an $80K/Month Receipt-Tracker App With Claude Code: A N'
  summary: The video highlights a tiny niche in the App Store's accounting category
    -- receipt and expense tracking -- where…
  keyPhrases:
  - Claude Code
  - Claude API
  - Supabase
  - MCP
  - no-code development
  - solo development
  bulletPoints:
  - time: 0
    text: The video highlights a tiny niche in the App Store's accounting category
      -- receipt and expense tracking -- where several apps pull in $40,000-$80,000
      a month.
  - time: 33
    text: It walks through building a receipt-tracker app from scratch with Claude
      Code, adding premium touches like animations, entirely without writing a single
      line of code.
  - time: 745
    text: The build uses Claude's API to scan and parse receipt images -- a separate,
      credit-based charge from a regular Claude subscription.
  - time: 786
    text: The creator warns never to paste an API key directly into chat, since a
      leaked chat history would expose it -- it should be stored in a .env file instead.
  - time: 799
    text: Supabase is used as the database, connected to Claude Code via an MCP connector.
  - time: 1503
    text: Opening Supabase's table editor shows the receipts, categories, and user-information
      tables that Claude Code generated automatically.
  sections:
  - heading: An $80K/Month 'Boring but Profitable' Niche App
    time: 0
    body: 'The video zeroes in on a small sub-niche inside the App Store''s accounting
      category: receipt and expense tracking. Apps like SimplyWise pull in $60,000-$80,000
      a month doing essentially one thing -- scanning physical receipts -- making
      the case that even the smallest categories can hide genuinely profitable, narrowly-focused
      apps.'
  - heading: Building It With Claude's API and Supabase
    time: 745
    body: 'To parse receipt images with AI, the build uses Claude''s API (noting OpenAI''s
      API is cheaper, but he already had credits on hand). API usage is billed separately
      from a Claude subscription, so credits need to be purchased in advance, and
      the API key should be stored in a .env file rather than pasted into chat, where
      a leaked conversation could expose it.


      The database layer runs on Supabase, connected to Claude Code through an MCP
      connector, with receipts, categories, and user data all stored there -- and
      QuickBooks integration built in as a target for accounting software sync.'
  - heading: Checking the Data Structure Inside Supabase
    time: 1503
    body: Opening Supabase's table editor reveals the receipts table Claude Code generated
      automatically -- totals, line-item breakdowns, card info, and categories --
      scoped per user. Add authentication on top, and the same structure is ready
      to ship as a full multi-user SaaS product.
  editorial: This video is a textbook example of the 'full-stack solo build' pattern
    now emerging around Claude Code, an AI API, Supabase, and an MCP connector. That
    a narrowly-scoped niche app -- just receipt scanning -- can pull in tens of thousands
    of dollars a month shows how falling implementation costs from AI are opening
    up previously high-barrier, fragmented markets to individual developers. At the
    same time, the explicit warning about storing API keys in a .env file is a reminder
    that as AI-driven development spreads, basic security hygiene needs to be taught
    just as deliberately.
  headerImage: /images/UMjeSU6C4qU/header.png
  heroImage: /images/UMjeSU6C4qU/header.png
---

## ハイライト

- [00:00] App Store上の『領収書・経費管理』という小さなニッチ市場で、月4万〜8万ドルを売り上げるアプリが複数存在することを紹介する。
- [00:33] 動画では、この領収書トラッカーアプリをClaude Codeでゼロから構築し、アニメーションを加えたプレミアム版として一切コードを書かずに実装する手順を解説する。
- [12:25] 構築にはClaudeのAPIを使い、レシート画像をスキャンしてデータ化する。API利用はサブスクリプションとは別料金で、事前にクレジットを購入する必要がある。
- [13:06] APIキーをClaudeに渡す際は、チャットに直接貼り付けるとチャット履歴の漏洩時に流出するリスクがあるため、.envファイルに保存するよう注意喚起している。
- [13:19] データベースにはSupabaseを採用し、MCPコネクタ経由でClaude Codeと接続する。
- [25:03] 実際にSupabaseのテーブルエディタを開き、Claude Codeが作成したレシート・カテゴリ・ユーザー情報のテーブル構造を確認できる。

## セクション

### 月8万ドルの『地味だが儲かる』ニッチアプリ

- 時刻: 00:00

動画はApp Store内の会計カテゴリの小さなサブニッチである『領収書・経費トラッカー』に着目する。SimplyWiseなど、月6万〜8万ドルを売り上げるアプリが複数存在し、いずれも『物理的な領収書をスキャンする』という単一機能に特化している点を指摘。小さなカテゴリでも収益性の高いアプリが存在しうる好例として紹介した。

### Claude APIとSupabaseで組み立てる実装手順

- 時刻: 12:25

構築にあたっては、レシート画像をAIで解析するためにClaudeのAPIを使用する(OpenAIのAPIの方が安価だが、既にクレジットがあるためClaudeを選択したと説明)。API利用は月額サブスクリプションとは別課金のため、事前にクレジットを購入し、APIキーは漏洩防止のため.envファイルに保存するよう注意を促している。

データベースにはSupabaseを採用し、領収書・カテゴリ・ユーザー情報などをMCPコネクタ経由でClaude Codeと接続。QuickBooksなど会計ソフトとの連携も視野に入れた設計とした。

### Supabase側でデータ構造を確認する

- 時刻: 25:03

Supabaseの管理画面からテーブルエディタを開くと、Claude Codeが自動生成したreceiptsテーブルの中身(合計金額、内訳、クレジットカード情報、カテゴリなど)を直接確認できる。ユーザーごとに固有のデータとして保存される設計になっており、認証機能を追加すれば複数ユーザー対応のSaaSとしてもそのまま展開可能な構成になっている。

## 編集部の視点

この動画が実践しているのは、Claude CodeとAPI、Supabase、MCPコネクタを組み合わせた『個人開発者向けフルスタック構築』の典型的なパターンだ。領収書スキャンという地味な機能に特化したニッチアプリが月数万ドル規模の収益を上げている事実は、AIによる実装コストの低下が、これまで参入障壁の高かった細分化市場を個人開発者にも開放しつつあることを示している。一方でAPIキーの.env管理を明示的に注意喚起している点は、AI駆動開発が広がるほどセキュリティ意識の基本を丁寧に伝える必要性が増している証左でもある。
