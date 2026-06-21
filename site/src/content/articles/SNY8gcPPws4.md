---
videoId: SNY8gcPPws4
title: 【速報解説】AnthropicのMythos級モデル「Claude Fable 5」をゆる解説 / Mythos 5と何が違う？ / 注目の価格設定
  / 性能が弱体化されているのはなぜ？
slug: claude-fable-5-pricing-filters-data-retention
articleTitle: Claude Fable 5の二段構えと価格・能力フィルタ・データ保持変更を整理する
seoTitle: Claude Fable 5の価格 能力フィルタ データ保持変更を整理
summary: Claude Fable 5 と Mythos 5 の違い、価格設定、能力制限、データ保持方針までをまとめて把握できる記事です。
channel: 安野貴博の自由研究
channelId: UCiMwbmcCSMORJ-85XWhStBw
publishedAt: '2026-06-11T07:22:21Z'
fetchedAt: '2026-06-13T23:58:45.238371Z'
originalThumbnail: https://i.ytimg.com/vi/SNY8gcPPws4/maxresdefault.jpg
headerImage: /images/SNY8gcPPws4/header.ja.png
heroImage: /images/SNY8gcPPws4/header.ja.png
viewCount: 135679
durationSec: 846
sourceLanguage: ja
matchedKeywords:
- Claude
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- Mythos 5
- 能力フィルタ
- トークン価格
- 蒸留防止
- データ保持30日
bulletPoints:
- time: 41
  text: 2026年4月発表のClaude Mythosが、能力過多で公開見送りとなった経緯から二段構えでリリースされた。
- time: 76
  text: Mythos 5は能力フル版で限定提供、Fable 5は能力フィルタを掛けた一般公開版という同一中身の二モデル。
- time: 167
  text: Stripe社の5,000万行のRubyコード移行を、人手なら2か月のところFable 5が1日で完遂した実例が共有された。
- time: 263
  text: トークン価格は入力10ドル・出力50ドルで、前世代Opus 4.8の約2倍、Mythosプレビュー(25/125ドル)より安く着地。
- time: 417
  text: サイバーセキュリティ・生物学・化学・AI開発の4領域で能力を弱体化、蒸留検知時はサイレントに性能を落とす仕組み。
- time: 663
  text: 6月23日まではサブスク内で使え、その後は重量課金へ移行。残り2週間はテスト窓として活用が推奨される。
- time: 724
  text: Fable 5のみデータ保持が30日に変更。エンタープライズのノーリテンション前提が崩れる点が情シスへの注意事項。
sections:
- heading: Mythos 5 / Fable 5 二段構えの背景
  time: 41
  body: 'Anthropicは2026年4月にClaude Mythosを発表したが、サイバーセキュリティの攻撃能力が高すぎるとして一般リリースを見送っていた。発表から約2か月後の6月9日(日本時間6月10日)に、ようやくMythos級モデルが世に出ることになった。


    今回のリリースは少し変則的で、同じモデルを二つの異なる出し方で公開している。能力フル版の「Mythos 5」はセキュリティ業務などごく一部の信頼できる用途にのみ限定提供。一般向けには能力フィルタを掛けた「Fable
    5」が公開された。誰でもアクセスできるのは後者のみだ。'
  image: null
- heading: ベンチマーク制覇とStripe 5,000万行移行の実例
  time: 116
  body: 'Fable 5は多くの主要ベンチマークで1位を取り、しかも他社モデルに僅差ではなくはっきり抜きん出た差を付けている領域も少なくない、と安野氏は整理している。ChatGPTやGeminiといった競合との比較を意識した数字が前面に出された。


    具体例として、Stripeが保有する5,000万行規模のRubyコードベース移行が紹介された。人手なら2か月以上は必要な作業を、Fable 5は1日で完了させたという。さらに、自動化ゲーム「Factorio」をAIで自動化するデモや、ブラウザ上の3D
    CADでプリント可能モデルを設計するデモ、EDMビートに同期した流体シミュレータなど、用途を超えて広く使われている例が並ぶ。'
  image: null
- heading: 価格は前世代の約2倍 - 予算設計が変わる
  time: 263
  body: 'トークン価格はOpus 4.8と比べて約2倍。入力が100万トークンあたり10ドル、出力が50ドル。日本円換算では入力およそ1,600円、出力およそ8,000円という水準だ。


    Mythosプレビューの25ドル/125ドルというリーク情報があったため、安野氏は「もっと高くなるかと思っていた」とコメントしている。それでも前世代の2倍であり、業務AI活用が進む企業の財務担当にとっては、来年の予算上のトークン費用を改めて見積もり直す必要が出てくる水準だ。AIと人間の比率をどう設定するか、そしてこの1年でさらに進化が進むことを前提にどう積むかが、企業の財務側の悩みどころとして提示されている。'
  image: null
- heading: 能力フィルタとサイレント弱体化の仕組み
  time: 417
  body: 'Fable 5にはサイバー攻撃・生物学・化学・AI開発の4領域に能力フィルタが入っている。サイバーは元々の懸念領域、生物学と化学は危険物質やDNA/RNA合成への悪用懸念、AI開発は他社からの蒸留(distillation)に対するブロックとして導入された。


    とくに蒸留に対する扱いが今回の新味だ。他社が自社モデルを使い倒して入出力データを集め、別モデルの学習に使うと判断したケースでは、Anthropicは「サイレントに弱体化する」措置を取り込んでいる。サイレントかどうかすら原則として公開されないため、蒸留を試みた企業は性能が落ちたことに気付きにくい。AI企業同士の競合バトルが新しい段階に入ったと安野氏は評している。'
  image: null
- heading: 6月23日まで2週間はテスト窓、保持ポリシーも30日に変更
  time: 663
  body: 'Fable 5は当面、サブスクリプションプランの一部として使えるが、6月23日以降は使った分だけ課金される重量課金へ移行する。残り2週間は事実上の評価期間として、既存コードベースの課題を一気に掘り起こすために使うのがおすすめだと安野氏は薦める。


    もう一点、運用上の注意点としてデータ保持ポリシーの変更がある。Fable 5は安全性確認のため30日間のデータ保持が入っており、これまでエンタープライズプランでノーリテンションを前提に運用してきた組織にとっては前提が変わる。情報システム部門は自社のデータポリシーに照らして取り扱いを再点検しておきたい。'
  image: null
en:
  articleTitle: 'Claude Fable 5 Explained: Pricing, Capability Filters, and Data Retention
    Changes'
  seoTitle: 'Claude Fable 5 Explained: Pricing, Capability Filters, and Data'
  summary: Claude Mythos, announced in April 2026 but held back from release because
    it was too capable, was ultimately launched…
  keyPhrases:
  - Claude Fable 5
  - Mythos 5
  - capability filters
  - token pricing
  - distillation prevention
  - 30-day data retention
  bulletPoints:
  - time: 41
    text: Claude Mythos, announced in April 2026 but held back from release because
      it was too capable, was ultimately launched in a two-tier structure.
  - time: 76
    text: Mythos 5 is the full-capability version offered on a limited basis, while
      Fable 5 is the public release with capability filters applied to the same underlying
      model.
  - time: 167
    text: One shared example claimed Fable 5 migrated Stripe’s 50 million lines of
      Ruby code in one day, versus roughly two months by hand.
  - time: 263
    text: Token pricing lands at $10 input and $50 output, about 2x the previous Opus
      4.8 generation and below the leaked Mythos preview pricing of $25/$125.
  - time: 417
    text: 'Capabilities are weakened across four domains: cybersecurity, biology,
      chemistry, and AI development. If distillation is detected, performance is silently
      reduced.'
  - time: 663
    text: The model remains included in subscriptions through June 23, then shifts
      to usage-based billing. The remaining two weeks are framed as a good test window.
  - time: 724
    text: Only Fable 5 moves to 30-day data retention, a change enterprise IT teams
      need to watch because it breaks prior no-retention assumptions.
  sections:
  - heading: Why Anthropic Split Mythos 5 and Fable 5
    time: 41
    body: 'Anthropic announced Claude Mythos in April 2026, but held back a general
      release because its offensive cybersecurity capabilities were considered too
      strong. About two months later, on June 9 (June 10 in Japan time), a Mythos-class
      model finally reached the market.


      This launch was unusual because the same underlying model was released in two
      different forms. The full-capability version, "Mythos 5," is restricted to a
      narrow set of trusted use cases such as security work. The public-facing release
      is "Fable 5," which applies capability filters. Only the latter is broadly accessible.'
    image: null
  - heading: Benchmark Lead and the 50-Million-Line Stripe Migration
    time: 116
    body: 'Yasuno argues that Fable 5 ranks first across many major benchmarks, and
      not just by slim margins. In several areas, he says, it opens up a visibly larger
      lead over competing models such as ChatGPT and Gemini.


      As a concrete example, he points to the migration of Stripe’s 50-million-line
      Ruby codebase. Work that would have taken more than two months manually was
      reportedly completed by Fable 5 in a single day. He also highlights demos ranging
      from automating the game Factorio, to designing printable models in browser-based
      3D CAD, to a fluid simulator synced to EDM beats, as signs of unusually broad
      applicability.'
    image: null
  - heading: Twice the Previous Generation’s Price Changes Budget Planning
    time: 263
    body: 'Compared with Opus 4.8, token pricing is roughly double: $10 per million
      input tokens and $50 per million output tokens. In yen terms, that works out
      to around 1,600 yen for input and 8,000 yen for output.


      Because leaked Mythos preview pricing had suggested $25 input and $125 output,
      Yasuno says he expected it to come in even higher. Even so, doubling versus
      the previous generation is enough that finance teams at companies scaling AI
      use will need to revisit next year’s token budgets. The segment frames this
      as a broader planning problem: how to set the right balance between AI and human
      labor while assuming the models will keep improving over the next year.'
    image: null
  - heading: Capability Filters and Silent Degradation
    time: 417
    body: 'Fable 5 includes capability filters across four domains: cyberattacks,
      biology, chemistry, and AI development. Cyber was already the core concern.
      Biology and chemistry were added because of possible misuse involving dangerous
      substances or DNA/RNA synthesis. AI development restrictions were introduced
      to block distillation by rival labs.


      The distillation response is the most novel part. If Anthropic decides another
      company is using its model to collect input-output data for training a different
      model, it can silently degrade performance. Because the company does not normally
      disclose whether the downgrade is happening, a firm attempting distillation
      may not easily notice that the model has been weakened. Yasuno describes this
      as a sign that competition among AI companies has entered a new phase.'
    image: null
  - heading: Two-Week Test Window and a New 30-Day Retention Policy
    time: 663
    body: 'For now, Fable 5 is available as part of subscription plans, but after
      June 23 it will move to usage-based billing. Yasuno recommends using the remaining
      two weeks as a de facto evaluation period, especially to surface issues hidden
      inside existing codebases all at once.


      There is also an operational caveat: the data retention policy changes. Fable
      5 retains data for 30 days for safety verification. That alters the assumptions
      for organizations that had been operating enterprise plans on a no-retention
      basis. IT departments will want to review how that fits with their internal
      data policies.'
    image: null
  headerImage: /images/SNY8gcPPws4/header.png
  heroImage: /images/SNY8gcPPws4/header.png
---

## ハイライト

- [00:41] 2026年4月発表のClaude Mythosが、能力過多で公開見送りとなった経緯から二段構えでリリースされた。
- [01:16] Mythos 5は能力フル版で限定提供、Fable 5は能力フィルタを掛けた一般公開版という同一中身の二モデル。
- [02:47] Stripe社の5,000万行のRubyコード移行を、人手なら2か月のところFable 5が1日で完遂した実例が共有された。
- [04:23] トークン価格は入力10ドル・出力50ドルで、前世代Opus 4.8の約2倍、Mythosプレビュー(25/125ドル)より安く着地。
- [06:57] サイバーセキュリティ・生物学・化学・AI開発の4領域で能力を弱体化、蒸留検知時はサイレントに性能を落とす仕組み。
- [11:03] 6月23日まではサブスク内で使え、その後は重量課金へ移行。残り2週間はテスト窓として活用が推奨される。
- [12:04] Fable 5のみデータ保持が30日に変更。エンタープライズのノーリテンション前提が崩れる点が情シスへの注意事項。

## セクション

### Mythos 5 / Fable 5 二段構えの背景

- 時刻: 00:41

Anthropicは2026年4月にClaude Mythosを発表したが、サイバーセキュリティの攻撃能力が高すぎるとして一般リリースを見送っていた。発表から約2か月後の6月9日(日本時間6月10日)に、ようやくMythos級モデルが世に出ることになった。

今回のリリースは少し変則的で、同じモデルを二つの異なる出し方で公開している。能力フル版の「Mythos 5」はセキュリティ業務などごく一部の信頼できる用途にのみ限定提供。一般向けには能力フィルタを掛けた「Fable 5」が公開された。誰でもアクセスできるのは後者のみだ。

### ベンチマーク制覇とStripe 5,000万行移行の実例

- 時刻: 01:56

Fable 5は多くの主要ベンチマークで1位を取り、しかも他社モデルに僅差ではなくはっきり抜きん出た差を付けている領域も少なくない、と安野氏は整理している。ChatGPTやGeminiといった競合との比較を意識した数字が前面に出された。

具体例として、Stripeが保有する5,000万行規模のRubyコードベース移行が紹介された。人手なら2か月以上は必要な作業を、Fable 5は1日で完了させたという。さらに、自動化ゲーム「Factorio」をAIで自動化するデモや、ブラウザ上の3D CADでプリント可能モデルを設計するデモ、EDMビートに同期した流体シミュレータなど、用途を超えて広く使われている例が並ぶ。

### 価格は前世代の約2倍 - 予算設計が変わる

- 時刻: 04:23

トークン価格はOpus 4.8と比べて約2倍。入力が100万トークンあたり10ドル、出力が50ドル。日本円換算では入力およそ1,600円、出力およそ8,000円という水準だ。

Mythosプレビューの25ドル/125ドルというリーク情報があったため、安野氏は「もっと高くなるかと思っていた」とコメントしている。それでも前世代の2倍であり、業務AI活用が進む企業の財務担当にとっては、来年の予算上のトークン費用を改めて見積もり直す必要が出てくる水準だ。AIと人間の比率をどう設定するか、そしてこの1年でさらに進化が進むことを前提にどう積むかが、企業の財務側の悩みどころとして提示されている。

### 能力フィルタとサイレント弱体化の仕組み

- 時刻: 06:57

Fable 5にはサイバー攻撃・生物学・化学・AI開発の4領域に能力フィルタが入っている。サイバーは元々の懸念領域、生物学と化学は危険物質やDNA/RNA合成への悪用懸念、AI開発は他社からの蒸留(distillation)に対するブロックとして導入された。

とくに蒸留に対する扱いが今回の新味だ。他社が自社モデルを使い倒して入出力データを集め、別モデルの学習に使うと判断したケースでは、Anthropicは「サイレントに弱体化する」措置を取り込んでいる。サイレントかどうかすら原則として公開されないため、蒸留を試みた企業は性能が落ちたことに気付きにくい。AI企業同士の競合バトルが新しい段階に入ったと安野氏は評している。

### 6月23日まで2週間はテスト窓、保持ポリシーも30日に変更

- 時刻: 11:03

Fable 5は当面、サブスクリプションプランの一部として使えるが、6月23日以降は使った分だけ課金される重量課金へ移行する。残り2週間は事実上の評価期間として、既存コードベースの課題を一気に掘り起こすために使うのがおすすめだと安野氏は薦める。

もう一点、運用上の注意点としてデータ保持ポリシーの変更がある。Fable 5は安全性確認のため30日間のデータ保持が入っており、これまでエンタープライズプランでノーリテンションを前提に運用してきた組織にとっては前提が変わる。情報システム部門は自社のデータポリシーに照らして取り扱いを再点検しておきたい。
