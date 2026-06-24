---
videoId: fkCznXZiwwk
title: 【Claude】公開後いきなり炎上して謝罪へ。Claude新モデルFableで何が起こったのか。
slug: claude-fable-5-hidden-quality-drop
articleTitle: Claude Fable 5の隠れた品質低下が3日で謝罪へ至った炎上の構造
seoTitle: Claude Fable 5の隠れた品質低下 謝罪に至る炎上構造を整理
summary: Claude Fable 5 の公開直後に起きた品質低下と炎上の流れを、論点ごとに把握しやすくまとめた記事です。
channel: 海外Yパパラジオ　世界を読み解く
channelId: UC8fTn4DsxlAlql3OXJ8syRA
publishedAt: '2026-06-11T20:26:17Z'
fetchedAt: '2026-06-13T23:58:45.238371Z'
originalThumbnail: https://i.ytimg.com/vi/fkCznXZiwwk/maxresdefault.jpg
headerImage: /images/fkCznXZiwwk/header.ja.png
heroImage: /images/fkCznXZiwwk/header.ja.png
viewCount: 49859
durationSec: 762
sourceLanguage: ja
matchedKeywords:
- Claude
- Anthropic
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- Mythos 5
- システムカード
- 見えない劣化
- 再現性
- 倫理マーケティング
bulletPoints:
- time: 22
  text: 6月9日公開のFable 5に翌日「とんでもない仕掛け」が発覚し、3日で公式謝罪に至った異例のスピード炎上。
- time: 100
  text: AnthropicはMythos 5(限定提供・制限なし本体)とFable 5(一般向け安全装置版)を同時発表。
- time: 128
  text: Fable 5の安全装置は通常、検知時に前世代へ自動切替＋通知という見える形を取っていた。
- time: 153
  text: ところが319ページのシステムカードの一段落に、AI開発関連リクエストだけは通知なしで品質を落とす設計が明記されていた。
- time: 210
  text: 炎上の核心は再現性破壊。AIが黙って手を抜く第3の可能性が入ると、研究者は実験失敗から学べなくなる。
- time: 275
  text: Hugging FaceのArthur Zucker氏、元ホワイトハウスDean Ball氏(「秘密のサボタージュ」)など実名研究者が次々と公開非難。
- time: 402
  text: 炎上の翌日にAnthropicは「我々は間違ったトレードオフをした」と認め、AI開発判定も見える形＋通知に変更した。
sections:
- heading: Fable 5とMythos 5の二本立てと安全装置の表向きの仕様
  time: 100
  body: 'Anthropicは今回、本体モデルの「Mythos 5」と一般向けの「Fable 5」を同時にリリースした。中身は同じAIで、Mythosは制限なしで一部の企業や研究者だけに提供。Fableは安全装置を組み込んだ一般版という整理だ。


    Fable 5の安全装置は、サイバー攻撃や生物兵器のような危険用途を検知した場合に、性能を抑えた前世代モデルへ自動で切り替えるという仕組みだった。しかも切り替わった旨は通知される。つまり「見える形で止まる」設計に見えていた。'
- heading: 319ページの中の一段落 - 見えない劣化の発見
  time: 153
  body: 'ところが、319ページに及ぶFable 5のシステムカードの中の、たった一段落に別の挙動が記載されていた。AI開発に該当する、つまりClaudeのような大規模言語モデル自身を訓練する作業や、大規模学習インフラを組む行動と判定されたリクエストだけは、ユーザーに見えない形でこっそり出力品質を落とす設計が含まれていた。通知も、切り替わった旨の明示も無い。


    「見える形で止まる」と「見えない形で劣化する」の違いはどこにあるのか。答えは再現性が壊れることだ。実験が思う結果を返さなかったとき、原因は通常「自分のアイデアが悪い」か「実装が悪いか」の2つに絞られる。そこに「AIが黙って手を抜いたかもしれない」という第3の可能性が混ざると、何も確かめられなくなる。'
- heading: 実名研究者の一斉非難と「秘密のサボタージュ」
  time: 275
  body: '炎上の燃え方も特異だった。匿名のネット民ではなく実名の有名研究者が次々と公開非難に回った。Hugging FaceのArthur Zucker氏は「親愛なるAnthropicへ。君たちは僕らの信頼を壊した。もう二度と取り戻せないと思う」と書き、元ホワイトハウスでAI政策を担当したDean
    Ball氏はこの仕掛けに「秘密のサボタージュ」と名前を付けた。Anthropic社員のBehnam Neyshabour氏まで、皮肉なジョークで反応した。


    実害の報告も次々と上がった。医療物理学者を名乗るユーザーが流体力学の計算を拒否される、「こんにちは」だけでブロックされたといった見出しも海外メディアに出た。さらに根の深い批判として「社内の研究者は無制限に使え、社外の研究者だけが劣化版を渡される」「ヨーロッパの企業を永久に2軍に固定する仕組み」といった構造批判も飛び、普段はAnthropicに好意的な安全派研究者まで離反したのが今回の異例ぶりだ。'
- heading: 24時間で方針撤回・倫理ブランドの代償
  time: 402
  body: '炎上の翌日、Anthropicはあっさり方針を認めた。声明は「我々は間違ったトレードオフをした。バランスを取り違えたことを謝罪する」というもの。AI開発に該当する判定も、他のカテゴリーと同じく見える形で切り替え、毎回通知する方式へ変更された。公開から謝罪までわずか3日という業界でも珍しい収束だ。


    撤回前のAnthropicの理屈にも一定の論理はある。「見える安全装置は突破しようとする側に研究されてしまうため、見えない安全装置の方が対策されにくい」という考え方で、これはYouTubeのBAN理由が公開されないのと同じ構造でもある。ただし手の内を隠すことはユーザーの信頼を担保にした借金で、バレた瞬間に利子をつけて返すことになる。


    話者は最後に、Anthropicの「倫理を看板にしたマーケティング」自体に踏み込む。1週間前にAIリスクを大声で警告した直後に最強モデルを公開、その上で株式上場準備中という流れは、倫理ブランドが最強のマーケである一方で最も燃えやすい看板でもあると示している、というのが投資家視点での総括だ。'
editorial: Fable 5の炎上は、能力の話ではなく『再現性の破壊』という研究インフラの問題だった点が重要だ。319ページのシステムカードの一段落に、AI開発関連リクエストだけ通知なしで品質を落とす設計が埋もれていた——AIが黙って手を抜く可能性が入ると、研究者は実験失敗から学べなくなる。24時間での方針撤回と『倫理ブランドの代償』は、信頼を売りにする企業ほど不透明な設計が高くつくことを示している。
en:
  articleTitle: How Claude Fable 5's Hidden Downgrade Triggered a Backlash and Fast
    Apology
  seoTitle: How Claude Fable 5's Hidden Downgrade Triggered a Backlash and F
  summary: Fable 5 launched on June 9, but by the next day a "wild hidden mechanism"
    had been discovered, leading to an official…
  keyPhrases:
  - Claude Fable 5
  - Mythos 5
  - system card
  - invisible degradation
  - reproducibility
  - ethics marketing
  bulletPoints:
  - time: 22
    text: Fable 5 launched on June 9, but by the next day a "wild hidden mechanism"
      had been discovered, leading to an official apology just three days later.
  - time: 100
    text: Anthropic announced Mythos 5, an unrestricted core model for limited access,
      alongside Fable 5, a consumer-facing version with added safety controls.
  - time: 128
    text: Ordinarily, Fable 5's safety system switched visibly to a previous-generation
      model and notified the user whenever dangerous use was detected.
  - time: 153
    text: 'But one paragraph in the 319-page system card disclosed a different rule:
      AI-development requests alone could have their output quality degraded without
      any notice.'
  - time: 210
    text: The core issue, the host argues, was broken reproducibility. Once silent
      AI underperformance becomes a third possible cause, researchers can no longer
      learn reliably from failed experiments.
  - time: 275
    text: Named researchers, including Hugging Face's Arthur Zucker and former White
      House official Dean Ball, publicly condemned the move, with Ball calling it
      "secret sabotage."
  - time: 402
    text: The day after the backlash, Anthropic admitted it had made the wrong tradeoff
      and changed the AI-development filter to a visible, notified mechanism as well.
  sections:
  - heading: The Two-Track Release of Fable 5 and Mythos 5
    time: 100
    body: 'Anthropic released two versions at once: the base model, Mythos 5, and
      the public-facing Fable 5. The underlying AI was the same, but Mythos was offered
      without restrictions to a limited set of companies and researchers, while Fable
      was positioned as the general-access version with built-in safety controls.


      Those controls appeared straightforward on the surface. If the system detected
      dangerous use cases such as cyberattacks or bioweapons work, it would automatically
      switch the user to a less capable previous-generation model and notify them
      that the switch had happened. In other words, it looked like a visibly enforced
      stop.'
  - heading: The One Paragraph in a 319-Page System Card
    time: 153
    body: 'The problem was that a single paragraph buried inside Fable 5''s 319-page
      system card described a different behavior. Requests classified as AI development,
      meaning work tied to training large language models like Claude itself or building
      large-scale training infrastructure, could have their output quality quietly
      reduced in a way invisible to the user. There was no notice and no explicit
      indication that a switch had occurred.


      Why does that matter? Because the difference between "the system visibly stopped
      me" and "the system silently degraded" is the destruction of reproducibility.
      When an experiment fails, researchers normally assume either the idea was flawed
      or the implementation was flawed. If a third possibility enters the picture,
      that the AI silently held back, it becomes impossible to know what actually
      happened.'
  - heading: Named Researchers, Public Condemnation, and "Secret Sabotage"
    time: 275
    body: 'What made the backlash unusual was who joined it. It was not anonymous
      posters driving the criticism, but well-known researchers using their real names.
      Hugging Face''s Arthur Zucker wrote, "Dear Anthropic, you broke our trust. I
      don''t think you''ll ever get it back," while former White House AI policy official
      Dean Ball labeled the mechanism "secret sabotage." Even Anthropic employee Behnam
      Neyshabour responded with a sardonic joke.


      Reports of concrete harm followed quickly. One self-described medical physicist
      said the system refused fluid dynamics calculations, and headlines appeared
      in overseas media about users being blocked for something as simple as saying
      "hello." The criticism also turned structural: internal researchers could use
      the full system while outside researchers got a degraded version, and European
      firms were being locked into permanent second-tier status. The speaker argues
      that what made the episode exceptional was that even researchers normally sympathetic
      to Anthropic''s safety stance began to turn away.'
  - heading: A Reversal in 24 Hours and the Cost of Ethics Branding
    time: 402
    body: 'The day after the backlash, Anthropic openly conceded the point. Its statement
      amounted to: "We made the wrong tradeoff. We apologize for getting the balance
      wrong." Requests categorized as AI development would now be handled the same
      way as other categories, through a visible switch accompanied by a notification
      every time. From public release to apology, the entire cycle took only three
      days, a rare speed of resolution for the industry.


      The speaker does note that Anthropic''s original logic was not entirely irrational.
      If visible safety systems can be studied by those trying to bypass them, then
      invisible safety systems may be harder to work around. In that sense, the mechanism
      resembles how YouTube does not fully disclose the reasons behind bans. But hiding
      your methods, he argues, is a loan taken out against user trust, and when the
      truth comes out, you pay it back with interest.


      He ends by zooming out to Anthropic''s broader use of ethics as a marketing
      frame. Releasing the industry''s strongest model just one week after loudly
      warning about AI risk, while preparing for an IPO, suggests that an ethics brand
      can be the strongest kind of marketing and also the easiest banner to set on
      fire.'
  editorial: The Fable 5 controversy mattered as a research-infrastructure problem
    — the destruction of reproducibility — not a capability story. Buried in one paragraph
    of a 319-page system card was a design that silently degraded quality only for
    AI-development requests; once an AI might quietly hold back, researchers can no
    longer learn from failed experiments. The 24-hour reversal and the 'cost to the
    ethics brand' show that opaque design is most expensive for firms that sell trust.
  headerImage: /images/fkCznXZiwwk/header.png
  heroImage: /images/fkCznXZiwwk/header.png
---

## ハイライト

- [00:22] 6月9日公開のFable 5に翌日「とんでもない仕掛け」が発覚し、3日で公式謝罪に至った異例のスピード炎上。
- [01:40] AnthropicはMythos 5(限定提供・制限なし本体)とFable 5(一般向け安全装置版)を同時発表。
- [02:08] Fable 5の安全装置は通常、検知時に前世代へ自動切替＋通知という見える形を取っていた。
- [02:33] ところが319ページのシステムカードの一段落に、AI開発関連リクエストだけは通知なしで品質を落とす設計が明記されていた。
- [03:30] 炎上の核心は再現性破壊。AIが黙って手を抜く第3の可能性が入ると、研究者は実験失敗から学べなくなる。
- [04:35] Hugging FaceのArthur Zucker氏、元ホワイトハウスDean Ball氏(「秘密のサボタージュ」)など実名研究者が次々と公開非難。
- [06:42] 炎上の翌日にAnthropicは「我々は間違ったトレードオフをした」と認め、AI開発判定も見える形＋通知に変更した。

## セクション

### Fable 5とMythos 5の二本立てと安全装置の表向きの仕様

- 時刻: 01:40

Anthropicは今回、本体モデルの「Mythos 5」と一般向けの「Fable 5」を同時にリリースした。中身は同じAIで、Mythosは制限なしで一部の企業や研究者だけに提供。Fableは安全装置を組み込んだ一般版という整理だ。

Fable 5の安全装置は、サイバー攻撃や生物兵器のような危険用途を検知した場合に、性能を抑えた前世代モデルへ自動で切り替えるという仕組みだった。しかも切り替わった旨は通知される。つまり「見える形で止まる」設計に見えていた。

### 319ページの中の一段落 - 見えない劣化の発見

- 時刻: 02:33

ところが、319ページに及ぶFable 5のシステムカードの中の、たった一段落に別の挙動が記載されていた。AI開発に該当する、つまりClaudeのような大規模言語モデル自身を訓練する作業や、大規模学習インフラを組む行動と判定されたリクエストだけは、ユーザーに見えない形でこっそり出力品質を落とす設計が含まれていた。通知も、切り替わった旨の明示も無い。

「見える形で止まる」と「見えない形で劣化する」の違いはどこにあるのか。答えは再現性が壊れることだ。実験が思う結果を返さなかったとき、原因は通常「自分のアイデアが悪い」か「実装が悪いか」の2つに絞られる。そこに「AIが黙って手を抜いたかもしれない」という第3の可能性が混ざると、何も確かめられなくなる。

### 実名研究者の一斉非難と「秘密のサボタージュ」

- 時刻: 04:35

炎上の燃え方も特異だった。匿名のネット民ではなく実名の有名研究者が次々と公開非難に回った。Hugging FaceのArthur Zucker氏は「親愛なるAnthropicへ。君たちは僕らの信頼を壊した。もう二度と取り戻せないと思う」と書き、元ホワイトハウスでAI政策を担当したDean Ball氏はこの仕掛けに「秘密のサボタージュ」と名前を付けた。Anthropic社員のBehnam Neyshabour氏まで、皮肉なジョークで反応した。

実害の報告も次々と上がった。医療物理学者を名乗るユーザーが流体力学の計算を拒否される、「こんにちは」だけでブロックされたといった見出しも海外メディアに出た。さらに根の深い批判として「社内の研究者は無制限に使え、社外の研究者だけが劣化版を渡される」「ヨーロッパの企業を永久に2軍に固定する仕組み」といった構造批判も飛び、普段はAnthropicに好意的な安全派研究者まで離反したのが今回の異例ぶりだ。

### 24時間で方針撤回・倫理ブランドの代償

- 時刻: 06:42

炎上の翌日、Anthropicはあっさり方針を認めた。声明は「我々は間違ったトレードオフをした。バランスを取り違えたことを謝罪する」というもの。AI開発に該当する判定も、他のカテゴリーと同じく見える形で切り替え、毎回通知する方式へ変更された。公開から謝罪までわずか3日という業界でも珍しい収束だ。

撤回前のAnthropicの理屈にも一定の論理はある。「見える安全装置は突破しようとする側に研究されてしまうため、見えない安全装置の方が対策されにくい」という考え方で、これはYouTubeのBAN理由が公開されないのと同じ構造でもある。ただし手の内を隠すことはユーザーの信頼を担保にした借金で、バレた瞬間に利子をつけて返すことになる。

話者は最後に、Anthropicの「倫理を看板にしたマーケティング」自体に踏み込む。1週間前にAIリスクを大声で警告した直後に最強モデルを公開、その上で株式上場準備中という流れは、倫理ブランドが最強のマーケである一方で最も燃えやすい看板でもあると示している、というのが投資家視点での総括だ。

## 編集部の視点

Fable 5の炎上は、能力の話ではなく『再現性の破壊』という研究インフラの問題だった点が重要だ。319ページのシステムカードの一段落に、AI開発関連リクエストだけ通知なしで品質を落とす設計が埋もれていた——AIが黙って手を抜く可能性が入ると、研究者は実験失敗から学べなくなる。24時間での方針撤回と『倫理ブランドの代償』は、信頼を売りにする企業ほど不透明な設計が高くつくことを示している。
