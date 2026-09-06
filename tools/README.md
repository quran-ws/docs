# tools

Every name in the dictionary is derived or measured. Nothing here is chosen by hand.

| tool | what it does |
| --- | --- |
| `translit.py` | Canonical Code Spelling: vocalized Arabic → ASCII identifier, per sections 4–8 |
| `test_translit.py` | 91 golden cases. If a spelling rule changes, this says which names change with it |
| `measure_display.py` | Measures which English spelling is dominant, so `display` is evidence, not taste |
| `unicode_props.py` | Unicode properties for a mark, read from the Unicode database |
| `generate_dabt.py` | Generates the 35 mark entries from the registry TSV |
| `build_aliases.py` | Builds `aliases.json`, so every attested spelling resolves to one concept |
| `validate.py` | Validates every concept file against `schema.json` |
| `check_examples.py` | Checks that every name used in the prose still resolves, and that counter-examples are still wrong |
| `check_conformance.py` | Checks the entries against the rules the standard states in prose, which `schema.json` cannot express |
| `check_registries.py` | Checks the registries: derived codes still derive, references resolve, every row cites a source |
| `build_registry_aliases.py` | Builds `registry_aliases.json`, the member index, namespaced by kind |
| `extract_ayah_counts.py` | Reads the per-surah counts of the six numbering schools out of al-Bayan, and proves the reading by reconciling it |
| `generate_dictionary.py` | Renders the dictionary page from the concept files |

```bash
python3 tools/test_translit.py     # spelling rules still hold
python3 tools/generate_dabt.py     # regenerate mark entries
python3 tools/build_aliases.py     # rebuild the alias index
python3 tools/validate.py          # every entry conforms
python3 tools/check_examples.py    # no stale name in the prose
python3 tools/check_conformance.py # every entry obeys the standard, not just the schema
python3 tools/check_registries.py  # every member of every closed set holds up
python3 tools/build_registry_aliases.py
python3 tools/extract_ayah_counts.py --check  # the counts still reconcile
python3 tools/generate_dictionary.py
```

## Why `code` and `display` differ

`code` is derived and never negotiated: `small_noon`, `waqf_lazim`, `tajwid`.
`display` is whatever English writing actually uses, measured: `Noon Saghirah`,
`Waqf Lazim`, `Tajweed`. Both are recorded, the evidence for the second is
recorded with it, and `aliases.json` resolves either to the same concept.

Letter names are the exception to derivation: they are written as they are
said, so `noon` and `meem` rather than `nun` and `mim`. See
`standards/terminology/data/letter_names.tsv`.

People are the other exception, for the same reason: a name carries no meaning
for the derivation to keep, so `hafs` and `qalun` are written the way they are
written. Surah names are words, not people, so they are derived and re-derived
on every run. See `standards/terminology/registries/`.

This exists because one string cannot be a stable identifier, a familiar label,
a faithful rendering of the sound, and a search target at once. Four fields can.
