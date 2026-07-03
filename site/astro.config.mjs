import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://claude-daily.com",
  integrations: [tailwind()],
  output: "static"
});
