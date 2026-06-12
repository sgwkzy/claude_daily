/**
 * Prepend the configured Astro `base` (e.g. "/claude_daily/") to an asset path
 * that starts with "/". Useful for `<img src>` / `<link href>` references that
 * Astro does NOT auto-rewrite at build time.
 *
 * `import.meta.env.BASE_URL` has a trailing slash; this helper normalises so
 * that `withBase("/images/foo.webp")` returns `"/claude_daily/images/foo.webp"`.
 */
export const withBase = (path: string): string => {
  const base = (import.meta.env.BASE_URL ?? "/").replace(/\/$/, "");
  const tail = path.startsWith("/") ? path : `/${path}`;
  return `${base}${tail}`;
};
