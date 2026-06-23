---
videoId: OiFtnBj1P9o
title: I Tested Claude Inside Unreal Engine 5.8...
slug: claude-code-unreal-engine-58-mcp-blueprint5チャレンジ実検証-oiftnbj1p9o
articleTitle: Claude Code × Unreal Engine 5.8 MCP — Blueprint5チャレンジ実検証
seoTitle: Claude Code × Unreal Engine 5.8 MCP — Blueprint5チャレンジ実検証
summary: Unreal Engine 5.8の新AI MCPプラグインにClaude Codeを接続し、Blueprintアシスト能力を5つのチャレンジで検証…
channel: Smart Poly
channelId: UCp1e34nrTQqVXkNU5ekH9CQ
publishedAt: '2026-06-20T15:30:19Z'
fetchedAt: '2026-06-23T02:47:55.918141Z'
originalThumbnail: https://i.ytimg.com/vi/OiFtnBj1P9o/maxresdefault.jpg
headerImage: /images/OiFtnBj1P9o/header.ja.png
heroImage: /images/OiFtnBj1P9o/header.ja.png
viewCount: 54018
durationSec: 1342
sourceLanguage: en
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Unreal Engine 5.8 MCP
- Claude Code Blueprint支援
- Blueprintチャレンジ5本
- Print Stringの配線ミス
- ラグドール自動生成
- ゲーム開発AI実用度
bulletPoints:
- time: 0
  text: Unreal Engine 5.8の新AI MCPプラグインにClaude Codeを接続し、Blueprintアシスト能力を5つのチャレンジで検証。動作するゲームプレイ系を作れるか、Blueprintノードを正しく繋げるか、指示に従えるか、を測る。
- time: 17
  text: 'テスト項目: 動作するゲームプレイシステム生成、Blueprintノード接続、指示遵守、そして最も重要な『開発者の時間を本当に節約できるか』。Smart
    Polyによる実地評価。'
- time: 578
  text: ヘルス管理ロジックの実検証では、計算ロジック自体は正確だったが、subtract health / add health のPrint Stringに誤ったSelectノードを繋ぐ細かな配線ミスが発生。手で1箇所つなぎ直すだけで完全に動作。
- time: 624
  text: ダメージボックスは75→50→25→0、ヘルスボックスは25→50→75→100と正しく加減算される。数式は正しく組まれており、Print Stringの配線だけが唯一の修正点だった。
- time: 1255
  text: ラグドール処理も実装。Set Timer by Functionで一定時間後にRecover from Ragdollを呼び、物理シミュレーションを停止、位置とローテーションをリセット、コリジョン再有効化までを自動生成。
- time: 1278
  text: '5チャレンジの最終評価: Hit Actor 8〜9/10、Soccer Ball 4/10、Hat 8〜9/10、Door 6〜7/10、ダメージボックス
    6〜7/10。全体として『かなりまとも』だが、プロンプト精度と既存Blueprint知識が成果を左右する。'
- time: 1315
  text: '結論: Blueprintの基礎知識があれば、Claudeの細かな配線ミスを手で修正できるため、クレジット節約と速度のバランスが取れる。MCP経由のClaude
    Codeはゲーム開発支援として十分実用域に入った。'
sections:
- heading: Unreal Engine 5.8 × Claude Code MCPの実検証フレーム
  time: 0
  body: 'Unreal Engine 5.8で公開された新AI MCPプラグインを使い、Claude CodeをUnrealプロジェクトに接続。Smart
    Polyが5つのBlueprintチャレンジで実力を測った。観点は明確で、（1）動作するゲームプレイシステムを組めるか、（2）Blueprintノードを正しく接続できるか、（3）指示通り動けるか、そして（4）開発者の時間を本当に節約できるかという核心。


    MCP接続によりClaude Codeがプロジェクトのファイル構造とBlueprintアセットにアクセスでき、テストはまさに『AIにエンジニアを任せる』スタイルで進む。著者のSmart
    PolyはUnreal Engineチュートリアル分野で実績のある制作者で、評価は実装結果に対するシビアな目線で行われた。'
  image: null
- heading: ヘルス処理とラグドール — 数式は完璧、配線は1箇所惜しい
  time: 578
  body: 'ヘルス管理ロジックでは、計算自体は完璧だった。健康値から減算してゼロでClampするか、加算で上限で抑えるかという基本ロジックは正しく構築されていた。問題はPrint
    Stringの配線で、Selectノードの純粋関数特性に依存した間違いをClaudeがしていたため、表示される数値だけが実際の値と合わなかった。配線を1本繋ぎ直しただけで完全動作し、ダメージボックスは75→50→25→0、ヘルスボックスは25→50→75→100と正しく動いた。


    ラグドール処理はより複雑だが、Set Timer by Functionで遅延を作り、Recover from Ragdoll関数で物理シミュレーション停止・位置とローテーションのリセット・コリジョン再有効化・ragdoll変数をfalseに戻すという一連を、自動でうまく組んできた。Blueprintの細かなアーキテクチャ感覚がClaude側にちゃんと宿っているのが分かる例だ。'
  image: null
- heading: 5チャレンジ評価とClaude Code MCPの実用度
  time: 1278
  body: '5チャレンジの最終評価は次の通り。Hit Actor 8〜9/10、Soccer Ball 4/10、Hat 8〜9/10、Door 6〜7/10、ダメージボックス
    6〜7/10。Soccer Ballがやや低めだが、全体として『かなりまともな仕事』という評価だ。


    著者は重要な実用観点も指摘する。プロンプト精度が成果を左右する以上、より具体的に指示するほど結果は良くなる。そしてBlueprintの基礎知識があれば、Claudeの細かな配線ミスを手で修正できるため、AIへの再プロンプトでクレジットを消費する代わりに自分で直すという選択肢も取れる。Claude
    Code × Unreal Engine MCPの組み合わせは、ゲーム開発支援として『実用域に入った』と結論づけられる。'
  image: null
en:
  articleTitle: Claude Code × Unreal Engine 5.8 MCP — A Real Test on 5 Blueprint Challenges
  seoTitle: Claude Code × Unreal Engine 5.8 MCP — A Real Test on 5 Blueprint
  summary: Claude Code is hooked into Unreal Engine 5.8's new AI MCP plugin and put
    through five Blueprint challenges. Can it…
  keyPhrases:
  - Unreal Engine 5.8 MCP
  - Claude Code Blueprint support
  - 5 Blueprint challenges
  - Print String wiring slip
  - auto-generated ragdoll
  - game-dev AI practicality
  bulletPoints:
  - time: 0
    text: Claude Code is hooked into Unreal Engine 5.8's new AI MCP plugin and put
      through five Blueprint challenges. Can it produce working gameplay systems,
      wire Blueprint nodes correctly, follow instructions, and ultimately save developer
      time?
  - time: 17
    text: 'The test set: build working gameplay systems, connect Blueprint nodes correctly,
      follow instructions, and most importantly save real developer time. The grader
      is Smart Poly, a serious Unreal Engine creator.'
  - time: 578
    text: On the health system test, the math was correct but a single wiring mistake
      hooked the Select node into the Print String for subtract/add health. One reconnect
      later, everything ran clean.
  - time: 624
    text: Damage box decremented 75 → 50 → 25 → 0, health box incremented 25 → 50
      → 75 → 100 — exactly as expected. The math was right; only the Print String
      wiring needed a fix.
  - time: 1255
    text: The ragdoll system also came together. A Set Timer by Function delays then
      calls Recover from Ragdoll — physics off, location and rotation reset, collision
      re-enabled, ragdoll flag back to false. All auto-generated.
  - time: 1278
    text: 'Final scores across the five challenges: Hit Actor 8–9/10, Soccer Ball
      4/10, Hat 8–9/10, Door 6–7/10, Damage Boxes 6–7/10. Overall: a pretty decent
      job, with prompt precision driving outcome quality.'
  - time: 1315
    text: 'Verdict: if you have basic Blueprint knowledge, you can fix Claude''s small
      wiring slips yourself, saving credits and time. Claude Code via Unreal MCP is
      firmly in the ''practical for real work'' zone now.'
  sections:
  - heading: The test setup — Claude Code wired into Unreal 5.8 via MCP
    time: 0
    body: 'Smart Poly hooks Claude Code into an Unreal Engine 5.8 project via the
      new AI MCP plugin and runs it through five Blueprint challenges. The questions
      are pointed: can it build working gameplay systems, connect Blueprint nodes
      properly, follow instructions, and — most importantly — save real developer
      time?


      MCP gives Claude Code access to the project''s file structure and Blueprint
      assets, so the test really is ''hand the engineering to the AI.'' Smart Poly
      is a credible grader with strong UE tutorial credentials, so the assessment
      isn''t soft — it''s a real-result review.'
    image: null
  - heading: Health system and ragdoll — perfect math, almost-perfect wiring
    time: 578
    body: 'On the health system test, the underlying math came out perfect — clamp
      at zero on subtract, cap at the max on add. The single issue was a misuse of
      a Select node: it got wired into the Print String for subtract/add health, so
      the displayed number disagreed with the actual value because Select is a pure
      function and was being called every time. One reconnect later, everything matched:
      damage box 75 → 50 → 25 → 0, health box 25 → 50 → 75 → 100.


      The ragdoll system was more architectural, but Claude built it cleanly. A Set
      Timer by Function fires after a delay and calls Recover from Ragdoll, which
      stops the physics simulation, resets the character''s location and rotation,
      re-enables collision, and flips the ragdoll boolean back to false. The Blueprint-architecture
      intuition was clearly there.'
    image: null
  - heading: Five-challenge scores and where Claude Code via MCP actually sits
    time: 1278
    body: 'The final scores across the five tests: Hit Actor 8–9/10, Soccer Ball 4/10,
      Hat 8–9/10, Door 6–7/10, Damage Boxes 6–7/10. Soccer Ball was the weak spot,
      but overall Smart Poly calls it ''a pretty decent job.''


      The practical takeaway is the important part. Prompt precision drives outcome
      quality — be specific and results improve. And if you have basic Blueprint knowledge,
      you can fix Claude''s small wiring mistakes by hand rather than burning more
      credits re-prompting. The combination of Claude Code and the Unreal MCP plugin
      has moved from ''interesting demo'' into the ''practical for real game work''
      zone.'
    image: null
  headerImage: /images/OiFtnBj1P9o/header.png
  heroImage: /images/OiFtnBj1P9o/header.png
---

## ハイライト

- [00:00] Unreal Engine 5.8の新AI MCPプラグインにClaude Codeを接続し、Blueprintアシスト能力を5つのチャレンジで検証。動作するゲームプレイ系を作れるか、Blueprintノードを正しく繋げるか、指示に従えるか、を測る。
- [00:17] テスト項目: 動作するゲームプレイシステム生成、Blueprintノード接続、指示遵守、そして最も重要な『開発者の時間を本当に節約できるか』。Smart Polyによる実地評価。
- [09:38] ヘルス管理ロジックの実検証では、計算ロジック自体は正確だったが、subtract health / add health のPrint Stringに誤ったSelectノードを繋ぐ細かな配線ミスが発生。手で1箇所つなぎ直すだけで完全に動作。
- [10:24] ダメージボックスは75→50→25→0、ヘルスボックスは25→50→75→100と正しく加減算される。数式は正しく組まれており、Print Stringの配線だけが唯一の修正点だった。
- [20:55] ラグドール処理も実装。Set Timer by Functionで一定時間後にRecover from Ragdollを呼び、物理シミュレーションを停止、位置とローテーションをリセット、コリジョン再有効化までを自動生成。
- [21:18] 5チャレンジの最終評価: Hit Actor 8〜9/10、Soccer Ball 4/10、Hat 8〜9/10、Door 6〜7/10、ダメージボックス 6〜7/10。全体として『かなりまとも』だが、プロンプト精度と既存Blueprint知識が成果を左右する。
- [21:55] 結論: Blueprintの基礎知識があれば、Claudeの細かな配線ミスを手で修正できるため、クレジット節約と速度のバランスが取れる。MCP経由のClaude Codeはゲーム開発支援として十分実用域に入った。

## セクション

### Unreal Engine 5.8 × Claude Code MCPの実検証フレーム

- 時刻: 00:00

Unreal Engine 5.8で公開された新AI MCPプラグインを使い、Claude CodeをUnrealプロジェクトに接続。Smart Polyが5つのBlueprintチャレンジで実力を測った。観点は明確で、（1）動作するゲームプレイシステムを組めるか、（2）Blueprintノードを正しく接続できるか、（3）指示通り動けるか、そして（4）開発者の時間を本当に節約できるかという核心。

MCP接続によりClaude Codeがプロジェクトのファイル構造とBlueprintアセットにアクセスでき、テストはまさに『AIにエンジニアを任せる』スタイルで進む。著者のSmart PolyはUnreal Engineチュートリアル分野で実績のある制作者で、評価は実装結果に対するシビアな目線で行われた。

### ヘルス処理とラグドール — 数式は完璧、配線は1箇所惜しい

- 時刻: 09:38

ヘルス管理ロジックでは、計算自体は完璧だった。健康値から減算してゼロでClampするか、加算で上限で抑えるかという基本ロジックは正しく構築されていた。問題はPrint Stringの配線で、Selectノードの純粋関数特性に依存した間違いをClaudeがしていたため、表示される数値だけが実際の値と合わなかった。配線を1本繋ぎ直しただけで完全動作し、ダメージボックスは75→50→25→0、ヘルスボックスは25→50→75→100と正しく動いた。

ラグドール処理はより複雑だが、Set Timer by Functionで遅延を作り、Recover from Ragdoll関数で物理シミュレーション停止・位置とローテーションのリセット・コリジョン再有効化・ragdoll変数をfalseに戻すという一連を、自動でうまく組んできた。Blueprintの細かなアーキテクチャ感覚がClaude側にちゃんと宿っているのが分かる例だ。

### 5チャレンジ評価とClaude Code MCPの実用度

- 時刻: 21:18

5チャレンジの最終評価は次の通り。Hit Actor 8〜9/10、Soccer Ball 4/10、Hat 8〜9/10、Door 6〜7/10、ダメージボックス 6〜7/10。Soccer Ballがやや低めだが、全体として『かなりまともな仕事』という評価だ。

著者は重要な実用観点も指摘する。プロンプト精度が成果を左右する以上、より具体的に指示するほど結果は良くなる。そしてBlueprintの基礎知識があれば、Claudeの細かな配線ミスを手で修正できるため、AIへの再プロンプトでクレジットを消費する代わりに自分で直すという選択肢も取れる。Claude Code × Unreal Engine MCPの組み合わせは、ゲーム開発支援として『実用域に入った』と結論づけられる。
