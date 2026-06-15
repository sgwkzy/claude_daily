from __future__ import annotations

import shutil
import subprocess
import urllib.request
from pathlib import Path

from .placeholder import write_placeholder as _write_placeholder


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
