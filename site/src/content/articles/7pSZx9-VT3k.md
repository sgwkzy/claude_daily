---
videoId: 7pSZx9-VT3k
title: Token消耗减少120倍？Codebase-Memory-MCP的性能突破原理解析
slug: token消費を120倍削減codebase-memory-mcpが変えるaiコーディングのコスト構造-7pszx9-vt3k
articleTitle: Token消費を120倍削減？Codebase-Memory-MCPが変えるAIコーディングのコスト構造
seoTitle: Token消費を120倍削減？Codebase-Memory-MCPが変えるAIコーディングのコスト構造
summary: GitHubで話題のCodebase-Memory-MCPは単一バイナリでコードベース全体を知識グラフに変換し、Tokenコストの構造そのものを変えようとしている。
channel: 为什么叫QQ
channelId: UClkMmnf9yOKbYRMfOv1HvwA
publishedAt: '2026-07-04T12:15:36Z'
fetchedAt: '2026-07-06T11:50:40.299596Z'
originalThumbnail: https://i.ytimg.com/vi/7pSZx9-VT3k/maxresdefault.jpg
headerImage: /images/7pSZx9-VT3k/header.ja.png
heroImage: /images/7pSZx9-VT3k/header.ja.png
viewCount: 4144
durationSec: 587
sourceLanguage: zh-Hans
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Codebase-Memory-MCP
- MCP
- Token削減
- コードグラフ
- Claude Code
- AIコーディングコスト
bulletPoints:
- time: 16
  text: GitHubで話題のCodebase-Memory-MCPは単一バイナリでコードベース全体を知識グラフに変換し、Tokenコストの構造そのものを変えようとしている。
- time: 30
  text: 論文評価ではToken消費が約10倍削減、ツール呼び出し回数が2.1倍削減され、READMEに記載の120倍は5つの構造クエリに関するマイクロベンチマークの数値だという。
- time: 73
  text: 類似プロジェクトのCodeGraphはGitHubスター数で上回るが、最近はCodebase-Memory-MCPへの注目度が急速に高まっている。
- time: 100
  text: 現状のCursorやClaude Codeは、コードベース理解のためgrepやファイル読み込みを繰り返す『手探り』状態で数十万トークンを消費してしまう。
- time: 263
  text: Codebase-Memory-MCPは外部のLanguage Serverに依存せず、C言語で軽量なシンボル・型解析を自前実装し、Python・TypeScript・Go・Javaなど複数言語に対応する。
- time: 323
  text: 知識グラフを圧縮スナップショット(graph.db.zst)としてGitリポジトリに直接コミットでき、新メンバーは再インデックス不要で即座にプロジェクト全体の記憶を得られる。
- time: 500
  text: AI基盤の周辺インフラは軽量化が必須であり、C/C++やRustによる書き換えが今後標準になっていくと予測される。
sections:
- heading: 『120倍』の数字の正しい読み方
  time: 16
  body: 'GitHubで話題のCodebase-Memory-MCPは、単一バイナリでコードベース全体を知識グラフに変換するツールだ。論文評価ではToken消費が約10倍削減、ツール呼び出し回数が2.1倍削減されるとされる。話題になっているREADMEの『120倍』という数字は、5つの構造クエリに関するマイクロベンチマークで約3400トークンが約412,000トークンを代替したという特定条件下の数値であり、すべてのタスクに一律で当てはまるわけではないと釘を刺す。


    類似プロジェクトのCodeGraphはGitHubスター数（57.3k対25.5k）で上回るものの、最近はCodebase-Memory-MCPへの注目度が急速に高まっている。両者はTree-sitterでASTを解析しSQLiteに保存しMCPインターフェースを提供する点は共通だが、性能・デプロイ形態を重視する路線と、Agentワークフロー・エコシステム拡張を重視する路線とで異なる方向に進んでいる。'
- heading: 外部LSP不要の軽量シンボル解析
  time: 263
  body: '現状のCursorやClaude Codeは、コードベースを理解するためgrepやファイル読み込みを繰り返す『手探り』状態にあり、1つの関数呼び出しを探すのに十数個のファイルを行き来して数十万トークンを消費してしまう。CodeGraphは工学的な解析ルールとフレームワーク対応（ルーティング識別、動的ディスパッチなど）を重視する実用的な路線だが、新しいフレームワークや言語仕様が増えるたびにルール保守コストが増大する。


    一方Codebase-Memory-MCPは、外部のLanguage Serverに依存せず、C言語で軽量なシンボル・型解析を自前実装しており、Python・TypeScript・Go・Javaなど複数言語ファミリーの呼び出し・インポート・継承関係を認識できる。これにより『このインターフェースは誰が呼んでいるか』という問いに対し、シンボルレベル・ファイルレベル・行番号レベルの正確な回答を返せるようになり、情報密度が上がりノイズが減る。'
- heading: 知識グラフをGitでコミットする、という発想
  time: 323
  body: 'CodeGraphは知識グラフをローカルキャッシュとして扱い、開発者ごとにローカルでインデックスを再計算する必要がある。対してCodebase-Memory-MCPは知識グラフを『コード資産』として扱い、zstd圧縮したスナップショット(graph.db.zst、圧縮率約8〜13倍)を直接Gitリポジトリにコミットできる設計を採用した。新メンバーがコードをプルすれば、数時間の再インデックスを待たずにスナップショットを読み込むだけでプロジェクト全体の記憶を即座に得られる。


    大規模言語モデル自体の推論コストが既にボトルネックとなっている今、周辺インフラの軽量化・高効率化は必須条件になりつつあり、C/C++やRustによる書き換えが今後標準になっていくと予測されている。将来的には`package.json`や`requirements.txt`のように、リポジトリに`.graph.db`のような標準化された知識グラフファイルが当たり前に存在するようになるとも述べられている。'
editorial: この解説が示唆するのは、AIコーディングツールのボトルネックが『モデルの賢さ』から『周辺インフラの効率』へと徐々に移りつつあるという構造変化だ。知識グラフをGitにコミットしてチームで共有するという発想は、計算コストを個々の開発者が繰り返し払う仕組みから、一度計算して資産化する仕組みへの転換を意味する。特に、リファクタリングが『人力の悪夢』から『計算可能な問題』へ変わるという指摘は、数百万行規模のレガシーコードベースを抱える組織にとって重要な意味を持つ。動画が最後に問いかける『ファイルを漁らせるか、知識グラフを持たせるか』という選択は、AIコーディングツールの導入コストを左右する実務的な判断軸として、今後さらに注目されていくだろう。
en:
  articleTitle: A 120x Token Reduction? How Codebase-Memory-MCP Is Rewriting the Economics
    of AI Coding
  seoTitle: A 120x Token Reduction? How Codebase-Memory-MCP Is Rewriting the
  summary: Codebase-Memory-MCP, trending on GitHub, turns an entire codebase into
    a knowledge graph via a single binary, aiming…
  keyPhrases:
  - Codebase-Memory-MCP
  - MCP
  - token reduction
  - code graph
  - Claude Code
  - AI coding cost
  bulletPoints:
  - time: 16
    text: Codebase-Memory-MCP, trending on GitHub, turns an entire codebase into a
      knowledge graph via a single binary, aiming to reshape the underlying token
      cost structure.
  - time: 30
    text: Its paper reports roughly a 10x reduction in tokens and a 2.1x reduction
      in tool calls; the '120x' figure from the README comes from a micro-benchmark
      on five structural queries.
  - time: 73
    text: The similar project CodeGraph has more GitHub stars, but attention has been
      shifting rapidly toward Codebase-Memory-MCP recently.
  - time: 100
    text: Tools like Cursor or Claude Code today understand a codebase by repeatedly
      grepping and reading files -- a 'blind groping' process that can burn hundreds
      of thousands of tokens.
  - time: 263
    text: Codebase-Memory-MCP implements lightweight symbol and type resolution in
      C itself, with no dependency on an external Language Server, covering Python,
      TypeScript, Go, Java, and more.
  - time: 323
    text: Its knowledge graph can be committed straight into a Git repo as a compressed
      snapshot (graph.db.zst), so new team members get instant project memory without
      re-indexing.
  - time: 500
    text: As inference cost becomes the bottleneck, surrounding AI infrastructure
      will need to get radically lighter -- expect more of it rewritten in C/C++ or
      Rust going forward.
  sections:
  - heading: Reading the '120x' Number Correctly
    time: 16
    body: 'Codebase-Memory-MCP, trending on GitHub, converts an entire codebase into
      a knowledge graph via a single binary. Its published evaluation shows roughly
      a 10x reduction in token usage and a 2.1x reduction in tool calls. The widely-cited
      ''120x'' figure from the README comes from a narrower micro-benchmark on five
      structural queries, where about 3,400 tokens replaced roughly 412,000 -- an
      impressive result, but not something that generalizes to every task.


      The similar project CodeGraph leads on GitHub stars (57.3k vs. 25.5k), yet attention
      has been shifting rapidly toward Codebase-Memory-MCP. Both parse ASTs via Tree-sitter,
      store results in SQLite, and expose an MCP interface -- but they''ve taken different
      paths, one prioritizing performance and deployment form factor, the other prioritizing
      agent workflows and ecosystem expansion.'
  - heading: Lightweight Symbol Resolution With No External LSP
    time: 263
    body: 'Tools like Cursor or Claude Code today understand a codebase by repeatedly
      grepping and reading files -- a blind-groping process where finding one function
      call can mean jumping through a dozen files and burning hundreds of thousands
      of tokens. CodeGraph takes a practical, engineering-heavy route -- solid parsing
      rules and framework adaptation (route recognition, dynamic dispatch, and so
      on) -- but maintenance costs climb every time a new framework or complex language
      semantic gets added.


      Codebase-Memory-MCP instead implements lightweight symbol and type resolution
      in C itself, with no external Language Server dependency, covering call, import,
      and inheritance relationships across Python, TypeScript, Go, Java, and more.
      That means when asked ''who calls this interface,'' it can return symbol-level,
      file-level, line-level answers -- higher information density, less noise, and
      a smaller context for the AI to process.'
  - heading: Committing a Knowledge Graph to Git
    time: 323
    body: 'CodeGraph treats its knowledge graph as a local cache, requiring each developer
      to re-run indexing locally. Codebase-Memory-MCP instead treats the graph as
      a code asset: it supports a zstd-compressed snapshot (graph.db.zst, roughly
      8-13x compression) that can be committed straight into the Git repo. A new hire
      pulling the repo gets instant access to full project memory just by loading
      the snapshot -- no hours-long re-indexing.


      With large-model inference cost already the bottleneck, the surrounding infrastructure
      has to become radically lighter and more efficient -- expect more of it rewritten
      in C/C++ or Rust going forward. The prediction: future repositories will routinely
      carry a standardized knowledge-graph file, much like package.json or requirements.txt
      today.'
  editorial: What this breakdown suggests is that the bottleneck for AI coding tools
    is gradually shifting from 'how smart the model is' to 'how efficient the surrounding
    infrastructure is.' Committing a knowledge graph to Git so a team can share it
    marks a shift from every developer repeatedly paying the same compute cost to
    computing it once and treating it as a shared asset. The claim that refactoring
    turns from a 'human nightmare' into a 'computable problem' matters most for organizations
    sitting on million-line legacy codebases. The video's closing question -- let
    the AI grope through files, or give it a knowledge graph -- is a practical framing
    worth revisiting as more teams evaluate the true cost of AI-assisted coding.
  headerImage: /images/7pSZx9-VT3k/header.png
  heroImage: /images/7pSZx9-VT3k/header.png
---

## ハイライト

- [00:16] GitHubで話題のCodebase-Memory-MCPは単一バイナリでコードベース全体を知識グラフに変換し、Tokenコストの構造そのものを変えようとしている。
- [00:30] 論文評価ではToken消費が約10倍削減、ツール呼び出し回数が2.1倍削減され、READMEに記載の120倍は5つの構造クエリに関するマイクロベンチマークの数値だという。
- [01:13] 類似プロジェクトのCodeGraphはGitHubスター数で上回るが、最近はCodebase-Memory-MCPへの注目度が急速に高まっている。
- [01:40] 現状のCursorやClaude Codeは、コードベース理解のためgrepやファイル読み込みを繰り返す『手探り』状態で数十万トークンを消費してしまう。
- [04:23] Codebase-Memory-MCPは外部のLanguage Serverに依存せず、C言語で軽量なシンボル・型解析を自前実装し、Python・TypeScript・Go・Javaなど複数言語に対応する。
- [05:23] 知識グラフを圧縮スナップショット(graph.db.zst)としてGitリポジトリに直接コミットでき、新メンバーは再インデックス不要で即座にプロジェクト全体の記憶を得られる。
- [08:20] AI基盤の周辺インフラは軽量化が必須であり、C/C++やRustによる書き換えが今後標準になっていくと予測される。

## セクション

### 『120倍』の数字の正しい読み方

- 時刻: 00:16

GitHubで話題のCodebase-Memory-MCPは、単一バイナリでコードベース全体を知識グラフに変換するツールだ。論文評価ではToken消費が約10倍削減、ツール呼び出し回数が2.1倍削減されるとされる。話題になっているREADMEの『120倍』という数字は、5つの構造クエリに関するマイクロベンチマークで約3400トークンが約412,000トークンを代替したという特定条件下の数値であり、すべてのタスクに一律で当てはまるわけではないと釘を刺す。

類似プロジェクトのCodeGraphはGitHubスター数（57.3k対25.5k）で上回るものの、最近はCodebase-Memory-MCPへの注目度が急速に高まっている。両者はTree-sitterでASTを解析しSQLiteに保存しMCPインターフェースを提供する点は共通だが、性能・デプロイ形態を重視する路線と、Agentワークフロー・エコシステム拡張を重視する路線とで異なる方向に進んでいる。

### 外部LSP不要の軽量シンボル解析

- 時刻: 04:23

現状のCursorやClaude Codeは、コードベースを理解するためgrepやファイル読み込みを繰り返す『手探り』状態にあり、1つの関数呼び出しを探すのに十数個のファイルを行き来して数十万トークンを消費してしまう。CodeGraphは工学的な解析ルールとフレームワーク対応（ルーティング識別、動的ディスパッチなど）を重視する実用的な路線だが、新しいフレームワークや言語仕様が増えるたびにルール保守コストが増大する。

一方Codebase-Memory-MCPは、外部のLanguage Serverに依存せず、C言語で軽量なシンボル・型解析を自前実装しており、Python・TypeScript・Go・Javaなど複数言語ファミリーの呼び出し・インポート・継承関係を認識できる。これにより『このインターフェースは誰が呼んでいるか』という問いに対し、シンボルレベル・ファイルレベル・行番号レベルの正確な回答を返せるようになり、情報密度が上がりノイズが減る。

### 知識グラフをGitでコミットする、という発想

- 時刻: 05:23

CodeGraphは知識グラフをローカルキャッシュとして扱い、開発者ごとにローカルでインデックスを再計算する必要がある。対してCodebase-Memory-MCPは知識グラフを『コード資産』として扱い、zstd圧縮したスナップショット(graph.db.zst、圧縮率約8〜13倍)を直接Gitリポジトリにコミットできる設計を採用した。新メンバーがコードをプルすれば、数時間の再インデックスを待たずにスナップショットを読み込むだけでプロジェクト全体の記憶を即座に得られる。

大規模言語モデル自体の推論コストが既にボトルネックとなっている今、周辺インフラの軽量化・高効率化は必須条件になりつつあり、C/C++やRustによる書き換えが今後標準になっていくと予測されている。将来的には`package.json`や`requirements.txt`のように、リポジトリに`.graph.db`のような標準化された知識グラフファイルが当たり前に存在するようになるとも述べられている。

## 編集部の視点

この解説が示唆するのは、AIコーディングツールのボトルネックが『モデルの賢さ』から『周辺インフラの効率』へと徐々に移りつつあるという構造変化だ。知識グラフをGitにコミットしてチームで共有するという発想は、計算コストを個々の開発者が繰り返し払う仕組みから、一度計算して資産化する仕組みへの転換を意味する。特に、リファクタリングが『人力の悪夢』から『計算可能な問題』へ変わるという指摘は、数百万行規模のレガシーコードベースを抱える組織にとって重要な意味を持つ。動画が最後に問いかける『ファイルを漁らせるか、知識グラフを持たせるか』という選択は、AIコーディングツールの導入コストを左右する実務的な判断軸として、今後さらに注目されていくだろう。
