---
videoId: vcU85OrwuV0
title: How Anthropic Engineers Actually Prompt Fable 5
slug: anthropicのエンジニアはどう使うclaude-fable-5プロンプトの実践6箇条-vcu85orwuv0
articleTitle: Anthropicのエンジニアはどう使う？Claude Fable 5プロンプトの実践6箇条
seoTitle: Anthropicのエンジニアはどう使う？Claude Fable 5プロンプトの実践6箇条
summary: Claude Fable 5は筆者がこれまで使った中で最も強力なモデルだと評価し、公式ベストプラクティス文書を読み込んで6つのコツに凝縮した。
channel: Nate Herk | AI Automation
channelId: UC2ojq-nuP8ceeHqiroeKhBA
publishedAt: '2026-07-01T21:21:58Z'
fetchedAt: '2026-07-02T13:29:28.028816Z'
originalThumbnail: https://i.ytimg.com/vi/vcU85OrwuV0/maxresdefault.jpg
headerImage: /images/vcU85OrwuV0/header.ja.png
heroImage: /images/vcU85OrwuV0/header.ja.png
viewCount: 31440
durationSec: 645
sourceLanguage: en
matchedKeywords:
- Anthropic
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- プロンプトエンジニアリング
- エフォートレベル
- Opus 4.8
- ネガティブプロンプティング
- Anthropic
bulletPoints:
- time: 0
  text: Claude Fable 5は筆者がこれまで使った中で最も強力なモデルだと評価し、公式ベストプラクティス文書を読み込んで6つのコツに凝縮した。
- time: 25
  text: 料金はOpusの2倍で、入力$10/百万トークン、出力$50/百万トークン。プロモーション期間は7月7日までと期限が短い。
- time: 48
  text: プロモーション期間中はウィークリー上限の最大50%までは追加課金なしで使え、それ以降は使用量クレジットが必要になる。
- time: 283
  text: 具体的な指示だけでなく、してほしくないことを伝える「ネガティブプロンプティング」も有効に働くケースが増えている。
- time: 305
  text: 計画モードを常用するのではなく「十分な情報が集まったら行動せよ」という指示で過剰な計画立てを防ぐのが公式推奨の第一歩。
- time: 344
  text: 低・中・高・エクストラハイという複数の思考努力(effort)レベルをタスクの難易度に応じて使い分けることが重要。
- time: 571
  text: 危険性の高い依頼(ハッキングや危険な生物学など)を検知すると、Fable 5は静かにOpus 4.8へルーティングして安全確認を行う。
sections:
- heading: コストと利用条件を最初に押さえる
  time: 25
  body: 'Claude Fable 5はOpusの2倍という高価格帯のモデルで、入力トークン$10/百万、出力トークン$50/百万というコスト構造を持つ。Claudeプランに常時含まれるわけではなく、現時点は「プロモーション期間」という位置づけで提供されている。


    この期間中はウィークリー上限の最大50%まで追加課金なしで利用できるが、それを超えると使用量クレジットへの切り替えが必要になる。プロモーション終了は7月7日と迫っており、無駄なトークン消費を避ける実践的な使い方の重要性が増している。'
- heading: 計画させすぎない・エフォートレベルを使い分ける
  time: 305
  body: '公式ドキュメントが最初に挙げる推奨は「十分な情報を集めたら計画を練り続けずに行動へ移す」よう促すことだ。筆者自身も以前は「必ずPlanモードから始める」としていたが、現在はPlanモードを常用せず、独自のプロンプトで「行動できる状態になったら行動せよ」と指示する運用に切り替えている。


    難しいタスクでは高いエフォートレベルで数分間にわたる処理が発生しうるため、低・中・高・エクストラハイの4段階を、タスクの複雑さや必要なコンテキスト収集量に応じて選び分けることが推奨されている。'
- heading: 危険な依頼は静かにOpusへルーティングされる
  time: 571
  body: 'Fable 5には安全性チェックの仕組みが組み込まれており、ハッキング支援や危険な生物学、モデル自身の内部推論の開示要求など特定のカテゴリに該当すると判断した場合、ユーザーに知らせないままOpus
    4.8へリクエストを静かにルーティングする。


    API経由であればレスポンスにOpusが処理したことが明示されるが、通常の利用では気づかないことが多い。幸いルーティング先はOpus 4.8のため、Fable
    5ほどのコストは発生しない。明らかに悪意のある依頼を避けることが、この予期せぬルーティングを回避する最善の方法だ。'
editorial: エフォートレベルの使い分けや「計画させすぎない」という指針は、Fable 5に限らず高性能・高コストなモデル全般に応用できる汎用的な運用知見だ。特に注目すべきは、危険とみなされたリクエストが利用者に知らせずOpusへ自動ルーティングされる仕組みで、これはモデル自身がガードレールとコスト管理を兼ねる設計思想を示している。プロモーション期間という限定的な無料枠の存在は、企業がモデル選定の意思決定を急がされる状況を生みやすく、コスト試算を後回しにしないよう注意喚起する材料になる。
en:
  articleTitle: 'How Anthropic Engineers Actually Prompt Claude Fable 5: Six Practical
    Rules'
  seoTitle: 'How Anthropic Engineers Actually Prompt Claude Fable 5: Six Prac'
  summary: The creator calls Claude Fable 5 the strongest model he's ever used, and
    distilled Anthropic's best-practices docs…
  keyPhrases:
  - Claude Fable 5
  - prompt engineering
  - effort levels
  - Opus 4.8
  - negative prompting
  - Anthropic
  bulletPoints:
  - time: 0
    text: The creator calls Claude Fable 5 the strongest model he's ever used, and
      distilled Anthropic's best-practices docs into six simple, effective habits.
  - time: 25
    text: Fable 5 costs double Opus -- $10 per million input tokens and $50 per million
      output tokens -- and the promotional access window is short.
  - time: 48
    text: During the promo period, up to 50% of weekly limits can be used at no extra
      cost; beyond that, usage credits are required.
  - time: 283
    text: Being specific isn't enough -- negative prompting (telling the model what
      not to do) is increasingly effective too.
  - time: 305
    text: Rather than always starting in Plan mode, the top recommendation is to let
      the model act once it has gathered enough information.
  - time: 344
    text: Effort levels -- low, medium, high, and extra-high -- should be matched
      to task difficulty rather than left on a default.
  - time: 571
    text: If a request looks like it involves hacking, dangerous biology, or exposing
      internal reasoning, Fable 5 silently reroutes it to Opus 4.8 for a safety check.
  sections:
  - heading: Cost and Access Come First
    time: 25
    body: 'Claude Fable 5 sits in a premium price tier -- double Opus at $10 per million
      input tokens and $50 per million output tokens -- and isn''t always included
      in a standard Claude plan. It''s currently offered through a ''promotional period''
      rather than as a permanent inclusion.


      During that window, up to 50% of weekly limits can be used with no extra charge,
      after which usage credits kick in. With the promo ending July 7, using tokens
      efficiently -- not wastefully -- matters more than ever.'
  - heading: Don't Over-Plan, and Match Effort to the Task
    time: 305
    body: 'Anthropic''s own documentation leads with a simple recommendation: once
      a model has gathered enough information, let it act instead of continuing to
      plan indefinitely. The creator says he no longer defaults to Plan mode -- something
      he used to always recommend -- and instead prompts the model to act as soon
      as it''s ready.


      Because hard tasks at higher effort settings can run for many minutes while
      gathering context and self-verifying, choosing the right effort level -- low,
      medium, high, or extra-high -- for the task at hand is one of the biggest levers
      for both quality and cost.'
  - heading: Risky Requests Get Silently Rerouted to Opus
    time: 571
    body: 'Fable 5 includes a built-in safety check. If a request falls into a sensitive
      category -- hacking assistance, dangerous biology, or attempts to expose the
      model''s private reasoning -- it gets silently rerouted to Opus 4.8 without
      notifying the user in the standard interface.


      API users do see a flag indicating Opus handled the response, but most users
      won''t notice. The routing is fortunately to Opus 4.8 rather than continuing
      on Fable 5''s pricier tier, and the simplest way to avoid it is straightforward:
      don''t ask for anything clearly malicious or suspicious.'
  editorial: The guidance to match effort levels to task difficulty and avoid over-planning
    generalizes well beyond Fable 5 to any high-cost, high-capability model. What's
    most notable is the silent safety reroute to Opus -- a design where the model
    itself acts as both a guardrail and a cost-management mechanism, without requiring
    explicit user action. With the promotional window closing July 7, teams evaluating
    Fable 5 for production use should treat the cost structure, not just the capability
    jump, as a first-class part of the decision.
  headerImage: /images/vcU85OrwuV0/header.png
  heroImage: /images/vcU85OrwuV0/header.png
---

## ハイライト

- [00:00] Claude Fable 5は筆者がこれまで使った中で最も強力なモデルだと評価し、公式ベストプラクティス文書を読み込んで6つのコツに凝縮した。
- [00:25] 料金はOpusの2倍で、入力$10/百万トークン、出力$50/百万トークン。プロモーション期間は7月7日までと期限が短い。
- [00:48] プロモーション期間中はウィークリー上限の最大50%までは追加課金なしで使え、それ以降は使用量クレジットが必要になる。
- [04:43] 具体的な指示だけでなく、してほしくないことを伝える「ネガティブプロンプティング」も有効に働くケースが増えている。
- [05:05] 計画モードを常用するのではなく「十分な情報が集まったら行動せよ」という指示で過剰な計画立てを防ぐのが公式推奨の第一歩。
- [05:44] 低・中・高・エクストラハイという複数の思考努力(effort)レベルをタスクの難易度に応じて使い分けることが重要。
- [09:31] 危険性の高い依頼(ハッキングや危険な生物学など)を検知すると、Fable 5は静かにOpus 4.8へルーティングして安全確認を行う。

## セクション

### コストと利用条件を最初に押さえる

- 時刻: 00:25

Claude Fable 5はOpusの2倍という高価格帯のモデルで、入力トークン$10/百万、出力トークン$50/百万というコスト構造を持つ。Claudeプランに常時含まれるわけではなく、現時点は「プロモーション期間」という位置づけで提供されている。

この期間中はウィークリー上限の最大50%まで追加課金なしで利用できるが、それを超えると使用量クレジットへの切り替えが必要になる。プロモーション終了は7月7日と迫っており、無駄なトークン消費を避ける実践的な使い方の重要性が増している。

### 計画させすぎない・エフォートレベルを使い分ける

- 時刻: 05:05

公式ドキュメントが最初に挙げる推奨は「十分な情報を集めたら計画を練り続けずに行動へ移す」よう促すことだ。筆者自身も以前は「必ずPlanモードから始める」としていたが、現在はPlanモードを常用せず、独自のプロンプトで「行動できる状態になったら行動せよ」と指示する運用に切り替えている。

難しいタスクでは高いエフォートレベルで数分間にわたる処理が発生しうるため、低・中・高・エクストラハイの4段階を、タスクの複雑さや必要なコンテキスト収集量に応じて選び分けることが推奨されている。

### 危険な依頼は静かにOpusへルーティングされる

- 時刻: 09:31

Fable 5には安全性チェックの仕組みが組み込まれており、ハッキング支援や危険な生物学、モデル自身の内部推論の開示要求など特定のカテゴリに該当すると判断した場合、ユーザーに知らせないままOpus 4.8へリクエストを静かにルーティングする。

API経由であればレスポンスにOpusが処理したことが明示されるが、通常の利用では気づかないことが多い。幸いルーティング先はOpus 4.8のため、Fable 5ほどのコストは発生しない。明らかに悪意のある依頼を避けることが、この予期せぬルーティングを回避する最善の方法だ。

## 編集部の視点

エフォートレベルの使い分けや「計画させすぎない」という指針は、Fable 5に限らず高性能・高コストなモデル全般に応用できる汎用的な運用知見だ。特に注目すべきは、危険とみなされたリクエストが利用者に知らせずOpusへ自動ルーティングされる仕組みで、これはモデル自身がガードレールとコスト管理を兼ねる設計思想を示している。プロモーション期間という限定的な無料枠の存在は、企業がモデル選定の意思決定を急がされる状況を生みやすく、コスト試算を後回しにしないよう注意喚起する材料になる。
