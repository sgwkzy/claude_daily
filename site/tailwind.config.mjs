export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        cream: "#F4EFE6",
        paper: "#FAF7F1",
        ink: "#26201A",
        coral: "#F0A04B",
        coralDark: "#D88533",
        salmon: "#E5736A",
        teal: "#69A89C",
        sky: "#9CBED5",
        sun: "#E8B43E",
        clay: "#7C5C49",
        line: "#EADFCB"
      },
      fontFamily: {
        sans: ["'Noto Sans JP'", "system-ui", "sans-serif"],
        display: ["'Noto Serif JP'", "'Noto Sans JP'", "serif"]
      },
      boxShadow: {
        card: "0 18px 40px rgba(38, 32, 26, 0.08)",
        slide: "0 30px 60px rgba(38, 32, 26, 0.10)"
      },
      borderRadius: {
        slide: "28px"
      }
    }
  },
  plugins: []
};
