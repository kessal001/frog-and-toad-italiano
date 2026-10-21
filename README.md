# Rana e Rospo — versione italiana

Traduzione e localizzazione italiana di Luca Pedersoli di *Frog and Toad and the Increasingly Capable Machines*.

Elizabeth Van Nostrand ha accolto la traduzione e l’ha pubblicata sul sito
ufficiale, con credito al traduttore. Per leggere e condividere la versione
italiana, usa **https://frogandtoad.ai/it**: in questo modo le visite vengono
conteggiate sul sito dell’autrice.

Questo repository conserva i sorgenti della versione italiana realizzata a
partire dal sito https://www.frogandtoad.ai/ acquisito il 21 ottobre 2026.
Copertina, storia completa, descrizioni delle immagini, comandi del lettore,
pagina Informazioni e pagina Contatti sono tradotti in italiano. Le altre nove
edizioni originali restano disponibili nel menu Lingua.

Il lettore conserva le illustrazioni, i caratteri, le texture, le proporzioni,
le animazioni 3D e i comandi dell’originale. Tutte le risorse visive e i font
sono locali. I collegamenti agli autori, alle fonti e ai social aprono i siti
originali. Non sono inclusi i sistemi di pubblicità o analisi dell’originale.

## Aprire la copia locale conservata

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
La traduzione italiana è ora ospitata sul sito ufficiale dell’autrice, con
credito a Luca Pedersoli per la traduzione. I diritti sul
testo e sulle illustrazioni rimangono ai rispettivi titolari.

## GitHub Pages

Il vecchio indirizzo https://kessal001.github.io/frog-and-toad-italiano/
reindirizza a **https://frogandtoad.ai/it**.

Il workflow `.github/workflows/pages.yml` pubblica soltanto le pagine di
reindirizzamento in `dist/github-pages` a ogni push su `main`. Copre la pagina
iniziale, le precedenti pagine del lettore, Informazioni, Contatti e gli
indirizzi non più esistenti tramite `404.html`. Ogni pagina include il
collegamento canonico, il reindirizzamento automatico e un link manuale.

Per preparare la pubblicazione GitHub Pages, senza installare dipendenze:

```powershell
npm run build:github-pages
```

I sorgenti del lettore e `npm run build` restano disponibili per la copia
locale conservata e per il precedente flusso Sites; non vengono pubblicati
su GitHub Pages.

## File principali

- `public/story-it.js`: storia e interfaccia in italiano.
- `src/reader.js`, `src/pageturn.js`: lettore e animazioni originali adattati a Vite.
- `src/reader.css`, `src/pageturn.css`, `src/sheet.css`: stili originali.
- `public/illustrations` e `public/fonts`: risorse originali conservate localmente.
- `.reference`: sorgenti e catture locali usati per la verifica, esclusi da Git.
- `design-qa.md`: esito delle verifiche visive e funzionali.
- `scripts/build-github-pages-redirect.mjs`: genera i reindirizzamenti al sito ufficiale.

`npm run build` genera la versione compilata in `dist/client`.
