import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { fileURLToPath } from "node:url";

export default defineConfig({
  base: process.env.SITE_BASE || "/",
  build: {
    outDir: "dist/client",
    rollupOptions: {
      input: Object.fromEntries(
        ["index", "en", "cs", "de", "eo", "sk", "ru", "bn", "ja", "zh", "simple", "about", "contact", "learn-more"].map(
          page => [page, fileURLToPath(new URL(`./${page}.html`, import.meta.url))],
        ),
      ),
    },
  },
  optimizeDeps: {
    include: ["react", "react-dom/client"],
  },
  server: {
    host: "0.0.0.0",
    allowedHosts: ["terminal.local"],
    warmup: {
      clientFiles: ["./src/main.jsx"],
    },
  },
  plugins: [react()],
});
