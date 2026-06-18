import type { APIRoute } from "astro";
import {
  buildArticlePath,
  getArticleDescription,
  getArticleSeoTitle,
  loadArticles,
} from "../lib/articles";

const SITE_URL = "https://www.claude-daily.com";

const escapeXml = (value: string): string =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

export const GET: APIRoute = async () => {
  const articles = await loadArticles();
  const items = articles
    .map((article) => {
      const title = getArticleSeoTitle(article);
      const description = getArticleDescription(article);
      const link = `${SITE_URL}${buildArticlePath(article)}`;

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
    "<title>Claude Daily</title>",
    `<link>${SITE_URL}/</link>`,
    "<description>Claude・Claude Code・Anthropic・MCP関連のYouTube要約を毎日配信するRSSです。</description>",
    "<language>ja</language>",
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
