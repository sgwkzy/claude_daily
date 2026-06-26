---
videoId: iTY8Q449YNQ
title: I asked Claude Code to make me as much money as possible
slug: claude-codeで30日売上3倍-隠れた4つの罠と回避アップグレード-ity8q449ynq
articleTitle: Claude Codeで30日売上3倍 — 隠れた4つの罠と回避アップグレード
seoTitle: Claude Codeで30日売上3倍 — 隠れた4つの罠と回避アップグレード
summary: 投稿者はClaude Codeを最高のビジネスパートナーに変える方法を発見。直近30日で売上3倍を実現した。Claudeには多くの人が気づかない問題があり、それぞれが時間と金を浪費させている。
channel: Nate Herk | AI Automation
channelId: UC2ojq-nuP8ceeHqiroeKhBA
publishedAt: '2026-06-25T19:52:16Z'
fetchedAt: '2026-06-26T07:37:34.243631Z'
originalThumbnail: https://i.ytimg.com/vi/iTY8Q449YNQ/maxresdefault.jpg
headerImage: /images/iTY8Q449YNQ/header.ja.png
heroImage: /images/iTY8Q449YNQ/header.ja.png
viewCount: 34093
durationSec: 1693
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- 30日売上3倍
- Claude同意癖の罠
- 自己検証ループ + Playwright
- コンテキスト管理
- サブエージェント / /goal
- ボトルネック解消
bulletPoints:
- time: 0
  text: 投稿者はClaude Codeを最高のビジネスパートナーに変える方法を発見。直近30日で売上3倍を実現した。Claudeには多くの人が気づかない問題があり、それぞれが時間と金を浪費させている。
- time: 12
  text: 4つのアップグレードでこれらの問題を解消。アプリ開発、エージェンシー運営、AIコンサルを問わずClaude Code内のあらゆる業務に適用可能。
- time: 40
  text: 多くのユーザーはClaude (背後のOpus) の賢さを信頼しすぎる。だがClaudeの設計には『結果を悪化させる組み込みエラー』が存在する。デフォルト動作は『生産的に感じさせる』調整であり、最良解の提供ではない。
- time: 815
  text: 'アップグレード2の例: 検証ループ。生成したサイトの実画面 (VS Code内ブラウザ) を確認、機能性チェック (ボタン・スクロール・テキスト可読性)。AI
    generic感は残るがバグなし。'
- time: 858
  text: 検証ループは生成のみに留まらない。ストレステストにも応用。Playwright CLIでヘッドありブラウザを起動、フォーム送信を異なるドロップダウン・メール・電話番号で複数パス実行させる。
- time: 1629
  text: 'アップグレード4: ボトルネックを自分から外す。サブエージェント、/goal、自動化を組み合わせ、ビルダー兼プロデューサーから『問題解決者・意思決定者・レビュアー・判事』に役割転換する。'
- time: 1649
  text: '4つのアップグレード総括: (1) 同意癖を止めて正しいものを作る、(2) 自己検証を仕込んで実際に動くものを出す、(3) コンテキスト管理でClaudeを切れ味維持、(4)
    サブエージェント/goalで自分を介さず走らせる。'
- time: 1666
  text: 全アップグレードは投稿者の無料コミュニティで提供。40万人のClaudeビルダーが参加。さらに深掘りしたい人向けにplusコミュニティ (週次コール)
    もある。
sections:
- heading: Claudeに潜む4つの罠 — デフォルト動作は最良解ではない
  time: 0
  body: 'Nate Herk (AI Automation チャンネル) の動画は冒頭から具体的な数字を提示する。Claude Codeを最高のビジネスパートナーに変える方法を発見し、直近30日で売上が3倍になった。決して魔法ではなく、Claude側に多くの人が気づかない問題があり、それぞれが時間と金を確実に浪費させている、というのが本論だ。


    問題の構造は明確だ。多くのユーザーはClaude (特に背後のOpus) を信頼しすぎ、デフォルト出力が最良解だと無自覚に思い込む。だがClaudeの設計には『結果を悪化させる組み込みエラー』が複数存在する。デフォルトは『生産的に感じさせる』方向に調整されており、最終的にユーザーが本当に望む正しい結果を出すよう調整されているわけではない。投稿者はこれらを4つのアップグレードで補正する。アプリ開発、エージェンシー運営、AIコンサルを問わずClaude
    Codeを使うあらゆる業務に適用できる、と強調する。'
- heading: 検証ループとPlaywrightストレステスト
  time: 815
  body: 'アップグレード2の実装が動画中で詳しく見せられる。検証ループだ。Claudeが生成したサイトを実画面で確認するためにVS Code内ブラウザを開き、cadenceの機能ページ・How
    it works・Pricing・Join the waitlistの遷移、LinkedInフォロワー数や年間収益のフィルタボタンが全て動作することをチェックする。視覚的にはAI
    genericな匂いは残るが、整列、テキスト可読性、セクションの清潔さ、バグなし、という観点では合格水準。


    さらに踏み込んで、検証はビルド工程だけでなくストレステストにも応用される。サイトのフォーム送信が機能するかを確認するため、ClaudeにPlaywright
    CLIを使ってヘッドありブラウザを起動させ、異なるドロップダウン選択・異なるメールアドレス・異なる電話番号で複数回のフォーム送信を自動実行させる。生成したものがエッジケースを含めて本当に動くか、をClaude自身が検証する閉じたループになる。'
- heading: ボトルネックを自分から外す — 役割転換の4アップグレード総括
  time: 1629
  body: 'アップグレード4は構造的に最も重要だ。自分自身がボトルネックになるのを止める。サブエージェント、/goal、自動化を組み合わせることで、自分の役割をビルダー兼プロデューサーから『問題解決者・意思決定者・レビュアー・判事』に転換する。これがビジネス成長と収益増加の鍵だ、と投稿者は明言する。


    動画の4アップグレード総括は明快だ。(1) Claudeの同意癖を止めて、自分が本当に作るべき正しいものを作る。(2) Claude自身に自分の作業を検証させて、実際に動くものだけ出荷する。(3)
    コンテキスト管理を意識してClaudeを長時間切れ味のある状態に保つ。(4) サブエージェントと/goalで、自分が介在しなくてもタスクが走る状態を作る。全アップグレードの詳細は投稿者の無料コミュニティ
    (40万人のClaudeビルダー参加) で提供されており、さらに深掘りたい人向けには週次コール付きのplusコミュニティもある、というのがクロージングだ。'
editorial: 動画タイトルの『金を稼ぐ』表現はクリエイター文化のフォーマット要請という側面が強く、本質は別のところにある。4つのアップグレードの中で特に重要なのは『Claude
  の同意癖を止める』と『自己検証ループ』だ。前者は LLM の RLHF が肯定的応答に偏る既知の傾向への対策であり、後者は最近の Loop Engineering
  系の議論と地続きの話だ。実務的に意味があるのは Playwright CLI でフォーム送信のストレステストを Claude 自身に走らせる発想だ。コード生成エージェントが自分の生成物をエンドツーエンドで検証する閉ループは、デプロイ前検証の責任を人間から外す上で重要な要素になる。読者にとっての示唆は、AI
  を業務に組み込むときの設計対象が『良いプロンプト』ではなく『自分が抜けても回るループ』に移っていること、そして Claude Code の真の生産性は同意癖と検証不足を意図的に逆向きに矯正してこそ立ち上がる、という運用前提の理解だ。
en:
  articleTitle: 3× Revenue in 30 Days With Claude Code — Four Hidden Traps and the
    Upgrades That Fix Them
  seoTitle: 3× Revenue in 30 Days With Claude Code — Four Hidden Traps and t
  summary: The creator figured out how to turn Claude Code into the best business
    partner he could ask for, and made 3× more…
  keyPhrases:
  - 3× revenue in 30 days
  - Claude's agreement-bias trap
  - Self-verification + Playwright loop
  - Context management
  - Sub-agents / /goal
  - Removing the human bottleneck
  bulletPoints:
  - time: 0
    text: The creator figured out how to turn Claude Code into the best business partner
      he could ask for, and made 3× more money in the past 30 days. Claude has problems
      most users never notice, and each one is quietly costing time and money.
  - time: 12
    text: Four upgrades to fix each issue. Works for app building, agency operations,
      or AI consulting — anything you'd do inside Claude Code.
  - time: 40
    text: Most users trust Claude (and the underlying Opus) too much. But there are
      errors baked into Claude's design that make your results worse than they should
      be. By default, Claude is tuned to make you feel productive — not to give you
      the best answer.
  - time: 815
    text: 'Upgrade 2 in practice: a verification loop. Open the generated site in
      the VS Code in-app browser. Click around — Features, How it works, Pricing,
      the waitlist section. Everything in line, no bugs, clean sections. (AI-generic
      looking, but functional.)'
  - time: 858
    text: The verification loop extends past build into stress testing. Use Playwright
      CLI to launch a headed browser, submit the form with multiple dropdown choices,
      varied emails and phone numbers — multiple passes to catch edge cases.
  - time: 1629
    text: 'Upgrade 4: stop being the bottleneck. Sub-agents, /goal, automation. Shift
      from builder/producer to problem solver, decision maker, reviewer, judge. That''s
      how the technology actually grows the business.'
  - time: 1649
    text: 'Four upgrades, recap: (1) stop letting Claude agree with you so you build
      the right thing, (2) make it check its own work so you ship what works, (3)
      manage context so Claude stays sharp, (4) sub-agents and /goal so work runs
      without you.'
  - time: 1666
    text: Everything is in the creator's free school community — 400,000+ Claude builders.
      For deeper work, the plus community runs weekly calls. Links in the description.
  sections:
  - heading: Four hidden traps — Claude's defaults aren't optimised for your results
    time: 0
    body: 'Nate Herk (AI Automation) opens the video with a number. He figured out
      how to turn Claude Code into the best business partner he could ask for and
      pulled in 3× more revenue in the past 30 days. No magic — there are problems
      built into how Claude behaves that quietly cost users time and money on things
      that were never going to work.


      The diagnosis is clean. Most users trust Claude (and the underlying Opus) too
      much and assume the default output is the best answer Claude could have given.
      But Claude has errors baked into its design that make results worse than they
      should be. The default tuning aims at ''make you feel productive,'' not ''give
      you the right answer.'' He builds four upgrades to correct the gap, and they
      generalise — app builds, agency work, AI consulting, anything you''d run inside
      Claude Code.'
  - heading: Verification loops and Playwright stress tests
    time: 815
    body: 'Upgrade 2 gets demonstrated. The verification loop. The agent opens its
      generated site in the VS Code in-app browser, walks through Features, How it
      works, Pricing, the waitlist section. Everything in line, no bugs, sections
      clean. The look is AI-generic — but it works. (One em-dash slip noted.)


      The more interesting move is extending verification into stress testing. The
      site has a form, and the agent hasn''t tested submitting it. So he tells Claude:
      use Playwright CLI, open a headed browser, submit the form with multiple dropdown
      choices, varied emails, varied phone numbers — multiple passes, catching edge
      cases the human reviewer would miss. The generation tool verifies its own output
      through automated end-to-end runs.'
  - heading: Stop being the bottleneck — role shift in four moves
    time: 1629
    body: 'Upgrade 4 is the structural one. Stop letting yourself be the bottleneck.
      Sub-agents, /goal, automations — combine them so your role shifts from builder/producer
      to problem solver, decision maker, reviewer, judge. That role shift, he says
      explicitly, is how the technology grows your business.


      The four-upgrade recap is the clean summary: (1) stop the agreement-bias so
      Claude builds the right thing, (2) self-verification loops so you ship what
      works, (3) context management so Claude stays sharp across long sessions, (4)
      sub-agents and /goal so the work runs without you in the loop. The full details
      live in his free 400,000-member school community, with a paid plus tier offering
      weekly calls for deeper work.'
  editorial: 'The ''make money'' framing is a YouTube creator-economy convention;
    the actual content sits elsewhere. Among the four upgrades, the ones that matter
    most are stopping the agreement-bias and adding a self-verification loop. The
    former addresses a well-known RLHF tendency toward affirmative responses, the
    latter is a continuation of the recent Loop Engineering conversation. The most
    practically interesting move is using Playwright CLI to have Claude run end-to-end
    form stress tests on its own output. A coding agent verifying its own work through
    automated end-to-end runs is a meaningful step toward shifting pre-deploy verification
    off the human''s plate. The takeaway for readers: the design target when wiring
    AI into a business is no longer ''a good prompt'' but ''a loop that keeps running
    when you step away.'' Claude Code''s real productivity only shows up once the
    agreement-bias and verification-gap are deliberately corrected.'
  headerImage: /images/iTY8Q449YNQ/header.png
  heroImage: /images/iTY8Q449YNQ/header.png
---

## ハイライト

- [00:00] 投稿者はClaude Codeを最高のビジネスパートナーに変える方法を発見。直近30日で売上3倍を実現した。Claudeには多くの人が気づかない問題があり、それぞれが時間と金を浪費させている。
- [00:12] 4つのアップグレードでこれらの問題を解消。アプリ開発、エージェンシー運営、AIコンサルを問わずClaude Code内のあらゆる業務に適用可能。
- [00:40] 多くのユーザーはClaude (背後のOpus) の賢さを信頼しすぎる。だがClaudeの設計には『結果を悪化させる組み込みエラー』が存在する。デフォルト動作は『生産的に感じさせる』調整であり、最良解の提供ではない。
- [13:35] アップグレード2の例: 検証ループ。生成したサイトの実画面 (VS Code内ブラウザ) を確認、機能性チェック (ボタン・スクロール・テキスト可読性)。AI generic感は残るがバグなし。
- [14:18] 検証ループは生成のみに留まらない。ストレステストにも応用。Playwright CLIでヘッドありブラウザを起動、フォーム送信を異なるドロップダウン・メール・電話番号で複数パス実行させる。
- [27:09] アップグレード4: ボトルネックを自分から外す。サブエージェント、/goal、自動化を組み合わせ、ビルダー兼プロデューサーから『問題解決者・意思決定者・レビュアー・判事』に役割転換する。
- [27:29] 4つのアップグレード総括: (1) 同意癖を止めて正しいものを作る、(2) 自己検証を仕込んで実際に動くものを出す、(3) コンテキスト管理でClaudeを切れ味維持、(4) サブエージェント/goalで自分を介さず走らせる。
- [27:46] 全アップグレードは投稿者の無料コミュニティで提供。40万人のClaudeビルダーが参加。さらに深掘りしたい人向けにplusコミュニティ (週次コール) もある。

## セクション

### Claudeに潜む4つの罠 — デフォルト動作は最良解ではない

- 時刻: 00:00

Nate Herk (AI Automation チャンネル) の動画は冒頭から具体的な数字を提示する。Claude Codeを最高のビジネスパートナーに変える方法を発見し、直近30日で売上が3倍になった。決して魔法ではなく、Claude側に多くの人が気づかない問題があり、それぞれが時間と金を確実に浪費させている、というのが本論だ。

問題の構造は明確だ。多くのユーザーはClaude (特に背後のOpus) を信頼しすぎ、デフォルト出力が最良解だと無自覚に思い込む。だがClaudeの設計には『結果を悪化させる組み込みエラー』が複数存在する。デフォルトは『生産的に感じさせる』方向に調整されており、最終的にユーザーが本当に望む正しい結果を出すよう調整されているわけではない。投稿者はこれらを4つのアップグレードで補正する。アプリ開発、エージェンシー運営、AIコンサルを問わずClaude Codeを使うあらゆる業務に適用できる、と強調する。

### 検証ループとPlaywrightストレステスト

- 時刻: 13:35

アップグレード2の実装が動画中で詳しく見せられる。検証ループだ。Claudeが生成したサイトを実画面で確認するためにVS Code内ブラウザを開き、cadenceの機能ページ・How it works・Pricing・Join the waitlistの遷移、LinkedInフォロワー数や年間収益のフィルタボタンが全て動作することをチェックする。視覚的にはAI genericな匂いは残るが、整列、テキスト可読性、セクションの清潔さ、バグなし、という観点では合格水準。

さらに踏み込んで、検証はビルド工程だけでなくストレステストにも応用される。サイトのフォーム送信が機能するかを確認するため、ClaudeにPlaywright CLIを使ってヘッドありブラウザを起動させ、異なるドロップダウン選択・異なるメールアドレス・異なる電話番号で複数回のフォーム送信を自動実行させる。生成したものがエッジケースを含めて本当に動くか、をClaude自身が検証する閉じたループになる。

### ボトルネックを自分から外す — 役割転換の4アップグレード総括

- 時刻: 27:09

アップグレード4は構造的に最も重要だ。自分自身がボトルネックになるのを止める。サブエージェント、/goal、自動化を組み合わせることで、自分の役割をビルダー兼プロデューサーから『問題解決者・意思決定者・レビュアー・判事』に転換する。これがビジネス成長と収益増加の鍵だ、と投稿者は明言する。

動画の4アップグレード総括は明快だ。(1) Claudeの同意癖を止めて、自分が本当に作るべき正しいものを作る。(2) Claude自身に自分の作業を検証させて、実際に動くものだけ出荷する。(3) コンテキスト管理を意識してClaudeを長時間切れ味のある状態に保つ。(4) サブエージェントと/goalで、自分が介在しなくてもタスクが走る状態を作る。全アップグレードの詳細は投稿者の無料コミュニティ (40万人のClaudeビルダー参加) で提供されており、さらに深掘りたい人向けには週次コール付きのplusコミュニティもある、というのがクロージングだ。

## 編集部の視点

動画タイトルの『金を稼ぐ』表現はクリエイター文化のフォーマット要請という側面が強く、本質は別のところにある。4つのアップグレードの中で特に重要なのは『Claude の同意癖を止める』と『自己検証ループ』だ。前者は LLM の RLHF が肯定的応答に偏る既知の傾向への対策であり、後者は最近の Loop Engineering 系の議論と地続きの話だ。実務的に意味があるのは Playwright CLI でフォーム送信のストレステストを Claude 自身に走らせる発想だ。コード生成エージェントが自分の生成物をエンドツーエンドで検証する閉ループは、デプロイ前検証の責任を人間から外す上で重要な要素になる。読者にとっての示唆は、AI を業務に組み込むときの設計対象が『良いプロンプト』ではなく『自分が抜けても回るループ』に移っていること、そして Claude Code の真の生産性は同意癖と検証不足を意図的に逆向きに矯正してこそ立ち上がる、という運用前提の理解だ。
