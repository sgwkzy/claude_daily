from pathlib import Path

from batch.header_image import HeaderContext, HeaderImageGenerator
from PIL import Image


def test_header_image_dry_run(tmp_path: Path) -> None:
    source = tmp_path / "src.webp"
    source.write_bytes(b"demo")
    generator = HeaderImageGenerator(api_key=None, style_prompt="style")
    destination = generator.generate(source, tmp_path / "header.png", "title", dry_run=True)
    assert destination.exists()
    assert destination.stat().st_size > 0
    with Image.open(destination) as image:
        assert image.size == (1280, 720)


def test_header_image_builds_directional_prompt(tmp_path: Path) -> None:
    source = tmp_path / "src.webp"
    source.write_bytes(b"demo")
    prompt_path = tmp_path / "header-editorial-rebuild.prompt.txt"
    context = HeaderContext(
        title="Claude Code workflow",
        article_title="Claude Code実践ガイド",
        channel="Demo Channel",
        category_label="Claude Code",
        key_phrases=["Claude Code", "MCP", "agents"],
        bullet_points=["CLIから実装まで進める", "社内ツール接続で文脈共有する"],
        section_headings=["導入", "実装フロー", "運用"],
    )
    generator = HeaderImageGenerator(api_key=None, style_prompt="style")
    generator.generate(
        source,
        tmp_path / "header.webp",
        "Claude Code workflow",
        dry_run=True,
        direction="editorial-rebuild",
        context=context,
        prompt_dump_path=prompt_path,
    )
    prompt_text = prompt_path.read_text(encoding="utf-8")
    assert "Generate the entire background and composition from scratch" in prompt_text
    assert "Composition: left side with strong Japanese headline text" in prompt_text
    assert "Avoid Claude Daily branding inside the image." in prompt_text
    assert "Japanese article headline: Claude Code実践ガイド." in prompt_text
    assert "Category chip text: Claude Code." in prompt_text
    assert "Key phrases: Claude Code; MCP; agents." in prompt_text
    assert "Article takeaways: CLIから実装まで進める; 社内ツール接続で文脈共有する." in prompt_text


def test_header_image_english_prompt(tmp_path: Path) -> None:
    source = tmp_path / "src.webp"
    source.write_bytes(b"demo")
    prompt_path = tmp_path / "header-en.prompt.txt"
    context = HeaderContext(
        title="Claude Code workflow",
        article_title="A practical guide to Claude Code",
        channel="Demo Channel",
    )
    generator = HeaderImageGenerator(api_key=None, style_prompt="style")
    generator.generate(
        source,
        tmp_path / "header.png",
        "Claude Code workflow",
        dry_run=True,
        direction="editorial-rebuild",
        context=context,
        prompt_dump_path=prompt_path,
        language="en",
    )
    prompt_text = prompt_path.read_text(encoding="utf-8")
    assert "English article headline: A practical guide to Claude Code." in prompt_text
    assert "Composition: left side with strong English headline text" in prompt_text
    assert "Japanese headline text" not in prompt_text
