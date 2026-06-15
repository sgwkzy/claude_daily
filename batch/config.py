from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class YoutubeConfig(BaseModel):
    keywords: list[str] = Field(default_factory=list)
    limit_total: int = 10
    per_keyword_top_n: int = 5
    min_view_count: int = 5000
    min_duration_sec: int = 180
    max_age_hours: int = 72
    region_code: str = "JP"


class PipelineConfig(BaseModel):
    dry_run_limit: int = 2
    section_count_min: int = 3
    section_count_max: int = 5
    output_articles_dir: str = "site/src/content/articles"
    output_images_dir: str = "site/public/images"
    temp_dir: str = "batch/tmp"


class PromptConfig(BaseModel):
    trend_limit: int = 3
    header_style: str = "cinematic editorial collage, vibrant lighting, high contrast"
    thumbnail_directions: list[str] = Field(default_factory=lambda: ["source-explainer"])


class Settings(BaseModel):
    youtube: YoutubeConfig
    pipeline: PipelineConfig
    prompts: PromptConfig


def load_config(path: str | Path) -> Settings:
    config_path = Path(path)
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("config.yaml の形式が不正です。")
    return Settings.model_validate(raw)


def ensure_directories(root: Path, settings: Settings) -> None:
    for relative_path in (
        settings.pipeline.output_articles_dir,
        settings.pipeline.output_images_dir,
        settings.pipeline.temp_dir,
    ):
        (root / relative_path).mkdir(parents=True, exist_ok=True)
