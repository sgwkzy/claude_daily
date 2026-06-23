---
videoId: QGaqvRLpx3U
title: 【AIエージェント】Claude CodeとUnity MCPでアニメ調のオープンワールドは作れるのか？
slug: claude-code-unity-mcpでアニメ調オープンワールドは作れるか-65分実検証-qgaqvrlpx3u
articleTitle: Claude Code × Unity MCPでアニメ調オープンワールドは作れるか — 65分実検証
seoTitle: Claude Code × Unity MCPでアニメ調オープンワールドは作れるか — 65分実検証
summary: Claude CodeとUnity MCPを組み合わせ、アニメ調オープンワールドの背景制作に挑戦。AIに判断を任せてアニメ調に寄せる難易度は高く、破綻なく実装できたのはClaude
  Code+MCPなしでは不可能だったと制作者は語る。
channel: 素人がCGアニメーション始めてみた
channelId: UCrvFX1u6DFCWCRr5mwtgD9A
publishedAt: '2026-06-20T09:30:25Z'
fetchedAt: '2026-06-23T02:47:55.918141Z'
originalThumbnail: https://i.ytimg.com/vi/QGaqvRLpx3U/maxresdefault.jpg
headerImage: /images/QGaqvRLpx3U/header.ja.png
heroImage: /images/QGaqvRLpx3U/header.ja.png
viewCount: 13725
durationSec: 3884
sourceLanguage: ja
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- Claude Code × Unity MCP
- アニメ調オープンワールド
- 参考画像から色合わせ自動化
- 地形ツール生成
- AIエージェント実用線
- バグ追跡力の強さ
bulletPoints:
- time: 0
  text: Claude CodeとUnity MCPを組み合わせ、アニメ調オープンワールドの背景制作に挑戦。AIに判断を任せてアニメ調に寄せる難易度は高く、破綻なく実装できたのはClaude
    Code+MCPなしでは不可能だったと制作者は語る。
- time: 35
  text: 前回動画のコメントで『Claude Codeで自動化できる』『Unity MCPでAIがUnityを直接操作できる』と教えられて検証開始。MCPを繋ぐと『お願いするだけでオブジェクト配置や調整』が成立する。
- time: 78
  text: 前回はGemini / GPT / Claudeの3AIから『今エージェントを使うのはお勧めしない、何も分からなくなる』とアドバイスを受けて見送り。今回はUnityの基礎を理解した上で本格運用。
- time: 1873
  text: ガラスマネージャーに参考画像を渡して『色を合わせて』と頼むと、Claude Codeがツールを使って自動的に色合わせを実行。狙っていない振る舞いだったが極めて有用だと判明。
- time: 1941
  text: 道だけを自動でへこませるツールも生成。自分でブラシで凹凸をつけた背景の上から使うとブラシ加工が消える問題も、Claude Codeに依頼すると配慮した修正版を返してきた。
- time: 3749
  text: '実用結論: AIに任せない方が早い局面も多い。Claude Code+MCPは時間がかかるため、ツール化して自分でサクサクできるところは自分でやり、大規模作業や反復作業をClaudeに任せるのが現実解。'
- time: 3779
  text: Claude Codeの真価はバグ追跡力。Unity内部に直接入り、原因を実験的に切り分けて特定する能力が極めて強い。複雑なシステム構築と反復作業、そしてデバッグでこそ価値が出る。
- time: 3820
  text: 最終評価は『だいぶ作れた』。アニメの雰囲気は前作ステージより明らかに良くなった。ただしフィールド作成ツール自体の制作には膨大な時間が掛かっており、同じツールはAsset
    Storeで数千円販売予定。
sections:
- heading: Unity MCPで広がる『お願いベース』のゲーム開発
  time: 35
  body: '前回動画のコメント欄で『Claude Codeを使うと自動化が進む』『Unity MCPを使うとAIがUnityを直接動かしてくれる』と教えられたのが出発点。調べてみると、MCPを繋ぐとUnityを直接触らなくてもオブジェクト配置や調整をAIに頼めるという、まさに次世代のワークフローが見えてきた。


    前回のアクションRPG制作時、エージェント運用の是非をGemini / GPT / Claudeの3AIに聞いたところ、いずれも『今の段階でエージェントを使うのはお勧めしない、何も分からなくなる』という見解で見送った。今回はUnityの基礎理解が進んだことを前提に、Claude
    Code + Unity MCPでアニメ調オープンワールドの背景制作という具体目標で本格運用に挑む。'
  image: null
- heading: 予想外のシナジー — 参考画像 → ガラスマネージャー → 色合わせ自動化
  time: 1873
  body: '意外な発見もあった。ガラスマネージャーに参考画像を渡して『色を合わせて』と依頼すると、Claude Codeがツールを使って自動で色を合わせてくれる。狙って組んだフローではなく、たまたま噛み合った組み合わせだ。明るすぎる色味になっても『もう少し落ち着かせて』と指示すると即座に修正。彩度が少し落ちつつもアニメ調の良い色味に着地した。


    地形ツールでも工夫が見えた。道だけを自動でへこませるツールを作ったが、自分でブラシで凹凸をつけた背景の上で使うとブラシ加工が消えてしまう問題が発生。Claude
    Codeに『そこも配慮して』と依頼したら、その点を尊重した修正版を返してきた。AIが既存の手作業を破壊しない振る舞いに収まる、というのは実プロダクションでは大きな安心材料になる。'
  image: null
- heading: 実用線の引き方 — 時間がかかる場面とClaude Codeが真価を発揮する場面
  time: 3749
  body: '実用結論は明確だ。Claude Code+MCPは万能ではなく、時間がかかる場面も多い。AIを介さない方が早い局面は普通にある。だから現実的には、ツール化して自分でサクサクできるところは自分で進め、大規模作業や反復作業をClaudeに任せるという役割分担になる。一体キャラを実装したら『これに倣って他のキャラもやっといて』と頼めるのが反復作業での強さだ。


    Claude Codeの真価はバグ追跡力にある。Unity内部に直接入り、原因を実験的に切り分けて特定する能力が極めて強い。複雑なシステム構築・反復作業・デバッグ、この3点こそClaude
    Codeを使うべき領域だと制作者は結論する。最終的なアニメ調オープンワールドは前作より明確に雰囲気が良くなり、『だいぶ作れた』という評価。ただしフィールド作成ツール自体の制作には膨大な時間がかかったため、同じものをAsset
    Storeで数千円販売予定。『買った方が安い』という率直な総括で締めくくる。'
  image: null
en:
  articleTitle: Can Claude Code × Unity MCP Build an Anime-Style Open World? A 65-Minute
    Field Test
  seoTitle: Can Claude Code × Unity MCP Build an Anime-Style Open World? A 6
  summary: A creator pairs Claude Code with Unity MCP and attempts to build an anime-style
    open-world background. The creator…
  keyPhrases:
  - Claude Code × Unity MCP
  - anime-style open world
  - reference image colour matching
  - auto-generated terrain tool
  - AI agent practical limits
  - Claude Code bug tracing
  bulletPoints:
  - time: 0
    text: A creator pairs Claude Code with Unity MCP and attempts to build an anime-style
      open-world background. The creator says nudging an AI toward anime-style art
      is genuinely hard — landing it without breakage wouldn't have been possible
      without Claude Code + MCP.
  - time: 35
    text: 'The trigger was a comment on the previous video: ''Claude Code automates
      more, and Unity MCP lets the AI drive Unity directly.'' With MCP wired in, ''just
      ask and Claude places and adjusts objects in Unity for you.'''
  - time: 78
    text: On the previous video the creator asked Gemini, GPT, and Claude whether
      to use agents; all three said 'don't, you'll lose track of what's happening'
      — so it was skipped. This time, with more Unity fluency, the creator commits
      to full agent operation.
  - time: 1873
    text: 'Surprise win: hand a reference image to the Grass Manager and ask ''match
      the colours,'' and Claude Code uses the tool to do the colour-matching automatically.
      Not designed for it, but it just works.'
  - time: 1941
    text: An auto-depress-the-road tool was generated too. On a terrain with hand-brushed
      bumps, naïve application would flatten the brushwork — but Claude Code respected
      those and produced a version that preserved them.
  - time: 3749
    text: 'Practical conclusion: not everything is faster with AI. Claude Code + MCP
      is slow for small things. The realistic split is: do the easy stuff yourself
      (use it as a tool), and hand big or repetitive work to Claude.'
  - time: 3779
    text: Claude Code's real superpower is bug tracing. It can step into Unity, run
      experiments, isolate root causes, and fix them. Complex systems, repetitive
      work, and debugging — that's where it pays off.
  - time: 3820
    text: 'Final assessment: ''we got most of the way there.'' The anime feel is clearly
      better than the previous stage. The field-building tool itself took enormous
      time, so the creator plans to sell it on the Asset Store for a few thousand
      yen — ''cheaper than rebuilding it yourself, even with Claude.'''
  sections:
  - heading: Unity MCP opens 'just ask' game development
    time: 35
    body: 'The starting point was a comment on the previous video: ''Claude Code automates
      more, and Unity MCP lets the AI drive Unity directly.'' Wire MCP in, and you
      can ask the AI to place objects and adjust the scene without touching Unity
      yourself.


      Last time, the creator asked Gemini, GPT, and Claude whether to use agents at
      that stage and all three said ''don''t — you''ll lose track of what''s happening,''
      so it was skipped. This time, with a stronger working knowledge of Unity, the
      creator commits to running Claude Code + Unity MCP at full strength, targeting
      an anime-style open-world background as the concrete goal.'
    image: null
  - heading: Unexpected synergies — reference image → Grass Manager → auto colour
      match
    time: 1873
    body: 'Some wins were not designed in. Hand a reference image to the Grass Manager
      and say ''match the colours,'' and Claude Code uses the tool to do the colour
      matching on its own. When the result felt too bright, asking for ''something
      more subdued'' produced an instant correction. The final palette landed with
      slightly lower saturation but a satisfying anime feel.


      Terrain tooling showed the same pattern. An auto-depress-the-road tool was generated;
      on terrain where the creator had hand-brushed bumps and dips, naïve application
      would have flattened the brushwork. After being told ''please respect those,''
      Claude Code returned a version that explicitly preserved the brush-made bumps.
      AI behavior that doesn''t trample your manual work matters a lot for real production.'
    image: null
  - heading: Where to use Claude Code and where to stop
    time: 3749
    body: 'The practical conclusion is honest. Not everything benefits from AI. Claude
      Code + MCP is slow for small interactions — sometimes skipping the AI is faster.
      The realistic split is to do the easy or fast bits yourself (treat it as a tool),
      and hand the big work or repetitive work to Claude. Implement one enemy and
      then say ''do the rest of the cast the same way'' — that''s where the agent
      really earns its keep.


      The biggest superpower is bug tracing. Claude Code can step inside Unity, run
      isolation experiments, and pin down root causes with a depth that''s hard to
      match manually. Complex systems, repetition, and debugging — those three are
      where Claude Code is genuinely strong. The final anime open-world background
      looked clearly better than the previous stage. The field-building tool itself
      took serious work to build, so the creator is shipping it on the Asset Store
      at a few thousand yen — ''cheaper than building it yourself again, even with
      Claude helping.'''
    image: null
  headerImage: /images/QGaqvRLpx3U/header.png
  heroImage: /images/QGaqvRLpx3U/header.png
---

## ハイライト

- [00:00] Claude CodeとUnity MCPを組み合わせ、アニメ調オープンワールドの背景制作に挑戦。AIに判断を任せてアニメ調に寄せる難易度は高く、破綻なく実装できたのはClaude Code+MCPなしでは不可能だったと制作者は語る。
- [00:35] 前回動画のコメントで『Claude Codeで自動化できる』『Unity MCPでAIがUnityを直接操作できる』と教えられて検証開始。MCPを繋ぐと『お願いするだけでオブジェクト配置や調整』が成立する。
- [01:18] 前回はGemini / GPT / Claudeの3AIから『今エージェントを使うのはお勧めしない、何も分からなくなる』とアドバイスを受けて見送り。今回はUnityの基礎を理解した上で本格運用。
- [31:13] ガラスマネージャーに参考画像を渡して『色を合わせて』と頼むと、Claude Codeがツールを使って自動的に色合わせを実行。狙っていない振る舞いだったが極めて有用だと判明。
- [32:21] 道だけを自動でへこませるツールも生成。自分でブラシで凹凸をつけた背景の上から使うとブラシ加工が消える問題も、Claude Codeに依頼すると配慮した修正版を返してきた。
- [62:29] 実用結論: AIに任せない方が早い局面も多い。Claude Code+MCPは時間がかかるため、ツール化して自分でサクサクできるところは自分でやり、大規模作業や反復作業をClaudeに任せるのが現実解。
- [62:59] Claude Codeの真価はバグ追跡力。Unity内部に直接入り、原因を実験的に切り分けて特定する能力が極めて強い。複雑なシステム構築と反復作業、そしてデバッグでこそ価値が出る。
- [63:40] 最終評価は『だいぶ作れた』。アニメの雰囲気は前作ステージより明らかに良くなった。ただしフィールド作成ツール自体の制作には膨大な時間が掛かっており、同じツールはAsset Storeで数千円販売予定。

## セクション

### Unity MCPで広がる『お願いベース』のゲーム開発

- 時刻: 00:35

前回動画のコメント欄で『Claude Codeを使うと自動化が進む』『Unity MCPを使うとAIがUnityを直接動かしてくれる』と教えられたのが出発点。調べてみると、MCPを繋ぐとUnityを直接触らなくてもオブジェクト配置や調整をAIに頼めるという、まさに次世代のワークフローが見えてきた。

前回のアクションRPG制作時、エージェント運用の是非をGemini / GPT / Claudeの3AIに聞いたところ、いずれも『今の段階でエージェントを使うのはお勧めしない、何も分からなくなる』という見解で見送った。今回はUnityの基礎理解が進んだことを前提に、Claude Code + Unity MCPでアニメ調オープンワールドの背景制作という具体目標で本格運用に挑む。

### 予想外のシナジー — 参考画像 → ガラスマネージャー → 色合わせ自動化

- 時刻: 31:13

意外な発見もあった。ガラスマネージャーに参考画像を渡して『色を合わせて』と依頼すると、Claude Codeがツールを使って自動で色を合わせてくれる。狙って組んだフローではなく、たまたま噛み合った組み合わせだ。明るすぎる色味になっても『もう少し落ち着かせて』と指示すると即座に修正。彩度が少し落ちつつもアニメ調の良い色味に着地した。

地形ツールでも工夫が見えた。道だけを自動でへこませるツールを作ったが、自分でブラシで凹凸をつけた背景の上で使うとブラシ加工が消えてしまう問題が発生。Claude Codeに『そこも配慮して』と依頼したら、その点を尊重した修正版を返してきた。AIが既存の手作業を破壊しない振る舞いに収まる、というのは実プロダクションでは大きな安心材料になる。

### 実用線の引き方 — 時間がかかる場面とClaude Codeが真価を発揮する場面

- 時刻: 62:29

実用結論は明確だ。Claude Code+MCPは万能ではなく、時間がかかる場面も多い。AIを介さない方が早い局面は普通にある。だから現実的には、ツール化して自分でサクサクできるところは自分で進め、大規模作業や反復作業をClaudeに任せるという役割分担になる。一体キャラを実装したら『これに倣って他のキャラもやっといて』と頼めるのが反復作業での強さだ。

Claude Codeの真価はバグ追跡力にある。Unity内部に直接入り、原因を実験的に切り分けて特定する能力が極めて強い。複雑なシステム構築・反復作業・デバッグ、この3点こそClaude Codeを使うべき領域だと制作者は結論する。最終的なアニメ調オープンワールドは前作より明確に雰囲気が良くなり、『だいぶ作れた』という評価。ただしフィールド作成ツール自体の制作には膨大な時間がかかったため、同じものをAsset Storeで数千円販売予定。『買った方が安い』という率直な総括で締めくくる。
