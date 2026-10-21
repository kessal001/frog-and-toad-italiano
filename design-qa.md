# Verifica della riproduzione italiana

**final result: passed**

Verifica del 21 ottobre 2026. Sorgente: https://www.frogandtoad.ai/.

## Evidenze e normalizzazione

- Desktop, copertina: `.reference/source-desktop-cover.png` e `.reference/implementation-desktop-cover-final.png`, entrambi 1536 × 695 pixel. Confronto combinato: `.reference/comparison-desktop-cover-final.jpg`.
- Desktop, apertura: `.reference/source-desktop-03-04.png` e `.reference/implementation-desktop-03-verified.png`, entrambi 1536 × 695 pixel; identico stato, pagine 3–4, originale inglese e traduzione italiana.
- Mobile, copertina: `.reference/source-mobile-cover.png` e `.reference/implementation-mobile-cover-final.png`, entrambi 390 × 843 pixel, viewport richiesta 390 × 844; l’arrotondamento del browser interessa entrambe le catture. Confronto combinato: `.reference/comparison-mobile-cover-final.jpg`.
- Le coppie principali sono a pari dimensioni, senza ricampionamento. Le catture rappresentano pixel logici del browser, non il display fisico di un telefono.
- Ulteriori catture di tutte le aperture: `.reference/source-desktop-03-verified.png` fino a `23`, e `.reference/implementation-desktop-03-verified.png` fino a `23`. Le catture sorgente aggiuntive hanno viewport 1536 × 639; quelle italiane 1536 × 695. Sono evidenza di contenuto e ordine delle illustrazioni; la verifica precisa delle proporzioni usa le coppie principali a pari viewport.
- Confronto dei dettagli: carattere e dialoghi dell’apertura, titolo, crediti, icone, immagine e comandi della copertina; le coppie di dettaglio sono salvate insieme alle catture. Non si giudicano colori o testo dalle catture effettuate durante una transizione.
- Controlli aggiuntivi: `.reference/implementation-small-cover.png` a 320 × 568 e `.reference/implementation-tablet-page6.png` a 768 × 1024.
- Build compilata aperta e verificata nel browser locale sulla porta 4174: `.reference/production-cover.png`, `.reference/production-opening.png`.

## Cinque superfici di fedeltà

1. **Caratteri e tipografia:** Noto Serif originale in locale, pesi 400/500/600 e corsivo. Titolo, sottotitolo, crediti e gerarchie conservati. Il motore originale adatta uniformemente il testo: scala italiana finale 0,94 su desktop e 0,86 nel formato mobile verificato. La variazione rispetto all’inglese è intenzionale e mantiene il testo completo nelle pagine, senza tagli.
2. **Spazi e impaginazione:** stessa copertina, dorso, pagine, margini, proporzioni, ombre e posizioni delle frecce. Alla viewport desktop principale il libro aperto misura 892 × 595 CSS px, come il riferimento. Le etichette italiane hanno un adattamento minimo nel piè di pagina per evitarne la sovrapposizione.
3. **Colori e superfici:** stili e texture originali conservati. Carta `#f5eedd`, inchiostro `#2a2318`, legno `#3b2819`, verdi e ombre originali.
4. **Immagini e icone:** tutte le 12 illustrazioni, le due copertine AVIF, le favicon, le icone SVG e le texture provengono dal sito originale e sono locali. Nessuna immagine sostitutiva o approssimazione disegnata a codice. Ordine e percorsi delle illustrazioni verificati contro la storia originale.
5. **Testi e contenuti:** storia completa in italiano, 24 pagine oltre alla copertina; mantenuti i collegamenti alle fonti. Tradotti titolo, crediti, descrizioni delle immagini, lettore, metadati, Informazioni, Contatti e vista semplificata. Conservate le nove lingue originali.

## Correzioni e confronto successivo

- **[P2, risolto] Sovrapposizione del piè di pagina:** le etichette italiane più lunghe entravano nel contatore. Correzione: etichetta `Info` e disposizione su due righe quando la copertina non offre spazio sufficiente. Le catture finali desktop, mobile e 320 px mostrano controlli separati e leggibili.
- **[P2, risolto] Riduzione eccessiva del corpo del testo:** la prima stesura ripeteva una perifrasi lunga per “sandbox”. La traduzione corretta e più concisa “sabbiera” ha portato la scala uniforme da 0,90 a 0,94 su desktop. Ricontrollate tutte le pagine dopo la modifica; nessun testo deborda.
- **Acquisizione:** alcune prime catture precedevano l’ultimo fotogramma dell’animazione. Sono state sostituite con catture a riposo nei file `*-verified.png`; le immagini transitorie non sono state considerate difetti permanenti dell’applicazione.

## Funzionamento verificato

- Tutte le aperture desktop e tutte le pagine 3–24 nel formato mobile: immagini presenti e nessun debordamento. Riscontri in `.reference/desktop-checks.json` e `.reference/mobile-checks.json`.
- Frecce avanti e indietro, limite iniziale e finale, frecce della tastiera, Home e salto a una pagina tramite contatore e Invio.
- Passaggio alla lettura semplificata e ritorno al libro; storia completa con 12 immagini nella vista semplificata.
- Tutte le lingue disponibili si aprono; passaggio italiano/inglese con mantenimento della pagina. Riscontro in `.reference/language-checks.json`.
- Collegamenti a Informazioni, Contatti e ritorno al libro.
- Modulo Contatti: email non valida bloccata dalla validazione; dati di prova validi mostrano il collegamento al modulo originale. Nessun messaggio viene inviato da questa edizione.
- Nessun errore o avviso di console nelle verifiche finali del lettore e della build compilata.
- `npm run build` completato; avvio Windows verificato con `Avvia-sito.ps1 -NoBrowser`.

## Limiti e rifiniture non bloccanti

- Il comando nativo di schermo intero è conservato. Nel browser automatizzato la richiesta non entra in schermo intero, sia sul riferimento sia sulla copia: la modalità nativa resta da provare manualmente.
- Le gesture touch provengono dal motore originale. Verifica responsive nel browser; nessun test su uno smartphone fisico.
- Contatti è un modulo di interfaccia con rinvio al sito originale, non un servizio di invio indipendente.

Nessun problema P0/P1/P2 aperto nelle superfici e interazioni verificate.

**final result: passed**
