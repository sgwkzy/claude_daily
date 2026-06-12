import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://sgwkzy.github.io/claude_daily",
  base: "/claude_daily/",
  integrations: [tailwind()],
  output: "static"
});

