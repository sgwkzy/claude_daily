from __future__ import annotations

import hashlib
import shutil
import subprocess
import urllib.request
from pathlib import Path


class MediaManager:
    def __init__(self, temp_dir: Path) -> None:
        self.temp_dir = temp_dir
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def download_thumbnail(self, url: str, destination: Path, dry_run: bool = False) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if dry_run:
            _write_placeholder(destination, seed=url, palette="thumbnail")
            return destination
        urllib.request.urlretrieve(url, destination)
        return destination

    def download_video(self, video_id: str, dry_run: bool = False) -> Path | None:
        if dry_run:
            dummy = self.temp_dir / f"{video_id}.mp4"
            dummy.write_bytes(b"dry-run-video")
            return dummy
        if shutil.which("yt-dlp") is None:
            return None
        output_path = self.temp_dir / f"{video_id}.%(ext)s"
        command = [
            "yt-dlp",
            "-f",
            "mp4[height<=720]/mp4/best",
            "-o",
            str(output_path),
            f"https://www.youtube.com/watch?v={video_id}",
        ]
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if completed.returncode != 0:
            return None
        for file in self.temp_dir.glob(f"{video_id}.*"):
            if file.suffix != ".part":
                return file
        return None

    def extract_frame(self, video_path: Path | None, second: int, destination: Path, dry_run: bool = False) -> Path | None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if dry_run or video_path is None or not video_path.exists():
            _write_placeholder(destination, seed=f"{destination.stem}-{second}", palette="scene")
            return destination
        if shutil.which("ffmpeg") is None:
            return None
        for offset in (0, -2, 2):
            command = [
                "ffmpeg",
                "-y",
                "-ss",
                str(max(second + offset, 0)),
                "-i",
                str(video_path),
                "-frames:v",
                "1",
                str(destination),
            ]
            completed = subprocess.run(command, capture_output=True, text=True, check=False)
            if completed.returncode == 0 and destination.exists():
                return destination
        return None

    def cleanup(self, path: Path | None) -> None:
        if path and path.exists():
            path.unlink()


_PALETTES = {
    "thumbnail": [(244, 239, 230), (217, 119, 87), (124, 92, 73)],
    "scene": [(250, 247, 241), (231, 221, 201), (217, 119, 87)],
    "header": [(217, 119, 87), (185, 94, 64), (31, 27, 22)],
}


def _write_placeholder(destination: Path, seed: str, palette: str) -> None:
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
