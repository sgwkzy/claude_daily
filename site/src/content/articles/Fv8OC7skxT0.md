---
videoId: Fv8OC7skxT0
title: 【新型Claude「Fable 5」はポケモン攻略】「Googleの聖域が危ない」今井翔太／ミュトスの能力を過剰制限“融通が利かない”／アンソロピックが計算資源不足→「課金地獄」に【AI
  QUEST】
slug: claude-fable-5-bloomberg-tbs-analysis
seoTitle: Claude Fable 5をTBS×Bloombergが分析 能力と制約の論点整理
summary: Claude Fable 5 をめぐる性能評価、制約、計算資源の問題までを、TBS CROSS DIG with Bloomberg の議論から整理した記事です。
channel: TBS CROSS DIG with Bloomberg
channelId: UCeCmAYh1ylwIsgGrmqaklzg
publishedAt: '2026-06-12T09:30:09Z'
fetchedAt: '2026-06-12T10:25:38.931514Z'
originalThumbnail: https://i.ytimg.com/vi/Fv8OC7skxT0/maxresdefault.jpg
headerImage: /images/Fv8OC7skxT0/header.ja.png
heroImage: /images/Fv8OC7skxT0/header.ja.png
viewCount: 223807
durationSec: 2041
sourceLanguage: ja
matchedKeywords:
- Claude
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- ミュトス5
- 外部AIフィルター
- ジェイルブレイク
- データセンター建設ボトルネック
- 課金地獄
bulletPoints:
- time: 15
  text: 2026年6月10日（水）、Anthropicが新モデル「Claude Fable 5」と「ミュトス5」を突然リリース。前週の収録直後という超緊急事態を受け、今井翔太氏が急遽出演して解説することになった。
- time: 70
  text: 同日、日本でAnthropicの「Code with Claude」イベントが開催され、Claude CodeやFable 5の開発担当者へのインタビューも実施。AIを社内の中心に据えることで開発サイクルが大幅に加速している実態が明かされた。
- time: 885
  text: Fable 5のサイバー攻撃能力評価はあえて「0」に抑えられており、これはモデル本体をガチガチにアラインメントしたためではなく、別途構築した外部AIフィルターによって危険コンテンツを遮断する設計によるものだと説明された。
- time: 949
  text: 外部フィルター方式にはジェイルブレイクやプロンプトインジェクションでフィルターを突破された場合にモデル本体が無制限に危険な出力を行うリスクがあり、一方でフィルターを厳しくしすぎると役員向けプレゼン作成まで拒否されるという過剰制限の問題も顕在化している。
- time: 1901
  text: データセンター建設が物理的に追いつかず各地で工事が進行中。計算資源の供給不足がAnthropicの「課金地獄」とも揶揄されるコスト高騰につながっており、AIの進化がインフラ整備のボトルネックを次々と生み出している構図が明らかになった。
- time: 1986
  text: スケーリング則によってAGIへの道が想定より早く拓けると期待されていたが、実際にはアムダールの法則のごとく一部が進化すると別の部分がボトルネックとなる連鎖が続き、「思ったより先は遠い」という現実認識に変わりつつある。
sections:
- heading: 緊急収録の背景と概要
  time: 2
  body: '2026年6月10日（水）、Anthropicが新型AIモデル「Claude Fable 5」および「ミュトス5」を突然公開した。前週の金曜日にちょうどClaudeに関する収録を終えたばかりのタイミングであり、出演予定だった学会（高崎）を急遽キャンセルして今井翔太氏が緊急参加することになった経緯が冒頭で語られた。


    同日には日本国内でAnthropicが「Code with Claude」イベントを開催しており、Claude CodeやFable 5担当者へのインタビューも行われた。Claude
    Codeを全社的に活用することで開発速度が飛躍的に向上しているという証言が得られており、その詳細は後日改めて報告される予定とのこと。'
  image: null
- heading: 安全設計と能力評価
  time: 885
  body: 'Fable 5のサイバー攻撃能力はシステムカード上「0」と評価されている。これはモデル本体に対してサイバーセキュリティ関連の能力を一切拒否するアラインメントを施したためではなく、Fable本体とは別に構築された外部判定AIがリクエストの危険度を評価してフィルタリングする方式を採用したことによるものだ。


    このアプローチはAnthropicやOpenAIが以前から用いてきた手法であるが、根本的な問題も内包している。プロンプトインジェクションやジェイルブレイクによってフィルターを突破された場合、アラインメントを施していないモデル本体が危険な出力を無制限に行うリスクがある。一方で安全を優先してフィルターを過剰に厳しく設定すると、役員向けプレゼン作成やAIとの人格形成テストといった無害な用途まで拒否されるという過剰制限の問題がSNS上で多数報告されており、バランスの取り方が大きな課題として浮上している。'
  image: null
- heading: インフラ不足と課金高騰
  time: 1901
  body: 'AI性能の急速な向上に対し、それを支えるデータセンターの物理的な建設が追いついていない状況が深刻化している。各地で工事が進行しているものの、資材・人員・電力設備の調達には相当な時間がかかり、「人間にとって最も分かりやすいボトルネック」と表現された。


    この計算資源の慢性的な不足が、Anthropicのサービス料金高騰（俗に「課金地獄」）に直結している。Fable 5・ミュトス5の価格設定を見ると、「思っていたより先は遠い、こんなにお金が必要だったのか」という現実認識を改めて突きつけられる形となっている。スケーリング則への期待が高まってAGIへの道が近いと感じられた時期とは様相が変わり、アムダールの法則的な連鎖ボトルネックが各所で顕在化しているとまとめられた。'
  image: null
en:
  articleTitle: Claude Fable 5, External Filters, and Why AI Infrastructure Is Now
    the Bottleneck
  seoTitle: Claude Fable 5, External Filters, and Why AI Infrastructure Is N
  summary: On Wednesday, June 10, 2026, Anthropic suddenly released the new models
    "Claude Fable 5" and "Mythos 5," prompting…
  keyPhrases:
  - Claude Fable 5
  - Mythos 5
  - external AI filter
  - jailbreak
  - data center construction bottleneck
  - billing hell
  bulletPoints:
  - time: 15
    text: On Wednesday, June 10, 2026, Anthropic suddenly released the new models
      "Claude Fable 5" and "Mythos 5," prompting Shota Imai to join on short notice
      for an emergency breakdown.
  - time: 70
    text: Anthropic also held its "Code with Claude" event in Japan that same day,
      where interviews with the Claude Code and Fable 5 teams highlighted how putting
      AI at the center of internal work has dramatically sped up development cycles.
  - time: 885
    text: The video's explanation for Fable 5's deliberately "0" cyberattack rating
      is that the model itself was not heavily aligned for refusal, but rather wrapped
      in a separate external AI filter that blocks dangerous content.
  - time: 949
    text: 'That external-filter design carries a dual risk: if jailbreaks or prompt
      injection bypass the filter, the core model can produce dangerous outputs freely,
      but if the filter is too strict it can end up refusing even harmless executive
      presentation work.'
  - time: 1901
    text: Data center construction is not keeping pace physically, with projects underway
      in many places. The shortage of compute supply is pushing up costs and feeding
      what the video calls Anthropic's "billing hell."
  - time: 1986
    text: The speaker says scaling-law optimism once suggested a faster path to AGI,
      but in reality one solved bottleneck keeps exposing another, more in line with
      Amdahl's law than with a smooth acceleration curve.
  sections:
  - heading: Why the Episode Was Recorded as an Emergency Update
    time: 2
    body: 'On Wednesday, June 10, 2026, Anthropic suddenly unveiled two new AI models,
      "Claude Fable 5" and "Mythos 5." The timing came immediately after the show''s
      previous Claude recording on the prior Friday, and the opening explains that
      Shota Imai canceled a planned academic event in Takasaki in order to join this
      emergency follow-up.


      Anthropic also held its "Code with Claude" event in Japan that same day, where
      interviews were conducted with people working on Claude Code and Fable 5. According
      to the segment, those conversations pointed to sharply faster development inside
      Anthropic by placing Claude Code at the center of company workflows, with a
      fuller report promised later.'
    image: null
  - heading: How the Safety Design Shapes the Capability Rating
    time: 885
    body: 'Fable 5''s cyberattack capability is rated "0" in the system card. The
      explanation given is not that the core model itself was aligned to categorically
      refuse all cybersecurity-related work, but that a separate external judgment
      model evaluates request risk and filters outputs before they are returned.


      The hosts note that this approach has been used before by both Anthropic and
      OpenAI, but argue that it carries a fundamental weakness. If prompt injection
      or jailbreak techniques break through the filter, the underlying model, which
      has not been directly aligned for refusal, may generate dangerous outputs without
      limit. At the same time, if the filter is tuned too aggressively for safety,
      it starts refusing benign tasks such as preparing an executive presentation
      or running personality-formation tests with AI. The segment says many such overblocking
      examples have already surfaced on social media, making the calibration problem
      a central issue.'
    image: null
  - heading: Compute Shortages, Higher Prices, and the Real Bottleneck
    time: 1901
    body: 'The video argues that physical data center construction is no longer keeping
      up with how quickly AI capability is advancing. Projects are underway in many
      regions, but securing materials, labor, and power infrastructure takes time,
      making this what the speaker calls the most obvious bottleneck from a human
      point of view.


      That chronic shortage of compute resources is directly tied, in the video''s
      telling, to Anthropic''s rising service costs, sarcastically described as "billing
      hell." Looking at the pricing for Fable 5 and Mythos 5, the hosts say the market
      is being forced to confront a harder truth: the road ahead is farther away and
      more expensive than many expected. The mood has shifted from scaling-law optimism
      toward a more Amdahl''s-law view, where solving one bottleneck simply reveals
      the next.'
    image: null
  headerImage: /images/Fv8OC7skxT0/header.png
  heroImage: /images/Fv8OC7skxT0/header.png
---

## ハイライト

- [00:15] 2026年6月10日（水）、Anthropicが新モデル「Claude Fable 5」と「ミュトス5」を突然リリース。前週の収録直後という超緊急事態を受け、今井翔太氏が急遽出演して解説することになった。
- [01:10] 同日、日本でAnthropicの「Code with Claude」イベントが開催され、Claude CodeやFable 5の開発担当者へのインタビューも実施。AIを社内の中心に据えることで開発サイクルが大幅に加速している実態が明かされた。
- [14:45] Fable 5のサイバー攻撃能力評価はあえて「0」に抑えられており、これはモデル本体をガチガチにアラインメントしたためではなく、別途構築した外部AIフィルターによって危険コンテンツを遮断する設計によるものだと説明された。
- [15:49] 外部フィルター方式にはジェイルブレイクやプロンプトインジェクションでフィルターを突破された場合にモデル本体が無制限に危険な出力を行うリスクがあり、一方でフィルターを厳しくしすぎると役員向けプレゼン作成まで拒否されるという過剰制限の問題も顕在化している。
- [31:41] データセンター建設が物理的に追いつかず各地で工事が進行中。計算資源の供給不足がAnthropicの「課金地獄」とも揶揄されるコスト高騰につながっており、AIの進化がインフラ整備のボトルネックを次々と生み出している構図が明らかになった。
- [33:06] スケーリング則によってAGIへの道が想定より早く拓けると期待されていたが、実際にはアムダールの法則のごとく一部が進化すると別の部分がボトルネックとなる連鎖が続き、「思ったより先は遠い」という現実認識に変わりつつある。

## セクション

### 緊急収録の背景と概要

- 時刻: 00:02

2026年6月10日（水）、Anthropicが新型AIモデル「Claude Fable 5」および「ミュトス5」を突然公開した。前週の金曜日にちょうどClaudeに関する収録を終えたばかりのタイミングであり、出演予定だった学会（高崎）を急遽キャンセルして今井翔太氏が緊急参加することになった経緯が冒頭で語られた。

同日には日本国内でAnthropicが「Code with Claude」イベントを開催しており、Claude CodeやFable 5担当者へのインタビューも行われた。Claude Codeを全社的に活用することで開発速度が飛躍的に向上しているという証言が得られており、その詳細は後日改めて報告される予定とのこと。

### 安全設計と能力評価

- 時刻: 14:45

Fable 5のサイバー攻撃能力はシステムカード上「0」と評価されている。これはモデル本体に対してサイバーセキュリティ関連の能力を一切拒否するアラインメントを施したためではなく、Fable本体とは別に構築された外部判定AIがリクエストの危険度を評価してフィルタリングする方式を採用したことによるものだ。

このアプローチはAnthropicやOpenAIが以前から用いてきた手法であるが、根本的な問題も内包している。プロンプトインジェクションやジェイルブレイクによってフィルターを突破された場合、アラインメントを施していないモデル本体が危険な出力を無制限に行うリスクがある。一方で安全を優先してフィルターを過剰に厳しく設定すると、役員向けプレゼン作成やAIとの人格形成テストといった無害な用途まで拒否されるという過剰制限の問題がSNS上で多数報告されており、バランスの取り方が大きな課題として浮上している。

### インフラ不足と課金高騰

- 時刻: 31:41

AI性能の急速な向上に対し、それを支えるデータセンターの物理的な建設が追いついていない状況が深刻化している。各地で工事が進行しているものの、資材・人員・電力設備の調達には相当な時間がかかり、「人間にとって最も分かりやすいボトルネック」と表現された。

この計算資源の慢性的な不足が、Anthropicのサービス料金高騰（俗に「課金地獄」）に直結している。Fable 5・ミュトス5の価格設定を見ると、「思っていたより先は遠い、こんなにお金が必要だったのか」という現実認識を改めて突きつけられる形となっている。スケーリング則への期待が高まってAGIへの道が近いと感じられた時期とは様相が変わり、アムダールの法則的な連鎖ボトルネックが各所で顕在化しているとまとめられた。
