"""Style A layout (chosen by Nana 2026-10-03, see /mnt/project-files/design-ideas/README.md).

Page text still comes unchanged from build.py; this module only rearranges it:
- page chrome (header, title band, section sidebar, footer)
- homepage (hero, service tiles, office cards)
- Terapeutit as cards + one profile page per therapist (option 2)
- Ajankohtaista posts as cards
Every rearrangement is logged to CHANGES via the log() callback.
"""
import re, html
from bs4 import BeautifulSoup

CUR = ' aria-current="page"'

# Therapist bios: Nana's text (sent 2026-10-03), word for word, as HTML blocks.
# Only whitespace is normalised (line breaks inside a paragraph, double spaces).
# One approved edit: Elina "tietoturvavastaavana" -> "tietosuojavastaavana" (Nana confirmed).
# Empty "Asiakasryhmät:" lines are kept in EMPTY_FIELDS and not shown until Nana fills them in.
BIOS = {
    'Elina Uusi-Hakala': [
        '<p>Elina työskentelee aikuisten ja koululaisten kanssa. Aikuisneurologisen puheterapian lisäksi hän tarjoaa ohjausta ja terapiaa sitkeiden äännevirheiden kanssa kamppaileville, pureutuu puheen sujuvuuden haasteisiin, sekä työskentelee valikoivan puhumattomuuden kanssa.</p>',
        '<p>Elina on valmistunut puheterapeutiksi Turun yliopistosta tutkien lopputyössään vakiintuneen dysartrian intensiivisen kuntoutuksen vaikuttavuutta. Täydennyskoulutuksessaan hän on perehtynyt laaja-alaisesti kielellisiin ja motorisiin kommunikointivaikeuksiin sekä lukivaikeuksien ja nielemishäiriöiden diagnosointiin ja hoitoon. Hän on kouluttautunut muun muassa OPT for TBI-, OPT-, OPT 2- ja DPNS-menetelmien käyttöön.</p>',
        '<p>Asiakastyön ohella Elina toimii Puheklinikan tietosuojavastaavana ja hoitaa Puheklinikan yleisiä asioita. Ota rohkeasti yhteyttä!</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
    ],
    'Annemari Hongell': [
        '<p>Annemari työskentelee aikuisneurologisten asiakkaiden kanssa toteuttaen yksilö-ja ryhmämuotoista terapiaa. Aikuisneurologisen puheterapian lisäksi hän tarjoaa ohjausta, terapiaa ja koulutusta äänihäiriöihin ja äänen oireiluun liittyvissä asioissa sekä ratkoo nielemiseen ja syömiseen liittyviä pulmia. Puheterapiatyön ohella Annemari tarjoaa tukipalveluita kuntoutujien läheisille kognitiivisen lyhytterapian muodossa.</p>',
        '<p>Annemari on valmistunut puheterapeutiksi Åbo Akademista. Lopputyössään hän kokosi ruotsinkielistä normiaineistoa Nopean sarjallisen nimeämisen testiin. Täydennyskoulutuksessaan Annemari on perehtynyt kielellisten ja motoristen kommunikointivaikeuksien sekä nielemistoimintojen kuntoutukseen. Hän on kouluttautunut muun muassa SCA™-, BCA-, OPT-, LSVT LOUD®-, SPEAK OUT!-, LOUD Crowd®- ja DPNS-menetelmien käyttöön sekä suun ja kasvojen alueen kinesioteippaukseen. Annemari on koulutukseltaan myös kognitiivinen lyhytterapeutti ja hyödyntää tätä osaamista sekä kuntoutujien että läheisten kanssa.</p>',
        '<p class="langs">Työskentelykielet: suomi, ruotsi, englanti.</p>',
    ],
    'Riitta Saari': [
        '<p>Riitta työskentelee aikuisneurologisten asiakkaiden kanssa ja toteuttaa sekä yksilö- että ryhmämuotoista puheterapiaa. Riitalta löytyy osaamista myös äänihäiriöden osalta. Hän tarjoaa ohjausta ja kuntoutusta toiminnallisten äänihäiriöiden kanssa kamppaileville henkilöille, ja toteuttaa ääniterapiaa, jossa tuetaan transsukupuolisia henkilöitä löytämään ääni ja puhetapa, jotka tuntuvat omilta ja vastaavat koettua sukupuoli-identiteettiä.</p>',
        '<p>Riitta on valmistunut puheterapeutiksi Turun yliopistosta. Lopputyössään hän tutki terveiden aikuisten suoriutumista kuullun erottelua mittaavista tehtävistä. Täydennyskoulutuksissaan Riitta on perehtynyt kommunikoinnin kuntoutukseen ja tukemiseen sekä laaja-alaisesti ääniterapiaan. Hän on kouluttautunut muun muassa SPEAK OUT!- ja LOUD Crowd® -menetelmien käyttöön ja toimii työterveyshuollon asiantuntijapuheterapeuttina.</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
    ],
    'Jenita Mattsson': [
        '<p>Jenitalta löytyy osaamista aikuisneurologisesta puheterapiasta sekä vuodeosasto-että avoterapiapuolelta. Jenita toteuttaa pääsääntöisesti yksilö-ja ryhmäterapiaa kokonaisvaltaisella työskentelyotteella läheisten ohjausta unohtamatta.</p>',
        '<p>Jenita on valmistunut puheterapeutiksi Turun yliopistosta. Lopputyössään hän tutki terveiden aikuisten suoriutumista kahdessa kehitteillä olevassa toistamistehtävässä. Täydennyskoulutuksessaan Jenita on perehtynyt kommunikointi-ja nielemisvaikeuksien kuntouttamiseen mm. SPEAKOUT! ja Loud Crowd® menetelmäkoulutuksella. Asiakastyön ohella Jenita toimii yliopisto-opettajana Turun yliopiston logopedian ja psykologian laitoksella ja kouluttaa tulevia puheterapeutteja.</p>',
        '<p class="langs">Työskentelykieli: suomi.</p>',
    ],
    'Marjaana Raukola-Lindblom': [
        '<p>Marjaanalla on laaja-alaisesti kokemusta aikuisten neurologisten ja neuropsykiatristen puheen, kielen ja vuorovaikutuksen häiriöiden kuntoutuksesta ja hän on perehtynyt erityisesti tapaturmaisten aivovammojen kuntoutukseen.</p>',
        '<p>Marjaana on valmistunut puheterapeutiksi Helsingin yliopistosta ja pätevöitynyt aikuisten neurologisperäisten kommunikaatiohäiriöiden erikoispuheterapeutiksi (FL) painottaen tapaturmassa syntyneiden aivovammojen jälkitiloja ja niiden kuntoutusta. Hän on tutkinut aivovammojen jälkitiloja myös väitöskirjassaan. Täydennyskoulutuksessaan Marjaana on perehtynyt on nielemishäiriöiden kuntoutusmenetelmiin (mm.DPNS), sosiaalisen vuorovaikutuksen kuntoutukseen ja ryhmämuotoiseen puheterapiaan. Marjaana on perehtynyt myös kognitiiviseen lyhytterapiaan ja eläinavusteiseen kuntoutukseen. Puheterapeutin työn ohella Marjaana työskentelee yliopisto-opettaajana sekä tutkimus- ja kehitystyössä Turun yliopistossa.</p>',
        '<p>Lisätietoja Marjaanasta löydät sivustolta <a href="https://www.skillful.fi">www.skillful.fi</a>.</p>',
        '<p class="langs">Työskentelykielet: suomi ja englanti.</p>',
    ],
    'Ida Luotonen': [
        '<p>Ida työskentelee Puheklinikalla itsenäisenä ammatinharjoittajana (Puheterapiapalvelut Ida Luotonen). Ida on perehtynyt erityisesti muistisairauksiin liittyviin kielellis-kognitiivisiin haasteisiin ja työskentelee asiakkaiden kanssa kokonaisvaltaisella työskentelyotteella.</p>',
        '<p>Ida on valmistunut puheterapeutiksi Turun yliopistosta. Hän tutki lopputyössään Alzheimerin tautia sairastavien henkilöiden kielellisiä taitoja. Täydennyskoulutuksissaan Ida on perehtynyt erityisesti muistisairauksien ja aivoverenkiertohäiriöiden aiheuttamiin kielellis-kommunikatiivisiin oireisiin, joita hän tutkii myös väitöskirjassaan. Lisäksi hän on perehtynyt kognitiivisen lyhytterapian menetelmiin.</p>',
        '<p class="langs">Työskentelykielet: suomi ja englanti.</p>',
    ],
    'Nana Lehtinen': [
        '<p>Nana on toiminut Puheklinikalla yrittäjänä sen perustamisesta alkaen ja edelleen hänen tehtäviinsä kuuluvat Puheklinikan toiminnan kehittäminen, terapiatyöskentelyn ohjaaminen ja hallinnollisten asioiden koordinointi.</p>',
        '<p>Lisäksi Nana kehittää Puheklinikalla suunniteltuja ja rakennettuja Sanapsis-perheen puheterapiasovelluksia. Sanapsis-perheeseen kuuluu kolme sovellusta:</p>',
        '<ul><li>SanapsisPro, kolmikielinen ammattisovellus, joka on suunnattu puheterapeuttien ammattikäyttöön (suomi, ruotsi ja englanti).</li>'
        '<li>SanapsisLite, joka tarjoaa pienen kurkistuksen SanapsisPro sovellukseen</li>'
        '<li>Sanapsis+, joka on suunniteltu kuntoutujien itsenäisen, sanatasoisen kotiharjoittelun tueksi. Harjoitusten lisäksi Sanapsis+ tarjoaa vinkkejä ja ideoita kotona toteutettavaan puheen ja kielellisten toimintojen aktivointiin.</li></ul>',
        '<p>Nana on valmistunut puheterapeutiksi Oulun yliopistosta ja lopputyössään hän tutki puhutun suomen kielen muuntumista vieraan kielen vaikutuksen alaisena. Täydennyskoulutuksessaan Nana on perehtynyt aikuisneurologiseen puheterapiaan ja kaksikielisyyteen laaja-alaisesti. Väitöskirjassaan Nana tutki terveiden kaksikielisten henkilöiden sanasujuvuustehtävissä suoriutumista suomeksi ja englanniksi.</p>',
        '<p class="langs">Työskentelykielet: suomi ja englanti.</p>',
    ],
}
# "Asiakasryhmät:" was empty for these six in Nana's text; not shown until filled in
EMPTY_FIELDS = {n: ['Asiakasryhmät:'] for n in BIOS if n != 'Nana Lehtinen'}
# CV PDFs replaced by profile pages (Nana, 2026-10-03): no longer published
CV_PDFS = {'Riitta-Saari.pdf', 'Elina-yynp.pdf', 'Nana-w2xz.pdf', 'Jenita.pdf',
           'Annemari-2023.pdf', 'Ida.pdf', 'Marjaana.pdf'}

def slugify(name):
    table = str.maketrans({'ä': 'a', 'ö': 'o', 'å': 'a', 'Ä': 'a', 'Ö': 'o', 'Å': 'a'})
    return re.sub(r'[^a-z0-9]+', '-', name.lower().translate(table)).strip('-')

# ---------------------------------------------------------------- chrome
def nav_html(menu, folder_lang, page_href, depth, current):
    items = []
    for i, (label, slug, children) in enumerate(menu):
        if slug == '' and children is None:
            continue  # "Etusivu": the logo links to the homepage (style A)
        if children is None:
            cur = CUR if slug == current or (slug and current.startswith(slug + '/')) else ''
            items.append(f'<li><a href="{page_href(depth, slug)}"{cur}>{label}</a></li>')
        else:
            lang = folder_lang.get(label)
            la = f' lang="{lang}"' if lang else ''
            active = any(s == current for _, s in children)
            sub = ''.join(f'<li><a href="{page_href(depth, s)}"{CUR if s == current else ""}>{l}</a></li>'
                          for l, s in children)
            items.append(f'<li class="folder{" active" if active else ""}"{la}>'
                         f'<button type="button" aria-expanded="false" aria-controls="sub{i}">{label}</button>'
                         f'<ul id="sub{i}" class="sub">{sub}</ul></li>')
    return '\n'.join(items)

def section_of(menu, current):
    for label, slug, children in menu:
        if children and any(s == current for _, s in children):
            return label, children
    return None, None

def sidebar_html(menu, folder_lang, page_href, depth, current):
    label, children = section_of(menu, current)
    if not children:
        return ''
    lang = folder_lang.get(label)
    la = f' lang="{lang}"' if lang else ''
    links = ''.join(f'<li><a href="{page_href(depth, s)}"{CUR if s == current else ""}>{l}</a></li>'
                    for l, s in children)
    return f'<nav class="side" aria-label="{label}"{la}><ul>{links}</ul></nav>'

def demote_headings(body):
    """One h1 per page (the title band); content headings move down one level."""
    for n in (5, 4, 3, 2, 1):
        body = re.sub(rf'<(/?)h{n}([ >])', rf'<\1h{n + 1}\2', body)
    return body

# ---------------------------------------------------------------- homepage
def home_body(body, rel, page_href, log):
    s = BeautifulSoup(body, 'html.parser')
    img = s.find('figure')
    ps = [p for p in s.find_all('p')]
    def find(start):
        for p in ps:
            if p.get_text(' ', strip=True).startswith(start):
                return p
        raise SystemExit(f'HOMEPAGE: paragraph "{start}" not found')
    intro = find('Puheklinikka on aikuisten')
    areas = find('Osaamisalueitamme')
    places = find('Toimitilamme')
    find('Tutustu asiantuntijoihimme')  # replaced by the Terapeutit button
    welcome = find('Tervetuloa kuntoutukseen')
    email = next(p for p in ps if p.find('a', href=re.compile('^mailto:toimisto')))
    addr_head = find('Käynti-ja postiosoite')
    # office sections: from each h2 up to the next <hr> or end
    offices = []
    for h in s.find_all('h3'):  # office names (h2 on the old site, demoted)
        parts, node = [], h.next_sibling
        while node is not None and not (getattr(node, 'name', None) == 'hr'):
            if getattr(node, 'name', None):
                parts.append(node)
            node = node.next_sibling
        mp = next((x for x in parts if x.find('iframe') or 'map' in (x.get('class') or [])), None)
        txt = ''.join(str(x) for x in parts if x is not mp and 'spacer' not in (x.get('class') or []))
        frame = mp.find('iframe') if mp else None
        offices.append((h.get_text(strip=True), str(frame) if frame else '', txt))
    a = email.find('a')
    tiles = ''.join(f'<li><a href="{page_href(0, sl)}">{lb}</a></li>' for lb, sl in SERVICE_TILES)
    out = f'''<div class="hero"><div class="wrap hero-grid"><div>
<h1>{intro.get_text(strip=True)}</h1>
{str(places)}
{str(welcome)}
<p class="btns"><a class="btn" href="{page_href(0, 'asiantuntijat')}">Terapeutit</a><a class="btn alt" href="{html.escape(a['href'], quote=True)}">{a.get_text(strip=True)}</a></p>
</div>
{str(img)}</div></div>
<section class="sec"><div class="wrap">
<h2>Palvelut</h2>
{str(areas)}
<ul class="tiles">{tiles}</ul>
</div></section>
<section class="sec sec-tight"><div class="wrap">
<h2>{addr_head.get_text(strip=True)}</h2>
<div class="places">''' + ''.join(
        f'<div class="place">{f"<div class=map>{fr}</div>" if fr else ""}<div class="txt"><h3>{name}</h3>{txt}</div></div>'
        for name, fr, txt in offices) + '</div></div></section>'
    if len(offices) != 2:
        raise SystemExit(f'HOMEPAGE: expected 2 offices, found {len(offices)}')
    log('', 'layout', 'Homepage rearranged in style A: first sentence is the main heading; intro, "Tervetuloa kuntoutukseen!" and the email are in the top band; "Osaamisalueitamme…" is under the heading "Palvelut" (menu label) with links to the eight service pages (menu names); both offices side by side with their maps')
    log('', 'text', '"Tutustu asiantuntijoihimme täällä." replaced by a "Terapeutit" button (menu label)')
    log('', 'text', '"Käynti-ja postiosoite:" is now a heading')
    return out

SERVICE_TILES = []  # filled by build.py from MENU

# ---------------------------------------------------------------- therapists
def parse_people(body):
    pairs = re.findall(r'<figure class="img">(?:<a [^>]*>)?(<img [^>]*>)(?:</a>)?</figure>\s*<p>(.*?)</p>', body, re.S)
    people = []
    for img, txt in pairs:
        m = re.match(r'\s*<a [^>]*>(.*?)</a>\s*<br/>(.*)', txt, re.S)
        name = m.group(1).strip()
        details = re.sub(r'\s{2,}', ' ', m.group(2)).strip()
        people.append({'name': name, 'img': img, 'details': details, 'slug': slugify(name)})
    return people

def terapeutit_body(body, log):
    intro = re.search(r'<h2>Asiantuntijat</h2>(<p>.*?</p>)', body, re.S)
    people = parse_people(body)
    if len(people) != 7:
        raise SystemExit(f'TERAPEUTIT: expected 7 people, found {len(people)}')
    cards = ''
    for p in people:
        img = re.sub(r' alt="[^"]*"', f' alt="{html.escape(p["name"], quote=True)}"', p['img'])
        cards += (f'<li class="person"><a class="photo" href="{p["slug"]}/">{img}</a>'
                  f'<div class="txt"><h3><a href="{p["slug"]}/">{p["name"]}</a></h3><p>{p["details"]}</p></div></li>')
    tail = body[body.rfind('<hr>'):]
    log('asiantuntijat', 'layout', 'Therapists shown as cards (style A). Each name and photo links to the therapist\'s own page instead of a CV PDF (Nana, option 2)')
    log('asiantuntijat', 'alt', 'therapist photos: alt text = the therapist\'s name (the photo is a link to the profile)')
    return f'<h2>Asiantuntijat</h2>{intro.group(1)}<ul class="people">{cards}</ul>{tail}', people

def profile_body(p, log):
    bio = BIOS.get(p['name'])
    img = re.sub(r' alt="[^"]*"', ' alt=""', p['img']).replace('src="../', 'src="../../')
    bio_html = ''.join(bio) if bio else ''
    if bio:
        extra = ' ("tietoturvavastaavana" → "tietosuojavastaavana", confirmed by Nana)' if 'Elina' in p['name'] else ''
        log(f'asiantuntijat/{p["slug"]}', 'text', f'new profile page with Nana\'s bio text for {p["name"]}, word for word{extra}')
    else:
        log(f'asiantuntijat/{p["slug"]}', 'layout', f'new profile page for {p["name"]}: photo and contact details only; bio text not yet provided')
    details = p['details'].replace('href="../', 'href="../../')
    return (f'<div class="profile"><div class="pcol">{img}<div class="card"><p>{details}</p></div></div>'
            f'<div class="content">{bio_html}<p><a class="back" href="../">← Terapeutit</a></p></div></div>')

# ---------------------------------------------------------------- news
def news_body(body, page_title, log):
    body = re.sub(rf'^\s*<h2>{re.escape(page_title)}</h2>\s*', '', body)
    posts = [x.strip() for x in re.split(r'<hr>', body) if x.strip()]
    log('new-page-1', 'layout', f'each dated post shown as its own card ({len(posts)} cards); repeated heading "Ajankohtaista" inside the page removed (same as page title)')
    return '<div class="news">' + ''.join(f'<article>{x}</article>' for x in posts) + '</div>'

# ---------------------------------------------------------------- page
def shell(*, lang, title, page_title, crumb, body, depth, rel, page_href, nav, sidebar, social, ui,
          office_email, logo, home=False):
    css = rel(depth, 'assets/site.css'); js = rel(depth, 'assets/site.js')
    if home:
        main = body
    else:
        band = (f'<div class="band"><div class="wrap">'
                f'{f"<p class=crumb>{crumb}</p>" if crumb else ""}<h1>{html.escape(page_title)}</h1></div></div>')
        layout = 'layout' if sidebar else 'layout single'
        main = f'{band}<div class="wrap {layout}">{sidebar}<div class="content">{body}</div></div>'
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
<a class="skip" href="#content" lang="fi">{ui['skip']}</a>
<header class="site" lang="fi"><div class="wrap head">
  <a class="logo" href="{page_href(depth, '')}"><img src="{rel(depth, 'images/' + logo)}" alt="Puheklinikka" width="945" height="246"></a>
  <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="mainnav">{ui['menu']}</button>
  <nav id="mainnav" class="main" aria-label="{ui['nav_label']}"><ul>
{nav}
  </ul></nav>
</div></header>
<main id="content" tabindex="-1">
{main}
</main>
<footer class="site" lang="fi"><div class="wrap foot">
  <div><p><strong>Ota yhteyttä!</strong><br><a href="mailto:{office_email}">{office_email}</a></p></div>
  {social}
</div></footer>
<script src="{js}"></script>
</body>
</html>
'''
