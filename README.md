# Puheklinikka website

Static version of www.puheklinikka.net, moved from Squarespace to GitHub Pages.

- `docs/` is the published site (GitHub Pages serves this folder).
- `tools/build.py` regenerates `docs/` from the captured Squarespace pages. The capture and the agreed changes live in the Puheklinikka project's shared files (`site-inventory/`, `site-plan/decisions.md`); run `python3 tools/build.py` there and copy the output into `docs/`.
- `CHANGES.md` lists every difference from the old Squarespace site.

The domain www.puheklinikka.net still points to Squarespace. A `CNAME` file is added only when the domain is switched over.
