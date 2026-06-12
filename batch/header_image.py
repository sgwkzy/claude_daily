from __future__ import annotations

import base64

from pathlib import Path


class HeaderImageGenerator:
    def __init__(self, api_key: str | None, style_prompt: str) -> None:
        self.api_key = api_key
        self.style_prompt = style_prompt

    def generate(self, source_image: Path, destination: Path, title: str, dry_run: bool = False) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if dry_run:
            from .media import _write_placeholder

            _write_placeholder(destination, seed=title, palette="header")
            return destination
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY が設定されていません。")
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key)
        with source_image.open("rb") as image_file:
            response = client.images.edit(
                model="gpt-image-1",
                image=image_file,
                prompt=f"{title} を表現したヘッダー画像。{self.style_prompt}",
                size="1536x1024",
            )
        image_base64 = response.data[0].b64_json
        destination.write_bytes(base64.b64decode(image_base64))
        return destination
