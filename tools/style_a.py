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
        '<p>Annemari työskentelee aikuisneurologisten asiakkaiden kanssa toteuttaen yksilö- ja ryhmämuotoista terapiaa. Aikuisneurologisen puheterapian lisäksi hän tarjoaa ohjausta, terapiaa ja koulutusta äänihäiriöihin ja äänen oireiluun liittyvissä asioissa sekä ratkoo nielemiseen ja syömiseen liittyviä pulmia. Puheterapiatyön ohella Annemari tarjoaa tukipalveluita kuntoutujien läheisille kognitiivisen lyhytterapian muodossa.</p>',
        '<p>Annemari on valmistunut puheterapeutiksi Åbo Akademista. Lopputyössään hän kokosi ruotsinkielistä normiaineistoa Nopean sarjallisen nimeämisen testiin. Täydennyskoulutuksessaan Annemari on perehtynyt kielellisten ja motoristen kommunikointivaikeuksien sekä nielemistoimintojen kuntoutukseen. Hän on kouluttautunut muun muassa SCA™-, BCA-, OPT-, LSVT LOUD®-, SPEAK OUT!®-, LOUD Crowd®- ja DPNS-menetelmien käyttöön sekä suun ja kasvojen alueen kinesioteippaukseen. Annemari on koulutukseltaan myös kognitiivinen lyhytterapeutti ja hyödyntää tätä osaamista sekä kuntoutujien että läheisten kanssa.</p>',
        '<p class="langs">Työskentelykielet: suomi, ruotsi, englanti.</p>',
    ],
    'Riitta Saari': [
        '<p>Riitta työskentelee aikuisneurologisten asiakkaiden kanssa ja toteuttaa sekä yksilö- että ryhmämuotoista puheterapiaa. Riitalta löytyy osaamista myös äänihäiriöiden osalta. Hän tarjoaa ohjausta ja kuntoutusta toiminnallisten äänihäiriöiden kanssa kamppaileville henkilöille, ja toteuttaa ääniterapiaa, jossa tuetaan transsukupuolisia henkilöitä löytämään ääni ja puhetapa, jotka tuntuvat omilta ja vastaavat koettua sukupuoli-identiteettiä.</p>',
        '<p>Riitta on valmistunut puheterapeutiksi Turun yliopistosta. Lopputyössään hän tutki terveiden aikuisten suoriutumista kuullun erottelua mittaavista tehtävistä. Täydennyskoulutuksissaan Riitta on perehtynyt kommunikoinnin kuntoutukseen ja tukemiseen sekä laaja-alaisesti ääniterapiaan. Hän on kouluttautunut muun muassa SPEAK OUT!®- ja LOUD Crowd® -menetelmien käyttöön ja toimii työterveyshuollon asiantuntijapuheterapeuttina.</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
    ],
    'Jenita Mattsson': [
        '<p>Jenitalta löytyy osaamista aikuisneurologisesta puheterapiasta sekä vuodeosasto- että avoterapiapuolelta. Jenita toteuttaa pääsääntöisesti yksilö- ja ryhmäterapiaa kokonaisvaltaisella työskentelyotteella läheisten ohjausta unohtamatta.</p>',
        '<p>Jenita on valmistunut puheterapeutiksi Turun yliopistosta. Lopputyössään hän tutki terveiden aikuisten suoriutumista kahdessa kehitteillä olevassa toistamistehtävässä. Täydennyskoulutuksessaan Jenita on perehtynyt kommunikointi- ja nielemisvaikeuksien kuntouttamiseen mm. SPEAK OUT!® ja LOUD Crowd® -menetelmäkoulutuksella. Asiakastyön ohella Jenita toimii yliopisto-opettajana Turun yliopiston logopedian ja psykologian laitoksella ja kouluttaa tulevia puheterapeutteja.</p>',
        '<p class="langs">Työskentelykieli: suomi.</p>',
    ],
    'Marjaana Raukola-Lindblom': [
        '<p>Marjaanalla on laaja-alaisesti kokemusta aikuisten neurologisten ja neuropsykiatristen puheen, kielen ja vuorovaikutuksen häiriöiden kuntoutuksesta ja hän on perehtynyt erityisesti tapaturmaisten aivovammojen kuntoutukseen.</p>',
        '<p>Marjaana on valmistunut puheterapeutiksi Helsingin yliopistosta ja pätevöitynyt aikuisten neurologisperäisten kommunikaatiohäiriöiden erikoispuheterapeutiksi (FL) painottaen tapaturmassa syntyneiden aivovammojen jälkitiloja ja niiden kuntoutusta. Hän on tutkinut aivovammojen jälkitiloja myös väitöskirjassaan. Täydennyskoulutuksessaan Marjaana on perehtynyt nielemishäiriöiden kuntoutusmenetelmiin (mm. DPNS), sosiaalisen vuorovaikutuksen kuntoutukseen ja ryhmämuotoiseen puheterapiaan. Marjaana on perehtynyt myös kognitiiviseen lyhytterapiaan ja eläinavusteiseen kuntoutukseen. Puheterapeutin työn ohella Marjaana työskentelee yliopisto-opettajana sekä tutkimus- ja kehitystyössä Turun yliopistossa.</p>',
        '<p>Lisätietoja Marjaanasta löydät sivustolta <a href="https://www.skillful.fi">www.skillful.fi</a>.</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
    ],
    'Ida Luotonen': [
        '<p>Ida työskentelee Puheklinikalla itsenäisenä ammatinharjoittajana (Puheterapiapalvelut Ida Luotonen). Ida on perehtynyt erityisesti muistisairauksiin liittyviin kielellis-kognitiivisiin haasteisiin ja työskentelee asiakkaiden kanssa kokonaisvaltaisella työskentelyotteella.</p>',
        '<p>Ida on valmistunut puheterapeutiksi Turun yliopistosta. Hän tutki lopputyössään Alzheimerin tautia sairastavien henkilöiden kielellisiä taitoja. Täydennyskoulutuksissaan Ida on perehtynyt erityisesti muistisairauksien ja aivoverenkiertohäiriöiden aiheuttamiin kielellis-kommunikatiivisiin oireisiin, joita hän tutkii myös väitöskirjassaan. Lisäksi hän on perehtynyt kognitiivisen lyhytterapian menetelmiin.</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
    ],
    'Nana Lehtinen': [
        '<p>Nana on toiminut Puheklinikalla yrittäjänä sen perustamisesta alkaen ja edelleen hänen tehtäviinsä kuuluvat Puheklinikan toiminnan kehittäminen, terapiatyöskentelyn ohjaaminen ja hallinnollisten asioiden koordinointi.</p>',
        '<p>Lisäksi Nana kehittää Puheklinikalla suunniteltuja ja rakennettuja Sanapsis-perheen puheterapiasovelluksia. Sanapsis-perheeseen kuuluu kolme sovellusta:</p>',
        '<ul><li>SanapsisPro, kolmikielinen ammattisovellus, joka on suunnattu puheterapeuttien ammattikäyttöön (suomi, ruotsi ja englanti).</li>'
        '<li>SanapsisLite, joka tarjoaa pienen kurkistuksen SanapsisPro-sovellukseen</li>'
        '<li>Sanapsis+, joka on suunniteltu kuntoutujien itsenäisen, sanatasoisen kotiharjoittelun tueksi. Harjoitusten lisäksi Sanapsis+ tarjoaa vinkkejä ja ideoita kotona toteutettavaan puheen ja kielellisten toimintojen aktivointiin.</li></ul>',
        '<p>Nana on valmistunut puheterapeutiksi Oulun yliopistosta ja lopputyössään hän tutki puhutun suomen kielen muuntumista vieraan kielen vaikutuksen alaisena. Täydennyskoulutuksessaan Nana on perehtynyt aikuisneurologiseen puheterapiaan ja kaksikielisyyteen laaja-alaisesti. Väitöskirjassaan Nana tutki terveiden kaksikielisten henkilöiden sanasujuvuustehtävissä suoriutumista suomeksi ja englanniksi.</p>',
        '<p class="langs">Työskentelykielet: suomi, englanti.</p>',
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
LIGHT_ATTR = ' class="light"'
LIGHT_TILES = 5  # = first row of five; upper row of homepage service tiles shown white (comparison, Nana 2026-10-04)


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
    # Comparison for others to see (Nana, 2026-10-04): the upper row is white with the therapist cards' hover,
    # the lower row stays orange. To switch back, set LIGHT_TILES = 0 (or 8 for all white).
    tiles = ''.join(f'<li><a{LIGHT_ATTR if i < LIGHT_TILES else ""} href="{page_href(0, sl)}">{lb}</a></li>'
                    for i, (lb, sl) in enumerate(SERVICE_TILES))
    out = f'''<div class="hero"><div class="wrap hero-grid"><div>
<h1>{intro.get_text(strip=True)}</h1>
{str(places)}
{str(welcome)}
<p class="btns"><a class="btn" href="{page_href(0, 'asiantuntijat')}">Terapeutit</a><a class="btn alt" href="{html.escape(a['href'], quote=True)}">{a.get_text(strip=True)}</a></p>
</div>
{str(img)}</div></div>
<section class="sec"><div class="wrap">
<h2>Palvelut</h2>
<p class="areas">{HOME_AREAS}</p>
<ul class="tiles">{tiles}</ul>
</div></section>
<section class="sec sec-tight"><div class="wrap">
<h2>Miten puheterapiaan hakeudutaan?</h2>
{''.join(f'<p class="areas">{x}</p>' for x in HOME_ACCESS)}
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

# Homepage section below the service tiles, Nana's text word for word (2026-10-04); split into two paragraphs where Nana broke the line
HOME_ACCESS = ('Puheterapia käynnistyy tyypillisesti lääkärin tai neurologin lähetteellä ja toteutuu Kelan, hyvinvointialueen tai '
               'vakuutusyhtiön maksusitoumuksella tai palvelusetelillä. Mikäli koet, että tarvitset puheterapiaa, ota asia puheeksi lääkärisi kanssa.',
               'Ota myös rohkeasti yhteyttä meihin. Neuvomme mielellämme puheterapiaan hakeutumisen eri vaiheissa. '
               'Tarjoamme palveluita myös itsemaksaville asiakkaille.')
# Homepage "Palvelut" text, Nana's new wording word for word (2026-10-04); replaces the old "Osaamisalueitamme…" paragraph
HOME_AREAS = ('Osaamisalueitamme ovat aikuisneurologiset puheen, kommunikoinnin ja nielemisen haasteet, jotka liittyvät esimerkiksi '
              'aivoverenkiertohäiriöihin, aivovammoihin ja eteneviin neurologisiin sairauksiin, kuten Parkinsonin tautiin. '
              'Olemme perehtyneet toiminnallisten äänihäiriöiden kuntoutukseen sekä trans- ja muunsukupuolisten ääniterapiaan. '
              'Tarjoamme puheterapiaa puheen sujuvuuden haasteisiin ja valikoivaan puhumattomuuteen aikuisille, nuorille ja kouluikäisille. '
              'Lisäksi toteutamme LUKI-tutkimuksia ja tarjoamme kuntoutujien läheisille tukea tilanteissa, joissa sairastuminen tai kuntoutuminen kuormittaa arkea.')

# ---------------------------------------------------------------- therapists
def parse_people(body):
    pairs = re.findall(r'<figure class="img">(?:<a [^>]*>)?(<img [^>]*>)(?:</a>)?</figure>\s*<p>(.*?)</p>', body, re.S)
    people = []
    for img, txt in pairs:
        m = re.match(r'\s*<a [^>]*>(.*?)</a>\s*<br/>(.*)', txt, re.S)
        name = m.group(1).strip()
        details = re.sub(r'\s{2,}', ' ', m.group(2)).strip()
        for old, new in DETAIL_EDITS.get(name, []):
            assert details.count(old) == 1, (name, old)
            details = details.replace(old, new)
        people.append({'name': name, 'img': img, 'details': details, 'slug': slugify(name)})
    return people

# Contact details on the cards and profile pages (Nana, 2026-10-04)
DETAIL_EDITS = {
    'Elina Uusi-Hakala': [('(Helsinki ja Turku) yleiset asiat', '(Helsinki ja Turku)<br/>yleiset asiat')],
    'Nana Lehtinen': [('Hallinnolliset asiat 040 593 0015', 'Hallinnolliset asiat<br/>040 593 0015')],
    'Annemari Hongell': [('kognitiivinen lyhyterapia ', 'kognitiivinen lyhytterapeutti')],
    'Ida Luotonen': [('puheterapeutti (Turku) ', 'puheterapeutti (Turku) kognitiivinen lyhytterapeutti')],
    'Marjaana Raukola-Lindblom': [('työnohjaaja <a ', 'työnohjaaja<br/>Lisätietoja: <a '),
                                  ('>Skillfull Interaction</a>', '>Skillful interaction</a>')],
}
# Card order on the Terapeutit page (Nana, 2026-10-04)
PEOPLE_ORDER = ['Elina Uusi-Hakala', 'Riitta Saari', 'Jenita Mattsson',
                'Annemari Hongell', 'Marjaana Raukola-Lindblom', 'Nana Lehtinen', 'Ida Luotonen']

def terapeutit_body(body, log):
    intro = re.search(r'<h2>Asiantuntijat</h2>(<p>.*?</p>)', body, re.S)
    people = parse_people(body)
    if len(people) != 7:
        raise SystemExit(f'TERAPEUTIT: expected 7 people, found {len(people)}')
    assert sorted(PEOPLE_ORDER) == sorted(p['name'] for p in people)
    people.sort(key=lambda p: PEOPLE_ORDER.index(p['name']))
    cards = ''
    for p in people:
        img = re.sub(r' alt="[^"]*"', ' alt=""', p['img'])  # whole card is clickable via the name link
        # card copy of the photo with the top corners filled orange (Nana, 2026-10-04); made in build.py
        img = re.sub(r'src="\.\./images/[^"]+"', f'src="../images/card-{p["slug"]}.jpg"', img)
        cards += (f'<li class="person">{img}'
                  f'<div class="txt"><h3><a class="card-link" href="{p["slug"]}/">{p["name"]}</a></h3><p>{p["details"]}</p></div></li>')
    # the line and toimisto email after the cards (left over from the old contact form) are removed (Nana, 2026-10-04)
    tail = body[body.rfind('<hr>'):]
    assert 'email-link' in tail and tail.count('<p') == 1, tail
    tail = ''
    log('asiantuntijat', 'layout', 'Therapists shown as cards (style A). The whole card opens the therapist\'s own page instead of a CV PDF (Nana, option 2); the name is the link, email and other links in the card stay separate')
    # heading "Asiantuntijat" removed: it repeats the page title (Nana, 2026-10-04)
    return f'{intro.group(1)}<ul class="people">{cards}</ul>{tail}', people

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


def mark_section_breaks(body):
    """Thin grey line between sections (Nana, 2026-10-03): every top-level content heading after the
    first gets class "sep", unless a horizontal rule already separates it."""
    soup = BeautifulSoup(body, 'html.parser')
    BLOCKS = ('hr', 'p', 'ul', 'ol', 'h2', 'h3', 'h4', 'figure', 'img', 'iframe')
    # section level = the highest heading level used on the page (h2, else h3)
    level = 'h2' if soup.find('h2') else 'h3'
    for h in soup.find_all(level)[1:]:
        if not h.get_text(strip=True):
            continue
        prev = h.find_previous(BLOCKS)
        if prev is not None and prev.name == 'hr':
            continue
        h['class'] = h.get('class', []) + ['sep']
    return str(soup)


def page_fixups(slug, body, log):
    """Layout changes Nana asked for on 2026-10-04."""
    if slug not in ('toimintatavat-ja-arvot', 'about-puheklinikka', 'about-puheklinikka-2', 'our-services', 'mit-puheterapia-on-1', 'koulutukset',
                    'mit-puheterapia-on', 'palvelut-lheisille', 'lukitutkimus'):
        return body
    soup = BeautifulSoup(body, 'html.parser')
    def h(text):
        x = soup.find(['h2', 'h3'], string=text)
        assert x is not None, (slug, text)
        return x
    def p_start(text):
        x = next((p for p in soup.find_all('p') if p.get_text(' ', strip=True).startswith(text)), None)
        assert x is not None, (slug, text)
        return x
    if slug == 'mit-puheterapia-on':
        # whole page text replaced by Nana's new text (2026-10-04); the two photos are kept, one per section
        figs = [f.find_parent('div', class_='block') or f for f in soup.find_all('figure')]
        assert len(figs) == 2, slug
        (h1, ps1), (h2, ps2) = AIKUISNEURO
        out = (f'<h3>{h1}</h3>{figs[0]}' + ''.join(f'<p>{p}</p>' for p in ps1) +
               f'<h3>{h2}</h3>{figs[1]}' + ''.join(f'<p>{p}</p>' for p in ps2))
        return out
    if slug == 'palvelut-lheisille':
        # photo moved to the bottom right, next to "Jakso sisältää 3-5 käyntiä…" (Nana, 2026-10-04)
        figs = soup.find_all('figure')
        assert len(figs) == 1, slug
        block = figs[0].find_parent('div', class_='block')
        block['class'] = [c if c != 'float-left' else 'float-right' for c in block['class']]
        p_start('Jakso sisältää').insert_before(block.extract())
        # photo bottom lined up with the last line of text (Nana, 2026-10-04): the last paragraphs and the photo
        # side by side, both aligned to the bottom
        paras = [p_start(t) for t in ('Tuki on tarkoitettu', 'Jakso sisältää', 'Hinta:', 'Ota rohkeasti')]
        pair = soup.new_tag('div', attrs={'class': 'pair'})
        txt = soup.new_tag('div', attrs={'class': 'pair-text'})
        img = soup.new_tag('div', attrs={'class': 'pair-img'})
        paras[0].insert_before(pair)
        for x in paras:
            txt.append(x.extract())
        img.append(block.find('figure').extract())
        block.decompose()
        pair.append(txt); pair.append(img)
        assert pair.find_next_sibling() is None, slug
    if slug == 'lukitutkimus':
        # two columns made one; the photo moves to the bottom right next to "LUKI-tutkimus toteutetaan yhdellä…"
        # (Nana, 2026-10-04). The toimisto email left over from the old contact form is removed (Nana, 2026-10-04).
        row = soup.find('div', class_='row')
        left, right = row.find_all('div', class_='col', recursive=False)
        block = soup.new_tag('div', attrs={'class': 'block float-right span-6'})
        block.append(left.find('figure').extract())
        left.find('p', class_='email-link').decompose()
        head = left.find('h3').extract()
        assert not left.get_text(strip=True)
        left.decompose()
        right.unwrap()
        row.insert_before(head)
        row.unwrap()
        p_start('LUKI-tutkimus toteutetaan yhdellä').insert_before(block)
    if slug == 'koulutukset':
        # toimisto email left over from the old contact form (Nana, 2026-10-04)
        e = soup.find_all('p', class_='email-link')
        assert len(e) == 1, slug
        parent = e[0].parent
        e[0].decompose()
        if parent.name == 'div' and not parent.get_text(strip=True) and not parent.find(['img', 'iframe']):
            parent.decompose()
    elif slug == 'toimintatavat-ja-arvot':
        h('Arvot').decompose()  # repeats the page title
    elif slug in ('about-puheklinikka', 'about-puheklinikka-2'):
        figs = soup.find_all('figure')
        assert len(figs) == 1, slug
        col = figs[0].find_parent('div', class_='col')
        (col or figs[0]).decompose()
        row = soup.find('div', class_='row')
        if row:
            for c in row.find_all('div', class_='col', recursive=False):
                c.unwrap()
            row.unwrap()
    elif slug == 'our-services':
        p_start('In Finland').insert_before(h('How to access Speech Therapy?').extract())
    elif slug == 'mit-puheterapia-on-1':
        q1, q2 = h('Vad är talterapi?'), h('Hur söker man sig till talterapi?')
        p1, p2 = p_start('Talterapi är medicinsk'), p_start('Till talterapi kommer')
        fig = q1.find_parent('div', class_='col').find('figure')
        row = q1.find_parent('div', class_='row')
        block = soup.new_tag('div', attrs={'class': 'block float-left span-6'})
        block.append(fig.extract())
        for x in (q1.extract(), block, p1.extract(), q2.extract(), p2.extract()):
            row.insert_before(x)
        rest = row.get_text(strip=True)
        assert not rest, ('mit-puheterapia-on-1 leftover', rest[:80])
        row.decompose()
    return str(soup)


def side_labels_first(body):
    """On the old site a wide text block (span-8/9) floated right and the section's heading and short
    notes sat beside it on the left. In this layout the wide block is not floated, so those headings ended
    up BELOW their text. Move them back above the text they belong to (reading order as on the old site's
    screen, 2026-10-04)."""
    if 'span-8 float' not in body and 'span-9 float' not in body and 'float-right span-8' not in body and 'float-right span-9' not in body:
        return body
    soup = BeautifulSoup(body, 'html.parser')
    moved = 0
    for b in soup.select('div.block.span-8, div.block.span-9'):
        cls = b.get('class', [])
        if 'float-right' not in cls and 'float-left' not in cls:
            continue
        group, n = [], b.find_next_sibling()
        while n is not None and n.name != 'hr' and not (n.name == 'div' and 'block' in (n.get('class') or [])
                                                        and n.get_text(strip=True)):
            group.append(n)
            n = n.find_next_sibling()
        # drop empty trailing headings / spacers from the group (they stay where they are)
        group = [g for g in group if g.get_text(strip=True)]
        for g in group:
            b.insert_before(g.extract())
            moved += 1
    return str(soup) if moved else body

# Aikuisneurologiset häiriöt, Nana's new page text word for word (2026-10-04).
# Short standalone lines read as subheadings; every other line break starts a new paragraph.
AIKUISNEURO = [
    ('Puheen ja kommunikoinnin haasteet', [
        'Aikuisneurologinen puheterapia kohdistuu sairauden tai vamman aiheuttamiin puheen, kielen ja kommunikoinnin haasteisiin. Tyypillisiä häiriöitä ovat esimerkiksi afasia, laaja-alaiset kielellis-kognitiiviset vaikeudet sekä motoriset puhehäiriöt, kuten dysartria. Haasteita voi esiintyä myös puheen selkeydessä ja äänenkäytössä.',
        'Puheterapia on tavoitteellista kuntoutusta, jonka tarkoituksena on vahvistaa asiakkaan valmiuksia ja mahdollisuuksia vastavuoroiseen ja merkitykselliseen kommunikointiin sekä sujuvaan arkeen. Asiakkaan läheisillä ja kommunikointiympäristöllä on usein tärkeä rooli kuntoutuksessa. Terapian tavoitteet laaditaan yhdessä asiakkaan ja tarvittaessa hänen läheistensä kanssa, ja työskentely perustuu aina asiakkaan yksilöllisiin tarpeisiin ja elämäntilanteeseen.',
        'Puheterapia toteutuu oman puheterapeutin vastaanotolla toimitiloissamme, etäterapiana tai tarvittaessa kotikäyntinä. Terapiakäyntien määrä, tapaamisten pituus ja kuntoutuksen aikataulu määräytyvät kuntoutussuunnitelman ja maksusitoumuksen mukaisesti.',
    ]),
    ('Nielemistoimintojen arviointi ja kuntoutus', [
        'Puheterapiaan voi kuulua myös nielemiseen ja syömiseen liittyvien vaikeuksien eli dysfagian arviointi ja kuntoutus. Nielemistoimintoja voidaan tukea eriasteisissa nielemisvaikeuksissa. Terapeuttimme ovat kouluttautuneet arvioimaan ja kuntouttamaan aikuisneurologisiin sairauksiin ja vammoihin liittyviä nielemisvaikeuksia muun muassa DPNS-menetelmällä (Deep Pharyngeal Neuromuscular Stimulation).',
        'Nielemiskuntoutukseen kuuluu olennaisena osana asiakkaan ja hänen lähiympäristönsä ohjaus ja neuvonta. Kuntoutuksen aikana arvioidaan ja valitaan turvallisia ja tarkoituksenmukaisia toimintatapoja ruokailutilanteisiin. Puheterapeutti voi ohjata esimerkiksi ruoan koostumukseen, ruokailuasentoon ja apuvälineiden käyttöön liittyvissä kysymyksissä.',
        'Toteutamme nielemisen arviointeja ja intensiivisiä DPNS-kuntoutusjaksoja myös laitoshoidossa oleville asiakkaille.',
    ]),
]


def ryhma_layout(body):
    """Ryhmämuotoinen kuntoutus (Nana, 2026-10-04): no button above the afasia section; the afasia text is the
    intro for Piirtäjät and Puhujat, which are shown as two cards side by side; the other groups follow below
    the dividing line. No group text changed."""
    soup = BeautifulSoup(body, 'html.parser')
    btns = soup.select('p.btn-wrap')
    assert len(btns) == 2, len(btns)
    btns[0].decompose()
    intro = soup.find('h3', string='Ryhmämuotoinen kuntoutus henkilöille, joilla on afasia')
    names = ['Piirtäjät, kommunikoinnin aktivointia ryhmässä', 'Puhujat, puheilmaisua ja keskustelutaitoja edistävä ryhmä']
    heads = [soup.find('h3', string=n) for n in names]
    assert intro and all(heads)
    end = heads[1].find_next_sibling('hr')
    assert end is not None
    cards = soup.new_tag('div', attrs={'class': 'places groups'})
    for i, h in enumerate(heads):
        stop = heads[1] if i == 0 else end
        parts, n = [], h.next_sibling
        while n is not None and n is not stop:
            parts.append(n)
            n = n.next_sibling
        card = soup.new_tag('div', attrs={'class': 'place'})
        txt = soup.new_tag('div', attrs={'class': 'txt'})
        card.append(txt)
        h4 = soup.new_tag('h4')
        h4.string = h.get_text()
        txt.append(h4)
        for x in parts:
            x = x.extract()
            if getattr(x, 'name', None) is None:
                continue
            if 'spacer' in (x.get('class') or []):
                continue
            if x.name == 'div' and 'block' in (x.get('class') or []):
                for c in list(x.children):
                    txt.append(c.extract())
                continue
            txt.append(x)
        h.decompose()
        cards.append(card)
    end.insert_before(cards)
    for sp in soup.select('div.spacer'):
        if sp.find_next_sibling() is cards:
            sp.decompose()
    # afasia photo to the top right, beside the opening text, so "Puheklinikalla kokoontuu…" runs full width
    # above the cards (Nana, 2026-10-04)
    photo = intro.find_next_sibling('div')
    assert photo is not None and 'span-6' in photo['class'], photo
    photo['class'] = [c if c != 'float-left' else 'float-right' for c in photo['class']]
    first = soup.find('p')
    assert first.get_text(strip=True).startswith('Ryhmämuotoinen puheterapia on tavoitelähtöistä'), first.get_text()[:40]
    first.insert_before(photo.extract())
    # grey line above the afasia heading, like between the other groups (Nana, 2026-10-04)
    assert intro.find_previous_sibling().name != 'hr'
    intro.insert_before(soup.new_tag('hr'))
    # dysartria group in the same format as Jatkokurssi: heading, bold notes, then the text (Nana, 2026-10-04)
    side = soup.select('div.block.span-4')
    assert len(side) == 1 and side[0].find('h3', string=lambda t: t and t.startswith('Ryhmämuotoinen kuntoutus henkilöille, joilla on dysartria'))
    side[0].unwrap()
    # the other group headings orange like the Piirtäjät and Puhujat card headings (Nana, 2026-10-04)
    titles = ('Jatkokurssi SpeakOut', 'Puheterapiaryhmä Parkinsonin', 'Ryhmämuotoinen kuntoutus henkilöille, joilla on dysartria',
              'Tavoitelähtöiset kuntoutusryhmät')
    done = 0
    for h in soup.find_all('h3'):
        if h.get_text(strip=True).startswith(titles):
            h['class'] = ['group-title']; done += 1
    assert done == 4, done
    return str(soup)
