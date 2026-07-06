---
videoId: -X600LTVjuU
title: 'MCP explained for beginners '
slug: 初心者向けmcp解説なぜaiは賢くてもメールひとつ送れないのか--x600ltvjuu
articleTitle: 初心者向けMCP解説：なぜAIは賢くてもメールひとつ送れないのか
seoTitle: 初心者向けMCP解説：なぜAIは賢くてもメールひとつ送れないのか
summary: 世界最強のAIモデルを持っていても、Gmailへのアクセスやカレンダー更新、Jiraチケット作成、データベースへの問い合わせはできないという問いから話が始まる。
channel: Withmesravani_
channelId: UCYed9SRwNY_EU1bwDH54m6A
publishedAt: '2026-07-04T12:37:41Z'
fetchedAt: '2026-07-06T11:50:40.299596Z'
originalThumbnail: https://i.ytimg.com/vi/-X600LTVjuU/maxresdefault.jpg
headerImage: /images/-X600LTVjuU/header.ja.png
heroImage: /images/-X600LTVjuU/header.ja.png
viewCount: 4904
durationSec: 1204
sourceLanguage: te
matchedKeywords:
- MCP
proposedByLLM: false
keyPhrases:
- MCP
- AI基礎解説
- LLM
- RAG
- ツール連携
- エンタープライズAI
bulletPoints:
- time: 16
  text: 世界最強のAIモデルを持っていても、Gmailへのアクセスやカレンダー更新、Jiraチケット作成、データベースへの問い合わせはできないという問いから話が始まる。
- time: 37
  text: ChatGPTやClaude、Geminiのようなツールは知識・推論・会話能力はあっても、それ単体では現実世界のアプリケーションを直接操作できない『孤立した』存在だと指摘する。
- time: 65
  text: 2023年のChatGPTブームで企業はAIによる全自動化に興奮したが、実際の導入では『AIが本番環境の監視ツールにアクセスできない』という現実に直面した。
- time: 547
  text: MCPのスキーマはツールの使い方を定義する『契約』であり、送信者やフィルタ条件などの入力パラメータ・型・必須かどうかを明示する。
- time: 618
  text: 従来のAPIはドキュメントを人間が読んで理解する必要があるが、MCPのスキーマはAIに対して自己記述的であり、AIがハードコードされた知識なしに動的にツールの使い方を発見できる。
- time: 1127
  text: 今日のAIは質問に答えるだけだが、明日のAIはメールを書き、宛先を検証し、正しい文書を添付して送信し、その活動をCRMに記録するところまで自律的にこなすようになる。
- time: 1154
  text: LLMがAIに言語理解と推論を与え、RAGが知識アクセスを与え、MCPがツールとシステムへのアクセスを与える。この3つを組み合わせて初めて強力なエンタープライズAIシステムが作れると総括する。
sections:
- heading: AIが賢くても『孤立』している理由
  time: 16
  body: '世界最強のAIモデル——GPT-5、Claude、Geminiのどれでも良い——を持っていたとして、そのAIはあなたのGmailにアクセスし、カレンダーを更新し、Jiraチケットを作成し、データベースにクエリを実行できるだろうか？答えはノーだ。AIが知的であることと、現実世界のシステムと通信できることは全く別問題だからだという。


    ChatGPTは賢いが孤立している。Claude、Geminiのようなツールも同様に、知識・推論・会話能力はあってもどんなアプリケーションも直接開くことができない。2023年のChatGPTブームで企業はAIによる全自動化に沸き立ったが、実際に導入を始めると『社員が昨日の本番障害についてAIに聞いても、AIは本番監視ツールへのアクセス権を持たないため答えられない』という現実に直面した。'
- heading: スキーマという『自己記述的な契約』
  time: 547
  body: 'MCPの核心はスキーマにある。例えば『メール検索』というツール名だけでは不十分で、送信者は誰か、日付範囲はどうかといった入力（プロパティ）が必要になる。スキーマはツールの使い方を定義する契約であり、パラメータの型（文字列・真偽値・整数など）や必須かどうかまで明示する。


    これが従来のAPIとの決定的な違いだ。APIではドキュメントを人間が読んで理解する必要があるが、MCPのスキーマはAIに対して自己記述的であり、AIはハードコードされた知識なしに実行時に動的にツールの使い方を発見できる。'
- heading: LLM×RAG×MCPで完成する自律型AI
  time: 1127
  body: '今日のAIは質問に答えるだけだが、明日のAIはメールを書き、宛先を検証し、正しい文書を添付して送信し、その活動をCRMに記録するところまで自律的にこなすようになるという。この未来を実現するには、安全で標準化されたプロトコルが不可欠だと強調する。


    最後に3つの技術の役割を整理する。LLMがAIに言語理解と推論を与え、RAGが知識へのアクセスを与え、そしてMCPがツールとシステムへのアクセスを与える。この3つを組み合わせて初めて、強力なエンタープライズAIシステムを構築できるとまとめている。'
editorial: この解説の価値は、MCPを『新しい技術トレンド』としてではなく『AIの孤立問題』という具体的な課題に対する解決策として提示している点にある。ChatGPTブーム初期に多くの企業が『AI導入すれば自動化できる』と期待し、その後『AIは現実のシステムにアクセスできない』という壁に直面したという指摘は、多くの現場が実際に経験した失望と重なる。スキーマの自己記述性という技術的な特徴を、非エンジニア層にも伝わる言葉で説明している点も評価できる。LLM・RAG・MCPという3層構造の整理は、AIシステムを設計する際の実務的なチェックリストとしても機能するだろう。
en:
  articleTitle: 'MCP Explained for Beginners: Why a Genius AI Still Can''t Send One
    Email'
  seoTitle: 'MCP Explained for Beginners: Why a Genius AI Still Can''t Send On'
  summary: 'The video opens with a question: even with the world''s most powerful
    AI model, can it access your Gmail, update your…'
  keyPhrases:
  - MCP
  - AI fundamentals
  - LLM
  - RAG
  - tool integration
  - enterprise AI
  bulletPoints:
  - time: 16
    text: 'The video opens with a question: even with the world''s most powerful AI
      model, can it access your Gmail, update your calendar, create Jira tickets,
      or query your database?'
  - time: 37
    text: Tools like ChatGPT, Claude, and Gemini have knowledge, reasoning, and conversation
      ability, but on their own they're described as 'isolated' -- unable to directly
      operate real-world applications.
  - time: 65
    text: 'During the 2023 ChatGPT boom, companies got excited about full automation,
      but real deployments hit a wall: AI couldn''t access production monitoring tools.'
  - time: 547
    text: An MCP schema is a 'contract' defining how a tool is used -- specifying
      input parameters like sender or filter conditions, their types, and whether
      they're required.
  - time: 618
    text: Traditional APIs require humans to read documentation, but MCP schemas are
      self-describing to the AI, letting it dynamically discover how to use a tool
      without hardcoded knowledge.
  - time: 1127
    text: Today's AI only answers questions; tomorrow's AI will autonomously write
      an email, verify the recipient, attach the correct document, send it, and log
      the activity in the CRM.
  - time: 1154
    text: LLMs give AI language understanding and reasoning, RAG gives it access to
      knowledge, and MCP gives it access to tools and systems -- combining all three
      is what builds powerful enterprise AI systems.
  sections:
  - heading: Why a Smart AI Is Still 'Isolated'
    time: 16
    body: 'Suppose you had the world''s most powerful AI model -- GPT-5, Claude, Gemini,
      whichever. Could it access your Gmail, update your calendar, create Jira tickets,
      or run a database query? The answer is no, because being intelligent and being
      able to communicate with real-world systems are entirely separate problems.


      ChatGPT is smart but isolated. Tools like Claude and Gemini have the same limitation:
      knowledge, reasoning, and conversation ability, but no way to directly open
      any application. During the 2023 ChatGPT boom, companies got excited about full
      automation, but once real deployments started, reality set in -- an employee
      asking the AI about yesterday''s production issue got nothing, because the AI
      had no access to the production monitoring tools.'
  - heading: 'The Schema: A Self-Describing Contract'
    time: 547
    body: 'MCP''s core idea is the schema. A tool name like ''search emails'' isn''t
      enough on its own -- it needs inputs (properties) like who the sender is or
      what date range to search. The schema is the contract defining how a tool is
      used, spelling out parameter types (string, boolean, integer, etc.) and whether
      each is required.


      This is the decisive difference from traditional APIs. With an API, a human
      has to read the documentation. An MCP schema is self-describing to the AI, letting
      it dynamically discover how to use any tool at runtime without hardcoded knowledge.'
  - heading: 'LLM + RAG + MCP: The Recipe for Autonomous AI'
    time: 1127
    body: 'Today''s AI only answers questions, but tomorrow''s AI will autonomously
      write an email, verify the recipient, attach the correct document, send it,
      and log the activity in the CRM. Making that future possible requires a secure,
      standardized protocol.


      The video closes by summarizing the three-part stack: LLMs give AI language
      understanding and reasoning, RAG gives it access to knowledge, and MCP gives
      it access to tools and systems. Combining all three is what it takes to build
      a genuinely powerful enterprise AI system.'
  editorial: What makes this explainer valuable is framing MCP not as a trend but
    as a direct answer to AI's 'isolation problem.' The observation that early ChatGPT-boom
    companies expected instant automation and then hit the wall of 'AI can't touch
    our real systems' mirrors disappointment many teams actually experienced. Explaining
    schema self-description in accessible language, without assuming an engineering
    background, is also a strength. The LLM/RAG/MCP three-layer framing doubles as
    a practical checklist for anyone designing an AI system from scratch.
  headerImage: /images/-X600LTVjuU/header.png
  heroImage: /images/-X600LTVjuU/header.png
---

## ハイライト

- [00:16] 世界最強のAIモデルを持っていても、Gmailへのアクセスやカレンダー更新、Jiraチケット作成、データベースへの問い合わせはできないという問いから話が始まる。
- [00:37] ChatGPTやClaude、Geminiのようなツールは知識・推論・会話能力はあっても、それ単体では現実世界のアプリケーションを直接操作できない『孤立した』存在だと指摘する。
- [01:05] 2023年のChatGPTブームで企業はAIによる全自動化に興奮したが、実際の導入では『AIが本番環境の監視ツールにアクセスできない』という現実に直面した。
- [09:07] MCPのスキーマはツールの使い方を定義する『契約』であり、送信者やフィルタ条件などの入力パラメータ・型・必須かどうかを明示する。
- [10:18] 従来のAPIはドキュメントを人間が読んで理解する必要があるが、MCPのスキーマはAIに対して自己記述的であり、AIがハードコードされた知識なしに動的にツールの使い方を発見できる。
- [18:47] 今日のAIは質問に答えるだけだが、明日のAIはメールを書き、宛先を検証し、正しい文書を添付して送信し、その活動をCRMに記録するところまで自律的にこなすようになる。
- [19:14] LLMがAIに言語理解と推論を与え、RAGが知識アクセスを与え、MCPがツールとシステムへのアクセスを与える。この3つを組み合わせて初めて強力なエンタープライズAIシステムが作れると総括する。

## セクション

### AIが賢くても『孤立』している理由

- 時刻: 00:16

世界最強のAIモデル——GPT-5、Claude、Geminiのどれでも良い——を持っていたとして、そのAIはあなたのGmailにアクセスし、カレンダーを更新し、Jiraチケットを作成し、データベースにクエリを実行できるだろうか？答えはノーだ。AIが知的であることと、現実世界のシステムと通信できることは全く別問題だからだという。

ChatGPTは賢いが孤立している。Claude、Geminiのようなツールも同様に、知識・推論・会話能力はあってもどんなアプリケーションも直接開くことができない。2023年のChatGPTブームで企業はAIによる全自動化に沸き立ったが、実際に導入を始めると『社員が昨日の本番障害についてAIに聞いても、AIは本番監視ツールへのアクセス権を持たないため答えられない』という現実に直面した。

### スキーマという『自己記述的な契約』

- 時刻: 09:07

MCPの核心はスキーマにある。例えば『メール検索』というツール名だけでは不十分で、送信者は誰か、日付範囲はどうかといった入力（プロパティ）が必要になる。スキーマはツールの使い方を定義する契約であり、パラメータの型（文字列・真偽値・整数など）や必須かどうかまで明示する。

これが従来のAPIとの決定的な違いだ。APIではドキュメントを人間が読んで理解する必要があるが、MCPのスキーマはAIに対して自己記述的であり、AIはハードコードされた知識なしに実行時に動的にツールの使い方を発見できる。

### LLM×RAG×MCPで完成する自律型AI

- 時刻: 18:47

今日のAIは質問に答えるだけだが、明日のAIはメールを書き、宛先を検証し、正しい文書を添付して送信し、その活動をCRMに記録するところまで自律的にこなすようになるという。この未来を実現するには、安全で標準化されたプロトコルが不可欠だと強調する。

最後に3つの技術の役割を整理する。LLMがAIに言語理解と推論を与え、RAGが知識へのアクセスを与え、そしてMCPがツールとシステムへのアクセスを与える。この3つを組み合わせて初めて、強力なエンタープライズAIシステムを構築できるとまとめている。

## 編集部の視点

この解説の価値は、MCPを『新しい技術トレンド』としてではなく『AIの孤立問題』という具体的な課題に対する解決策として提示している点にある。ChatGPTブーム初期に多くの企業が『AI導入すれば自動化できる』と期待し、その後『AIは現実のシステムにアクセスできない』という壁に直面したという指摘は、多くの現場が実際に経験した失望と重なる。スキーマの自己記述性という技術的な特徴を、非エンジニア層にも伝わる言葉で説明している点も評価できる。LLM・RAG・MCPという3層構造の整理は、AIシステムを設計する際の実務的なチェックリストとしても機能するだろう。
