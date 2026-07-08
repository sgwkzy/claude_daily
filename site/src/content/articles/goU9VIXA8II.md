---
videoId: goU9VIXA8II
title: 'MCP vs Skills: Which Is Right for Your AI Agent and LLMs?'
slug: mcpとskillsどちらを選ぶべきかibmが解説するaiエージェント構築の使い分け-gou9vixa8ii
articleTitle: MCPとSkills、どちらを選ぶべきか：IBMが解説するAIエージェント構築の使い分け
seoTitle: MCPとSkills、どちらを選ぶべきか：IBMが解説するAIエージェント構築の使い分け
summary: LLMに正しい答えを出させるには正しいコンテキストを与える必要があり、役割やタスクだけを与えるのがプロンプトエンジニアリング、追加情報まで含めるのがコンテキストエンジニアリングだと整理する。
channel: IBM Technology
channelId: UCKWaEZ-_VweaEx1j62do_vQ
publishedAt: '2026-07-07T11:00:35Z'
fetchedAt: '2026-07-08T03:09:48.567447Z'
originalThumbnail: https://i.ytimg.com/vi/goU9VIXA8II/maxresdefault.jpg
headerImage: /images/goU9VIXA8II/header.ja.png
heroImage: /images/goU9VIXA8II/header.ja.png
viewCount: 8910
durationSec: 483
sourceLanguage: en
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- MCP
- Skills
- コンテキストエンジニアリング
- AIエージェント
- IBM Technology
- LLM統合
bulletPoints:
- time: 70
  text: LLMに正しい答えを出させるには正しいコンテキストを与える必要があり、役割やタスクだけを与えるのがプロンプトエンジニアリング、追加情報まで含めるのがコンテキストエンジニアリングだと整理する。
- time: 175
  text: MCP(Model Context Protocol)はAIモデルが様々なデータソースと会話する方法を標準化し、サービスのAPIをLLMが扱いやすいシンプルな形式に抽象化する。
- time: 227
  text: MCPはLLMとデータソースの間の標準化されたレイヤーであり、ほぼすべてのAIツールがサポートしている。
- time: 244
  text: MCPは外部データを与える問題を解決したが、LLMが持っていないドメイン知識を毎回同じ形式で再現可能に与える手段が欠けていた。
- time: 314
  text: Skillsは基本的にメタデータ付きのMarkdownファイルで、タイトル・使うべき場面の説明・実際にLLMに渡されるプロンプトから構成され、フォルダにまとめられる。
- time: 374
  text: リアルタイムかつ厳密に権限管理されたデータアクセスが必要な場面ではMCPを、再利用可能なカスタム能力を軽量に追加したい場面ではSkillsを選ぶとよい。
- time: 436
  text: MCPもSkillsもどちらもオープンソースで主要なAIツールに広くサポートされており、今日からローカルで使い始められる。
sections:
- heading: プロンプトエンジニアリングとコンテキストエンジニアリングの違い
  time: 70
  body: LLMは膨大な情報で学習された『予測マシン』のようなもので、多くの質問に答えられるが、正しい答えを引き出すには正しいコンテキストを与える必要がある。役割とタスクだけを与えるのがプロンプトエンジニアリングであるのに対し、データのフォーマット方法やチーム固有のデータベース設定など追加情報まで与えることをコンテキストエンジニアリングと呼ぶ。この違いを理解することが、MCPとSkillsという2つの手法を使い分ける前提になる。
- heading: MCP：外部データソースとの標準化された対話
  time: 175
  body: エージェントがCRMのデータを必要とする場合を例に、MCP(Model Context Protocol)がどう機能するかを説明する。サービスのAPI仕様書やトークンをそのままLLMに渡して『間違えないように』と祈るのではなく、MCPはAIモデルが様々なデータソースと対話する方法そのものを標準化する。サービスのAPIをLLMが扱いやすいシンプルな形式に抽象化し、認証も処理する。MCPサーバーはIDEやAIアプリケーションに組み込まれ、LLMが必要な情報についてJSONリクエストを生成し、それをPOSTやGETリクエストに変換してサービスを呼び出す。ほぼすべてのAIツールがサポートする標準化レイヤーだ。
- heading: Skills：再現可能なドメイン知識の付与と使い分けの基準
  time: 244
  body: 'MCPは外部データを与える問題を解決したが、LLMが持っていないドメイン知識——例えば営業チームが望むCRMデータのフォーマット（顧客名・連絡先・そして『好きなクッキーの種類』まで）——を毎回同じ形式で再現可能に与える手段が欠けていた。LLMは本質的に非決定論的なため、この『毎回同じフォーマットにする』という要求は簡単ではない。


    Skillsは基本的にメタデータ付きのMarkdownファイルで、タイトル・使うべき場面の説明・実際にLLMに渡されるプロンプトから構成され、フォルダにまとめられる。必要なときだけLLMのコンテキストウィンドウに自動的に読み込まれる点が特徴だ。リアルタイムかつ厳密に権限管理されたデータアクセスが必要な場面（VMの稼働状況の確認など）ではMCPを、再利用可能なカスタム能力を軽量に追加したい場面（投資データの取得・分析など）ではSkillsを選ぶとよい。両者はどちらもオープンソースで、多くのAIツールで広くサポートされており、今日からローカルで使い始められる。'
editorial: この解説の価値は、MCPとSkillsを『どちらが優れているか』ではなく『何を解決する技術か』という切り口で整理し直している点にある。MCPが『外部データへのリアルタイムかつ権限管理されたアクセス』を、Skillsが『再現可能なドメイン知識の注入』を担うという役割分担は、実際にAIエージェントを設計する際の判断基準として明快で実務的だ。特に『MCPの設定はSkillsだけで十分な場面には過剰(overkill)になり得る』という指摘は、技術選定において常に最も強力な手段を使えばよいわけではないという原則を思い出させる。IBMという企業向けインフラを長年手がけてきた企業からの解説であるだけに、エンタープライズ環境でのAIエージェント設計における実用性の高い判断軸として参考になるだろう。
en:
  articleTitle: 'MCP vs. Skills: IBM Breaks Down When to Use Each for Building AI
    Agents'
  seoTitle: 'MCP vs. Skills: IBM Breaks Down When to Use Each for Building AI'
  summary: Getting the right answer from an LLM requires the right context -- giving
    it just a role and task is prompt…
  keyPhrases:
  - MCP
  - Skills
  - context engineering
  - AI agents
  - IBM Technology
  - LLM integration
  bulletPoints:
  - time: 70
    text: Getting the right answer from an LLM requires the right context -- giving
      it just a role and task is prompt engineering, while adding extra information
      is context engineering.
  - time: 175
    text: MCP (Model Context Protocol) standardizes how an AI model talks to different
      data sources, abstracting a service's API into a simple, LLM-ready format.
  - time: 227
    text: MCP is a standardized layer between the LLM and data sources, supported
      by nearly every AI tool out there.
  - time: 244
    text: 'MCP solves the problem of feeding external data to an LLM, but leaves a
      gap: how do you give it domain knowledge, reproducibly, the same way every time?'
  - time: 314
    text: Skills are essentially markdown files with metadata -- a title, a description
      of when to use it, and the actual prompt passed to the LLM -- packaged into
      a folder.
  - time: 374
    text: Use MCP when you need real-time, tightly-permissioned access to data; use
      Skills when you need a lightweight, reusable custom capability.
  - time: 436
    text: Both MCP and Skills are open source and broadly supported across today's
      major AI tools, and you can start using both locally right now.
  sections:
  - heading: Prompt Engineering vs. Context Engineering
    time: 70
    body: An LLM is essentially a prediction engine trained on vast amounts of information,
      capable of answering many kinds of questions -- but getting the right answer
      depends on giving it the right context. Providing just a role and a task is
      prompt engineering; adding extra information, like how you want data formatted
      or how your team's database is configured, is context engineering. Understanding
      that distinction is the foundation for knowing when to reach for MCP versus
      Skills.
  - heading: 'MCP: A Standardized Conversation With External Data Sources'
    time: 175
    body: Using an agent that needs CRM data as the example, the video explains how
      MCP works. Instead of pasting a service's raw API docs and a token into the
      LLM and hoping for the best, MCP standardizes how an AI model talks to different
      data sources -- abstracting a service's API into a simple, LLM-ready format
      and handling authentication. An MCP server gets wired into your IDE or AI application,
      has the LLM generate a JSON request for the information it needs, and translates
      that into the actual POST or GET request to the service. It's a standardized
      layer supported by nearly every AI tool out there.
  - heading: 'Skills: Reproducible Domain Knowledge, and How to Choose'
    time: 244
    body: 'MCP solves the problem of feeding external data to an LLM, but leaves one
      gap: how do you give it domain knowledge it doesn''t already have -- for example,
      a sales team wanting CRM data formatted the exact same way every time, down
      to a customer''s name, contact info, and even their favorite type of cookie.
      Since LLMs are inherently non-deterministic, reliably repeating a format like
      that is genuinely hard.


      Skills are essentially markdown files with metadata -- a title, a description
      of when to use it, and the actual prompt passed to the LLM -- packaged into
      a folder, auto-loaded into the context window only when needed. Use MCP for
      situations requiring real-time, tightly-permissioned data access (checking VM
      status, for example); use Skills when you need a lightweight, reusable custom
      capability (fetching and analyzing investment data, for example). Both are open
      source, broadly supported across today''s AI tools, and usable locally starting
      today.'
  editorial: The value in this explainer is reframing MCP versus Skills not as a 'which
    is better' debate but as a question of what problem each actually solves. MCP
    handles real-time, permissioned access to external data; Skills inject reproducible
    domain knowledge -- a division of labor that's clear and practically useful when
    actually designing an AI agent. The observation that setting up MCP can be overkill
    for something Skills alone would cover is a good reminder that the most powerful
    tool isn't always the right choice. Coming from IBM, a company with decades of
    enterprise infrastructure experience, this reads as a genuinely practical decision
    framework for designing AI agents in enterprise environments.
  headerImage: /images/goU9VIXA8II/header.png
  heroImage: /images/goU9VIXA8II/header.png
---

## ハイライト

- [01:10] LLMに正しい答えを出させるには正しいコンテキストを与える必要があり、役割やタスクだけを与えるのがプロンプトエンジニアリング、追加情報まで含めるのがコンテキストエンジニアリングだと整理する。
- [02:55] MCP(Model Context Protocol)はAIモデルが様々なデータソースと会話する方法を標準化し、サービスのAPIをLLMが扱いやすいシンプルな形式に抽象化する。
- [03:47] MCPはLLMとデータソースの間の標準化されたレイヤーであり、ほぼすべてのAIツールがサポートしている。
- [04:04] MCPは外部データを与える問題を解決したが、LLMが持っていないドメイン知識を毎回同じ形式で再現可能に与える手段が欠けていた。
- [05:14] Skillsは基本的にメタデータ付きのMarkdownファイルで、タイトル・使うべき場面の説明・実際にLLMに渡されるプロンプトから構成され、フォルダにまとめられる。
- [06:14] リアルタイムかつ厳密に権限管理されたデータアクセスが必要な場面ではMCPを、再利用可能なカスタム能力を軽量に追加したい場面ではSkillsを選ぶとよい。
- [07:16] MCPもSkillsもどちらもオープンソースで主要なAIツールに広くサポートされており、今日からローカルで使い始められる。

## セクション

### プロンプトエンジニアリングとコンテキストエンジニアリングの違い

- 時刻: 01:10

LLMは膨大な情報で学習された『予測マシン』のようなもので、多くの質問に答えられるが、正しい答えを引き出すには正しいコンテキストを与える必要がある。役割とタスクだけを与えるのがプロンプトエンジニアリングであるのに対し、データのフォーマット方法やチーム固有のデータベース設定など追加情報まで与えることをコンテキストエンジニアリングと呼ぶ。この違いを理解することが、MCPとSkillsという2つの手法を使い分ける前提になる。

### MCP：外部データソースとの標準化された対話

- 時刻: 02:55

エージェントがCRMのデータを必要とする場合を例に、MCP(Model Context Protocol)がどう機能するかを説明する。サービスのAPI仕様書やトークンをそのままLLMに渡して『間違えないように』と祈るのではなく、MCPはAIモデルが様々なデータソースと対話する方法そのものを標準化する。サービスのAPIをLLMが扱いやすいシンプルな形式に抽象化し、認証も処理する。MCPサーバーはIDEやAIアプリケーションに組み込まれ、LLMが必要な情報についてJSONリクエストを生成し、それをPOSTやGETリクエストに変換してサービスを呼び出す。ほぼすべてのAIツールがサポートする標準化レイヤーだ。

### Skills：再現可能なドメイン知識の付与と使い分けの基準

- 時刻: 04:04

MCPは外部データを与える問題を解決したが、LLMが持っていないドメイン知識——例えば営業チームが望むCRMデータのフォーマット（顧客名・連絡先・そして『好きなクッキーの種類』まで）——を毎回同じ形式で再現可能に与える手段が欠けていた。LLMは本質的に非決定論的なため、この『毎回同じフォーマットにする』という要求は簡単ではない。

Skillsは基本的にメタデータ付きのMarkdownファイルで、タイトル・使うべき場面の説明・実際にLLMに渡されるプロンプトから構成され、フォルダにまとめられる。必要なときだけLLMのコンテキストウィンドウに自動的に読み込まれる点が特徴だ。リアルタイムかつ厳密に権限管理されたデータアクセスが必要な場面（VMの稼働状況の確認など）ではMCPを、再利用可能なカスタム能力を軽量に追加したい場面（投資データの取得・分析など）ではSkillsを選ぶとよい。両者はどちらもオープンソースで、多くのAIツールで広くサポートされており、今日からローカルで使い始められる。

## 編集部の視点

この解説の価値は、MCPとSkillsを『どちらが優れているか』ではなく『何を解決する技術か』という切り口で整理し直している点にある。MCPが『外部データへのリアルタイムかつ権限管理されたアクセス』を、Skillsが『再現可能なドメイン知識の注入』を担うという役割分担は、実際にAIエージェントを設計する際の判断基準として明快で実務的だ。特に『MCPの設定はSkillsだけで十分な場面には過剰(overkill)になり得る』という指摘は、技術選定において常に最も強力な手段を使えばよいわけではないという原則を思い出させる。IBMという企業向けインフラを長年手がけてきた企業からの解説であるだけに、エンタープライズ環境でのAIエージェント設計における実用性の高い判断軸として参考になるだろう。
