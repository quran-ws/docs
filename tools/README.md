# Tools

Every name in the dictionary is derived or measured, with two named exceptions
(below). Nothing here is chosen by hand.

## Prerequisites

- Python 3.8 or later, with the packages the tools import:

  ```bash
  python3 -m pip install -r requirements.txt   # PyYAML, jsonschema, pytest
  ```

- Nothing else for the build. `measure_display.py` alone needs the GitHub CLI
  (`gh`, authenticated), and rebuilding `registries/ayah_counts.tsv` without
  `--check` fetches al-Bayan once from turath.io into `tools/turath_cache/`.

## The build

```bash
python3 tools/build.py                # all of it, in order; the only entry point
python3 tools/build.py --keep-going   # run every step, report at the end
python3 -m pytest -q                  # the tests in tests/
```

`build.py` runs the steps below in the order they depend on each other, and
stops at the first failure. A step whose script is not written yet is skipped
with a note. CI runs the build, then the tests, then `git diff --exit-code`:
a generated file that the build changes is a file that was hand-edited, or a
source that was changed without regenerating.

| step | what it does |
| --- | --- |
| `test_translit.py` | The golden cases for the derivation. If a spelling rule changes, this says which names change with it |
| `generate_dabt.py` | Generates the mark entries from `data/dabt_marks.tsv`, with their Unicode properties |
| `build_aliases.py` | Builds `aliases.json`, so every attested spelling resolves to one concept |
| `generate_tajwid_registry.py` | Generates `registries/tajwid_rules.tsv` from the tajweed-engine corpus |
| `build_registry_aliases.py` | Builds `registry_aliases.json`, the member index, namespaced by kind |
| `extract_ayah_counts.py --check` | The per-surah counts of the 6 numbering systems still reconcile with al-Dani's totals |
| `validate.py` | Every concept file matches `schema.json` |
| `check_issue_templates.py` | The term issue form offers the values `schema.json` allows |
| `check_conformance.py` | Every entry obeys the rules the standard states in prose, which the schema cannot express |
| `check_registries.py` | Every member of every closed set holds up: derived codes derive, references resolve, every row cites a source |
| `generate_dictionary.py` | Renders the dictionary pages, Arabic and English, from the concept files |
| `generate_registries.py` | Renders the registry pages, Arabic and English, from the registries |
| `generate_glossary.py` | Writes `content/glossary.json`, the short glossary quran.ws renders, from the concept entries named in its `TERMS` list; `--check` reports staleness |
| `generate_pages.py` | Renders the guideline pages from `content/pages/*.yml`: English always, Arabic once fully translated; `--check` and `--stamp` track the translation |
| `check_examples.py` | Every name in the prose resolves, every counter-example still doesn't, every section reference exists, every YAML example is a true excerpt |
| `check_example_files.py` | The files under `examples/` still say what the prose that cites them says |
| `generate_skill.py` | Builds `skills/quranic-terminology/`: the standard, the dictionary and the scripts an agent audits a codebase with |

Tools the build does not run:

| tool | what it does |
| --- | --- |
| `translit.py` | Canonical Code Spelling: vocalised Arabic → ASCII identifier, per §4–§8. `python3 tools/translit.py "رُبْع الحِزْب"`, `--json`, `--help` |
| `unicode_props.py` | Unicode properties for a mark, read from the Unicode database |
| `measure_display.py` | Measures which English spelling is dominant, so `display` is evidence, not taste |
| `extract_ayah_counts.py` | Without `--check`: rereads al-Bayan and rewrites `registries/ayah_counts.tsv` |
| `audit_text.py` | Audits a Quranic text file against the invariants of the text page |
| `registry.py` | The one reader for the tab-separated registries and data tables; imported, not run |

## The skill

`generate_skill.py` writes `skills/quranic-terminology/`, which is generated in
full on every build and never edited by hand. It carries the English standard,
the dictionary, the decision record, the registries, and 4 scripts: one that
resolves any spelling to its concept (`lookup.py`), one that audits a codebase
against the standard and exits non-zero for CI (`audit_terminology.py`), one
that derives a code spelling from vocalised Arabic (`spell.py`, a copy of
`translit.py`), and one that says whether the copy has fallen behind this
repository (`update_check.py`).

The skill is stamped with a snapshot: a hash of everything it was built from.
Two builds of the same source give the same stamp on any machine, and
`update_check.py` compares it with the snapshot published in this repository.
`generate_skill.py --release` adds the commit as a label for people; the
comparison never reads it.

To use the skill, copy `skills/quranic-terminology/` into the skills directory
of your agent, or point the agent at it; the repository README says how for
each host.

## Why `code` and `display` differ

`code` is derived and never negotiated: `small_noon`, `waqf_lazim`, `tajwid`.
`display` is whatever English writing actually uses, measured: `Noon Saghirah`,
`Waqf Lazim`, `Tajweed`. Both are recorded, the evidence for the second is
recorded with it, and `aliases.json` resolves either to the same concept.

The derivation has two exceptions, each a table with a reason on every row:

- **Letter names** are written as they are said, so `noon` and `meem` rather
  than `nun` and `mim` — `standards/terminology/data/letter_names.tsv`.
- **Established spellings** — `juz`, not `juzu` — where a measurement shows one
  form dominates: `standards/terminology/data/established_spellings.tsv`.

People are treated like letter names, for the same reason: a name carries no
meaning for the derivation to keep, so `hafs` and `qalun` are written the way
they are written. Surah names are words, not people, so they are derived and
re-derived on every run. See `standards/terminology/registries/`.

Two smaller tables serve the derivation inside a compound name:
`general_words.tsv` (the ordinary word beside a Quranic one is translated —
`small_meem`) and `connectives.tsv` (a word that only joins the parts is
dropped — `waqf_jaiz_wasl_awla`).

Naming needs four different things: a stable identifier in code, a clear label
for the reader, an accurate way to write the pronunciation, and a value suited
to search. One string cannot do all four, so each has its own field.
