"""Assemble the captured source as a self-contained Italian Vite site."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
REF, PUBLIC, SRC = ROOT/'.reference', ROOT/'public', ROOT/'src'
TITLE = 'Rana e Rospo e le macchine sempre più capaci'
ORIGINAL_TITLE = 'Frog and Toad and the Increasingly Capable Machines'
LANGS = ['cs','de','eo','sk','ru','bn','ja','zh']
shutil.copytree(REF/'assets', PUBLIC, dirs_exist_ok=True)
for name in ['reader.css','pageturn.css','sheet.css','reader.js','pageturn.js','simple.js','languages.js']:
    shutil.copy2(REF/name,SRC/name)
shutil.copy2(REF/'illustrations_web_sizes.js',SRC/'sizes.js')
shutil.copy2(REF/'story.js',PUBLIC/'story.js')
languages=(SRC/'languages.js').read_text(encoding='utf-8')
languages=languages.replace("{ lang: 'en', name: 'English', href: 'index.html'", "{ lang: 'en', name: 'English', href: 'en.html'")
languages=languages.replace("{ lang: 'sk',", "{ lang: 'it', name: 'Italiano', href: 'index.html', story: 'story-it.js' },\n  { lang: 'sk',")
(SRC/'languages.js').write_text(languages,encoding='utf-8')

page_turn=(SRC/'pageturn.js').read_text(encoding='utf-8').replace('function createPageTurner(root, options)','export function createPageTurner(root, options)',1)
(SRC/'pageturn.js').write_text(page_turn,encoding='utf-8')
reader="import { createPageTurner } from './pageturn.js';\n"+(SRC/'reader.js').read_text(encoding='utf-8')
reader=re.sub(r'  const SOURCE = \(function \(\) \{.*?\n  \}\)\(\);',"  const SOURCE = 'local';",reader,flags=re.S)
reader=re.sub(r'  function linkHref\(href\) \{.*?\n  \}','  function linkHref(href) { return href;\n  }',reader,count=1,flags=re.S)
reader=re.sub(r'  function trackProgress\(\) \{.*?\n  \}','  function trackProgress() {}',reader,count=1,flags=re.S)
reader=re.sub(r'  function trackFirstTurn\(from, to\) \{.*?\n  \}','  function trackFirstTurn() {}',reader,count=1,flags=re.S)
reader=reader.replace("      status.classList.remove('stacked');", "      const closed = book.classList.contains('closed');\n      status.classList.toggle('stacked', closed && sides[0] + sides[1] + gap > status.clientWidth);")
reader=reader.replace('    onLand(o, { instant }) {','    onLand(o, { instant }) {\n      fitStatus();')
(SRC/'reader.js').write_text(reader,encoding='utf-8')

# Copy the actual font resources used by the original language editions.
font_map={'Noto Serif':'fonts/noto-serif.css'}
font_jobs={}
for lang in LANGS:
    html=(REF/'assets'/(lang+'.html')).read_text(encoding='utf-8')
    for href in re.findall(r'<link[^>]+href="(https://fonts.googleapis.com/css2[^"]+)"[^>]*>',html,re.S):
        href=re.sub(r'\s+','',href).replace('&amp;','&')
        for marker,name,slug in [('Zen+Maru','Zen Maru Gothic','zen-maru-gothic'),('Baloo','Baloo Da 2','baloo-da-2'),('Noto+Serif+SC','Noto Serif SC','noto-serif-sc')]:
            if marker in href: font_jobs[name]=(slug,href)
for name,(slug,href) in font_jobs.items():
    req=Request(href,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'})
    with urlopen(req,timeout=60) as response: css=response.read().decode()
    urls=list(dict.fromkeys(re.findall(r'url\((https://[^)]+)\)',css)))
    folder=PUBLIC/'fonts'/slug
    folder.mkdir(parents=True,exist_ok=True)
    def one(item):
        i,url=item
        filename=str(i)+'.woff2'
        if not (folder/filename).exists():
            with urlopen(url,timeout=60) as response: (folder/filename).write_bytes(response.read())
        return url,filename
    with ThreadPoolExecutor(max_workers=12) as pool:
        for url,filename in pool.map(one,enumerate(urls)): css=css.replace(url,filename)
    (folder/'font.css').write_text(css,encoding='utf-8')
    font_map[name]='fonts/'+slug+'/font.css'
    print('Local font:',name,len(urls),'files',flush=True)

def sanitize(html):
    html=re.sub(r'<script\b[^>]*>.*?</script>','',html,flags=re.S|re.I)
    html=re.sub(r'<link\b[^>]*(?:rel="(?:canonical|alternate|preconnect)"|fonts.googleapis.com)[^>]*>','',html,flags=re.S|re.I)
    html=html.replace('https://www.frogandtoad.ai/illustrations/','illustrations/')
    for css in ['reader','pageturn','sheet']:
        html=html.replace('href="'+css+'.css"','href="/src/'+css+'.css"').replace('href="/'+css+'.css"','href="/src/'+css+'.css"')
    html=re.sub(r'<!--.*?-->','',html,flags=re.S)
    html=re.sub(r'<meta property="og:url"[^>]*>','',html)
    html=html.replace('</head>','<link rel="stylesheet" href="/fonts/noto-serif.css">\n</head>')
    return re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+','\n\n',html)

def italian(html):
    html=html.replace('lang="en"','lang="it"').replace(ORIGINAL_TITLE,TITLE)
    html=html.replace('Frog and Toad face the most modern of challenges','Rana e Rospo affrontano la più moderna delle sfide')
    html=html.replace('Frog and Toad in their workshop surrounded by small helpful robots, from '+TITLE,'Rana e Rospo nel laboratorio, circondati da piccoli robot pronti ad aiutarli')
    return html.replace('Previous page','Pagina precedente').replace('Next page','Pagina successiva').replace('Full screen','Schermo intero')

book=sanitize((REF/'index.html').read_text(encoding='utf-8'))
entry='<script type="module" src="/src/main.jsx"></script>\n'
(ROOT/'index.html').write_text(italian(book).replace('</body>',entry+'</body>'),encoding='utf-8')
(ROOT/'en.html').write_text(book.replace('</body>',entry+'</body>'),encoding='utf-8')
for lang in LANGS:
    html=sanitize((REF/'assets'/(lang+'.html')).read_text(encoding='utf-8'))
    font={'bn':'Baloo Da 2','ja':'Zen Maru Gothic','zh':'Noto Serif SC'}.get(lang)
    if font and font in font_map: html=html.replace('</head>','<link rel="stylesheet" href="/'+font_map[font]+'">\n</head>')
    (ROOT/(lang+'.html')).write_text(html.replace('</body>',entry+'</body>'),encoding='utf-8')
    (PUBLIC/(lang+'.html')).unlink(missing_ok=True)

simple=(SRC/'simple.js').read_text(encoding='utf-8')
simple=simple.replace("const edition = EDITIONS.find(e => e.lang === wanted) || ENGLISH;","const edition = EDITIONS.find(e => e.lang === (wanted || 'it')) || ENGLISH;")
simple=simple.replace("link.href = 'https://fonts.googleapis.com/css2?family=' + FONTS[font] + '&display=swap';","link.href = window.LOCAL_FONT_CSS[font];")
(SRC/'simple.js').write_text(simple,encoding='utf-8')
simple_html=italian(sanitize((REF/'simple.html').read_text(encoding='utf-8')))
simple_html=simple_html.replace('This page needs JavaScript to show the story.','Per leggere la storia, abilita JavaScript nel browser.')
(ROOT/'simple.html').write_text(simple_html.replace('</body>','<script type="module" src="/src/simple-entry.js"></script>\n</body>'),encoding='utf-8')
(SRC/'font-map.js').write_text('window.LOCAL_FONT_CSS = '+json.dumps(font_map)+';\n',encoding='utf-8')
pkg=json.loads((ROOT/'package.json').read_text())
pkg['name']='rana-e-rospo-italiano'
(ROOT/'package.json').write_text(json.dumps(pkg,indent=2)+'\n',encoding='utf-8')
print('Source assembled with Italian home page and all original language editions.')
