# CLAUDE.md

Instructions for the agent that drafts and edits pages in this repository. The
two writing pages under `docs/agent/{ar,en}/` are written for you, not for a
reader of the guidelines.

## Where a page lives

- A guideline page (naming, quranic-text, versioning, engineering,
  repositories) is written once, as rules, in `content/pages/<page>.yml`.
  Every text field has an `_ar` twin. `python3 tools/generate_pages.py`
  renders `content/en/<page>.md` always and `content/ar/<page>.md` once every
  field has its Arabic. Never edit the rendered pages.
- After writing or revising Arabic, run `python3 tools/generate_pages.py
  --stamp <page>` so the translation is recorded as current;
  `tests/test_pages.py` fails when English changed after its Arabic did.
- A prose page (`content/{ar,en}/index.md`, `licensing.md`, and
  `reference/standard.md` and `reference/decisions.md`) is one file per
  language.
- Nothing in `content/` or `README.md` mentions the agent, this file, or the
  tooling that writes the pages. Those belong in `docs/agent/` and `tools/`.

## Before writing or editing a page

Read the rules and follow them. Each page ends with a "before you publish"
checklist — answer it before you call the work finished.

| Read | For |
| --- | --- |
| [`docs/agent/ar/writing-style.md`](docs/agent/ar/writing-style.md) | How an Arabic sentence is written. Its §13 carries the rules that apply to English only. |
| [`docs/agent/en/writing-style.md`](docs/agent/en/writing-style.md) | How an English sentence is written. Its §9 carries the rules that apply to Arabic only. |
| [`docs/agent/ar/writing-guides.md`](docs/agent/ar/writing-guides.md) و[`docs/agent/en/writing-guides.md`](docs/agent/en/writing-guides.md) | What a page must contain and how it is arranged: the rule in the first line, `status` in the frontmatter, no information written twice, and what verifies each rule. |

Editing one language means editing the other. A rule that differs between the
two versions is an error, not a translation choice.

## Generated files — never edit by hand

`standards/terminology/` is the source; `content/` explains it. `python3
tools/build.py` rewrites all of these, so an edit made here is lost on the next
build:

- `content/{ar,en}/reference/dictionary.md` and `registries.md`
- `content/glossary.json` — from the concept entries, by `tools/generate_glossary.py`
- `content/{ar,en}/naming.md`, `quranic-text.md`, `versioning.md`,
  `engineering.md`, `repositories.md` — from `content/pages/*.yml`
- `skills/quranic-terminology/` — written whole on every build
- `standards/terminology/aliases.json` and `registry_aliases.json`
- `standards/terminology/registries/ayah_counts.tsv` and `tajwid_rules.tsv`
- the dabt mark entries in `standards/terminology/concepts/` — generated from
  `standards/terminology/data/dabt_marks.tsv`; change the TSV or
  `tools/generate_dabt.py`, not the YAML

## Before you finish

```bash
python3 tools/build.py
python3 -m pytest -q
```

Both must pass. `tools/build.py` also checks the prose: every name in a page has
to resolve to a dictionary entry, and every "section N" reference has to exist.
