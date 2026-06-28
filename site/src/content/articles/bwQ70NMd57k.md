---
videoId: bwQ70NMd57k
title: 'Google OKF + MCP : Explained The New "AI Context Stack"'
slug: google-okf-mcpが示すaiコンテキストスタック-意味の層と実行の層を分けて考える-bwq70nmd57k
articleTitle: Google OKF + MCPが示すAIコンテキストスタック — 意味の層と実行の層を分けて考える
seoTitle: Google OKF + MCPが示すAIコンテキストスタック — 意味の層と実行の層を分けて考える
summary: 動画は、現代のAIが賢くても自社の週次アクティブユーザーを知らない、という例から始まる。問題は知能ではなくコンテキストだ。
channel: Cloud Codes
channelId: UC0DZj1PNa_Fp0MU6uPSKv5w
publishedAt: '2026-06-26T01:00:05Z'
fetchedAt: '2026-06-28T12:02:05.714987Z'
originalThumbnail: https://i.ytimg.com/vi/bwQ70NMd57k/maxresdefault.jpg
headerImage: /images/bwQ70NMd57k/header.ja.png
heroImage: /images/bwQ70NMd57k/header.ja.png
viewCount: 14165
durationSec: 512
sourceLanguage: en
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Google OKF
- MCP
- AIコンテキストスタック
- 意味レイヤー
- 実行レイヤー
- LLM Wiki
bulletPoints:
- time: 0
  text: 動画は、現代のAIが賢くても自社の週次アクティブユーザーを知らない、という例から始まる。問題は知能ではなくコンテキストだ。
- time: 35
  text: OKFはファイルツリーではなく、メトリクス、顧客、ドキュメント、意味の関係をつなぐ知識レイヤーとして説明される。
- time: 190
  text: KarpathyのLLM wiki構想に触れ、モデルが自分の知識ベースを書き、維持し、知識が複利で効く状態が紹介される。
- time: 330
  text: MCPは、その知識から実ツールへ届くライブで統制されたアクセスの層として整理される。
- time: 430
  text: OKFが意味を与え、MCPが行動を与える。両者を合わせるとAI context stackとして理解しやすい。
sections:
- heading: 問題は知能ではなく、AIが会社の文脈を知らないこと
  time: 0
  body: 'Cloud Codesの動画は分かりやすい例から始まる。モデルはSQLを書ける。だが「先週の週次アクティブユーザーは？」と聞くと答えられない。能力が足りないのではなく、会社のデータ、定義、関係、判断基準に接続されていない。


    この問題を「コンテキスト不足」として捉えると、AI導入の焦点はモデル選びだけではなくなる。どの知識を、どんな構造で、どの権限でAIへ渡すかが設計対象になる。'
- heading: OKFは意味の層、MCPは実行の層
  time: 190
  body: '動画ではOKFを、単なるフォルダやドキュメント置き場ではなく、メトリクス、顧客、テーブル、意思決定の関係をつなぐ意味の層として説明する。KarpathyのLLM
    wikiにも触れ、モデルが自分の知識ベースを書き、保守し、知識が蓄積するイメージが提示される。


    一方でMCPは、AIが実際のツールやデータソースへ到達するためのライブで統制されたアクセス層だ。OKFが「何を意味するか」を与え、MCPが「何を実行できるか」を与える。'
- heading: AI context stackとして運用を設計する
  time: 430
  body: 'OKFとMCPを分けて考えると、AIシステムの設計が整理しやすくなる。知識を厚くしても実行権限がなければレポート止まりになる。逆にツール接続だけを増やしても、意味の関係がなければ危ない自動化になる。


    ClaudeやCodexを業務に入れるなら、まず意味の層を整え、次にMCPで必要最小限の実行権限を与える。この順序が、今後の社内AI設計の基本になりそうだ。'
editorial: この動画の価値は、MCPを単独の流行語として扱わず、OKFのような意味レイヤーと組み合わせて説明している点にある。AIが動けるようになるほど、ツール接続だけでは危険になる。何が何を意味し、どの定義が正で、どの操作が許されるかを分けて設計する必要がある。Claude
  Daily読者にとっては、MCP導入前に社内知識の関係づけを整える重要性を思い出させる内容だ。
en:
  articleTitle: Google OKF + MCP — the AI context stack as meaning plus action
  seoTitle: Google OKF + MCP — the AI context stack as meaning plus action
  summary: 'The video opens with a simple problem: models can write SQL, but they
    do not know your company’s weekly active users…'
  keyPhrases:
  - Google OKF
  - MCP
  - AI context stack
  - meaning layer
  - action layer
  - LLM wiki
  bulletPoints:
  - time: 0
    text: 'The video opens with a simple problem: models can write SQL, but they do
      not know your company’s weekly active users unless context is connected.'
  - time: 35
    text: OKF is framed as a meaning layer that links metrics, customers, documents,
      and definitions rather than a simple folder tree.
  - time: 190
    text: Karpathy’s LLM wiki idea appears as a way for agents to write and maintain
      compounding knowledge.
  - time: 330
    text: MCP becomes the live governed access layer from knowledge into real tools
      and systems.
  - time: 430
    text: 'Together, OKF and MCP form a useful mental model: meaning at the bottom,
      action on top.'
  sections:
  - heading: The problem is context, not intelligence
    time: 0
    body: 'The video starts with a useful distinction. A modern model can write a
      query, but it cannot answer a company-specific metrics question unless it has
      access to the definitions, data, and relationships behind that metric. The missing
      part is context.


      That shifts the design problem from model selection to context architecture.'
  - heading: OKF as meaning, MCP as action
    time: 190
    body: 'OKF is presented as a meaning layer: a graph of metrics, customers, docs,
      and definitions. MCP is the live, governed tool-access layer. One tells the
      model what things mean; the other lets it act.


      The video connects this to Karpathy’s LLM wiki idea, where knowledge compounds
      because the agent can maintain its own working context.'
  - heading: Designing the stack
    time: 430
    body: 'The stack is useful because either layer alone is incomplete. Knowledge
      without action produces reports. Tool access without meaning produces risky
      automation.


      For Claude and Codex deployments, the practical sequence is: organize meaning
      first, then add least-privilege MCP actions.'
  editorial: The important point is that MCP should not be treated as the whole context
    story. Tool access needs a meaning layer beneath it. As agents become more capable,
    this separation between definitions and actions becomes a safety and reliability
    requirement, not architecture trivia.
  headerImage: /images/bwQ70NMd57k/header.png
  heroImage: /images/bwQ70NMd57k/header.png
---

## ハイライト

- [00:00] 動画は、現代のAIが賢くても自社の週次アクティブユーザーを知らない、という例から始まる。問題は知能ではなくコンテキストだ。
- [00:35] OKFはファイルツリーではなく、メトリクス、顧客、ドキュメント、意味の関係をつなぐ知識レイヤーとして説明される。
- [03:10] KarpathyのLLM wiki構想に触れ、モデルが自分の知識ベースを書き、維持し、知識が複利で効く状態が紹介される。
- [05:30] MCPは、その知識から実ツールへ届くライブで統制されたアクセスの層として整理される。
- [07:10] OKFが意味を与え、MCPが行動を与える。両者を合わせるとAI context stackとして理解しやすい。

## セクション

### 問題は知能ではなく、AIが会社の文脈を知らないこと

- 時刻: 00:00

Cloud Codesの動画は分かりやすい例から始まる。モデルはSQLを書ける。だが「先週の週次アクティブユーザーは？」と聞くと答えられない。能力が足りないのではなく、会社のデータ、定義、関係、判断基準に接続されていない。

この問題を「コンテキスト不足」として捉えると、AI導入の焦点はモデル選びだけではなくなる。どの知識を、どんな構造で、どの権限でAIへ渡すかが設計対象になる。

### OKFは意味の層、MCPは実行の層

- 時刻: 03:10

動画ではOKFを、単なるフォルダやドキュメント置き場ではなく、メトリクス、顧客、テーブル、意思決定の関係をつなぐ意味の層として説明する。KarpathyのLLM wikiにも触れ、モデルが自分の知識ベースを書き、保守し、知識が蓄積するイメージが提示される。

一方でMCPは、AIが実際のツールやデータソースへ到達するためのライブで統制されたアクセス層だ。OKFが「何を意味するか」を与え、MCPが「何を実行できるか」を与える。

### AI context stackとして運用を設計する

- 時刻: 07:10

OKFとMCPを分けて考えると、AIシステムの設計が整理しやすくなる。知識を厚くしても実行権限がなければレポート止まりになる。逆にツール接続だけを増やしても、意味の関係がなければ危ない自動化になる。

ClaudeやCodexを業務に入れるなら、まず意味の層を整え、次にMCPで必要最小限の実行権限を与える。この順序が、今後の社内AI設計の基本になりそうだ。

## 編集部の視点

この動画の価値は、MCPを単独の流行語として扱わず、OKFのような意味レイヤーと組み合わせて説明している点にある。AIが動けるようになるほど、ツール接続だけでは危険になる。何が何を意味し、どの定義が正で、どの操作が許されるかを分けて設計する必要がある。Claude Daily読者にとっては、MCP導入前に社内知識の関係づけを整える重要性を思い出させる内容だ。
