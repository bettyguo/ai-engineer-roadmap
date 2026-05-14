import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// The site is deployed to https://bettyguo.github.io/ai-engineer-roadmap/,
// so production builds use `/ai-engineer-roadmap/` as the base. Local dev
// uses `/`. CI sets BASE_PATH explicitly.
const base = process.env.BASE_PATH || "/";

export default defineConfig({
  plugins: [react()],
  base,
  build: {
    outDir: "dist",
    sourcemap: false,
    chunkSizeWarningLimit: 1200,
  },
});
