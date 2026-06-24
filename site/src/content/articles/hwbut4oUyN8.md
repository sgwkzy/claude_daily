---
videoId: hwbut4oUyN8
title: 全ての士業は保険屋になる。僕のAIエージェントが３か国の公認会計士試験に受かるようになって確信したこと
slug: 全ての士業は保険屋になる-自作aiがシンガポール公認会計士試験に10戦10勝した日-hwbut4ouyn8
articleTitle: 全ての士業は『保険屋』になる — 自作AIがシンガポール公認会計士試験に10戦10勝した日
seoTitle: 全ての士業は『保険屋』になる — 自作AIがシンガポール公認会計士試験に10戦10勝した日
summary: 投稿者の自作AIエージェントがシンガポール公認会計士試験 (SCAQ) の過去問で10回受験10回合格。平均70点台、人間3時間のところを1時間以内で完答。
channel: 海外Yパパラジオ　世界を読み解く
channelId: UC8fTn4DsxlAlql3OXJ8syRA
publishedAt: '2026-06-23T08:12:44Z'
fetchedAt: '2026-06-24T00:51:56.393092Z'
originalThumbnail: https://i.ytimg.com/vi/hwbut4oUyN8/maxresdefault.jpg
headerImage: /images/hwbut4oUyN8/header.ja.png
heroImage: /images/hwbut4oUyN8/header.ja.png
viewCount: 16739
durationSec: 599
sourceLanguage: ja
matchedKeywords:
- AIエージェント
proposedByLLM: false
keyPhrases:
- シンガポールSCAQ AI合格
- ハイブリッド検索 + HyDE + リランキング
- 士業の保険料モデルへの転換
- 賠償責任引受
- AI×公認会計士業務
- 海外Yパパラジオ
bulletPoints:
- time: 0
  text: 投稿者の自作AIエージェントがシンガポール公認会計士試験 (SCAQ) の過去問で10回受験10回合格。平均70点台、人間3時間のところを1時間以内で完答。
- time: 26
  text: 元はニュージーランドの試験で合格させた話を予定していたが著作権・規約がグレーになるため断念。シンガポールはSCAQの過去問と模範解答を公的機関がPDFで公開しているためクリーンに話せる、と切り替え。
- time: 95
  text: SCAQは財務報告・監査・税務・ガバナンスの4科目。すべてオンライン受験 (Webカメラ監視) という真面目な試験。
- time: 232
  text: 'AIの仕組みは3層構成: ベクトル検索＋キーワード検索のハイブリッド (条文番号や法令用語はキーワードが強い)、HyDE (仮の答えで検索)、リランキング
    (30件取って別モデルで5件に絞り込み)。'
- time: 275
  text: この3工夫を入れる前は平均52点で合格ライン50点ギリギリ。入れた途端70点台に跳ね上がり、ギリギリ合格から余裕合格へ。
- time: 302
  text: 弱点も人間に似ていた。図表問題で5〜10点下落 (マルチモーダル未成熟)、シンガポール消費税8→9%引き上げの税制改正混同、監査が苦手で財務 (ZAM)
    は得意、という傾向。
- time: 334
  text: 本題はここから。AIが士業になった、という話ではない。試験に受かっても、AIが顧客の税務相談に署名して責任を取れるわけではない。
- time: 484
  text: '結論: 顧客が士業に払うお金の意味が『調査費・分析費』から『保険料』に変わる。報酬主軸が賠償責任引受料へ。AI使いの士業が件数10倍×保険料ベースで回し、抵抗組は時間単価で徐々に苦しくなる。'
sections:
- heading: 自作AIがSCAQで10戦10勝 — 過程の検証
  time: 0
  body: '海外Yパパラジオの投稿者は、自分で組んだAIエージェントにシンガポール公認会計士試験 (SCAQ) の過去問を解かせ、10回受験して10回合格させた。本来はニュージーランドの試験で合格させた話を予定していたが、試験問題・模範解答の出所が著作権・試験機関規約上グレーになるため断念。シンガポールは過去問と模範解答を公的機関がPDFで堂々と公開しているのでクリーンに話せる、と動画テーマを切り替えている。


    SCAQは財務報告・監査・税務・ガバナンスの4科目をWebカメラ監視下のオンラインで受験する真面目な試験で、いわゆる『出題予想』で押し切れる試験ではない。それを自作AIに通させた、というのが本動画の検証対象だ。'
- heading: AIの仕組み — ハイブリッド検索・HyDE・リランキングの3層
  time: 232
  body: 'AIの実装は3つの工夫を組み合わせている。第1にハイブリッド検索。ベクトル検索とキーワード検索を並行に走らせて結果をマージする。条文番号や法令用語のような語はキーワード検索の方が強いため、片方だけでは性能が出ない。


    第2にHyDE (Hypothetical Document Embeddings)。質問をそのまま検索するのでなく、AIに一度『仮の答え』を作らせ、その仮答案で検索する。資料の中では質問文より答え風の文の方が、正解に近い場所にあるからだ。第3にリランキング。広く30件取得し、別の専門モデルで本当に必要な5件に絞り込む2段階方式。この3工夫を入れる前の単純検索だけのときは平均52点でラインギリギリだったが、入れた途端に70点台へ跳ね上がった。10回受験して10回合格、人間が3時間かけるところAIは1時間以内で完答する。弱点も興味深く、図表問題は5〜10点下落
    (マルチモーダル未成熟)、シンガポール消費税8→9%引き上げの税制改正で混同、監査が苦手で財務が得意 — 人間の合格者の傾向と似ているのが面白い点だ。'
- heading: 本題 — 士業ビジネスは『調査費』から『保険料』へ
  time: 334
  body: '投稿者はここからが本題だ、と言う。これはAIが公認会計士になったという話ではない。試験に受かったところで、AIが顧客の税務相談に乗って書類に署名し、賠償責任まで取れるわけではない。


    投稿者の本当の主張は別軸にある。公認会計士・弁護士の戦うゾーンが変わる。顧客が士業に払うお金の意味が『調査費・分析費』から『保険料』に変わるのだ。今でも士業賠償責任保険は存在するが、おまけの位置づけで、報酬の主軸はプロフェッショナルサービス料だ。これが逆転して、報酬の主軸が賠償責任引受料になる。士業はAIと人間のチェック役＋責任引受人として、保険料ベースのビジネスモデルへ移行する。AIを早く受け入れた士業は件数を10倍に増やして保険料ベースで回し、抵抗組は時間単価で徐々に苦しくなる、というのが10年後・20年後の景色になる、と動画は締めくくる。'
editorial: 『士業は保険屋になる』という結論が、AI合格そのものより重要だ。自作AIがSCAQに10戦10勝しても、顧客の税務相談に署名して責任を取れるわけではない——ここに自動化が届く範囲と人間が残る範囲の境界が鮮明に出る。報酬の意味が調査費から賠償責任の保険料へ移るという見立ては、専門職の価値の再定義として説得力がある。ハイブリッド検索＋HyDE＋リランキングで52点が70点台に跳ねた事実は、RAG設計の工夫が成果を決めることの好例でもある。
en:
  articleTitle: Every Licensed Professional Becomes an Insurer — My AI Just Passed
    the Singapore CPA Exam 10 for 10
  seoTitle: Every Licensed Professional Becomes an Insurer — My AI Just Pass
  summary: The creator's home-built AI agent passed the Singapore CPA exam (SCAQ)
    on past papers — 10 attempts, 10 passes.…
  keyPhrases:
  - Singapore SCAQ AI 10/10
  - hybrid retrieval + HyDE + reranking
  - profession shifts to insurance premium
  - liability absorption pricing
  - AI × CPA workflow
  - Yparadigm channel
  bulletPoints:
  - time: 0
    text: The creator's home-built AI agent passed the Singapore CPA exam (SCAQ) on
      past papers — 10 attempts, 10 passes. Average 70s, finishing in under an hour
      where humans take three.
  - time: 26
    text: He originally planned to talk about New Zealand's CPA exam, which the AI
      also passed, but the source materials sit in a grey copyright zone. Singapore
      publishes past papers and answer keys via its public body, so the discussion
      can be clean.
  - time: 95
    text: SCAQ has four serious modules — financial reporting, audit, tax, and governance
      — taken online under webcam proctoring.
  - time: 232
    text: 'The AI stack has three pieces: hybrid retrieval (vector search plus keyword
      search — clauses and legal terms need keyword), HyDE (let the AI draft a hypothetical
      answer and search that), and reranking (pull 30, rerank to 5 with a specialist
      model).'
  - time: 275
    text: 'Before adding those three, the system averaged 52 — barely above the 50
      pass line. After: low 70s. Margin of pass turned into margin of comfort.'
  - time: 302
    text: Failure modes mirror humans. Image and table questions drop 5–10 points
      (multimodal isn't there yet), Singapore's 8→9% GST tax change gets confused
      occasionally, and audit is weaker than financial reporting — same skew real
      candidates show.
  - time: 334
    text: The point isn't 'AI became a CPA.' It can't sign a tax return or take liability
      for client advice. The point is what the profession itself is becoming.
  - time: 484
    text: 'The conclusion: what clients pay licensed professionals for shifts from
      research and analysis to an insurance premium. The early adopters scale 10×
      on volume with premium-based pricing; the holdouts get squeezed on hourly billing.'
  sections:
  - heading: 10 attempts, 10 passes — the SCAQ experiment
    time: 0
    body: 'The creator built an AI agent and ran it against past papers for the Singapore
      CPA exam (SCAQ). It passed 10 times out of 10. He had originally planned to
      talk about the New Zealand CPA exam, which his AI also passed, but the source
      materials there sit in a grey zone — copyright and exam-board terms get murky
      the moment you describe where the questions came from. Singapore''s public exam
      body publishes past papers and answer keys as PDFs, so this whole video can
      be discussed cleanly.


      SCAQ is no toy exam. Four modules — financial reporting, audit, tax, and governance
      — taken online under webcam proctoring. Not the kind of test you cheese with
      question-guessing. That''s the workload the AI was put against.'
  - heading: The retrieval stack — hybrid + HyDE + rerank
    time: 232
    body: 'The AI''s edge comes from three layered tricks. First, hybrid retrieval
      — vector search and keyword search run in parallel, results merged. Clause numbers
      and legal terms favour keyword search, which pure embeddings can miss. Second,
      HyDE: instead of searching with the question, ask the AI to draft a hypothetical
      answer first, then search with that. In the source material, the answer text
      sits closer to the real answer than the question text does.


      Third, reranking. Pull a wide 30 candidates, then use a separate specialist
      model to filter down to the actual 5 needed. Before these three layers landed,
      average score was 52 — just over the 50 pass line. After: low 70s. The system
      moved from barely-passing to comfortably-passing in one upgrade. The AI finishes
      in under an hour where humans take three. Its failure modes are oddly human
      — 5–10 points off on image and table questions (multimodal isn''t there yet),
      occasional confusion on Singapore''s 8→9% GST change, audit weaker than financial
      reporting. Same skew real candidates show.'
  - heading: Where the profession actually goes — from fees to premiums
    time: 334
    body: 'The headline isn''t ''AI became a CPA.'' The AI can''t sign a tax return
      or take liability for advice given to a real client. The author''s actual claim
      is sharper, and structural.


      What clients pay licensed professionals for shifts. Today they pay for research,
      analysis, and a deliverable. Tomorrow they''re paying for liability absorption
      — the professional''s malpractice insurance is what''s really being purchased.
      Today professional indemnity insurance is a side item, with the main bill being
      the professional service fee. That gets inverted. Premium becomes the main line
      item. The professional sits between an AI doing the research and a human doing
      the sign-off, taking a premium to absorb the risk. Once that flips, new insurance
      products and new liability designs follow. The author''s prediction: licensed
      professionals who embrace AI scale 10× on case volume and run on premium-based
      pricing. The holdouts keep billing hourly and get squeezed. That''s the 10–20
      year view he says became unmistakable from this one experiment.'
  editorial: The conclusion that 'professionals become insurers' matters more than
    the AI passing the exam. Even with a self-built AI going 10-for-10 on the SCAQ,
    it cannot sign off on a client's tax advice and bear liability — sharply drawing
    the line between what automation reaches and where humans remain. The view that
    fees shift from research cost to a liability-insurance premium is a persuasive
    redefinition of professional value. That hybrid search plus HyDE plus reranking
    lifted 52 to the 70s is also a clean example of RAG design deciding the outcome.
  headerImage: /images/hwbut4oUyN8/header.png
  heroImage: /images/hwbut4oUyN8/header.png
---

## ハイライト

- [00:00] 投稿者の自作AIエージェントがシンガポール公認会計士試験 (SCAQ) の過去問で10回受験10回合格。平均70点台、人間3時間のところを1時間以内で完答。
- [00:26] 元はニュージーランドの試験で合格させた話を予定していたが著作権・規約がグレーになるため断念。シンガポールはSCAQの過去問と模範解答を公的機関がPDFで公開しているためクリーンに話せる、と切り替え。
- [01:35] SCAQは財務報告・監査・税務・ガバナンスの4科目。すべてオンライン受験 (Webカメラ監視) という真面目な試験。
- [03:52] AIの仕組みは3層構成: ベクトル検索＋キーワード検索のハイブリッド (条文番号や法令用語はキーワードが強い)、HyDE (仮の答えで検索)、リランキング (30件取って別モデルで5件に絞り込み)。
- [04:35] この3工夫を入れる前は平均52点で合格ライン50点ギリギリ。入れた途端70点台に跳ね上がり、ギリギリ合格から余裕合格へ。
- [05:02] 弱点も人間に似ていた。図表問題で5〜10点下落 (マルチモーダル未成熟)、シンガポール消費税8→9%引き上げの税制改正混同、監査が苦手で財務 (ZAM) は得意、という傾向。
- [05:34] 本題はここから。AIが士業になった、という話ではない。試験に受かっても、AIが顧客の税務相談に署名して責任を取れるわけではない。
- [08:04] 結論: 顧客が士業に払うお金の意味が『調査費・分析費』から『保険料』に変わる。報酬主軸が賠償責任引受料へ。AI使いの士業が件数10倍×保険料ベースで回し、抵抗組は時間単価で徐々に苦しくなる。

## セクション

### 自作AIがSCAQで10戦10勝 — 過程の検証

- 時刻: 00:00

海外Yパパラジオの投稿者は、自分で組んだAIエージェントにシンガポール公認会計士試験 (SCAQ) の過去問を解かせ、10回受験して10回合格させた。本来はニュージーランドの試験で合格させた話を予定していたが、試験問題・模範解答の出所が著作権・試験機関規約上グレーになるため断念。シンガポールは過去問と模範解答を公的機関がPDFで堂々と公開しているのでクリーンに話せる、と動画テーマを切り替えている。

SCAQは財務報告・監査・税務・ガバナンスの4科目をWebカメラ監視下のオンラインで受験する真面目な試験で、いわゆる『出題予想』で押し切れる試験ではない。それを自作AIに通させた、というのが本動画の検証対象だ。

### AIの仕組み — ハイブリッド検索・HyDE・リランキングの3層

- 時刻: 03:52

AIの実装は3つの工夫を組み合わせている。第1にハイブリッド検索。ベクトル検索とキーワード検索を並行に走らせて結果をマージする。条文番号や法令用語のような語はキーワード検索の方が強いため、片方だけでは性能が出ない。

第2にHyDE (Hypothetical Document Embeddings)。質問をそのまま検索するのでなく、AIに一度『仮の答え』を作らせ、その仮答案で検索する。資料の中では質問文より答え風の文の方が、正解に近い場所にあるからだ。第3にリランキング。広く30件取得し、別の専門モデルで本当に必要な5件に絞り込む2段階方式。この3工夫を入れる前の単純検索だけのときは平均52点でラインギリギリだったが、入れた途端に70点台へ跳ね上がった。10回受験して10回合格、人間が3時間かけるところAIは1時間以内で完答する。弱点も興味深く、図表問題は5〜10点下落 (マルチモーダル未成熟)、シンガポール消費税8→9%引き上げの税制改正で混同、監査が苦手で財務が得意 — 人間の合格者の傾向と似ているのが面白い点だ。

### 本題 — 士業ビジネスは『調査費』から『保険料』へ

- 時刻: 05:34

投稿者はここからが本題だ、と言う。これはAIが公認会計士になったという話ではない。試験に受かったところで、AIが顧客の税務相談に乗って書類に署名し、賠償責任まで取れるわけではない。

投稿者の本当の主張は別軸にある。公認会計士・弁護士の戦うゾーンが変わる。顧客が士業に払うお金の意味が『調査費・分析費』から『保険料』に変わるのだ。今でも士業賠償責任保険は存在するが、おまけの位置づけで、報酬の主軸はプロフェッショナルサービス料だ。これが逆転して、報酬の主軸が賠償責任引受料になる。士業はAIと人間のチェック役＋責任引受人として、保険料ベースのビジネスモデルへ移行する。AIを早く受け入れた士業は件数を10倍に増やして保険料ベースで回し、抵抗組は時間単価で徐々に苦しくなる、というのが10年後・20年後の景色になる、と動画は締めくくる。

## 編集部の視点

『士業は保険屋になる』という結論が、AI合格そのものより重要だ。自作AIがSCAQに10戦10勝しても、顧客の税務相談に署名して責任を取れるわけではない——ここに自動化が届く範囲と人間が残る範囲の境界が鮮明に出る。報酬の意味が調査費から賠償責任の保険料へ移るという見立ては、専門職の価値の再定義として説得力がある。ハイブリッド検索＋HyDE＋リランキングで52点が70点台に跳ねた事実は、RAG設計の工夫が成果を決めることの好例でもある。
