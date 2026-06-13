const clientId = import.meta.env.PUBLIC_ADSENSE_CLIENT_ID;

export function GET() {
  if (!clientId) {
    return new Response("# AdSense クライアント ID 未設定のため ads.txt は空です。\n", {
      headers: { "Content-Type": "text/plain; charset=utf-8" },
    });
  }
  // PUBLIC_ADSENSE_CLIENT_ID は "ca-pub-XXXXXXXXXXXXXXXX" 形式で入る想定。
  // ads.txt の publisher-id は "pub-XXXXXXXXXXXXXXXX" 形式なので "ca-" を落とす。
  const publisherId = clientId.startsWith("ca-") ? clientId.slice(3) : clientId;
  const body = `google.com, ${publisherId}, DIRECT, f08c47fec0942fa0\n`;
  return new Response(body, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
