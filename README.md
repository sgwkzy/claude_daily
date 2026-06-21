# Claude Daily

Claude / Claude Code / Anthropic / MCP / AIエージェント に関する YouTube 動画を毎日自動収集し、字幕から日本語のスライド風記事を生成して静的サイト「Claude Daily」に蓄積するシステムです。バッチは字幕を起点に記事 Markdown と画像アセットを生成し、GitHub Actions で 1 日 3 回の定期実行を想定しています。

## ディレクトリ構成

```text
claude-daily/
├── batch/                  # Python バッチ
├── site/                   # Astro 静的サイト
├── .github/workflows/      # GitHub Actions
├── .env.example
└── README.md
```

## 前提環境

- Windows 11 + PowerShell 7
- Python 3.13 以上
- Node.js 22 以上
- `ffmpeg` が PATH に通っていること
- `yt-dlp` が利用可能であること

Node.js を手動で PATH へ追加する場合の例:

```powershell
$env:Path += ';C:\Program Files\nodejs'
node --version
npm --version
```

## セットアップ

```powershell
cd F:\Work\claude-daily
Copy-Item .env.example .env
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r .\batch\requirements.txt
cd .\site
npm install
cd ..
```

`.env` に以下を設定してください。

- `YOUTUBE_API_KEY`
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`

字幕取得が `youtube_transcript_api` の `IpBlocked` / `429` に当たる環境では、任意で次も使えます。

- `YTDLP_COOKIES_FROM_BROWSER`
- `YTDLP_COOKIES_PATH`

サイト公開時に任意で使う公開向け変数:

- `PUBLIC_GA_MEASUREMENT_ID`
- `PUBLIC_GOOGLE_SITE_VERIFICATION`

GitHub Pages の本番ビルドで使う場合は、`Repository Settings > Secrets and variables > Actions > Variables` に同名で設定してください。

## 実行方法

ドライラン:

```powershell
cd F:\Work\claude-daily
. .\.venv\Scripts\Activate.ps1
python .\batch\main.py --dry-run
```

1 本だけ実行:

```powershell
python .\batch\main.py --limit 1
```

既定のサムネイル生成:

```powershell
python .\batch\main.py --limit 1
```

既定では `source-explainer` 方針で `16:9` の `header.png` を生成します。比較したい場合のみ `--thumbnail-directions` で複数方針を指定できます。

Pytest:

```powershell
python -m pytest
```

Astro 開発サーバー:

```powershell
cd F:\Work\claude-daily\site
npm run dev
```

## 実装メモ

- `--dry-run` では API 呼び出しを行わず、ダミー動画・ダミー字幕・ダミー画像でパイプラインを最後まで通します。
- 字幕取得は `youtube_transcript_api` を優先し、`IpBlocked` などで失敗した場合は `yt-dlp` の字幕取得へフォールバックします。
- 字幕なし、動画ダウンロード失敗、画像生成失敗は該当動画をスキップまたはサムネイルへフォールバックし、全体処理は継続します。
- 実行ログは `batch/tmp/batch.log` に追記され、字幕取得経路と失敗理由の確認に使えます。
- 記事フロントマターの構造と Astro Content Collections の zod スキーマは同じ項目を表現しています。
- 画像生成は OpenAI `gpt-image-1` の image edit API を利用します。
- サムネイル仕様と運用方針は [docs/thumbnail-directions.md](/F:/Work/claude-daily/docs/thumbnail-directions.md) を参照してください。

## 多言語対応（英語デフォルト / 日本語 `/jp/`）

サイトは英語をデフォルト（ルート `/`）、日本語を `/jp/` プレフィックスで配信するバイリンガル構成です。

- ロケール判定・UI 文言・パス変換は `site/src/i18n/ui.ts` に集約しています（`/jp/` 始まりを `ja` と判定）。
- 記事の表示テキストはフロントマターの `en` ブロック（英語）とトップレベル（日本語・原文）で持ち、`site/src/lib/articles.ts` の `localizeArticleData` が解決します。`en` が無い記事は日本語へフォールバックします。
- バッチは要約後に `batch/translator.py` で英訳し、ヘッダー画像は `header.png`（英語）と `header.ja.png`（日本語）を AI で個別生成します。
- 言語切り替えはヘッダーのトグル（選択を `localStorage` に保存）と、初回訪問時の `navigator.language` による自動誘導（ルート閲覧時に `ja` ブラウザのみ `/jp/` へ）で行います。
- 各ページに hreflang 相互リンク（en / ja / x-default=en）を出力し、`sitemap.xml` は両言語 URL を、RSS は `rss.xml`（英語）と `jp/rss.xml`（日本語）を生成します。

既存記事へ英語ブロックと英語ヘッダー画像を後付けするバックフィル:

```powershell
python .\batch\backfill_translations.py --limit 5
```

`--dry-run` でプレースホルダ動作確認、`en` 済み記事はスキップ（冪等）。`/jp/**` 公開後は Search Console / IndexNow へ再送信して再インデックスしてください。

## GitHub Actions

- `batch.yml`: 1 日 3 回 cron 実行し、生成された記事と画像をコミットします。
- `deploy.yml`: `site/**` の push をトリガに Astro をビルドし、GitHub Pages にデプロイします。

## 公開と集客の基本設定

- `site/src/layouts/BaseLayout.astro` で canonical / OGP / Twitter Card / JSON-LD / GA4 を出力します。
- `site/src/pages/robots.txt.ts` で `robots.txt` を生成します。
- `site/src/pages/sitemap.xml.ts` で `sitemap.xml` を生成します。
- `site/public/b32626ab-6fcd-48b6-a66e-edb27a8f8b56.txt` を `IndexNow` の所有確認キーとして公開します。
- Google Analytics 4 を使う場合は `PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX` を設定します。
- Search Console を使う場合は `PUBLIC_GOOGLE_SITE_VERIFICATION` を設定するか、DNS レコードで所有権確認を行います。
- GitHub Pages 本番ビルドでは `.github/workflows/deploy.yml` から GitHub Actions Variables を環境変数として渡します。
- GitHub Pages デプロイ後は `.github/workflows/deploy.yml` から `IndexNow` に公開 URL 一覧を自動送信します。
