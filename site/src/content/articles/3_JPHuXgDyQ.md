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
headerImage: /images/3_JPHuXgDyQ/header.png
heroImage: /images/3_JPHuXgDyQ/header.png
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
