"""スタンドアロン Tor を必要時だけ起動・終了する。

YouTube 取得が失敗したときのフォールバック経路（proxy_fetch 経由の Tor 取得）でだけ
Tor を立ち上げ、処理が終わったら自分で起動した分だけ落とす。既に 9050 で Tor が
listen 中（例: nyaa-downloader の常駐 Tor）なら、それを流用して終了時にも止めない。
"""
from __future__ import annotations

import logging
import socket
import subprocess
import time
from pathlib import Path

logger = logging.getLogger(__name__)

# nyaa-downloader と同じ Tor Browser 同梱の tor.exe を流用する。
TOR_EXE = r"C:\Users\User\Tor Browser\Browser\TorBrowser\Tor\tor.exe"
TORRC = Path(__file__).parent / "tor" / "torrc"
SOCKS_PORT = 9050


def _listening(port: int = SOCKS_PORT) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex(("127.0.0.1", port)) == 0


class ManagedTor:
    """Tor の起動/終了をコンテキスト管理する。`ensure()` で遅延起動する。

    使い方:
        with ManagedTor() as tor:
            ...
            tor.ensure()          # ここで初めて（必要なら）起動
            ... proxy_fetch.fetch(...) ...
        # 自分で起動した場合のみ __exit__ で停止
    """

    def __init__(self) -> None:
        self._proc: subprocess.Popen | None = None
        self._started = False

    def __enter__(self) -> "ManagedTor":
        return self

    def __exit__(self, *_exc) -> None:
        if self._started and self._proc is not None:
            logger.info("自前起動した Tor を終了します。")
            self._proc.terminate()
            try:
                self._proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self._proc.kill()
            self._proc = None
            self._started = False

    def ensure(self, wait_ready: float = 60.0) -> bool:
        """Tor が使える状態であることを保証する。必要なら起動して回路完成まで待つ。"""
        if _listening():
            return True  # 既存の Tor（nyaa 等）を流用。終了時に止めない。
        if not Path(TOR_EXE).exists():
            logger.warning("tor.exe が見つかりません: %s", TOR_EXE)
            return False
        logger.info("Tor を起動します（9050）。")
        self._proc = subprocess.Popen(
            [TOR_EXE, "-f", str(TORRC)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        self._started = True
        return self._wait_until_ready(wait_ready)

    def _wait_until_ready(self, timeout: float) -> bool:
        """SOCKS ポートが開き、Tor 経由で実際に出口 IP を取れるまで待つ。"""
        from . import proxy_fetch

        deadline = time.time() + timeout
        while time.time() < deadline:
            if _listening():
                session = proxy_fetch.make_session()
                try:
                    if proxy_fetch.current_ip(session):
                        logger.info("Tor の回路が完成しました。")
                        return True
                finally:
                    session.close()
            time.sleep(2)
        logger.warning("Tor が時間内に使える状態になりませんでした（%ss）。", timeout)
        return False
