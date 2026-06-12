from pathlib import Path

from batch.header_image import HeaderImageGenerator


def test_header_image_dry_run(tmp_path: Path) -> None:
    source = tmp_path / "src.webp"
    source.write_bytes(b"demo")
    generator = HeaderImageGenerator(api_key=None, style_prompt="style")
    destination = generator.generate(source, tmp_path / "header.webp", "title", dry_run=True)
    assert destination.exists()
    assert destination.stat().st_size > 0

