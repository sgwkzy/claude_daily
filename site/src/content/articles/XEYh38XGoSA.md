---
videoId: XEYh38XGoSA
title: I Switched Back to Obsidian (because of AI)
slug: notionからobsidianへ回帰した理由ローカルaiエージェント時代のノート環境選び-xeyh38xgosa
articleTitle: NotionからObsidianへ回帰した理由：ローカルAIエージェント時代のノート環境選び
seoTitle: NotionからObsidianへ回帰した理由：ローカルAIエージェント時代のノート環境選び
summary: 以前『Obsidianからノーションへ移行した理由』という動画を出していた本人が、メインのノート・プロジェクト管理ツールをNotionからObsidianへ戻したと告白する。
channel: Christian Lempa
channelId: UCZNhwA1B5YqiY1nLzmM0ZRg
publishedAt: '2026-07-02T14:00:34Z'
fetchedAt: '2026-07-04T18:06:42.180866Z'
originalThumbnail: https://i.ytimg.com/vi/XEYh38XGoSA/maxresdefault.jpg
headerImage: /images/XEYh38XGoSA/header.ja.png
heroImage: /images/XEYh38XGoSA/header.ja.png
viewCount: 11223
durationSec: 1765
sourceLanguage: en
matchedKeywords:
- AIエージェント
proposedByLLM: false
keyPhrases:
- Obsidian
- Notion
- AIエージェント
- MCP
- ローカルツール
- ホームラボ
bulletPoints:
- time: 0
  text: 以前『Obsidianからノーションへ移行した理由』という動画を出していた本人が、メインのノート・プロジェクト管理ツールをNotionからObsidianへ戻したと告白する。
- time: 21
  text: きっかけは、ターミナルベースのAIエージェントやローカルツールを使う頻度が大きく増えたというワークフローの変化だった。
- time: 33
  text: NotionやConfluence、ClickUp、Airtableのようなクラウドベースのツールは、自前のAIエージェントや既存ローカルツール、独自ワークフローを持ち込もうとすると急に扱いにくくなる。
- time: 54
  text: 大手プラットフォームは自社のAIアシスタントを独自のサブスクリプションと閉じたエコシステムの中で使わせようとする傾向があると指摘する。
- time: 66
  text: MCPサーバーやAPI、CLIアプリで技術的には連携できるものの、クラウド接続に依存し動作が遅く扱いにくいと感じている。
- time: 839
  text: スキル(ルールファイル)にサービス固有のデプロイ内容を重複させない、インフラはTerraformなどのコードで管理するといった具体的なガイドラインをAIエージェントに読ませる運用を紹介する。
- time: 1708
  text: データ・ツール・AIサブスクリプションを完全に自分でコントロールしたいなら、シンプルなMarkdownファイルとObsidianが最適だと結論づける。
sections:
- heading: ワークフローの変化が引き起こしたツール回帰
  time: 0
  body: 'かつて『Obsidianからノーションへ移行した理由』という動画を出していた発信者が、メインのノート・プロジェクト管理ツールをNotionからObsidianへ戻したと告白する。きっかけは、ターミナルベースのAIエージェントやローカルツールを使う頻度が大きく増えたというワークフローの変化だった。


    NotionやConfluence、ClickUp、Airtableといったクラウドベースの開発者向けツールはそのままでは非常によく機能するが、自前のAIエージェントや既存のローカルツール、独自ワークフローを持ち込もうとした途端に事情が複雑になる。これらの大手プラットフォームはクラウド前提で、自社のAIアシスタントを独自サブスクリプションと閉じたエコシステムの中で使わせようとする傾向があるという。'
- heading: MCPやAPIでの連携はあっても『扱いにくい』という現実
  time: 66
  body: 技術的にはMCPサーバーやAPI、CLIアプリを介してこれらのクラウドツールと連携することは可能だが、依然としてクラウド接続に依存し、動作が遅く、ポータブルでないと感じるという。そのためローカル・オープンなツールへワークフローを移す決断をし、単純なMarkdownファイルを使うObsidianがその選択にちょうど合致したと説明する。
- heading: スキル(ルールファイル)でAIエージェントに運用方針を教え込む
  time: 839
  body: '具体的な運用として、サービス固有のデプロイ内容をスキル(ルールファイル)内で重複させない、インフラはTerraformやOpenTofuのようなコードで管理する運用を優先する、GitLabやDNS、Prometheusなど重要リポジトリの扱い方を明記する、といったガイドラインをAIエージェントに読ませる方法を紹介する。


    こうしたルールを整備しておくことで、ターミナルからのスラッシュコマンド一つでオンボーディング計画やチェックリストを生成させることができる。最終的には、データ・ツール・AIサブスクリプションを完全に自分でコントロールしたいなら、シンプルなMarkdownファイルとObsidianが最良の選択だと結論づけている。'
editorial: この事例が示すのは、AIエージェントの普及がノートアプリ選定の力学そのものを変えつつあるという点だ。従来は『使いやすさ』や『チーム連携のしやすさ』で選ばれていたクラウド型ツールが、今や『自分のAIエージェントを自由に持ち込めるか』という新しい評価軸で見直されている。大手プラットフォームが自社AIアシスタントを閉じたエコシステムに囲い込もうとする動きは、短期的にはユーザー体験の向上に見えても、ローカルAIエージェントを重視するパワーユーザーにとってはむしろ離脱要因になり得る。Markdownという最も基本的なフォーマットへの回帰は、AIエージェント時代における『ポータビリティ』の価値を再評価する動きとして興味深い。
en:
  articleTitle: 'Why I Went Back to Obsidian From Notion: Choosing a Notes Setup for
    the Local-AI-Agent Era'
  seoTitle: 'Why I Went Back to Obsidian From Notion: Choosing a Notes Setup'
  summary: The same creator who once published a video on 'why I switched from Obsidian
    to Notion' admits he's moved his main…
  keyPhrases:
  - Obsidian
  - Notion
  - AI agents
  - MCP
  - local tools
  - home lab
  bulletPoints:
  - time: 0
    text: The same creator who once published a video on 'why I switched from Obsidian
      to Notion' admits he's moved his main notes and project-management workflow
      back to Obsidian.
  - time: 21
    text: 'The trigger was a workflow shift: using terminal-based AI agents and local
      tools far more often than before.'
  - time: 33
    text: Cloud tools like Notion, Confluence, ClickUp, and Airtable work great out
      of the box -- until you try bringing in your own AI agents, existing local tools,
      or custom workflows.
  - time: 54
    text: He points out that major platforms tend to push you toward using their own
      AI assistant, tied to their own subscription and locked inside their own ecosystem.
  - time: 66
    text: Technically you can connect via MCP servers, APIs, or CLI apps, but it still
      feels clunky, cloud-dependent, and slow.
  - time: 839
    text: He shows concrete guidelines fed to the AI agent as a 'skill' file -- don't
      duplicate service-specific deployment details, prefer managing infrastructure
      as code via Terraform, and so on.
  - time: 1708
    text: 'His conclusion: if you want full control over your data, tools, and AI
      subscriptions, simple markdown files and Obsidian are the best fit.'
  sections:
  - heading: A Workflow Shift Triggers a Return to an Old Tool
    time: 0
    body: 'The creator who once made a video explaining why he moved from Obsidian
      to Notion now admits he''s switched his main notes and project-management tool
      back to Obsidian. The trigger was a shift in workflow -- using terminal-based
      AI agents and local tools far more than before.


      Cloud-based developer tools like Notion, Confluence, ClickUp, and Airtable work
      great out of the box, but the moment you try to bring in your own AI agents,
      existing local tools, or custom workflows, things get complicated. These major
      platforms tend to push users toward their own AI assistant, tied to a proprietary
      subscription and locked inside a closed ecosystem.'
  - heading: MCP and APIs Connect, But It Still Feels Clunky
    time: 66
    body: Technically, MCP servers, APIs, and CLI apps can connect these cloud tools
      to your own AI setup, but it still feels dependent on a cloud connection, slow,
      and not portable. That's what drove the decision to move workflows toward local,
      open tools -- and Obsidian, which just uses plain markdown files, fit that shift
      naturally.
  - heading: Teaching an AI Agent Operating Rules via 'Skill' Files
    time: 839
    body: 'In practice, that means writing guidelines into a ''skill'' file that the
      AI agent reads: don''t duplicate service-specific deployment details inside
      the skill itself, prefer managing infrastructure as code via Terraform or OpenTofu
      over ad hoc runtime changes, and document how key repositories like GitLab,
      DNS, and Prometheus should be handled.


      With those rules in place, a single slash command from the terminal can generate
      an onboarding plan and checklist. His conclusion: for anyone who wants full
      control over their data, tools, and AI subscriptions, simple markdown files
      paired with Obsidian remain the best choice.'
  editorial: This case shows how the rise of AI agents is reshaping the calculus behind
    choosing a notes app. Cloud tools once won on ease of use and team collaboration;
    now they're being re-evaluated against a new criterion -- can you freely bring
    your own AI agent into the workflow? Major platforms locking their own AI assistant
    into a closed ecosystem may look like a UX win short-term, but for power users
    leaning on local AI agents, it's increasingly a reason to leave. The return to
    plain markdown -- about as basic a format as exists -- is a notable reassessment
    of portability's value in the AI-agent era.
  headerImage: /images/XEYh38XGoSA/header.png
  heroImage: /images/XEYh38XGoSA/header.png
---

## ハイライト

- [00:00] 以前『Obsidianからノーションへ移行した理由』という動画を出していた本人が、メインのノート・プロジェクト管理ツールをNotionからObsidianへ戻したと告白する。
- [00:21] きっかけは、ターミナルベースのAIエージェントやローカルツールを使う頻度が大きく増えたというワークフローの変化だった。
- [00:33] NotionやConfluence、ClickUp、Airtableのようなクラウドベースのツールは、自前のAIエージェントや既存ローカルツール、独自ワークフローを持ち込もうとすると急に扱いにくくなる。
- [00:54] 大手プラットフォームは自社のAIアシスタントを独自のサブスクリプションと閉じたエコシステムの中で使わせようとする傾向があると指摘する。
- [01:06] MCPサーバーやAPI、CLIアプリで技術的には連携できるものの、クラウド接続に依存し動作が遅く扱いにくいと感じている。
- [13:59] スキル(ルールファイル)にサービス固有のデプロイ内容を重複させない、インフラはTerraformなどのコードで管理するといった具体的なガイドラインをAIエージェントに読ませる運用を紹介する。
- [28:28] データ・ツール・AIサブスクリプションを完全に自分でコントロールしたいなら、シンプルなMarkdownファイルとObsidianが最適だと結論づける。

## セクション

### ワークフローの変化が引き起こしたツール回帰

- 時刻: 00:00

かつて『Obsidianからノーションへ移行した理由』という動画を出していた発信者が、メインのノート・プロジェクト管理ツールをNotionからObsidianへ戻したと告白する。きっかけは、ターミナルベースのAIエージェントやローカルツールを使う頻度が大きく増えたというワークフローの変化だった。

NotionやConfluence、ClickUp、Airtableといったクラウドベースの開発者向けツールはそのままでは非常によく機能するが、自前のAIエージェントや既存のローカルツール、独自ワークフローを持ち込もうとした途端に事情が複雑になる。これらの大手プラットフォームはクラウド前提で、自社のAIアシスタントを独自サブスクリプションと閉じたエコシステムの中で使わせようとする傾向があるという。

### MCPやAPIでの連携はあっても『扱いにくい』という現実

- 時刻: 01:06

技術的にはMCPサーバーやAPI、CLIアプリを介してこれらのクラウドツールと連携することは可能だが、依然としてクラウド接続に依存し、動作が遅く、ポータブルでないと感じるという。そのためローカル・オープンなツールへワークフローを移す決断をし、単純なMarkdownファイルを使うObsidianがその選択にちょうど合致したと説明する。

### スキル(ルールファイル)でAIエージェントに運用方針を教え込む

- 時刻: 13:59

具体的な運用として、サービス固有のデプロイ内容をスキル(ルールファイル)内で重複させない、インフラはTerraformやOpenTofuのようなコードで管理する運用を優先する、GitLabやDNS、Prometheusなど重要リポジトリの扱い方を明記する、といったガイドラインをAIエージェントに読ませる方法を紹介する。

こうしたルールを整備しておくことで、ターミナルからのスラッシュコマンド一つでオンボーディング計画やチェックリストを生成させることができる。最終的には、データ・ツール・AIサブスクリプションを完全に自分でコントロールしたいなら、シンプルなMarkdownファイルとObsidianが最良の選択だと結論づけている。

## 編集部の視点

この事例が示すのは、AIエージェントの普及がノートアプリ選定の力学そのものを変えつつあるという点だ。従来は『使いやすさ』や『チーム連携のしやすさ』で選ばれていたクラウド型ツールが、今や『自分のAIエージェントを自由に持ち込めるか』という新しい評価軸で見直されている。大手プラットフォームが自社AIアシスタントを閉じたエコシステムに囲い込もうとする動きは、短期的にはユーザー体験の向上に見えても、ローカルAIエージェントを重視するパワーユーザーにとってはむしろ離脱要因になり得る。Markdownという最も基本的なフォーマットへの回帰は、AIエージェント時代における『ポータビリティ』の価値を再評価する動きとして興味深い。
