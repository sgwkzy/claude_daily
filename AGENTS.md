# Claude Daily 開発環境

Claude Daily（https://www.claude-daily.com）の開発専用環境。本体はここ `F:\ClaudeWorks\DevelopClaudeDaily`（旧 `F:\Work\claude-daily` はジャンクションで互換維持）。

## 構成

- `batch/` — 記事生成パイプライン（Python）。動画取得→字幕→要約→翻訳→ヘッダー画像→記事書き出し
- `site/` — Astro サイト。`npm run dev`（port 4321）/ `npm run build`
- `serve/` — 配信設定
- `docs/` — 運用ドキュメント
- `_scratch_*` — 日次運用の使い捨てスクリプト・中間データ（消さない）

## 環境の注意

- Claude Code の PowerShell ツールはプロファイル未読込で起動するため `node`/`npm` が PATH に無い。コマンド先頭に `. $PROFILE; $env:Path = "$env:APPDATA\npm;$env:Path"` を付ける
- テスト: `python -m pytest`（pytest.ini あり、testpaths=batch/tests）
- ANTHROPIC_API_KEY / OPENAI_API_KEY は不要（ローカル + Codex image_gen で完結）

## 役割分担

- 開発（機能追加・設計変更）: この環境
- 日次運用（記事更新・公開）: `F:\ClaudeWorks\OperationClaudeDaily` + スキル `claude-daily-update`
