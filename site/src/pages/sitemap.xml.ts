import { getCollection } from "astro:content";
import { loadDailyGroups } from "../lib/articles";

const site = import.meta.env.SITE ?? "https://www.claude-daily.com";

const toUrl = (path: string) => new URL(path, site).toString();

const escapeXml = (value: string) =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

export async function GET() {
  const articles = await getCollection("articles");
  const groups = await loadDailyGroups();

  const urls = [
    { loc: toUrl("/"), lastmod: articles[0]?.data.fetchedAt.toISOString() },
    ...groups.map((group) => ({
      loc: toUrl(`/days/${group.date}/`),
      lastmod: group.articles[0]?.data.fetchedAt.toISOString(),
    })),
    ...articles.map((article) => ({
      loc: toUrl(`/articles/${article.id}/`),
      lastmod: article.data.fetchedAt.toISOString(),
    })),
  ];

  const body = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ...urls.map(
      ({ loc, lastmod }) => `  <url>
    <loc>${escapeXml(loc)}</loc>
    ${lastmod ? `<lastmod>${lastmod}</lastmod>` : ""}
  </url>`
    ),
    "</urlset>",
    "",
  ].join("\n");

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
    },
  });
}
