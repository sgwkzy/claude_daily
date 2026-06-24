---
videoId: HtKx75MwDBc
title: El creador de Claude Code dejó de promptear (ahora corre loops)
slug: プロンプトを書くなループを設計しろ-claude-codeを4台で24-7自走させる実践-htkx75mwdbc
articleTitle: 『プロンプトを書くな、ループを設計しろ』 — Claude Codeを4台で24/7自走させる実践
seoTitle: 『プロンプトを書くな、ループを設計しろ』 — Claude Codeを4台で24/7自走させる実践
summary: 動画のオープニング映像はデモではなく日常運用。投稿者は4台のマシンでClaude Codeをノンストップ稼働させ、数日間プロンプトを1つも書いていない。
channel: Benjamín Cordero
channelId: UCpq8lHHliCS3oBt-gfL0bKQ
publishedAt: '2026-06-22T01:32:52Z'
fetchedAt: '2026-06-24T00:51:56.393092Z'
originalThumbnail: https://i.ytimg.com/vi/HtKx75MwDBc/maxresdefault.jpg
headerImage: /images/HtKx75MwDBc/header.ja.png
heroImage: /images/HtKx75MwDBc/header.ja.png
viewCount: 31672
durationSec: 2278
sourceLanguage: es-419
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Claude Code 24/7自走
- Anthropic責任者『loopsを書く』
- /goal と /loopスキル
- ループ5要素
- 操作者から建築家へ
- Benjamín Cordero実践
bulletPoints:
- time: 0
  text: 動画のオープニング映像はデモではなく日常運用。投稿者は4台のマシンでClaude Codeをノンストップ稼働させ、数日間プロンプトを1つも書いていない。
- time: 12
  text: 1台目はコミュニティ投稿を常時スクレイプして再インデックス、成果に応じて再学習。2台目は毎時YouTubeでバズる切り口・動画をハント。3台目はワールドニュースとコミュニティ動向を監視。
- time: 41
  text: 別の1台はそれらを統合してToDoリスト化、さらに別の1台は長時間ビルドを単独実行中。各台はそれぞれ独立サブスクリプションでClaude Codeを24/7稼働。
- time: 66
  text: AnthropicのClaude Code責任者本人が壇上で『プロンプトを書くのをやめてループを書いている』と発言。動画はその設計手法を実装レベルで解説。
- time: 1062
  text: 'ループ4要素: 構築→修正→検証→ゴール判定。脱出条件を満たすまで反復。これに『記憶』(コンテキスト外を覚えておく頭脳) を加えるのが安定稼働の鍵。'
- time: 1110
  text: Claude CodeのSlash skillsとして実装可能 (Codexにもループ機能あり)。/goalは有限ループ、/loopは無限ループ用に使い分ける。
- time: 2206
  text: '結論: ツールを操作するな、エージェントを編成してツールを操作させ、さらにループでエージェント編成を編成しろ。一段抽象を上げてプロンプトをやめ設計を始めよ。'
- time: 2220
  text: プロンプトは1メッセージで使い切るが、ループは自分が席にいなくても回り続ける。我々はもう操作者ではなく『建築家』。買うな、ループで構築せよ、というのが本動画のマントラ。
sections:
- heading: 4台のClaude Codeが24/7自走する日常
  time: 0
  body: '動画の冒頭は派手なデモに見えるが、これは投稿者Benjamín Corderoの日常運用そのものだ。物理的に4台のマシンが並び、各台でClaude
    Codeがノンストップに動いており、もう数日間プロンプトは1行も書いていない。


    各台の役割は明確に分かれている。1台目は自身のコミュニティ投稿を常時スクレイプしてラックに再インデックスし、パフォーマンス良し悪しに応じて再学習を回す。2台目は1時間ごとにYouTube側でバズっている切り口・動画をハントし、翌朝にアプローチ案付きで提示。3台目は世界とコミュニティの動向を監視。4台目はそれら全てを統合してToDoリストを更新。さらに別の1台が長時間ビルドを単独実行している。すべて独立サブスクリプションでClaude
    Codeを24/7稼働させる。投稿者はこれを誰かのツイートで知ったのではなく数ヶ月前から実践してきた、と強調する。'
- heading: ループ設計の核 — 構築・修正・検証・ゴール・記憶
  time: 1062
  body: 'Anthropic内部でClaude Codeを率いる人物自身が壇上で『プロンプトを書くのをやめてループを書いている』と発言した。本動画はその実装を5つの構成要素で整理する。構築
    → 修正 → 検証 → ゴール判定の主ループ、さらに『記憶』としてコンテキストウィンドウ外の情報を保持する脳部分。これを揃えると、人が見ていない間もエージェントが進捗を出し続ける。


    実装はClaude CodeのSlashスキルで完結する。`/goal` は有限ループ (達成条件で抜ける) 用、`/loop` は無限ループ用、と使い分ける。Anthropicが新機能を出すと大抵この付近の改善になる、というのが投稿者の観察だ。同じ発想はCodexでも実装可能で、ツール固有のテクニックというより、ワークフロー設計のメンタルモデルが本質である点が繰り返し強調される。'
- heading: プロンプトは消費、ループは滞留 — 操作者から建築家へ
  time: 2206
  body: '結論部で投稿者は明快なテーゼを提示する。『ツールを操作するな、エージェントを編成してツールを操作させ、さらにループでエージェント編成を編成せよ』。一段抽象を上げ、プロンプトを書くのをやめて『設計』を始める、という呼びかけだ。


    プロンプトは1メッセージ送れば使い切られる消費財だが、ループは自分が席にいなくても回り続ける。だから我々はもうエージェントの操作者ではなく『建築家』であるべきだ。3年以上動画を上げてきた投稿者の中核テーゼ『未来のプログラミング言語は自然言語』が、いまループという形で具体的な実装手法に落ちた、という総括で締める。チャンネルのマントラ『買うな、構築せよ、そしてループでより良く構築せよ』に繋がる。'
en:
  articleTitle: Stop Writing Prompts, Start Designing Loops — Running Four Claude
    Code Boxes 24/7
  seoTitle: Stop Writing Prompts, Start Designing Loops — Running Four Claud
  summary: The opening footage isn't a demo. It's the creator's daily setup — four
    machines running Claude Code nonstop, with no…
  keyPhrases:
  - Claude Code 24/7 self-running
  - Anthropic lead says 'I write loops'
  - /goal and /loop slash skills
  - five loop primitives
  - operator to architect
  - Benjamín Cordero workflow
  bulletPoints:
  - time: 0
    text: The opening footage isn't a demo. It's the creator's daily setup — four
      machines running Claude Code nonstop, with no prompt typed in days.
  - time: 12
    text: Box 1 continuously scrapes his community posts and reindexes them, retraining
      on what performs. Box 2 hunts trending YouTube angles each hour. Box 3 monitors
      world and community signals.
  - time: 41
    text: One box ties everything together into a running to-do list, another is mid-multi-hour
      build. Each box runs on its own subscription, Claude Code 24/7.
  - time: 66
    text: 'The lead on Claude Code inside Anthropic said it on stage: he doesn''t
      write prompts anymore, he writes loops. This video walks through the design
      pattern from the ground up.'
  - time: 1062
    text: 'Four loop pieces plus memory: build → fix → verify → goal check, then a
      ''brain'' that holds context the chat window forgets. That''s the rig.'
  - time: 1110
    text: It's implementable as Claude Code slash skills (Codex has a loop function
      too). /goal handles bounded loops, /loop handles open-ended ones.
  - time: 2206
    text: 'Thesis: stop operating tools. Orchestrate agents that operate tools. Then
      orchestrate the agent orchestration with loops. Move one level up the abstraction
      stack — stop prompting, start designing.'
  - time: 2220
    text: 'A prompt is spent in one message. A loop keeps running while you''re not
      there. You are no longer an operator — you''re an architect. The channel''s
      mantra: don''t buy, build, and build better with loops.'
  sections:
  - heading: Four Claude Code machines, running 24/7 — the actual daily setup
    time: 0
    body: 'The video opens on what looks like a flashy demo but is creator Benjamín
      Cordero''s daily reality. Four physical machines, each running Claude Code nonstop,
      and he hasn''t typed a prompt in days. He walks past them while they keep working.


      The roles are split cleanly. Box 1 continuously scrapes his community''s posts
      and reindexes them into a rack, retraining on which posts performed and which
      didn''t. Box 2 goes out once an hour to hunt trending angles and videos on YouTube,
      dropping them in his morning queue with possible approaches. Box 3 monitors
      the world and the community at large. A fourth ties it all into a running to-do
      list, and yet another is in the middle of a multi-hour build right now. Each
      box has its own subscription and runs Claude Code 24/7. He didn''t build this
      for the video — it''s been his workflow for months, longer than most people
      have been talking about this approach.'
  - heading: The loop primitives — build, fix, verify, goal, and memory
    time: 1062
    body: 'The lead on Claude Code inside Anthropic said it on stage: he no longer
      writes prompts, he writes loops. The video walks the pattern through five concrete
      pieces. The main loop is build → fix → verify → goal check, repeating until
      the exit condition fires. The fifth piece is memory — a ''brain'' that retains
      what falls out of the active context window so the loop doesn''t forget itself.


      The implementation is straight Claude Code slash skills (Codex has a loop function
      too, and the same pattern works there with the right prompting). `/goal` handles
      bounded loops — those with a definite finish line. `/loop` handles open-ended
      ones. The author observes that when Anthropic ships new features, they mostly
      land in this area — Dream and the rest are refinements on how loops work — which
      suggests the platform is moving toward this pattern as the primary mode.'
  - heading: Prompt vs loop — operator to architect
    time: 2206
    body: 'The closing thesis is crisp: stop operating tools. Orchestrate agents that
      operate tools. Then orchestrate the agent orchestration with loops. Move one
      level up the abstraction stack. Stop prompting, start designing.


      A prompt is spent in one message. A loop keeps running while you''re not at
      the keyboard. So you stop being an operator and become an architect. This isn''t
      a technique, the author says — it''s a mentality shift. If you can write and
      you can build, the programming language of the future is natural language. He''s
      been pushing that thesis for over a year and a half on the channel; loops are
      where it finally cashes out into a concrete workflow. Channel mantra to close:
      don''t buy, build, and build better with loops.'
  headerImage: /images/HtKx75MwDBc/header.png
  heroImage: /images/HtKx75MwDBc/header.png
---

## ハイライト

- [00:00] 動画のオープニング映像はデモではなく日常運用。投稿者は4台のマシンでClaude Codeをノンストップ稼働させ、数日間プロンプトを1つも書いていない。
- [00:12] 1台目はコミュニティ投稿を常時スクレイプして再インデックス、成果に応じて再学習。2台目は毎時YouTubeでバズる切り口・動画をハント。3台目はワールドニュースとコミュニティ動向を監視。
- [00:41] 別の1台はそれらを統合してToDoリスト化、さらに別の1台は長時間ビルドを単独実行中。各台はそれぞれ独立サブスクリプションでClaude Codeを24/7稼働。
- [01:06] AnthropicのClaude Code責任者本人が壇上で『プロンプトを書くのをやめてループを書いている』と発言。動画はその設計手法を実装レベルで解説。
- [17:42] ループ4要素: 構築→修正→検証→ゴール判定。脱出条件を満たすまで反復。これに『記憶』(コンテキスト外を覚えておく頭脳) を加えるのが安定稼働の鍵。
- [18:30] Claude CodeのSlash skillsとして実装可能 (Codexにもループ機能あり)。/goalは有限ループ、/loopは無限ループ用に使い分ける。
- [36:46] 結論: ツールを操作するな、エージェントを編成してツールを操作させ、さらにループでエージェント編成を編成しろ。一段抽象を上げてプロンプトをやめ設計を始めよ。
- [37:00] プロンプトは1メッセージで使い切るが、ループは自分が席にいなくても回り続ける。我々はもう操作者ではなく『建築家』。買うな、ループで構築せよ、というのが本動画のマントラ。

## セクション

### 4台のClaude Codeが24/7自走する日常

- 時刻: 00:00

動画の冒頭は派手なデモに見えるが、これは投稿者Benjamín Corderoの日常運用そのものだ。物理的に4台のマシンが並び、各台でClaude Codeがノンストップに動いており、もう数日間プロンプトは1行も書いていない。

各台の役割は明確に分かれている。1台目は自身のコミュニティ投稿を常時スクレイプしてラックに再インデックスし、パフォーマンス良し悪しに応じて再学習を回す。2台目は1時間ごとにYouTube側でバズっている切り口・動画をハントし、翌朝にアプローチ案付きで提示。3台目は世界とコミュニティの動向を監視。4台目はそれら全てを統合してToDoリストを更新。さらに別の1台が長時間ビルドを単独実行している。すべて独立サブスクリプションでClaude Codeを24/7稼働させる。投稿者はこれを誰かのツイートで知ったのではなく数ヶ月前から実践してきた、と強調する。

### ループ設計の核 — 構築・修正・検証・ゴール・記憶

- 時刻: 17:42

Anthropic内部でClaude Codeを率いる人物自身が壇上で『プロンプトを書くのをやめてループを書いている』と発言した。本動画はその実装を5つの構成要素で整理する。構築 → 修正 → 検証 → ゴール判定の主ループ、さらに『記憶』としてコンテキストウィンドウ外の情報を保持する脳部分。これを揃えると、人が見ていない間もエージェントが進捗を出し続ける。

実装はClaude CodeのSlashスキルで完結する。`/goal` は有限ループ (達成条件で抜ける) 用、`/loop` は無限ループ用、と使い分ける。Anthropicが新機能を出すと大抵この付近の改善になる、というのが投稿者の観察だ。同じ発想はCodexでも実装可能で、ツール固有のテクニックというより、ワークフロー設計のメンタルモデルが本質である点が繰り返し強調される。

### プロンプトは消費、ループは滞留 — 操作者から建築家へ

- 時刻: 36:46

結論部で投稿者は明快なテーゼを提示する。『ツールを操作するな、エージェントを編成してツールを操作させ、さらにループでエージェント編成を編成せよ』。一段抽象を上げ、プロンプトを書くのをやめて『設計』を始める、という呼びかけだ。

プロンプトは1メッセージ送れば使い切られる消費財だが、ループは自分が席にいなくても回り続ける。だから我々はもうエージェントの操作者ではなく『建築家』であるべきだ。3年以上動画を上げてきた投稿者の中核テーゼ『未来のプログラミング言語は自然言語』が、いまループという形で具体的な実装手法に落ちた、という総括で締める。チャンネルのマントラ『買うな、構築せよ、そしてループでより良く構築せよ』に繋がる。
