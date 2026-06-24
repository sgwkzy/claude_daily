import { buildArticlePath, loadArticles, loadDailyGroups, loadTopicGroups } from "../lib/articles";
import { localePath, locales } from "../i18n/ui";

const site = import.meta.env.SITE ?? "https://www.claude-daily.com";

const toUrl = (path: string) => new URL(path, site).toString();

const escapeXml = (value: string) =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

interface SitemapEntry {
  /** ロケール非依存のベースパス。両ロケールのエントリと hreflang を生成する。 */
  basePath: string;
  lastmod?: string;
}

export async function GET() {
  // loadArticles は fetchedAt の新しい順にソート済み。articles[0] が最新記事になり、
  // 静的ページの lastmod を「サイトの最終更新日」として正しく反映できる。
  const articles = await loadArticles();
  const groups = await loadDailyGroups();
  const latestFetchedAt = articles[0]?.data.fetchedAt.toISOString();

  // 両ロケールで同一スラッグを共有するページ（トピックは言語でスラッグが異なるため別扱い）。
  const sharedEntries: SitemapEntry[] = [
    { basePath: "/", lastmod: latestFetchedAt },
    { basePath: "/about/", lastmod: latestFetchedAt },
    { basePath: "/editorial-policy/", lastmod: latestFetchedAt },
    { basePath: "/privacy/", lastmod: latestFetchedAt },
    { basePath: "/contact/", lastmod: latestFetchedAt },
    { basePath: "/notes/", lastmod: latestFetchedAt },
    { basePath: "/archive/", lastmod: latestFetchedAt },
    { basePath: "/topics/", lastmod: latestFetchedAt },
    ...groups.map((group) => ({
      basePath: `/days/${group.date}/`,
      lastmod: group.articles[0]?.data.fetchedAt.toISOString(),
    })),
    ...articles.map((article) => ({
      basePath: buildArticlePath(article),
      lastmod: article.data.fetchedAt.toISOString(),
    })),
  ];

  const renderAlternates = (basePath: string): string =>
    [...locales, "en" as const]
      .map((loc, index) => {
        const hreflang = index === locales.length ? "x-default" : loc;
        return `    <xhtml:link rel="alternate" hreflang="${hreflang}" href="${escapeXml(
          toUrl(localePath(basePath, loc))
        )}" />`;
      })
      .join("\n");

  const renderSharedUrls = (entry: SitemapEntry): string =>
    locales
      .map(
        (loc) => `  <url>
    <loc>${escapeXml(toUrl(localePath(entry.basePath, loc)))}</loc>
${entry.lastmod ? `    <lastmod>${entry.lastmod}</lastmod>\n` : ""}${renderAlternates(entry.basePath)}
  </url>`
      )
      .join("\n");

  // トピックは言語ごとにスラッグが異なるため、各ロケールで個別に列挙する。
  const topicUrls: string[] = [];
  for (const loc of locales) {
    const topics = await loadTopicGroups(loc);
    for (const topic of topics) {
      const lastmod = topic.articles[0]?.data.fetchedAt.toISOString() ?? latestFetchedAt;
      topicUrls.push(`  <url>
    <loc>${escapeXml(toUrl(localePath(`/topics/${topic.slug}/`, loc)))}</loc>
${lastmod ? `    <lastmod>${lastmod}</lastmod>\n` : ""}  </url>`);
    }
  }

  const body = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ...sharedEntries.map(renderSharedUrls),
    ...topicUrls,
    "</urlset>",
    "",
  ].join("\n");

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
    },
  });
}
