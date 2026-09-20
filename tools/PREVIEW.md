# Local preview

The published Quran.ws site imports this repository's content. This optional
Python preview lets contributors read local changes in English and Arabic.
It is a content preview, not a reproduction of the website's design.

From the repository root, using Python 3.9 or later:

```sh
source .venv/bin/activate
python -m pip install -r requirements-preview.txt
make preview
```

If the environment uses uv without pip, install with
`uv pip install -r requirements-preview.txt` instead.

Open http://127.0.0.1:8765/en/naming/ or
http://127.0.0.1:8765/ar/naming/. Use `python tools/preview.py --port 8766`
to choose another port.

Edit `content/pages/<page>.yml` for the five guideline pages. Each English
field has its Arabic counterpart in the same file. Saving the source
regenerates the pages and refreshes the browser, preserving its scroll position.
The preview also regenerates dictionary and registry pages when their YAML
or TSV sources change. Direct edits to prose Markdown refresh automatically.
Expand "Source to edit" on a page to find its source.

The preview runs only page generators; it does not replace the full build or
translation checks. After reviewing an Arabic translation, stamp that page
with `python tools/generate_pages.py --stamp <page>`. Before contributing,
run `python tools/build.py` and `python -m pytest -q`.

Stop the preview with Ctrl-C. Changes to the preview script require a restart.
