---
videoId: 3_JPHuXgDyQ
title: 'An MCP for your Postgres DB | POSETTE: An Event for Postgres 2026'
slug: postgres用mcpサーバーの作り方-自然言語db操作を安全にする4層防御-3_jphuxgdyq
articleTitle: Postgres用MCPサーバーの作り方 — 自然言語DB操作を安全にする4層防御
seoTitle: Postgres用MCPサーバーの作り方 — 自然言語DB操作を安全にする4層防御
summary: MicrosoftのパメラがPOSETTEで、エージェントが完全なSQLを送れる探索型サーバーから、完全に型付けされた運用型サーバーまで、Postgres向けMCPの幅広い構築方法を解説する。
channel: Microsoft Developer
channelId: UCsMica-v34Irf9KVTh6xx-g
publishedAt: '2026-06-16T20:50:47Z'
fetchedAt: '2026-06-19T00:52:38.910395Z'
originalThumbnail: https://i.ytimg.com/vi/3_JPHuXgDyQ/maxresdefault.jpg
headerImage: /images/3_JPHuXgDyQ/header.ja.png
heroImage: /images/3_JPHuXgDyQ/header.ja.png
viewCount: 41850
durationSec: 1427
sourceLanguage: en
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- MCP
- PostgreSQL
- 最小権限ロール
- GitHub Copilot
- SQLセキュリティ
- Model Context Protocol
bulletPoints:
- time: 16
  text: MicrosoftのパメラがPOSETTEで、エージェントが完全なSQLを送れる探索型サーバーから、完全に型付けされた運用型サーバーまで、Postgres向けMCPの幅広い構築方法を解説する。
- time: 62
  text: GitHub CopilotがOpus 4.6を使い、住んでいる地域で4月に活動するハチの種類を尋ねる質問に、MCP経由でDBにSQLを実行して回答するデモから始まる。
- time: 120
  text: MCPはModel Context Protocolの略で、AIアプリやエージェントが外部ツールやデータソースからコンテキストを取得する方法を定めるオープンプロトコル。Anthropicが提唱し、現在はLinux
    Foundationの一部となっている。
- time: 666
  text: 最小権限ロールを使い、特定スキーマへのSELECT権限のみを与えることで、INSERT・DROP・DELETEや、パーサーをすり抜けるCTEもデータベースレベルで強制的にブロックできる。
- time: 718
  text: エージェントが自分でSQLを生成しても安全だと確信するには複数の保護レイヤーが必要で、トリッキーなクエリが各層を通過しうるため4層の防御を組む。
- time: 754
  text: pg_sleep()や巨大なCROSS JOINといったサーバーへのDDoS的な操作には、ツールに最大30秒などのタイムアウトを設定して強制終了させる。
- time: 1306
  text: 探索型・読み取り専用・完全型付けの3方式にはそれぞれ利点と制約があり、自分の状況に合う範囲を見極めて組み合わせるべきだと結論づける。
sections:
- heading: MCPとは何か、Postgresでの実演
  time: 62
  body: 'セッションは、GitHub CopilotがOpus 4.6を介してPostgresにクエリを投げ、地域のハチの観測データから回答を導くデモで幕を開ける。エージェントがMCPサーバーの存在を認識し、自らSQLを実行する流れだ。


    MCPはAIアプリやエージェントが外部データソースからコンテキストを取得する方法を定義するオープンプロトコルである。Anthropicが最初に提唱し、その後広く採用されて今はLinux
    Foundationの傘下にある。


    MCP以前は各データソースごとにカスタム統合が必要だったが、今はソースごとにMCPサーバーを置けば共通の取得手段が手に入る、とパメラは説明する。'
  image: null
- heading: 自然言語SQLを安全にする4層防御
  time: 666
  body: '中核は、エージェントに自由なSQLを書かせても安全にするための防御設計だ。まず最小権限ロールで特定スキーマへのSELECTのみを許可し、INSERTやDROP、DELETEをデータベースレベルで遮断する。


    パーサーをすり抜けてしまうCTE(WITH句)も、このデータベースレベルの強制でブロックされる。副作用を伴う関数呼び出しも最小権限ロールで防げる。


    さらにpg_sleepや巨大なCROSS JOINのようなDDoS的操作に対しては、ツールにタイムアウトを設定して強制終了させる。これら複数の層を重ねて初めて、生成SQLの実行に確信が持てるという。'
  image: null
- heading: 用途に応じたサーバー設計の選択
  time: 1306
  body: '終盤、パメラはPostgres上にMCPサーバーを構築する複数の方法を振り返る。あらゆる質問に答えられる探索型は柔軟だが、あらゆるSQL操作を許してしまうリスクを伴う。


    一方、完全に型付けされたツールは安全だが、答えられる質問の範囲は限定される。その中間に読み取り専用のSQLクエリという選択肢がある。


    データベースレベルで多くを強制できるため最も安全なアプローチになると述べ、内部・外部を問わずユーザーが自然言語でDBと対話できる強力さを、設計上の注意とともに勧めて締めくくった。'
  image: null
en:
  articleTitle: 'How to Build a Postgres MCP Server: Four Layers of Defense for Natural-Language
    SQL'
  seoTitle: 'How to Build a Postgres MCP Server: Four Layers of Defense for N'
  summary: At POSETTE, Microsoft's Pamela explains the full range of Postgres MCP
    architectures, from exploratory servers that…
  keyPhrases:
  - MCP
  - PostgreSQL
  - least-privilege roles
  - GitHub Copilot
  - SQL security
  - Model Context Protocol
  bulletPoints:
  - time: 16
    text: At POSETTE, Microsoft's Pamela explains the full range of Postgres MCP architectures,
      from exploratory servers that let agents send arbitrary SQL to fully typed operational
      servers.
  - time: 62
    text: The talk opens with a demo in which GitHub Copilot, using Opus 4.6, answers
      a question about which bee species are active locally in April by issuing SQL
      through MCP.
  - time: 120
    text: MCP stands for Model Context Protocol, an open protocol that defines how
      AI apps and agents retrieve context from external tools and data sources. It
      was proposed by Anthropic and is now part of the Linux Foundation.
  - time: 666
    text: By using least-privilege roles that grant only SELECT access to a specific
      schema, the system can block INSERT, DROP, DELETE, and even CTE-based evasions
      at the database level.
  - time: 718
    text: To be confident that agents can safely generate their own SQL, multiple
      protection layers are required, since tricky queries can slip through any single
      layer.
  - time: 754
    text: Potential DDoS-like queries such as `pg_sleep()` or massive `CROSS JOIN`s
      are handled by enforcing tool timeouts such as 30 seconds.
  - time: 1306
    text: The talk concludes that exploratory, read-only, and fully typed server designs
      each have strengths and tradeoffs, and should be combined according to the situation.
  sections:
  - heading: What MCP is and how it works with Postgres
    time: 62
    body: 'The session opens with a demo in which GitHub Copilot, working through
      Opus 4.6, queries Postgres and answers a question using local bee observation
      data. The agent recognizes the MCP server, decides to use it, and executes SQL
      on its own.


      MCP is an open protocol that defines how AI applications and agents retrieve
      context from external data sources. It was first proposed by Anthropic, later
      broadly adopted, and now sits under the Linux Foundation.


      Before MCP, every data source typically required a custom integration. Pamela
      explains that by putting an MCP server in front of each source, developers now
      get a common access mechanism instead.'
    image: null
  - heading: Four layers of defense for natural-language SQL
    time: 666
    body: 'The core of the talk is a defensive design that makes it safer to let agents
      write SQL freely. The first layer is a least-privilege role that allows only
      SELECT access to a specific schema, blocking INSERT, DROP, and DELETE at the
      database level.


      Even CTE-based evasions using `WITH` clauses can be stopped when the database
      itself enforces those restrictions. Function calls with side effects can likewise
      be prevented through the least-privilege role.


      On top of that, DDoS-style operations such as `pg_sleep()` or huge `CROSS JOIN`s
      are handled by giving the tool a timeout and terminating the query. The message
      is that only by combining multiple layers can teams have confidence in executing
      generated SQL.'
    image: null
  - heading: Choosing the right server design for the job
    time: 1306
    body: 'In the closing section, Pamela reviews several ways to build an MCP server
      on top of Postgres. An exploratory design is flexible because it can answer
      a wide range of questions, but it also carries the risk of permitting any SQL
      operation.


      A fully typed toolset is safer, but the scope of questions it can answer is
      narrower. Between those extremes sits the option of read-only SQL queries.


      She concludes that because so much can be enforced at the database level, this
      becomes the safest practical approach. The talk ends by recommending natural-language
      database interaction for both internal and external users, while emphasizing
      the need for careful server design.'
    image: null
  headerImage: /images/3_JPHuXgDyQ/header.png
  heroImage: /images/3_JPHuXgDyQ/header.png
---

## ハイライト

- [00:16] MicrosoftのパメラがPOSETTEで、エージェントが完全なSQLを送れる探索型サーバーから、完全に型付けされた運用型サーバーまで、Postgres向けMCPの幅広い構築方法を解説する。
- [01:02] GitHub CopilotがOpus 4.6を使い、住んでいる地域で4月に活動するハチの種類を尋ねる質問に、MCP経由でDBにSQLを実行して回答するデモから始まる。
- [02:00] MCPはModel Context Protocolの略で、AIアプリやエージェントが外部ツールやデータソースからコンテキストを取得する方法を定めるオープンプロトコル。Anthropicが提唱し、現在はLinux Foundationの一部となっている。
- [11:06] 最小権限ロールを使い、特定スキーマへのSELECT権限のみを与えることで、INSERT・DROP・DELETEや、パーサーをすり抜けるCTEもデータベースレベルで強制的にブロックできる。
- [11:58] エージェントが自分でSQLを生成しても安全だと確信するには複数の保護レイヤーが必要で、トリッキーなクエリが各層を通過しうるため4層の防御を組む。
- [12:34] pg_sleep()や巨大なCROSS JOINといったサーバーへのDDoS的な操作には、ツールに最大30秒などのタイムアウトを設定して強制終了させる。
- [21:46] 探索型・読み取り専用・完全型付けの3方式にはそれぞれ利点と制約があり、自分の状況に合う範囲を見極めて組み合わせるべきだと結論づける。

## セクション

### MCPとは何か、Postgresでの実演

- 時刻: 01:02

セッションは、GitHub CopilotがOpus 4.6を介してPostgresにクエリを投げ、地域のハチの観測データから回答を導くデモで幕を開ける。エージェントがMCPサーバーの存在を認識し、自らSQLを実行する流れだ。

MCPはAIアプリやエージェントが外部データソースからコンテキストを取得する方法を定義するオープンプロトコルである。Anthropicが最初に提唱し、その後広く採用されて今はLinux Foundationの傘下にある。

MCP以前は各データソースごとにカスタム統合が必要だったが、今はソースごとにMCPサーバーを置けば共通の取得手段が手に入る、とパメラは説明する。

### 自然言語SQLを安全にする4層防御

- 時刻: 11:06

中核は、エージェントに自由なSQLを書かせても安全にするための防御設計だ。まず最小権限ロールで特定スキーマへのSELECTのみを許可し、INSERTやDROP、DELETEをデータベースレベルで遮断する。

パーサーをすり抜けてしまうCTE(WITH句)も、このデータベースレベルの強制でブロックされる。副作用を伴う関数呼び出しも最小権限ロールで防げる。

さらにpg_sleepや巨大なCROSS JOINのようなDDoS的操作に対しては、ツールにタイムアウトを設定して強制終了させる。これら複数の層を重ねて初めて、生成SQLの実行に確信が持てるという。

### 用途に応じたサーバー設計の選択

- 時刻: 21:46

終盤、パメラはPostgres上にMCPサーバーを構築する複数の方法を振り返る。あらゆる質問に答えられる探索型は柔軟だが、あらゆるSQL操作を許してしまうリスクを伴う。

一方、完全に型付けされたツールは安全だが、答えられる質問の範囲は限定される。その中間に読み取り専用のSQLクエリという選択肢がある。

データベースレベルで多くを強制できるため最も安全なアプローチになると述べ、内部・外部を問わずユーザーが自然言語でDBと対話できる強力さを、設計上の注意とともに勧めて締めくくった。
