#!/usr/bin/env python3
"""Build the static Puheklinikka site from the verified Squarespace capture.

Source: /mnt/project-files/site-inventory/raw-html (authoritative page HTML).
Agreed changes: /mnt/project-files/site-plan/decisions.md. Every text change
is applied by EDITS below and asserted, so nothing changes silently.
Output: ../site (static files for GitHub Pages).
"""
import json, os, re, shutil, sys, html, unicodedata
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag, Comment
sys.path.insert(0, str(Path(__file__).resolve().parent))
import style_a

ROOT = Path(__file__).resolve().parent
INV = Path('/mnt/project-files/site-inventory')
RAW = INV / 'raw-html'
OUT = ROOT.parent / 'site'
ASSETS = ROOT / 'assets'

# ---------------------------------------------------------------- pages
# slug -> (raw file, menu title for <title>, lang)
PAGES = {
    '':                              ('index.html', 'Etusivu', 'fi'),
    'asiantuntijat':                 ('asiantuntijat.html', 'Terapeutit', 'fi'),
    'mit-puheterapia-on':            ('mit-puheterapia-on.html', None, 'fi'),
    'ryhmmuotoinen-terapia':         ('ryhmmuotoinen-terapia.html', None, 'fi'),
    'niterapia':                     ('niterapia.html', None, 'fi'),
    'palvelut-lheisille':            ('palvelut-lheisille.html', None, 'fi'),
    'lukitutkimus':                  ('lukitutkimus.html', None, 'fi'),
    'arviot-ja-konsultointi':        ('arviot-ja-konsultointi.html', None, 'fi'),
    'koulutukset':                   ('koulutukset.html', None, 'fi'),
    'new-page':                      ('new-page.html', None, 'fi'),
    'toimintatavat-ja-arvot':        ('toimintatavat-ja-arvot.html', None, 'fi'),
    'new-page-1':                    ('new-page-1.html', None, 'fi'),
    'tapahtumia-aiemmilta-vuosilta': ('tapahtumia-aiemmilta-vuosilta.html', None, 'fi'),
    'about-puheklinikka':            ('about-puheklinikka.html', None, 'sv'),
    'mit-puheterapia-on-1':          ('mit-puheterapia-on-1.html', None, 'sv'),
    'about-puheklinikka-2':          ('about-puheklinikka-2.html', None, 'en'),
    'our-services':                  ('our-services.html', None, 'en'),
    'new-page-2':                    ('new-page-2.html', None, 'fi'),
}
# Old address kept working by forwarding (decision 9: keep addresses).
REDIRECTS = {'nanalehtinengmailcom': ''}

# Menu exactly as on the live site (site-wide.md). Folder label trailing space dropped.
MENU = [
    ('Etusivu', '', None),
    ('Terapeutit', 'asiantuntijat', None),
    ('Palvelut', None, [
        ('Aikuisneurologiset häiriöt', 'mit-puheterapia-on'),
        ('Ryhmämuotoinen kuntoutus', 'ryhmmuotoinen-terapia'),  # swapped with Nielemishäiriöt (Nana, 2026-10-04)
        # TRIAL (Nana, 2026-10-04): two new services, text to come from Nana. Revert: remove these two lines
        # and their entries in NEW_PAGES.
        ('Nielemishäiriöt', 'nielemishairiot'),
        ('Puheen sujuvuuden häiriöt', 'puheen-sujuvuuden-hairiot'),
        ('Ääniterapia', 'niterapia'),
        ('LUKI-tutkimus', 'lukitutkimus'),  # before Palvelut läheisille (Nana, 2026-10-04)
        ('Palvelut läheisille', 'palvelut-lheisille'),
        ('Tutkimus ja konsultointi', 'arviot-ja-konsultointi'),
        ('Koulutukset', 'koulutukset'),
        ('Sovellukset ja tuotteet', 'new-page'),  # label shortened (Nana, 2026-10-04); page title unchanged
    ]),
    # Split in two (Nana, 2026-10-03)
    ('Tapahtumat', None, [
        ('Ajankohtaista', 'new-page-1'),
        ('Menneet tapahtumat', 'tapahtumia-aiemmilta-vuosilta'),
    ]),
    ('Arvot ja toimintatavat', 'toimintatavat-ja-arvot', None),
    ('Asiakaspalaute', 'new-page-2', None),  # moved before På svenska (Nana, 2026-10-03)
    ('På svenska', None, [
        ('Introduktion', 'about-puheklinikka'),
        ('Våra tjänster', 'mit-puheterapia-on-1'),
    ]),
    ('In English', None, [
        ('About Puheklinikka', 'about-puheklinikka-2'),
        ('Our services', 'our-services'),
    ]),
]
NEW_PAGES = {  # TRIAL (Nana, 2026-10-04): Palvelut pages with no text yet
    'nielemishairiot': 'Nielemishäiriöt',
    'puheen-sujuvuuden-hairiot': 'Puheen sujuvuuden häiriöt',
}
CUR = ' aria-current="page"'
FOLDER_LANG = {'På svenska': 'sv', 'In English': 'en'}

OFFICE_EMAIL = 'toimisto@puheklinikka.net'

# ------------------------------------------------- new UI text (flagged)
# Text that does not exist on the live site. Listed in CHANGES.md for Nana.
UI = {
    'skip': 'Siirry sisältöön',
    'menu': 'Valikko',
    'nav_label': 'Päävalikko',
    'social_label': 'Puheklinikka sosiaalisessa mediassa',
}
# Alt texts for images that are links or carry text (decision: drafted, flagged).
ALT = {
    'lookbook-thumb.jpg': 'Sanapsis',
    'screen.jpeg': 'Sanapsis+',
    'Kommunikaatiokurssi+syyskuu.png': 'Tule mukaan! Kommunikaatiokuntoutuskurssi Turun Caribiaan! Seuraava kurssi alkaa 7.9.2026. Mukaan mahtuu vielä! Coronaria ja Puheklinikka yhteistyössä.',
    'Kommunikaatiokurssipromo.jpg': 'Tule mukaan! Kommunikaatiokuntoutuskurssi Turun Caribiaan! Seuraava kurssi alkaa 8. kesäkuuta. Mukaan mahtuu vielä! Coronaria ja Puheklinikka yhteistyössä.',
    'IMG_1119.PNG': 'Sanapsis-sovelluksen uusi ilme: Production, Comprehension, Reading, Writing, Semantics, Perseveration',
}
MAP_TITLE = {  # iframe titles, built from the address text on the homepage
    'Turku': 'Kartta: Käsityöläiskatu 4a, Turku',
    'Helsinki': 'Kartta: Kumpulantie 1 A, Helsinki',
}

# ------------------------------------------------- agreed text edits
# (slug, old, new, expected count). Applied to the final page HTML.
EDITS = [
    ('', 'Yhteyenotto', 'Yhteydenotto', 1),                                   # B1
    ('lukitutkimus', 'tarvittatessa', 'tarvittaessa', 1),                     # B1
    ('new-page-1', 'korvaavata tahosta', 'korvaavasta tahosta', 1),           # B1
    ('our-services', '4–6 sessions', '3–5 sessions', 1),                      # B3
    ('mit-puheterapia-on-1', 'FPA:s, stadens, kommunens eller', 'FPA:s, välfärdsområdets eller', 1),  # B4
    ('new-page', '<p>ehtävien lisäksi', '<p>Tehtävien lisäksi', 1),
    ('ryhmmuotoinen-terapia', '>Lisätietoa vuoden 2026 ryhmistä<', '>Lataa esite<', 1),  # Nana 2026-10-04
    ('ryhmmuotoinen-terapia', 'kootaan parhailaan', 'kootaan parhaillaan', 2),  # typo, Nana 2026-10-04             # Nana 2026-10-03
    ('new-page', '<h2>Sanapsis</h2>', '<h2>SanapsisPro</h2>', 1),  # Nana 2026-10-04
    ('new-page', '<strong>Sanapsis</strong> on Puheklinikalla', '<strong>SanapsisPro</strong> on Puheklinikalla', 1),  # Nana 2026-10-04
    ('new-page', '<img alt="Sanapsis" decoding="async" height="300" loading="lazy" src="../images/1615150163682_lookbook-thumb.jpg" width="400"/>',
     '<img alt="SanapsisPro-sovelluksen päävalikko" decoding="async" height="750" loading="lazy" src="../images/sanapsispro-paavalikko.jpg" width="1024"/>', 1),  # Nana's new image 2026-10-04
    ('ryhmmuotoinen-terapia', '<p>Tervetuloa mukaan! </p><p>Ilmoittaudu mukaan <a href="mailto:annemari.hongell@puheklinikka.net?subject=Ilmoittautuminen%20SpeakOut%20jatkokurssiin%20tapaamiseen">sähköpostitse</a> tai täyttämällä <a href="../asiantuntijat/" rel="noopener" target="_blank">yhteydenottolomake</a>. </p>',
     '<p>Ilmoittaudu sähköpostitse <a href="mailto:annemari.hongell@puheklinikka.net?subject=Ilmoittautuminen%20SpeakOut%20jatkokurssiin%20tapaamiseen">tästä</a>. Tervetuloa mukaan!</p>', 1),  # Nana 2026-10-04
    ('ryhmmuotoinen-terapia', '<p>Voit ilmoittautua myös ottamalla yhteyttä puheterapeutti Annemari Hongelliin tai Riitta Saareen. </p>', '', 1),  # Nana 2026-10-04
    ('', 'ohjaamaan sinut odotustilaan.</p></div>', 'ohjaamaan sinut odotustilaan.</p><p>Tilojen välittömään läheisyyteen pääsee esteettömästi, ja tiloissa voi liikkua itsenäisesti tai avustettuna henkilökohtaisten apuvälineiden avulla.</p></div>', 1),  # Nana 2026-10-04
    ('', 'toimitilojen odotustilasta. </p></div>', 'toimitilojen odotustilasta. </p><p>Tilojen välittömään läheisyyteen pääsee esteettömästi, ja tiloissa voi liikkua itsenäisesti tai avustettuna henkilökohtaisten apuvälineiden avulla.</p></div>', 1),  # Nana 2026-10-04
    ('toimintatavat-ja-arvot', 'Laki sosiaali-ja terveydenhuollon asiakastietojen käsittelystä (703/2023). </p>',
     'Laki sosiaali-ja terveydenhuollon asiakastietojen käsittelystä (703/2023). </p><p>Verkkosivustomme täyttää digitaalisten palvelujen tarjoamisesta annetun lain (306/2019) saavutettavuusvaatimukset. <a href="../saavutettavuusseloste/">Saavutettavuusseloste</a></p>', 1),  # Nana 2026-10-04
    ('', 'Käynti-ja postiosoite', 'Käynti- ja postiosoite', 1),  # hyphen spacing fixed (Nana, 2026-10-04)
    ('asiantuntijat', 'Voit tutustua osaamiseemme tarkemmin kuvaa napauttamalla.', 'Saat lisätietoja napauttamalla.', 1),  # Nana 2026-10-03; full stop added (flagged)
]
# Broken /yhteystiedot links -> Terapeutit (B2). Count checked per page.
YHTEYS_EXPECTED = {'': 1, 'about-puheklinikka': 1, 'about-puheklinikka-2': 1,
                   'ryhmmuotoinen-terapia': 1, 'tapahtumia-aiemmilta-vuosilta': None}

LOG = []          # change log lines for CHANGES.md
IMAGES_USED = {}  # cdn file name -> local name
WARN = []

# ---------------------------------------------------------------- helpers
def rel(depth, target):
    """Relative URL from a page at `depth` (0 = root) to site path `target`."""
    prefix = '../' * depth
    return (prefix + target) if (prefix + target) else './'

def page_href(depth, slug):
    return rel(depth, (slug + '/') if slug else '')

def load_image_map():
    m = {}
    for line in (INV / 'image-urls.txt').read_text().splitlines():
        if line.startswith('#') or not line.strip():
            continue
        local, url = line.split('\t')[:2]
        m[url.split('?')[0]] = local
    return m
IMG_MAP = load_image_map()

INTERNAL = set(PAGES) | set(REDIRECTS)
DROPPED = {'aivoverenkiertohirit', 'etenevt-neurologiset-sairaudet', 'kehitykselliset-kielihirt',
           'tapaturmaiset-aivovammat', 'terapeutit-copy', 'new-page-3'}

def fix_href(href, depth, slug):
    if href is None:
        return None
    h = href.strip()
    m = re.match(r'^(?:https?://(?:www\.)?puheklinikka\.net)?(/[^?#]*)?([?#].*)?$', h)
    if h.startswith(('mailto:', 'tel:')) or (h.startswith('//') and 'puheklinikka.net' not in h):
        return 'https:' + h if h.startswith('//') else h
    if m and (h.startswith('/') or 'puheklinikka.net' in h):
        path = (m.group(1) or '/').strip('/')
        if path.startswith('s/'):
            return rel(depth, path)
        if path == 'yhteystiedot':
            LOG.append((slug, 'link', '/yhteystiedot (404) → Terapeutit (/asiantuntijat)'))
            return page_href(depth, 'asiantuntijat')
        if path in INTERNAL:
            return page_href(depth, path)
        if path in DROPPED:
            WARN.append(f'{slug}: link to dropped page {path}')
            return page_href(depth, path)
        WARN.append(f'{slug}: unknown internal link {href}')
        return h
    return h

def clean_attrs(tag, depth, slug):
    for t in [tag] + list(tag.find_all(True)):
        keep = {}
        for k, v in t.attrs.items():
            if k == 'href':
                keep['href'] = fix_href(v, depth, slug)
            elif k == 'target' and v == '_blank':
                keep['target'] = '_blank'; keep['rel'] = 'noopener'
            elif k in ('colspan', 'rowspan', 'lang'):
                keep[k] = v
        t.attrs = keep
    for s in tag.find_all('span'):
        s.unwrap()
    for a in tag.find_all('a'):
        if not a.get_text(strip=True) and not a.find('img'):
            LOG.append((slug, 'tech', f'removed an invisible empty link to {a.get("href")} (fails WCAG 2.4.4)'))
            a.unwrap()
    return tag

def is_empty_html(frag):
    return not frag.get_text(strip=True) and not frag.find(['img', 'iframe', 'hr'])

# ---------------------------------------------------------------- blocks
def conv_text(b, depth, slug):
    c = b.select_one('.sqs-html-content')
    if c is None:
        return ''
    c = clean_attrs(BeautifulSoup(str(c), 'html.parser').div, depth, slug)
    # Empty paragraphs used as spacing on Squarespace: keep as spacing only
    for p in c.find_all('p'):
        if not p.get_text(strip=True) and not p.find(['img', 'br']):
            p.decompose()
    return ''.join(str(x) for x in c.contents).strip()

def image_local(url):
    base = url.split('?')[0]
    if base in IMG_MAP:
        return IMG_MAP[base]
    WARN.append(f'image not in inventory: {url}')
    return None

def conv_image(b, depth, slug):
    img = b.find('img')
    url = img.get('data-src') or img.get('src')
    local = image_local(url)
    if not local:
        return ''
    IMAGES_USED[local] = True
    fname = url.split('?')[0].rsplit('/', 1)[-1]
    alt = ALT.get(fname, img.get('alt') or '')
    if fname in ALT:
        LOG.append((slug, 'alt', f'{fname}: alt="{alt}" (new text)'))
    w, h = (img.get('data-image-dimensions') or 'x').split('x') if img.get('data-image-dimensions') else ('', '')
    size = f' width="{w}" height="{h}"' if w and h else ''
    tag = f'<img src="{rel(depth, "images/" + web_name(local))}" alt="{html.escape(alt, quote=True)}"{size} loading="lazy" decoding="async">'
    a = b.find('a')
    if a and a.get('href'):
        href = fix_href(a['href'], depth, slug)
        tgt = ' target="_blank" rel="noopener"' if a.get('target') == '_blank' else ''
        if not alt:
            WARN.append(f'{slug}: linked image without alt {fname}')
        tag = f'<a href="{html.escape(href, quote=True)}"{tgt}>{tag}</a>'
    cap = b.select_one('.image-caption')
    capt = ''
    if cap and cap.get_text(strip=True):
        capt = '<figcaption>' + ''.join(str(x) for x in clean_attrs(cap, depth, slug).contents) + '</figcaption>'
    return f'<figure class="img">{tag}{capt}</figure>'

def conv_button(b, depth, slug):
    a = b.find('a')
    text = a.get_text(' ', strip=True)
    href = fix_href(a.get('href'), depth, slug)
    tgt = ' target="_blank" rel="noopener"' if a.get('target') == '_blank' else ''
    cont = b.select_one('.sqs-block-button-container')
    align = 'center'
    if cont:
        for c in cont.get('class', []):
            m = re.match(r'sqs-block-button-container--(\w+)', c)
            if m: align = m.group(1)
    return f'<p class="btn-wrap {align}"><a class="btn" href="{html.escape(href, quote=True)}"{tgt}>{html.escape(text)}</a></p>'

def conv_markdown(b, depth, slug):
    c = b.select_one('.sqs-block-content')
    c = clean_attrs(BeautifulSoup(str(c), 'html.parser').div, depth, slug)
    if is_empty_html(c):
        return ''
    return ''.join(str(x) for x in c.contents).strip()

def conv_form(b, depth, slug):
    # Decision 7: forms become an email link. Link text is the address itself (no new wording).
    LOG.append((slug, 'form', f'Squarespace form replaced with email link {OFFICE_EMAIL}'))
    return f'<p class="email-link"><a href="mailto:{OFFICE_EMAIL}">{OFFICE_EMAIL}</a></p>'

def conv_map(b, depth, slug):
    ctx = json.loads(b.select_one('[data-context]')['data-context'])
    loc = ctx['location']
    city = 'Helsinki' if 'Helsinki' in loc.get('addressLine2', '') else 'Turku'
    title = MAP_TITLE[city]
    LOG.append((slug, 'map', f'map embed title="{title}" (new text)'))
    src = f'https://maps.google.com/maps?q={loc["mapLat"]},{loc["mapLng"]}&z={loc.get("mapZoom", 12)}&output=embed'
    return f'<div class="map"><iframe src="{html.escape(src, quote=True)}" title="{title}" loading="lazy"></iframe></div>'

def conv_code(b, depth, slug):
    if b.find('stand-card') is not None:
        LOG.append((slug, 'drop', 'hidden chat box ("Kysy puheterapeutilta!") removed (decision D2)'))
        return ''
    ifr = b.find('iframe')
    if ifr is not None:
        src = ifr['src']
        LOG.append((slug, 'iframe', 'Google feedback form embed kept; added title="Asiakaspalaute" (new text)'))
        return f'<div class="embed"><iframe src="{html.escape(src, quote=True)}" title="Asiakaspalaute" height="{ifr.get("height", "1666")}"></iframe></div>'
    WARN.append(f'{slug}: unknown code block')
    return ''

def convert_block(b, depth, slug):
    cls = b.get('class', [])
    kind = b.get('data-sqsp-block')
    if 'sqs-block-html' in cls:      out = conv_text(b, depth, slug)
    elif 'sqs-block-image' in cls:   out = conv_image(b, depth, slug)
    elif 'sqs-block-button' in cls:  out = conv_button(b, depth, slug)
    elif 'sqs-block-markdown' in cls: out = conv_markdown(b, depth, slug)
    elif 'sqs-block-form' in cls:    out = conv_form(b, depth, slug)
    elif 'sqs-block-map' in cls:     out = conv_map(b, depth, slug)
    elif 'sqs-block-code' in cls:    out = conv_code(b, depth, slug)
    elif 'sqs-block-horizontalrule' in cls: out = '<hr>'
    elif 'sqs-block-spacer' in cls:  out = '<div class="spacer" aria-hidden="true"></div>'
    else:
        WARN.append(f'{slug}: unhandled block {cls}'); out = ''
    if not out:
        return ''
    extra = []
    if 'float' in cls:
        extra.append('float-right' if 'float-right' in cls else 'float-left')
        span = next((c for c in cls if c.startswith('span-')), 'span-6')
        extra.append(span)
    return f'<div class="block {" ".join(extra)}">{out}</div>' if extra else out

def convert_layout(node, depth, slug):
    parts = []
    for ch in node.children:
        if not isinstance(ch, Tag):
            continue
        cls = ch.get('class', [])
        if 'sqs-block' in cls:
            parts.append(convert_block(ch, depth, slug))
        elif 'row' in cls:
            inner = convert_layout(ch, depth, slug)
            if inner.strip():
                parts.append(f'<div class="row">{inner}</div>')
        elif 'col' in cls:
            span = next((c for c in cls if c.startswith('span-')), 'span-12')
            inner = convert_layout(ch, depth, slug)
            parts.append(f'<div class="col {span}">{inner}</div>')
        else:
            parts.append(convert_layout(ch, depth, slug))
    return '\n'.join(p for p in parts if p)

def simplify(htmltext):
    """Unwrap single full-width rows/cols so the markup stays readable."""
    prev = None
    while prev != htmltext:
        prev = htmltext
        htmltext = re.sub(r'<div class="row"><div class="col span-12">((?:(?!<div class="row">).)*?)</div></div>', r'\1', htmltext, flags=re.S)
    return htmltext

# ---------------------------------------------------------------- images
BIG_PNG_AS_JPEG = set()  # large photo-like PNGs without transparency are served as JPEG

def web_name(local):
    # ASCII-only file names: safer for every server and browser
    n = unicodedata.normalize('NFKD', local).encode('ascii', 'ignore').decode()
    stem, ext = n.rsplit('.', 1)
    ext = 'jpg' if local in BIG_PNG_AS_JPEG else ext.lower()
    return re.sub(r'[^A-Za-z0-9._-]+', '-', stem) + '.' + ext

def _scan_big_pngs():
    from PIL import Image
    for f in (INV / 'images').iterdir():
        if f.suffix.lower() == '.png' and f.stat().st_size > 600_000:
            im = Image.open(f)
            if im.mode in ('RGB', 'P') and 'transparency' not in im.info:
                BIG_PNG_AS_JPEG.add(f.name)
_scan_big_pngs()

def copy_assets():
    (OUT / 'images').mkdir(parents=True, exist_ok=True)
    from PIL import Image
    for local in list(IMAGES_USED) + ['1474309377546_puheklinikka_logo_rgb_white_transparen.png', '1474309468304_puheklinikka_logo_pieni.jpg']:
        src = INV / 'images' / local
        dst = OUT / 'images' / web_name(local)
        im = Image.open(src)
        if im.width > 1500 or src.stat().st_size > 600_000:
            # Same picture, smaller file (Squarespace also served max 1500 px wide)
            im.thumbnail((1500, 1500))
            if src.suffix.lower() in ('.jpg', '.jpeg') or local in BIG_PNG_AS_JPEG:
                im.convert('RGB').save(dst, 'JPEG', quality=85, optimize=True, progressive=True)
            else:
                im.save(dst, optimize=True)
        else:
            shutil.copy2(src, dst)
    # images Nana supplied for the new site
    for f in (ASSETS / 'images').glob('*'):
        shutil.copy2(f, OUT / 'images' / f.name)
    # favicon: the captured .ico is JPEG data; save a real PNG favicon
    Image.open(INV / 'images' / '1474309397440_favicon.ico').convert('RGB').resize((64, 64)).save(OUT / 'favicon.png')
    # PDFs keep their old /s/ addresses
    (OUT / 's').mkdir(exist_ok=True)
    for pdf in (INV / 'documents').glob('*.pdf'):
        if pdf.name in style_a.CV_PDFS:
            continue  # CVs replaced by profile pages (Nana, 2026-10-03)
        shutil.copy2(pdf, OUT / 's' / pdf.name)
    (OUT / 'assets' / 'fonts').mkdir(parents=True, exist_ok=True)
    for f in (ASSETS / 'fonts').iterdir():
        shutil.copy2(f, OUT / 'assets' / 'fonts' / f.name)
    shutil.copy2(ASSETS / 'site.css', OUT / 'assets' / 'site.css')
    shutil.copy2(ASSETS / 'site.js', OUT / 'assets' / 'site.js')

# ---------------------------------------------------------------- chrome
ICONS = json.loads((ASSETS / 'icons.json').read_text())

def nav_html(depth, current):
    items = []
    for i, (label, slug, children) in enumerate(MENU):
        if children is None:
            cur = ' aria-current="page"' if slug == current else ''
            items.append(f'<li><a href="{page_href(depth, slug)}"{cur}>{label}</a></li>')
        else:
            lang = FOLDER_LANG.get(label)
            la = f' lang="{lang}"' if lang else ''
            active = any(s == current for _, s in children)
            sub = ''.join(
                f'<li><a href="{page_href(depth, s)}"{CUR if s == current else ""}>{l}</a></li>'
                for l, s in children)
            items.append(
                f'<li class="folder{" active" if active else ""}"{la}>'
                f'<button type="button" aria-expanded="false" aria-controls="sub{i}">{label}</button>'
                f'<ul id="sub{i}" class="sub">{sub}</ul></li>')
    return '\n'.join(items)

def subnav_html(depth, current):
    for label, slug, children in MENU:
        if children and any(s == current for _, s in children):
            lang = FOLDER_LANG.get(label)
            la = f' lang="{lang}"' if lang else ''
            links = ''.join(
                f'<li><a href="{page_href(depth, s)}"{CUR if s == current else ""}>{l}</a></li>'
                for l, s in children)
            return f'<nav class="subnav" aria-label="{label}"{la}><ul>{links}</ul></nav>'
    return ''

def social_html():
    li = 'M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45z'
    mail = 'M2 5h20v14H2V5zm2 2v.3l8 5.2 8-5.2V7H4zm16 2.7-8 5.2-8-5.2V17h16V9.7z'
    links = [
        ('Facebook', 'http://www.facebook.com/puheklinikka', ICONS['facebook']),
        ('LinkedIn', 'https://www.linkedin.com/company/puheklinikka/', li),
        ('Instagram', 'https://www.instagram.com/puheklinikka/', ICONS['instagram']),
        (OFFICE_EMAIL, f'mailto:{OFFICE_EMAIL}', mail),
    ]
    out = []
    for name, href, d in links:
        out.append(f'<li><a href="{href}" aria-label="{name}"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="{d}"/></svg></a></li>')
    return f'<ul class="social" aria-label="{UI["social_label"]}">' + ''.join(out) + '</ul>'

def page_shell(slug, lang, title, page_title, body, depth):
    css = rel(depth, 'assets/site.css'); js = rel(depth, 'assets/site.js')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="{rel(depth, 'favicon.png')}">
<link rel="stylesheet" href="{css}">
<meta property="og:image" content="https://www.puheklinikka.net/images/1474309468304_puheklinikka_logo_pieni.jpg">
</head>
<body>
<a class="skip" href="#content" lang="fi">{UI['skip']}</a>
<header class="site-header" lang="fi">
  <div class="brand"><a href="{page_href(depth, '')}"><img src="{rel(depth, 'images/' + web_name('1474309377546_puheklinikka_logo_rgb_white_transparen.png'))}" alt="Puheklinikka" width="300" height="75"></a></div>
  <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="mainnav">{UI['menu']}</button>
  <nav id="mainnav" class="mainnav" aria-label="{UI['nav_label']}"><ul>
{nav_html(depth, slug)}
  </ul></nav>
</header>
<main id="content" tabindex="-1">
{subnav_html(depth, slug)}
<h1 class="page-title">{html.escape(page_title)}</h1>
<div class="content">
{body}
</div>
</main>
<footer class="site-footer" lang="fi">
  <div class="contact">
    <h2 lang="en">Contact Us</h2>
    <p>Ota yhteyttä!</p>
    <p><a href="mailto:{OFFICE_EMAIL}">{OFFICE_EMAIL}</a></p>
  </div>
  {social_html()}
</footer>
<script src="{js}"></script>
</body>
</html>
'''

PEOPLE = []
style_a.SERVICE_TILES[:] = next(c for l, sl, c in MENU if l == 'Palvelut')

def log(slug, kind, msg):
    LOG.append((slug, kind, msg))

def render(slug, lang, title, page_title, crumb, body, depth, home, sidebar=True):
    side = style_a.sidebar_html(MENU, FOLDER_LANG, page_href, depth, slug) if sidebar else ''
    if slug == 'asiantuntijat' or slug.startswith('asiantuntijat/'):
        side = ''
    return style_a.shell(lang=lang, title=title, page_title=page_title, crumb=crumb, body=body, depth=depth,
                         rel=rel, page_href=page_href, nav=style_a.nav_html(MENU, FOLDER_LANG, page_href, depth, slug),
                         sidebar=side, social=social_html(), ui=UI, office_email=OFFICE_EMAIL,
                         logo=web_name('1474309468304_puheklinikka_logo_pieni.jpg'), home=home)

def redirect_page(target_depth_from, target_slug):
    href = page_href(target_depth_from, target_slug)
    return f'''<!doctype html>
<html lang="fi"><head><meta charset="utf-8"><title>Puheklinikka</title>
<meta http-equiv="refresh" content="0; url={href}"><link rel="canonical" href="https://www.puheklinikka.net/{target_slug}">
</head><body><p><a href="{href}">Puheklinikka</a></p></body></html>
'''

# Headings form a clean outline on every page: H1 page title, then H2, H3 with no skipped levels
# (WCAG 1.3.1 / 2.4.6; Nana, 2026-10-04). Section headings become H2 on every page. The CSS keeps their look.
HEADING_MATCH = {  # headings one level lower than their neighbours on the old site, raised to match
    'toimintatavat-ja-arvot': ['Ajanmukaisuus'],
    'new-page': ['Nenälovimuki Flexi cup'],
}

def outline_headings(slug, page):
    a = page.index('<main'); b = page.index('</main>')
    main = page[a:b]
    for text in HEADING_MATCH.get(slug, []):
        m = re.search(r'<h4([^>]*)>(\s*' + re.escape(text) + r'[^<]*)</h4>', main)
        assert m, (slug, text)
        main = main[:m.start()] + f'<h3{m.group(1)}>{m.group(2)}</h3>' + main[m.end():]
    stack = []  # (original level, new level)
    out, pos = [], 0
    for m in re.finditer(r'<h([1-6])([^>]*)>(.*?)</h\1>', main, re.S):
        o = int(m.group(1))
        while stack and stack[-1][0] >= o:
            stack.pop()
        n = 1 if o == 1 else (stack[-1][1] + 1 if stack else 2)
        stack.append((o, n))
        out.append(main[pos:m.start()] + f'<h{n}{m.group(2)}>{m.group(3)}</h{n}>')
        pos = m.end()
    out.append(main[pos:])
    return page[:a] + ''.join(out) + page[b:]

# ---------------------------------------------------------------- main
def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for slug, (raw, _, lang) in PAGES.items():
        depth = 1 if slug else 0
        soup = BeautifulSoup((RAW / raw).read_text(), 'html.parser')
        tab_title = soup.title.get_text(strip=True)
        page_title = soup.select_one('.page-title').get_text(strip=True)
        layout = soup.select_one('.main-content-wrapper .sqs-layout')
        body = simplify(convert_layout(layout, depth, slug))
        body = style_a.demote_headings(body)
        body = style_a.page_fixups(slug, body, log)
        body = style_a.side_labels_first(body)
        home = slug == ''
        if home:
            body = style_a.home_body(body, rel, page_href, log)
        elif slug == 'asiantuntijat':
            body, PEOPLE[:] = style_a.terapeutit_body(body, log)
        elif slug == 'new-page-1':
            body = style_a.news_body(body, page_title, log)
        elif not home and slug != 'toimintatavat-ja-arvot':  # that page already has dividing lines between its sections
            body = style_a.mark_section_breaks(body)
        if slug == 'ryhmmuotoinen-terapia':
            body = style_a.ryhma_layout(body)
        crumb = None  # section label above the title removed (Nana, 2026-10-03)
        page = render(slug, lang, tab_title, page_title, crumb, body, depth, home)
        if unicodedata.normalize('NFC', page) != page:
            LOG.append((slug, 'tech', 'some letters were stored in decomposed Unicode form (e.g. a + ¨); normalised to standard form, looks identical'))
            page = unicodedata.normalize('NFC', page)
        # agreed text edits
        for s, old, new, n in EDITS:
            if s != slug:
                continue
            c = page.count(old)
            if c == 0 or (n is not None and c != n):
                sys.exit(f'EDIT FAILED on {slug or "/"}: "{old}" found {c}x, expected {n}')
            page = page.replace(old, new)
            LOG.append((slug, 'text', f'"{old}" → "{new}" ({c}×)'))
        page = outline_headings(slug, page)
        dest = OUT / slug / 'index.html' if slug else OUT / 'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page)
    for p in PEOPLE:
        ps = f'asiantuntijat/{p["slug"]}'
        page = render(ps, 'fi', f'{p["name"]} — Puheklinikka', p['name'], None,
                      style_a.profile_body(p, log), 2, False, sidebar=False)
        page = unicodedata.normalize('NFC', page)
        (OUT / ps).mkdir(parents=True, exist_ok=True)
        (OUT / ps / 'index.html').write_text(page)
    # new pages with only a title until Nana supplies their text (must not go live empty at launch)
    for ns, title in NEW_PAGES.items():
        page = render(ns, 'fi', f'{title} — Puheklinikka', title, None, '', 1, False)
        (OUT / ns).mkdir(parents=True, exist_ok=True)
        (OUT / ns / 'index.html').write_text(unicodedata.normalize('NFC', page))
    # accessibility statement page: title only until Nana completes the statement (Nana, 2026-10-04)
    page = render('saavutettavuusseloste', 'fi', 'Saavutettavuusseloste — Puheklinikka', 'Saavutettavuusseloste', None,
                  '', 1, False, sidebar=False)
    (OUT / 'saavutettavuusseloste').mkdir(parents=True, exist_ok=True)
    (OUT / 'saavutettavuusseloste' / 'index.html').write_text(unicodedata.normalize('NFC', page))
    for old, target in REDIRECTS.items():
        (OUT / old).mkdir(parents=True, exist_ok=True)
        (OUT / old / 'index.html').write_text(redirect_page(1, target))
        LOG.append((old, 'redirect', f'/{old} (duplicate of homepage) now forwards to the homepage'))
    # check yhteystiedot counts
    for s, n in YHTEYS_EXPECTED.items():
        c = sum(1 for x in LOG if x[0] == s and x[1] == 'link')
        if c == 0 or (n is not None and c != n):
            sys.exit(f'YHTEYSTIEDOT CHECK FAILED on {s}: {c}')
    copy_assets()
    make_card_photos()
    (OUT / '.nojekyll').write_text('')
    # CNAME (www.puheklinikka.net) is added only at the domain switch-over step, with Nana's approval
    log('', 'layout', 'Style A for the whole site (Nana, 2026-10-03): white header with the orange logo, menu on one line, light title band with the section name, section menu as a sidebar, dark footer')
    log('', 'drop', 'menu item "Etusivu" removed; the logo links to the homepage')
    log('', 'drop', 'footer heading "Contact Us" removed')
    log('', 'drop', f'CV PDFs no longer published: {", ".join(sorted(style_a.CV_PDFS))}')
    write_changes()
    for w in WARN:
        print('WARN', w)
    print('built', len(PAGES), 'pages,', len(IMAGES_USED), 'images')

def make_card_photos():
    """Copies of the therapist photos for the Terapeutit cards. The photos have rounded corners baked
    in (transparent or white); the two top corners are filled with the card's border orange so the photo
    meets the border without white gaps (Nana, 2026-10-04). The bottom corners become white."""
    from PIL import Image
    orange, white = (0xc4, 0x60, 0x13), (255, 255, 255)
    for p in PEOPLE:
        src = re.search(r'src="\.\./images/([^"]+)"', p['img']).group(1)
        im = Image.open(OUT / 'images' / src)
        w, h = im.size
        r = int(w * 0.09) + 2  # baked-in corner radius is about 7% of the width
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA')
            top = Image.new('RGB', (w, h), white)
            top.paste(Image.new('RGB', (w, r), orange), (0, 0))
            top.paste(im, (0, 0), im)
            im = top
        else:
            # white corners: measure where the photo starts on the top row, then paint everything
            # outside that quarter circle (1px inside, to cover the soft edge) orange
            im = im.convert('RGB')
            px = im.load()
            white_ish = lambda c: min(c) > 235
            R = next(x for x in range(w) if not white_ish(px[x, 0])) + 1
            for y in range(R):
                for x in range(R):
                    if (R - x) ** 2 + (R - y) ** 2 > (R - 1) ** 2:
                        px[x, y] = orange
                        px[w - 1 - x, y] = orange
        im.save(OUT / 'images' / f'card-{p["slug"]}.jpg', quality=85, optimize=True)

def write_changes():
    lines = ['# Changes compared with the live Squarespace site', '',
             'Generated by tools/build.py. Every difference in the site text, links and features is listed here.', '']
    by = {}
    for s, k, msg in LOG:
        by.setdefault(s, []).append((k, msg))
    for s in sorted(by):
        lines.append(f'## /{s}')
        seen = set()
        for k, msg in by[s]:
            if (k, msg) in seen: continue
            seen.add((k, msg)); lines.append(f'- [{k}] {msg}')
        lines.append('')
    (ROOT.parent / 'CHANGES-generated.md').write_text('\n'.join(lines))

if __name__ == '__main__':
    build()
