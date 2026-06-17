from pathlib import Path

from batch.config import ensure_directories, load_config


def test_load_config() -> None:
    settings = load_config(Path("batch/config.yaml"))
    assert settings.youtube.limit_total == 10
    assert settings.pipeline.output_articles_dir.endswith("articles")
    assert settings.prompts.thumbnail_directions == ["editorial-rebuild"]


def test_ensure_directories(tmp_path: Path) -> None:
    settings = load_config(Path("batch/config.yaml"))
    ensure_directories(tmp_path, settings)
    assert (tmp_path / settings.pipeline.output_articles_dir).exists()
    assert (tmp_path / settings.pipeline.output_images_dir).exists()
