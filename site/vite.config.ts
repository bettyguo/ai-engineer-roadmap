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
    rollupOptions: {
      output: {
        // Split the React Flow library into its own chunk so the initial
        // TopBar/Sidebar paint doesn't carry it. Loaded via React.lazy
        // when the user is ready to see the diagram.
        manualChunks(id) {
          if (id.includes("node_modules/@xyflow")) return "xyflow";
          if (id.includes("node_modules/react-dom")) return "react";
          if (id.includes("node_modules/react/")) return "react";
          return undefined;
        },
      },
    },
  },
});
