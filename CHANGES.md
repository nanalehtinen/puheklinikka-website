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
  6. One spelling for everyone, "SPEAK OUT!®" and "LOUD Crowd®": Jenita "SPEAKOUT! ja Loud Crowd® menetelmäkoulutuksella" → "SPEAK OUT!® ja LOUD Crowd® -menetelmäkoulutuksella"; Riitta and Annemari "SPEAK OUT!-" → "SPEAK OUT!®-". The hyphen added before "menetelmäkoulutuksella" is an extra change; Nana confirmed it 2026-10-03. The spelling could not be checked against Parkinson Voice Project's site (blocked from this environment).
  7. Nana: "SanapsisPro sovellukseen" → "SanapsisPro-sovellukseen"
  - Working languages written the same way for everyone: "suomi ja englanti" → "suomi, englanti" (Marjaana, Ida, Nana).
- New text: the link "← Terapeutit" at the end of each profile page.
- Homepage service tiles: the text is centred horizontally and vertically (Nana, 2026-10-03).
- The seven CV PDFs are no longer published (replaced by the profile pages).
- Two large photo PNG files are now served as JPEG (same picture, smaller download).
- Accessibility re-check after these changes: axe-core, all WCAG 2.0/2.1 A and AA rules, 21 pages at desktop and phone width: 0 violations, no broken links. One item axe could not decide (text on the light card background, #3a3a3a on #f6f2ee: 10.2:1, passes).

## 7. More colour: variant A3 with A's header and hero (Nana, 2026-10-03)
Design only, no text changes. Matches the brainstorm mock-up design-ideas/a3b-varikkaat-palvelut.html.
- Header and hero unchanged from style A (4px orange line under the header, beige hero, photo with rounded corners).
- Homepage service tiles: solid orange (#B4580F) with white text, centred. On hover and keyboard focus they turn white with orange text and an orange border; keyboard focus also shows a dark outline.
- Office cards: white with an orange (#C46013) border; the town names are orange.
- Buttons: #B4580F (white text 4.83:1).
- Footer: dark grey #474747 with white text and links (9.3:1). The keyboard focus outline in the footer is white so it shows on the grey.
- All colours are CSS variables at the top of assets/site.css, so the palette can still be changed in one place.

## 8. Menu: "Tapahtumat ja toimintatavat" split in two (Nana, 2026-10-03)
- "Tapahtumat ▾" is a drop-down with Ajankohtaista and Menneet tapahtumat. Those two pages show "Tapahtumat" above the title and only each other in the side menu.
- "Arvot ja toimintatavat" is its own menu link to the same page as before (/toimintatavat-ja-arvot/). It no longer has a side menu or a section name above the title.
- Order: Terapeutit, Palvelut ▾, Tapahtumat ▾, Arvot ja toimintatavat, På svenska ▾, In English ▾, Asiakaspalaute. (Superseded: Asiakaspalaute was later moved before På svenska, see section 13.)
- Page addresses are unchanged. Tested: the drop-down opens with Enter, Tab moves into it, Esc closes it; it also works in the phone menu.

## 9. Consistency sweep (Nana asked, 2026-10-03)
Design only, no text changes. Brought in line with the brainstorm thread's reference stylesheet design-ideas/shared/style-a3.css.
- Orange text, links and the current menu item use #B4580F on every page (was #A34E0E on inner pages). Lines and borders use the logo orange #C46013.
- (Superseded by section 10: the section name was later removed.) Exception, for contrast: the small section name above page titles (e.g. "Tapahtumat") stays #A34E0E, because #B4580F on the beige band is only about 4.4:1 and WCAG AA needs 4.5:1. This differs from style-a3.css.
- One card style: white, 2px orange border, rounded corners. Applies to therapist cards, news cards on Ajankohtaista, the contact box on profile pages and the office cards. Therapist names on cards are orange; the card turns light peach on hover.
- One keyboard focus outline everywhere: dark grey #262626, 3px (was blue on some pages). In the dark footer the outline is white so it can be seen.
- Menu: the current page or section is underlined in orange on every page; drop-down items and the side menu get a light peach background on hover.
- Footer #474747 with white text on every page (already done in section 7).
- Approved by Nana 2026-10-03: buttons invert on hover like the service tiles (orange button turns white with orange text, white button turns orange).

## 10. Uniform look, round 2 (Nana, 2026-10-03)
Design only, no text changes.
- Therapist profile pages: the contact details under the photo no longer have an orange border.
- Ajankohtaista: the posts are no longer separate cards; a thin grey line (#474747, same as the footer) separates them.
- Pages with several sections: a thin grey line (#474747) now separates the sections. The build adds it above every top-level heading after the first, except where the page already had a dividing line there. Existing dividing lines are now the same grey.
- The section name above page titles (e.g. "Palvelut", "Tapahtumat", "Terapeutit") is removed on every page. The side menu still shows which section you are in.
- (Superseded below) The title band stayed beige at this point.

## 11. Orange title band (Nana, 2026-10-03)
- Every inner page's title band is now logo orange (#C46013) with a white page title. The homepage hero stays beige.
- Contrast: white on #C46013 is 4.18:1, which meets WCAG AA only for large text. The page title is 33.6px (25.6px on phones), so it qualifies. No normal-size text is placed in the band.

## 12. Lower footer (Nana, 2026-10-03)
- The footer is less tall: about 80px on a wide screen (was about 130px). The text is slightly smaller (.92rem). The social media buttons stay 44px so they are easy to tap.
- Checked: every page has the dark grey footer. The only page without one is the old address /nanalehtinengmailcom, which immediately forwards to the homepage.

## 13. Nana's answers (2026-10-03)
- Button hover kept on all buttons, including the homepage's Terapeutit and email buttons.
- Menu order: Terapeutit, Palvelut ▾, Tapahtumat ▾, Arvot ja toimintatavat, Asiakaspalaute, På svenska ▾, In English ▾.
- Jenita's "LOUD Crowd® -menetelmäkoulutuksella" hyphen kept.
- Saavutettavuusseloste: draft for Nana's review in site-plan/saavutettavuusseloste-luonnos.md. Not on the site yet.

## 14. Nana's first preview tweaks (2026-10-04)
- Homepage, under "Palvelut": the old "Osaamisalueitamme…" paragraph is replaced by Nana's new text, word for word. It is now as wide as the service tiles.
- Terapeutit, card order: Elina, Riitta, Jenita / Annemari, Marjaana, Nana / Ida.
- Terapeutit, contact details (cards and profile pages):
  - Elina: "yleiset asiat, tietosuojavastaava" starts on a new line.
  - Nana: the phone number starts on a new line.
  - Annemari: "kognitiivinen lyhyterapia" → "kognitiivinen lyhytterapeutti".
  - Ida: "kognitiivinen lyhytterapeutti" added after "puheterapeutti (Turku)".
  - Marjaana: new line "Lisätietoja: Skillful interaction" (Nana's wording; was "Skillfull Interaction"). The link still points to https://www.vikingfilm.fi/marjaana_raukola/suomeksi.html (the address on the current site's card).
- Terapeutit cards: the photos have rounded corners built into the image files. On the cards, the two top corners are now filled with the border orange so there is no white gap. The bottom corners are white. Profile pages use the original photos.
- Headings removed because they repeated the page title: "Asiantuntijat" (Terapeutit) and "Arvot" (Arvot ja toimintatavat). Arvot ja toimintatavat keeps its existing dividing lines; no extra lines were added there.
- In English / About Puheklinikka and På svenska / Introduktion: the photo is removed; the text now uses the full width.
- In English / Our services: "How to access Speech Therapy?" now starts at the paragraph "In Finland…"; "What is Speech Therapy?" covers the first three paragraphs.
- På svenska / Våra tjänster (NOT asked by Nana, same problem as the English page, flagged): "Vad är talterapi?" now sits above the first paragraph and "Hur söker man sig till talterapi?" above the second.
- Terapeutit: the grey line and the toimisto email under the cards are removed (left over from the old "send us a note" form). The footer email stays.
- Koulutukset: the toimisto email left over from the old contact form is removed.
- Koulutukset and Ryhmämuotoinen kuntoutus (NOT asked by Nana, flagged): on the old site, the section headings (and on Ryhmämuotoinen kuntoutus the short notes such as "Tervetuloa mukaan!") sat in a column to the left of the text. In the draft they had ended up below the text they belong to. They are now above it again. No text changed.
- Homepage: new section "Miten puheterapiaan hakeudutaan?" below the service tiles and above the addresses, Nana's text word for word (2026-10-04). Read as a heading plus two paragraphs, split where Nana broke the line. As wide as the tiles.
- Aikuisneurologiset häiriöt: the whole page text is replaced by Nana's new text, word for word (2026-10-04). Read as two subheadings ("Puheen ja kommunikoinnin haasteet", "Nielemistoimintojen arviointi ja kuntoutus") with three paragraphs each; each line break in Nana's message starts a new paragraph. The lone "*" at the end of the message was treated as a stray character. Both photos are kept, one per section.
  - No longer on this page (not in the new text): the old sections "Mitä puheterapia on?", "Miten puheterapiaan hakeudutaan?" (now on the homepage) and "Ryhmämuotoinen kuntoutus", including its "täältä" link to the Ryhmämuotoinen kuntoutus page.
- Ryhmämuotoinen kuntoutus (Nana, 2026-10-04):
  - The button "Lisätietoa ryhmämuotoisesta kuntoutuksesta" above the afasia section is removed.
  - The bottom button "Lisätietoa vuoden 2026 ryhmistä" now says "Lataa esite" (same PDF).
  - (Redone the same day at Nana's request; the Piirtäjät/Puhujat cards were dropped.) Every group now uses the arrangement the dysartria group had on the old site: the group heading and its short notes (e.g. "Vuoden 2026 ryhmää kootaan parhaillaan.", "Kysy lisää!") in a narrow column on the left, the description on the right. On phones the two stack.
  - The afasia photo moved to the top of the page, on the right of the opening text "Ryhmämuotoinen puheterapia on tavoitelähtöistä…" (Nana, 2026-10-04).
  - The afasia text (heading, two paragraphs) stays above as the intro to Piirtäjät and Puhujat, whose names are sub-headings under it. Grey lines separate all six groups (a line between Piirtäjät and Puhujat is new). No text changed.
  - Typo fixed (Nana confirmed): "kootaan parhailaan" → "kootaan parhaillaan" in the Parkinson and dysartria groups.
- Palvelut läheisille: the photo moved to the bottom right, next to "Jakso sisältää 3-5 käyntiä…" (Nana, 2026-10-04). No text change.
- LUKI-tutkimus: the two columns are now one; the photo moved to the bottom right, next to "LUKI-tutkimus toteutetaan yhdellä…" (Nana, 2026-10-04). No text change. The toimisto email left over from the old contact form is removed (Nana, 2026-10-04).
