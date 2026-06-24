---
videoId: v-6KM2ysQYo
title: 'Claude Code + Unreal Engine: Build a Full Game with AI (MCP Setup Tutorial)'
slug: claude-code-unreal-engine-58-ゲーム開発未経験者がgta-v-6km2ysqyo
articleTitle: Claude Code × Unreal Engine 5.8 — ゲーム開発未経験者がGTA 6風を2時間で作るMCPチュートリアル
seoTitle: Claude Code × Unreal Engine 5.8 — ゲーム開発未経験者がGTA 6風を2時間で作るMCPチュート
summary: 投稿者はゲーム開発経験ゼロ、Unreal Engineも触ったことなし。Claude CodeにGTA 6風ゲームをリクエストしたところ、2時間でNPC群、車両、Lucia/Jasonキャラ、射撃機能を備えたシーンが完成。
channel: Leon van Zyl
channelId: UCtevzRsHEKhs-RK8pAqwSyQ
publishedAt: '2026-06-21T12:46:07Z'
fetchedAt: '2026-06-24T00:52:44.972015Z'
originalThumbnail: https://i.ytimg.com/vi/v-6KM2ysQYo/maxresdefault.jpg
headerImage: /images/v-6KM2ysQYo/header.ja.png
heroImage: /images/v-6KM2ysQYo/header.ja.png
viewCount: 10237
durationSec: 1135
sourceLanguage: en
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Claude Code × Unreal Engine 5.8
- Unreal MCPサーバー
- GTA 6 thin sliceの2時間生成
- planning modeで設計を詰める
- 同期編集の限界
- インディー開発の生産性底上げ
bulletPoints:
- time: 0
  text: 投稿者はゲーム開発経験ゼロ、Unreal Engineも触ったことなし。Claude CodeにGTA 6風ゲームをリクエストしたところ、2時間でNPC群、車両、Lucia/Jasonキャラ、射撃機能を備えたシーンが完成。
- time: 33
  text: 本人は『ゲームデザイナーでも開発者でもないが、こんなものを2時間でvibe codingで作れるのは衝撃』とコメント。インディーシーンと創作層への影響を予感。
- time: 48
  text: セットアップは2点だけ。Unreal Engine 5.8 (最低5.8必須、launcher経由でDL) と、Claude Codeなどのcoding
    agent。MCPサーバーがUnreal側に登場したのが転機。
- time: 468
  text: 実演ではキューブ追加の指示でClaudeがシーンに直接介入できることを確認。playボタンでシーン内にキューブが出現する基本動作が成立。
- time: 505
  text: コツは planning mode の活用。プランニングモードではClaudeはシーンを変更せず、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを議論してから実装に入れる。
- time: 525
  text: '実プロンプト例: 『GTA 6を待ちきれないので、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを調査して、このゲームワールドでGTA 6のthin
    sliceを作って』。'
- time: 1066
  text: 現状の課題はMCPサーバーがまだ新しく、シーン編集が同期的なこと。同時に1つの編集しかできないため、複数エージェントの並列作業はまだ難しい。
- time: 1110
  text: '投稿者の結論: これらのツールはインディー開発者を置き換えるのでなく、雑用をAIに渡してハイチケット作業に集中できるようにする方向に向かう。'
sections:
- heading: ゲーム未経験者がClaude CodeでGTA 6風を組んだ衝撃
  time: 0
  body: 'Leon van Zylの動画オープニングは衝撃的だ。『私はゲームを作ったことがないし、Unreal Engineについても何も知らない』。それなのにClaude
    CodeにGTA 6風のゲームを作るよう頼んだら、約2時間でNPCで埋まったワールド、走行する車両、Lucia / Jasonキャラ、射撃機能を持つプレイ可能シーンができた、と本人もまだ実感がついていない様子で語る。


    投稿者は『ゲームデザイナーでも開発者でもない素人がvibe codingでこのレベルを2時間で組めるのは、率直に言って衝撃』だと述べる。これがインディーゲームシーンや創作層に与える影響は大きく、技術が個々のクリエイターを底上げする方向に向かう、というのが導入のテーゼだ。'
- heading: セットアップとプランニングモード — Unreal Engine 5.8 + Claude Code
  time: 48
  body: 'セットアップは2点だけだ。Unreal Engineを公式launcherからインストールし (最低5.8必須)、Claude Codeなどのコーディングエージェントを用意する。MCPサーバーがUnreal側に登場したことで、外部エージェントがシーンに直接介入できる構図が成立した。チュートリアル前半では小さなキューブを追加させる実演で、Claudeが本当にシーンと対話していることを確認し、playボタンを押すとキューブが出現する基本動作を見せる。


    実用上の重要なテクニックがplanning modeの活用だ。プランニングモードではClaudeはシーンに変更を加えない。代わりにゲームメカニクス・キャラデザ・ビジュアルデザイン・ロケーションといった設計事項を会話で詰められる。実際のプロンプト例は『GTA
    6を待ちきれないので、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを調査して、このゲームワールドでGTA 6のthin sliceを作って』だ。具体性と抽象性のバランスがうまく取れている。'
- heading: 現状の限界と将来 — 同期実行と複数エージェント並列の課題
  time: 1063
  body: '投稿者の総括は冷静だ。エージェントの完了に時間がかかった理由は、MCPサーバーがまだ新しいから。今後Epicが洗練させて、複数エージェントが同じシーンを同時編集できる経路を作る可能性が高い。現状は同期的で、一度に1編集しかできないため『エージェントチームを編成して各エージェントが別の変更を担当』という理想像にはまだ届いていない。


    産業構造の見立てはバランスが良い。インディーゲームが大好きで、ソロ開発者の生産物には常々感心している投稿者は、これらのツールがインディー開発者を置き換えるとは思っていない。むしろ、雑用
    (trivial tasks) をコーディングエージェントに渡して、本人が高付加価値タスクに集中できるようにする方向に向かう。次の技術展開を楽しみにしている、と締めくくる。'
editorial: ゲーム未経験者がUnreal Engine 5.8とClaude CodeでGTA 6風を2時間で組んだ事実は、エンジン習熟という参入障壁が崩れ始めたことを示す。転機はUnreal側にMCPサーバーが載ったことで、AIがエディタを直接操作できる点にある。重要なのはplanning
  mode——実装前にメカニクスや設計を議論させる使い方で、一発生成より設計対話が成果を左右する。投稿者の『置き換えではなく雑用を渡してハイチケット作業に集中』という結論は、AI開発支援の最も現実的な見立てだ。
en:
  articleTitle: Claude Code × Unreal Engine 5.8 — A First-Timer Built a GTA 6-Style
    World in Two Hours
  seoTitle: Claude Code × Unreal Engine 5.8 — A First-Timer Built a GTA 6-St
  summary: The creator has never built a game and doesn't know Unreal Engine. He asked
    Claude Code to build a GTA 6-style game;…
  keyPhrases:
  - Claude Code × Unreal Engine 5.8
  - Unreal MCP server
  - GTA 6 thin slice in two hours
  - planning mode for design
  - synchronous edit limit
  - indie productivity boost
  bulletPoints:
  - time: 0
    text: The creator has never built a game and doesn't know Unreal Engine. He asked
      Claude Code to build a GTA 6-style game; about two hours later he had a world
      full of NPCs, vehicles, Lucia and Jason in-game, and working shooting.
  - time: 33
    text: He's not a game designer or developer. The fact that vibe coding a scene
      at this level took two hours is, he says, mind-blowing. Implications for the
      indie scene are real.
  - time: 48
    text: 'Setup is minimal: Unreal Engine 5.8+ via the official launcher, and Claude
      Code (or any equivalent coding agent). The Unreal MCP server is the unlock.'
  - time: 468
    text: The first walk-through is a cube-add command, which Claude lands in the
      scene. Hit play and the cube is there. Basic interaction confirmed.
  - time: 505
    text: 'The big productivity tip: planning mode. Claude won''t touch the scene,
      so you can hash out mechanics, character design, visual direction, and locations
      before any code or asset moves.'
  - time: 525
    text: 'Sample prompt used: ''Hey Claude, I''m tired of waiting for GTA 6 — research
      mechanics, character design, visual design, location, and create a thin slice
      of GTA 6 inside this game world.'''
  - time: 1066
    text: 'The honest caveat: the MCP server is new, scene editing is currently synchronous,
      so multi-agent parallel work isn''t there yet. Expect Epic to refine this.'
  - time: 1110
    text: 'His take on indie devs: this isn''t a replacement. It frees solo creators
      from trivial tasks so they can spend their time on the higher-leverage parts
      of the build.'
  sections:
  - heading: Zero game-dev experience to GTA 6 thin slice in two hours
    time: 0
    body: 'Leon van Zyl''s opener doesn''t pull punches. ''I''ve never built a game
      in my life and I don''t really know much about Unreal Engine at all.'' He asked
      Claude Code to build a GTA 6-style game. Roughly two hours later he had a world
      full of NPCs, working vehicles, Lucia and Jason both in the scene, and working
      shoot mechanics. He stopped recording because he wanted to show the setup, not
      because the build had run out.


      He''s careful to call himself neither a game designer nor a developer. The point
      isn''t ''AI made me a game dev.'' The point is that vibe coding a scene at this
      level in two hours is, in his words, mind-blowing — and what it implies for
      the indie scene and for creative people generally is the larger story.'
  - heading: Setup and planning mode — Unreal Engine 5.8 + Claude Code
    time: 48
    body: 'Setup is two items. Download Unreal Engine via the official launcher (5.8
      minimum), and install Claude Code or any equivalent coding agent. The actual
      unlock is the Unreal MCP server, which lets an external agent reach into the
      scene directly. The tutorial confirms it with the smallest possible test: ask
      Claude to add a cube, watch the cube show up, hit play, and see the cube in
      the running scene. Basic interaction works.


      The productivity move is planning mode. Claude won''t touch the scene in this
      mode, so you can talk through mechanics, character design, visual direction,
      and locations until both sides are on the same page. The example prompt used
      is concrete enough to be useful and abstract enough to give Claude room: ''Hey
      Claude, I''m tired of waiting for GTA 6 — research mechanics, character design,
      visual design, location, and create a thin slice of GTA 6 inside this game world.'''
  - heading: Current limits and where this is going
    time: 1063
    body: 'The honest closing is balanced. Build time was long for the agent, but
      the MCP server is new. Epic will refine it. The current limitation is synchronous
      editing — only one change to the scene at a time. The ideal is a team of agents
      each handling a separate change in parallel, and that isn''t here yet.


      On indie devs: Leon enjoys indie games and is consistently impressed by what
      solo developers ship. He doesn''t think these tools replace those developers.
      They make their lives easier — hand the trivial work to the agent, focus your
      time on the higher-leverage parts of the game. That''s the future he''s watching
      for.'
  editorial: A game-development novice assembling a GTA 6-style scene in two hours
    with Unreal Engine 5.8 and Claude Code shows the barrier of engine mastery beginning
    to fall. The turning point is the MCP server on the Unreal side letting AI operate
    the editor directly. What matters is planning mode — discussing mechanics and
    design before implementation, where design dialogue, not one-shot generation,
    drives the result. The creator's conclusion — not replacement, but handing off
    chores to focus on high-ticket work — is the most realistic read on AI-assisted
    development.
  headerImage: /images/v-6KM2ysQYo/header.png
  heroImage: /images/v-6KM2ysQYo/header.png
---

## ハイライト

- [00:00] 投稿者はゲーム開発経験ゼロ、Unreal Engineも触ったことなし。Claude CodeにGTA 6風ゲームをリクエストしたところ、2時間でNPC群、車両、Lucia/Jasonキャラ、射撃機能を備えたシーンが完成。
- [00:33] 本人は『ゲームデザイナーでも開発者でもないが、こんなものを2時間でvibe codingで作れるのは衝撃』とコメント。インディーシーンと創作層への影響を予感。
- [00:48] セットアップは2点だけ。Unreal Engine 5.8 (最低5.8必須、launcher経由でDL) と、Claude Codeなどのcoding agent。MCPサーバーがUnreal側に登場したのが転機。
- [07:48] 実演ではキューブ追加の指示でClaudeがシーンに直接介入できることを確認。playボタンでシーン内にキューブが出現する基本動作が成立。
- [08:25] コツは planning mode の活用。プランニングモードではClaudeはシーンを変更せず、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを議論してから実装に入れる。
- [08:45] 実プロンプト例: 『GTA 6を待ちきれないので、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを調査して、このゲームワールドでGTA 6のthin sliceを作って』。
- [17:46] 現状の課題はMCPサーバーがまだ新しく、シーン編集が同期的なこと。同時に1つの編集しかできないため、複数エージェントの並列作業はまだ難しい。
- [18:30] 投稿者の結論: これらのツールはインディー開発者を置き換えるのでなく、雑用をAIに渡してハイチケット作業に集中できるようにする方向に向かう。

## セクション

### ゲーム未経験者がClaude CodeでGTA 6風を組んだ衝撃

- 時刻: 00:00

Leon van Zylの動画オープニングは衝撃的だ。『私はゲームを作ったことがないし、Unreal Engineについても何も知らない』。それなのにClaude CodeにGTA 6風のゲームを作るよう頼んだら、約2時間でNPCで埋まったワールド、走行する車両、Lucia / Jasonキャラ、射撃機能を持つプレイ可能シーンができた、と本人もまだ実感がついていない様子で語る。

投稿者は『ゲームデザイナーでも開発者でもない素人がvibe codingでこのレベルを2時間で組めるのは、率直に言って衝撃』だと述べる。これがインディーゲームシーンや創作層に与える影響は大きく、技術が個々のクリエイターを底上げする方向に向かう、というのが導入のテーゼだ。

### セットアップとプランニングモード — Unreal Engine 5.8 + Claude Code

- 時刻: 00:48

セットアップは2点だけだ。Unreal Engineを公式launcherからインストールし (最低5.8必須)、Claude Codeなどのコーディングエージェントを用意する。MCPサーバーがUnreal側に登場したことで、外部エージェントがシーンに直接介入できる構図が成立した。チュートリアル前半では小さなキューブを追加させる実演で、Claudeが本当にシーンと対話していることを確認し、playボタンを押すとキューブが出現する基本動作を見せる。

実用上の重要なテクニックがplanning modeの活用だ。プランニングモードではClaudeはシーンに変更を加えない。代わりにゲームメカニクス・キャラデザ・ビジュアルデザイン・ロケーションといった設計事項を会話で詰められる。実際のプロンプト例は『GTA 6を待ちきれないので、ゲームメカニクス・キャラデザ・ビジュアル・ロケーションを調査して、このゲームワールドでGTA 6のthin sliceを作って』だ。具体性と抽象性のバランスがうまく取れている。

### 現状の限界と将来 — 同期実行と複数エージェント並列の課題

- 時刻: 17:43

投稿者の総括は冷静だ。エージェントの完了に時間がかかった理由は、MCPサーバーがまだ新しいから。今後Epicが洗練させて、複数エージェントが同じシーンを同時編集できる経路を作る可能性が高い。現状は同期的で、一度に1編集しかできないため『エージェントチームを編成して各エージェントが別の変更を担当』という理想像にはまだ届いていない。

産業構造の見立てはバランスが良い。インディーゲームが大好きで、ソロ開発者の生産物には常々感心している投稿者は、これらのツールがインディー開発者を置き換えるとは思っていない。むしろ、雑用 (trivial tasks) をコーディングエージェントに渡して、本人が高付加価値タスクに集中できるようにする方向に向かう。次の技術展開を楽しみにしている、と締めくくる。

## 編集部の視点

ゲーム未経験者がUnreal Engine 5.8とClaude CodeでGTA 6風を2時間で組んだ事実は、エンジン習熟という参入障壁が崩れ始めたことを示す。転機はUnreal側にMCPサーバーが載ったことで、AIがエディタを直接操作できる点にある。重要なのはplanning mode——実装前にメカニクスや設計を議論させる使い方で、一発生成より設計対話が成果を左右する。投稿者の『置き換えではなく雑用を渡してハイチケット作業に集中』という結論は、AI開発支援の最も現実的な見立てだ。
