import type { CollectionEntry } from "astro:content";
import { getCollection } from "astro:content";
import type { Locale } from "../i18n/ui";

export type Article = CollectionEntry<"articles">;

export interface LocalizedBulletPoint {
  time: number;
  text: string;
}

export interface LocalizedSection {
  heading: string;
  time: number;
  body: string;
  image?: string | null;
}

export interface LocalizedArticle {
  title: string; // 元動画タイトル（言語非依存）
  articleTitle: string;
  seoTitle?: string;
  summary?: string;
  keyPhrases: string[];
  bulletPoints: LocalizedBulletPoint[];
  sections: LocalizedSection[];
  editorial?: string;
  headerImage: string;
  heroImage: string;
}

/**
 * 記事の表示テキスト・画像を指定ロケールへ解決する。トップレベルは日本語（原文）、
 * `en` ブロックは英語。`en` が無ければ日本語へフォールバックするため、部分翻訳でも破綻しない。
 */
export const localizeArticleData = (article: Article, locale: Locale): LocalizedArticle => {
  const d = article.data;
  if (locale === "en" && d.en) {
    return {
      title: d.title,
      articleTitle: d.en.articleTitle,
      seoTitle: d.en.seoTitle,
      summary: d.en.summary,
      keyPhrases: d.en.keyPhrases,
      bulletPoints: d.en.bulletPoints,
      sections: d.en.sections,
      editorial: d.en.editorial ?? undefined,
      headerImage: d.en.headerImage,
      heroImage: d.en.heroImage ?? d.en.headerImage,
    };
  }
  return {
    title: d.title,
    articleTitle: d.articleTitle ?? d.title,
    seoTitle: d.seoTitle,
    summary: d.summary,
    keyPhrases: d.keyPhrases,
    bulletPoints: d.bulletPoints,
    sections: d.sections,
    editorial: d.editorial ?? undefined,
    headerImage: d.headerImage,
    heroImage: d.heroImage ?? d.headerImage,
  };
};

export const getLocalizedDescription = (article: Article, locale: Locale): string => {
  const loc = localizeArticleData(article, locale);
  if (loc.summary) return loc.summary;
  if (loc.bulletPoints[0]?.text) return loc.bulletPoints[0].text;
  return locale === "en"
    ? `An English summary of "${loc.articleTitle}" from ${article.data.channel}.`
    : `${article.data.channel}の動画「${loc.articleTitle}」を日本語で要約した記事。`;
};

export interface DayGroup {
  date: string; // YYYY-MM-DD
  articles: Article[];
}

export interface TopicGroup {
  slug: string;
  label: string;
  articles: Article[];
}

// 日次バケットは JST (Asia/Tokyo) で決定する。ビルド環境のローカル時間に依存させない。
const JST_DATE_FORMATTER = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Tokyo",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

const toDateKey = (date: Date): string => JST_DATE_FORMATTER.format(date);

const sortArticlesNewestFirst = (articles: Article[]): Article[] =>
  articles.sort((a, b) => b.data.fetchedAt.getTime() - a.data.fetchedAt.getTime());

export const slugifyPathSegment = (value: string): string =>
  value
    .normalize("NFKC")
    .trim()
    .toLowerCase()
    .replace(/[\/\s]+/g, "-")
    .replace(/[^\p{L}\p{N}-]+/gu, "")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");

export const loadDailyGroups = async (): Promise<DayGroup[]> => {
  const articles = await getCollection("articles");
  const groups = new Map<string, Article[]>();
  for (const article of articles) {
    const key = toDateKey(article.data.fetchedAt);
    const list = groups.get(key) ?? [];
    list.push(article);
    groups.set(key, list);
  }
  return Array.from(groups.entries())
    .map(([date, items]) => ({
      date,
      articles: sortArticlesNewestFirst(items),
    }))
    .sort((a, b) => (a.date < b.date ? 1 : -1));
};

export const loadArticles = async (): Promise<Article[]> => {
  const articles = await getCollection("articles");
  return sortArticlesNewestFirst(articles);
};

const slugifyTopicLabel = (label: string): string => slugifyPathSegment(label) || "topic";

export const buildTopicHref = (slug: string): string => `/topics/${slug}/`;

export const buildTopicHrefFromLabel = (label: string): string =>
  buildTopicHref(slugifyTopicLabel(label));

export const getArticleDisplayTitle = (article: Article): string =>
  article.data.articleTitle ?? article.data.title;

export const getArticleSeoTitle = (article: Article): string =>
  article.data.seoTitle ?? getArticleDisplayTitle(article);

export const getArticleId = (article: Article): string =>
  String(article.data.videoId).trim().toLowerCase();

export const getArticleCustomSlug = (article: Article): string | undefined => {
  const slug = article.data.slug?.trim().toLowerCase();
  return slug ? slugifyPathSegment(slug) : undefined;
};

export const getArticleDescription = (article: Article): string =>
  article.data.summary ??
  article.data.bulletPoints[0]?.text ??
  `${article.data.channel}の動画「${getArticleDisplayTitle(article)}」を日本語で要約した記事。`;

const ARTICLE_SLUG_MAX_LENGTH = 56;

const trimSlugSegment = (slug: string, maxLength = ARTICLE_SLUG_MAX_LENGTH): string => {
  if (slug.length <= maxLength) {
    return slug;
  }

  const trimmed = slug.slice(0, maxLength).replace(/-+$/g, "");
  const safe = trimmed.slice(0, trimmed.lastIndexOf("-")).replace(/-+$/g, "");

  return safe.length >= Math.floor(maxLength * 0.55) ? safe : trimmed;
};

export const buildLegacyArticleSlug = (title: string, articleId: string): string => {
  const titleSlug = slugifyPathSegment(title);
  const normalizedId = articleId.toLowerCase();
  return titleSlug ? `${titleSlug}-${normalizedId}` : normalizedId;
};

export const buildArticleSlug = (
  title: string,
  articleId: string,
  explicitSlug?: string
): string => {
  if (explicitSlug) {
    return slugifyPathSegment(explicitSlug) || articleId.toLowerCase();
  }

  const titleSlug = trimSlugSegment(slugifyPathSegment(title));
  const normalizedId = articleId.toLowerCase();
  return titleSlug ? `${titleSlug}-${normalizedId}` : normalizedId;
};

export const buildArticlePath = (article: Article): string =>
  `/articles/${buildArticleSlug(
    getArticleDisplayTitle(article),
    getArticleId(article),
    getArticleCustomSlug(article)
  )}/`;

export const buildArticlePathFromTitle = (
  title: string,
  articleId: string,
  explicitSlug?: string
): string => `/articles/${buildArticleSlug(title, articleId, explicitSlug)}/`;

export const loadTopicGroups = async (locale: Locale = "ja"): Promise<TopicGroup[]> => {
  const articles = await loadArticles();
  const labelToArticles = new Map<string, Article[]>();

  for (const article of articles) {
    for (const phrase of localizeArticleData(article, locale).keyPhrases) {
      const list = labelToArticles.get(phrase) ?? [];
      list.push(article);
      labelToArticles.set(phrase, list);
    }
  }

  const slugCounts = new Map<string, number>();

  return Array.from(labelToArticles.entries())
    .map(([label, topicArticles]) => {
      const baseSlug = slugifyTopicLabel(label);
      const count = slugCounts.get(baseSlug) ?? 0;
      slugCounts.set(baseSlug, count + 1);

      return {
        label,
        slug: count === 0 ? baseSlug : `${baseSlug}-${count + 1}`,
        articles: sortArticlesNewestFirst(topicArticles),
      };
    })
    .sort((left, right) => {
      if (right.articles.length !== left.articles.length) {
        return right.articles.length - left.articles.length;
      }
      return left.label.localeCompare(right.label, locale);
    });
};

export const findTopicByLabel = (
  topics: TopicGroup[],
  label: string
): TopicGroup | undefined => topics.find((topic) => topic.label === label);

export interface ResolvedDay extends DayGroup {
  prevDate?: string;
  nextDate?: string;
}

export const resolveDay = (groups: DayGroup[], date: string): ResolvedDay | undefined => {
  const index = groups.findIndex((g) => g.date === date);
  if (index === -1) return undefined;
  const group = groups[index];
  return {
    ...group,
    prevDate: groups[index + 1]?.date,
    nextDate: groups[index - 1]?.date,
  };
};

const WEEKDAY_LABELS = ["日", "月", "火", "水", "木", "金", "土"];
const EN_WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
const EN_MONTHS = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
];

export const formatDateLabel = (date: string, locale: Locale = "ja"): string => {
  const [y, m, d] = date.split("-").map((part) => parseInt(part, 10));
  const dt = new Date(Date.UTC(y, m - 1, d));
  if (locale === "en") {
    return `${EN_MONTHS[m - 1]} ${d}, ${y} (${EN_WEEKDAYS[dt.getUTCDay()]})`;
  }
  return `${y}年${m}月${d}日 (${WEEKDAY_LABELS[dt.getUTCDay()]})`;
};

export const formatShortDate = (date: string): string => {
  const [y, m, d] = date.split("-");
  return `${y}/${m}/${d}`;
};

const intersectCount = (left: string[], right: string[]): number => {
  const rightSet = new Set(right.map((value) => value.toLowerCase()));
  return left.reduce((count, value) => {
    return count + (rightSet.has(value.toLowerCase()) ? 1 : 0);
  }, 0);
};

export const findRelatedArticles = (
  currentArticle: Article,
  allArticles: Article[],
  limit = 3
): Article[] => {
  return allArticles
    .filter((article) => getArticleId(article) !== getArticleId(currentArticle))
    .map((article) => {
      const phraseMatches = intersectCount(
        currentArticle.data.keyPhrases,
        article.data.keyPhrases
      );
      const keywordMatches = intersectCount(
        currentArticle.data.matchedKeywords,
        article.data.matchedKeywords
      );
      const sameChannel = currentArticle.data.channelId === article.data.channelId ? 1 : 0;
      const score = phraseMatches * 4 + keywordMatches * 2 + sameChannel;
      return { article, score };
    })
    .filter(({ score }) => score > 0)
    .sort((left, right) => {
      if (right.score !== left.score) {
        return right.score - left.score;
      }
      return (
        right.article.data.fetchedAt.getTime() - left.article.data.fetchedAt.getTime()
      );
    })
    .slice(0, limit)
    .map(({ article }) => article);
};
