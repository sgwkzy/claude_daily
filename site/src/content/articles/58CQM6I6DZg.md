---
videoId: 58CQM6I6DZg
title: Claude Design 2.0 Just Changed Everything...
slug: claude-design-20-の主要4変更点-クレジット効率と-mcp-連携の実装ガイド-58cqm6i6dzg
articleTitle: Claude Design 2.0 の主要4変更点 — クレジット効率と MCP 連携の実装ガイド
seoTitle: Claude Design 2.0 の主要4変更点 — クレジット効率と MCP 連携の実装ガイド
summary: Jack Roberts は『Claude Code は世界最高水準のデザインエージェント』と評し、その新世代 Claude Design 2.0
  の使いこなしを5レベルで整理する。最大の制約と回避策まで含めた実装ガイドの構成。
channel: Jack Roberts
channelId: UCxVxcTULO9cFU6SB9qVaisQ
publishedAt: '2026-06-28T18:03:35Z'
fetchedAt: '2026-06-29T11:18:54.774165Z'
originalThumbnail: https://i.ytimg.com/vi/58CQM6I6DZg/maxresdefault.jpg
headerImage: /images/58CQM6I6DZg/header.ja.png
heroImage: /images/58CQM6I6DZg/header.ja.png
viewCount: 21547
durationSec: 902
sourceLanguage: en-GB
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Claude Design 2.0 主要4変更
- Firecrawl MCP ブランド抽出
- Higgsfield/Kia AI 画像生成
- クレジット消費効率改善
- GLM 5.2 1/6 コスト併用
- Claude Code クレジット建て増し連携
bulletPoints:
- time: 0
  text: Jack Roberts は『Claude Code は世界最高水準のデザインエージェント』と評し、その新世代 Claude Design 2.0
    の使いこなしを5レベルで整理する。最大の制約と回避策まで含めた実装ガイドの構成。
- time: 47
  text: Claude Design とはウェブサイト・アプリ・プロトタイプデックなどを生成するクリエイティブ機能。Opus 4.8 を裏で使い、初週で100万ユーザーを獲得した。
- time: 67
  text: 2.0 では大きな4変更と細かな複数変更が入っている。映像はそれぞれの変更が実際のデザインフローに与える影響を順に解説する形を取る。
- time: 73
  text: 最大の変更点はクレジットの消費効率が改善され、同じ手元クレジットで生成できる量が大幅に増えたこと。Anthropic 側の Opus 4.8 最適化と連動した変更となる。
- time: 416
  text: Firecrawl MCP を接続し、glido.com のブランドアイデンティティを抽出して3ページ構成のアニメーション付きデックを生成する実演。MCP
    経由の外部データ取り込みが標準ワークフロー化している。
- time: 449
  text: 画像生成は Higgsfield か Kia AI が安価な選択肢として推奨される。API キーを Claude Design に接続するだけで動き、Firecrawl
    と組み合わせて『参照→生成→組み込み』が連続する。
- time: 828
  text: Claude Code 側で構築中のプロジェクトでクレジット上限に到達した場合、Claude Design 経由で建て増しを継続できる。両者の連携が制約緩和の現実的な手段になっている。
- time: 864
  text: GLM 5.2 を Claude Design ターミナルから呼び出すと Opus 4.8 と同等品質を約1/6のコストで使える。商用モデルとオープンソースモデルの併用が公式に推奨される形になった。
sections:
- heading: Claude Design 2.0 の概要と4つの主要変更
  time: 0
  body: 'Jack Roberts は『Claude Code は世界最高水準のデザインエージェント』と評価し、Claude Design 2.0 の使いこなしを5レベルで整理する。動画は新規ユーザー向けの基本確認から、上級者向けの
    MCP 連携・モデル切り替えまで一本道で進む構成だ。


    Claude Design 自体はウェブサイト・アプリ・プロトタイプデックの生成機能で、裏では Opus 4.8 が稼働する。初週で100万ユーザーを獲得した話題機能でもある。2.0
    では大きな4変更と複数の細かな変更が加わっており、最大の変更点はクレジットの消費効率改善だ。同じ手元クレジットで生成できる量が大きく増え、Opus 4.8
    側のモデル最適化と連動している。'
- heading: Firecrawl MCP 連携でブランド抽出からデック生成まで自動化
  time: 416
  body: '実演の中心は MCP コネクタ経由のワークフローだ。glido.com に Firecrawl MCP を接続し『ここのブランドアイデンティティを抽出して3ページのアニメーション付きデックを作って』と指示するだけで、外部サイトから企業の色・タイポグラフィ・トーンが抽出され、それに沿ったデックが生成される。


    画像生成は Higgsfield か Kia AI が安価な選択肢として推奨される。API キーを Claude Design に接続すれば、Firecrawl
    で抽出したブランド情報をベースに『参照→生成→デック組み込み』が連続して走る。Firecrawl は HTML を除いて意味のあるテキストのみを返すため、トークン消費が小さい点が選定理由として強調される。MCP
    経由のデータ取り込みがデザインワークフローの標準コンポーネントになりつつある。'
- heading: クレジット節約戦略 — GLM 5.2 併用と Claude Code 連携
  time: 828
  body: 'Claude Design 2.0 の運用上の最大の制約はやはりクレジット上限だ。Jack の提案は二段構えである。第一に、Claude Code
    側のプロジェクトで上限に到達しても Claude Design 経由で建て増しを継続できるため、両ツールを行き来する設計でクレジット圧迫を緩和できる。


    第二に、GLM 5.2 をターミナルから呼び出す方法が公式に推奨されたことだ。Opus 4.8 とほぼ同等品質を約1/6のコストで使えるため、上限のないラフ作業を
    GLM 5.2 で進め、最終仕上げのみ Opus 4.8 で行う、といった役割分担が成り立つ。商用モデルとオープンソースモデルの併用が前提化したことで、Claude
    Design はクリエイティブ生成ハブとしての性格を強めている。Open AI 製テンプレートのように『PowerPoint へエクスポートできない』制約はあるものの、Claude
    Design 内で完結する作業に対しては高い柔軟性を提供する。'
editorial: Claude Design 2.0 は単独機能の更新ではなく、Claude プロダクト群全体の連携設計の更新として読むのが正しい。最大の変更点であるクレジット効率改善は
  Opus 4.8 のモデル最適化と連動し、Firecrawl などの MCP コネクタが標準ワークフローの一部に組み込まれ、さらに公式に GLM 5.2 併用が推奨される。デザインエージェントというより、商業モデルとオープンソースモデル、外部
  SaaS データを一つのキャンバスで束ねる『クリエイティブハブ』の輪郭が見えてきた。読者にとっての含意は二つある。Claude エコシステムを使い込むほど MCP
  コネクタの設計選定が成果差を決める変数になる。そして商業モデル単独に閉じる運用は無料/低価格 OSS の浸透で割高になり始めており、組み合わせ運用を前提に設計を始めるのが現実的な選択肢になる。
en:
  articleTitle: Claude Design 2.0's Four Big Changes — A Practical Guide to Credit
    Efficiency and MCP Integration
  seoTitle: Claude Design 2.0's Four Big Changes — A Practical Guide to Cred
  summary: Jack Roberts calls Claude Code 'the world's best design agent' and organizes
    Claude Design 2.0 across five levels —…
  keyPhrases:
  - Claude Design 2.0 four big changes
  - Firecrawl MCP brand extraction
  - Higgsfield and Kia AI for image generation
  - Credit-efficiency improvement
  - GLM 5.2 at one-sixth the cost
  - Bridging credit caps with Claude Code
  bulletPoints:
  - time: 0
    text: Jack Roberts calls Claude Code 'the world's best design agent' and organizes
      Claude Design 2.0 across five levels — from basics to the biggest limitation
      and how to work around it.
  - time: 47
    text: Claude Design generates websites, apps and prototype decks. It runs Opus
      4.8 under the hood and pulled a million users in its first week.
  - time: 67
    text: 2.0 ships four big changes plus a handful of smaller ones. The video walks
      through how each change shapes the actual design workflow in order.
  - time: 73
    text: The biggest change is improved credit efficiency — the same credit balance
      now buys substantially more output. It's coordinated with Anthropic's Opus 4.8
      optimization on the model side.
  - time: 416
    text: The demo connects Firecrawl MCP, extracts brand identity from glido.com,
      and generates a three-page animated deck. External-data ingestion via MCP has
      become a standard part of the workflow.
  - time: 449
    text: For image generation, Higgsfield or Kia AI are recommended as inexpensive
      options. Connect your API key to Claude Design and 'reference, generate, embed'
      runs as one continuous loop with Firecrawl.
  - time: 828
    text: When you hit a credit ceiling on a Claude Code project, you can continue
      building via Claude Design. The integration between the two surfaces becomes
      a practical pressure release for the credit limit.
  - time: 864
    text: Calling GLM 5.2 from the Claude Design terminal gets you Opus 4.8-equivalent
      quality at roughly one-sixth the cost. Mixing a commercial model with an open-source
      one is now officially recommended.
  sections:
  - heading: Claude Design 2.0 in Context and Its Four Major Changes
    time: 0
    body: 'Jack Roberts calls Claude Code ''the world''s best design agent'' and organizes
      Claude Design 2.0 across five levels of use. The video runs in a single line
      from basics for new users through MCP integration and model switching for advanced
      users.


      Claude Design itself generates websites, apps and prototype decks, with Opus
      4.8 running under the hood. It pulled in a million users in its first week.
      2.0 adds four major changes and a handful of smaller ones, and the largest is
      credit-efficiency improvement — the same credit balance now buys substantially
      more output, coordinated with the model-side optimization on Opus 4.8.'
  - heading: Firecrawl MCP Integration Automates Brand Extraction Through Deck Generation
    time: 416
    body: 'The center of the demo is the MCP-connector workflow. Connect Firecrawl
      MCP to glido.com and ask ''Extract the brand identity here and generate a three-page
      animated deck'' — the external site''s color, typography and tone get pulled
      back, and a deck aligned to them is generated.


      For image generation, Higgsfield or Kia AI are recommended as inexpensive options.
      With API keys connected to Claude Design, ''reference, generate, embed'' runs
      as one continuous loop using the brand information Firecrawl extracted. Firecrawl
      is highlighted because it strips HTML and returns only the meaningful text —
      token cost stays low. MCP-based data ingestion is becoming a standard component
      of design workflows.'
  - heading: Credit-Saving Strategies — Pair With GLM 5.2 and Bridge to Claude Code
    time: 828
    body: 'Claude Design 2.0''s biggest operational constraint is still the credit
      ceiling. Jack''s proposal is layered. First, when you hit the ceiling on a Claude
      Code project, you can keep building through Claude Design, so a design that
      alternates between the two surfaces eases credit pressure.


      Second, calling GLM 5.2 from the terminal is now officially supported. With
      Opus 4.8-equivalent quality at roughly one-sixth the cost, you can do rough
      exploratory work on GLM 5.2 without a ceiling and reserve Opus 4.8 for final
      polish. Mixing a commercial model with an open-source companion is now baked
      into the assumed workflow, and Claude Design''s identity is sharpening as a
      creative-generation hub. There are constraints — Open AI-style templates can''t
      be exported to PowerPoint, for instance — but for work that stays inside Claude
      Design, the flexibility is high.'
  editorial: Claude Design 2.0 is best read not as a standalone-feature update but
    as an update to the integration design across Anthropic's full product surface.
    The biggest change — credit efficiency — sits in lock-step with Opus 4.8's model
    optimization. MCP connectors like Firecrawl are becoming part of the standard
    workflow. And the official endorsement of GLM 5.2 as a companion model layers
    in. The outline emerging is less 'design agent' and more 'creative hub' — one
    canvas binding a commercial model, an open-source model, and external SaaS data.
    Two implications for readers. The more you live inside the Claude ecosystem, the
    more your MCP-connector design choices become the variable that decides output
    quality. And exclusively running on a single commercial model is becoming a higher-cost
    path as cheap-or-free OSS spreads — designing for combined use from the start
    is the realistic call.
  headerImage: /images/58CQM6I6DZg/header.png
  heroImage: /images/58CQM6I6DZg/header.png
---

## ハイライト

- [00:00] Jack Roberts は『Claude Code は世界最高水準のデザインエージェント』と評し、その新世代 Claude Design 2.0 の使いこなしを5レベルで整理する。最大の制約と回避策まで含めた実装ガイドの構成。
- [00:47] Claude Design とはウェブサイト・アプリ・プロトタイプデックなどを生成するクリエイティブ機能。Opus 4.8 を裏で使い、初週で100万ユーザーを獲得した。
- [01:07] 2.0 では大きな4変更と細かな複数変更が入っている。映像はそれぞれの変更が実際のデザインフローに与える影響を順に解説する形を取る。
- [01:13] 最大の変更点はクレジットの消費効率が改善され、同じ手元クレジットで生成できる量が大幅に増えたこと。Anthropic 側の Opus 4.8 最適化と連動した変更となる。
- [06:56] Firecrawl MCP を接続し、glido.com のブランドアイデンティティを抽出して3ページ構成のアニメーション付きデックを生成する実演。MCP 経由の外部データ取り込みが標準ワークフロー化している。
- [07:29] 画像生成は Higgsfield か Kia AI が安価な選択肢として推奨される。API キーを Claude Design に接続するだけで動き、Firecrawl と組み合わせて『参照→生成→組み込み』が連続する。
- [13:48] Claude Code 側で構築中のプロジェクトでクレジット上限に到達した場合、Claude Design 経由で建て増しを継続できる。両者の連携が制約緩和の現実的な手段になっている。
- [14:24] GLM 5.2 を Claude Design ターミナルから呼び出すと Opus 4.8 と同等品質を約1/6のコストで使える。商用モデルとオープンソースモデルの併用が公式に推奨される形になった。

## セクション

### Claude Design 2.0 の概要と4つの主要変更

- 時刻: 00:00

Jack Roberts は『Claude Code は世界最高水準のデザインエージェント』と評価し、Claude Design 2.0 の使いこなしを5レベルで整理する。動画は新規ユーザー向けの基本確認から、上級者向けの MCP 連携・モデル切り替えまで一本道で進む構成だ。

Claude Design 自体はウェブサイト・アプリ・プロトタイプデックの生成機能で、裏では Opus 4.8 が稼働する。初週で100万ユーザーを獲得した話題機能でもある。2.0 では大きな4変更と複数の細かな変更が加わっており、最大の変更点はクレジットの消費効率改善だ。同じ手元クレジットで生成できる量が大きく増え、Opus 4.8 側のモデル最適化と連動している。

### Firecrawl MCP 連携でブランド抽出からデック生成まで自動化

- 時刻: 06:56

実演の中心は MCP コネクタ経由のワークフローだ。glido.com に Firecrawl MCP を接続し『ここのブランドアイデンティティを抽出して3ページのアニメーション付きデックを作って』と指示するだけで、外部サイトから企業の色・タイポグラフィ・トーンが抽出され、それに沿ったデックが生成される。

画像生成は Higgsfield か Kia AI が安価な選択肢として推奨される。API キーを Claude Design に接続すれば、Firecrawl で抽出したブランド情報をベースに『参照→生成→デック組み込み』が連続して走る。Firecrawl は HTML を除いて意味のあるテキストのみを返すため、トークン消費が小さい点が選定理由として強調される。MCP 経由のデータ取り込みがデザインワークフローの標準コンポーネントになりつつある。

### クレジット節約戦略 — GLM 5.2 併用と Claude Code 連携

- 時刻: 13:48

Claude Design 2.0 の運用上の最大の制約はやはりクレジット上限だ。Jack の提案は二段構えである。第一に、Claude Code 側のプロジェクトで上限に到達しても Claude Design 経由で建て増しを継続できるため、両ツールを行き来する設計でクレジット圧迫を緩和できる。

第二に、GLM 5.2 をターミナルから呼び出す方法が公式に推奨されたことだ。Opus 4.8 とほぼ同等品質を約1/6のコストで使えるため、上限のないラフ作業を GLM 5.2 で進め、最終仕上げのみ Opus 4.8 で行う、といった役割分担が成り立つ。商用モデルとオープンソースモデルの併用が前提化したことで、Claude Design はクリエイティブ生成ハブとしての性格を強めている。Open AI 製テンプレートのように『PowerPoint へエクスポートできない』制約はあるものの、Claude Design 内で完結する作業に対しては高い柔軟性を提供する。

## 編集部の視点

Claude Design 2.0 は単独機能の更新ではなく、Claude プロダクト群全体の連携設計の更新として読むのが正しい。最大の変更点であるクレジット効率改善は Opus 4.8 のモデル最適化と連動し、Firecrawl などの MCP コネクタが標準ワークフローの一部に組み込まれ、さらに公式に GLM 5.2 併用が推奨される。デザインエージェントというより、商業モデルとオープンソースモデル、外部 SaaS データを一つのキャンバスで束ねる『クリエイティブハブ』の輪郭が見えてきた。読者にとっての含意は二つある。Claude エコシステムを使い込むほど MCP コネクタの設計選定が成果差を決める変数になる。そして商業モデル単独に閉じる運用は無料/低価格 OSS の浸透で割高になり始めており、組み合わせ運用を前提に設計を始めるのが現実的な選択肢になる。
