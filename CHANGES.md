# First draft: what differs from the live site

Draft built 2026-10-03 from the verified capture (site-inventory/). Page text is copied from the live HTML by a script; nothing was retyped.
The full machine list of every change is in CHANGES-generated.md. Screenshots of every page are in preview/.

## 1. Text changes you agreed

| Page | Before | After |
|---|---|---|
| Etusivu (email subject) | Yhteyenotto | Yhteydenotto |
| LUKI-tutkimus | tarvittatessa | tarvittaessa |
| Ajankohtaista | korvaavata tahosta | korvaavasta tahosta |
| Our services (EN) | 4–6 sessions | 3–5 sessions |
| Våra tjänster (SV) | FPA:s, stadens, kommunens eller | FPA:s, välfärdsområdets eller |
| Sanapsis-sovellukset ja tuotteet | ehtävien lisäksi | Tehtävien lisäksi |
| Etusivu, Introduktion, About, Ryhmämuotoinen kuntoutus, Menneet tapahtumat | links to /yhteystiedot (broken) | links to Terapeutit; link text unchanged |

Not applied, and why:
- "kielihäiröt" and "LIsätietoa" were only on the four info pages you dropped. (The earlier inventory said "LIsätietoa" was also on Menneet tapahtumat; the capture shows it is not.)

## 2. Removed, as agreed
- The four unlinked info pages, the draft therapist page, the hidden chat box, the search icon.
- All Squarespace forms (header, Terapeutit, LUKI-tutkimus, Koulutukset) are now the link toimisto@puheklinikka.net. The form questions and help texts are gone.

## 3. New text added for accessibility (approved by Nana 2026-10-03)
Needed for accessibility (WCAG 2.1) or because something had no text before:
- Skip link at the top for keyboard users: "Siirry sisältöön"
- Phone menu button: "Valikko" (the old site used an icon labelled "Menu")
- Hidden labels for screen readers: "Päävalikko" (menu), "Puheklinikka sosiaalisessa mediassa" (social icons), and the names Facebook, LinkedIn, Instagram, toimisto@puheklinikka.net on the icons
- Image descriptions (alt text). All other photos are marked decorative, because the text next to them says the same thing.
  - Riitta's photo (links to her PDF): "Riitta Saari (PDF)"
  - Sanapsis images (they are links): "Sanapsis" and "Sanapsis+"
  - The two course posters on Ajankohtaista: the poster's own text (Tule mukaan! Kommunikaatiokuntoutuskurssi Turun Caribiaan! …)
  - Sanapsis new look screenshot: "Sanapsis-sovelluksen uusi ilme: Production, Comprehension, Reading, Writing, Semantics, Perseveration"
- Map titles on Etusivu: "Kartta: Käsityöläiskatu 4a, Turku" and "Kartta: Kumpulantie 1 A, Helsinki"
- Title of the Google feedback form on Asiakaspalaute: "Asiakaspalaute"

## 4. Look and layout
- Layout, colours and menu follow the old stylesheet: orange header with the logo, grey menu bar, white content column.
- The old font (Proxima Nova) is a paid Adobe font tied to Squarespace. The draft uses Montserrat, a free font that looks similar, stored on the site itself (no Google or Adobe calls).
- Link colour is a slightly darker orange (#a34e0e instead of #c46013), and links are underlined, because the old orange is too faint against white for WCAG AA (4.2:1, needs 4.5:1).
- The header "Info" and "Email" pop-up panels are not reproduced. The contact text ("Contact Us / Ota yhteyttä!" and the email) is now in the footer on every page.
- Some two-column sections (e.g. Ryhmämuotoinen kuntoutus, Koulutukset) are rebuilt from the Squarespace column data. I could not see the live layout (screenshots of the live site were blocked), so please compare these.
- Large photos were resized to max 1500 px wide (Squarespace did the same); image file names are now plain ASCII. PDFs keep their old addresses (/s/…pdf).
- /nanalehtinengmailcom (an accidental copy of the homepage) now forwards to the homepage.

## 5. Accessibility check (WCAG 2.1 A and AA)
Automated: axe-core 4.13 with all WCAG 2.0/2.1 A and AA rules, on all 18 pages at desktop and phone width. Result: 0 violations.
- Fixed on the way: an invisible empty link on the Sanapsis page (existed on the live site).
- 12 items axe could not decide (text next to floating images); I checked them by calculation: body text #4f4f4f on white is 8.2:1.
- Link check: no broken internal links, images or PDFs.

Automated tools find only part of the 49 criteria. Still to be checked by a person:
- The 15 PDFs (they are not checked at all yet; the law covers documents on the site too).
- Whether the image descriptions above are right.
- The Google feedback form and Google Maps are third-party; I cannot change their accessibility.
- A real screen reader and keyboard run-through.
- An accessibility statement (saavutettavuusseloste) page, if you want one. I have not written it.

## 6. Style A and therapist pages (Nana, 2026-10-03)
Design: style A ("selkeä") from the design brainstorm, applied to every page. Text is unchanged except where listed here.
- Header: white with the orange logo and an orange line; the menu is on one line. "Etusivu" is no longer a menu item; the logo links to the homepage. "På svenska" and "In English" stay as drop-downs, because each has two pages (the sketch showed them as plain links).
- Every page has a light title band. Pages inside Palvelut, Tapahtumat ja toimintatavat, På svenska and In English show that section's name above the title, and the section's pages as a side menu (a row of buttons on phones).
- Headings inside the pages moved down one level, so each page has one main heading (better for screen readers). They look the same size as before relative to each other.
- Footer: dark, with "Ota yhteyttä!", the email and the social media icons. The heading "Contact Us" is removed.
- Homepage: rearranged as in the sketch. The first sentence is the main heading. "Tutustu asiantuntijoihimme täällä." is replaced by a "Terapeutit" button. "Osaamisalueitamme…" sits under the heading "Palvelut" with a link to each service page. "Käynti-ja postiosoite:" is a heading, with Turku and Helsinki side by side.
- Ajankohtaista: each dated post is its own card. The second "Ajankohtaista" heading inside the page was removed because it repeated the page title.
- Terapeutit: one card per therapist. The whole card opens the therapist's own page (Nana, 2026-10-03); for screen readers the name is the link. Email and other links in the card stay separate and clickable. The intro sentence "Voit tutustua osaamiseemme tarkemmin kuvaa napauttamalla." is now "Saat lisätietoja napauttamalla." (Nana's wording, 2026-10-03). Punctuation addition: the full stop at the end is added; Nana's text had none.
- New profile pages, e.g. /asiantuntijat/elina-uusi-hakala/. All seven bios are Nana's text word for word (only line breaks and double spaces tidied). One approved edit: Elina "tietoturvavastaavana" → "tietosuojavastaavana". Each page ends with the working languages line ("Työskentelykielet: …").
- Not shown yet: the empty "Asiakasryhmät:" lines (six bios), until Nana fills them in.
- Bio fixes approved by Nana (2026-10-03), changed in the bios:
  1. Riitta: "äänihäiriöden" → "äänihäiriöiden"
  2. Marjaana: "perehtynyt on nielemishäiriöiden" → "perehtynyt nielemishäiriöiden" (extra "on" removed)
  3. Marjaana: "yliopisto-opettaajana" → "yliopisto-opettajana"
  4. Marjaana: "(mm.DPNS)" → "(mm. DPNS)"
  5. Space added after the hyphen: "yksilö-ja" → "yksilö- ja" (Annemari, Jenita), "vuodeosasto-että" → "vuodeosasto- että", "kommunikointi-ja" → "kommunikointi- ja" (Jenita)
  6. One spelling for everyone, "SPEAK OUT!®" and "LOUD Crowd®": Jenita "SPEAKOUT! ja Loud Crowd® menetelmäkoulutuksella" → "SPEAK OUT!® ja LOUD Crowd® -menetelmäkoulutuksella"; Riitta and Annemari "SPEAK OUT!-" → "SPEAK OUT!®-". The hyphen added before "menetelmäkoulutuksella" is an extra change, not yet confirmed by Nana. The spelling could not be checked against Parkinson Voice Project's site (blocked from this environment).
  7. Nana: "SanapsisPro sovellukseen" → "SanapsisPro-sovellukseen"
  - Working languages written the same way for everyone: "suomi ja englanti" → "suomi, englanti" (Marjaana, Ida, Nana).
- New text: the link "← Terapeutit" at the end of each profile page.
- Homepage service tiles: the text is centred horizontally and vertically (Nana, 2026-10-03).
- The seven CV PDFs are no longer published (replaced by the profile pages).
- Two large photo PNG files are now served as JPEG (same picture, smaller download).
- Accessibility re-check after these changes: axe-core, all WCAG 2.0/2.1 A and AA rules, 21 pages at desktop and phone width: 0 violations, no broken links. One item axe could not decide (text on the light card background, #3a3a3a on #f6f2ee: 10.2:1, passes).
