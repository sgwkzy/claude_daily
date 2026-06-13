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
- 字幕なし、動画ダウンロード失敗、画像生成失敗は該当動画をスキップまたはサムネイルへフォールバックし、全体処理は継続します。
- 記事フロントマターの構造と Astro Content Collections の zod スキーマは同じ項目を表現しています。
- 画像生成は OpenAI `gpt-image-1` の image edit API を利用します。
- サムネイル仕様と運用方針は [docs/thumbnail-directions.md](/F:/Work/claude-daily/docs/thumbnail-directions.md) を参照してください。

## GitHub Actions

- `batch.yml`: 1 日 3 回 cron 実行し、生成された記事と画像をコミットします。
- `deploy.yml`: `site/**` の push をトリガに Astro をビルドし、GitHub Pages にデプロイします。
