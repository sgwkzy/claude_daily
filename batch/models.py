from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class TranscriptSegment(BaseModel):
    start: int = Field(ge=0)
    duration: int = Field(ge=0)
    text: str = Field(min_length=1)


class BulletPoint(BaseModel):
    time: int = Field(ge=0)
    text: str = Field(min_length=1)


class ArticleSection(BaseModel):
    heading: str = Field(min_length=1)
    time: int = Field(ge=0)
    body: str = Field(min_length=1)
    image: str | None = None


class SummaryResult(BaseModel):
    articleTitle: str = Field(min_length=1)
    bulletPoints: list[BulletPoint] = Field(min_length=1)
    sections: list[ArticleSection] = Field(min_length=1)
    keyPhrases: list[str] = Field(min_length=1)
    # 編集部の独自論評。動画字幕には無い視点（重要性・読者への示唆・他動向との接続）。
    # 既存記事の再構築経路を壊さないよう Optional。新規生成では必ず埋める。
    editorial: str | None = None


class ArticleTranslation(BaseModel):
    """記事フロントマターに格納する翻訳済み（既定では英語）表示テキストと画像。

    トップレベルのフィールドが原文（日本語）を表すのに対し、このブロックは
    別ロケール向けの上書きを表す。``time`` と ``image`` は言語非依存なので
    原文の値をそのまま流用する。
    """

    articleTitle: str = Field(min_length=1)
    seoTitle: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    keyPhrases: list[str] = Field(min_length=1)
    bulletPoints: list[BulletPoint] = Field(min_length=1)
    sections: list[ArticleSection] = Field(min_length=1)
    editorial: str | None = None
    headerImage: str = Field(min_length=1)
    heroImage: str | None = None


class VideoCandidate(BaseModel):
    video_id: str = Field(alias="videoId", min_length=1)
    title: str = Field(min_length=1)
    channel: str = Field(min_length=1)
    channel_id: str = Field(alias="channelId", min_length=1)
    published_at: datetime = Field(alias="publishedAt")
    view_count: int = Field(alias="viewCount", ge=0)
    duration_sec: int = Field(alias="durationSec", ge=0)
    original_thumbnail: HttpUrl = Field(alias="originalThumbnail")
    source_language: str = Field(alias="sourceLanguage", min_length=2)
    matched_keywords: list[str] = Field(alias="matchedKeywords", default_factory=list)
    proposed_by_llm: bool = Field(alias="proposedByLLM", default=False)
    score: float = 0.0

    model_config = {"populate_by_name": True}


class ArticleFrontmatter(BaseModel):
    videoId: str = Field(min_length=1)
    title: str = Field(min_length=1)
    slug: str | None = None
    articleTitle: str | None = None
    seoTitle: str | None = None
    summary: str | None = None
    channel: str = Field(min_length=1)
    channelId: str = Field(min_length=1)
    publishedAt: datetime
    fetchedAt: datetime
    originalThumbnail: HttpUrl
    headerImage: str = Field(min_length=1)
    heroImage: str | None = None
    viewCount: int = Field(ge=0)
    durationSec: int = Field(ge=0)
    sourceLanguage: str = Field(min_length=2)
    matchedKeywords: list[str] = Field(default_factory=list)
    proposedByLLM: bool = False
    keyPhrases: list[str] = Field(default_factory=list)
    bulletPoints: list[BulletPoint] = Field(default_factory=list)
    sections: list[ArticleSection] = Field(default_factory=list)
    # 編集部の独自論評。既存記事は未保有のため後方互換でOptionalかつNoneデフォルト。
    editorial: str | None = None
    # 既定では英語の翻訳ブロック。トップレベルが日本語（原文）を表す。
    en: ArticleTranslation | None = None


class PipelineStats(BaseModel):
    processed: int = 0
    created: int = 0
    skipped_existing: int = 0
    skipped_transcript: int = 0
    skipped_errors: int = 0
    # skipped_errors の内訳（標準出力サマリには出さず、ログ・調査用）。
    failed_transcript: int = 0
    failed_summary: int = 0
    failed_media: int = 0
    failed_header: int = 0
    failed_write: int = 0
