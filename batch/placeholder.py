"""dry-run / フォールバック時に使うプレースホルダ画像生成。

以前は media.py のプライベート関数 ``_write_placeholder`` を header_image.py が
モジュール跨ぎで import していたため、公開関数として独立させた。
"""
from __future__ import annotations

import hashlib
from pathlib import Path

_PALETTES = {
    "thumbnail": [(244, 239, 230), (217, 119, 87), (124, 92, 73)],
    "scene": [(250, 247, 241), (231, 221, 201), (217, 119, 87)],
    "header": [(217, 119, 87), (185, 94, 64), (31, 27, 22)],
}


def write_placeholder(destination: Path, seed: str, palette: str) -> None:
    from PIL import Image, ImageDraw

    colors = _PALETTES.get(palette, _PALETTES["thumbnail"])
    hash_bytes = hashlib.md5(seed.encode("utf-8")).digest()
    base = colors[0]
    accent = colors[1]
    shadow = colors[2]
    width, height = (1280, 720)
    image = Image.new("RGB", (width, height), base)
    draw = ImageDraw.Draw(image, "RGBA")
    offset_a = int(hash_bytes[0]) * 2
    offset_b = int(hash_bytes[1]) * 2
    draw.ellipse(
        [width - 360 - offset_a, -160, width + 200, 360 + offset_a],
        fill=(*accent, 220),
    )
    draw.ellipse(
        [-200, height - 400 - offset_b, 480 + offset_b, height + 200],
        fill=(*shadow, 80),
    )
    draw.rectangle(
        [0, height - 12, width, height],
        fill=(*accent, 255),
    )
    if destination.suffix.lower() == ".png":
        image.save(destination, "PNG")
    else:
        image.save(destination, "WEBP", quality=82)
