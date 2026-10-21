from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent.parent
REF=ROOT/'.reference'
TITLE='Rana e Rospo e le macchine sempre più capaci'
ORIGINAL='Frog and Toad and the Increasingly Capable Machines'

def clean(name):
    html=(REF/name).read_text(encoding='utf-8')
    html=re.sub(r'<script\b[^>]*>.*?</script>','',html,flags=re.S|re.I)
    html=re.sub(r'<link\b[^>]*(?:rel="(?:canonical|preconnect)"|fonts.googleapis.com)[^>]*>','',html,flags=re.S|re.I)
    html=html.replace('lang="en"','lang="it"').replace(ORIGINAL,TITLE)
    html=html.replace('href="sheet.css"','href="/src/sheet.css"').replace('href="/sheet.css"','href="/src/sheet.css"')
    html=re.sub(r'<!--.*?-->','',html,flags=re.S)
    return html.replace('</head>','<link rel="stylesheet" href="/fonts/noto-serif.css">\n</head>')

about=clean('about.html')
start=about.index('  <h1>')
end=about.index('\n</main>')
about=about[:start]+'''  <h1>Informazioni sul libro</h1>
  <hr class="rule">

  <p>Rana e Rospo e le macchine sempre più capaci è una satira dei libri di Arnold Lobel dedicati a Frog and Toad. Non ha alcun legame con gli eredi o gli editori di Lobel, né il loro patrocinio.</p>

  <p>Questo libro è stato scritto da <a href="https://acesounderglass.com/about-me-2/">Elizabeth Van Nostrand</a> dopo che, per scherzo, aveva chiesto a Claude di spiegare l’incidente di Hugging Face nello stile di Frog and Toad, ottenendo in risposta un racconto a chiave. La trama di fondo è la stessa, come era inevitabile, ma del testo iniziale rimane ben poco. Puoi leggere lo scambio originale <a href="https://claude.ai/share/52385381-9df2-4b39-a127-f583d862dc0c">qui</a>.</p>

  <p>Le illustrazioni sono di <a href="https://www.deviantart.com/hungerartist">HungerArtist</a> che, nonostante lo pseudonimo possa suggerire il contrario, è una persona con decenni di esperienza nell’illustrazione. Se desideri lavorare con lui, Elizabeth ha il permesso di condividere privatamente il suo profilo Upwork.</p>

  <p>Il libro è stato finanziato da Timothy Telleen-Lawton. Grazie, Timothy!</p>

  <h2>Licenza</h2>
  <p>Testo &copy; 2026 Elizabeth Van Nostrand. Illustrazioni &copy; 2026 HungerArtist. Il libro originale è distribuito con licenza <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" target="_blank" rel="license noopener">Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale</a> (CC BY-NC-ND 4.0). Puoi condividerlo liberamente a condizione di citare l’autrice e l’illustratore, non venderlo e non modificarlo. Per altri utilizzi, <a href="contact.html">contatta gli autori</a>.</p>

  <h2>Aggiornamenti</h2>
  <p>Seguici su <a href="https://frogandtoadai.substack.com/?r=64iai2&amp;utm_campaign=pub-share-checklist" target="_blank" rel="noopener">Substack</a>, <a href="https://x.com/frogandtoad_ai" target="_blank" rel="noopener">Twitter</a>, <a href="https://www.facebook.com/people/Frog-and-Toad-Learn-About-AI/61594283794206/" target="_blank" rel="noopener">Facebook</a> o <a href="https://www.instagram.com/frogandtoad_ai/" target="_blank" rel="noopener">Instagram</a>.</p>

  <p class="back"><a href="index.html">&#8249; Torna al libro</a> · <a href="contact.html">Contatti</a></p>'''+about[end:]
about=about.replace('<title>About ·','<title>Informazioni ·')
about=re.sub(r'(<meta name="description" content=")[^"]*',r'\1Scopri chi ha creato il libro e gli eventi reali che lo hanno ispirato',about)
(ROOT/'about.html').write_text(about,encoding='utf-8')

contact=clean('contact.html')
contact=re.sub(r'<!--.*?-->','',contact,flags=re.S)
contact=re.sub(r'<input type="hidden"[^>]*>','',contact)
contact=contact.replace('action="https://api.web3forms.com/submit" method="POST"','')
for old,new in [('Contact ·','Contatti ·'),('>Contact<','>Contatti<'),('Your name','Il tuo nome'),('Your email','La tua email'),('Message','Messaggio'),('>Send<','>Invia<'),('>Elsewhere<','>Altri contatti<'),("You can also reach us through one of the book's accounts:",'Puoi contattare gli autori anche attraverso uno dei profili del libro:'),('Back to the book','Torna al libro'),('>About<','>Informazioni<')]:
    contact=contact.replace(old,new)
contact=re.sub(r'(<meta name="description" content=")[^"]*',r'\1Come contattare gli autori del libro',contact)
contact=contact.replace('</body>','<script type="module" src="/src/contact.js"></script>\n</body>')
(ROOT/'contact.html').write_text(contact,encoding='utf-8')

learn=clean('learn-more.html').replace('Frog and Toad · Learn more','Rana e Rospo · Approfondisci')
learn=learn.replace('Taking you to the article…','Ti stiamo reindirizzando all’articolo…').replace('>Continue<','>Continua<')
(ROOT/'learn-more.html').write_text(learn,encoding='utf-8')
print('Informazioni, Contatti e pagina di approfondimento tradotte.')
