/**
 * 多言語対応の中心。英語を既定（ルート）、日本語を `/jp/` プレフィックスで配信する。
 *
 * - `getLocaleFromUrl` で現在ロケールを判定（`/jp/` 始まりなら ja）。
 * - `localePath` で「ロケール非依存のベースパス」から各ロケールの URL を組み立てる。
 * - `toBasePath` で現在の URL からベースパス（/jp を剥がした正準パス）を得る。
 * - `t(locale)` で UI 文言を引く（欠落時は英語へフォールバック）。
 *
 * 注: ここで返すパスは Astro の `base` を含まない。`<a href>` では `withBase` と併用する。
 */

export const locales = ["en", "ja"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "en";

const BASE = (import.meta.env.BASE_URL ?? "/").replace(/\/$/, "");

/** BASE を取り除いた純粋なパス（先頭スラッシュ付き）を返す。 */
const stripBase = (pathname: string): string => {
  const withoutBase = BASE && pathname.startsWith(BASE) ? pathname.slice(BASE.length) : pathname;
  return withoutBase.startsWith("/") ? withoutBase : `/${withoutBase}`;
};

export const getLocaleFromUrl = (url: URL): Locale => {
  const [first] = stripBase(url.pathname).split("/").filter(Boolean);
  return first === "jp" ? "ja" : "en";
};

/** 現在パスから `/jp` プレフィックスと BASE を取り除いた正準（en 相当）パスを返す。 */
export const toBasePath = (pathname: string): string => {
  const clean = stripBase(pathname);
  if (clean === "/jp" || clean === "/jp/") return "/";
  if (clean.startsWith("/jp/")) return clean.slice("/jp".length);
  return clean;
};

/** ロケール非依存のベースパスを、指定ロケールの URL（BASE 非含有）に変換する。 */
export const localePath = (basePath: string, locale: Locale): string => {
  const clean = basePath.startsWith("/") ? basePath : `/${basePath}`;
  if (locale === "ja") {
    return clean === "/" ? "/jp/" : `/jp${clean}`;
  }
  return clean;
};

export const htmlLang: Record<Locale, string> = { en: "en", ja: "ja" };
export const ogLocale: Record<Locale, string> = { en: "en_US", ja: "ja_JP" };

type Dict = Record<string, string>;

const en = {
  "site.tagline": "Daily digest of Claude-related YouTube",
  "nav.rss": "RSS",
  "nav.about": "About",
  "nav.topics": "Topics",
  "nav.archive": "Archive",
  "nav.notes": "Notes",
  "nav.editorialPolicy": "Editorial Policy",
  "nav.privacy": "Privacy Policy",
  "nav.contact": "Contact",
  "footer.disclaimer":
    "Claude Daily — auto-generated summaries; accuracy is not guaranteed. Sources are listed at the end of each article.",
  "lang.switchLabel": "Language",
  "lang.en": "EN",
  "lang.ja": "日本語",
  "index.lastBrief": "LAST BRIEF",
  "index.heroTitleA": "Catch up on Claude videos",
  "index.heroTitleB": "just by reading.",
  "index.heroSubtitleA":
    "We collect videos about Claude, Claude Code, Anthropic, and MCP every day ",
  "index.heroSubtitleB":
    "and auto-generate slide-style summaries from their transcripts.",
  "index.dailyBrief": "Daily Brief",
  "index.datesWithArticles": "Dates with articles",
  "index.latest": "Latest",
  "index.noPrev": "No previous day",
  "index.noNext": "No next day",
  "index.pickups": "Today's picks",
  "nav.dateAria": "Date navigation",
  "nav.timeline": "Timeline",
  "card.topics": "Topics covered",
  "unit.items": "articles",
  "article.minVideo": "min video",
  "article.slides": "slides",
  "article.tldr": "TL;DR · What you'll learn",
  "article.readSlides": "Read as slides",
  "article.allSlides": "slides total",
  "article.source": "Source",
  "article.sourceNote":
    "This article auto-summarizes the YouTube video's transcript with Claude. Please refer to the original video for nuance and exact wording.",
  "article.watchYoutube": "Watch on YouTube",
  "article.related": "Related",
  "article.publishedOn": "Published",
  "article.views": "views",
  "article.highlights": "highlights",
  "article.minutes": "min",
  "article.notFound": "Article not found.",
  "section.watchAt": "Watch at",
  "section.slide": "Slide",
  "topics.title": "Topics | Claude Daily",
  "topics.heading": "Browse topics by theme",
  "topics.lead":
    "Related video summaries grouped by the key phrases attached to each article. Handy when you want to follow a single thread across videos.",
  "topics.featured": "Featured Topics",
  "topics.totalUnit": "topics",
  "topics.latest": "Latest",
  "topics.description":
    "Claude Daily topic index. Explore Claude, Anthropic, and MCP themes grouped by key phrase.",
  "topic.label": "Topic",
  "topic.lead":
    "Video summaries that touch on this topic, newest first. Useful for comparing the same point across multiple channels.",
  "topic.viewOthers": "Browse other topics",
  "topic.articlesUnit": "articles",
} satisfies Dict;

const ja: Dict = {
  "site.tagline": "Claude関連YouTubeを毎日まとめる",
  "nav.rss": "RSS",
  "nav.about": "About",
  "nav.topics": "Topics",
  "nav.archive": "Archive",
  "nav.notes": "編集メモ",
  "nav.editorialPolicy": "Editorial Policy",
  "nav.privacy": "プライバシーポリシー",
  "nav.contact": "Contact",
  "footer.disclaimer":
    "Claude Daily — 自動要約のため正確性は保証されません。出典は各記事末尾に記載しています。",
  "lang.switchLabel": "言語",
  "lang.en": "EN",
  "lang.ja": "日本語",
  "index.lastBrief": "LAST BRIEF",
  "index.heroTitleA": "Claudeを語る動画を、",
  "index.heroTitleB": "読むだけで掴む。",
  "index.heroSubtitleA":
    "Claude・Claude Code・Anthropic・MCPに関する動画を毎日収集し、",
  "index.heroSubtitleB":
    "字幕からスライド風の日本語まとめを自動生成しています。",
  "index.dailyBrief": "Daily Brief",
  "index.datesWithArticles": "記事のある日付",
  "index.latest": "最新",
  "index.noPrev": "前日なし",
  "index.noNext": "翌日なし",
  "index.pickups": "本日のピックアップ",
  "nav.dateAria": "日付ナビゲーション",
  "nav.timeline": "タイムライン",
  "card.topics": "触れている論点",
  "unit.items": "件",
  "article.minVideo": "分の動画",
  "article.slides": "slides",
  "article.tldr": "TL;DR · この記事で分かること",
  "article.readSlides": "スライドで読む",
  "article.allSlides": "スライド",
  "article.source": "出典",
  "article.sourceNote":
    "この記事はYouTube動画の字幕をもとにClaudeで自動要約しています。細部のニュアンスや正確な発言は元動画をご参照ください。",
  "article.watchYoutube": "YouTubeで視聴する",
  "article.related": "関連記事",
  "article.publishedOn": "動画公開日",
  "article.views": "回再生",
  "article.highlights": "highlights",
  "article.minutes": "分",
  "article.notFound": "記事が見つかりません。",
  "section.watchAt": "で観る",
  "section.slide": "Slide",
  "topics.title": "トピック一覧 | Claude Daily",
  "topics.heading": "話題ごとに追えるトピック一覧",
  "topics.lead":
    "記事に付いているキーフレーズをもとに、関連する動画要約をまとめています。気になる論点だけを横断して追いたいときに使えます。",
  "topics.featured": "Featured Topics",
  "topics.totalUnit": "トピック",
  "topics.latest": "最新",
  "topics.description":
    "Claude Daily のトピック一覧。Claude、Anthropic、MCP まわりの話題をキーフレーズ単位でまとめて辿れます。",
  "topic.label": "Topic",
  "topic.lead":
    "このトピックに触れている動画要約を新しい順にまとめています。同じ論点を複数のチャンネルで比較したいときに使えます。",
  "topic.viewOthers": "他のトピックを見る",
  "topic.articlesUnit": "記事",
};

const dictionaries: Record<Locale, Dict> = { en, ja };

export type TranslationKey = keyof typeof en;

export const t = (locale: Locale) => (key: TranslationKey): string =>
  dictionaries[locale][key] ?? en[key];
