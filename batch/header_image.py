from __future__ import annotations

import base64
from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps


SUPPORTED_DIRECTIONS = {
    "source-first",
    "source-explainer",
    "frame-summary",
    "reconstructed-concept",
}
TARGET_HEADER_SIZE = (1672, 941)


@dataclass(slots=True)
class HeaderContext:
    title: str
    channel: str
    key_phrases: list[str] = field(default_factory=list)
    bullet_points: list[str] = field(default_factory=list)
    section_headings: list[str] = field(default_factory=list)


class HeaderImageGenerator:
    def __init__(self, api_key: str | None, style_prompt: str) -> None:
        self.api_key = api_key
        self.style_prompt = style_prompt

    def generate(
        self,
        source_image: Path,
        destination: Path,
        title: str,
        dry_run: bool = False,
        *,
        direction: str = "source-explainer",
        context: HeaderContext | None = None,
        prompt_dump_path: Path | None = None,
    ) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        prompt = self._build_prompt(title, direction=direction, context=context)
        if prompt_dump_path:
            prompt_dump_path.parent.mkdir(parents=True, exist_ok=True)
            prompt_dump_path.write_text(prompt, encoding="utf-8")
        if dry_run:
            from .placeholder import write_placeholder

            write_placeholder(destination, seed=title, palette="header")
            return destination
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY が設定されていません。")
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key)
        with source_image.open("rb") as image_file:
            response = client.images.edit(
                model="gpt-image-1",
                image=image_file,
                prompt=prompt,
                size="1536x1024",
            )
        image_base64 = response.data[0].b64_json
        _normalize_header_image(base64.b64decode(image_base64), destination)
        return destination

    def _build_prompt(self, title: str, *, direction: str, context: HeaderContext | None) -> str:
        if direction not in SUPPORTED_DIRECTIONS:
            supported = ", ".join(sorted(SUPPORTED_DIRECTIONS))
            raise ValueError(f"未対応のサムネイル方針です: {direction} / supported={supported}")
        if context is None:
            context = HeaderContext(title=title, channel="")

        key_phrase_text = _compact_list(context.key_phrases, limit=3)
        bullet_text = _compact_list(context.bullet_points, limit=2)
        section_text = _compact_list(context.section_headings, limit=3)
        source_label = f"Source video title: {context.title}."
        channel_label = f"Channel: {context.channel}." if context.channel else ""
        style = f"Visual style: {self.style_prompt}."

        if direction == "source-first":
            return " ".join(
                part
                for part in (
                    source_label,
                    channel_label,
                    "Keep the original video thumbnail clearly recognizable.",
                    "Preserve the main subject, composition, and mood of the source image.",
                    "Add only a small editorial label for Claude Daily and one short explanatory line.",
                    "Do not hide faces, hands, or important UI.",
                    style,
                )
                if part
            )
        if direction == "source-explainer":
            return " ".join(
                part
                for part in (
                    source_label,
                    channel_label,
                    _optional_sentence("Key phrases", key_phrase_text),
                    _optional_sentence("Article takeaways", bullet_text),
                    "Use the original video thumbnail as the main background.",
                    "Design the composition specifically for a consistent 16:9 widescreen editorial thumbnail.",
                    "Keep safe margins so no critical text or focal subject sits too close to the edges.",
                    "Add minimal editorial overlays that explain what the article teaches.",
                    "Include one small category label and one short summary headline.",
                    "Do not hide the original subject or important UI elements.",
                    "Avoid adding extra media-brand labels such as Claude Daily inside the image.",
                    style,
                )
                if part
            )
        if direction == "frame-summary":
            return " ".join(
                part
                for part in (
                    source_label,
                    channel_label,
                    _optional_sentence("Section themes", section_text),
                    _optional_sentence("Article takeaways", bullet_text),
                    "Create a composition that feels like a representative frame from the source video.",
                    "Add a clean editorial summary card with two or three concise ideas.",
                    "Optimize the card for mobile readability.",
                    style,
                )
                if part
            )
        return " ".join(
            part
            for part in (
                source_label,
                channel_label,
                _optional_sentence("Key phrases", key_phrase_text),
                _optional_sentence("Section themes", section_text),
                "Create an editorial concept image inspired by the topic of the source video, not a literal copy.",
                "Keep the image grounded in the article's actual takeaways and add a subtle source label.",
                "Avoid generic AI art and prefer concrete product, code, or workflow cues.",
                style,
            )
            if part
        )


def _compact_list(items: list[str], *, limit: int) -> str:
    cleaned = [item.strip() for item in items if item.strip()]
    return "; ".join(cleaned[:limit])


def _optional_sentence(label: str, value: str) -> str:
    if not value:
        return ""
    return f"{label}: {value}."


def _normalize_header_image(image_bytes: bytes, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(BytesIO(image_bytes)) as image:
        normalized = ImageOps.fit(
            image.convert("RGB"),
            TARGET_HEADER_SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        normalized.save(destination, "PNG")
