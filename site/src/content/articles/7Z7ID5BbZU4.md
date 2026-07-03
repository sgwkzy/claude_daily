---
videoId: 7Z7ID5BbZU4
title: Containers Don't Make Your AI Agent Safe
slug: コンテナだけではaiエージェントは安全にならないnpm脆弱性時代のサンドボックス実践-7z7id5bbzu4
articleTitle: コンテナだけではAIエージェントは安全にならない：npm脆弱性時代のサンドボックス実践
seoTitle: コンテナだけではAIエージェントは安全にならない：npm脆弱性時代のサンドボックス実践
summary: AIがデータベースを削除したりコンピュータを破壊したりする事故を避けるため、多くの人は危険な操作の度に許可を求める設定にしている。
channel: Web Dev Simplified
channelId: UCFbNIlppjAuEX4znoulh0Cw
publishedAt: '2026-06-30T16:00:22Z'
fetchedAt: '2026-07-02T13:29:28.028816Z'
originalThumbnail: https://i.ytimg.com/vi/7Z7ID5BbZU4/maxresdefault.jpg
headerImage: /images/7Z7ID5BbZU4/header.ja.png
heroImage: /images/7Z7ID5BbZU4/header.ja.png
viewCount: 15234
durationSec: 2176
sourceLanguage: en-US
matchedKeywords:
- AIエージェント
proposedByLLM: false
keyPhrases:
- AIエージェント
- サンドボックス
- Docker Sandbox
- npm脆弱性
- ネットワークポリシー
- 権限管理
bulletPoints:
- time: 0
  text: AIがデータベースを削除したりコンピュータを破壊したりする事故を避けるため、多くの人は危険な操作の度に許可を求める設定にしている。
- time: 12
  text: 許可待ちは生産性を大きく損なうため、逆に無制限にAIへ権限を与えてしまう人も多く、これが新たなリスクを生む。
- time: 18
  text: npmでは毎週のように新たなセキュリティ脆弱性が見つかり、APIキー窃取やシステム破壊を狙う悪意あるパッケージが後を絶たない。
- time: 37
  text: 筆者はAI開発を含む全ての作業でサンドボックスを使い、権限チェックなしでAIを走らせてもシステムに実害が及ばないようにしている。
- time: 1039
  text: デフォルトでは外部APIへのアクセスがロックされており、許可した特定サイト以外へのfetchはエラーになる仕組みを実演。
- time: 1070
  text: ネットワークポリシーをコマンドで追加・一覧表示でき、必要なサイトだけをグローバルまたは個別に許可できる。
- time: 2141
  text: 紹介した機能はDocker Sandboxの使用例の99%をカバーしており、今ではサンドボックス外でAIコードを書かないと明言。
sections:
- heading: 許可待ちか無制限権限か、という誤った二択
  time: 0
  body: 'AIがデータベースを削除したりファイルを破壊したりする事故を防ぐため、多くの開発者は危険な操作のたびに許可確認を求める設定にしている。しかしこの方式は頻繁な割り込みで生産性を著しく下げる。


    結果として一部の開発者は権限チェックを完全に外し、AIに無制限の実行権限を与えてしまう。npmは毎週のように新しいセキュリティ脆弱性が報告される環境であり、AIを使うかどうかに関わらず悪意あるパッケージに引っかかりやすい状況が続いている。'
- heading: ネットワークポリシーで外部アクセスを制御する
  time: 1039
  body: '動画ではDocker Sandboxを使い、デフォルトで外部APIアクセスがロックされている状態を実演する。許可されていないサイトへのfetchはエラーになり、許可済みのページのみアクセス可能という設計だ。


    SBXのポリシーコマンドでネットワークポリシーの一覧表示や追加ができ、開発でよく使うサイト(パッケージリポジトリ、Figmaなど)をあらかじめ許可リストに登録しておく運用が紹介されている。グローバル許可と個別サンドボックス限定の許可を使い分けられる点も特徴だ。'
- heading: サンドボックスは業務の99%をカバーする日常インフラに
  time: 2141
  body: '動画の後半ではセットアップキットをGitHubに保存し再利用する方法も紹介されるが、筆者は「これが自分の日常業務の99%をカバーしている」と述べ、サンドボックス外でAIにコードを書かせることはもはやないと明言する。


    なお本編はDocker Sandboxのスポンサードコンテンツであり、紹介されている具体的な操作性やポリシー設計は同ツール固有の実装に基づく点には留意したい。'
editorial: この動画が突きつけるのは「許可確認 vs 無制限権限」という二択そのものが誤りだという指摘だ。エージェントの自律性を高めるほど、権限管理を個々の操作ではなく実行環境そのもの(サンドボックス)に委ねる設計が現実的になる。npmのサプライチェーン攻撃が常態化する中、ネットワークアクセスをホワイトリスト方式で制御する発想は、AIエージェント特有の問題というより従来からのセキュリティ原則の延長線上にある。ただし本編がスポンサード企画である点は差し引いて評価すべきで、同種の機能はDocker公式のsandboxやfirejailなど他の選択肢でも代替可能である点は留意したい。
en:
  articleTitle: 'Containers Alone Don''t Make Your AI Agent Safe: Sandboxing in the
    Age of Weekly npm Exploits'
  seoTitle: 'Containers Alone Don''t Make Your AI Agent Safe: Sandboxing in th'
  summary: To avoid AI wiping databases or destroying machines, most developers require
    permission prompts before any risky action.
  keyPhrases:
  - AI agents
  - sandboxing
  - Docker Sandbox
  - npm vulnerabilities
  - network policy
  - permission management
  bulletPoints:
  - time: 0
    text: To avoid AI wiping databases or destroying machines, most developers require
      permission prompts before any risky action.
  - time: 12
    text: Constant permission prompts kill productivity, pushing some developers to
      grant AI unrestricted access instead -- creating new risks.
  - time: 18
    text: npm sees a new security vulnerability nearly every week, with malicious
      packages designed to steal API keys and destroy systems.
  - time: 37
    text: The creator now sandboxes every task, including AI development, so agents
      can run with zero permission checks yet cause no real damage.
  - time: 1039
    text: By default, external API access is locked down, and fetch calls to non-allowlisted
      sites fail -- demonstrated live in the video.
  - time: 1070
    text: Network policies can be listed and added via simple commands, allowing specific
      sites to be permitted globally or per sandbox.
  - time: 2141
    text: The features shown cover 99% of the creator's daily usage, and he says he
      no longer writes AI-generated code outside a sandbox.
  sections:
  - heading: The False Choice Between Prompts and Unrestricted Access
    time: 0
    body: 'To prevent AI from deleting databases or wiping files, many developers
      require a permission prompt for every risky action. But those constant interruptions
      crush productivity.


      As a result, some developers swing to the other extreme, removing permission
      checks entirely and giving AI unrestricted access. Combined with npm''s near-weekly
      stream of new vulnerabilities and malicious packages, that unrestricted approach
      leaves systems exposed regardless of whether AI is involved.'
  - heading: Controlling Outbound Access With Network Policies
    time: 1039
    body: 'The video demonstrates Docker Sandbox with external API access locked down
      by default -- fetch requests to non-allowlisted domains simply fail. Only explicitly
      permitted destinations are reachable.


      Using the SBX policy commands, developers can list and add network policies,
      pre-approving commonly needed sites (package registries, Figma, and similar
      developer tools) either globally across all sandboxes or scoped to a single
      one.'
  - heading: Sandboxing Becomes Daily Infrastructure, Not a One-Off Setup
    time: 2141
    body: 'The later part of the video covers saving reusable setup kits to GitHub,
      but the creator''s core claim is that these features now cover 99% of his day-to-day
      workflow -- he no longer writes AI-generated code outside a sandbox.


      Worth noting: this segment is sponsored content for Docker Sandbox, so the specific
      tooling and policy design shown are particular to that product rather than universal.'
  editorial: The real insight here isn't about Docker Sandbox specifically -- it's
    that the choice between 'ask permission every time' and 'grant unrestricted access'
    is a false dichotomy. As agents become more autonomous, permission management
    shifts from individual actions to the execution environment itself. With npm supply-chain
    attacks now a near-weekly occurrence, allowlist-based network control isn't really
    an AI-specific innovation so much as a long-standing security principle finally
    being applied to agentic coding. Given this is sponsored content, teams should
    weigh Docker Sandbox against comparable options like Docker's own sandboxing or
    firejail before standardizing on one.
  headerImage: /images/7Z7ID5BbZU4/header.png
  heroImage: /images/7Z7ID5BbZU4/header.png
---

## ハイライト

- [00:00] AIがデータベースを削除したりコンピュータを破壊したりする事故を避けるため、多くの人は危険な操作の度に許可を求める設定にしている。
- [00:12] 許可待ちは生産性を大きく損なうため、逆に無制限にAIへ権限を与えてしまう人も多く、これが新たなリスクを生む。
- [00:18] npmでは毎週のように新たなセキュリティ脆弱性が見つかり、APIキー窃取やシステム破壊を狙う悪意あるパッケージが後を絶たない。
- [00:37] 筆者はAI開発を含む全ての作業でサンドボックスを使い、権限チェックなしでAIを走らせてもシステムに実害が及ばないようにしている。
- [17:19] デフォルトでは外部APIへのアクセスがロックされており、許可した特定サイト以外へのfetchはエラーになる仕組みを実演。
- [17:50] ネットワークポリシーをコマンドで追加・一覧表示でき、必要なサイトだけをグローバルまたは個別に許可できる。
- [35:41] 紹介した機能はDocker Sandboxの使用例の99%をカバーしており、今ではサンドボックス外でAIコードを書かないと明言。

## セクション

### 許可待ちか無制限権限か、という誤った二択

- 時刻: 00:00

AIがデータベースを削除したりファイルを破壊したりする事故を防ぐため、多くの開発者は危険な操作のたびに許可確認を求める設定にしている。しかしこの方式は頻繁な割り込みで生産性を著しく下げる。

結果として一部の開発者は権限チェックを完全に外し、AIに無制限の実行権限を与えてしまう。npmは毎週のように新しいセキュリティ脆弱性が報告される環境であり、AIを使うかどうかに関わらず悪意あるパッケージに引っかかりやすい状況が続いている。

### ネットワークポリシーで外部アクセスを制御する

- 時刻: 17:19

動画ではDocker Sandboxを使い、デフォルトで外部APIアクセスがロックされている状態を実演する。許可されていないサイトへのfetchはエラーになり、許可済みのページのみアクセス可能という設計だ。

SBXのポリシーコマンドでネットワークポリシーの一覧表示や追加ができ、開発でよく使うサイト(パッケージリポジトリ、Figmaなど)をあらかじめ許可リストに登録しておく運用が紹介されている。グローバル許可と個別サンドボックス限定の許可を使い分けられる点も特徴だ。

### サンドボックスは業務の99%をカバーする日常インフラに

- 時刻: 35:41

動画の後半ではセットアップキットをGitHubに保存し再利用する方法も紹介されるが、筆者は「これが自分の日常業務の99%をカバーしている」と述べ、サンドボックス外でAIにコードを書かせることはもはやないと明言する。

なお本編はDocker Sandboxのスポンサードコンテンツであり、紹介されている具体的な操作性やポリシー設計は同ツール固有の実装に基づく点には留意したい。

## 編集部の視点

この動画が突きつけるのは「許可確認 vs 無制限権限」という二択そのものが誤りだという指摘だ。エージェントの自律性を高めるほど、権限管理を個々の操作ではなく実行環境そのもの(サンドボックス)に委ねる設計が現実的になる。npmのサプライチェーン攻撃が常態化する中、ネットワークアクセスをホワイトリスト方式で制御する発想は、AIエージェント特有の問題というより従来からのセキュリティ原則の延長線上にある。ただし本編がスポンサード企画である点は差し引いて評価すべきで、同種の機能はDocker公式のsandboxやfirejailなど他の選択肢でも代替可能である点は留意したい。
