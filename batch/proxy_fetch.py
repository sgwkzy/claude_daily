#!/usr/bin/env python3
"""Tor 経由で HTTP リクエストを送る軽量ラッパー。

IP ブロックされたサイトへ、自分の実 IP ではなく Tor の出口 IP 経由でアクセスする
ためのスクリプト。ブラウザ全体や OS の通信には影響せず、このスクリプトを通した
リクエストだけが Tor 経由になる（＝「そのサイトのときだけ別 IP」を実現する）。

前提:
  - ローカルで Tor が起動しており、SOCKS5 が listen していること。
    既定ポートは 9050（tor.exe スタンドアロン / Linux / macOS）。
    Tor Browser は 9150 を使うので --proxy socks5h://127.0.0.1:9150 を指定。
    環境変数 PROXY_FETCH_PROXY でも上書き可能。
  - (任意) 出口 IP のローテーションを使う場合は ControlPort 9051 を有効にすること。

使い方:
  python proxy_fetch.py --check                                       # 動作確認
  python proxy_fetch.py https://example.com                           # 取得
  python proxy_fetch.py --proxy socks5h://127.0.0.1:9150 --check      # Tor Browser
  python proxy_fetch.py --rotate https://...                           # IP 切替

詳細は README.md を参照。
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from typing import Optional

import requests

# --- 設定 -------------------------------------------------------------------

# socks5h の "h" が重要: ホスト名の DNS 解決も Tor 側で行うことで、
# DNS リーク（問い合わせから実 IP / アクセス先が漏れること）を防ぐ。
DEFAULT_TOR_SOCKS_PROXY = "socks5h://127.0.0.1:9050"
TOR_SOCKS_PROXY = os.environ.get("PROXY_FETCH_PROXY", DEFAULT_TOR_SOCKS_PROXY)
TOR_CONTROL_PORT = 9051

# ブロック / レート制限とみなして出口 IP の切替を試みるステータスコード。
BLOCK_STATUS = {403, 429, 503}

# 出口 IP 確認に使う、軽量で素直に IP を返すエンドポイント。
IP_ECHO_URL = "https://api.ipify.org?format=json"

DEFAULT_HEADERS = {
    # 既定の python-requests UA はブロックされやすいので一般的なブラウザ UA を使う。
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
}


# --- セッション / プロキシ ----------------------------------------------------

def make_session(proxy: Optional[str] = None) -> requests.Session:
    """Tor の SOCKS5 プロキシを経由する requests.Session を返す。

    proxy が None の場合は環境変数 / デフォルト値 (9050) を使う。
    """
    if proxy is None:
        proxy = TOR_SOCKS_PROXY
    session = requests.Session()
    session.proxies.update({"http": proxy, "https": proxy})
    session.headers.update(DEFAULT_HEADERS)
    return session


def current_ip(session: Optional[requests.Session] = None,
               timeout: int = 30) -> Optional[str]:
    """現在の出口（見かけ上の）IP を返す。取得失敗時は None。

    session を渡せばそのプロキシ経由の IP、None なら直結（プロキシなし）の IP。
    """
    try:
        if session is None:
            resp = requests.get(IP_ECHO_URL, headers=DEFAULT_HEADERS,
                                timeout=timeout)
        else:
            resp = session.get(IP_ECHO_URL, timeout=timeout)
        resp.raise_for_status()
        return resp.json().get("ip")
    except requests.RequestException as exc:
        print(f"[warn] IP 取得に失敗: {exc}", file=sys.stderr)
        return None


# --- 出口 IP のローテーション -------------------------------------------------

def renew_identity(control_port: int = TOR_CONTROL_PORT,
                   password: Optional[str] = None,
                   wait: float = 5.0) -> bool:
    """Tor に NEWNYM シグナルを送り、新しい出口 IP を要求する。

    ControlPort が有効でないと使えない（README の torrc 設定参照）。
    成功すれば True。stem 未インストールや接続失敗時は False。
    """
    try:
        from stem import Signal
        from stem.control import Controller
    except ImportError:
        print("[warn] stem が未インストールのため IP ローテーション不可 "
              "(pip install stem)", file=sys.stderr)
        return False

    try:
        with Controller.from_port(port=control_port) as controller:
            # password が None ならクッキー認証 (CookieAuthentication 1) を試みる。
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
        # 新しい回路が張られるまで少し待つ。
        time.sleep(wait)
        return True
    except Exception as exc:  # stem は多様な例外を投げるため広めに捕捉する。
        print(f"[warn] 出口 IP のローテーションに失敗: {exc}", file=sys.stderr)
        return False


# --- 取得本体 ----------------------------------------------------------------

def fetch(url: str,
          *,
          session: Optional[requests.Session] = None,
          retries: int = 3,
          rotate_on_block: bool = True,
          timeout: int = 30,
          control_port: int = TOR_CONTROL_PORT,
          control_password: Optional[str] = None) -> requests.Response:
    """url を Tor 経由で取得する。ブロック検知時は出口 IP を切替えて再試行。

    retries: 最大リトライ回数（指数バックオフ 2,4,8...秒）。
    rotate_on_block: 403/429/503 を受けたとき renew_identity() を試すか。
    例外を投げずに、最後に得た Response を返す（呼び出し側で status を確認する）。
    """
    own_session = session is None
    if own_session:
        session = make_session()

    last_exc: Optional[Exception] = None
    last_resp: Optional[requests.Response] = None
    try:
        for attempt in range(retries + 1):
            try:
                resp = session.get(url, timeout=timeout)
                last_resp = resp
                if resp.status_code in BLOCK_STATUS:
                    print(f"[info] HTTP {resp.status_code}（ブロック/制限の可能性）"
                          f" attempt={attempt}", file=sys.stderr)
                    if rotate_on_block and attempt < retries:
                        renew_identity(control_port=control_port,
                                       password=control_password)
                        continue
                return resp
            except requests.RequestException as exc:
                last_exc = exc
                print(f"[warn] リクエスト失敗 attempt={attempt}: {exc}",
                      file=sys.stderr)

            if attempt < retries:
                backoff = 2 ** (attempt + 1)
                time.sleep(backoff)

        if last_resp is not None:
            return last_resp
        raise last_exc if last_exc else RuntimeError("取得に失敗しました")
    finally:
        if own_session:
            session.close()


# --- 自己テスト / CLI --------------------------------------------------------

def run_check(proxy: Optional[str] = None) -> int:
    """直結 IP と Tor 経由 IP を比較し、別 IP になっていることを確認する。"""
    used_proxy = proxy or TOR_SOCKS_PROXY
    print(f"使用プロキシ           : {used_proxy}")

    direct = current_ip(None)
    print(f"直結 IP (プロキシなし) : {direct or '取得失敗'}")

    session = make_session(proxy=used_proxy)
    try:
        tor_ip = current_ip(session)
    finally:
        session.close()
    print(f"Tor 経由 IP            : {tor_ip or '取得失敗（Tor は起動済み？）'}")

    # Tor ネットワーク上かどうかを Tor 公式エンドポイントでも確認する。
    try:
        s = make_session(proxy=used_proxy)
        try:
            r = s.get("https://check.torproject.org/api/ip", timeout=30)
            is_tor = r.json().get("IsTor")
            print(f"check.torproject.org   : IsTor={is_tor}")
        finally:
            s.close()
    except requests.RequestException as exc:
        print(f"check.torproject.org   : 確認失敗 ({exc})")

    if tor_ip and tor_ip != direct:
        print("\nOK: 出口 IP が実 IP と異なっています。Tor 経由で動作しています。")
        return 0
    if tor_ip and direct is None:
        print("\nOK: Tor 経由 IP を取得できました（直結 IP は環境都合で取得不可）。")
        return 0
    print("\nNG: 別 IP を確認できませんでした。Tor の起動と 9050 を確認してください。")
    return 1


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Tor 経由で URL を取得する（IP ブロック回避用）。")
    parser.add_argument("url", nargs="?", help="取得する URL")
    parser.add_argument("--check", action="store_true",
                        help="直結 IP と Tor 経由 IP を比較して動作確認する")
    parser.add_argument("--rotate", action="store_true",
                        help="取得前に出口 IP を切り替える (要 ControlPort)")
    parser.add_argument("--retries", type=int, default=3,
                        help="最大リトライ回数 (default: 3)")
    parser.add_argument("--timeout", type=int, default=30,
                        help="タイムアウト秒 (default: 30)")
    parser.add_argument("--control-password", default=None,
                        help="Tor ControlPort のパスワード (任意)")
    parser.add_argument("--show-body", action="store_true",
                        help="レスポンス本文を標準出力に表示する")
    parser.add_argument("--proxy", default=None,
                        help=("SOCKS5 プロキシ URL を指定 (例: "
                              "socks5h://127.0.0.1:9150 ← Tor Browser, "
                              "socks5h://127.0.0.1:1080 ← ssh -D). "
                              "未指定なら環境変数 PROXY_FETCH_PROXY か "
                              "デフォルトの 9050 を使用"))
    args = parser.parse_args(argv)

    if args.check:
        return run_check(proxy=args.proxy)

    if not args.url:
        parser.error("URL を指定するか --check を使ってください")

    if args.rotate:
        renew_identity(password=args.control_password)

    session = make_session(proxy=args.proxy)
    resp = fetch(args.url,
                 session=session,
                 retries=args.retries,
                 timeout=args.timeout,
                 control_password=args.control_password)

    print(f"HTTP {resp.status_code}  {resp.url}", file=sys.stderr)
    exit_ip_session = make_session(proxy=args.proxy)
    try:
        print(f"出口 IP: {current_ip(exit_ip_session) or '不明'}", file=sys.stderr)
    finally:
        exit_ip_session.close()
    if args.show_body:
        sys.stdout.write(resp.text)
    else:
        print(f"本文 {len(resp.content)} バイトを取得（--show-body で表示）",
              file=sys.stderr)
    return 0 if resp.status_code < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main())
