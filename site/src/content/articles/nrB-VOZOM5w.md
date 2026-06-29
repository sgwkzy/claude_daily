---
videoId: nrB-VOZOM5w
title: How to Build AI Employees That Work On a Schedule | Twin
slug: スケジュール駆動の-ai-従業員-twin-プラットフォームで-no-code-に-sdr-を運用する-nrb-vozom5w
articleTitle: スケジュール駆動の AI 従業員 — Twin プラットフォームで no-code に SDR を運用する
seoTitle: スケジュール駆動の AI 従業員 — Twin プラットフォームで no-code に SDR を運用する
summary: Jon Law は朝8時に AI エージェントが寝ている間にこなした作業を見せる。EC 企業20社の発見、創業者連絡先の抽出、パーソナライズメール作成、送信、CRM
  記録、Slack へのサマリ送信までを完全自動で完了した。
channel: 'Jon Law '
channelId: UCQM_HxoKmza1simMUchYfVA
publishedAt: '2026-06-27T19:33:09Z'
fetchedAt: '2026-06-29T11:18:54.774165Z'
originalThumbnail: https://i.ytimg.com/vi/nrB-VOZOM5w/maxresdefault.jpg
headerImage: /images/nrB-VOZOM5w/header.ja.png
heroImage: /images/nrB-VOZOM5w/header.ja.png
viewCount: 93333
durationSec: 739
sourceLanguage: en
matchedKeywords:
- AIエージェント
proposedByLLM: false
keyPhrases:
- Twin AI 従業員プラットフォーム
- SDR エージェント自動化
- 時刻トリガー実行
- クラウド常駐稼働
- クレジット課金制
- 単純頻発タスク最適化
bulletPoints:
- time: 0
  text: Jon Law は朝8時に AI エージェントが寝ている間にこなした作業を見せる。EC 企業20社の発見、創業者連絡先の抽出、パーソナライズメール作成、送信、CRM
    記録、Slack へのサマリ送信までを完全自動で完了した。
- time: 28
  text: AI チャットボットとワークフロービルダーの二項対立の議論は論点を外している、と Jon は指摘する。チャットボットはコンテキストとメモリが弱い、ワークフローツールは自分がエンジニア役になる必要がある。
- time: 64
  text: 自動化ツール(N8N/Zapier/make.com)は強力だが硬直しており、自分で組み立てる必要がある。一方で常時稼働の信頼性は強み。チャットボット型エージェントとの中間が求められている。
- time: 315
  text: 実機デモでは SDR エージェントが Google Sheets に20社の調査結果を出力し、その流れでパーソナライズされた20通のメールを送信。1通ずつ正しいフルセットのコールドメール構成になっている。
- time: 385
  text: 次の手順は時刻トリガーの設定だ。『毎日午前9時に1回繰り返す』と指示するだけで完全自動化フローに切り替わり、サブスクリプションではなくクレジット課金のみで稼働する。
- time: 657
  text: ノート PC を閉じてもクラウド上でエージェントが稼働し続け、設定スケジュールに従って実行を続ける。常時稼働の AI 従業員という体験が、技術的セットアップ抜きで成立している。
- time: 679
  text: Jon が挙げる弱点はクレジット課金制という点だ。複雑で野心的なタスクほど価値が大きい一方で、トークンとコンピュートの制約が直接コストとして跳ね返るため、上限まで使い切る運用には注意が必要。
- time: 716
  text: 最も投資対効果が高いのは『単純で頻発するタスクの自動化』だと Jon は強調する。月30ドル程度のトークン費用で10時間の人手作業を肩代わりさせる、というのが推奨される最初の一歩。
sections:
- heading: AI 従業員の現在地 — Twin プラットフォームの SDR 実行デモ
  time: 0
  body: 'Jon Law は冒頭で、朝8時に寝ている間に AI エージェントが完了させた作業を提示する。EC 企業20社の発見、創業者の連絡先抽出、パーソナライズされたメール作成、送信、CRM
    への記録、Slack へのサマリまでを Jon が一切触れずに完了している。プラットフォーム名は『The Twin』だ。


    ここで Jon は問題設定を整理する。AI チャットボット対ワークフロービルダーの二項対立は論点を外している。チャットボットはコンテキストとメモリが弱く、N8N
    や Zapier のようなワークフローツールは結局自分がエンジニア役になる必要がある。求められているのはその中間で、エージェント自身が手順を組み立て、スケジュールに従って自走し、ログオフ中も動き続ける存在だ。動画はその実装手順を具体的に示す構成になっている。'
- heading: スケジュール駆動 — 時刻トリガーとクラウド常駐運用
  time: 379
  body: '実機部分では SDR エージェントが Google Sheets に20社の調査結果を出力し、その後20通のパーソナライズメールを送信する。1通ずつ確認すると本物のコールドメール構造になっていて、AI
    SDR がフルタイムで稼働するイメージが具体的に描ける。


    次の手順は時刻トリガーの設定だ。『毎日午前9時に1回繰り返す』と指示するだけで完全自動化フローに切り替わり、ノート PC を閉じてもクラウド上で稼働を続ける。サブスクリプション課金ではなくクレジット課金のため、走らなければ請求は発生しない。Anthropic
    の Claude Tag が組織全体に常駐するハーネスを目指すのと別系統で、業務単位ごとに切り出した小さな AI 従業員を no-code で立ち上げる方向の到達点を示している。'
- heading: クレジット課金の制約と最も投資すべきタスク選定
  time: 657
  body: 'Jon は強みと弱みを整理する。強みはスケジュール駆動による信頼性と、open-class エージェントに比べて技術的セットアップが軽い点だ。一方で弱みはクレジット課金制で、複雑で野心的なタスクほど価値が出る半面、トークンとコンピュートの制約が直接コストへ跳ね返る。


    結論として Jon が最も推奨するのは『単純で頻発するタスクの自動化』だ。月30ドル程度のトークン費用で人手作業10時間を肩代わりさせるユースケースが、最初に投資すべき領域として最も投資対効果が高い。価格プランは無料スタータークレジット、Pro
    プランは月20ドル分のクレジット付与で、エージェントが実際にクレジットを消費したときだけ目減りする。AI 従業員を『安く・狭く・常時稼働』で始めて、効果を見ながら範囲を広げる進め方が現実的な勝ち筋として提示される。'
editorial: Twin のようなプラットフォームは Claude Tag や Notion 常駐エージェントとは別系統の解として読むのが正しい。前者は組織全体のハーネスを目指すのに対し、Twin
  は SDR・カスタマーサポートなど明確な業務単位を no-code で立ち上げ、時刻スケジュールで走らせる方向に振っている。読者にとっての含意は二つある。第一に、AI
  エージェント導入の初手として組織全体の設計から入る必要はなく、頻発する単純業務一つを月30ドル程度から自動化し、効果検証してから範囲を広げる進め方が合理的だ。第二に、クレジット課金制は『使えば使うほど高くなる』ため、最終的に価値が出るのは『この業務は本当に頻度が高いか』のタスク選定であり、エージェント技術よりも業務棚卸しの精度が成果を左右する。
en:
  articleTitle: Schedule-Driven AI Employees — Running No-Code SDRs on the Twin Platform
  seoTitle: Schedule-Driven AI Employees — Running No-Code SDRs on the Twin
  summary: Jon Law opens with what an AI agent finished at 8 a.m. while he was asleep.
    It found 20 brand-new e-commerce…
  keyPhrases:
  - Twin AI-employee platform
  - SDR agent automation
  - Time-trigger execution
  - Cloud-resident operation
  - Credit-based pricing
  - Optimize for simple, frequent tasks
  bulletPoints:
  - time: 0
    text: Jon Law opens with what an AI agent finished at 8 a.m. while he was asleep.
      It found 20 brand-new e-commerce companies, dug up founder contact info, wrote
      personalized cold emails, sent them, logged everything in a CRM, and sent him
      a Slack summary. He didn't touch any of it.
  - time: 28
    text: The 'AI chatbots vs workflow builders' debate misses the point, Jon argues.
      Chatbots are weak on context and memory; workflow builders force you to be the
      engineer. The middle is what's needed.
  - time: 64
    text: Automation tools like N8N, Zapier and make.com are powerful but rigid —
      you have to assemble them yourself. Their strength is consistent always-on execution.
      The combination with chatbot-style agents is the open space.
  - time: 315
    text: In the hands-on, an SDR agent outputs research on 20 companies into Google
      Sheets and sends 20 personalized cold emails as part of the same flow. Each
      email is a properly structured full cold-email setup.
  - time: 385
    text: Next is the time trigger. Set 'repeat once daily at 9 a.m.' and the whole
      thing flips to a fully automated flow — credit-based pricing, no subscription,
      only charges when the agent actually runs.
  - time: 657
    text: Even when you close the laptop, the agent continues to run on the cloud
      on the schedule you set. The always-on AI employee experience comes together
      without any of the technical setup.
  - time: 679
    text: Jon's named weakness is the credit pricing. Complex, ambitious tasks generate
      the most value, but token and compute costs hit the bill directly — running
      to the credit ceiling needs attention.
  - time: 716
    text: The highest ROI is automating 'simple tasks you do a lot,' Jon emphasizes.
      A roughly $30/month token spend that absorbs 10 hours of manual work is the
      recommended starting point.
  sections:
  - heading: Where AI Employees Stand Now — The Twin Platform's SDR Demo
    time: 0
    body: 'Jon Law opens by showing what an AI agent finished while he was asleep
      at 8 a.m. — 20 e-commerce companies discovered, founder contact info collected,
      personalized cold emails written and sent, the whole batch logged in a CRM,
      and a Slack summary delivered to him. He didn''t touch any of it. The platform
      is called The Twin.


      From there Jon sets up the problem. The ''AI chatbot vs workflow builder'' debate
      misses the point. Chatbots are weak on context and memory; tools like N8N or
      Zapier eventually force you to be the engineer. What''s needed is the middle
      — an agent that assembles steps itself, runs on a schedule, and keeps running
      while you''re logged off. The video walks through what that implementation looks
      like in practice.'
  - heading: Schedule-Driven — Time Triggers and Cloud-Resident Execution
    time: 379
    body: 'In the hands-on segment, the SDR agent outputs research on 20 companies
      into Google Sheets and then sends 20 personalized cold emails as part of the
      same flow. Each email is a properly structured full cold-email setup, and the
      picture of an AI SDR running full-time becomes concrete.


      The next step is the time trigger. Set ''repeat once daily at 9 a.m.'' and the
      whole thing flips to a fully automated flow. Even when the laptop closes, the
      agent keeps running in the cloud. Pricing is credit-based, not subscription-based,
      so nothing runs means nothing bills. Separate from Claude Tag''s bid to be the
      organization-wide harness, this is the endpoint of a different track — small
      AI employees carved out at the level of a single business unit, stood up no-code.'
  - heading: The Credit-Pricing Constraint and the Tasks Worth Investing In
    time: 657
    body: 'Jon lays out the strengths and weaknesses. The strengths: schedule-driven
      reliability, and a much lighter technical-setup load compared to open-class
      agents. The weakness is credit pricing — the most valuable tasks tend to be
      complex and ambitious, but token and compute costs hit the bill directly.


      His recommended starting point is ''automating simple tasks you do a lot.''
      A use case that absorbs 10 hours of manual work for roughly $30/month in tokens
      is the highest-ROI place to begin. Pricing-wise, free starter credits get you
      in, and the Pro plan adds $20/month of credits that only burn when the agent
      actually runs. The realistic path is to start AI employees ''cheap, narrow,
      and always-on,'' measure value, and expand from there.'
  editorial: Platforms like Twin are best read as a separate solution track from Claude
    Tag and Notion-resident agents. The latter aims to be an organization-wide harness;
    Twin leans into carving out clear business units like SDR or customer support,
    standing them up no-code, and running them on a time schedule. Two implications
    for readers. The first move into agents doesn't have to start with a full organizational
    design — automating one frequent simple task for around $30/month and only then
    expanding scope is the rational path. The second implication is that credit-based
    pricing penalizes overuse, so what really decides outcomes is task selection —
    'is this task actually high-frequency enough.' The accuracy of your inventory-of-work
    matters more than the sophistication of the agent technology.
  headerImage: /images/nrB-VOZOM5w/header.png
  heroImage: /images/nrB-VOZOM5w/header.png
---

## ハイライト

- [00:00] Jon Law は朝8時に AI エージェントが寝ている間にこなした作業を見せる。EC 企業20社の発見、創業者連絡先の抽出、パーソナライズメール作成、送信、CRM 記録、Slack へのサマリ送信までを完全自動で完了した。
- [00:28] AI チャットボットとワークフロービルダーの二項対立の議論は論点を外している、と Jon は指摘する。チャットボットはコンテキストとメモリが弱い、ワークフローツールは自分がエンジニア役になる必要がある。
- [01:04] 自動化ツール(N8N/Zapier/make.com)は強力だが硬直しており、自分で組み立てる必要がある。一方で常時稼働の信頼性は強み。チャットボット型エージェントとの中間が求められている。
- [05:15] 実機デモでは SDR エージェントが Google Sheets に20社の調査結果を出力し、その流れでパーソナライズされた20通のメールを送信。1通ずつ正しいフルセットのコールドメール構成になっている。
- [06:25] 次の手順は時刻トリガーの設定だ。『毎日午前9時に1回繰り返す』と指示するだけで完全自動化フローに切り替わり、サブスクリプションではなくクレジット課金のみで稼働する。
- [10:57] ノート PC を閉じてもクラウド上でエージェントが稼働し続け、設定スケジュールに従って実行を続ける。常時稼働の AI 従業員という体験が、技術的セットアップ抜きで成立している。
- [11:19] Jon が挙げる弱点はクレジット課金制という点だ。複雑で野心的なタスクほど価値が大きい一方で、トークンとコンピュートの制約が直接コストとして跳ね返るため、上限まで使い切る運用には注意が必要。
- [11:56] 最も投資対効果が高いのは『単純で頻発するタスクの自動化』だと Jon は強調する。月30ドル程度のトークン費用で10時間の人手作業を肩代わりさせる、というのが推奨される最初の一歩。

## セクション

### AI 従業員の現在地 — Twin プラットフォームの SDR 実行デモ

- 時刻: 00:00

Jon Law は冒頭で、朝8時に寝ている間に AI エージェントが完了させた作業を提示する。EC 企業20社の発見、創業者の連絡先抽出、パーソナライズされたメール作成、送信、CRM への記録、Slack へのサマリまでを Jon が一切触れずに完了している。プラットフォーム名は『The Twin』だ。

ここで Jon は問題設定を整理する。AI チャットボット対ワークフロービルダーの二項対立は論点を外している。チャットボットはコンテキストとメモリが弱く、N8N や Zapier のようなワークフローツールは結局自分がエンジニア役になる必要がある。求められているのはその中間で、エージェント自身が手順を組み立て、スケジュールに従って自走し、ログオフ中も動き続ける存在だ。動画はその実装手順を具体的に示す構成になっている。

### スケジュール駆動 — 時刻トリガーとクラウド常駐運用

- 時刻: 06:19

実機部分では SDR エージェントが Google Sheets に20社の調査結果を出力し、その後20通のパーソナライズメールを送信する。1通ずつ確認すると本物のコールドメール構造になっていて、AI SDR がフルタイムで稼働するイメージが具体的に描ける。

次の手順は時刻トリガーの設定だ。『毎日午前9時に1回繰り返す』と指示するだけで完全自動化フローに切り替わり、ノート PC を閉じてもクラウド上で稼働を続ける。サブスクリプション課金ではなくクレジット課金のため、走らなければ請求は発生しない。Anthropic の Claude Tag が組織全体に常駐するハーネスを目指すのと別系統で、業務単位ごとに切り出した小さな AI 従業員を no-code で立ち上げる方向の到達点を示している。

### クレジット課金の制約と最も投資すべきタスク選定

- 時刻: 10:57

Jon は強みと弱みを整理する。強みはスケジュール駆動による信頼性と、open-class エージェントに比べて技術的セットアップが軽い点だ。一方で弱みはクレジット課金制で、複雑で野心的なタスクほど価値が出る半面、トークンとコンピュートの制約が直接コストへ跳ね返る。

結論として Jon が最も推奨するのは『単純で頻発するタスクの自動化』だ。月30ドル程度のトークン費用で人手作業10時間を肩代わりさせるユースケースが、最初に投資すべき領域として最も投資対効果が高い。価格プランは無料スタータークレジット、Pro プランは月20ドル分のクレジット付与で、エージェントが実際にクレジットを消費したときだけ目減りする。AI 従業員を『安く・狭く・常時稼働』で始めて、効果を見ながら範囲を広げる進め方が現実的な勝ち筋として提示される。

## 編集部の視点

Twin のようなプラットフォームは Claude Tag や Notion 常駐エージェントとは別系統の解として読むのが正しい。前者は組織全体のハーネスを目指すのに対し、Twin は SDR・カスタマーサポートなど明確な業務単位を no-code で立ち上げ、時刻スケジュールで走らせる方向に振っている。読者にとっての含意は二つある。第一に、AI エージェント導入の初手として組織全体の設計から入る必要はなく、頻発する単純業務一つを月30ドル程度から自動化し、効果検証してから範囲を広げる進め方が合理的だ。第二に、クレジット課金制は『使えば使うほど高くなる』ため、最終的に価値が出るのは『この業務は本当に頻度が高いか』のタスク選定であり、エージェント技術よりも業務棚卸しの精度が成果を左右する。
