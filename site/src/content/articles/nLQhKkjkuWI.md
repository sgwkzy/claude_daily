---
videoId: nLQhKkjkuWI
title: Claude Tested Over 9,000 Trading Strategies (Here's What Works)
slug: claude-で9000本のバックテストを実行-残ったのは平均回帰だけだった-brendan-の方法論-nlqhkkjkuwi
articleTitle: Claude で9,000本のバックテストを実行 — 残ったのは平均回帰だけだった Brendan の方法論
seoTitle: Claude で9,000本のバックテストを実行 — 残ったのは平均回帰だけだった Brendan の方法論
summary: AI Pathways の Brendan が Claude を使い9,000本のトレード戦略バックテストを実行。トレンドフォロー、平均回帰、モメンタム、ブレイクアウトなど主要戦略を30銘柄・15年分のデータで検証した結果を公開する。
channel: AI Pathways
channelId: UCJ-KJeHzrnZkGX7qAM2V74Q
publishedAt: '2026-06-28T13:00:30Z'
fetchedAt: '2026-06-30T12:28:42.794042Z'
originalThumbnail: https://i.ytimg.com/vi/nLQhKkjkuWI/maxresdefault.jpg
headerImage: /images/nLQhKkjkuWI/header.ja.png
heroImage: /images/nLQhKkjkuWI/header.ja.png
viewCount: 129391
durationSec: 1195
sourceLanguage: en-US
matchedKeywords:
- Claude
proposedByLLM: false
keyPhrases:
- 9,000本バックテストシステム
- 平均回帰戦略の優位性
- 6フィルタ生存率64%
- Claude Code 実装手順公開
- ロバストネス・ブートストラップ検証
- 投資銀行出身者の定量検証
bulletPoints:
- time: 0
  text: AI Pathways の Brendan が Claude を使い9,000本のトレード戦略バックテストを実行。トレンドフォロー、平均回帰、モメンタム、ブレイクアウトなど主要戦略を30銘柄・15年分のデータで検証した結果を公開する。
- time: 17
  text: 解説者は数学・経済を UCLA で学び Raymond James で投資銀行に3年勤務した経歴。クライアント向けのトレードシステム構築を2年続けており、定量分析の実務経験から動画は組み立てられている。
- time: 49
  text: Claude で構築したこのテストシステムは、9,000本のバックテストを6つのフィルタで段階的にふるい落とす設計。動画は各タイル(モジュール)の役割を順に解説する形を取る。
- time: 68
  text: テスト対象は流動性の高い銘柄の日足。S&P 500/NASDAQ などの主要 ETF、セクター ETF、金、原油、債券、ビットコイン、イーサリアムを含む15年(2010-2025)分の履歴で検証する。
- time: 557
  text: 結果は明確だった。主要戦略カテゴリの中で正のリターンを残したのは平均回帰のみ。トレード順序をシャッフルしても結果が崩れず、運に依存しない頑健性を示した。
- time: 591
  text: 6フィルタを通過したのは524本、10年以上の履歴がある銘柄に絞ると478本。そのうち64%が平均回帰戦略で、生き残った戦略の約2/3を占めた。
- time: 612
  text: 平均回帰は学術研究で最も裏付けが厚い戦略。価格が平均から極端に乖離した後は人間心理と市場構造の両方の理由で平均へ戻るという仕組み。一方の移動平均クロスオーバーは理論的根拠が薄く、データもそれを示していた。
- time: 1112
  text: このシステムは Claude Code か Claude.ai で再現可能。プロンプトをスクリーンショットして AI に渡すだけで、データ・戦略ライブラリ、6フィルタのバックテストファネル、ロバストネスチェックの各層を構築できる。
sections:
- heading: 9,000本バックテスト — Claude で組んだ戦略検証システムの全体像
  time: 0
  body: 'AI Pathways の Brendan が Claude で構築した戦略検証システムを公開する。トレンドフォロー、平均回帰、モメンタム、ブレイクアウトといった主要なファミリを30銘柄・15年分のデータで9,000本バックテストし、何が生き残るかを定量で示すという内容だ。


    解説者の経歴は UCLA で数学と経済、Raymond James で投資銀行3年、クライアント向けトレードシステム構築2年。動画冒頭で投資助言ではないと明言したうえで、データとメソドロジーの提示に徹する。テスト対象は流動性の高い銘柄の日足で、S&P
    500/NASDAQ などの主要 ETF、セクター ETF、金、原油、債券、ビットコイン、イーサリアムを含む。6フィルタで段階的にふるい落とす構造になっている。'
- heading: 残ったのは平均回帰だけ — 478本の生存戦略の内訳
  time: 557
  body: '結果は明確だった。主要カテゴリの中で正のリターンを残したのは平均回帰のみで、トレード順序をシャッフルしても結果が崩れず、運に依存しない頑健性を示した。6フィルタ全通過は524本、10年以上の履歴がある銘柄に限定すると478本まで絞られる。そのうち64%が平均回帰戦略だった。


    平均回帰が強い理由は学術研究と整合的だ。価格が平均から極端に乖離した後は、人間心理(過剰反応の修正)と市場構造の両方の理由で平均へ戻る傾向がある。何十年にも及ぶ研究がこの仕組みを裏付けている。対照的に移動平均クロスオーバーは『一本の線がもう一本を横切る』だけのもので、これが将来を予測すべき理論的根拠は薄く、9,000本のデータもそれを支持しなかった。'
- heading: 再現可能なシステム — Claude Code でレイヤを組み立てる
  time: 1112
  body: 'Brendan はこのシステムを誰でも再現できる形で公開している。プロンプトをスクリーンショットして AI モデルに渡せば、Claude.ai のウェブアプリでも
    Claude Code でも構築できる。Claude Code を使うほうが一箇所でコードを管理・更新できる利点がある。


    構成は階層的だ。第一層はデータ・戦略ライブラリで、コピーして Claude Code に貼り付ければ動く。第二層はバックテストファネルで、ウォークフォワード/アウトオブサンプル検証と6つのフィルタを含む。第三層はロバストネスチェックで、パラメータ感度とブートストラップ・ストレステストを行う。最終層がモメンタム戦略向けのクロスセクショナル検証だ。これらが揃えば、Trading
    View で見かけた怪しいバックテストに頼らず、自分のアイデアを定量的に検証できるツールセットになる。'
editorial: この検証が示すのは『AI でトレードが儲かる』という派手な結論ではなく、9,000本という規模のバックテストを Claude で組み立てて回せるようになった、その実装ハードルの低下のほうだ。従来は専門のクオンツチームと独自インフラが必要だった検証作業が、個人投資家のレベルで再現可能になっている。読者にとっての含意は二つある。第一に、AI
  で『良い戦略』を探すより、既存の検証研究を AI で素早く再現して自分の前提条件に当て直すほうが投資対効果が高い。第二に、Brendan が示したように再現可能なプロンプト一式が公開されている以上、競争力の源泉は『プロンプトを持っているか』ではなく『6フィルタの後ろにある手法選択と銘柄選定の判断』に移る。ツールは平準化し、判断力が差別化要因として残る局面に入っている。
en:
  articleTitle: Running 9,000 Backtests Through Claude — Only Mean Reversion Survived
    in Brendan's Method
  seoTitle: Running 9,000 Backtests Through Claude — Only Mean Reversion Sur
  summary: AI Pathways' Brendan ran 9,000 trading-strategy backtests through Claude.
    Trend following, mean reversion, momentum,…
  keyPhrases:
  - 9,000-backtest validation system
  - Mean-reversion dominance
  - Six-filter 64% survivor share
  - Public Claude Code implementation
  - Bootstrap and robustness checks
  - Quant validation by an IB alumnus
  bulletPoints:
  - time: 0
    text: AI Pathways' Brendan ran 9,000 trading-strategy backtests through Claude.
      Trend following, mean reversion, momentum, breakouts — every major family —
      across 30 assets and 15 years of data, with the results published in this video.
  - time: 17
    text: 'Brendan''s background: math and econ at UCLA, three years in investment
      banking at Raymond James, and two years building trading systems for clients.
      The quantitative experience is the backbone of how the video is structured.'
  - time: 49
    text: The test system Brendan built with Claude funnels 9,000 backtests through
      six filters in stages. The video walks through what each tile (module) in the
      system does, in order.
  - time: 68
    text: The test surface is daily bars on liquid assets — major ETFs like S&P 500
      and NASDAQ, the sector ETFs, gold, oil, bonds, Bitcoin, Ethereum — across 15
      years of history (2010-2025).
  - time: 557
    text: The result is clear. Among the major strategy families, mean reversion was
      the only category that came out positive. Even shuffling the order of trades
      didn't break it — the robustness signal showed it wasn't relying on luck.
  - time: 591
    text: 524 strategies passed all six filters; narrowing to assets with over 10
      years of history drops it to 478. Of those 478, 64% are mean reversion — about
      two-thirds of everything that survived.
  - time: 612
    text: Mean reversion has the deepest academic backing of any major strategy. The
      mechanism — prices that overshoot mean-revert due to both human psychology and
      market structure — is well-documented over decades. By contrast, a moving-average
      crossover has no theoretical reason to predict anything, and the data showed
      mostly that it doesn't.
  - time: 1112
    text: The system is reproducible. Screenshot the prompts and hand them to an AI
      model — you can build it in claude.ai or in Claude Code. Data and strategy library,
      six-filter backtest funnel, robustness checks — each layer is published.
  sections:
  - heading: 9,000 Backtests — The Strategy Validation System Built on Claude
    time: 0
    body: 'AI Pathways'' Brendan publishes the strategy-validation system he built
      on Claude. Trend following, mean reversion, momentum, breakouts — every major
      family — tested across 30 assets and 15 years of data, with 9,000 backtests
      in total. The frame is to show quantitatively what survives.


      His background: math and econ at UCLA, three years at Raymond James in investment
      banking, and two years building trading systems for clients. The video opens
      with a clear disclaimer that nothing here is financial advice, and is then disciplined
      in sticking to data and methodology. The test surface is daily bars on liquid
      assets — major ETFs like S&P 500 and NASDAQ, the sector ETFs, gold, oil, bonds,
      Bitcoin and Ethereum. Six filters whittle the candidate set down in stages.'
  - heading: Only Mean Reversion Survived — Inside the 478 Surviving Strategies
    time: 557
    body: 'The result lands cleanly. Among the major categories, mean reversion was
      the only family that came out positive, and shuffling the trade order didn''t
      break it — a sign the result wasn''t a luck artifact. 524 strategies cleared
      all six filters; restrict that to assets with over 10 years of history and it
      drops to 478. Of those 478, 64% are mean reversion strategies.


      Why mean reversion dominates is consistent with the academic literature. After
      prices overshoot the mean, both human psychology (the unwinding of overreaction)
      and market structure pull them back. Decades of research underwrite the mechanism.
      By contrast, a moving-average crossover — one line crossing another — has no
      theoretical reason to predict anything, and the 9,000 backtests didn''t support
      it either.'
  - heading: A Reproducible System — Build the Layers in Claude Code
    time: 1112
    body: 'Brendan publishes this in a form anyone can replicate. Screenshot the prompts
      and hand them to an AI model — you can build it in the claude.ai web app or
      in Claude Code. Claude Code has the advantage of letting you manage and update
      the codebase in one place.


      The construction is layered. The first layer is the data and strategy library
      — copy it into Claude Code and you''re up. The second is the backtest funnel
      — walk-forward / out-of-sample validation plus the six filters. The third layer
      is robustness checks — parameter sensitivity and bootstrap stress testing. The
      final layer is the cross-sectional check, specific to momentum-based strategies.
      Together the layers give you a tool to validate your own ideas quantitatively,
      rather than trusting a backtest you happened to see on TradingView.'
  editorial: What this validation actually shows isn't the splashy 'AI makes trading
    profitable' claim — it's the collapse of the implementation barrier. Running 9,000
    backtests, the kind of work that used to require a specialist quant team and bespoke
    infrastructure, has become a personal-investor capability via Claude. Two implications
    for readers. First, the higher-ROI move is no longer using AI to 'discover' a
    good strategy — it's using AI to quickly reproduce the existing validation literature
    against your own constraints. Second, with a complete prompt set publicly shared
    as Brendan has done here, the competitive edge moves off 'do you have the prompt'
    and onto 'do you make the right method and asset choices behind the six filters.'
    Tools level out; judgment is what stays differentiated.
  headerImage: /images/nLQhKkjkuWI/header.png
  heroImage: /images/nLQhKkjkuWI/header.png
---

## ハイライト

- [00:00] AI Pathways の Brendan が Claude を使い9,000本のトレード戦略バックテストを実行。トレンドフォロー、平均回帰、モメンタム、ブレイクアウトなど主要戦略を30銘柄・15年分のデータで検証した結果を公開する。
- [00:17] 解説者は数学・経済を UCLA で学び Raymond James で投資銀行に3年勤務した経歴。クライアント向けのトレードシステム構築を2年続けており、定量分析の実務経験から動画は組み立てられている。
- [00:49] Claude で構築したこのテストシステムは、9,000本のバックテストを6つのフィルタで段階的にふるい落とす設計。動画は各タイル(モジュール)の役割を順に解説する形を取る。
- [01:08] テスト対象は流動性の高い銘柄の日足。S&P 500/NASDAQ などの主要 ETF、セクター ETF、金、原油、債券、ビットコイン、イーサリアムを含む15年(2010-2025)分の履歴で検証する。
- [09:17] 結果は明確だった。主要戦略カテゴリの中で正のリターンを残したのは平均回帰のみ。トレード順序をシャッフルしても結果が崩れず、運に依存しない頑健性を示した。
- [09:51] 6フィルタを通過したのは524本、10年以上の履歴がある銘柄に絞ると478本。そのうち64%が平均回帰戦略で、生き残った戦略の約2/3を占めた。
- [10:12] 平均回帰は学術研究で最も裏付けが厚い戦略。価格が平均から極端に乖離した後は人間心理と市場構造の両方の理由で平均へ戻るという仕組み。一方の移動平均クロスオーバーは理論的根拠が薄く、データもそれを示していた。
- [18:32] このシステムは Claude Code か Claude.ai で再現可能。プロンプトをスクリーンショットして AI に渡すだけで、データ・戦略ライブラリ、6フィルタのバックテストファネル、ロバストネスチェックの各層を構築できる。

## セクション

### 9,000本バックテスト — Claude で組んだ戦略検証システムの全体像

- 時刻: 00:00

AI Pathways の Brendan が Claude で構築した戦略検証システムを公開する。トレンドフォロー、平均回帰、モメンタム、ブレイクアウトといった主要なファミリを30銘柄・15年分のデータで9,000本バックテストし、何が生き残るかを定量で示すという内容だ。

解説者の経歴は UCLA で数学と経済、Raymond James で投資銀行3年、クライアント向けトレードシステム構築2年。動画冒頭で投資助言ではないと明言したうえで、データとメソドロジーの提示に徹する。テスト対象は流動性の高い銘柄の日足で、S&P 500/NASDAQ などの主要 ETF、セクター ETF、金、原油、債券、ビットコイン、イーサリアムを含む。6フィルタで段階的にふるい落とす構造になっている。

### 残ったのは平均回帰だけ — 478本の生存戦略の内訳

- 時刻: 09:17

結果は明確だった。主要カテゴリの中で正のリターンを残したのは平均回帰のみで、トレード順序をシャッフルしても結果が崩れず、運に依存しない頑健性を示した。6フィルタ全通過は524本、10年以上の履歴がある銘柄に限定すると478本まで絞られる。そのうち64%が平均回帰戦略だった。

平均回帰が強い理由は学術研究と整合的だ。価格が平均から極端に乖離した後は、人間心理(過剰反応の修正)と市場構造の両方の理由で平均へ戻る傾向がある。何十年にも及ぶ研究がこの仕組みを裏付けている。対照的に移動平均クロスオーバーは『一本の線がもう一本を横切る』だけのもので、これが将来を予測すべき理論的根拠は薄く、9,000本のデータもそれを支持しなかった。

### 再現可能なシステム — Claude Code でレイヤを組み立てる

- 時刻: 18:32

Brendan はこのシステムを誰でも再現できる形で公開している。プロンプトをスクリーンショットして AI モデルに渡せば、Claude.ai のウェブアプリでも Claude Code でも構築できる。Claude Code を使うほうが一箇所でコードを管理・更新できる利点がある。

構成は階層的だ。第一層はデータ・戦略ライブラリで、コピーして Claude Code に貼り付ければ動く。第二層はバックテストファネルで、ウォークフォワード/アウトオブサンプル検証と6つのフィルタを含む。第三層はロバストネスチェックで、パラメータ感度とブートストラップ・ストレステストを行う。最終層がモメンタム戦略向けのクロスセクショナル検証だ。これらが揃えば、Trading View で見かけた怪しいバックテストに頼らず、自分のアイデアを定量的に検証できるツールセットになる。

## 編集部の視点

この検証が示すのは『AI でトレードが儲かる』という派手な結論ではなく、9,000本という規模のバックテストを Claude で組み立てて回せるようになった、その実装ハードルの低下のほうだ。従来は専門のクオンツチームと独自インフラが必要だった検証作業が、個人投資家のレベルで再現可能になっている。読者にとっての含意は二つある。第一に、AI で『良い戦略』を探すより、既存の検証研究を AI で素早く再現して自分の前提条件に当て直すほうが投資対効果が高い。第二に、Brendan が示したように再現可能なプロンプト一式が公開されている以上、競争力の源泉は『プロンプトを持っているか』ではなく『6フィルタの後ろにある手法選択と銘柄選定の判断』に移る。ツールは平準化し、判断力が差別化要因として残る局面に入っている。
