import { readdir, readFile } from "node:fs/promises";
import path from "node:path";

const [articlesDirArg, siteUrlArg, keyArg] = process.argv.slice(2);

if (!articlesDirArg || !siteUrlArg || !keyArg) {
  console.error("Usage: node build-indexnow-payload.mjs <articlesDir> <siteUrl> <key>");
  process.exit(1);
}

const articlesDir = path.resolve(articlesDirArg);
const siteUrl = new URL(siteUrlArg.endsWith("/") ? siteUrlArg : `${siteUrlArg}/`);
const keyLocation = new URL(`/${keyArg}.txt`, siteUrl).toString();

const articleFiles = (await readdir(articlesDir)).filter((name) => name.endsWith(".md")).sort();
const dayUrls = new Set();
const urlList = [siteUrl.toString()];

for (const fileName of articleFiles) {
  const slug = path.basename(fileName, ".md");
  const content = await readFile(path.join(articlesDir, fileName), "utf8");
  const publishedAtMatch = content.match(/^publishedAt:\s*['"]?([^'"\r\n]+)['"]?/m);

  if (!publishedAtMatch) {
    throw new Error(`publishedAt not found in ${fileName}`);
  }

  const publishedDate = new Date(publishedAtMatch[1]);
  if (Number.isNaN(publishedDate.valueOf())) {
    throw new Error(`Invalid publishedAt in ${fileName}: ${publishedAtMatch[1]}`);
  }

  const day = publishedDate.toISOString().slice(0, 10);
  dayUrls.add(new URL(`/days/${day}/`, siteUrl).toString());
  urlList.push(new URL(`/articles/${slug}/`, siteUrl).toString());
}

urlList.push(...Array.from(dayUrls).sort());

const payload = {
  host: siteUrl.host,
  key: keyArg,
  keyLocation,
  urlList,
};

process.stdout.write(`${JSON.stringify(payload)}\n`);
