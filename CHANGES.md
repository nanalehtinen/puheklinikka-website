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
  - Intro: the heading "Ryhmämuotoinen kuntoutus henkilöille, joilla on afasia", its photo and its two paragraphs ("Puheklinikalla kokoontuu säännöllisesti kaksi afasian kuntoutusryhmää…" and "Ryhmät kokoontuvat 20 kertaa vuodessa…").
  - Below it, two cards side by side (same style as the office cards on the homepage): Piirtäjät and Puhujat, each with its notes ("Syksyn 2026 ryhmää…", "Tervetuloa mukaan!") and its description. The group names are now card headings one level below the afasia heading. No text changed.
  - Then the dividing line and the other groups as before.
  - A later redo (heading-beside-text for every group, photo at the top) was tried and reverted the same day; Nana chose this cards version (2026-10-04).
  - On top of the cards version (Nana, 2026-10-04): the afasia photo moved to the top right, beside "Ryhmämuotoinen puheterapia on tavoitelähtöistä…", so "Puheklinikalla kokoontuu…" runs full width above the cards; the headings Jatkokurssi, Parkinson, dysartria and Tavoitelähtöiset are orange like the card headings; the dysartria group now has the same format as Jatkokurssi (heading, bold notes, then the text; its narrow left column is gone). No text changed.
  - A grey line added above the heading "Ryhmämuotoinen kuntoutus henkilöille, joilla on afasia", like between the other groups (Nana, 2026-10-04).
  - Jatkokurssi SpeakOut!®: "Ilmoittaudu mukaan sähköpostitse tai täyttämällä yhteydenottolomake." → "Ilmoittaudu sähköpostitse tästä." The email link (to Annemari, same subject line) is now on "tästä"; the yhteydenottolomake link is removed. "mukaan" dropped to match Nana's wording. "Tervetuloa mukaan!" moved from its own line above into the same paragraph, right after the link: "Ilmoittaudu sähköpostitse tästä. Tervetuloa mukaan!" (Nana, 2026-10-04).
  - Jatkokurssi SpeakOut!®: the sentence "Voit ilmoittautua myös ottamalla yhteyttä puheterapeutti Annemari Hongelliin tai Riitta Saareen." removed (Nana, 2026-10-04).
  - Typo fixed (Nana confirmed): "kootaan parhailaan" → "kootaan parhaillaan" in the Parkinson and dysartria groups.
- Sanapsis-sovellukset ja tuotteet (Nana, 2026-10-04): the professional app is now called "SanapsisPro" in its heading (was "Sanapsis") and in the first sentence ("**SanapsisPro** on Puheklinikalla suunniteltu…"). Its image is replaced with Nana's screenshot of the app's main menu (iPad status bar cropped off), alt text "SanapsisPro-sovelluksen päävalikko" (was "Sanapsis"); still links to sanapsis.com. Unchanged: page title and menu name "Sanapsis-sovellukset ja tuotteet", "Sanapsis Lite", "Sanapsiksen sivuilta", Sanapsis+, the App Store link.
- Homepage service tiles, COMPARISON for others to see, not a final decision (Nana, 2026-10-04): the upper row (Aikuisneurologiset häiriöt, Ryhmämuotoinen kuntoutus, Ääniterapia, Palvelut läheisille) is white with orange border and orange text; on hover/keyboard focus a peach background and underline like the therapist cards, with the text a shade darker (#A34E0E) so it keeps AA contrast on peach. The lower row stays orange. Switch with LIGHT_TILES in tools/style_a.py (0 = all orange, 8 = all white).
- Homepage office cards (Turku and Helsinki), new sentence from Nana word for word, as the last paragraph of each card: "Tilojen välittömään läheisyyteen pääsee esteettömästi, ja tiloissa voi liikkua itsenäisesti tai avustettuna henkilökohtaisten apuvälineiden avulla." (Nana, 2026-10-04)
- Arvot ja toimintatavat: new last paragraph, Nana's sentence word for word: "Verkkosivustomme täyttää digitaalisten palvelujen tarjoamisesta annetun lain (306/2019) saavutettavuusvaatimukset." followed by a link "Saavutettavuusseloste" (link text is my wording) to a new page /saavutettavuusseloste/, which has only its title until Nana completes the statement (Nana, 2026-10-04). Launch checklist: the sentence states full conformance, so it must be true by launch.
- Terapeutit cards: on hover the name turns a darker orange (#A34E0E) so it keeps AA contrast on the peach hover background (Nana, 2026-10-04).
- Headings on every page (Nana, 2026-10-04, from heading-audit.md): headings now form a clean outline with no skipped levels: H1 page title, H2 section headings, H3 sub-headings (WCAG 1.3.1, 2.4.6). Section headings that were H3 (or H4 on Ääniterapia) are now H2 and keep their old look; the Sanapsis page's section headings (SanapsisPro, Sanapsis+, Muut tuotteet) are now the same size as section headings elsewhere (were bigger) and its sub-headings slightly smaller. "Ajanmukaisuus" (Arvot ja toimintatavat) and "Nenälovimuki Flexi cup" (Sanapsis page) were one level lower than their neighbours; now they match. Orange group headings, cards, news dates and therapist names look as before. The homepage keeps its larger section headings (hero layout). No text changed.
- TRIAL (Nana, 2026-10-04): two new services, "Nielemishäiriöt" and "Puheen sujuvuuden häiriöt", added as homepage cards and as pages in the Palvelut menu and side menu (/nielemishairiot/, /puheen-sujuvuuden-hairiot/). The pages have only their title until Nana sends the text; they must not go live empty. Card order: row 1 Aikuisneurologiset häiriöt, Nielemishäiriöt, Puheen sujuvuuden häiriöt, Ryhmämuotoinen kuntoutus (white, comparison); row 2 Ääniterapia, Palvelut läheisille, LUKI-tutkimus, Tutkimus ja konsultointi; row 3 Koulutukset, Sanapsis-sovellukset ja tuotteet. Menus use the same order. Revert: remove the two lines in MENU and NEW_PAGES in tools/build.py.
  - Then "keep only two rows" (Nana, 2026-10-04): read as two rows of five on desktop (no card dropped). Row 1 (white): Aikuisneurologiset häiriöt, Nielemishäiriöt, Puheen sujuvuuden häiriöt, Ryhmämuotoinen kuntoutus, Ääniterapia. Row 2: Palvelut läheisille, LUKI-tutkimus, Tutkimus ja konsultointi, Koulutukset, Sanapsis-sovellukset ja tuotteet. Narrower screens: three per row below 1100 px, two on phones, one on very small phones.
  - Then LUKI-tutkimus and Palvelut läheisille swapped (Nana, 2026-10-04). Row 2: LUKI-tutkimus, Palvelut läheisille, Tutkimus ja konsultointi, Koulutukset, Sanapsis-sovellukset ja tuotteet. Same order in the Palvelut menu and side menu.
  - Then Ryhmämuotoinen kuntoutus and Nielemishäiriöt swapped (Nana, 2026-10-04). Row 1: Aikuisneurologiset häiriöt, Ryhmämuotoinen kuntoutus, Puheen sujuvuuden häiriöt, Nielemishäiriöt, Ääniterapia. Menus follow.
  - Then Puheen sujuvuuden häiriöt and Nielemishäiriöt swapped (Nana, 2026-10-04). Row 1: Aikuisneurologiset häiriöt, Ryhmämuotoinen kuntoutus, Nielemishäiriöt, Puheen sujuvuuden häiriöt, Ääniterapia. Menus follow.
- Menu label, side menu and homepage card "Sanapsis-sovellukset ja tuotteet" → "Sovellukset ja tuotteet" (Nana, 2026-10-04). The page's own title (orange band, browser tab) and address /new-page/ still use the old name.
- Homepage "Miten puheterapiaan hakeudutaan?": the word "mahdollisesti" removed (1 occurrence): "…toteutuu Kelan, hyvinvointialueen tai vakuutusyhtiön maksusitoumuksella tai palvelusetelillä." (Nana, 2026-10-04)
- Homepage: the extra space above "Käynti-ja postiosoite:" removed (Nana, 2026-10-04). Cause: the last paragraph of the section above kept its bottom margin (28 px) on top of the section spacing; now the gap is the same as above "Miten puheterapiaan hakeudutaan?". No text change.
- Homepage Palvelut intro: Nana's sentence added word for word at the end of the paragraph above the service cards: "Lisätietoa koulutusmahdollisuuksista osaamisalueisiimme liittyen sekä kehittämistämme sovelluksista ja tuotteista löydät alta." (Nana, 2026-10-04)
  - Then revised (Nana, 2026-10-04): the added sentence is now "Alta löydät lisätietoa myös koulutusmahdollisuuksista osaamisalueisiimme liittyen sekä kehittämistämme sovelluksista ja tuotteista." (same place, end of the paragraph). Paragraph break and the LUKI sentence change wait for Nana's full wording.
- Homepage Palvelut intro replaced with Nana's full new text, word for word, in two paragraphs (break before "Toteutamme LUKI-tutkimuksia…") (Nana, 2026-10-04). Supersedes the sentence edits above.
- Homepage heading "Käynti-ja postiosoite:" → "Käynti- ja postiosoite:" (Nana, 2026-10-04).
- The section "Nielemistoimintojen arviointi ja kuntoutus" (heading, its three paragraphs and its photo) moved from Aikuisneurologiset häiriöt to the Nielemishäiriöt page (Nana, 2026-10-04). No text changed. Aikuisneurologiset häiriöt now has only "Puheen ja kommunikoinnin haasteet".
- Ryhmämuotoinen kuntoutus: the four orange group headings (Jatkokurssi, Parkinson, dysartria, Tavoitelähtöiset) are dark grey again, like the afasia heading and section headings on every other page (Nana flagged the inconsistency, 2026-10-04). The Piirtäjät/Puhujat card headings stay orange (card style).
- Ryhmämuotoinen kuntoutus, Jatkokurssi SpeakOut!®: the line "Ilmoittaudu sähköpostitse tästä. Tervetuloa mukaan!" moved down into the description, just above "Ryhmään voi tulla myös itsemaksavana (50€)." (Nana, 2026-10-04). No text change.
- Ryhmämuotoinen kuntoutus, Jatkokurssi: "Seuraava tapaaminen on 3.12.2026 klo 11-12." is now bold (Nana, 2026-10-04).
- TRIAL, Ryhmämuotoinen kuntoutus (Nana, 2026-10-04): the Piirtäjät and Puhujat cards removed; the two texts sit side by side with a thin grey vertical line between them, headings dark grey (#262626, the site's heading colour). On phones they stack with a horizontal line between. No text change. Revert: delete the TRIAL block in tools/assets/site.css.
- Ryhmämuotoinen kuntoutus: the paragraph "Huom. Vuonna 2026 kuntoutusryhmät kokoontuvat poikkeuksellisesti vain syyskaudella… ota yhteyttä niin mietitään ratkaisuvaihtoehtoja." removed (Nana, 2026-10-04).
- Therapist profile pages (all 7): new line "Asiakasryhmät: TBA" under the working languages, placeholder until Nana sends the keywords (Nana, 2026-10-05). Must be filled before launch.
- Homepage service cards: all ten are orange and turn white on hover/keyboard focus, like the lower row was (Nana, 2026-10-10). The white upper-row comparison is ended.
- Homepage Palvelut intro, last sentence: "Lisätietoa palveluistamme sekä koulutusmahdollisuuksista osaamisalueisiimme liittyen ja puheterapian tueksi kehittämistämme sovelluksista ja tuotteista löydät alta." → "Lisätietoa palveluista, koulutuksista, tuotteista ja puheterapian tueksi kehittämistämme sovelluksista löydät alta." (Nana, 2026-10-10)
- Therapist profiles for Elina Uusi-Hakala, Annemari Hongell, Riitta Saari and Jenita Mattsson: bio text replaced with Nana's new text (2026-10-10), word for word (source kept in tools/bios-2026-10-10.txt). The "Asiakasryhmät: TBA" placeholder is gone on these four; Marjaana, Ida and Nana still show it.
  - Layout only: "Täydennyskoulutus", "Valikoidut koulutukset ja pätevyydet:" and "Asiakasryhmät:" shown as H2 headings; the Asiakasryhmät lines as a bulleted list, with the four indented lines as a sub-list under the first item.
  - One edit: Elina "tietoturvavastaavana" → "tietosuojavastaavana", as Nana confirmed earlier.
  - Nana's fixes (2026-10-10): "SPEAK OUT! & LOUD Crowd Training" → "SPEAK OUT!® & LOUD Crowd® Training" (Riitta, Jenita); comma added after "…and their Families" (Annemari); "Transsukupuolisen ääniterapia" → "Transsukupuolisten ääniterapia" (Riitta ×3, Jenita); Jenita "Täydennyskoulutus" → "Täydennyskoulutus:".
  - Uniform on all seven profiles (Nana, 2026-10-10): the languages line comes last; "Asiakasryhmät:" is a heading everywhere, so on Marjaana's, Ida's and Nana's pages the placeholder now reads as the heading "Asiakasryhmät:" with "TBA" under it, above the languages line.
- Therapist profiles for Marjaana Raukola-Lindblom, Ida Luotonen and Nana Lehtinen: bio text replaced with Nana's new text (2026-10-10), word for word (source in tools/bios-2026-10-10b.txt), in the same layout as the other four (H2 headings, Asiakasryhmät as a list, languages line last). Nana's bulleted Sanapsis list kept as a list.
  - Marjaana: Asiakasryhmät filled in. The four lines "Yksilö- ja ryhmämuotoinen kuntoutus" … "Ohjaavat puheterapiajaksot" are nested under "Nuoret, työikäiset ja iäkkäät asiakkaat" as on the other profiles; the message showed no indentation, so this is assumed, flagged to Nana.
  - Ida and Nana: no Asiakasryhmät in the new text, so "Asiakasryhmät: TBA" stays, flagged to Nana.
- Therapist profiles, all seven: languages line in one format, "Työskentelykielet: xx, xx." (Nana, 2026-10-10). Elina and Riitta: full stop added; Marjaana, Ida and Nana: "suomi ja englanti." → "suomi, englanti.".
- Ida Luotonen: Asiakasryhmät filled in with Nana's list (2026-10-10), word for word; replaces "TBA". Nana Lehtinen: Asiakasryhmät section removed from her own page (Nana, 2026-10-10). No TBA placeholders remain on the profiles.
- Annemari Hongell (Nana, 2026-10-10): "kokosi ruotsinkielistä normiaineistoa Nopean sarjallisen nimeämisen testiin." → "kokosi ruotsinkielistä normiaineistoa arviointityökaluun Nopean sarjallisen nimeämisen testi."; the words "tukipalveluita kuntoutujien läheisille kognitiivisen lyhytterapian muodossa" now link to the Palvelut läheisille page.
- Homepage service tiles (Nana, 2026-10-10 04:42): all ten white with orange text, turning orange with white text on hover/focus (reversed from all-orange).
- Ida Luotonen (Nana, 2026-10-10): paragraph break after the first sentence "…(Puheterapiapalvelut Ida Luotonen)." No text change.
- Palvelut läheisille (Nana, 2026-10-10): last sentence "Ota rohkeasti yhteyttä, olemme täällä sinua varten." removed.
- Nielemishäiriöt (Nana, 2026-10-10): "…liittyviä nielemisvaikeuksia muun muassa DPNS-menetelmällä (Deep Pharyngeal Neuromuscular Stimulation)." → "…liittyviä nielemisvaikeuksia."; "intensiivisiä DPNS-kuntoutusjaksoja" → "intensiivisiä kuntoutusjaksoja".
- Tutkimus ja konsultointi (Nana, 2026-10-10), the 1–2 käynnistä paragraph: "ja se voidaan toteuttaa joko laitoksessa (esimerkiksi terveyskeskuksen vuodeosastolla) tai vastaanotolla." → "ja käynnit voidaan toteuttaa laitoksessa (esimerkiksi vuodeosastolla), kotikäynnillä tai vastaanotolla."; "Tarvittaessa tutkimus toteutetaan yhteistyössä hoitavan puheterapeutin kanssa." removed; "johon sisältyvät suositukset jatkotoimenpiteistä." → "johon sisältyy suositus jatkotoimenpiteistä."
- Koulutukset (Nana, 2026-10-10), Nana's new wording:
  - Intro: "Ota yhteyttä – suunnitellaan yhdessä juuri teidän tarpeisiinne sopiva kokonaisuus!" → "Suunnittelemme mielellämme myös juuri teidän tarpeisiinne sopivan kokonaisuuden. Ota yhteyttä!" (Nana's message had no "tähän"; replaced the matching sentence, flagged.)
  - Aivoverenkiertohäiriöt: "…liittyy hyvin monenlaisia kommunikoinnin häiriöitä… esimerkiksi puheen tuottamisen…" → "…voi liittyä monenlaisia kommunikoinnin haasteita… eri-asteisina puheen tuottamisen…"; "vastavuoroista, ongelmista huolimatta?" → "vastavuoroista haasteista huolimatta?"; "avain yhteisen toimintamallin löytämiseen ja onnistuneen…" → "avain onnistuneen…".
  - Tapaturmaiset aivovammat: "mutta jokin tuntuu silti "pois paikaltaan" – potilas ei toimi…" → "mutta kuntoutuja ei toimi…"; paragraph "Kommunikointi- ja vuorovaikutustaitojen muutokset…itsenäiseen asumiseen." removed; "aivovammojen jälkeisistä vuorovaikutushäiriöistä." → "aivovammojen jälkeisiin vuorovaikutushaasteisiin liittyen."
  - Ääni työvälineenä: both paragraphs replaced with Nana's new two paragraphs (word for word; two double spaces normalised; "tai sekä kouluttajia" kept as written, flagged).
  - Nielemisvaikeudet: second paragraph replaced with Nana's new text.
  - New last section after a line: "Koulutukset hinnoitellaan aina yksilöllisesti. Ota yhteyttä niin teemme tarjouksen!"
  - Empty heading left over from the old site at the bottom of the page removed (no visible change; screen readers announced it). The build now removes empty headings on every page.
- Sovellukset ja tuotteet (Nana, 2026-10-10):
  - Bold removed from "Sanapsis+-sovelluksen avulla voit kohentaa… puhuminen, kuuntelu, lukeminen ja kirjoittaminen." and from "toimisto@puheklinikka.net".
  - Ordering paragraph "Tuotteita voi tilata… Tuotteet toimitetaan postitse… Tuotteet voi myös noutaa…" replaced with Nana's new text, kept as one paragraph (05:23): "Tuotteita voi tilata suoraan terapeuteiltamme tai sähköpostitse osoitteesta toimisto@puheklinikka.net. Tuotteet voi noutaa Turun toimipisteeltämme ennalta sovittuna ajankohtana. Toimitamme tuotteita myös postitse. Tee tilaus sähköpostitse, ja saat laskun joko sähköpostitse tai postitse. Postitettaviin tuotteisiin lisätään toimituskulu toteutuneen mukaan sekä toimistomaksu 11,50€." (two double spaces normalised).
  - Removed: "Kaikki Sanapsis+-sovelluksen tehtävät perustuvat arkisanastoon… suomeksi, ruotsiksi ja englanniksi." and "Vastaamme mielellämme kaikkiin kysymyksiin – otathan rohkeasti yhteyttä!"
  - "Kaikki tuotteet ovat käytössä toteuttamassamme kuntoutuksessa, joten ne ovat huolellisesti valittuja sekä terapiakäytössä…" → "Kaikki tuotteet ovat huolellisesti valittuja ja terapiakäytössä…"
  - Nenälovimuki: added after the instructions link: "Mukia on saatavana kolmena erilaisena versiona:" + the three versions as a bulleted list + "Hinta on 18,00€/kpl." (Nana's text word for word; "valmitettu" → "valmistettu", Nana confirmed).
  - Sitruuna-glyseriinitikut: added "Hinta: 35,00€/ltk (75kpl)".
  - Resonaattoriputki: added "Pituudet: 26cm, 26,5cm, 27cm, 27,5cm, 28cm" and "Hinta: 11,50€/kpl" ("HInta" → "Hinta"; € sign added, Nana confirmed).
- Homepage, Miten puheterapiaan hakeudutaan? (Nana, 2026-10-10): "Meille pääset nopeallakin aikataululla. Keskimääräisesti ensimmäinen tapaaminen järjestyy noin kahden viikon sisällä yhteydenotosta." placed in the second paragraph between "…puheterapiaan hakeutumisen eri vaiheissa." and "Tarjoamme palveluita…" (moved twice at Nana's request, 05:39 and 05:45; double space normalised).
- Arvot ja toimintatavat (Nana, 2026-10-10): paragraph break before "Asiakas ja hänen lähihenkilönsä…"; "jotka osallistuvat hänen hoitoonsa tai kuntoutukseensa." → "jotka osallistuvat hoitoon tai kuntoutukseen." (double space normalised).
- About Puheklinikka, English (Nana, 2026-10-10): "…toimisto(at)puheklinikka.net or visit our Contact page for details." → "…toimisto(at)puheklinikka.net."; the "In addition to clinical services… SanapsisPro… Sanapsis+…" text → "To learn about our apps, SanapsisPro and Sanapsis+, please navigate to www.sanapsis.com" (link to https://www.sanapsis.com; "Sanapsis +" written as "Sanapsis+" like elsewhere, double space normalised, no final full stop as in Nana's text; all flagged).
- Our services (English), Support for family members (Nana, 2026-10-10): bold removed from "Annemari Hongell", "3–5 sessions", "Turku or remotely", "Finnish or Swedish", "Price:" and "toimisto@puheklinikka.net". The bold lead line "Puheklinikka offers support sessions…" kept bold, as on the Finnish page. No text change.
- Puheen sujuvuuden häiriöt (Nana, 2026-10-10): page text added, word for word: heading "Puheen sujuvuuden arviointi ja kuntoutus" and three paragraphs. The page is no longer empty.
- Our services (English), Support for family members (Nana, 2026-10-10): English-only text removed to match the Finnish Palvelut läheisille page: "Sessions are led by Annemari Hongell, a speech-language therapist with additional training in cognitive brief therapy techniques."; ", 2025" in the price; "For more information and bookings: toimisto@puheklinikka.net / Don’t hesitate to get in touch – we are here for you."
- Our services (English), Support for family members: English versions of the Finnish-only text, approved by Nana (2026-10-10): new first sentence "When a family member becomes ill or is injured, everyday life can change suddenly." (Nana's "eryday … suddently" read as "everyday … suddenly"); third bullet "Strengthen your ability to adapt to a changed daily life" → "Make communication and everyday life smoother"; new text "The support is intended for all family members of adults in neurological rehabilitation, regardless of where speech therapy takes place or whether it is currently ongoing. You do not need a referral, and the person in rehabilitation does not need to be a client of Puheklinikka." replaces "You do not need a referral to access the sessions."; "The program includes 3–5 sessions…" now its own paragraph.
- Aikuisneurologiset häiriöt (Nana, 2026-10-10): new last paragraph "Puheterapia toteutuu tyypillisesti maksusitoumuksella tai palvelusetelillä. Omakustannehinta: 139,10€/45min".
- Prices (Nana, 2026-10-10), new last paragraph, word for word:
  - Ryhmämuotoinen kuntoutus: "Puheterapia toteutuu tyypillisesti maksusitoumuksella tai palvelusetelillä. Joihinkin ryhmiin on mahdollista osallistua myös omakustanteisesti. Omakustannehinta:" followed on separate lines by "60min ryhmä 50,00€/krt" and "90min ryhmä 100,00€/krt" (after the "Lataa esite" button, at the very end of the page).
  - Nielemishäiriöt, Puheen sujuvuuden häiriöt, Ääniterapia: "Puheterapia toteutuu tyypillisesti maksusitoumuksella tai palvelusetelillä. Omakustannehinta: 139,10€/45min".
- Sovellukset ja tuotteet (Nana, 2026-10-10 05:55): toimistomaksu 11,50€ → 15,50€.
- Tutkimus ja konsultointi (Nana, 2026-10-10): "Omakustannehinta: 139,10€/45min tapaaminen" added after the last paragraph of Puheterapeuttinen tutkimus; "…puheen sujuvuuteen sekä kasvojen alueen sensomotoriikkaan." → "…puheen sujuvuuteen, kasvojen alueen sensomotoriikkaan sekä nielemishäiriöihin."; the whole Nielemistutkimus section (heading, three paragraphs, photo) moved to Nielemishäiriöt as its second section, after a line, before the price paragraph. No text change in the moved section.
- Tutkimus ja konsultointi, Konsultointi (Nana, 2026-10-10): "Konsultointi hinnoitellaan yksilöllisesti." added as the last sentence of the last paragraph (double space normalised).
- Aikuisneurologiset häiriöt (Nana, 2026-10-10 06:00): "Omakustannehinta: 139,10€/45min" starts on a new line within the same paragraph.
- Prices (Nana, 2026-10-10 06:01): "Omakustannehinta…" starts on a new line within the same paragraph on Ryhmämuotoinen kuntoutus, Nielemishäiriöt, Puheen sujuvuuden häiriöt and Ääniterapia (as on Aikuisneurologiset häiriöt). Ryhmämuotoinen kuntoutus: "Omakustannehinta: 60min ryhmä 50,00€/krt, 90min ryhmä 100,00€/krt" on one line.
- Nielemishäiriöt (Nana, 2026-10-10 06:07): "Puheterapia toteutuu tyypillisesti maksusitoumuksella tai palvelusetelillä. / Omakustannehinta: 139,10€/45min" now under the first section (Nielemistoimintojen arviointi ja kuntoutus); the price under Nielemistutkimus changed to "Tutkimus toteutuu tyypillisesti maksusitoumuksella. / Omakustannehinta: 139,10€/45min".
- Sovellukset ja tuotteet, Nenälovimuki (Nana, 2026-10-10 06:11): the three cup descriptions shortened to "Pieni, 0,5 dl (vaaleanpunainen)", "Keskikokoinen, 1dl (sininen)", "Suuri 2dl, suunniteltu erityisesti itsenäiseen juomiseen (vihreä)"; "Hinta on 18,00€/kpl." → "Hinta: 18,00€/kpl". Word for word (one double space normalised).
- Homepage (Nana, 2026-10-10 06:12): "Meille pääset nopeallakin aikataululla. Keskimääräisesti ensimmäinen tapaaminen…" → "Meille pääset nopeallakin aikataululla ja keskimääräisesti ensimmäinen tapaaminen…".
- Nenälovimuki (Nana, 2026-10-10 06:14): cup sizes made uniform: "1dl" → "1 dl"; "Suuri 2dl," → "Suuri, 2 dl,".
- Nenälovimuki (Nana, 2026-10-10 06:16): "Mukia on saatavana kolmena erilaisena versiona:" → "Mukia on saatavana kolmena versiona:".
- Nenälovimuki (Nana, 2026-10-10 06:16): order is now "Apuväline turvalliseen juomiseen." / versions list / "Ohjeet nenälovimukin käyttöön löydät tästä linkistä." / "Hinta: 18,00€/kpl" (instructions line moved to just above the price). Nana's pasted block had the earlier wording ("kolmena erilaisena versiona", "1dl", "Suuri 2dl"); the wording she approved minutes before was kept, flagged.
- Tapahtumat (Nana, 2026-10-10): "Menneet tapahtumat" replaced by one page per year, 2025–2016 (titles "Tapahtumat 2025" etc., address /tapahtumat-2025/ etc.). The years are listed under Ajankohtaista in the Tapahtumat menu and side menu. Every post moved word for word to its year (98 posts, nothing left out); the year column of the old page is gone. "Tunnelmalista Joulua ja energistä vuotta 2024!" has no date; placed under 2023 (it sat between the January 2024 and September 2023 posts; Nana confirmed). The old Menneet tapahtumat address forwards to 2025.
- Tapahtumat (Nana, 2026-10-10 06:27): no dropdown any more; "Tapahtumat" in the main menu opens Ajankohtaista directly. Ajankohtaista and the years 2025–2016 are links in the side menu. (The old year column was already removed in the year-page change.)
- Palvelut läheisille: the photo moved to the bottom right, next to "Jakso sisältää 3-5 käyntiä…" (Nana, 2026-10-04). No text change.
  - Then (Nana, 2026-10-04): the photo's bottom edge lines up with the last line of text ("Ota rohkeasti yhteyttä…"). To do that, the last four paragraphs (from "Tuki on tarkoitettu…") now sit in a column beside the photo, so "Tuki on tarkoitettu…" is narrower than before. On phones the photo comes below the text. No text change.
- LUKI-tutkimus: the two columns are now one; the photo moved to the bottom right, next to "LUKI-tutkimus toteutetaan yhdellä…" (Nana, 2026-10-04). No text change. The toimisto email left over from the old contact form is removed (Nana, 2026-10-04).
