#!/usr/bin/env node
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const output = path.join(root, "dist", "github-pages");
const destination = "https://frogandtoad.ai/it";
const pages = [
  "index", "en", "cs", "de", "eo", "sk", "ru", "bn", "ja", "zh",
  "simple", "about", "contact", "learn-more", "404",
];
const html = `<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rana e Rospo · versione italiana sul sito ufficiale</title>
  <meta name="description" content="La traduzione italiana di Rana e Rospo è disponibile sul sito ufficiale dell'autrice.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="${destination}">
  <meta http-equiv="refresh" content="0; url=${destination}">
  <script>window.location.replace(${JSON.stringify(destination)});</script>
  <style>
    body { margin: 0; padding: 3rem 1.5rem; background: #faf9f6; color: #252520; font: 1.125rem/1.6 Georgia, serif; }
    main { max-width: 36rem; margin: 8vh auto; }
    h1 { font-size: 2rem; line-height: 1.2; }
    a { color: #355a38; text-underline-offset: .2em; }
    a:focus-visible { outline: 2px solid currentColor; outline-offset: 5px; }
  </style>
</head>
<body>
  <main>
    <h1>Rana e Rospo</h1>
    <p>La traduzione italiana è ora disponibile sul sito ufficiale dell’autrice.</p>
    <p><a href="${destination}">Leggi la versione italiana su frogandtoad.ai</a></p>
    <p>Se il reindirizzamento automatico non parte, usa il collegamento qui sopra.</p>
  </main>
</body>
</html>
`;

mkdirSync(output, { recursive: true });
writeFileSync(path.join(output, ".nojekyll"), "");
for (const page of pages) {
  writeFileSync(path.join(output, `${page}.html`), html);
  if (page === "index" || page === "404") continue;
  const directory = path.join(output, page);
  mkdirSync(directory, { recursive: true });
  writeFileSync(path.join(directory, "index.html"), html);
}

console.log(`GitHub Pages redirect prepared in dist/github-pages → ${destination}`);
