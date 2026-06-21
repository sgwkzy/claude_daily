import {
  buildArticlePath,
  getLocalizedDescription,
  loadArticles,
  localizeArticleData,
} from "./articles";
import { localePath, type Locale } from "../i18n/ui";

const SITE_URL = "https://www.claude-daily.com";

const escapeXml = (value: string): string =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

const channelMeta: Record<Locale, { title: string; description: string; language: string }> = {
  en: {
    title: "Claude Daily",
    description: "Daily English digests of YouTube videos about Claude, Claude Code, Anthropic, and MCP.",
    language: "en",
  },
  ja: {
    title: "Claude Daily",
    description: "Claude・Claude Code・Anthropic・MCP関連のYouTube要約を毎日配信するRSSです。",
    language: "ja",
  },
};

/** ロケール別の RSS フィードを生成する。`en` はルート、`ja` は /jp/ プレフィックス。 */
export const buildRssFeed = async (locale: Locale): Promise<Response> => {
  const articles = await loadArticles();
  const meta = channelMeta[locale];
  const items = articles
    .map((article) => {
      const loc = localizeArticleData(article, locale);
      const title = loc.seoTitle ?? loc.articleTitle;
      const description = getLocalizedDescription(article, locale);
      const link = `${SITE_URL}${localePath(buildArticlePath(article), locale)}`;

      return [
        "<item>",
        `<title>${escapeXml(title)}</title>`,
        `<link>${link}</link>`,
        `<guid>${link}</guid>`,
        `<pubDate>${article.data.fetchedAt.toUTCString()}</pubDate>`,
        `<description>${escapeXml(description)}</description>`,
        "</item>",
      ].join("");
    })
    .join("");

  const xml = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0">',
    "<channel>",
    `<title>${escapeXml(meta.title)}</title>`,
    `<link>${SITE_URL}${localePath("/", locale)}</link>`,
    `<description>${escapeXml(meta.description)}</description>`,
    `<language>${meta.language}</language>`,
    `<lastBuildDate>${new Date().toUTCString()}</lastBuildDate>`,
    items,
    "</channel>",
    "</rss>",
  ].join("");

  return new Response(xml, {
    headers: {
      "Content-Type": "application/rss+xml; charset=utf-8",
    },
  });
};
