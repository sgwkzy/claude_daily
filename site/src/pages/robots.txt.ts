const site = import.meta.env.SITE ?? "https://claude-daily.com";

export function GET() {
  const body = [
    "User-agent: *",
    "Allow: /",
    "Disallow: /preview-thumbnails/",
    "",
    `Sitemap: ${new URL("/sitemap.xml", site).toString()}`,
    "",
  ].join("\n");

  return new Response(body, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
