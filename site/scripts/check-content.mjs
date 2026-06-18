import fs from "node:fs/promises";
import path from "node:path";

const contentDir = path.resolve("src/content/articles");
const requiredFields = ["videoId", "title", "slug", "seoTitle", "summary"];

const files = (await fs.readdir(contentDir))
  .filter((name) => name.endsWith(".md"))
  .sort((a, b) => a.localeCompare(b, "en"));

const errors = [];

for (const fileName of files) {
  const fullPath = path.join(contentDir, fileName);
  const source = await fs.readFile(fullPath, "utf8");
  const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---/);

  if (!match) {
    errors.push(`${fileName}: frontmatter が見つかりません`);
    continue;
  }

  const frontmatter = match[1];

  for (const field of requiredFields) {
    const fieldPattern = new RegExp(`^${field}:\\s*(.+)$`, "m");
    const fieldMatch = frontmatter.match(fieldPattern);
    const value = fieldMatch?.[1]?.trim();

    if (!value) {
      errors.push(`${fileName}: ${field} が未設定です`);
    }
  }
}

if (errors.length > 0) {
  console.error("Content validation failed:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log(`Content validation passed: ${files.length} article files checked.`);
