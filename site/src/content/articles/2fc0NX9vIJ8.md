---
videoId: 2fc0NX9vIJ8
title: How to Build A Self-Improving System with Claude Code
slug: claude-code-で自己改善システムを作る5ステップ-austin-marchese-の-2fc0nx9vij8
articleTitle: Claude Code で自己改善システムを作る5ステップ — Austin Marchese の Karpathy×Anthropic
  統合フレームワーク
seoTitle: Claude Code で自己改善システムを作る5ステップ — Austin Marchese の Karpathy×Anthr
summary: Austin Marchese は Andrej Karpathy と Anthropic の知見を統合した自己改善システムの5ステップを公開する。何百人にも同じ設計を教えてきた経験を踏まえ、誰でも実装できる形まで落とし込んだ実装ガイド。
channel: Austin Marchese
channelId: UCFeFVytEkT8kaqPCJZGFswg
publishedAt: '2026-06-28T14:15:20Z'
fetchedAt: '2026-06-30T12:28:42.794042Z'
originalThumbnail: https://i.ytimg.com/vi/2fc0NX9vIJ8/maxresdefault.jpg
headerImage: /images/2fc0NX9vIJ8/header.ja.png
heroImage: /images/2fc0NX9vIJ8/header.ja.png
viewCount: 25018
durationSec: 1007
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Karpathy LLM ナレッジベース
- raw/wiki フォルダ構造
- claude.md による規約強制
- Sync curated content スキル
- Periodic data dumps via Whisper
- Action produces information 原則
bulletPoints:
- time: 0
  text: Austin Marchese は Andrej Karpathy と Anthropic の知見を統合した自己改善システムの5ステップを公開する。何百人にも同じ設計を教えてきた経験を踏まえ、誰でも実装できる形まで落とし込んだ実装ガイド。
- time: 21
  text: ステップ1は『Base』。改善のための土台を作るフェーズ。プロジェクトを1つ立ち上げ、データを蓄積して時系列で価値を伸ばす器を用意する。中身はナレッジベースとスキルの2つ。
- time: 35
  text: Karpathy がバイラルさせた『LLM ナレッジベース』のコンセプトを基盤に置く。raw フォルダに通話記録など生資源を蓄積し、wiki フォルダで
    raw への参照を保持して AI が情報を素早く見つけられるようにする。
- time: 64
  text: claude.md ファイルで構造を明文化し、一貫した参照ルールを Claude Code に強制する。これがプロジェクト全体の一貫性を維持する仕組みになる。
- time: 462
  text: メールから情報を取り込むパイプラインでは alias domain を使って特定の発信源を分類しやすくする工夫を共有。Austin のニュースレター購読も同じパイプラインで処理されるよう設計されている。
- time: 481
  text: 情報取り込みを駆動するのが sync curated content スキル。alias inbox からニュースレターを引き、各メールから要点を抽出し、wiki
    に処理して入れる。少なく高品質な情報源だけを意図的に選ぶことが要点。
- time: 508
  text: パイプライン4は periodic data dumps。1日や1週の終わりに学んだことを音声で吐き出し、Whisper Flow などで Claude
    Code に取り込む。生の経験を構造化された知識へ変換するルーティン。
- time: 977
  text: 最終ルールは『Action produces information』(Brian Armstrong のフレーズ)。少なすぎる試行と多すぎる分析のどちらが致命的かと言えば、後者だ、と
    Austin は強調する。反復が設計を磨く。
sections:
- heading: Base ステップ — Karpathy 流ナレッジベースを Claude Code に据える
  time: 0
  body: 'Austin Marchese は Andrej Karpathy と Anthropic の知見を統合した自己改善システムの5ステップを公開する。動画は何百人にも同じ設計を教えてきた経験を背景に、再現性のある実装ガイドとして組まれている。


    ステップ1は『Base』だ。改善のための土台を作るフェーズで、プロジェクトを1つ立ち上げ、データを蓄積して時系列で価値を伸ばす器を用意する。中身は2つに分かれる。一つ目はナレッジベース。Karpathy
    がバイラルさせた『LLM ナレッジベース』のコンセプトをそのまま採用し、raw フォルダに通話記録など生資源を蓄積、wiki フォルダで raw への参照を持って
    AI が情報を素早く見つけられる構造にする。本の目次のような役割だ。二つ目はスキル。設計を強制する claude.md ファイルでプロジェクト全体の一貫した参照ルールを明文化する。Claude
    Code に対する『どの順で何を読むか』の規約として機能する。'
- heading: Sync パイプラインと periodic data dumps — 情報源を狭く深く保つ
  time: 462
  body: '中盤では情報を取り込むパイプラインが具体的に示される。メールからの取り込みでは alias domain を使って特定の発信源を分類しやすくする工夫を共有する。Austin
    のニュースレター購読も同じパイプラインで処理されるよう設計されている。


    駆動役は sync curated content スキルだ。alias inbox からニュースレターを引き、各メールから要点を抽出し、wiki に処理して入れる。設計上の要点は『少なく高品質な情報源だけを意図的に選ぶ』こと。情報源を増やすと出力が薄まる、と明確に警告する。パイプライン4の
    periodic data dumps は別の発想で、1日や1週の終わりに学んだことを Whisper Flow で音声入力し、add new resource
    スキルに渡して取り込む。自分の経験という最強の情報源を構造化された知識へ変換する仕組みだ。'
- heading: Action produces information — 反復が設計を磨く
  time: 931
  body: '終盤では運用ルールが整理される。スキルが期待通り動かなかったら、その会話を踏まえて『この会話を元にスキルを改善して』と一言追加するだけでよい。自動改善を待たずに手動で押し進めることがシステムの推進力になる。


    そして最終ルールが『Action produces information』だ。これは Coinbase の Brian Armstrong の言葉で、Austin
    はこれを動画の核に置く。raw/inputs と raw/sessions のどちらがいいか、午前6時か9時か。こうした細部の最適化は無意味で、『過剰に考えること』だけが本当の間違いだと断じる。AI
    は十分に強力だから、まず使って構築せよ。システムはホワイトボード会議ではなく反復で磨かれる。動画の締めもこの主題に揃っている。やってみることが情報を生む、その情報が次の判断を確かにする。'
editorial: Austin の5ステップが示すのは『AI に何を頼むか』ではなく『AI に何を継続的に渡し続けるか』という設計思考の変化だ。これは Claude
  Tag や Notion 常駐エージェントが企業スケールでやろうとしていることを、個人スケールで再現する設計図と読める。読者にとっての具体的な含意は二つある。第一に、自己改善システムは『すごい仕組み』を作ることではなく『継続して情報を流し込む配管』を整えることが本質で、初期セットアップに過剰な時間を使うよりも
  raw/wiki/skills の最小構成を立ち上げて稼働させるほうが早く価値が出る。第二に、Brian Armstrong の『Action produces
  information』というメタルールは、AI システム設計に限らない汎用的な指針で、不確実な判断を抱え込むより小さく動かして学習することが今期の AI ツール群の正しい使い方になる。完璧な設計を待たず、反復で磨くという姿勢自体が、エージェント時代の最も価値のある実務スキルだ。
en:
  articleTitle: A Five-Step Framework for Building a Self-Improving System with Claude
    Code — Austin Marchese's Karpathy x Anthropic Synthesis
  seoTitle: A Five-Step Framework for Building a Self-Improving System with
  summary: Austin Marchese publishes a five-step self-improving-system framework that
    synthesizes Andrej Karpathy's work and the…
  keyPhrases:
  - Karpathy LLM knowledge base
  - Raw/wiki folder structure
  - claude.md as protocol enforcer
  - Sync curated content skill
  - Periodic data dumps via Whisper
  - Action produces information
  bulletPoints:
  - time: 0
    text: Austin Marchese publishes a five-step self-improving-system framework that
      synthesizes Andrej Karpathy's work and the Anthropic team's approach. Refined
      by teaching hundreds of people the same design, it's an implementation guide
      anyone can build.
  - time: 21
    text: 'Step 1 is Base. The phase that builds the foundation for improvement. Set
      up one project, create a container where data accumulates and value compounds
      over time. The container has two parts: a knowledge base and skills.'
  - time: 35
    text: The foundation borrows directly from Karpathy's viral 'LLM knowledge base'
      concept. A raw folder holds raw resources like call transcripts; a wiki folder
      holds references into raw, so the AI can locate information quickly — like a
      book's table of contents.
  - time: 64
    text: The claude.md file makes the structure explicit and enforces consistent
      reference rules on Claude Code. This is the mechanism that keeps the project
      consistent across sessions.
  - time: 462
    text: The email pipeline uses an alias domain to make filtering by sender easy.
      Austin's own newsletter subscription is processed through the same pipeline
      so the design is consistent.
  - time: 481
    text: What drives ingestion is the 'sync curated content' skill. It pulls newsletters
      from the alias inbox, extracts the key claims from each one, and processes them
      into the wiki. The discipline is to deliberately choose only a few high-quality
      sources.
  - time: 508
    text: Pipeline 4 is periodic data dumps. At the end of a day or a week, you voice-dump
      what you learned via Whisper Flow into Claude Code. The routine converts raw
      lived experience into structured knowledge.
  - time: 977
    text: The final rule is 'Action produces information' (a Brian Armstrong line).
      Of the two failure modes — too few attempts vs. too much analysis — the latter
      is the fatal one, Austin stresses. Reps sharpen the design.
  sections:
  - heading: The Base Step — Plant a Karpathy-Style Knowledge Base in Claude Code
    time: 0
    body: 'Austin Marchese publishes a five-step self-improving-system framework synthesizing
      Andrej Karpathy''s work and the Anthropic team''s approach. The video reflects
      experience teaching hundreds of people the same design and is structured as
      a reproducible implementation guide.


      Step 1 is Base. This phase builds the foundation for improvement. Set up one
      project and create a container where data accumulates and value compounds over
      time. The container splits into two. The first is the knowledge base — adopt
      Karpathy''s viral ''LLM knowledge base'' concept directly. A raw folder holds
      raw resources like call transcripts; a wiki folder holds references into raw
      so the AI can locate information quickly, in the role of a book''s table of
      contents. The second is skills. The claude.md file explicitly enforces consistent
      reference rules on Claude Code — it functions as the protocol for ''what to
      read in what order.'''
  - heading: Sync Pipelines and Periodic Data Dumps — Keep Sources Narrow and Deep
    time: 462
    body: 'The middle of the video specifies the ingestion pipelines. The email pipeline
      uses an alias domain to make filtering by sender easy. Austin''s own newsletter
      subscription is processed through the same pipeline, so the design pattern stays
      consistent.


      The driver is the ''sync curated content'' skill — it pulls newsletters from
      the alias inbox, extracts key claims from each, and processes them into the
      wiki. The design discipline is to deliberately choose only a few high-quality
      sources. He''s explicit: adding more sources dilutes the output. Pipeline 4
      is a different shape — periodic data dumps. At the end of a day or week, voice-dump
      what you learned via Whisper Flow and hand it to the add-new-resource skill.
      It''s a way of converting your own experience — the strongest possible information
      source — into structured knowledge.'
  - heading: Action Produces Information — Reps Sharpen the Design
    time: 931
    body: 'The closing section organizes the operating rules. If a skill didn''t work
      the way you wanted, just say ''based on this conversation, improve this skill.''
      Pushing it forward manually, rather than waiting for auto-improvement, is what
      gives the system its momentum.


      And the final rule is ''Action produces information'' — a Brian Armstrong line,
      which Austin places at the heart of the video. Whether to use raw/inputs or
      raw/sessions, 6 a.m. or 9 a.m. — these micro-optimizations are meaningless,
      and overthinking is the only genuinely wrong choice. AI is plenty strong already;
      just use it and build. Systems sharpen through reps, not whiteboard sessions.
      The closing mirrors the message: doing produces information, which makes the
      next decision sharper.'
  editorial: 'The shift Austin''s five steps represent isn''t ''what to ask the AI''
    but ''what to keep feeding the AI continuously.'' Read this way, it''s a personal-scale
    blueprint for what Claude Tag and Notion-resident agents are doing at company
    scale. Two concrete implications. First, a self-improving system isn''t about
    building something impressive — it''s about laying down the pipes that keep information
    flowing. Spending excess time on initial setup is the wrong move; standing up
    the minimum raw/wiki/skills configuration and getting it running produces value
    faster. Second, Brian Armstrong''s ''Action produces information'' meta-rule is
    a general guide not specific to AI: small, fast moves are the right use of today''s
    AI tools, especially when you''re carrying an uncertain decision. Refusing to
    wait for the perfect design and sharpening it through iteration is one of the
    most valuable practical skills of the agent era.'
  headerImage: /images/2fc0NX9vIJ8/header.png
  heroImage: /images/2fc0NX9vIJ8/header.png
---

## ハイライト

- [00:00] Austin Marchese は Andrej Karpathy と Anthropic の知見を統合した自己改善システムの5ステップを公開する。何百人にも同じ設計を教えてきた経験を踏まえ、誰でも実装できる形まで落とし込んだ実装ガイド。
- [00:21] ステップ1は『Base』。改善のための土台を作るフェーズ。プロジェクトを1つ立ち上げ、データを蓄積して時系列で価値を伸ばす器を用意する。中身はナレッジベースとスキルの2つ。
- [00:35] Karpathy がバイラルさせた『LLM ナレッジベース』のコンセプトを基盤に置く。raw フォルダに通話記録など生資源を蓄積し、wiki フォルダで raw への参照を保持して AI が情報を素早く見つけられるようにする。
- [01:04] claude.md ファイルで構造を明文化し、一貫した参照ルールを Claude Code に強制する。これがプロジェクト全体の一貫性を維持する仕組みになる。
- [07:42] メールから情報を取り込むパイプラインでは alias domain を使って特定の発信源を分類しやすくする工夫を共有。Austin のニュースレター購読も同じパイプラインで処理されるよう設計されている。
- [08:01] 情報取り込みを駆動するのが sync curated content スキル。alias inbox からニュースレターを引き、各メールから要点を抽出し、wiki に処理して入れる。少なく高品質な情報源だけを意図的に選ぶことが要点。
- [08:28] パイプライン4は periodic data dumps。1日や1週の終わりに学んだことを音声で吐き出し、Whisper Flow などで Claude Code に取り込む。生の経験を構造化された知識へ変換するルーティン。
- [16:17] 最終ルールは『Action produces information』(Brian Armstrong のフレーズ)。少なすぎる試行と多すぎる分析のどちらが致命的かと言えば、後者だ、と Austin は強調する。反復が設計を磨く。

## セクション

### Base ステップ — Karpathy 流ナレッジベースを Claude Code に据える

- 時刻: 00:00

Austin Marchese は Andrej Karpathy と Anthropic の知見を統合した自己改善システムの5ステップを公開する。動画は何百人にも同じ設計を教えてきた経験を背景に、再現性のある実装ガイドとして組まれている。

ステップ1は『Base』だ。改善のための土台を作るフェーズで、プロジェクトを1つ立ち上げ、データを蓄積して時系列で価値を伸ばす器を用意する。中身は2つに分かれる。一つ目はナレッジベース。Karpathy がバイラルさせた『LLM ナレッジベース』のコンセプトをそのまま採用し、raw フォルダに通話記録など生資源を蓄積、wiki フォルダで raw への参照を持って AI が情報を素早く見つけられる構造にする。本の目次のような役割だ。二つ目はスキル。設計を強制する claude.md ファイルでプロジェクト全体の一貫した参照ルールを明文化する。Claude Code に対する『どの順で何を読むか』の規約として機能する。

### Sync パイプラインと periodic data dumps — 情報源を狭く深く保つ

- 時刻: 07:42

中盤では情報を取り込むパイプラインが具体的に示される。メールからの取り込みでは alias domain を使って特定の発信源を分類しやすくする工夫を共有する。Austin のニュースレター購読も同じパイプラインで処理されるよう設計されている。

駆動役は sync curated content スキルだ。alias inbox からニュースレターを引き、各メールから要点を抽出し、wiki に処理して入れる。設計上の要点は『少なく高品質な情報源だけを意図的に選ぶ』こと。情報源を増やすと出力が薄まる、と明確に警告する。パイプライン4の periodic data dumps は別の発想で、1日や1週の終わりに学んだことを Whisper Flow で音声入力し、add new resource スキルに渡して取り込む。自分の経験という最強の情報源を構造化された知識へ変換する仕組みだ。

### Action produces information — 反復が設計を磨く

- 時刻: 15:31

終盤では運用ルールが整理される。スキルが期待通り動かなかったら、その会話を踏まえて『この会話を元にスキルを改善して』と一言追加するだけでよい。自動改善を待たずに手動で押し進めることがシステムの推進力になる。

そして最終ルールが『Action produces information』だ。これは Coinbase の Brian Armstrong の言葉で、Austin はこれを動画の核に置く。raw/inputs と raw/sessions のどちらがいいか、午前6時か9時か。こうした細部の最適化は無意味で、『過剰に考えること』だけが本当の間違いだと断じる。AI は十分に強力だから、まず使って構築せよ。システムはホワイトボード会議ではなく反復で磨かれる。動画の締めもこの主題に揃っている。やってみることが情報を生む、その情報が次の判断を確かにする。

## 編集部の視点

Austin の5ステップが示すのは『AI に何を頼むか』ではなく『AI に何を継続的に渡し続けるか』という設計思考の変化だ。これは Claude Tag や Notion 常駐エージェントが企業スケールでやろうとしていることを、個人スケールで再現する設計図と読める。読者にとっての具体的な含意は二つある。第一に、自己改善システムは『すごい仕組み』を作ることではなく『継続して情報を流し込む配管』を整えることが本質で、初期セットアップに過剰な時間を使うよりも raw/wiki/skills の最小構成を立ち上げて稼働させるほうが早く価値が出る。第二に、Brian Armstrong の『Action produces information』というメタルールは、AI システム設計に限らない汎用的な指針で、不確実な判断を抱え込むより小さく動かして学習することが今期の AI ツール群の正しい使い方になる。完璧な設計を待たず、反復で磨くという姿勢自体が、エージェント時代の最も価値のある実務スキルだ。
