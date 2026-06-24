---
videoId: YAS4ojuhbW4
title: Stop Prompting Claude. Start Loop Engineering.
slug: claudeはもうプロンプトしない時代-loop-engineering入門と4つの必須要素-yas4ojuhbw4
articleTitle: Claudeはもうプロンプトしない時代 — Loop Engineering入門と4つの必須要素
seoTitle: Claudeはもうプロンプトしない時代 — Loop Engineering入門と4つの必須要素
summary: Claude Code作者Boris Cherny氏が『もうClaudeにプロンプトしない、僕の仕事はループを書くことだ』と発言。Open Claude作者Peter…
channel: Austin Marchese
channelId: UCFeFVytEkT8kaqPCJZGFswg
publishedAt: '2026-06-19T13:45:19Z'
fetchedAt: '2026-06-22T03:01:58.768492Z'
originalThumbnail: https://i.ytimg.com/vi/YAS4ojuhbW4/maxresdefault.jpg
headerImage: /images/YAS4ojuhbW4/header.ja.png
heroImage: /images/YAS4ojuhbW4/header.ja.png
viewCount: 33740
durationSec: 735
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Loop Engineering
- Boris Cherny提言
- ループのゴールと検証
- /engineer-reviewスキル
- human verification checkpoint
- loop orchestration skill
bulletPoints:
- time: 0
  text: Claude Code作者Boris Cherny氏が『もうClaudeにプロンプトしない、僕の仕事はループを書くことだ』と発言。Open Claude作者Peter
    Steinberg氏も同様の主張で『コーディングエージェントに自分でプロンプトする時代は終わった』と述べた。
- time: 16
  text: ループエンジニアリングは複雑に見えて実はシンプル。動画では3パートで体系化する。ループの定義／必須4要素／非技術者でも作れる最初の1本の作り方。
- time: 49
  text: 通常のプロンプトは1回実行して終了。ループは特定のタスクや目標が完了するまでプロンプトを繰り返し走らせる仕組み。Borisは『ループがClaudeにプロンプトしている、僕は次の抽象レイヤに移った』と語る。
- time: 320
  text: 成功するループには『ゴール』と『検証』のペアが必須。ゴールを定義しても、その達成を検証できなければループは終われない。両者は不可分。
- time: 332
  text: '技術タスクの例: 『このドメインにサイトをデプロイし、ロード時間2秒以内にすること』。検証はAIがそのドメインにアクセスし、期待コンテンツ確認・ロード時間計測・/engineer-reviewスキルの承認、までを自動でループ。'
- time: 367
  text: 非技術タスクの鍵は『抽象を検証可能な形に橋渡しする』こと。コードの良し悪しすら『/engineer-reviewスキル』が承認/非承認の二値に落とせる。同じ発想で定性的タスクも構造化できる。
- time: 663
  text: 'ルール: ゴールが定量化しにくいほど、ループを小さなサブゴールに分解し、要所要所に人間の検証チェックポイントを置く。AIをインターン扱いするとイメージしやすい。'
- time: 712
  text: 非定量タスクほど『誤った方向に進むと残り全てが台無しになる分岐点』を人間が必ず検証する設計が重要。loop orchestration skillとして小さく始めるのが推奨。
sections:
- heading: 『プロンプトする時代は終わった』 — Boris CherneyとPeter Steinbergが揃って提言
  time: 0
  body: 'Claude Code作者のBoris Cherny氏が公の場で『僕はもうClaudeにプロンプトしない。僕の仕事はループを書くことだ』と明言した。さらにOpen
    Claude作者のPeter Steinberg氏もまったく同じ趣旨のツイートを投下している。『コーディングエージェントに自分で直接プロンプトを送るのはやめて、エージェントにプロンプトを送るループを設計せよ』。


    AI界はハイプに満ちているが、私たちが日々使っているツールの作者2人が揃って同じことを言うなら聞く価値がある。動画作者はこの提言を受けて『ループエンジニアリング』を深掘りし、3パート構成で解説する。ループとは何か／成功するループの4要素／技術知識ゼロでも今日作れる最初のループ、という流れだ。'
- heading: ループの本質 — ゴールと検証の不可分性
  time: 320
  body: '通常のプロンプトは1回実行して止まる。対してループは、特定のゴールが完了するまで何度でも自走するプロンプトの集合体だ。Boris氏自身の働き方を引用すると『ループが回っている。ループが
    Claude にプロンプトを投げている。僕の仕事はその上の抽象レイヤに移った』。


    成功するループにはゴールと検証が必ずセットで必要となる。検証ができなければゴールが達成された証拠が無く、ループは終われない。技術タスクは比較的単純で、『このドメインにサイトをデプロイ、ロード時間2秒未満』というゴールなら、AIがドメインへアクセスして期待コンテンツ確認・ロード時間計測・/engineer-reviewスキルの承認、を自動で繰り返せばよい。'
- heading: 非技術タスクと人間チェックポイント — 最初のループを作るコツ
  time: 367
  body: '非技術タスクのループは『抽象を検証可能な形に橋渡しする』ところがキモだ。『コードの良し悪し』のような曖昧な概念も、/engineer-reviewスキルを通せば『承認／非承認』の二値判定に落とせる。同じ発想を非技術タスクにも適用すれば、定量化しにくい結果でも検証可能なステップを設計できる。


    ルールはシンプルで、ゴールが定量化しにくいほど小さなサブゴールへ分解し、各チェックポイントで成果を確認する。AIをインターン扱いしてみよう。『社内パーティを企画して』と丸投げすると何でもしてしまうが、『日程』『会場』『テーマ』のような重要分岐点では人間が必ず判断する。これがループのhuman
    verification checkpointだ。非定量タスクほど、AIが誤った方向へ進むと残り全てが台無しになる分岐点を人間が押さえる設計が重要になる。動画作者は『loop
    orchestration skillとして小さく始めるのが最良の入口だ』と締め括る。'
editorial: 「もうプロンプトしない、僕の仕事はループを書くことだ」というBoris Cherny氏の提言は、抽象レイヤーの一段上への移行を宣言している。要点は『ゴールと検証は不可分』という原則——達成を検証できなければループは終われない。非定量タスクを検証可能な二値に落とし込み、誤れば全てが台無しになる分岐点に人間のチェックポイントを置く設計思想は、エージェント運用の最も実践的な骨格を与える。
en:
  articleTitle: Stop Prompting Claude — Loop Engineering and the Four Things Every
    Loop Needs
  seoTitle: Stop Prompting Claude — Loop Engineering and the Four Things Eve
  summary: 'Claude Code creator Boris Cherny said it out loud: ''I don''t prompt Claude
    anymore. My job is to write loops.'' Peter…'
  keyPhrases:
  - loop engineering
  - Boris Cherny on loops
  - goal and verification pairing
  - /engineer-review skill
  - human verification checkpoints
  - loop orchestration skill
  bulletPoints:
  - time: 0
    text: 'Claude Code creator Boris Cherny said it out loud: ''I don''t prompt Claude
      anymore. My job is to write loops.'' Peter Steinberg, creator of Open Claude,
      posted the same idea. Stop prompting coding agents — design the loops that prompt
      them.'
  - time: 16
    text: 'Loop engineering looks complex but is actually simple — most people overcomplicate
      it. The video breaks it into three parts: what a loop is, the four things every
      successful loop needs, and how to build your first one today.'
  - time: 49
    text: 'A normal prompt runs once and stops. A loop runs over and over until a
      specific task or goal is complete. Boris: the loops prompt Claude now, and his
      job moved to the next level of abstraction.'
  - time: 320
    text: Every successful loop pairs a goal with a verification. You can't have a
      goal unless you can verify it was reached, and verification gives the loop its
      terminator.
  - time: 332
    text: 'Technical example: ''launch a website to this domain and make sure it loads
      in under 2 seconds.'' Verification — AI hits the domain, checks expected content,
      calculates load time, and runs /engineer-review for sign-off.'
  - time: 367
    text: 'Non-technical tasks need the same shape: bridge the abstract to something
      verifiable. ''Is this code good?'' becomes ''did /engineer-review approve?''
      Same move scales to fuzzier tasks.'
  - time: 663
    text: 'Rule of thumb: the harder a goal is to quantify, the smaller the sub-goals
      you should break it into, with checkpoints at each one. Treat the AI like an
      intern handling a corporate party — you still pick the date, venue, and theme
      yourself.'
  - time: 712
    text: For non-measurable tasks, mark every key fork where a wrong turn ruins the
      rest of the loop, and verify those by hand. Start small — build one loop orchestration
      skill for something concrete.
  sections:
  - heading: '''The prompting era is over'' — Boris Cherny and Peter Steinberg say
      the same thing'
    time: 0
    body: 'Claude Code creator Boris Cherny said the quiet part out loud: ''I don''t
      prompt Claude anymore. My job is to write loops.'' Peter Steinberg, creator
      of Open Claude, posted the same idea on Twitter — stop prompting coding agents,
      design the loops that prompt them instead.


      AI Twitter is full of hype, but when two of the people who built the tools we
      use every day land on the same point on the same week, it earns attention. The
      video author takes the claim seriously and breaks loop engineering into three
      parts: what a loop actually is, the four ingredients of a successful loop, and
      how a non-technical person can build their first one today.'
  - heading: What a loop actually is — goal and verification are inseparable
    time: 320
    body: 'A normal prompt runs once and stops. A loop is a prompt structure that
      runs over and over until a specific goal is complete. Boris''s own framing:
      loops are now the things prompting Claude, and his job moved one level up the
      abstraction stack.


      For a loop to work, it needs a goal and a way to verify the goal. The two are
      inseparable — without verification, the loop has no stopping condition. Technical
      tasks make this easy. ''Deploy this site and make sure it loads in under 2 seconds''
      has obvious verification: hit the domain, check content, time the load, and
      run /engineer-review for the final yes/no.'
  - heading: Non-technical loops and human checkpoints — building your first one
    time: 367
    body: 'Non-technical loops are about bridging an abstract goal to a verifiable
      signal. The /engineer-review skill collapses ''is the code good?'' into a yes/no
      answer. The same move works on fuzzier tasks — find a way to verify the final
      result even when it isn''t strictly measurable.


      The operating rule: the less quantifiable your goal, the smaller the sub-goals
      you should break it into, with checkpoints at each one. Treat the AI like an
      intern. ''Plan a corporate party'' could go anywhere; you''d still want to make
      the date, venue, and theme calls yourself. Same with loops — mark the forks
      where one wrong turn ruins the rest of the run, and verify those by hand. The
      author''s closing advice: pick something small and build a single loop orchestration
      skill for it. That''s how the muscle gets built.'
  editorial: 'Boris Cherny''s claim — ''I no longer prompt; my job is to write loops''
    — declares a move up one level of abstraction. The crux is the principle that
    goal and verification are inseparable: a loop can''t end if you can''t verify
    completion. Reducing non-quantitative tasks to a verifiable binary and placing
    human checkpoints at branch points where a wrong turn ruins everything gives the
    most practical skeleton for operating agents.'
  headerImage: /images/YAS4ojuhbW4/header.png
  heroImage: /images/YAS4ojuhbW4/header.png
---

## ハイライト

- [00:00] Claude Code作者Boris Cherny氏が『もうClaudeにプロンプトしない、僕の仕事はループを書くことだ』と発言。Open Claude作者Peter Steinberg氏も同様の主張で『コーディングエージェントに自分でプロンプトする時代は終わった』と述べた。
- [00:16] ループエンジニアリングは複雑に見えて実はシンプル。動画では3パートで体系化する。ループの定義／必須4要素／非技術者でも作れる最初の1本の作り方。
- [00:49] 通常のプロンプトは1回実行して終了。ループは特定のタスクや目標が完了するまでプロンプトを繰り返し走らせる仕組み。Borisは『ループがClaudeにプロンプトしている、僕は次の抽象レイヤに移った』と語る。
- [05:20] 成功するループには『ゴール』と『検証』のペアが必須。ゴールを定義しても、その達成を検証できなければループは終われない。両者は不可分。
- [05:32] 技術タスクの例: 『このドメインにサイトをデプロイし、ロード時間2秒以内にすること』。検証はAIがそのドメインにアクセスし、期待コンテンツ確認・ロード時間計測・/engineer-reviewスキルの承認、までを自動でループ。
- [06:07] 非技術タスクの鍵は『抽象を検証可能な形に橋渡しする』こと。コードの良し悪しすら『/engineer-reviewスキル』が承認/非承認の二値に落とせる。同じ発想で定性的タスクも構造化できる。
- [11:03] ルール: ゴールが定量化しにくいほど、ループを小さなサブゴールに分解し、要所要所に人間の検証チェックポイントを置く。AIをインターン扱いするとイメージしやすい。
- [11:52] 非定量タスクほど『誤った方向に進むと残り全てが台無しになる分岐点』を人間が必ず検証する設計が重要。loop orchestration skillとして小さく始めるのが推奨。

## セクション

### 『プロンプトする時代は終わった』 — Boris CherneyとPeter Steinbergが揃って提言

- 時刻: 00:00

Claude Code作者のBoris Cherny氏が公の場で『僕はもうClaudeにプロンプトしない。僕の仕事はループを書くことだ』と明言した。さらにOpen Claude作者のPeter Steinberg氏もまったく同じ趣旨のツイートを投下している。『コーディングエージェントに自分で直接プロンプトを送るのはやめて、エージェントにプロンプトを送るループを設計せよ』。

AI界はハイプに満ちているが、私たちが日々使っているツールの作者2人が揃って同じことを言うなら聞く価値がある。動画作者はこの提言を受けて『ループエンジニアリング』を深掘りし、3パート構成で解説する。ループとは何か／成功するループの4要素／技術知識ゼロでも今日作れる最初のループ、という流れだ。

### ループの本質 — ゴールと検証の不可分性

- 時刻: 05:20

通常のプロンプトは1回実行して止まる。対してループは、特定のゴールが完了するまで何度でも自走するプロンプトの集合体だ。Boris氏自身の働き方を引用すると『ループが回っている。ループが Claude にプロンプトを投げている。僕の仕事はその上の抽象レイヤに移った』。

成功するループにはゴールと検証が必ずセットで必要となる。検証ができなければゴールが達成された証拠が無く、ループは終われない。技術タスクは比較的単純で、『このドメインにサイトをデプロイ、ロード時間2秒未満』というゴールなら、AIがドメインへアクセスして期待コンテンツ確認・ロード時間計測・/engineer-reviewスキルの承認、を自動で繰り返せばよい。

### 非技術タスクと人間チェックポイント — 最初のループを作るコツ

- 時刻: 06:07

非技術タスクのループは『抽象を検証可能な形に橋渡しする』ところがキモだ。『コードの良し悪し』のような曖昧な概念も、/engineer-reviewスキルを通せば『承認／非承認』の二値判定に落とせる。同じ発想を非技術タスクにも適用すれば、定量化しにくい結果でも検証可能なステップを設計できる。

ルールはシンプルで、ゴールが定量化しにくいほど小さなサブゴールへ分解し、各チェックポイントで成果を確認する。AIをインターン扱いしてみよう。『社内パーティを企画して』と丸投げすると何でもしてしまうが、『日程』『会場』『テーマ』のような重要分岐点では人間が必ず判断する。これがループのhuman verification checkpointだ。非定量タスクほど、AIが誤った方向へ進むと残り全てが台無しになる分岐点を人間が押さえる設計が重要になる。動画作者は『loop orchestration skillとして小さく始めるのが最良の入口だ』と締め括る。

## 編集部の視点

「もうプロンプトしない、僕の仕事はループを書くことだ」というBoris Cherny氏の提言は、抽象レイヤーの一段上への移行を宣言している。要点は『ゴールと検証は不可分』という原則——達成を検証できなければループは終われない。非定量タスクを検証可能な二値に落とし込み、誤れば全てが台無しになる分岐点に人間のチェックポイントを置く設計思想は、エージェント運用の最も実践的な骨格を与える。
