---
videoId: cGuyrANVi4A
title: How Model Context Protocol (MCP) actually works
slug: google-cloudが解説するmcp-anthropic発のオープン標準がaiのhttpになる理由-cguyranvi4a
articleTitle: Google Cloudが解説するMCP — Anthropic発のオープン標準が『AIのHTTP』になる理由
seoTitle: Google Cloudが解説するMCP — Anthropic発のオープン標準が『AIのHTTP』になる理由
summary: AIモデルを社内ツールやデータに接続する作業は煩雑。APIごとに挙動が異なり、統合ごとにカスタムコード、モデルが変わると接続が壊れる。これを解消するために生まれたのが
  Model Context Protocol (MCP)。
channel: Google Cloud Tech
channelId: UCJS9pqu9BzkAMNTmzNMNhvg
publishedAt: '2026-06-24T16:00:39Z'
fetchedAt: '2026-06-25T03:19:10.836404Z'
originalThumbnail: https://i.ytimg.com/vi/cGuyrANVi4A/maxresdefault.jpg
headerImage: /images/cGuyrANVi4A/header.ja.png
heroImage: /images/cGuyrANVi4A/header.ja.png
viewCount: 6004
durationSec: 478
sourceLanguage: en-US
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Model Context Protocol (MCP)
- AI向けに設計されたAPI層
- tools / resources / prompts / context
- 動的ケイパビリティ発見
- MCP aware設計
- HTTP級のプロトコル普及
bulletPoints:
- time: 4
  text: AIモデルを社内ツールやデータに接続する作業は煩雑。APIごとに挙動が異なり、統合ごとにカスタムコード、モデルが変わると接続が壊れる。これを解消するために生まれたのが
    Model Context Protocol (MCP)。
- time: 51
  text: MCPはモデルとツール・データ・コンテキストを構造的につなぐオープン標準。モデルが利用可能なツールを発見し、情報を取得し、アクションを実行できる『共通言語』。
- time: 76
  text: Anthropicが提唱し、業界全体に採用が広がっている。AI開発で最大の課題『外部リソースを安全かつ確実にモデルに使わせる』を解決する。
- time: 93
  text: 従来APIはAI向けに設計されていない。プログラムが正確で決定論的なリクエストを送る前提だが、LLMは確率的に推論し、質問・確認・探索を経て決まる。
- time: 169
  text: 'アーキテクチャ: サーバーがDB・ファイルシステム・社内ツール・ドキュメント検索などのリソースを公開。クライアント接続時、サーバーは『何ができるか』のケイパビリティと必要入力を広告。'
- time: 231
  text: 'MCPの主要リソースは4種: tools (実行可能なアクション)、resources (データ・状態)、prompts (再利用テンプレート)、context
    (外部情報)。メタデータ付きで動的発見可能。'
- time: 360
  text: '実例: パーソナルアシスタントエージェント (カレンダー確認・議事録取得・フォローアップメール作成)。旧来はGoogle Calendar/Notion/Gmail各APIにグルーコードと脆いシステムプロンプトが必要だった。'
- time: 425
  text: MCPは『HTTPがWebを統一した』のと同じレベルでAIモデルとツールの対話を統一しつつある。今後の本格AI開発者は自社システムを MCP aware
    に作る必要がある。
sections:
- heading: なぜMCPが生まれたか — 従来APIがAIに合わない構造的理由
  time: 4
  body: 'Google Cloud Techが Anthropic 発の Model Context Protocol (MCP) を概説する公式動画。冒頭の問題提起は明快だ。AIモデルを自社のツールやデータと連携させようとすると、API挙動がバラバラ、統合ごとにカスタムコード、モデル更新で接続が壊れる。AI
    開発者の長年の頭痛の種だった。


    根本原因はAPIの設計思想にある。従来APIは『すでに自分が何を欲しいか分かっているプログラム』向けに設計され、正確で決定論的なリクエストを前提とする。一方LLMは確率的に出力し、不確実な入力で推論し、結論を出す前に質問・確認・探索を必要とする。マッチしないインターフェース同士を強引につなぐ役割を、これまでは脆いシステムプロンプトと開発者の苦労が引き受けていた。MCPはここに『AI
    に合わせたインターフェース層』を入れる試みだ。'
- heading: MCPアーキテクチャ — クライアント・サーバーと4種のリソース
  time: 169
  body: 'MCPアーキテクチャはシンプルなクライアント/サーバー構造を取る。サーバー側はDB、ファイルシステム、社内ツール、ドキュメント検索エンジンといったリソースを公開する。クライアント
    (Claude などモデル側) が接続すると、サーバーはデータを返すのではなく『自分には何ができ、どんな入力が必要か』というケイパビリティを広告する。


    この設計の効果が大きい。モデルは事前に全APIエンドポイントを知っている必要がなく、接続時に動的に発見できる。やり取りはシンプルで定義の明確なスキーマに従う。クライアントは『利用可能なリソース一覧』『このアクション実行』『このデータ取得』といったリクエストを送り、サーバーは構造化JSONで何が可能か・何が起こったかを返す。技術的には4種のリソースが基本要素になる:
    tools (実行可能なアクション)、resources (データ・状態)、prompts (再利用テンプレート)、context (外部情報)。各要素はメタデータ付きで、何ができ、何を入力に取り、何を返すかが明示される。'
- heading: 実例とHTTP級の普及 — なぜ今学ぶべきか
  time: 360
  body: '実例で見るとMCPの恩恵が際立つ。カレンダー確認・議事録取得・フォローアップメール作成を担うパーソナルアシスタントエージェントを作るとする。旧世界では
    Google Calendar、Notion、Gmail それぞれのAPIに個別コードを書き、認証・レート制限・各種エッジケースを処理し、さらに長く脆いシステムプロンプトでモデルに使い方を教える必要があった。


    MCPでは各システム向けにサーバーをビルドかインストールするだけだ。カレンダーサーバー、ノートサーバー、メールサーバー。各サーバーは『list events』『get
    meeting summary』『send email』のような利用可能ツールを広告し、モデルは自動でそれらを認識する。どれを、どの順で、どんなデータを渡して使うか、をモデル自身が推論する。グルーコードを毎回書く必要がない。動画は『HTTPがWebを統一した』のと同じ意味でMCPがAIモデルとツールの対話を統一しつつある、と締める。本格的なAI開発者は自社システムを
    MCP aware に設計する必要が出てくるだろう、というのが Google Cloud からの提言だ。'
editorial: Anthropic 発の MCP を Google Cloud が公式チャンネルで解説した、という事実そのものが業界の力学を端的に表している。OpenAI
  系と Anthropic 系のフロンティアモデル競争が続く一方で、接続層は標準化が進み、ハイパースケーラーが採用を後押しする側に回った。読者にとっての含意は二段ある。短期的にはエージェント実装の自由度が増える。MCP
  サーバーを 1 つ立てれば、Claude / Codex / Gemini に同じツールを使わせられる前提が現実になりつつある。長期的には『どの SaaS が
  MCP サーバーを最初に提供したか』が業務 AI 経済圏での順位を決める。Notion、Gmail、CRM、社内ツールが MCP コネクタを揃えれば、社内エージェントは自社向けに最適化された汎用基盤を持てる。AI
  のフロンティアモデルが何になるかを当てるより、自社の業務基盤を MCP aware にする方が事業上の意思決定として確実な投資になる。
en:
  articleTitle: Google Cloud Explains MCP — Why Anthropic's Open Standard Is Becoming
    the 'HTTP of AI'
  seoTitle: Google Cloud Explains MCP — Why Anthropic's Open Standard Is Bec
  summary: Connecting an AI model to your tools and data has always been messy. Every
    API behaves differently, every integration…
  keyPhrases:
  - Model Context Protocol (MCP)
  - API layer designed for AI
  - tools / resources / prompts / context
  - Dynamic capability discovery
  - MCP-aware system design
  - HTTP-level standardisation
  bulletPoints:
  - time: 4
    text: Connecting an AI model to your tools and data has always been messy. Every
      API behaves differently, every integration needs custom code, and every model
      change breaks the connection. Model Context Protocol (MCP) was created to fix
      exactly that.
  - time: 51
    text: MCP is an open standard for connecting models to tools, data, and context
      in a consistent, structured way — a shared language between models and the systems
      around them.
  - time: 76
    text: 'Introduced by Anthropic and now being adopted across the industry, MCP
      addresses one of AI development''s biggest pain points: making models use external
      resources safely and reliably.'
  - time: 93
    text: 'Why traditional APIs don''t fit: they were designed for programs that already
      know exactly what they want and form precise, deterministic requests. LLMs generate
      probabilistically and need to ask, clarify, and explore first.'
  - time: 169
    text: 'Architecture: the server exposes resources — a database, a file system,
      internal tools, a document search engine. On connection, the server advertises
      what it supports, what resources exist, what actions are possible, and what
      inputs are required.'
  - time: 231
    text: 'MCP defines four main resource types: tools (actions the model can invoke),
      resources (data and state), prompts (reusable templates), and context (external
      information for reasoning).'
  - time: 360
    text: 'Practical example: a personal assistant agent that checks your calendar,
      pulls meeting notes, and drafts follow-up emails. In the old world you''d integrate
      Google Calendar, Notion, and Gmail APIs with glue code and brittle system prompts.'
  - time: 425
    text: MCP is starting to unify how models talk to tools the way HTTP unified the
      web. Every serious AI developer will soon need to make their systems MCP-aware.
  sections:
  - heading: Why MCP exists — the structural mismatch between APIs and AI models
    time: 4
    body: 'Google Cloud Tech''s official explainer on Anthropic''s Model Context Protocol
      (MCP) opens with the lived pain. Wire an AI model to your tools and data and
      the mess hits immediately — every API behaves differently, every integration
      needs custom code, and any model change breaks the connection. Familiar territory
      for AI developers.


      The root cause sits in API design philosophy. APIs were built for programs that
      already know exactly what they want and can form precise, deterministic requests.
      LLMs work the other way — they generate probabilistically, reason over uncertain
      inputs, and often need to ask, clarify, or explore before they can decide. Forcing
      two mismatched interfaces to talk has historically been the developer''s burden,
      glued together with brittle system prompts. MCP introduces an interface layer
      designed for AI on the AI side.'
  - heading: MCP architecture — client / server and the four resource types
    time: 169
    body: 'MCP uses a clean client/server architecture. Servers expose resources —
      databases, file systems, internal tools, document search engines. When a client
      (like Claude) connects, the server doesn''t return data; it advertises capabilities.
      What can be done, what resources exist, what actions are available, what inputs
      are required.


      The payoff is substantial. The model doesn''t need to be pre-programmed with
      every API or endpoint — it discovers them at connection time. Communication
      runs on a simple, well-defined schema: the client sends requests like ''list
      resources,'' ''call this action,'' ''retrieve this data,'' and the server replies
      with structured JSON describing what''s possible and what happened. Four resource
      types form the basis: tools (invocable actions), resources (data and state),
      prompts (reusable templates), and context (external information). Each carries
      metadata describing what it does, what input it expects, and what output it
      returns.'
  - heading: A worked example, and HTTP-level adoption
    time: 360
    body: 'The example makes the win concrete. Build a personal assistant agent that
      checks your calendar, pulls meeting notes, and drafts follow-up emails. In the
      old world you wrote integrations against Google Calendar, Notion, and Gmail
      APIs, handled authentication, rate limits, and every edge case, then taught
      the model how to use those endpoints through long, fragile system prompts.


      Under MCP you build or install a server per system — a calendar server, a notes
      server, an email server. Each advertises what it can do: list events, get meeting
      summary, send email. The model reasons about which to use, in what order, and
      what data to pass between them. The developer doesn''t write glue code per tool.
      The video closes with the historical parallel: HTTP unified the web; MCP is
      doing the same for how models talk to tools. Every serious AI developer will
      need MCP-aware systems soon. That''s Google Cloud''s framing of the shift.'
  editorial: The fact that Google Cloud is publishing the explainer for an Anthropic-originated
    protocol on its official channel says a lot about how the industry is sorting
    itself out. The frontier-model race continues; the connection layer is standardising,
    and the hyperscalers are now actively pushing adoption. Two implications for readers.
    Short term, agent implementation flexibility goes up — stand up one MCP server
    and Claude, Codex, and Gemini can all reach the same tool. Long term, which SaaS
    ships an MCP server first determines its position in the business-AI economy.
    If Notion, Gmail, CRMs, and your internal tools all expose MCP connectors, your
    in-house agent stack inherits a general-purpose foundation tailored to your operations.
    Predicting which frontier model wins is probably the wrong question; making your
    own business platform MCP-aware is the more defensible investment.
  headerImage: /images/cGuyrANVi4A/header.png
  heroImage: /images/cGuyrANVi4A/header.png
---

## ハイライト

- [00:04] AIモデルを社内ツールやデータに接続する作業は煩雑。APIごとに挙動が異なり、統合ごとにカスタムコード、モデルが変わると接続が壊れる。これを解消するために生まれたのが Model Context Protocol (MCP)。
- [00:51] MCPはモデルとツール・データ・コンテキストを構造的につなぐオープン標準。モデルが利用可能なツールを発見し、情報を取得し、アクションを実行できる『共通言語』。
- [01:16] Anthropicが提唱し、業界全体に採用が広がっている。AI開発で最大の課題『外部リソースを安全かつ確実にモデルに使わせる』を解決する。
- [01:33] 従来APIはAI向けに設計されていない。プログラムが正確で決定論的なリクエストを送る前提だが、LLMは確率的に推論し、質問・確認・探索を経て決まる。
- [02:49] アーキテクチャ: サーバーがDB・ファイルシステム・社内ツール・ドキュメント検索などのリソースを公開。クライアント接続時、サーバーは『何ができるか』のケイパビリティと必要入力を広告。
- [03:51] MCPの主要リソースは4種: tools (実行可能なアクション)、resources (データ・状態)、prompts (再利用テンプレート)、context (外部情報)。メタデータ付きで動的発見可能。
- [06:00] 実例: パーソナルアシスタントエージェント (カレンダー確認・議事録取得・フォローアップメール作成)。旧来はGoogle Calendar/Notion/Gmail各APIにグルーコードと脆いシステムプロンプトが必要だった。
- [07:05] MCPは『HTTPがWebを統一した』のと同じレベルでAIモデルとツールの対話を統一しつつある。今後の本格AI開発者は自社システムを MCP aware に作る必要がある。

## セクション

### なぜMCPが生まれたか — 従来APIがAIに合わない構造的理由

- 時刻: 00:04

Google Cloud Techが Anthropic 発の Model Context Protocol (MCP) を概説する公式動画。冒頭の問題提起は明快だ。AIモデルを自社のツールやデータと連携させようとすると、API挙動がバラバラ、統合ごとにカスタムコード、モデル更新で接続が壊れる。AI 開発者の長年の頭痛の種だった。

根本原因はAPIの設計思想にある。従来APIは『すでに自分が何を欲しいか分かっているプログラム』向けに設計され、正確で決定論的なリクエストを前提とする。一方LLMは確率的に出力し、不確実な入力で推論し、結論を出す前に質問・確認・探索を必要とする。マッチしないインターフェース同士を強引につなぐ役割を、これまでは脆いシステムプロンプトと開発者の苦労が引き受けていた。MCPはここに『AI に合わせたインターフェース層』を入れる試みだ。

### MCPアーキテクチャ — クライアント・サーバーと4種のリソース

- 時刻: 02:49

MCPアーキテクチャはシンプルなクライアント/サーバー構造を取る。サーバー側はDB、ファイルシステム、社内ツール、ドキュメント検索エンジンといったリソースを公開する。クライアント (Claude などモデル側) が接続すると、サーバーはデータを返すのではなく『自分には何ができ、どんな入力が必要か』というケイパビリティを広告する。

この設計の効果が大きい。モデルは事前に全APIエンドポイントを知っている必要がなく、接続時に動的に発見できる。やり取りはシンプルで定義の明確なスキーマに従う。クライアントは『利用可能なリソース一覧』『このアクション実行』『このデータ取得』といったリクエストを送り、サーバーは構造化JSONで何が可能か・何が起こったかを返す。技術的には4種のリソースが基本要素になる: tools (実行可能なアクション)、resources (データ・状態)、prompts (再利用テンプレート)、context (外部情報)。各要素はメタデータ付きで、何ができ、何を入力に取り、何を返すかが明示される。

### 実例とHTTP級の普及 — なぜ今学ぶべきか

- 時刻: 06:00

実例で見るとMCPの恩恵が際立つ。カレンダー確認・議事録取得・フォローアップメール作成を担うパーソナルアシスタントエージェントを作るとする。旧世界では Google Calendar、Notion、Gmail それぞれのAPIに個別コードを書き、認証・レート制限・各種エッジケースを処理し、さらに長く脆いシステムプロンプトでモデルに使い方を教える必要があった。

MCPでは各システム向けにサーバーをビルドかインストールするだけだ。カレンダーサーバー、ノートサーバー、メールサーバー。各サーバーは『list events』『get meeting summary』『send email』のような利用可能ツールを広告し、モデルは自動でそれらを認識する。どれを、どの順で、どんなデータを渡して使うか、をモデル自身が推論する。グルーコードを毎回書く必要がない。動画は『HTTPがWebを統一した』のと同じ意味でMCPがAIモデルとツールの対話を統一しつつある、と締める。本格的なAI開発者は自社システムを MCP aware に設計する必要が出てくるだろう、というのが Google Cloud からの提言だ。

## 編集部の視点

Anthropic 発の MCP を Google Cloud が公式チャンネルで解説した、という事実そのものが業界の力学を端的に表している。OpenAI 系と Anthropic 系のフロンティアモデル競争が続く一方で、接続層は標準化が進み、ハイパースケーラーが採用を後押しする側に回った。読者にとっての含意は二段ある。短期的にはエージェント実装の自由度が増える。MCP サーバーを 1 つ立てれば、Claude / Codex / Gemini に同じツールを使わせられる前提が現実になりつつある。長期的には『どの SaaS が MCP サーバーを最初に提供したか』が業務 AI 経済圏での順位を決める。Notion、Gmail、CRM、社内ツールが MCP コネクタを揃えれば、社内エージェントは自社向けに最適化された汎用基盤を持てる。AI のフロンティアモデルが何になるかを当てるより、自社の業務基盤を MCP aware にする方が事業上の意思決定として確実な投資になる。
