---
videoId: tOC2N0B9lio
title: The next paradigm shift (according to Karpathy)
slug: karpathyの3回目のパラダイム転換-theo-t3ggが渋々anthropicを擁護した理由-toc2n0b9lio
articleTitle: Karpathyの『3回目のパラダイム転換』 — Theo (t3.gg)が渋々Anthropicを擁護した理由
seoTitle: Karpathyの『3回目のパラダイム転換』 — Theo (t3.gg)が渋々Anthropicを擁護した理由
summary: 'Anthropicの公式説明: Claudeとの新しい対話パラダイム。表面下の統合作業を済ませれば Claude はチームの一員のように加わり、別の人間と話すように使える。LLM
  UI / UX の第3の再設計。'
channel: Theo - t3․gg
channelId: UCbRP3c757lWg9M-U7TyEkXA
publishedAt: '2026-06-25T07:55:16Z'
fetchedAt: '2026-06-27T06:58:57.961686Z'
originalThumbnail: https://i.ytimg.com/vi/tOC2N0B9lio/maxresdefault.jpg
headerImage: /images/tOC2N0B9lio/header.ja.png
heroImage: /images/tOC2N0B9lio/header.ja.png
viewCount: 83252
durationSec: 1247
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Karpathy第3のLLMパラダイム
- ambient behavior機能
- Claudeの並列非同期実行
- Theo自作Hermesエージェント
- 組織レベルハーネス
- OpenClaude/Hermesによる自前実装
bulletPoints:
- time: 0
  text: 'Anthropicの公式説明: Claudeとの新しい対話パラダイム。表面下の統合作業を済ませれば Claude はチームの一員のように加わり、別の人間と話すように使える。LLM
    UI / UX の第3の再設計。'
- time: 24
  text: 第1のパラダイムは『LLM = アクセスするWebサイト』。第2が『PCにダウンロードするアプリ』。第3が『組織横断のツールとコンテキストを持つ自己完結・永続・非同期エンティティが人間チームと並走する』形態。
- time: 48
  text: 'Theoの懸念: LLM の先駆者 Karpathy が Slackbot について語っているように聞こえると、彼の判断力を疑いたくなる人もいるはず。最近Anthropic入りしたからKool-Aidを早く飲んだのではないか、と思うのも自然な反応。'
- time: 75
  text: 'Theoが本動画で行うこと: 嫌な仕事を3つする。Anthropicを擁護する、それについて動画を作る、そして自身の信念を改めて検証する。'
- time: 577
  text: '機能詳細: ambient behavior をオンにすると Claude は能動的に情報を更新してくれる。チャネル横断で関連情報をフラグ、未解決のまま静かになったスレッドやタスクをフォローアップ。Slackのカオスを考えると本当に便利。'
- time: 610
  text: '非同期動作: タスクを Claude に投げて他優先事項に集中可。Claude は自身のタスクをスケジュール化し、プロジェクトを数時間〜数日にわたって自律的に追える。Anthropic自身も並列に多くの
    Claude にタスク委譲して時間を使うようになった。'
- time: 632
  text: 'Theo自身の対比例: 同じ思想の自作 Hermes エージェント。Discordサーバー専用で動かし、Rust移植も検討中。Claude Tagはこの方向の組織向け実装版。'
- time: 1168
  text: 'Theoの結論: 単なる Slackbot ではなく、組織レベルのハーネス。3つの会社を運営している立場から見て、Anthropicの方向性は100%正しい。Karpathyの主張も正当だった、と擁護して動画を締める。'
sections:
- heading: Karpathyが宣言した『LLM第3のパラダイム』とは
  time: 0
  body: 'Theo (t3.gg) は Anthropic の Claude Tag リリースに合わせて、Andrej Karpathy が打ち出したパラダイム議論を真正面から取り上げる。Anthropic公式の説明はこうだ。表面下の統合作業を済ませれば
    Claude はチームの一員のようにシームレスに加わり、別の人間と話すように使える。多様なワークロードに対応する。


    そしてKarpathyがこれを『LLMの第3の再設計』と位置づけた。第1のパラダイムは『LLM = アクセスするWebサイト』。第2が『PCにダウンロードするアプリ』。第3が『組織横断のツールとコンテキストを持つ自己完結・永続・非同期エンティティが人間チームと並走する』形態だ。最初は理解に時間がかかるが、実際に動かしてみるとうまく機能する、というのが
    Karpathy の主張だ。'
- heading: Theoの渋々の擁護 — 機能詳細
  time: 48
  body: 'Theoの正直な反応はまず懐疑だった。LLM の先駆者の一人で AI 界で最も重要な人物の一人である Karpathy が Slackbot について語っているように聞こえると、判断力を疑いたくなる。Anthropic
    に最近移籍したから Kool-Aid を早く飲んだのではないか、というのも自然な反応だ。Theo は明示的に『嫌な仕事を3つする』と宣言する。Anthropicを擁護する、それについて動画を作る、そして自身の信念を再検証する。


    機能詳細を見ていくとTheoは納得していく。ambient behavior をオンにすると Claude は能動的に情報を更新してくれる。チャネル横断で関連情報をフラグし、未解決のまま静かになったスレッドやタスクをフォローアップする。Slackのカオスな性質を考えると、これは現実に役立つ機能だ、とTheoは認める。非同期動作も鍵だ。Claude
    にタスクを投げて自分は他優先事項に集中、Claude は自身のタスクをスケジュール化し、プロジェクトを数時間〜数日にわたって自律的に追う。Anthropic
    自身も並列に多くの Claude にタスク委譲して時間を使うようになった、と公式が認めている。'
- heading: Hermes自作実装からの肯定 — 組織レベルハーネスとして
  time: 632
  body: 'Theoが特に説得力を持って語れるのは、自身が同じ思想の自作エージェント Hermes を運用しているからだ。Hermes は専用 Discord
    サーバーで動き、Rust への移植も検討中だという。彼の3つの会社運営でこの方向が機能していることを実体験しているため、Claude Tag を組織レベルのハーネスとして評価できる。


    結論部でTheoは100%の確信を持って言う。Claude Tag は単なる Slackbot ではなく、組織レベルのハーネスだ。3つの会社を運営している立場から見て、Anthropicの方向性は正しい。Karpathy
    が clowned on された (ネット上で揶揄された) ことについては気の毒だが、Anthropic 入社直後にこれを言わされる立場の悪さもある程度想定される、とコメントする。Anthropic
    Enterprise の高額プランを払いたくない読者には、OpenClaude や Hermes エージェントを自分の Discord / Slack に立ててみることを薦め、それで本動画で見えた価値が体感できるはずだ、と締める。Anthropic
    と Slack の両方を擁護する動画を作ることになるとは思わなかった、というのが本人のオチだ。'
editorial: Theo の擁護動画が説得力を持つのは、彼自身が同じ思想の自作エージェントを運用していて、Claude Tag のコンセプトを自分の体験で検証できる位置にいるからだ。Karpathy
  が提示した『LLM 第3のパラダイム』フレーミングは、製品マーケティングとしては強い言葉だが、現場の実装視点では『組織レベルハーネス』という Theo の用語の方が機能を正確に捉えている。これは個別のエージェント実行を組織横断のコンテキストと並列実行で組み立て直す抽象化層を指していて、Slack
  統合は単なる入出力面に過ぎない。読者にとっての示唆は二段ある。Claude Tag を試す前提のあるチームは、必要なのは Slack 統合の良し悪しではなく、社内ナレッジ・タスク状態・進行プロジェクトを横断する『常駐エージェントが見るべきコンテキスト層』を自分たちでどう設計するかという問題に直面する。試す予算がない場合でも、Theo
  が示唆するように OpenClaude や自作 Hermes エージェントで小規模に検証することが現実的な学習経路になる。
en:
  articleTitle: Karpathy's 'Third Paradigm Shift' — Theo (t3.gg) Reluctantly Defends
    Anthropic
  seoTitle: Karpathy's 'Third Paradigm Shift' — Theo (t3.gg) Reluctantly Def
  summary: 'Anthropic''s official pitch: a new paradigm for interacting with Claude.
    Do the under-the-hood integration once and…'
  keyPhrases:
  - Karpathy's third LLM paradigm
  - Ambient behaviour feature
  - Parallel async Claude execution
  - Theo's self-built Hermes agent
  - Org-level harness framing
  - OpenClaude / Hermes self-host
  bulletPoints:
  - time: 0
    text: 'Anthropic''s official pitch: a new paradigm for interacting with Claude.
      Do the under-the-hood integration once and Claude joins the team seamlessly,
      useful across a wide range of workloads. The third major LLM UI / UX redesign.'
  - time: 24
    text: 'First paradigm: the LLM is a website you go to. Second: an app you download.
      Third: a self-contained, persistent, asynchronous entity with org-wide tools
      and context, working alongside teams of humans.'
  - time: 48
    text: Theo's worry — when one of the most important AI researchers alive talks
      about a Slackbot, it's natural to wonder if Karpathy drank the Anthropic Kool-Aid
      too quickly as a recent hire.
  - time: 75
    text: 'What Theo''s going to do in this video, declared up front: three of his
      least favourite things — defend Anthropic, make a video about it, and revisit
      his own priors.'
  - time: 577
    text: Feature detail. With 'ambient behaviour' enabled, Claude proactively keeps
      you updated — flagging relevant info across channels and tools, following up
      on threads or tasks that went quiet. Given how chaotic Slack is, that's actually
      useful.
  - time: 610
    text: Async work. Hand Claude a task and focus elsewhere. Claude schedules itself,
      pursues projects autonomously over hours or days. Anthropic itself says it now
      spends much more time delegating tasks to many Claudes in parallel.
  - time: 632
    text: 'Theo''s own parallel: his self-built Hermes agent, running in a dedicated
      Discord server (Rust port in progress). Claude Tag is the org-scale shape of
      that same idea.'
  - time: 1168
    text: 'Theo''s conclusion: this isn''t a Slackbot, it''s an org-level harness.
      As someone running three companies, he says with 100% confidence Anthropic is
      heading in the right direction. Karpathy got dunked on unfairly — the feature
      is actually cool.'
  sections:
  - heading: What Karpathy actually called the 'third LLM paradigm'
    time: 0
    body: 'Theo (t3.gg) takes Andrej Karpathy''s framing of Claude Tag at face value
      rather than dismissing it. Anthropic''s official description: do the under-the-hood
      integration work once, and Claude joins the team seamlessly. Talk to it like
      you''d talk to a teammate; it handles a wide variety of workloads.


      Karpathy positioned this as the third redesign of LLM interface and UX. The
      first paradigm was that the LLM is a website you go to. The second, an app you
      download. The third — what Claude Tag exemplifies — is a self-contained, persistent,
      asynchronous entity with org-wide tools and context, working alongside teams
      of humans. It takes a while to wrap your head around it, but it works, Karpathy
      says, and it''s impressive.'
  - heading: Theo's reluctant defence — and the feature details that won him over
    time: 48
    body: 'Theo''s honest first reaction was scepticism. When one of the most important
      AI researchers alive talks about what looks like a Slackbot, it''s reasonable
      to wonder if Karpathy drank the Anthropic Kool-Aid too quickly as a recent hire.
      Theo declares up front that he''s about to do three of his least favourite things
      — defend Anthropic, make a video about it, and revisit his own priors.


      The feature details bring him around. With ambient behaviour enabled, Claude
      proactively keeps you updated, flagging relevant information across channels
      and tools, following up on threads or tasks that have gone quiet. Given how
      chaotic Slack typically is, that genuinely helps. The async work model is the
      bigger lever — hand Claude a task and focus on something else, while Claude
      schedules itself and pursues projects autonomously over hours or days. Anthropic
      openly admits it now spends much more of its time delegating to many Claudes
      in parallel.'
  - heading: Hermes parallel — Claude Tag as an org-level harness
    time: 632
    body: 'Theo can speak with unusual authority here because he runs his own version
      of the same idea — a self-built Hermes agent that lives in a dedicated Discord
      server, with a Rust port in progress. His three companies have given him a working
      sense of what this shape of system actually does. That''s the perspective from
      which he can evaluate Claude Tag.


      His closing read is direct, with full confidence. Claude Tag isn''t a Slackbot
      — it''s an org-level harness. From running three companies, he''s saying with
      100% certainty that Anthropic''s direction is right. Karpathy getting dunked
      on by AI Twitter was, he notes, somewhat predictable given how Anthropic-as-a-company
      has been performing publicly lately, but the feature is genuinely cool. For
      readers who don''t want to pay for Claude Enterprise to test it, he suggests
      setting up OpenClaude or a Hermes agent in your own Discord or Slack — you''ll
      see most of the value from there. He didn''t expect to make a video defending
      both Anthropic and Slack — but here he is.'
  editorial: Theo's defence works precisely because he's running the same architecture
    himself and can cross-check Claude Tag against his own experience. Karpathy's
    'third LLM paradigm' framing is strong as a marketing line, but Theo's 'org-level
    harness' is the more accurate operational term. That's the right level of abstraction
    — the harness composes individual agent runs with cross-organisation context and
    parallel execution. Slack integration is just I/O on top of that. Two takeaways
    for readers. For teams considering Claude Tag, the question isn't 'is the Slack
    experience good' — it's 'what context layer should an embedded agent see, and
    how do we design it.' For teams without the budget, Theo's suggestion to run OpenClaude
    or a Hermes agent at small scale is the practical learning path. The shape of
    the future is now clear enough to start practising; what matters is the design
    work upstream of the chat interface.
  headerImage: /images/tOC2N0B9lio/header.png
  heroImage: /images/tOC2N0B9lio/header.png
---

## ハイライト

- [00:00] Anthropicの公式説明: Claudeとの新しい対話パラダイム。表面下の統合作業を済ませれば Claude はチームの一員のように加わり、別の人間と話すように使える。LLM UI / UX の第3の再設計。
- [00:24] 第1のパラダイムは『LLM = アクセスするWebサイト』。第2が『PCにダウンロードするアプリ』。第3が『組織横断のツールとコンテキストを持つ自己完結・永続・非同期エンティティが人間チームと並走する』形態。
- [00:48] Theoの懸念: LLM の先駆者 Karpathy が Slackbot について語っているように聞こえると、彼の判断力を疑いたくなる人もいるはず。最近Anthropic入りしたからKool-Aidを早く飲んだのではないか、と思うのも自然な反応。
- [01:15] Theoが本動画で行うこと: 嫌な仕事を3つする。Anthropicを擁護する、それについて動画を作る、そして自身の信念を改めて検証する。
- [09:37] 機能詳細: ambient behavior をオンにすると Claude は能動的に情報を更新してくれる。チャネル横断で関連情報をフラグ、未解決のまま静かになったスレッドやタスクをフォローアップ。Slackのカオスを考えると本当に便利。
- [10:10] 非同期動作: タスクを Claude に投げて他優先事項に集中可。Claude は自身のタスクをスケジュール化し、プロジェクトを数時間〜数日にわたって自律的に追える。Anthropic自身も並列に多くの Claude にタスク委譲して時間を使うようになった。
- [10:32] Theo自身の対比例: 同じ思想の自作 Hermes エージェント。Discordサーバー専用で動かし、Rust移植も検討中。Claude Tagはこの方向の組織向け実装版。
- [19:28] Theoの結論: 単なる Slackbot ではなく、組織レベルのハーネス。3つの会社を運営している立場から見て、Anthropicの方向性は100%正しい。Karpathyの主張も正当だった、と擁護して動画を締める。

## セクション

### Karpathyが宣言した『LLM第3のパラダイム』とは

- 時刻: 00:00

Theo (t3.gg) は Anthropic の Claude Tag リリースに合わせて、Andrej Karpathy が打ち出したパラダイム議論を真正面から取り上げる。Anthropic公式の説明はこうだ。表面下の統合作業を済ませれば Claude はチームの一員のようにシームレスに加わり、別の人間と話すように使える。多様なワークロードに対応する。

そしてKarpathyがこれを『LLMの第3の再設計』と位置づけた。第1のパラダイムは『LLM = アクセスするWebサイト』。第2が『PCにダウンロードするアプリ』。第3が『組織横断のツールとコンテキストを持つ自己完結・永続・非同期エンティティが人間チームと並走する』形態だ。最初は理解に時間がかかるが、実際に動かしてみるとうまく機能する、というのが Karpathy の主張だ。

### Theoの渋々の擁護 — 機能詳細

- 時刻: 00:48

Theoの正直な反応はまず懐疑だった。LLM の先駆者の一人で AI 界で最も重要な人物の一人である Karpathy が Slackbot について語っているように聞こえると、判断力を疑いたくなる。Anthropic に最近移籍したから Kool-Aid を早く飲んだのではないか、というのも自然な反応だ。Theo は明示的に『嫌な仕事を3つする』と宣言する。Anthropicを擁護する、それについて動画を作る、そして自身の信念を再検証する。

機能詳細を見ていくとTheoは納得していく。ambient behavior をオンにすると Claude は能動的に情報を更新してくれる。チャネル横断で関連情報をフラグし、未解決のまま静かになったスレッドやタスクをフォローアップする。Slackのカオスな性質を考えると、これは現実に役立つ機能だ、とTheoは認める。非同期動作も鍵だ。Claude にタスクを投げて自分は他優先事項に集中、Claude は自身のタスクをスケジュール化し、プロジェクトを数時間〜数日にわたって自律的に追う。Anthropic 自身も並列に多くの Claude にタスク委譲して時間を使うようになった、と公式が認めている。

### Hermes自作実装からの肯定 — 組織レベルハーネスとして

- 時刻: 10:32

Theoが特に説得力を持って語れるのは、自身が同じ思想の自作エージェント Hermes を運用しているからだ。Hermes は専用 Discord サーバーで動き、Rust への移植も検討中だという。彼の3つの会社運営でこの方向が機能していることを実体験しているため、Claude Tag を組織レベルのハーネスとして評価できる。

結論部でTheoは100%の確信を持って言う。Claude Tag は単なる Slackbot ではなく、組織レベルのハーネスだ。3つの会社を運営している立場から見て、Anthropicの方向性は正しい。Karpathy が clowned on された (ネット上で揶揄された) ことについては気の毒だが、Anthropic 入社直後にこれを言わされる立場の悪さもある程度想定される、とコメントする。Anthropic Enterprise の高額プランを払いたくない読者には、OpenClaude や Hermes エージェントを自分の Discord / Slack に立ててみることを薦め、それで本動画で見えた価値が体感できるはずだ、と締める。Anthropic と Slack の両方を擁護する動画を作ることになるとは思わなかった、というのが本人のオチだ。

## 編集部の視点

Theo の擁護動画が説得力を持つのは、彼自身が同じ思想の自作エージェントを運用していて、Claude Tag のコンセプトを自分の体験で検証できる位置にいるからだ。Karpathy が提示した『LLM 第3のパラダイム』フレーミングは、製品マーケティングとしては強い言葉だが、現場の実装視点では『組織レベルハーネス』という Theo の用語の方が機能を正確に捉えている。これは個別のエージェント実行を組織横断のコンテキストと並列実行で組み立て直す抽象化層を指していて、Slack 統合は単なる入出力面に過ぎない。読者にとっての示唆は二段ある。Claude Tag を試す前提のあるチームは、必要なのは Slack 統合の良し悪しではなく、社内ナレッジ・タスク状態・進行プロジェクトを横断する『常駐エージェントが見るべきコンテキスト層』を自分たちでどう設計するかという問題に直面する。試す予算がない場合でも、Theo が示唆するように OpenClaude や自作 Hermes エージェントで小規模に検証することが現実的な学習経路になる。
