from pathlib import Path

from batch.media import MediaManager


def test_media_dry_run(tmp_path: Path) -> None:
    media = MediaManager(tmp_path / "tmp")
    thumb = media.download_thumbnail("https://example.com/a.webp", tmp_path / "thumb.webp", dry_run=True)
    video = media.download_video("abc", dry_run=True)
    frame = media.extract_frame(video, 10, tmp_path / "scene-1.webp", dry_run=True)
    assert thumb.exists()
    assert video is not None and video.exists()
    assert frame is not None and frame.exists()
    media.cleanup(video)
    assert not video.exists()

