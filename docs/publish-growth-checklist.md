# Publish And Growth Checklist

## Current Technical Baseline

- 独自ドメインは `https://www.claude-daily.com`
- Astro 側の `site` は独自ドメインに設定済み
- `CNAME` は `site/public/CNAME` で管理
- canonical / OGP / Twitter Card / JSON-LD をレイアウトで出力
- `robots.txt` と `sitemap.xml` を Astro で生成
- GA4 は `PUBLIC_GA_MEASUREMENT_ID` を設定すれば有効化できる
- `IndexNow` は GitHub Pages デプロイ完了後に自動送信する

## Immediate Launch Tasks

1. GitHub Pages の DNS と HTTPS を安定化する
2. Google Search Console に `https://www.claude-daily.com/` を登録する
3. `sitemap.xml` を Search Console に送信する
4. GA4 プロパティを作り、`PUBLIC_GA_MEASUREMENT_ID` を GitHub Repository Variables へ設定する
5. Bing Webmaster Tools にも同じサイトマップを送信する
6. `IndexNow` の自動送信が GitHub Actions で成功していることを確認する

## GitHub Variables

- `PUBLIC_GA_MEASUREMENT_ID`
- `PUBLIC_GOOGLE_SITE_VERIFICATION`

GitHub の設定場所:

- `Repository Settings > Secrets and variables > Actions > Variables`

## Content SEO Tasks

- トップページタイトルと説明文を定期的に見直す
- 記事タイトルは検索語を意識しつつ長すぎない形にする
- `keyPhrases` は検索ニーズに沿った語を優先する
- 記事冒頭の TL;DR で「この記事で分かること」を明確にする
- 元動画タイトルをそのまま使いすぎず、日本語要約として意味が通る見出しに寄せる

## Distribution Tasks

- X で毎日の更新を固定フォーマットで投稿する
- note / Zenn / はてなブログに週次まとめを出す
- 「今日の Claude 動画 3 本」形式の短い再配布導線を作る
- Reddit / Hacker News 向けではなく、日本語の AI コミュニティ向け導線を優先する

## Metrics To Watch

- Search Console の表示回数
- Search Console のクリック数
- 上位クエリ
- GA4 のランディングページ別セッション
- 記事別の平均エンゲージメント時間
- OGP 経由の流入が多い記事の傾向

## Notes

- `preview-thumbnails` は `noindex` にする
- DNS が安定するまでは Search Console の登録先 URL を `www` に統一する
- 将来 feed が必要なら `rss.xml` の追加を検討する
- 本番ビルドで GA4 と Search Console の meta を出すには `deploy.yml` から GitHub Variables を渡す必要がある
- `IndexNow` 用キーは公開情報なので、現在はルート配置の `.txt` ファイルと `deploy.yml` で管理している
