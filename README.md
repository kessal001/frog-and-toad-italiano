# Rana e Rospo — versione italiana

Riproduzione italiana indipendente del sito https://www.frogandtoad.ai/ acquisito il 21 ottobre 2026.
Copertina, storia completa, descrizioni delle immagini, comandi del lettore,
pagina Informazioni e pagina Contatti sono tradotti in italiano. Le altre nove
edizioni originali restano disponibili nel menu Lingua.

Il lettore conserva le illustrazioni, i caratteri, le texture, le proporzioni,
le animazioni 3D e i comandi dell’originale. Tutte le risorse visive e i font
sono locali. I collegamenti agli autori, alle fonti e ai social aprono i siti
originali. Non sono inclusi i sistemi di pubblicità o analisi dell’originale.

## Aprire il sito

Aprire `Avvia sito.cmd` oppure, da questa cartella:

```powershell
npm install
npm run dev -- --host 127.0.0.1 --port 4173 --strictPort
```

Indirizzo: http://localhost:4173

## Lettura

- Clic sulle frecce o sui lati delle pagine; trascinamento e scorrimento touch.
- Frecce della tastiera e Pagina su/Pagina giù per sfogliare.
- Home per la copertina, Fine per l’ultima pagina.
- G o clic sul numero di pagina per andare a una pagina precisa.
- F per la modalità a schermo intero, se supportata dal browser.
- Semplificato per leggere l’intera storia in una pagina scorrevole.

## Contatti e utilizzo

Il modulo Contatti riproduce l’interfaccia e la validazione. Non invia dati:
mostra il collegamento al modulo originale al momento dell’invio. Per usarlo
come modulo di un sito indipendente occorre collegare il proprio servizio.

Testo originale © 2026 Elizabeth Van Nostrand.
Illustrazioni © 2026 HungerArtist.
Licenza dichiarata dagli autori: CC BY-NC-ND 4.0, consultabile in `about.html`.
La traduzione è un’edizione indipendente, non un’edizione ufficiale.
La pubblicazione della traduzione avviene sulla base del permesso degli autori
confermato dal responsabile del progetto. I diritti sul testo e sulle
illustrazioni rimangono ai rispettivi titolari.

## GitHub Pages

Indirizzo del sito: https://kessal001.github.io/frog-and-toad-italiano/

Il workflow `.github/workflows/pages.yml` compila il progetto e pubblica
`dist/client` a ogni push su `main`. Il percorso base di Vite è configurato
tramite `SITE_BASE`; lo sviluppo locale continua a usare la radice `/`.

Per compilare con il percorso di GitHub Pages in PowerShell:

```powershell
$env:SITE_BASE = '/frog-and-toad-italiano/'
npm run build
```

## File principali

- `public/story-it.js`: storia e interfaccia in italiano.
- `src/reader.js`, `src/pageturn.js`: lettore e animazioni originali adattati a Vite.
- `src/reader.css`, `src/pageturn.css`, `src/sheet.css`: stili originali.
- `public/illustrations` e `public/fonts`: risorse originali conservate localmente.
- `.reference`: sorgenti e catture locali usati per la verifica, esclusi da Git.
- `design-qa.md`: esito delle verifiche visive e funzionali.

`npm run build` genera la versione compilata in `dist/client`.
