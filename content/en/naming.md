---
title: Naming
description: One concept, one name, derived from the Arabic. The rules a developer applies when naming a table, a field, a route or a package that holds a Quranic concept.
status: proposed
generated: content/pages/naming.yml
sidebar:
  order: 1
---

**The governing rule:** every Quranic concept has one canonical name, and that
name is the same in the model, the table, the foreign key and the API. The name
is looked up in the [dictionary](/guidelines/en/reference/dictionary/), never
invented at the keyboard.

This page is what a developer needs. The full
[terminology standard](/guidelines/en/reference/standard/) says how a name is
derived from its vocalised Arabic and how a dictionary entry is written; you
need it only when adding a concept to the dictionary.

## 1. One name per concept

Settle the concept, then look up its name.

**1.1** Decide what the concept is and what it excludes before you name it.

```text
Not:  How do we translate this word?
But:  What are we modelling, and how does it differ from its neighbours?
```

*Checked by:* The dictionary's `definition` and `boundaries` fields, which every entry must carry (`tools/validate.py`).

**1.2** Every concept has one canonical `code` name, and a name belongs to one concept.

```text
surah   ayah   word   mushaf   tajwid
```

One name means one spelling across sibling repositories as well; a bundle that writes `hafs-kfgqpc` in its manifest and `hafs-kfqc` in its pages, or a catalogue that spells `qalon`, `douri` and `sousi` where the text dataset spells `qalun`, `duri` and `susi`, needs a mapping table in every consumer.

*Checked by:* `tools/build_aliases.py` fails the build when two entries claim one name, in any of their spellings.

**1.3** Resolve a name in the dictionary before you write it, because most "new" names are a spelling of an entry that exists.

```bash
python3 skills/quranic-terminology/scripts/lookup.py aya verse "Waqf Lazim" مصحف
python3 skills/quranic-terminology/scripts/lookup.py --search waqf
```

*Checked by:* `audit_terminology.py --strict` reports a spelling that is not the canonical one, with the entry it resolves to.

**1.4** A concept the dictionary lacks is proposed there before the code that needs it is merged, not after.

A project may keep concepts of its own, in a concepts directory beside the standard's, when the concept cannot be defined by the Quran or the mushaf (standard, section 30).

*Checked by:* The term issue form, and the audit's `--strict` mode, which flags a Quranic name the dictionary does not know.

## 2. Arabic or English

A Quranic or scholarly concept keeps its Arabic name; a general concept takes its English one.

**2.1** Keep the Arabic term when it carries a Quranic or scholarly concept, and use plain English for a general concept.

```text
Arabic:   surah  ayah  mushaf  juz  hizb  qiraah  riwayah  tajwid  tafsir
English:  word  letter  page  line  root  translation  glyph

surah → ayah → word       not  chapter → verse → word
                          not  surah → ayah → kalimah
```

*Checked by:* `audit_terminology.py` reports an English gloss (`verse`, `chapter`) standing in for a Quranic name, and points to the entry.

**2.2** In a compound name the technical word is transliterated and the ordinary word is translated, in English word order.

```text
المِيم الصَّغِيرَة      → small_meem        not meem_saghirah
عَلَامَة الوَقْف        → waqf_mark
نَوْع عَلَامَة الوَقْف   → waqf_mark_type
النُّون السَّاكِنَة     → noon_sakinah      sakinah is a term of tajwid, so it stays
```

*Checked by:* `tools/check_conformance.py`, which derives every compound from its vocalised Arabic and the list of ordinary words in `general_words.tsv`.

**2.3** The code spelling of an Arabic term is derived from its vocalised Arabic by one function, never chosen by taste.

```bash
python3 tools/translit.py "رُبْع الحِزْب"     # rub_al_hizb
```

The derivation rules are sections 4 to 8 of the standard. You do not need them to use a name, only to add one.

*Checked by:* `tools/test_translit.py` holds the golden cases, and `tools/check_conformance.py` checks that every entry's `code` is its own derivation.

## 3. Code name and display name

The identifier and the label are two fields, and they may differ.

**3.1** `code` is the identifier in code, APIs and databases; `display` is what a reader sees; the two may differ, and that is intended.

```text
code:     tajwid          qiraah
display:  Tajweed         Qiraah
```

*Checked by:* `tools/measure_display.py` measures the dominant English spelling, and the result is recorded in the entry's `display_evidence` before it is adopted.

**3.2** In prose, write a concept the way its `code` is spelt, lowercase, and keep `display` for interfaces.

```text
Yes:  The mushaf carries tajwid colouring on every ayah.
No:   The Mushaf carries Tajweed colouring on every Ayah.
```

The rule is for the prose of a repository, its `README`, its guides and these pages. A user interface, a documentation site included, is a display surface and may write the `display` form under rule 5.4; it takes that form from the entry, never from a second list of its own.

*Checked by:* `tools/check_examples.py`, which resolves every name written in the pages of this repository.

**3.3** An alternative spelling, an English gloss and a deprecated name are three fields, and none of them competes with the canonical name.

```text
ayah:   alternative_spellings: aya, ayat     english_glosses: Verse
```

*Checked by:* `tools/check_conformance.py` refuses a gloss that is also recorded as a spelling; `lookup.py` says which kind of name an input matched.

**3.4** A deprecated name is not wrong, it is superseded; it keeps resolving to its entry so old code can be audited.

*Checked by:* `lookup.py` resolves a deprecated name and says so; `audit_terminology.py` reports it with the name that replaced it.

## 4. The shape of a name

Complete, unabbreviated, and precise.

**4.1** Use the complete name, never an abbreviation, and never a vague word where a precise name exists.

```text
Yes:  surah  ayah  word  translation
No:   srh  ay  wrd  trans  data  info  item  value
```

*Checked by:* `audit_terminology.py --strict` reports abbreviations and vague names.

**4.2** The plural in code is the whole code name plus `s`, and an Arabic plural is never a collection name.

```text
Yes:  ayahs  surahs  juzs  hizbs  riwayahs
No:   ayat  suwar  ajza  ahzab
```

*Checked by:* `tools/check_conformance.py` checks every recorded plural; the audit reports an Arabic plural used as a collection.

**4.3** `id` is the internal key, `number` the number a reader cites, `position` the place in a sequence, and `order` an ordering that meaning decides.

```text
ayah_id   surah_number   word_position   revelation_order
```

A survey found `word_index`, `word_number` and `segment_number` in one table, and whether `word_index` was 0-based could not be recovered from the names.

*Checked by:* The audit, which reports `index` and `idx` as suffixes; the choice between the four is a rule for the writer (standard, section 21).

**4.4** Name a classification by what it classifies, and never by `type`.

```text
waqf_ruling        not waqf_type
recitation_style   not recitation_type
waqf_mark_type     the one exception: the kind of a drawn mark
```

*Checked by:* The audit reports `type` as a suffix on a Quranic concept (standard, section 24).

**4.5** A classification column stores member codes from the registry, never a display string in either language.

```text
Yes:  revelation_classification = "makki" | "madani" | "disputed"
No:   enum('meccan', 'medinan')     surah_type: "مدنية"
```

*Checked by:* A schema check that every classification column's distinct values are a subset of its [registry](/guidelines/en/reference/registries/).

## 5. The same name in every layer

Model, table, foreign key, route and package share one vocabulary.

**5.1** The model, the table, the foreign key and the API path are the same name in four shapes.

```text
Model:        Ayah            Riwayah
Table:        ayahs           riwayahs
Foreign key:  ayah_id         riwayah_id
API:          /ayahs          /riwayahs
```

A survey found one concept named three ways, a truncated spelling in the model, that spelling plus `s` on the table, and the Arabic plural in the route.

*Checked by:* `audit_terminology.py --strict` over the whole tree, on every pull request.

**5.2** A repository or package is named by the dictionary's `code` name in kebab-case, and everything inside it in snake_case.

```text
repository:  qiraat-ayah-map   mushaf-layout   ayah-timing
inside:      ayah_numbering_system   mushaf_edition
```

*Checked by:* The audit, run with the repository name included.

**5.3** A name the project does not own, such as a vendor's column, a font family or a Unicode character name, is quoted exactly as its owner writes it.

*Checked by:* The `external_names` list in `.terminology.json`, which the audit reads past.

**5.4** A user interface may translate or display a name differently; the four layers do not.

*Checked by:* The `allow_gloss_in` list in `.terminology.json`, which admits a gloss in interface strings and nowhere else.

## 6. Running the audit

The audit reports; it never renames.

**6.1** Every repository that holds Quranic concepts runs the terminology audit in CI and blocks a merge on an error.

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

*Checked by:* The CI workflow of the repository, and the exit code of the audit.

**6.2** A project tells the audit what it already knows in `.terminology.json`, and excuses a single line with a comment carrying the words `terminology: ignore`.

```text
paths            what to audit when no path is given
exclude          trees that share a word with the Quran but are about something else
ignore_words     words that mean something else in this project
allow_gloss_in   published API and interface strings
external_names   names quoted from a vendor, a font or Unicode
compatibility    columns and wire formats whose rename is a migration, reported once
```

*Checked by:* `skills/quranic-terminology/assets/terminology.example.json` documents every key, and the audit rejects an unknown one.
