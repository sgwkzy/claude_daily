---
videoId: 1zaA6QlRScg
title: How I Control Home Assistant with Hermes Agent
slug: hermes-agentでhome-assistantを動かす-エージェントとはモデルではなくハーネスである-1zaa6qlrscg
articleTitle: Hermes AgentでHome Assistantを動かす — エージェントとはモデルではなくハーネスである
seoTitle: Hermes AgentでHome Assistantを動かす — エージェントとはモデルではなくハーネスである
summary: Tailscaleの動画は、Hermesというセルフホスト可能なAIエージェントでHome Assistantを操作する実験から始まる。
channel: Tailscale
channelId: UCcdv38QxPjSMqbt5ffLhJLA
publishedAt: '2026-06-26T15:19:02Z'
fetchedAt: '2026-06-28T12:02:05.722278Z'
originalThumbnail: https://i.ytimg.com/vi/1zaA6QlRScg/maxresdefault.jpg
headerImage: /images/1zaA6QlRScg/header.ja.png
heroImage: /images/1zaA6QlRScg/header.ja.png
viewCount: 6213
durationSec: 592
sourceLanguage: en
matchedKeywords:
- AIエージェント
proposedByLLM: false
keyPhrases:
- Hermes Agent
- Home Assistant
- Tailscale
- エージェントハーネス
- ツール権限
- サンドボックス
bulletPoints:
- time: 0
  text: Tailscaleの動画は、Hermesというセルフホスト可能なAIエージェントでHome Assistantを操作する実験から始まる。
- time: 20
  text: 投稿者は、agent、harness、runtime、tool access、memory、sandboxなどの用語が混乱していると認め、ノイズを減らして説明すると宣言する。
- time: 260
  text: 重要なのはモデル単体ではなく、モデルに渡すツール、権限、サンドボックス、ループを管理する周辺システムだ。
- time: 430
  text: ハーネスまたはランタイムは、プロンプトの組み立て、利用可能ツール、エージェントループ、実行制御を担う層として説明される。
- time: 980
  text: 結論では、エージェントは魔法でも新種のモデルでもなく、通常のモデルをコンテキストとツールへ接続するラッパーだと整理される。
sections:
- heading: Home Assistant実験から、エージェント用語をほどく
  time: 0
  body: 'Tailscaleの動画は、Hermesというセルフホスト可能なAIエージェントを使ってHome Assistantを操作する話から入る。ただし主題はスマートホームだけではない。投稿者は、agent、harness、runtime、tool
    access、memory、sandboxといった言葉が混ざりすぎていると認め、実際に何が起きているのかを整理しようとする。


    これはClaude CodeやMCPを使う読者にも近い話だ。エージェントという言葉は派手だが、多くの場合、モデルそのものではなく、モデルを囲む実行環境の設計を指している。'
- heading: ツール、権限、サンドボックスが失敗時の被害を決める
  time: 260
  body: '動画の中核は、モデルに何をさせるかではなく、何へアクセスさせ、どこまで許可し、失敗時の被害範囲をどう絞るかにある。Home Assistantのように実世界の機器へ触れる対象では、特にこの設計が重要になる。


    ツールを増やすほど便利になるが、同時に危険も増える。だから権限とサンドボックスが必要になる。これはMCPサーバー設計や社内ツール接続でも同じだ。'
- heading: エージェントはモデルではなく、モデルを回すハーネス
  time: 430
  body: '投稿者はハーネスまたはランタイムを、モデルの周囲にある管理層として説明する。プロンプトをどう組み立てるか、どのツールを使えるか、ループをどう進めるか、実行結果を次の入力へどう戻すか。ここがエージェントの実体に近い。


    最後に、エージェントは魔法でも新種のモデルでもなく、通常のモデルを文脈、ツール、権限、ループへ接続するラッパーだと整理される。この説明はかなり健全だ。'
editorial: Hermesの動画が良いのは、エージェントを神秘化せず、ハーネスとして説明している点だ。Claude CodeでもCodexでも、成果はモデル単体ではなく、読み取れる文脈、許された操作、検証ループ、失敗時の隔離で決まる。Home
  Assistantのような物理世界に近い対象ほど、この設計思想は重要になる。エージェント導入で最初に設計すべきなのは「何ができるか」ではなく「どこまでしかできないか」だ。
en:
  articleTitle: Hermes Agent and Home Assistant — agents are harnesses, not magic
    models
  seoTitle: Hermes Agent and Home Assistant — agents are harnesses, not magi
  summary: Tailscale’s video starts with using the self-hostable Hermes agent to control
    Home Assistant.
  keyPhrases:
  - Hermes Agent
  - Home Assistant
  - Tailscale
  - agent harness
  - tool permissions
  - sandboxing
  bulletPoints:
  - time: 0
    text: Tailscale’s video starts with using the self-hostable Hermes agent to control
      Home Assistant.
  - time: 20
    text: The creator calls out the confusion around agents, harnesses, runtimes,
      tool access, memory, and sandboxes.
  - time: 260
    text: The important design pieces are tools, permissions, sandboxing, and the
      loop around the model.
  - time: 430
    text: A harness or runtime assembles prompts, exposes tools, manages the agentic
      loop, and controls execution.
  - time: 980
    text: 'The conclusion is clear: agents are not magic or new model types; they
      are wrappers around normal models with context and tools.'
  sections:
  - heading: A smart-home demo that explains agent basics
    time: 0
    body: 'The video begins with Hermes, a self-hostable AI agent, controlling Home
      Assistant. But the useful part is the conceptual cleanup. The creator points
      out how crowded the terminology has become: agents, harnesses, runtimes, tools,
      memory, sandboxes.


      That makes the video relevant beyond smart homes. It explains the system around
      the model.'
  - heading: Permissions and sandboxing define the risk
    time: 260
    body: 'When an agent can touch real tools, the key question is not only capability.
      It is permission boundaries. What can it access? What can it change? How is
      the blast radius limited?


      This matters for Home Assistant, but also for MCP servers and internal company
      tools.'
  - heading: The harness is the agent
    time: 430
    body: 'The harness or runtime is the practical agent layer. It assembles prompts,
      decides which tools are available, manages the loop, and feeds results back
      into the model.


      The video’s conclusion is refreshingly grounded: agents are normal models wrapped
      with context, tools, and control logic.'
  editorial: 'This is a useful corrective to agent hype. The model matters, but the
    harness decides what the model can see, do, and damage. For Claude and Codex workflows,
    the same lesson applies: design permissions, tools, and verification loops before
    celebrating autonomy.'
  headerImage: /images/1zaA6QlRScg/header.png
  heroImage: /images/1zaA6QlRScg/header.png
---

## ハイライト

- [00:00] Tailscaleの動画は、Hermesというセルフホスト可能なAIエージェントでHome Assistantを操作する実験から始まる。
- [00:20] 投稿者は、agent、harness、runtime、tool access、memory、sandboxなどの用語が混乱していると認め、ノイズを減らして説明すると宣言する。
- [04:20] 重要なのはモデル単体ではなく、モデルに渡すツール、権限、サンドボックス、ループを管理する周辺システムだ。
- [07:10] ハーネスまたはランタイムは、プロンプトの組み立て、利用可能ツール、エージェントループ、実行制御を担う層として説明される。
- [16:20] 結論では、エージェントは魔法でも新種のモデルでもなく、通常のモデルをコンテキストとツールへ接続するラッパーだと整理される。

## セクション

### Home Assistant実験から、エージェント用語をほどく

- 時刻: 00:00

Tailscaleの動画は、Hermesというセルフホスト可能なAIエージェントを使ってHome Assistantを操作する話から入る。ただし主題はスマートホームだけではない。投稿者は、agent、harness、runtime、tool access、memory、sandboxといった言葉が混ざりすぎていると認め、実際に何が起きているのかを整理しようとする。

これはClaude CodeやMCPを使う読者にも近い話だ。エージェントという言葉は派手だが、多くの場合、モデルそのものではなく、モデルを囲む実行環境の設計を指している。

### ツール、権限、サンドボックスが失敗時の被害を決める

- 時刻: 04:20

動画の中核は、モデルに何をさせるかではなく、何へアクセスさせ、どこまで許可し、失敗時の被害範囲をどう絞るかにある。Home Assistantのように実世界の機器へ触れる対象では、特にこの設計が重要になる。

ツールを増やすほど便利になるが、同時に危険も増える。だから権限とサンドボックスが必要になる。これはMCPサーバー設計や社内ツール接続でも同じだ。

### エージェントはモデルではなく、モデルを回すハーネス

- 時刻: 07:10

投稿者はハーネスまたはランタイムを、モデルの周囲にある管理層として説明する。プロンプトをどう組み立てるか、どのツールを使えるか、ループをどう進めるか、実行結果を次の入力へどう戻すか。ここがエージェントの実体に近い。

最後に、エージェントは魔法でも新種のモデルでもなく、通常のモデルを文脈、ツール、権限、ループへ接続するラッパーだと整理される。この説明はかなり健全だ。

## 編集部の視点

Hermesの動画が良いのは、エージェントを神秘化せず、ハーネスとして説明している点だ。Claude CodeでもCodexでも、成果はモデル単体ではなく、読み取れる文脈、許された操作、検証ループ、失敗時の隔離で決まる。Home Assistantのような物理世界に近い対象ほど、この設計思想は重要になる。エージェント導入で最初に設計すべきなのは「何ができるか」ではなく「どこまでしかできないか」だ。
