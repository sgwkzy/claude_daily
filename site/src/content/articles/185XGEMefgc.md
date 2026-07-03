---
videoId: 185XGEMefgc
title: 'MCP vs API: The protocol every developer needs to know'
slug: mcpとapiは何が違うのかai時代のプロトコルを基礎から整理する-185xgemefgc
articleTitle: MCPとAPIは何が違うのか：AI時代のプロトコルを基礎から整理する
seoTitle: MCPとAPIは何が違うのか：AI時代のプロトコルを基礎から整理する
summary: AIモデルとツールをつなぐ方法が根本的に書き換えられつつあり、その中心にあるのがMCP(Model Context Protocol)だ。
channel: Google Cloud Tech
channelId: UCJS9pqu9BzkAMNTmzNMNhvg
publishedAt: '2026-07-01T13:00:03Z'
fetchedAt: '2026-07-02T13:29:28.028816Z'
originalThumbnail: https://i.ytimg.com/vi/185XGEMefgc/maxresdefault.jpg
headerImage: /images/185XGEMefgc/header.ja.png
heroImage: /images/185XGEMefgc/header.ja.png
viewCount: 16754
durationSec: 745
sourceLanguage: en-US
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- MCP
- Model Context Protocol
- API
- LLM統合
- JSON schema
- 相互運用性
bulletPoints:
- time: 4
  text: AIモデルとツールをつなぐ方法が根本的に書き換えられつつあり、その中心にあるのがMCP(Model Context Protocol)だ。
- time: 61
  text: 従来のAPIはプログラム同士の決まりきったやり取り向けに設計されており、複数エンドポイントを連鎖的に扱うLLMの推論には不向き。
- time: 107
  text: APIは「鍵の形と引き出しの場所を正確に知る必要がある鍵付き棚」に例えられ、曖昧な状況を推論するモデルとは相性が悪い。
- time: 347
  text: MCPサーバーはJSON schemaで自身の機能を自己記述し、モデルはメタデータをもとに関数を直接呼び出せる。
- time: 410
  text: 100個の個別統合を作る代わりに、1つのMCPインターフェースを作れば対応する全モデルが即座に使える。
- time: 607
  text: HTTPがFTPやTelnetなど乱立したプロトコルを統一したように、MCPはAIエージェント向けの統一層になろうとしている。
- time: 668
  text: 結論として、APIは死なない。決定論的システム向けのAPIと、確率的に推論するAIモデル向けのMCPは補完関係にある。
sections:
- heading: なぜ通常のAPIはLLMに向かないのか
  time: 61
  body: 'APIは数十年にわたり、システム間の「共通言語」として機能してきた。エンドポイントを定義し、リクエストを送ればレスポンスが返る——予測可能でクリーンな仕組みだ。従来型ソフトウェアにはこれで十分だった。


    しかし大規模言語モデルが登場すると事情が変わる。モデルは1つのエンドポイントだけでなく、10個のエンドポイントを連鎖させたり、非構造化データを解釈したり、追加の質問をしたりする必要がある。単なる「ツールへのアクセス」だけでなく「文脈(コンテキスト)」そのものを必要とするようになった。'
- heading: MCPサーバーの自己記述という仕組み
  time: 347
  body: 'MCPサーバーは、サービスやデータソースのそばに置かれる軽量なプロセスで、自分が何をできるかをJSON schemaで記述する。モデルはWebSocketやHTTPなど標準化されたインターフェース経由でこのサーバーに接続し、利用可能なリソースのメタデータを受け取る。


    接続後、モデルは推測ではなくメタデータをもとに関数を直接呼び出せる。必要な入力、各フィールドの意味、期待される出力形式まで自己記述されているため、開発者がスキーマをプロンプトエンジニアリングしたりレスポンスを整形し直したりする必要がない。個別のAPI統合ごとにドキュメントを読み込んでペイロードをマッピングする従来の手間を、MCPは丸ごと抽象化する。'
- heading: APIとMCPは対立ではなく分業
  time: 668
  body: 'HTTPがFTP・Gopher・Telnetといった乱立するプロトコルを統一しインターネット全体を相互運用可能にしたように、MCPは各社が独自に作っていたプラグイン形式や統合レイヤーを1つのオープンプロトコルへ集約しようとしている。一度コネクタを作れば、対応する全てのモデルがそれを使える世界だ。


    結論として、APIは無くならない。APIは決定論的なシステム同士のやり取り向けであり、MCPはモデルが「自分に何ができるか」を推論するための確率的なシステム向けだ。MCPはAPIの1つ上のレイヤーに位置し、静的なルートを「モデルが推論できる生きたインターフェース」へと変えていく。'
editorial: MCPとAPIの関係を「対立」ではなく「レイヤーの違い」として整理した点がこの動画の価値だ。実務でMCPサーバーを設計する際、既存APIを単純にラップするだけでは自己記述性というMCPの本質的な利点を活かせない。入出力の意味づけやスキーマ設計にこそ投資すべきだという示唆になる。またHTTPの歴史との比較は、標準化がエコシステム全体の統合コストを下げるという普遍的な教訓を思い出させる。100個の個別統合が1つのMCPサーバーに置き換わるという主張は、Claude以外のモデルを併用する組織にとっても導入判断の材料になるだろう。
en:
  articleTitle: 'MCP vs API: Understanding the Protocol Rewriting How AI Connects
    to Everything'
  seoTitle: 'MCP vs API: Understanding the Protocol Rewriting How AI Connects'
  summary: 'The way AI models connect to tools, data, and systems is being rewritten
    around a new standard: the Model Context…'
  keyPhrases:
  - MCP
  - Model Context Protocol
  - API
  - LLM integration
  - JSON schema
  - interoperability
  bulletPoints:
  - time: 4
    text: 'The way AI models connect to tools, data, and systems is being rewritten
      around a new standard: the Model Context Protocol (MCP).'
  - time: 61
    text: Traditional APIs were built for predictable program-to-program calls, not
      for models that need to chain endpoints and reason over messy data.
  - time: 107
    text: An API is like a locked cabinet where you must know exactly which drawer
      to open -- a poor fit for a model that's reasoning about unlabeled contents.
  - time: 347
    text: An MCP server is a lightweight process that self-describes its capabilities
      via JSON schemas, letting models call functions directly using that metadata.
  - time: 410
    text: Instead of building 100 custom integrations, you build one MCP interface
      and every compatible model can use it instantly.
  - time: 607
    text: Just as HTTP unified fragmented protocols like FTP and Telnet, MCP aims
      to become the unifying layer for AI agents.
  - time: 668
    text: APIs aren't going away -- they remain the deterministic foundation, while
      MCP is the layer built for probabilistic, reasoning-based systems.
  sections:
  - heading: Why Traditional APIs Don't Fit LLMs
    time: 61
    body: 'For decades, APIs served as the universal handshake between systems: define
      an endpoint, send a request, get a response back. Clean and predictable -- perfect
      for traditional software.


      Large language models changed the equation. Models don''t just call one endpoint;
      they chain many together, interpret unstructured data, and ask follow-up questions.
      That means they need context, not just tool access, and conventional APIs simply
      weren''t designed for that kind of reasoning.'
  - heading: How MCP Servers Self-Describe
    time: 347
    body: 'An MCP server sits next to a service or data source as a lightweight process,
      describing what it can do and what functions it exposes entirely through JSON
      schemas. Models connect via a standardized interface like WebSocket or HTTP
      and receive metadata about available resources.


      Once connected, a model can call functions directly -- not by guessing, but
      by reading the metadata for required inputs, field meanings, and expected output
      types. Everything is self-describing, eliminating the need to hand-craft prompts
      around a schema or manually wrap each endpoint the way traditional API integration
      requires.'
  - heading: APIs and MCP Are Complementary, Not Competing
    time: 668
    body: 'Just as HTTP once unified fragmented internet protocols like FTP, Gopher,
      and Telnet, MCP is trying to do the same for AI agents -- replacing each company''s
      bespoke plugin format with a single open protocol that any model can understand.
      Build a connector once, and any compliant model can use it.


      The conclusion isn''t that APIs are dead; they''re evolving. APIs remain the
      foundation for deterministic, program-to-program systems, while MCP is built
      for probabilistic systems where a model reasons about what it can do. MCP sits
      one layer above APIs, turning static routes into living interfaces models can
      actually reason about.'
  editorial: 'The most useful framing here is treating MCP and API not as rivals but
    as different layers of the same stack. Teams building MCP servers who simply wrap
    an existing API without rethinking self-description lose the protocol''s core
    benefit -- the payoff comes from investing in how inputs, outputs, and semantics
    are described, not just exposing endpoints. The HTTP analogy is also a reminder
    that standardization compounds: once one protocol wins, integration costs across
    the whole ecosystem drop, which matters for any team weighing MCP adoption today.'
  headerImage: /images/185XGEMefgc/header.png
  heroImage: /images/185XGEMefgc/header.png
---

## ハイライト

- [00:04] AIモデルとツールをつなぐ方法が根本的に書き換えられつつあり、その中心にあるのがMCP(Model Context Protocol)だ。
- [01:01] 従来のAPIはプログラム同士の決まりきったやり取り向けに設計されており、複数エンドポイントを連鎖的に扱うLLMの推論には不向き。
- [01:47] APIは「鍵の形と引き出しの場所を正確に知る必要がある鍵付き棚」に例えられ、曖昧な状況を推論するモデルとは相性が悪い。
- [05:47] MCPサーバーはJSON schemaで自身の機能を自己記述し、モデルはメタデータをもとに関数を直接呼び出せる。
- [06:50] 100個の個別統合を作る代わりに、1つのMCPインターフェースを作れば対応する全モデルが即座に使える。
- [10:07] HTTPがFTPやTelnetなど乱立したプロトコルを統一したように、MCPはAIエージェント向けの統一層になろうとしている。
- [11:08] 結論として、APIは死なない。決定論的システム向けのAPIと、確率的に推論するAIモデル向けのMCPは補完関係にある。

## セクション

### なぜ通常のAPIはLLMに向かないのか

- 時刻: 01:01

APIは数十年にわたり、システム間の「共通言語」として機能してきた。エンドポイントを定義し、リクエストを送ればレスポンスが返る——予測可能でクリーンな仕組みだ。従来型ソフトウェアにはこれで十分だった。

しかし大規模言語モデルが登場すると事情が変わる。モデルは1つのエンドポイントだけでなく、10個のエンドポイントを連鎖させたり、非構造化データを解釈したり、追加の質問をしたりする必要がある。単なる「ツールへのアクセス」だけでなく「文脈(コンテキスト)」そのものを必要とするようになった。

### MCPサーバーの自己記述という仕組み

- 時刻: 05:47

MCPサーバーは、サービスやデータソースのそばに置かれる軽量なプロセスで、自分が何をできるかをJSON schemaで記述する。モデルはWebSocketやHTTPなど標準化されたインターフェース経由でこのサーバーに接続し、利用可能なリソースのメタデータを受け取る。

接続後、モデルは推測ではなくメタデータをもとに関数を直接呼び出せる。必要な入力、各フィールドの意味、期待される出力形式まで自己記述されているため、開発者がスキーマをプロンプトエンジニアリングしたりレスポンスを整形し直したりする必要がない。個別のAPI統合ごとにドキュメントを読み込んでペイロードをマッピングする従来の手間を、MCPは丸ごと抽象化する。

### APIとMCPは対立ではなく分業

- 時刻: 11:08

HTTPがFTP・Gopher・Telnetといった乱立するプロトコルを統一しインターネット全体を相互運用可能にしたように、MCPは各社が独自に作っていたプラグイン形式や統合レイヤーを1つのオープンプロトコルへ集約しようとしている。一度コネクタを作れば、対応する全てのモデルがそれを使える世界だ。

結論として、APIは無くならない。APIは決定論的なシステム同士のやり取り向けであり、MCPはモデルが「自分に何ができるか」を推論するための確率的なシステム向けだ。MCPはAPIの1つ上のレイヤーに位置し、静的なルートを「モデルが推論できる生きたインターフェース」へと変えていく。

## 編集部の視点

MCPとAPIの関係を「対立」ではなく「レイヤーの違い」として整理した点がこの動画の価値だ。実務でMCPサーバーを設計する際、既存APIを単純にラップするだけでは自己記述性というMCPの本質的な利点を活かせない。入出力の意味づけやスキーマ設計にこそ投資すべきだという示唆になる。またHTTPの歴史との比較は、標準化がエコシステム全体の統合コストを下げるという普遍的な教訓を思い出させる。100個の個別統合が1つのMCPサーバーに置き換わるという主張は、Claude以外のモデルを併用する組織にとっても導入判断の材料になるだろう。
