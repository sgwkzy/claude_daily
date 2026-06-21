import type { APIRoute } from "astro";
import { buildRssFeed } from "../../lib/feeds";

export const GET: APIRoute = async () => buildRssFeed("ja");
