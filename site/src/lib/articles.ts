import type { CollectionEntry } from "astro:content";
import { getCollection } from "astro:content";

export type Article = CollectionEntry<"articles">;

export interface DayGroup {
  date: string; // YYYY-MM-DD
  articles: Article[];
}

const toDateKey = (date: Date): string => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

export const loadDailyGroups = async (): Promise<DayGroup[]> => {
  const articles = await getCollection("articles");
  const groups = new Map<string, Article[]>();
  for (const article of articles) {
    const key = toDateKey(article.data.publishedAt);
    const list = groups.get(key) ?? [];
    list.push(article);
    groups.set(key, list);
  }
  return Array.from(groups.entries())
    .map(([date, items]) => ({
      date,
      articles: items.sort(
        (a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime()
      ),
    }))
    .sort((a, b) => (a.date < b.date ? 1 : -1));
};

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

export const formatDateLabel = (date: string): string => {
  const [y, m, d] = date.split("-").map((part) => parseInt(part, 10));
  const dt = new Date(Date.UTC(y, m - 1, d));
  return `${y}年${m}月${d}日 (${WEEKDAY_LABELS[dt.getUTCDay()]})`;
};

export const formatShortDate = (date: string): string => {
  const [y, m, d] = date.split("-");
  return `${y}/${m}/${d}`;
};
