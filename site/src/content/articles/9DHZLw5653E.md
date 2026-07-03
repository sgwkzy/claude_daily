---
videoId: 9DHZLw5653E
title: How Spotify runs agents across 20M+ lines of code, with Niklas Gustavsson
slug: spotifyのエージェント活用術2000万行のコードベースで何が変わったか-9dhzlw5653e
articleTitle: Spotifyのエージェント活用術：2000万行のコードベースで何が変わったか
seoTitle: Spotifyのエージェント活用術：2000万行のコードベースで何が変わったか
summary: Spotifyのエンジニア歴30年のNiklas Gustavsson氏が、AIエージェント導入で開発スタイルが2ヶ月で一変したと語る。
channel: Claude
channelId: UCV03SRZXJEz-hchIAogeJOg
publishedAt: '2026-06-29T16:05:17Z'
fetchedAt: '2026-07-02T13:29:28.028816Z'
originalThumbnail: https://i.ytimg.com/vi/9DHZLw5653E/maxresdefault.jpg
headerImage: /images/9DHZLw5653E/header.ja.png
heroImage: /images/9DHZLw5653E/header.ja.png
viewCount: 81557
durationSec: 1571
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Spotify
- AIエージェント
- テスト自動化
- 自動マージ
- プロトタイピング
- Claude
bulletPoints:
- time: 0
  text: Spotifyのエンジニア歴30年のNiklas Gustavsson氏が、AIエージェント導入で開発スタイルが2ヶ月で一変したと語る。
- time: 10
  text: 「年内にIDEを使わなくなる」という昨年9月の予測が、実際にはわずか2ヶ月で現実になった。
- time: 755
  text: 数千のコンポーネントに分割された巨大なコードベースで、各チームが所有権を持つ体制を敷いていた。
- time: 799
  text: PRを自動マージする体制へ移行するため、事前にテスト自動化を大幅に強化する必要があった。
- time: 821
  text: 強化済みのテスト検証基盤があったからこそ、そこにエージェントを投入できるようになった。
- time: 1483
  text: 以前ならエンジニアチームを動かして数週間かかっていたアイデア検証が、1〜2時間で動くプロトタイプになる。
- time: 1525
  text: 共同CEOを含む経営陣までもが自らプロトタイプを作ってアプリストアに公開している。
sections:
- heading: IDE不要時代への急速な移行
  time: 0
  body: 'Spotifyでソフトウェアエンジニアリングを率いるNiklas Gustavsson氏は、molecular biology(分子生物学)出身という異色の経歴を持つ。かつて「年内には誰もIDEを使わなくなる」という趣旨の発言をした際、聞き手は「2年スケールならまだしも2ヶ月は極端すぎる」と感じたという。


    しかし実際には2ヶ月後、Gustavsson氏自身がIDEを使わなくなり、30年のキャリアで見たことのない働き方の変化を経験した。社内でもこの変化は外部の受け止めと全く同じ速度で起きていた。'
- heading: 自動マージを支える大規模テスト自動化
  time: 755
  body: 'Spotifyのコードベースは数千のコンポーネントに分割され、各コンポーネントは特定チームが設計・実装・運用まで一貫して責任を持つ体制だった。これまではチームが全てのPRを目視確認できる前提があったため、テスト自動化がやや甘くても許容されていた。


    しかしAIエージェントによる自動PR作成を進めるにあたり、「チームが見ないままマージされる変更」を前提とした体制へ転換する必要が生じた。そのため、変更に耐えられるだけの堅牢なテスト自動化基盤を先に構築した。'
- heading: 非エンジニアも数時間でプロトタイプを形にする
  time: 1483
  body: 'テスト基盤の整備が完了した今、Spotifyはその検証の仕組みをエージェントにもそのまま活用できるようになった。かつてはアイデアを形にするためにエンジニアチームを何週間も動かす必要があったが、今では1〜2時間で実際に触れるプロトタイプができ、リアルなユーザーやデータを使って検証できる。


    この変化は共同CEOを含む経営層にも及んでおり、アイデアを持つ非エンジニアが自らプロトタイプを作りアプリストアに公開する事例まで生まれている。1年前には想像もできなかったことが、今では日常になっている。'
editorial: この事例が示すのは、AIエージェントの生産性向上が「エージェント単体の性能」だけでなく「それを安全に使うための検証基盤」に強く依存するという点だ。Spotifyは自動マージを許容する前にテスト自動化への投資を先行させており、エージェント活用の成否は事前のインフラ整備で決まることを裏付けている。また、プロトタイピングの民主化により非エンジニアの経営層までコードを書く動きは、開発組織における役割分担そのものを揺るがす可能性がある。企業がエージェント導入を急ぐ際、まずテストと権限設計に投資すべきだという教訓は、日本企業にも直接応用できる示唆だろう。
en:
  articleTitle: How Spotify's Agents Rewired a 20M-Line Codebase in Two Months
  seoTitle: How Spotify's Agents Rewired a 20M-Line Codebase in Two Months
  summary: Niklas Gustavsson, a 30-year Spotify engineering veteran, says AI agents
    changed how his team works within just two…
  keyPhrases:
  - Spotify
  - AI agents
  - test automation
  - auto-merge
  - prototyping
  - Claude
  bulletPoints:
  - time: 0
    text: Niklas Gustavsson, a 30-year Spotify engineering veteran, says AI agents
      changed how his team works within just two months.
  - time: 10
    text: A prediction last September that 'no one would use an IDE by year-end' sounded
      extreme but became true in about two months.
  - time: 755
    text: Spotify's massive codebase is split into thousands of components, each fully
      owned by a single team.
  - time: 799
    text: Moving to auto-merged PRs required investing heavily in test automation
      beforehand.
  - time: 821
    text: That stronger verification infrastructure is exactly what let Spotify safely
      throw agents at the codebase.
  - time: 1483
    text: Ideas that once took weeks of engineering effort now become working prototypes
      in an hour or two.
  - time: 1525
    text: Even Spotify's co-CEOs have shipped their own prototypes to the internal
      app store.
  sections:
  - heading: A Sudden Shift Away From IDEs
    time: 0
    body: 'Niklas Gustavsson, who leads software engineering at Spotify and trained
      as a molecular biologist, once predicted that engineers would stop using IDEs
      by the end of the year. At the time it sounded implausible on anything shorter
      than a two-year horizon.


      Instead, the shift happened in about two months. Gustavsson found himself no
      longer using an IDE, describing a change in his workflow unlike anything he''d
      seen in three decades in the industry -- and the internal experience matched
      what was visible externally.'
  - heading: Test Automation as the Foundation for Auto-Merge
    time: 755
    body: 'Spotify''s codebase is split into thousands of components, each owned end-to-end
      by a specific team responsible for design, implementation, and operation. Historically,
      teams could review every PR merged into their code, which meant test automation
      could afford to be a bit loose.


      Rolling out AI agents that open PRs automatically meant teams would no longer
      see every change before it merged. That required building out much stronger
      test automation so the codebase could survive automated changes safely.'
  - heading: Prototypes in Hours, Not Weeks -- Even From Non-Engineers
    time: 1483
    body: 'With that verification infrastructure in place, Spotify could point agents
      at the same safety net. Ideas that once required mobilizing an engineering team
      for weeks now become working prototypes with real data and real users in an
      hour or two.


      That shift reaches beyond engineering: several senior executives, including
      one of Spotify''s co-CEOs, have built and shipped their own prototypes to the
      internal app store -- something unimaginable a year ago and now routine.'
  editorial: 'This case study shows that agent-driven productivity gains depend less
    on the agent''s raw capability and more on the verification infrastructure surrounding
    it. Spotify invested in test automation before allowing auto-merge, and that ordering
    is the real lesson: safety infrastructure has to come first. The democratization
    of prototyping -- reaching all the way to co-CEOs -- also hints at a coming shift
    in how engineering organizations divide labor, and it''s a pattern worth watching
    as more companies push agents into core codebases.'
  headerImage: /images/9DHZLw5653E/header.png
  heroImage: /images/9DHZLw5653E/header.png
---

## ハイライト

- [00:00] Spotifyのエンジニア歴30年のNiklas Gustavsson氏が、AIエージェント導入で開発スタイルが2ヶ月で一変したと語る。
- [00:10] 「年内にIDEを使わなくなる」という昨年9月の予測が、実際にはわずか2ヶ月で現実になった。
- [12:35] 数千のコンポーネントに分割された巨大なコードベースで、各チームが所有権を持つ体制を敷いていた。
- [13:19] PRを自動マージする体制へ移行するため、事前にテスト自動化を大幅に強化する必要があった。
- [13:41] 強化済みのテスト検証基盤があったからこそ、そこにエージェントを投入できるようになった。
- [24:43] 以前ならエンジニアチームを動かして数週間かかっていたアイデア検証が、1〜2時間で動くプロトタイプになる。
- [25:25] 共同CEOを含む経営陣までもが自らプロトタイプを作ってアプリストアに公開している。

## セクション

### IDE不要時代への急速な移行

- 時刻: 00:00

Spotifyでソフトウェアエンジニアリングを率いるNiklas Gustavsson氏は、molecular biology(分子生物学)出身という異色の経歴を持つ。かつて「年内には誰もIDEを使わなくなる」という趣旨の発言をした際、聞き手は「2年スケールならまだしも2ヶ月は極端すぎる」と感じたという。

しかし実際には2ヶ月後、Gustavsson氏自身がIDEを使わなくなり、30年のキャリアで見たことのない働き方の変化を経験した。社内でもこの変化は外部の受け止めと全く同じ速度で起きていた。

### 自動マージを支える大規模テスト自動化

- 時刻: 12:35

Spotifyのコードベースは数千のコンポーネントに分割され、各コンポーネントは特定チームが設計・実装・運用まで一貫して責任を持つ体制だった。これまではチームが全てのPRを目視確認できる前提があったため、テスト自動化がやや甘くても許容されていた。

しかしAIエージェントによる自動PR作成を進めるにあたり、「チームが見ないままマージされる変更」を前提とした体制へ転換する必要が生じた。そのため、変更に耐えられるだけの堅牢なテスト自動化基盤を先に構築した。

### 非エンジニアも数時間でプロトタイプを形にする

- 時刻: 24:43

テスト基盤の整備が完了した今、Spotifyはその検証の仕組みをエージェントにもそのまま活用できるようになった。かつてはアイデアを形にするためにエンジニアチームを何週間も動かす必要があったが、今では1〜2時間で実際に触れるプロトタイプができ、リアルなユーザーやデータを使って検証できる。

この変化は共同CEOを含む経営層にも及んでおり、アイデアを持つ非エンジニアが自らプロトタイプを作りアプリストアに公開する事例まで生まれている。1年前には想像もできなかったことが、今では日常になっている。

## 編集部の視点

この事例が示すのは、AIエージェントの生産性向上が「エージェント単体の性能」だけでなく「それを安全に使うための検証基盤」に強く依存するという点だ。Spotifyは自動マージを許容する前にテスト自動化への投資を先行させており、エージェント活用の成否は事前のインフラ整備で決まることを裏付けている。また、プロトタイピングの民主化により非エンジニアの経営層までコードを書く動きは、開発組織における役割分担そのものを揺るがす可能性がある。企業がエージェント導入を急ぐ際、まずテストと権限設計に投資すべきだという教訓は、日本企業にも直接応用できる示唆だろう。
