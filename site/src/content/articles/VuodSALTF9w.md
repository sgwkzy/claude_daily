---
videoId: VuodSALTF9w
title: Claude Sonnet 5 IS OUT & ITS HORRIBLE! Worst Model By Anthropic EVER? (Fully
  Tested)
slug: claude-sonnet-5-は-anthropic-史上最悪のモデルか-worldofai-の辛口検証-vuodsaltf9w
articleTitle: Claude Sonnet 5 は Anthropic 史上最悪のモデルか — WorldofAI の辛口検証
seoTitle: Claude Sonnet 5 は Anthropic 史上最悪のモデルか — WorldofAI の辛口検証
summary: WorldofAI は Sonnet シリーズ最大のアップデートとして Sonnet 5 を紹介する。幻覚が減り、エージェント性能とツール利用が向上し、ブラウザやターミナルなど各種ツールを自律的に使いこなせる水準に達したと導入部で評価する。
channel: WorldofAI
channelId: UC2WmuBuFq6gL08QYG-JjXKw
publishedAt: '2026-06-30T19:58:13Z'
fetchedAt: '2026-07-01T08:39:58.378543Z'
originalThumbnail: https://i.ytimg.com/vi/VuodSALTF9w/maxresdefault.jpg
headerImage: /images/VuodSALTF9w/header.ja.png
heroImage: /images/VuodSALTF9w/header.ja.png
viewCount: 24846
durationSec: 779
sourceLanguage: en
matchedKeywords:
- Anthropic
proposedByLLM: false
keyPhrases:
- Sonnet 5 ベンチマーク詳細
- トークナイザー効率低下
- GLM 5.2 以下のクリエイティブ評価
- Mac OS クローン実演
- Opus 4.8 継続使用推奨
- 40分・大量トークン消費
bulletPoints:
- time: 0
  text: WorldofAI は Sonnet シリーズ最大のアップデートとして Sonnet 5 を紹介する。幻覚が減り、エージェント性能とツール利用が向上し、ブラウザやターミナルなど各種ツールを自律的に使いこなせる水準に達したと導入部で評価する。
- time: 26
  text: ベンチマークでは Sway の Agentic Coding 検証で63.2%、Terminal Bench 2.1 で80.4%を記録。Opus
    4.8 に肉薄する水準で、HLE や computer use、GDP Evolve では Opus を上回る項目も見られる。
- time: 89
  text: 総合ランキングでは第5位に位置づけられる。まだ評価が進行中のため順位は変動しうるとしつつ、全 Claude プランで既に利用可能になっている点を紹介する。
- time: 424
  text: 実演のMac OS クローン生成では、ランチパッド・Safari・メッセンジャー・カレンダー・音楽アプリ・FPS シューティングゲームまで一通り機能する形で生成された。ただし完成まで約40分、max
    モードで大量のトークンを消費しており効率は良くない。
- time: 693
  text: 検証の本題はここから。新しいトークナイザーの効率が予想を裏切る形で悪く、より多くのトークンを使うのに期待した結果が出ない。これが Opus 4.8
    上位互換としての説得力を弱めている。
- time: 714
  text: SVG などクリエイティブタスクではデザインセンスが GLM 5.2 にも劣ると評価。WorldofAI はこの点で GLM 5.2 以下にランクすると明言し、汎用用途でも
    Sonnet 5 の使用を勧めない立場を取る。
- time: 743
  text: 結論として『Opus 4.8 を使い続けたほうが良い結果が得られる』と断言。Fable 5 の近日再開に期待を寄せつつ、Sonnet 5 自体への評価は厳しいまま締めくくる。
- time: 384
  text: アプリケーション全般が機能する点、SVG生成やトップバー・下部メニューの各種コンポーネントが正常動作する点は好意的に評価。地図アプリのみ Opus
    モデルの生成結果と比べて見劣りすると指摘する。
sections:
- heading: ベンチマークは高評価 — Opus 4.8 に迫る数値
  time: 0
  body: 'WorldofAI はまず好意的な導入で始める。Sonnet シリーズ最大のアップデートであり、最もエージェント性能の高い Sonnet モデル。幻覚が減り、エージェント性、ツール利用能力が向上し、ブラウザやターミナルなど各種ツールを自律的に扱える水準に達したと評価する。


    ベンチマークの数字も具体的だ。Sway の Agentic Coding 検証済みスコアで63.2%、これは Sonnet 4.6 から大きく跳ね上がり Opus
    4.8 に約6ポイント差まで迫る。Terminal Bench 2.1 では80.4%で Opus 4.8 に肉薄。HLE では81.2%とほぼ同水準、computer
    use と GDP Evolve では Opus を上回る項目もある。総合ランキングでは第5位に位置づけられ、全 Claude プランで既に利用可能だ。'
- heading: Mac OS クローン実演 — 機能はするが効率が悪い
  time: 346
  body: '実演として Mac OS クローンを生成させる検証を行う。ランチパッド、Safari、メッセンジャー、メール、写真、カレンダー、ノート、リマインダー、地図、音楽アプリ、さらに
    FPS シューティングゲームまで、一通り機能する形で生成された。各アプリが SVG で生成されている点も見た目の良さとして評価される。


    ただし懸念点も明確だ。完成まで約40分、max モードで大量のトークンを消費しており、効率の面では全く良くない、と WorldofAI は指摘する。地図アプリのみ
    Opus モデルの生成結果と比べて見劣りするという細部の評価も添えられる。全体としては『機能はするが手放しで褒められる出来ではない』という評価だ。'
- heading: トークナイザーの効率悪化とクリエイティブ性能の低さが致命傷
  time: 689
  body: '後半で評価は一転する。最も驚いたのは新しいトークナイザーの効率だ。より多くのトークンを消費するにもかかわらず、新しいモデルに期待するような結果が得られない。この点が、Opus
    4.8 の代わりにこのモデルを使う理由を正当化しづらくする、と WorldofAI は明言する。


    SVG などクリエイティブタスクでは GLM のようなモデルにすら劣ると評価し、『GLM 5.2 以下にランクする』とまで言い切る。汎用用途を含め、このモデルを使うべきではないというのが結論だ。Fable
    5 が近日中に再開されることへの期待を語りつつ、Sonnet 5 自体への評価は『Opus 4.8 を使い続けたほうが良い結果が得られる』という辛口な着地で締めくくられる。'
editorial: 同時期に公開された Alex Finn の好意的レビューと本レビューを並べると、Sonnet 5 の評価は用途によって大きく割れることが分かる。ベンチマーク数値は両者とも認めるが、WorldofAI
  が指摘するトークナイザーの効率悪化とクリエイティブタスクの弱さは、単純なベンチマークスコアでは見えない実運用上の重要な欠陥だ。読者にとっての含意は二つある。第一に、新モデルのリリース直後はベンチマークだけでなく実タスクでのトークン消費効率を必ず自分で検証すべきで、レビュアーによって評価が真逆になる状況では単一のレビューを鵜呑みにするリスクが高い。第二に、Anthropic
  が主要モデルを短期間で連続リリースする現在のペースでは、評価が固まる前に本番導入するコストとリスクを慎重に見積もる必要がある。ベンチマークの高得点と実務での効率性は必ずしも一致しない、という基本原則を再確認させる回だった。
en:
  articleTitle: Is Claude Sonnet 5 Anthropic's Worst Model Ever? WorldofAI's Harsh
    Verdict
  seoTitle: Is Claude Sonnet 5 Anthropic's Worst Model Ever? WorldofAI's Har
  summary: WorldofAI introduces Sonnet 5 as the biggest update to the Sonnet series.
    Reduced hallucination, better agentic…
  keyPhrases:
  - Sonnet 5 benchmark breakdown
  - Tokenizer efficiency regression
  - Ranked below GLM 5.2 on creative tasks
  - Mac OS clone hands-on demo
  - Recommends sticking with Opus 4.8
  - 40 minutes and heavy token spend
  bulletPoints:
  - time: 0
    text: WorldofAI introduces Sonnet 5 as the biggest update to the Sonnet series.
      Reduced hallucination, better agentic performance and tool use, and the ability
      to autonomously operate browsers and terminals at a level rated favorably in
      the opening.
  - time: 26
    text: 'Benchmarks: 63.2% on Sway''s verified Agentic Coding score, 80.4% on Terminal
      Bench 2.1 — nearly matching Opus 4.8, with HLE, computer use, and GDP Evolve
      scores that in some cases surpass Opus.'
  - time: 89
    text: Sonnet 5 lands as the 5th-ranked model overall. Rankings may shift as evaluation
      continues, but it's already available across all Claude plans.
  - time: 424
    text: In a Mac OS clone build demo, the model produces a working launchpad, Safari,
      messenger, calendar, music app, and even an FPS shooter. But it took about 40
      minutes and heavy token spend in max mode — efficiency was poor.
  - time: 693
    text: The real critique starts here. The new tokenizer's efficiency undershoots
      expectations — it burns more tokens without delivering the results you'd expect
      from a newer model. This undercuts the case for using it over Opus 4.8.
  - time: 714
    text: On creative tasks like SVG generation, WorldofAI rates its design taste
      below even GLM 5.2, ranking Sonnet 5 below GLM 5.2 outright and recommending
      against using it for general-purpose work at all.
  - time: 743
    text: 'The conclusion is blunt: ''stick with Opus 4.8 for better results.'' Anticipation
      for Fable 5''s return remains, but the verdict on Sonnet 5 itself stays harsh
      through the close.'
  - time: 384
    text: 'On the positive side: apps generally functioned, SVG generation and top-bar/bottom-menu
      components worked properly. Only the maps app looked noticeably worse than Opus-model
      output.'
  sections:
  - heading: Benchmarks Look Strong — Nearly Matching Opus 4.8
    time: 0
    body: 'WorldofAI opens favorably. Sonnet 5 is the Sonnet series'' biggest update,
      its most agentic Sonnet model yet. Reduced hallucination, better agentic performance,
      improved tool use, and the capability to autonomously operate browsers and terminals
      at a level once reserved for much larger, more expensive models.


      The numbers back it up. Sway''s verified Agentic Coding score comes in at 63.2%,
      a huge jump from Sonnet 4.6 and within about 6 points of Opus 4.8. Terminal
      Bench 2.1 reaches 80.4%, closely rivaling Opus. HLE lands nearly level, and
      computer use plus GDP Evolve scores actually outperform Opus in places. Overall,
      Sonnet 5 ranks 5th and is already rolled out across every Claude plan.'
  - heading: The Mac OS Clone Demo — It Works, But Inefficiently
    time: 346
    body: 'The hands-on test builds a Mac OS clone. Launchpad, Safari, messenger,
      mail, photos, calendar, notes, reminders, maps, music, and even a functional
      FPS shooter all get generated — each app rendered in SVG, which WorldofAI notes
      as a nice visual touch.


      But the concerns are just as clear. The build took roughly 40 minutes and burned
      heavy tokens in max mode — efficiency-wise, not good at all. The maps app looks
      noticeably worse than what Opus models produce. Overall verdict: functional,
      but not something to praise unreservedly.'
  - heading: Tokenizer Inefficiency and Weak Creative Output Land the Killing Blow
    time: 689
    body: 'The second half of the video turns. What surprised WorldofAI most was the
      new tokenizer''s efficiency — it burns more tokens without delivering the results
      you''d expect from a newer model. That makes it hard to justify using this model
      over Opus 4.8, WorldofAI states directly.


      On creative tasks like SVG generation, the design taste falls short of models
      like GLM — WorldofAI goes as far as ranking Sonnet 5 below GLM 5.2, and recommends
      against using it for general-purpose work at all. The video closes anticipating
      Fable 5''s near-term return, but lands on a harsh verdict for Sonnet 5 itself:
      ''you''ll get better results sticking with Opus 4.8.'''
  editorial: Set this review next to Alex Finn's more favorable one published around
    the same time, and Sonnet 5's evaluation clearly splits by use case. Both agree
    on the benchmark numbers, but WorldofAI's flags — tokenizer inefficiency and weak
    creative output — are real-world defects that pure benchmark scores don't surface.
    Two implications for readers. First, right after any major model release, verify
    token-efficiency on real tasks yourself rather than trusting benchmarks alone
    — when reviewers land on opposite verdicts, taking a single review at face value
    carries real risk. Second, given how quickly Anthropic is shipping major model
    releases in succession, deploying to production before evaluations settle needs
    a careful cost-risk calculation. This episode is a clean reminder that a high
    benchmark score and real-world operational efficiency don't always move together.
  headerImage: /images/VuodSALTF9w/header.png
  heroImage: /images/VuodSALTF9w/header.png
---

## ハイライト

- [00:00] WorldofAI は Sonnet シリーズ最大のアップデートとして Sonnet 5 を紹介する。幻覚が減り、エージェント性能とツール利用が向上し、ブラウザやターミナルなど各種ツールを自律的に使いこなせる水準に達したと導入部で評価する。
- [00:26] ベンチマークでは Sway の Agentic Coding 検証で63.2%、Terminal Bench 2.1 で80.4%を記録。Opus 4.8 に肉薄する水準で、HLE や computer use、GDP Evolve では Opus を上回る項目も見られる。
- [01:29] 総合ランキングでは第5位に位置づけられる。まだ評価が進行中のため順位は変動しうるとしつつ、全 Claude プランで既に利用可能になっている点を紹介する。
- [07:04] 実演のMac OS クローン生成では、ランチパッド・Safari・メッセンジャー・カレンダー・音楽アプリ・FPS シューティングゲームまで一通り機能する形で生成された。ただし完成まで約40分、max モードで大量のトークンを消費しており効率は良くない。
- [11:33] 検証の本題はここから。新しいトークナイザーの効率が予想を裏切る形で悪く、より多くのトークンを使うのに期待した結果が出ない。これが Opus 4.8 上位互換としての説得力を弱めている。
- [11:54] SVG などクリエイティブタスクではデザインセンスが GLM 5.2 にも劣ると評価。WorldofAI はこの点で GLM 5.2 以下にランクすると明言し、汎用用途でも Sonnet 5 の使用を勧めない立場を取る。
- [12:23] 結論として『Opus 4.8 を使い続けたほうが良い結果が得られる』と断言。Fable 5 の近日再開に期待を寄せつつ、Sonnet 5 自体への評価は厳しいまま締めくくる。
- [06:24] アプリケーション全般が機能する点、SVG生成やトップバー・下部メニューの各種コンポーネントが正常動作する点は好意的に評価。地図アプリのみ Opus モデルの生成結果と比べて見劣りすると指摘する。

## セクション

### ベンチマークは高評価 — Opus 4.8 に迫る数値

- 時刻: 00:00

WorldofAI はまず好意的な導入で始める。Sonnet シリーズ最大のアップデートであり、最もエージェント性能の高い Sonnet モデル。幻覚が減り、エージェント性、ツール利用能力が向上し、ブラウザやターミナルなど各種ツールを自律的に扱える水準に達したと評価する。

ベンチマークの数字も具体的だ。Sway の Agentic Coding 検証済みスコアで63.2%、これは Sonnet 4.6 から大きく跳ね上がり Opus 4.8 に約6ポイント差まで迫る。Terminal Bench 2.1 では80.4%で Opus 4.8 に肉薄。HLE では81.2%とほぼ同水準、computer use と GDP Evolve では Opus を上回る項目もある。総合ランキングでは第5位に位置づけられ、全 Claude プランで既に利用可能だ。

### Mac OS クローン実演 — 機能はするが効率が悪い

- 時刻: 05:46

実演として Mac OS クローンを生成させる検証を行う。ランチパッド、Safari、メッセンジャー、メール、写真、カレンダー、ノート、リマインダー、地図、音楽アプリ、さらに FPS シューティングゲームまで、一通り機能する形で生成された。各アプリが SVG で生成されている点も見た目の良さとして評価される。

ただし懸念点も明確だ。完成まで約40分、max モードで大量のトークンを消費しており、効率の面では全く良くない、と WorldofAI は指摘する。地図アプリのみ Opus モデルの生成結果と比べて見劣りするという細部の評価も添えられる。全体としては『機能はするが手放しで褒められる出来ではない』という評価だ。

### トークナイザーの効率悪化とクリエイティブ性能の低さが致命傷

- 時刻: 11:29

後半で評価は一転する。最も驚いたのは新しいトークナイザーの効率だ。より多くのトークンを消費するにもかかわらず、新しいモデルに期待するような結果が得られない。この点が、Opus 4.8 の代わりにこのモデルを使う理由を正当化しづらくする、と WorldofAI は明言する。

SVG などクリエイティブタスクでは GLM のようなモデルにすら劣ると評価し、『GLM 5.2 以下にランクする』とまで言い切る。汎用用途を含め、このモデルを使うべきではないというのが結論だ。Fable 5 が近日中に再開されることへの期待を語りつつ、Sonnet 5 自体への評価は『Opus 4.8 を使い続けたほうが良い結果が得られる』という辛口な着地で締めくくられる。

## 編集部の視点

同時期に公開された Alex Finn の好意的レビューと本レビューを並べると、Sonnet 5 の評価は用途によって大きく割れることが分かる。ベンチマーク数値は両者とも認めるが、WorldofAI が指摘するトークナイザーの効率悪化とクリエイティブタスクの弱さは、単純なベンチマークスコアでは見えない実運用上の重要な欠陥だ。読者にとっての含意は二つある。第一に、新モデルのリリース直後はベンチマークだけでなく実タスクでのトークン消費効率を必ず自分で検証すべきで、レビュアーによって評価が真逆になる状況では単一のレビューを鵜呑みにするリスクが高い。第二に、Anthropic が主要モデルを短期間で連続リリースする現在のペースでは、評価が固まる前に本番導入するコストとリスクを慎重に見積もる必要がある。ベンチマークの高得点と実務での効率性は必ずしも一致しない、という基本原則を再確認させる回だった。
