---
videoId: NCJ5tvZw7qM
title: ¿Puede Claude sustituirme?
slug: インディー開発者が本音で検証claudeはfableでもバグ修正にトークンの25以上を浪費逆にopusが一発で完-ncj5tvzw7qm
articleTitle: インディー開発者が本音で検証：ClaudeはFableでもバグ修正にトークンの25%以上を浪費、逆にOpusが一発で完璧に直した
seoTitle: インディー開発者が本音で検証：ClaudeはFableでもバグ修正にトークンの25%以上を浪費、逆にOpusが一発で完璧に直した
summary: 手作業でゲームを開発するインディー開発者が、視聴者から毎日のように浴びせられる『AIを使わないのか』という質問に応えるべく、実際にClaudeを試してみた。
channel: Alva Majo
channelId: UCmaEoq1zaakpdudbzgll-zw
publishedAt: '2026-07-08T17:00:01Z'
fetchedAt: '2026-07-10T09:40:18.238833Z'
originalThumbnail: https://i.ytimg.com/vi/NCJ5tvZw7qM/maxresdefault.jpg
headerImage: /images/NCJ5tvZw7qM/header.ja.png
heroImage: /images/NCJ5tvZw7qM/header.ja.png
viewCount: 182452
durationSec: 2087
sourceLanguage: es-ES
matchedKeywords:
- Claude
proposedByLLM: false
keyPhrases:
- Claude Fable 5
- Claude Opus
- Claude Sonnet
- バグ修正
- インディーゲーム開発
bulletPoints:
- time: 0
  text: 手作業でゲームを開発するインディー開発者が、視聴者から毎日のように浴びせられる『AIを使わないのか』という質問に応えるべく、実際にClaudeを試してみた。
- time: 33
  text: AIを使わない理由は、複雑な構造を持つプロジェクトの半ばにいて全体を自分で把握しておきたいからだと説明しつつ、それでも一度自分で検証してみることにした。
- time: 2013
  text: 最上位モデルのFableに2つのバグを直させたところ、セッショントークンの25%以上を消費してしまい、実用性に疑問符がついた。
- time: 2027
  text: 好奇心で同じバグをOpusに切り替えて試したところ、Fableより賢いはずなのに削除されていたチェックを復活させるという完璧な解決策を一発で出した一方、Sonnetは全く直せなかった。
sections:
- heading: 『AIを使わないのか』への本音
  time: 0
  body: インディーゲーム開発者の著者は、Twitchでの開発配信中に毎日のように『手作業でコーディングしているのか』『Claude Codeを使わないのか』と尋ねられることにうんざりしていたという。手で書いているのは、複雑な構造を持つプロジェクトの半ばにいて全体を自分で把握しておきたいからだと説明しつつ、視聴者から『ロボット差別だ』と言われることもあり、一度自分で実際に検証してみることにした。
- heading: Fable・Opus・Sonnetのバグ修正対決
  time: 2013
  body: 実際にゲーム内で発生した2つのバグを最上位モデルのFableに修正させたところ、それだけでセッショントークンの25%以上を消費してしまい、実用性に疑問符がついたと振り返る。好奇心から同じバグを再現させてモデルをOpusに切り替えたところ、Fableより賢いはずなのに、削除されていたチェック処理を復活させるという完璧な解決策を一発で提示した。さらにSonnetでも試したが、こちらは問題を解決しない無関係な変更をコードのあちこちに加えただけで、修正には至らなかった。
- heading: 使うかどうかの結論
  time: 2065
  body: 総括として、予想より優れていたが完全に信頼できるわけではないと結論づける。自分のプロジェクトのメインコード生成には使わないとしつつも、原因箇所の特定に何十分も費やすようなバグ探しの補助としては、多くの手間とストレスを省けると評価する。今後新しいプロジェクトを始めるなら、最初からAIなしで全て手作業に戻るのは『石器時代に戻るようなもの』とも語る一方、頼りすぎるとコードを理解できなくなり自分では何も追加できなくなる危険があるとも警告し、慎重に使えば生産性の乗数になると締めくくった。
editorial: この検証で最も興味深いのは、上位モデルであるはずのFableが単純なバグ修正で大量のトークンを消費した一方、Opusが同じバグを一発で完璧に直したという逆転現象だ。モデルのランク付けが必ずしもタスクごとの実用的な効率に直結しないことを示しており、『とりあえず最上位モデルを使えばよい』という単純な判断が、コストと精度の両面で最適とは限らないという実務的な教訓になる。また、自分でコードを書き続ける開発者ならではの『理解を失うことへの警戒』は、AIエージェント全盛の時代においてこそ意識すべき視点であり、生産性の追求と技術的な自律性の維持という二つの価値のバランスを考えさせる証言だ。
en:
  articleTitle: 'An Indie Developer''s Honest Verdict: Claude''s Top Model Burned
    Over 25% of Session Tokens on a Bug Fix -- Then Opus Nailed It in One Shot'
  seoTitle: 'An Indie Developer''s Honest Verdict: Claude''s Top Model Burned O'
  summary: A developer who codes his game entirely by hand finally put Claude to the
    test, after fielding the same 'why don't you…
  keyPhrases:
  - Claude Fable 5
  - Claude Opus
  - Claude Sonnet
  - bug fixing
  - indie game development
  bulletPoints:
  - time: 0
    text: A developer who codes his game entirely by hand finally put Claude to the
      test, after fielding the same 'why don't you use AI?' question from viewers
      day after day.
  - time: 33
    text: He explains he avoids AI because he's mid-way through a project with a complex
      structure and wants to keep understanding it fully himself -- but agreed to
      try it out regardless.
  - time: 2013
    text: Fixing two bugs with the top-tier Fable model alone burned over 25% of the
      session's tokens, raising real doubts about its practicality.
  - time: 2027
    text: Out of curiosity, he switched to Opus for the same bugs -- and despite Fable
      supposedly being smarter, Opus nailed a perfect fix (restoring a deleted check)
      in one shot, while Sonnet couldn't fix it at all.
  sections:
  - heading: The Honest Answer to 'Why Don't You Use AI?'
    time: 0
    body: This indie game developer says he's tired of being asked, almost every single
      stream on Twitch, whether he's coding by hand and why he doesn't just use Claude
      Code. He explains that he codes by hand because he's mid-way through a project
      with a complicated structure and wants to keep a full grasp of how everything
      works. Viewers sometimes accuse him of being 'a robot racist' for it -- so he
      decided it was time to actually put it to the test himself.
  - heading: 'Fable vs. Opus vs. Sonnet: The Bug-Fix Showdown'
    time: 2013
    body: Handing two real bugs from his game to the top-tier Fable model alone burned
      through more than 25% of the session's tokens, he recalls, which raised real
      doubts about its practicality. Out of curiosity, he reproduced the same bug
      and switched the model to Opus -- and despite Fable supposedly being the smarter
      model, Opus delivered a perfect fix in one shot, restoring a check that had
      been deleted. He also tried Sonnet, which failed entirely, scattering unrelated
      changes through the code without ever actually resolving the issue.
  - heading: The Verdict
    time: 2065
    body: 'His overall conclusion: better than expected, but not fully reliable. He
      won''t use it to generate the main code for his own project, but for hunting
      down bugs -- something that can eat up half an hour of searching for the exact
      cause -- it can save a lot of time and frustration. Starting a brand-new project
      entirely by hand from now on would feel like ''going back to the stone age,''
      he admits, while also warning that leaning on it too much risks losing your
      grip on your own code to the point you can''t add anything without asking Claude
      first. Used carefully, he concludes, it''s a genuine productivity multiplier.'
  editorial: 'The most interesting twist here is the reversal: the supposedly top-ranked
    Fable model burned a huge share of tokens on a simple bug fix, while Opus solved
    the exact same bug perfectly in one attempt. It''s a reminder that a model''s
    rank doesn''t necessarily translate into task-level efficiency -- ''just use the
    top model'' isn''t automatically the optimal call on cost or accuracy. And the
    developer''s own wariness about losing his grip on the codebase is a perspective
    worth holding onto in the agentic era: the pursuit of productivity and the preservation
    of technical self-sufficiency are two values that need active balancing, not one
    traded blindly for the other.'
  headerImage: /images/NCJ5tvZw7qM/header.png
  heroImage: /images/NCJ5tvZw7qM/header.png
---

## ハイライト

- [00:00] 手作業でゲームを開発するインディー開発者が、視聴者から毎日のように浴びせられる『AIを使わないのか』という質問に応えるべく、実際にClaudeを試してみた。
- [00:33] AIを使わない理由は、複雑な構造を持つプロジェクトの半ばにいて全体を自分で把握しておきたいからだと説明しつつ、それでも一度自分で検証してみることにした。
- [33:33] 最上位モデルのFableに2つのバグを直させたところ、セッショントークンの25%以上を消費してしまい、実用性に疑問符がついた。
- [33:47] 好奇心で同じバグをOpusに切り替えて試したところ、Fableより賢いはずなのに削除されていたチェックを復活させるという完璧な解決策を一発で出した一方、Sonnetは全く直せなかった。

## セクション

### 『AIを使わないのか』への本音

- 時刻: 00:00

インディーゲーム開発者の著者は、Twitchでの開発配信中に毎日のように『手作業でコーディングしているのか』『Claude Codeを使わないのか』と尋ねられることにうんざりしていたという。手で書いているのは、複雑な構造を持つプロジェクトの半ばにいて全体を自分で把握しておきたいからだと説明しつつ、視聴者から『ロボット差別だ』と言われることもあり、一度自分で実際に検証してみることにした。

### Fable・Opus・Sonnetのバグ修正対決

- 時刻: 33:33

実際にゲーム内で発生した2つのバグを最上位モデルのFableに修正させたところ、それだけでセッショントークンの25%以上を消費してしまい、実用性に疑問符がついたと振り返る。好奇心から同じバグを再現させてモデルをOpusに切り替えたところ、Fableより賢いはずなのに、削除されていたチェック処理を復活させるという完璧な解決策を一発で提示した。さらにSonnetでも試したが、こちらは問題を解決しない無関係な変更をコードのあちこちに加えただけで、修正には至らなかった。

### 使うかどうかの結論

- 時刻: 34:25

総括として、予想より優れていたが完全に信頼できるわけではないと結論づける。自分のプロジェクトのメインコード生成には使わないとしつつも、原因箇所の特定に何十分も費やすようなバグ探しの補助としては、多くの手間とストレスを省けると評価する。今後新しいプロジェクトを始めるなら、最初からAIなしで全て手作業に戻るのは『石器時代に戻るようなもの』とも語る一方、頼りすぎるとコードを理解できなくなり自分では何も追加できなくなる危険があるとも警告し、慎重に使えば生産性の乗数になると締めくくった。

## 編集部の視点

この検証で最も興味深いのは、上位モデルであるはずのFableが単純なバグ修正で大量のトークンを消費した一方、Opusが同じバグを一発で完璧に直したという逆転現象だ。モデルのランク付けが必ずしもタスクごとの実用的な効率に直結しないことを示しており、『とりあえず最上位モデルを使えばよい』という単純な判断が、コストと精度の両面で最適とは限らないという実務的な教訓になる。また、自分でコードを書き続ける開発者ならではの『理解を失うことへの警戒』は、AIエージェント全盛の時代においてこそ意識すべき視点であり、生産性の追求と技術的な自律性の維持という二つの価値のバランスを考えさせる証言だ。
