---
videoId: hDsZMb_8FYo
title: Anthropic Just Replaced Claude Code With New Claude Tag
slug: anthropic新製品claude-tag-slackで動くチーム向け常駐aiとmatt-greenの暗号調査-hdszmb_8fyo
articleTitle: Anthropic新製品Claude Tag — Slackで動くチーム向け常駐AIと、Matt Greenの暗号調査
seoTitle: Anthropic新製品Claude Tag — Slackで動くチーム向け常駐AIと、Matt Greenの暗号調査
summary: Anthropicは大きな一週間を迎えた。Claude Code の進化形として Claude Tag を発表。個人開発者ではなくチーム単位で使う設計に再構築。
channel: AI Revolution
channelId: UC5l7RouTQ60oUjLjt1Nh-UQ
publishedAt: '2026-06-24T22:49:14Z'
fetchedAt: '2026-06-27T06:58:57.961686Z'
originalThumbnail: https://i.ytimg.com/vi/hDsZMb_8FYo/maxresdefault.jpg
headerImage: /images/hDsZMb_8FYo/header.ja.png
heroImage: /images/hDsZMb_8FYo/header.ja.png
viewCount: 37058
durationSec: 965
sourceLanguage: en
matchedKeywords:
- Claude Code
proposedByLLM: false
keyPhrases:
- Claude Tag (Slack統合チーム向けエージェント)
- Anthropic社内コード65%
- Karpathyの3回目LLM革命
- GitHub / Jira / Linear / CRM連携
- Matt Green暗号reasoning解析
- Fernetベースの推論状態暗号化
bulletPoints:
- time: 2
  text: Anthropicは大きな一週間を迎えた。Claude Code の進化形として Claude Tag を発表。個人開発者ではなくチーム単位で使う設計に再構築。
- time: 25
  text: 'Anthropic 自身の主張: 同社製品コードの約 65% が Claude Tag を介して書かれている。社内ドッグフード比率の高さでプロダクトの自信を示す。'
- time: 33
  text: Anthropic に最近加わった Andrej Karpathy は Claude Tag を『LLMインターフェースの3回目の大変革』と位置づけた。Webチャット→デスクトップアプリ→組織インフラに常駐し人間チームと協業する独立連続稼働システムへ。
- time: 54
  text: 現状の動作面は Slack に統合される形式。チャネルやスレッドで呼び出すと要求をステップに分解、接続済みツールで実行、結果をスレッドに戻す。
- time: 63
  text: 対応範囲は PR 提出・マージ、データ分析、問題解決まで。連携先は GitHub、Jira、Linear、データベース、CRM システム。
- time: 73
  text: 'デモ: エンジニア Nadia が #productingles-launches チャネルで機能追加を提案、Claude が即座にコードベース解析と解決策提示。すべて公開チャネルで対話が完結する形が示された。'
- time: 444
  text: 別軸でジョンズホプキンス大暗号学教授 Matt Green が Claude のオープンエージェントを構築中に thinking block 出力で奇妙な署名エラーに遭遇、週末を費やし約500万
    Codex トークンを溶かした。
- time: 482
  text: 'Green の解析結果: OpenAI / Anthropic 両方の reasoning ブロックは base-64 暗号化テキストを含む JSON。OpenAI
    実装は Fernet トークン規格に近い (推測)。ステートレス会話・ゼロデータ保持・ツールループでクライアントが状態を保持しつつ中身は読めない設計意図。'
sections:
- heading: Claude Tag 発表 — Claude Code を team プロダクトへ作り直す
  time: 2
  body: 'AI Revolution の動画は Anthropic の発表が立て込んだ一週間を整理する。中心になるのは新製品 Claude Tag だ。Claude
    Code の進化形と位置づけられているが、個人開発者向けではなくチーム単位で使う設計に作り直されている。


    社内ドッグフード比率としてアピールされたのが『Anthropic 自身の製品コードの約 65% が Claude Tag を介して書かれている』という数字だ。さらに、最近
    Anthropic に加わった Andrej Karpathy が Claude Tag を『LLM インターフェースの3回目の大変革』と位置づけた。Webチャット→デスクトップアプリ→そして組織インフラに常駐して人間チームと協業する独立した連続稼働システムへ、という整理だ。プロダクトとしての構えがこれまでと違うレベルにある、という訴えだ。'
- heading: Slack 統合と運用範囲 — どう動かすか
  time: 54
  body: '現時点の Claude Tag は Slack に統合される形式で動作する。チャネルやスレッドで Claude Tag を呼び出すと、与えられた要求をステップに分解し、接続済みツールで実行し、結果をそのスレッドに戻す。チャネルが業務動線になっているチームには摩擦が極めて少ない設計だ。


    対応範囲は広い。PR 提出・マージ、データ分析、問題解決まで Claude Tag が引き受け、連携先には GitHub、Jira、Linear、データベース、CRM
    システムが並ぶ。Anthropic が共有したデモでは、エンジニア Nadia が #productingles-launches というチャネルで機能追加を提案、Claude
    が即座にコードベース解析と解決策提示を行い、対話が公開チャネルで完結した。チームの可視性とエージェントの実行能力が同じ場所で交わる、というのが本プロダクトの核だ。'
- heading: Matt Green が Anthropic / OpenAI の暗号 reasoning を解析した話
  time: 424
  body: '別軸の話として動画が取り上げたのが、ジョンズホプキンス大学の暗号学教授 Matt Green が掘り下げた reasoning ブロック暗号化の解析だ。Green
    は open Claude エージェントを構築中に thinking block 出力で奇妙な署名エラーに遭遇、暗号学者として放置できず週末を費やした。約
    500 万 Codex トークンを溶かし、OpenAI のセキュリティシステムにアグレッシブにフラグされ運転免許証の写真を撮って cyber trusted
    access ポータルへ提出するまで追い込まれた。


    Green が突き止めたのは、OpenAI と Anthropic 両方の reasoning ブロックは base-64 暗号化テキストを含む JSON
    形式だということ。OpenAI 実装は Fernet トークン規格に近い (Green は推測と明言) 形をしているらしい。設計意図自体は理にかなっている。ステートレス会話・ゼロデータ保持モード・永続セッションを持たないツールループでも、クライアントが暗号化された推論状態を持ち回り、プロバイダー側が
    hidden state を渡したまま読めない・改変できない形に保てる。理屈は通る設計だが、Anthropic 実装には 64 バイトの『signature』とラベルされたフィールドが意味的に何をしているのかが不明、という問題が残った。'
editorial: Claude Tag のリリース時点でのプロダクト読みは明確だ。Anthropic は『個人のパワーユーザー向けツール』から『チーム業務の中に常駐する基盤』への重心移動を試みている。65%
  という社内コード比率は数字としては印象的だが、これを外部チームが再現できるかは別問題で、Slack に AI を常駐させる文化的・運用的準備が前提になる。Karpathy
  の『3回目の変革』フレーミングはマーケティング装飾としても言葉として強いが、要点はインターフェースが Web チャットから組織内常駐へと進む流れに名前を付けたところにある。Matt
  Green の暗号解析は別軸の独立した重要さを持つ。Anthropic / OpenAI 両社が reasoning ブロックを暗号化して返す設計は、ステートレス運用の現実解として理にかなっているが、外部監査が難しい層が日常運用の中に組み込まれていく流れも同時に意味する。読者にとっての示唆は、新製品で得られる業務生産性と、推論プロセスがブラックボックス化していく傾向を、別物として並べて評価する習慣をつけることだ。
en:
  articleTitle: Claude Tag Arrives — Anthropic's Slack-Resident Team Agent, and Matt
    Green's Crypto Probe
  seoTitle: Claude Tag Arrives — Anthropic's Slack-Resident Team Agent, and
  summary: Anthropic had a big week. Claude Tag launches as the evolution of Claude
    Code, rebuilt around teams rather than…
  keyPhrases:
  - Claude Tag (Slack-resident team agent)
  - 65% Anthropic internal codebase
  - Karpathy's third LLM transformation
  - GitHub / Jira / Linear / CRM integration
  - Matt Green cryptographic reasoning probe
  - Fernet-based reasoning encryption
  bulletPoints:
  - time: 2
    text: Anthropic had a big week. Claude Tag launches as the evolution of Claude
      Code, rebuilt around teams rather than individual developers.
  - time: 25
    text: 'The headline stat from Anthropic: around 65% of the company''s own product
      code is now being written with Claude Tag''s involvement. A heavy dogfooding
      bet.'
  - time: 33
    text: Andrej Karpathy, who recently joined Anthropic, framed Claude Tag as the
      third major LLM-interface transformation — from web chat to desktop app, and
      now to an independent, continuously running system embedded in organisational
      infrastructure, collaborating with human teams.
  - time: 54
    text: 'Today''s surface: Slack integration. Mention it in a channel or thread,
      it breaks the request into steps, executes via connected tools, and posts results
      back in the conversation.'
  - time: 63
    text: Scope covers PR submissions and merges, data analysis, problem solving.
      Integrations include GitHub, Jira, Linear, databases, CRM systems.
  - time: 73
    text: 'Demo: an engineer named Nadia proposed a feature in a #productingles-launches
      channel, Claude analysed the codebase and produced a solution — the full exchange
      happening publicly in the channel.'
  - time: 444
    text: Separately, Johns Hopkins cryptography professor Matt Green hit a strange
      signature error in Claude's thinking-block output while setting up an open Claude
      agent, and spent a weekend on it. Burned about 5 million Codex tokens.
  - time: 482
    text: 'Green''s findings: reasoning blocks for both OpenAI and Anthropic ship
      to the client as JSON containing base-64 ciphertext. OpenAI''s implementation
      looks loosely Fernet-based (his guess). The intent — stateless conversations,
      zero-retention modes, tool loops without a persistent server — makes sense in
      principle.'
  sections:
  - heading: Claude Tag — rebuilding Claude Code as a team product
    time: 2
    body: 'AI Revolution''s video walks through Anthropic''s loaded week. The centrepiece
      is Claude Tag, a new product positioned as the evolution of Claude Code, rebuilt
      for teams rather than individual developers.


      The dogfooding claim is striking — around 65% of Anthropic''s own product code
      now goes through Claude Tag. On top of that, Andrej Karpathy, recently arrived
      at Anthropic, framed Claude Tag as the third major transformation of LLM interfaces.
      Web chat first, desktop apps second, and now independent, continuously running
      systems embedded in organisational infrastructure, collaborating with human
      teams. The framing signals a different posture for the product than what came
      before.'
  - heading: Slack integration and operational scope — how it actually works
    time: 54
    body: 'Today''s Claude Tag surface is Slack. Mention it in a channel or thread,
      and it breaks the request into steps, executes through connected tools, and
      posts results back in the conversation. For teams whose workflow already lives
      in Slack, the friction is essentially zero.


      The scope is broad. Claude Tag handles PR submissions and merges, data analysis,
      and problem solving, with integrations that include GitHub, Jira, Linear, databases,
      and CRM systems. In Anthropic''s demo, an engineer named Nadia proposed adding
      a feature in a #productingles-launches channel; Claude analysed the codebase
      and delivered a solution, the entire exchange playing out in public view. Team
      visibility and agent execution meet in the same surface — that''s the structural
      move.'
  - heading: Matt Green's crypto probe of Anthropic / OpenAI reasoning blocks
    time: 424
    body: 'On a separate axis, the video covers Johns Hopkins cryptography professor
      Matt Green''s investigation of how reasoning blocks are encrypted. Green hit
      a strange signature error in Claude''s thinking-block output while setting up
      an open Claude agent and, true to form for a cryptographer, couldn''t let it
      go. A full weekend, roughly 5 million Codex tokens spent, and at one point OpenAI''s
      security flagged him hard enough that he had to photograph his driver''s licence
      and submit it to a cyber-trusted access portal just to keep going.


      His findings: both OpenAI and Anthropic ship reasoning blocks to the client
      as JSON containing base-64 ciphertext. OpenAI''s implementation appears loosely
      Fernet-based (Green flags this as a guess). The design intent makes sense —
      in stateless conversations, zero-retention modes, or tool loops without a persistent
      server session, the client needs to carry state forward, and encrypted reasoning
      lets the provider hand back hidden model state in a form the client can relay
      but not read or modify. Reasonable on paper. In practice, Anthropic''s implementation
      has a 64-byte field labelled ''signature'' whose role wasn''t clear.'
  editorial: Reading Claude Tag at release, the product strategy is clear. Anthropic
    is shifting weight from 'tool for the individual power user' to 'foundation embedded
    in team operations.' The 65% internal code stat is impressive as a marker, but
    whether external teams can reproduce that depends on cultural and operational
    readiness to host an AI inside Slack as a first-class presence. Karpathy's 'third
    transformation' framing is strong as marketing language, but the substance is
    simply naming the move from web-chat interfaces to org-resident agents. Matt Green's
    cryptographic probe matters independently. The decision by both Anthropic and
    OpenAI to encrypt reasoning blocks is sound from a stateless-operations standpoint,
    but it also formalises a layer that's hard to audit externally as it embeds itself
    in everyday workflows. The reader's takeaway is to evaluate the productivity gains
    and the increasing opacity of the reasoning layer as separate, parallel considerations.
  headerImage: /images/hDsZMb_8FYo/header.png
  heroImage: /images/hDsZMb_8FYo/header.png
---

## ハイライト

- [00:02] Anthropicは大きな一週間を迎えた。Claude Code の進化形として Claude Tag を発表。個人開発者ではなくチーム単位で使う設計に再構築。
- [00:25] Anthropic 自身の主張: 同社製品コードの約 65% が Claude Tag を介して書かれている。社内ドッグフード比率の高さでプロダクトの自信を示す。
- [00:33] Anthropic に最近加わった Andrej Karpathy は Claude Tag を『LLMインターフェースの3回目の大変革』と位置づけた。Webチャット→デスクトップアプリ→組織インフラに常駐し人間チームと協業する独立連続稼働システムへ。
- [00:54] 現状の動作面は Slack に統合される形式。チャネルやスレッドで呼び出すと要求をステップに分解、接続済みツールで実行、結果をスレッドに戻す。
- [01:03] 対応範囲は PR 提出・マージ、データ分析、問題解決まで。連携先は GitHub、Jira、Linear、データベース、CRM システム。
- [01:13] デモ: エンジニア Nadia が #productingles-launches チャネルで機能追加を提案、Claude が即座にコードベース解析と解決策提示。すべて公開チャネルで対話が完結する形が示された。
- [07:24] 別軸でジョンズホプキンス大暗号学教授 Matt Green が Claude のオープンエージェントを構築中に thinking block 出力で奇妙な署名エラーに遭遇、週末を費やし約500万 Codex トークンを溶かした。
- [08:02] Green の解析結果: OpenAI / Anthropic 両方の reasoning ブロックは base-64 暗号化テキストを含む JSON。OpenAI 実装は Fernet トークン規格に近い (推測)。ステートレス会話・ゼロデータ保持・ツールループでクライアントが状態を保持しつつ中身は読めない設計意図。

## セクション

### Claude Tag 発表 — Claude Code を team プロダクトへ作り直す

- 時刻: 00:02

AI Revolution の動画は Anthropic の発表が立て込んだ一週間を整理する。中心になるのは新製品 Claude Tag だ。Claude Code の進化形と位置づけられているが、個人開発者向けではなくチーム単位で使う設計に作り直されている。

社内ドッグフード比率としてアピールされたのが『Anthropic 自身の製品コードの約 65% が Claude Tag を介して書かれている』という数字だ。さらに、最近 Anthropic に加わった Andrej Karpathy が Claude Tag を『LLM インターフェースの3回目の大変革』と位置づけた。Webチャット→デスクトップアプリ→そして組織インフラに常駐して人間チームと協業する独立した連続稼働システムへ、という整理だ。プロダクトとしての構えがこれまでと違うレベルにある、という訴えだ。

### Slack 統合と運用範囲 — どう動かすか

- 時刻: 00:54

現時点の Claude Tag は Slack に統合される形式で動作する。チャネルやスレッドで Claude Tag を呼び出すと、与えられた要求をステップに分解し、接続済みツールで実行し、結果をそのスレッドに戻す。チャネルが業務動線になっているチームには摩擦が極めて少ない設計だ。

対応範囲は広い。PR 提出・マージ、データ分析、問題解決まで Claude Tag が引き受け、連携先には GitHub、Jira、Linear、データベース、CRM システムが並ぶ。Anthropic が共有したデモでは、エンジニア Nadia が #productingles-launches というチャネルで機能追加を提案、Claude が即座にコードベース解析と解決策提示を行い、対話が公開チャネルで完結した。チームの可視性とエージェントの実行能力が同じ場所で交わる、というのが本プロダクトの核だ。

### Matt Green が Anthropic / OpenAI の暗号 reasoning を解析した話

- 時刻: 07:04

別軸の話として動画が取り上げたのが、ジョンズホプキンス大学の暗号学教授 Matt Green が掘り下げた reasoning ブロック暗号化の解析だ。Green は open Claude エージェントを構築中に thinking block 出力で奇妙な署名エラーに遭遇、暗号学者として放置できず週末を費やした。約 500 万 Codex トークンを溶かし、OpenAI のセキュリティシステムにアグレッシブにフラグされ運転免許証の写真を撮って cyber trusted access ポータルへ提出するまで追い込まれた。

Green が突き止めたのは、OpenAI と Anthropic 両方の reasoning ブロックは base-64 暗号化テキストを含む JSON 形式だということ。OpenAI 実装は Fernet トークン規格に近い (Green は推測と明言) 形をしているらしい。設計意図自体は理にかなっている。ステートレス会話・ゼロデータ保持モード・永続セッションを持たないツールループでも、クライアントが暗号化された推論状態を持ち回り、プロバイダー側が hidden state を渡したまま読めない・改変できない形に保てる。理屈は通る設計だが、Anthropic 実装には 64 バイトの『signature』とラベルされたフィールドが意味的に何をしているのかが不明、という問題が残った。

## 編集部の視点

Claude Tag のリリース時点でのプロダクト読みは明確だ。Anthropic は『個人のパワーユーザー向けツール』から『チーム業務の中に常駐する基盤』への重心移動を試みている。65% という社内コード比率は数字としては印象的だが、これを外部チームが再現できるかは別問題で、Slack に AI を常駐させる文化的・運用的準備が前提になる。Karpathy の『3回目の変革』フレーミングはマーケティング装飾としても言葉として強いが、要点はインターフェースが Web チャットから組織内常駐へと進む流れに名前を付けたところにある。Matt Green の暗号解析は別軸の独立した重要さを持つ。Anthropic / OpenAI 両社が reasoning ブロックを暗号化して返す設計は、ステートレス運用の現実解として理にかなっているが、外部監査が難しい層が日常運用の中に組み込まれていく流れも同時に意味する。読者にとっての示唆は、新製品で得られる業務生産性と、推論プロセスがブラックボックス化していく傾向を、別物として並べて評価する習慣をつけることだ。
