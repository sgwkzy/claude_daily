import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const bulletPointSchema = z.object({
  time: z.number().int().nonnegative(),
  text: z.string().min(1)
});

const sectionSchema = z.object({
  heading: z.string().min(1),
  time: z.number().int().nonnegative(),
  image: z.string().min(1).nullable().optional(),
  body: z.string().min(1)
});

// 既定では英語の翻訳ブロック。トップレベルが日本語（原文）を表すのに対し、
// このオブジェクトは別ロケール向けの表示テキストと画像の上書きを表す。
const translationSchema = z.object({
  articleTitle: z.string().min(1),
  seoTitle: z.string().min(1),
  summary: z.string().min(1),
  keyPhrases: z.array(z.string()),
  bulletPoints: z.array(bulletPointSchema),
  sections: z.array(sectionSchema),
  editorial: z.string().min(1).optional(),
  headerImage: z.string().min(1),
  heroImage: z.string().min(1).nullable().optional()
});

const articles = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/articles",
  }),
  schema: z.object({
    videoId: z.string().min(1),
    slug: z.string().min(1).optional(),
    title: z.string().min(1),
    articleTitle: z.string().min(1).optional(),
    seoTitle: z.string().min(1).optional(),
    summary: z.string().min(1).optional(),
    channel: z.string().min(1),
    channelId: z.string().min(1),
    publishedAt: z.coerce.date(),
    fetchedAt: z.coerce.date(),
    originalThumbnail: z.string().url(),
    headerImage: z.string().min(1),
    heroImage: z.string().min(1).optional(),
    viewCount: z.number().int().nonnegative(),
    durationSec: z.number().int().nonnegative(),
    sourceLanguage: z.string().min(2),
    matchedKeywords: z.array(z.string()),
    proposedByLLM: z.boolean(),
    keyPhrases: z.array(z.string()),
    bulletPoints: z.array(bulletPointSchema),
    sections: z.array(sectionSchema),
    editorial: z.string().min(1).optional(),
    en: z.optional(translationSchema.nullable())
  })
});

export const collections = { articles };
