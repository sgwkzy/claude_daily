# Thumbnail Specification

## Overview

Claude Daily のヘッダーは、記事一覧と記事ページの両方で一貫した見え方になることを目的に、`editorial-rebuild` 方針を標準採用する。

この方針では、元動画サムネイルをそのまま土台にせず、記事内容に合わせて背景・構図・タイポグラフィをまとめて再生成する。優先するのは次の 3 点。

- 元動画のトピックがすぐ分かる
- 記事の要点が 1 秒で伝わる
- 複数記事を並べたときに統一感が出る

## Final Direction

採用方針は `Editorial Rebuild`。

### Visual Rules

- 左に強い日本語見出し、右に主ビジュアルを置く
- 小さなカテゴリチップを 1 つ置く
- 補足要素は 2 から 3 個まで
- warm beige / coral / charcoal を軸にした上品な editorial explainer にする
- 画像内に `Claude Daily` のような媒体ロゴは基本的に入れない
- 騒がしい YouTube サムネ風の矢印・丸囲み・過剰な煽りは避ける

### Text Rules

- 見出しは短く、一覧で読める長さにする
- 煽りより要約を優先する
- 記事本文で扱っていない論点は画像に書かない

## Fixed Output Format

### Aspect Ratio

- すべてのサムネイルは `16:9`

### Output Size

- 標準出力サイズは `1672 x 941`

### File Format

- 標準出力ファイルは `header.png`

### Safe Area

- 文字や主役は端に寄せすぎない
- 後段の `object-cover` 表示で多少トリミングされても成立する中央寄せ構図を基本にする

## Site Usage

### Top Page

- 一覧カードでは 16:9 サムネイルを共通比率で表示する
- カード本文は高さ上限を持たせる
- タイトルと要点は行数で制御する
- キーワードチップは 3 件まで

### Article Page

- タイトルは画像から分離して上部に独立表示する
- `Takeaways` と `Source` はタイトル近くに配置する
- ヒーロー画像は記事上部で大きく表示する
- 記事ページでは一覧より左右余白を広く取る

## Generation Inputs

生成時には次の情報を使う。

- 動画タイトル
- 日本語記事タイトル
- チャンネル名
- 記事の key phrases
- 記事の bullet points
- セクション見出し

## Batch Logic

### Default Behavior

- 既定の生成方針は `editorial-rebuild`
- 出力は `header.png`
- フロントマターの `headerImage` と `heroImage` は、初期状態では同じ画像を指す

### Normalization

- OpenAI 画像生成結果は保存前に `1672 x 941` へ正規化する
- 比率が異なる画像は中央基準で整形する

### Dry Run

- `--dry-run` ではダミー画像を生成する
- 生成フローと保存先だけは本番と同じ扱いにする

## Optional Comparison Mode

比較検証が必要な場合のみ、複数方針を使う。

- `editorial-rebuild`
- `source-first`
- `source-explainer`
- `frame-summary`
- `reconstructed-concept`

通常運用では比較用途のみ。既定運用は `editorial-rebuild` のみ。

## Maintenance Notes

- 比率を変更する場合は、画像生成プロンプト、保存時の正規化、一覧カード、記事ヒーローを同時に見直す
- 画像内の文字量を増やしすぎると、トップカードで見切れやすくなる
- 記事ページのヒーロー画像だけ別デザインにしたい場合は `heroImage` を個別に設定できる

## Related Files

- `batch/header_image.py`
- `batch/main.py`
- `batch/article_writer.py`
- `batch/models.py`
- `site/src/components/ArticleCard.astro`
- `site/src/pages/articles/[slug].astro`
- `site/src/content/config.ts`
