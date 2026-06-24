---
videoId: t6Zmu-pBZlE
title: 【Claudeが自分で爆速開発→「Fable 5」誕生】アンソロピック幹部「寝て起きたらAIが仕事完了」新型モデル“月イチ発表”の裏側／ミュトス級は「ざっくり指示」で意図を理解【1on1
  Tech】
slug: catherine-woo-fable-5-development
articleTitle: Anthropicキャサリン・ウー氏が語るFable 5の進化と月1モデル開発の現場
seoTitle: キャサリン・ウー氏が語るFable 5進化と月1開発体制
summary: Anthropic 幹部キャサリン・ウー氏の発言をもとに、Fable 5 の進化と高速なモデル開発体制を整理した記事です。
channel: TBS CROSS DIG with Bloomberg
channelId: UCeCmAYh1ylwIsgGrmqaklzg
publishedAt: '2026-06-12T22:00:09Z'
fetchedAt: '2026-06-13T23:58:45.238371Z'
originalThumbnail: https://i.ytimg.com/vi/t6Zmu-pBZlE/maxresdefault.jpg
headerImage: /images/t6Zmu-pBZlE/header.ja.png
heroImage: /images/t6Zmu-pBZlE/header.ja.png
viewCount: 43483
durationSec: 2086
sourceLanguage: ja
matchedKeywords:
- Claude
- Anthropic
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- キャサリン・ウー
- Claude Code
- Cowork
- Auto Mode
- AIネイティブ
bulletPoints:
- time: 126
  text: Fable 5は過去最強のコーディングモデルで、長時間・複雑コードベースでの慎重な変更タスクで他を上回るとウー氏。
- time: 228
  text: 「Fable 5は本当に意図を汲んでくれる」 - 高レベルの方針相談でも答えを返すブレインストーミング相手として使える。
- time: 559
  text: 顧客サポートのトリアージを自動で根本原因特定 → 担当エンジニア特定 → PR作成までこなすワークフローが既に運用に。
- time: 729
  text: Anthropic社員はQuadで2021〜25年比で1人あたり8倍のコードを出荷、月1モデル投下を可能にしている。
- time: 908
  text: 安全性を全ての判断軸の頂点に置き、Auto Modeは社内検証・レッドチーム後にやっと外部公開された経緯がある。
- time: 1113
  text: トークン消費は可視化で対応 - 「人間にやらせたかったタスクかどうか」を基準にすべきとウー氏。
- time: 1717
  text: Claude Codeはエンジニア/PM/デザイナー、CoworkはマーケLeagal営業中心。法務チームが既にCoworkプラグインを内製。
sections:
- heading: Fable 5は「ざっくり指示で意図を汲む」設計パートナーへ
  time: 126
  body: 'Catherine Wu氏(Claude Code / Cowork プロダクト責任者)は、Fable 5を「これまでで最強のコーディングモデル」と位置付ける。前世代モデルが苦戦していた、長時間にわたるタスクや複雑なコードベース上での慎重な変更で、Fable
    5は最も適したモデルになっているという。


    従来は「この機能をこの通りに作って」と細かい指示を出していた領域で、Fable 5は「こういう問題があって、いくつか案もあるけどどうする?」というレベルの相談に応じられる。設計パートナーとしてブレストし、合意した方針を渡せばあとは本人に近い成功率で進める。Wu氏自身、複雑タスクに直面するとまずFable
    5とブレストする使い方に切り替えていると語る。'
- heading: 自走するエージェントと顧客サポートのトリアージ自動化
  time: 559
  body: '番組ではWu氏が、Claude Desktopで試している「self-doing to-do list」(各タスクごとにClaudeを起動する設計)、マーケティング/セールス資料の自動合成(複数の製品仕様書とローンチ素材を渡してプレゼン用デッキを作らせる)といった社内利用例を紹介した。


    とくに強調されたのが、顧客サポートのトリアージワークフローだ。「このチャネルを監視して、顧客から問題が来るたびに、根本原因を特定し、コードベースのその部分に最後に触れたエンジニアを特定してissueでタグ付けし、修正PRも合わせて作成する」というレベルの仕事をFable
    5級モデルで日常的に回している例が示された。Wu氏は「自分のチームは大きくなってもう一人一人が何をしているか把握しきれない。Fableがコードを読み、誰が直近触ったか、その変更の背景まで提示してくれるのが助かる」と話している。'
- heading: 月1モデル投下を支える「Quad駆動」の開発体制
  time: 729
  body: 'AnthropicはFable 5以前から、月に1つペースで新モデルを出荷してきた。背景にあるのはQuad(Claude Code / Cowork)による社内生産性の向上で、Wu氏は「2021〜2025年の通算と比べて、最新モデルの導入以降は1人あたり8倍のコードを出荷できている」と数字を挙げた。


    夜寝る前にエージェントへ最後のジョブを投げ、起きると完成しているという働き方も社内で広がっている。「自分は8時間しか働かないが、エージェントは24時間働ける」というメッセージで、自動化を増やして繰り返しタスクを置き換え、人は楽しい仕事に集中するよう促されている。ただしAnthropicは「最初の自動化は3割失敗する。誤りを見てプロンプトやハーネスを直し、100%安定するまで人間が監督する」プロセスを徹底するよう求めている。'
- heading: Auto Modeに見る安全性の徹底とトークンコストへの考え方
  time: 908
  body: '「安全はAnthropicの全ての意思決定を駆動する」とWu氏は繰り返した。具体例が今年公開された「Auto Mode」だ。多くのユーザーが許可プロンプトに対し97%もYesと押し、ミリ秒単位で判断していたという社内データを受けて、許可判定をClaude側に委譲する実装が検討された。


    Yesと言ったケース、Noと言ったケースのログを蓄積し、人間より良い判断ができる水準まで分類器を調整。さらに外部の赤チーム企業を雇って敵対的シナリオで攻撃させ、分類器を頑健化してから初めて外部公開した。当初アイデアは前年12月にあったが、安全な状態を確認するまで数か月待った経緯がある。


    トークンコストについては、ユーザー側に「自分のセッションがどれだけ消費したか」を可視化する方針。良いガイドラインは「もし人間にやらせたかったタスクならClaudeを使え」、一方で「10案でいいのに1000案出すのはやめよう」という個人の判断責任にも触れた。Fable
    5の価格をMythosプレビュー時点より下げたのも、日常タスクで使える水準を狙ったため。'
- heading: Claude CodeとCoworkの棲み分け - 法務チームまでプラグイン内製へ
  time: 1717
  body: '社内ではClaude Codeはエンジニア・一部のPM・デザイナー・データサイエンス担当が中心に使う。マーケティング、法務、セールスなど成果物がコードでない職種はCowork側を主に使うという棲み分けだ。


    ただしモデルが進化するにつれて、その境界は曖昧になっていく。番組では、法務チームのある弁護士が「製品に関する法律質問が来たら、Product Council
    Teamの誰が担当か答える」社内アプリをClaude Codeで自作している事例が紹介された。Wu氏は「Coworkの個別ロール向けUIをClaudeに作らせる時代がたぶん年内に来る」と予想する。最後にWu氏は「Claudeが詰まらないなら、まだ難しいタスクを投げ切れていない」とエンジニアに向けた言葉を残した。'
editorial: キャサリン・ウー氏のインタビューで最も重いのは、月1回のモデル投下を支える『1人あたり8倍のコード出荷』という社内変化だ。安全性を判断軸の頂点に置き、Auto
  Modeを社内検証とレッドチームの後にやっと外部公開する姿勢と、開発速度の両立がどう成立しているかが垣間見える。『トークン消費は人間にやらせたかったタスクかで測る』という基準は、コスト管理を費用ではなく価値の観点から捉え直す実務的な指針だ。
en:
  articleTitle: 'Inside Fable 5 at Anthropic: Catherine Wu on Faster Model Shipping
    and AI Workflows'
  seoTitle: 'Inside Fable 5 at Anthropic: Catherine Wu on Faster Model Shippi'
  summary: Wu says Fable 5 is Anthropic’s strongest coding model yet, outperforming
    earlier systems on long-running tasks and…
  keyPhrases:
  - Claude Fable 5
  - Catherine Wu
  - Claude Code
  - Cowork
  - Auto Mode
  - AI-native
  bulletPoints:
  - time: 126
    text: Wu says Fable 5 is Anthropic’s strongest coding model yet, outperforming
      earlier systems on long-running tasks and careful changes inside complex codebases.
  - time: 228
    text: '"Fable 5 really understands intent," she says, making it useful even as
      a brainstorming partner for high-level product and design direction.'
  - time: 559
    text: Anthropic is already running workflows where customer support triage goes
      from root-cause identification to owner lookup to pull request creation.
  - time: 729
    text: Wu says employees using Quad ship 8x more code per person than in 2021-2025,
      enabling Anthropic’s pace of one model release per month.
  - time: 908
    text: Safety sits at the top of every decision. Auto Mode was only released externally
      after internal validation and red-team testing.
  - time: 1113
    text: Wu argues token usage should be made visible, and that the right benchmark
      is whether the task was something you would otherwise want a human to do.
  - time: 1717
    text: Claude Code is used mainly by engineers, PMs, and designers, while Cowork
      is centered more on marketing, legal, and sales. Anthropic’s legal team has
      already built its own Cowork plugin.
  sections:
  - heading: Fable 5 as a Design Partner That Understands Intent
    time: 126
    body: 'Catherine Wu, who leads product for Claude Code and Cowork, describes Fable
      5 as "the strongest coding model we’ve ever had." She says it is especially
      well suited to the kinds of work earlier models struggled with: long-duration
      tasks and careful changes inside complex codebases.


      In areas where teams previously had to specify every detail, Fable 5 can now
      handle conversations at the level of "Here is the problem, we have a few options,
      what should we do?" It can brainstorm like a design partner, align on an approach,
      and then carry execution through with something close to human-level success
      rates. Wu says that when she faces a complex task, her first step now is to
      brainstorm with Fable 5.'
  - heading: Self-Running Agents and Automated Support Triage
    time: 559
    body: 'In the program, Wu highlights internal use cases such as a "self-doing
      to-do list" in Claude Desktop, where Claude is launched for each task, and automated
      assembly of marketing and sales materials by feeding in multiple product specs
      and launch assets to generate presentation decks.


      The most notable example is customer support triage. Anthropic is already running
      workflows at the level of: monitor this channel, and whenever a customer issue
      comes in, identify the root cause, find the engineer who last touched that part
      of the codebase, tag that person in an issue, and generate the fix PR as well.
      Wu says this kind of support is increasingly important because teams get too
      large for any one person to track what everyone has changed. Fable can read
      the code, identify who touched it most recently, and explain the context behind
      that change.'
  - heading: A Quad-Driven Development System Behind Monthly Model Releases
    time: 729
    body: 'Anthropic had already been shipping new models at roughly one per month
      before Fable 5. Wu attributes that pace in part to productivity gains from Quad,
      including Claude Code and Cowork. She cites an internal metric that, compared
      with the 2021-2025 baseline, employees ship eight times more code per person
      after adopting the latest models.


      The workflow of handing a final job to an agent before bed and waking up to
      completed work is also spreading inside the company. The message is simple:
      humans work eight hours, but agents can work 24. Anthropic encourages teams
      to increase automation, replace repetitive tasks, and reserve human time for
      the interesting work. At the same time, the company insists on close supervision,
      warning that the first pass at automation fails about 30% of the time. Humans
      are expected to inspect the errors, fix the prompts and harnesses, and keep
      supervising until stability reaches 100%.'
  - heading: How Anthropic Thinks About Auto Mode Safety and Token Costs
    time: 908
    body: 'Wu repeatedly says that safety drives every decision at Anthropic. Her
      example is Auto Mode, released earlier this year. Internal data showed that
      users hit "Yes" on permission prompts 97% of the time, often within milliseconds,
      which led the company to consider handing those permission decisions to Claude
      itself.


      Anthropic accumulated logs of both "Yes" and "No" decisions and tuned the classifier
      until it could make better judgments than a human. The company then hired external
      red-team firms to attack the system under adversarial scenarios and only released
      it publicly after hardening the classifier. Wu says the concept had existed
      since December of the previous year, but Anthropic waited months to confirm
      it was safe enough.


      On token costs, she says the product direction is to make each user’s consumption
      visible. Her rule of thumb is: if it is a task you would otherwise want a human
      to do, use Claude. At the same time, users should exercise judgment and avoid
      waste, such as asking for 1,000 options when 10 is enough. She also notes that
      Fable 5 was priced below the Mythos preview because Anthropic wanted it to be
      usable for everyday work.'
  - heading: Claude Code vs. Cowork, and the Blurring Line Between Them
    time: 1717
    body: 'Inside Anthropic, Claude Code is used primarily by engineers, some PMs,
      designers, and data science staff. Cowork is the main tool for teams whose deliverables
      are not code, including marketing, legal, and sales.


      But Wu expects that boundary to blur as the models improve. One example featured
      in the segment is a lawyer on the legal team who built an internal app with
      Claude Code that answers which member of the Product Counsel team should handle
      a product-related legal question. Wu predicts that within the year, teams will
      likely have Claude build role-specific Cowork interfaces for them. She closes
      with a challenge to engineers: if Claude is not getting stuck, you probably
      still are not giving it hard enough tasks.'
  editorial: 'The weightiest part of Catherine Wu''s interview is the internal change
    behind monthly model drops: ''8x more code shipped per person.'' It offers a glimpse
    of how development speed coexists with placing safety atop every decision axis
    and releasing Auto Mode externally only after internal validation and red-teaming.
    The yardstick — ''measure token spend by whether it was a task you wanted a human
    to do'' — is a practical reframing of cost management from expense to value.'
  headerImage: /images/t6Zmu-pBZlE/header.png
  heroImage: /images/t6Zmu-pBZlE/header.png
---

## ハイライト

- [02:06] Fable 5は過去最強のコーディングモデルで、長時間・複雑コードベースでの慎重な変更タスクで他を上回るとウー氏。
- [03:48] 「Fable 5は本当に意図を汲んでくれる」 - 高レベルの方針相談でも答えを返すブレインストーミング相手として使える。
- [09:19] 顧客サポートのトリアージを自動で根本原因特定 → 担当エンジニア特定 → PR作成までこなすワークフローが既に運用に。
- [12:09] Anthropic社員はQuadで2021〜25年比で1人あたり8倍のコードを出荷、月1モデル投下を可能にしている。
- [15:08] 安全性を全ての判断軸の頂点に置き、Auto Modeは社内検証・レッドチーム後にやっと外部公開された経緯がある。
- [18:33] トークン消費は可視化で対応 - 「人間にやらせたかったタスクかどうか」を基準にすべきとウー氏。
- [28:37] Claude Codeはエンジニア/PM/デザイナー、CoworkはマーケLeagal営業中心。法務チームが既にCoworkプラグインを内製。

## セクション

### Fable 5は「ざっくり指示で意図を汲む」設計パートナーへ

- 時刻: 02:06

Catherine Wu氏(Claude Code / Cowork プロダクト責任者)は、Fable 5を「これまでで最強のコーディングモデル」と位置付ける。前世代モデルが苦戦していた、長時間にわたるタスクや複雑なコードベース上での慎重な変更で、Fable 5は最も適したモデルになっているという。

従来は「この機能をこの通りに作って」と細かい指示を出していた領域で、Fable 5は「こういう問題があって、いくつか案もあるけどどうする?」というレベルの相談に応じられる。設計パートナーとしてブレストし、合意した方針を渡せばあとは本人に近い成功率で進める。Wu氏自身、複雑タスクに直面するとまずFable 5とブレストする使い方に切り替えていると語る。

### 自走するエージェントと顧客サポートのトリアージ自動化

- 時刻: 09:19

番組ではWu氏が、Claude Desktopで試している「self-doing to-do list」(各タスクごとにClaudeを起動する設計)、マーケティング/セールス資料の自動合成(複数の製品仕様書とローンチ素材を渡してプレゼン用デッキを作らせる)といった社内利用例を紹介した。

とくに強調されたのが、顧客サポートのトリアージワークフローだ。「このチャネルを監視して、顧客から問題が来るたびに、根本原因を特定し、コードベースのその部分に最後に触れたエンジニアを特定してissueでタグ付けし、修正PRも合わせて作成する」というレベルの仕事をFable 5級モデルで日常的に回している例が示された。Wu氏は「自分のチームは大きくなってもう一人一人が何をしているか把握しきれない。Fableがコードを読み、誰が直近触ったか、その変更の背景まで提示してくれるのが助かる」と話している。

### 月1モデル投下を支える「Quad駆動」の開発体制

- 時刻: 12:09

AnthropicはFable 5以前から、月に1つペースで新モデルを出荷してきた。背景にあるのはQuad(Claude Code / Cowork)による社内生産性の向上で、Wu氏は「2021〜2025年の通算と比べて、最新モデルの導入以降は1人あたり8倍のコードを出荷できている」と数字を挙げた。

夜寝る前にエージェントへ最後のジョブを投げ、起きると完成しているという働き方も社内で広がっている。「自分は8時間しか働かないが、エージェントは24時間働ける」というメッセージで、自動化を増やして繰り返しタスクを置き換え、人は楽しい仕事に集中するよう促されている。ただしAnthropicは「最初の自動化は3割失敗する。誤りを見てプロンプトやハーネスを直し、100%安定するまで人間が監督する」プロセスを徹底するよう求めている。

### Auto Modeに見る安全性の徹底とトークンコストへの考え方

- 時刻: 15:08

「安全はAnthropicの全ての意思決定を駆動する」とWu氏は繰り返した。具体例が今年公開された「Auto Mode」だ。多くのユーザーが許可プロンプトに対し97%もYesと押し、ミリ秒単位で判断していたという社内データを受けて、許可判定をClaude側に委譲する実装が検討された。

Yesと言ったケース、Noと言ったケースのログを蓄積し、人間より良い判断ができる水準まで分類器を調整。さらに外部の赤チーム企業を雇って敵対的シナリオで攻撃させ、分類器を頑健化してから初めて外部公開した。当初アイデアは前年12月にあったが、安全な状態を確認するまで数か月待った経緯がある。

トークンコストについては、ユーザー側に「自分のセッションがどれだけ消費したか」を可視化する方針。良いガイドラインは「もし人間にやらせたかったタスクならClaudeを使え」、一方で「10案でいいのに1000案出すのはやめよう」という個人の判断責任にも触れた。Fable 5の価格をMythosプレビュー時点より下げたのも、日常タスクで使える水準を狙ったため。

### Claude CodeとCoworkの棲み分け - 法務チームまでプラグイン内製へ

- 時刻: 28:37

社内ではClaude Codeはエンジニア・一部のPM・デザイナー・データサイエンス担当が中心に使う。マーケティング、法務、セールスなど成果物がコードでない職種はCowork側を主に使うという棲み分けだ。

ただしモデルが進化するにつれて、その境界は曖昧になっていく。番組では、法務チームのある弁護士が「製品に関する法律質問が来たら、Product Council Teamの誰が担当か答える」社内アプリをClaude Codeで自作している事例が紹介された。Wu氏は「Coworkの個別ロール向けUIをClaudeに作らせる時代がたぶん年内に来る」と予想する。最後にWu氏は「Claudeが詰まらないなら、まだ難しいタスクを投げ切れていない」とエンジニアに向けた言葉を残した。

## 編集部の視点

キャサリン・ウー氏のインタビューで最も重いのは、月1回のモデル投下を支える『1人あたり8倍のコード出荷』という社内変化だ。安全性を判断軸の頂点に置き、Auto Modeを社内検証とレッドチームの後にやっと外部公開する姿勢と、開発速度の両立がどう成立しているかが垣間見える。『トークン消費は人間にやらせたかったタスクかで測る』という基準は、コスト管理を費用ではなく価値の観点から捉え直す実務的な指針だ。
