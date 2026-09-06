---
name: quranic-terminology
description: Name and audit the concepts of Quranic software by the Quran.ws Terminology Standard. Use when writing or reviewing code, APIs, schemas, datasets or docs that touch the Quran — ayah, surah, mushaf, qiraah, riwayah, tajwid, waqf, tafsir, recitation, mushaf marks — to pick a canonical name, resolve an unfamiliar spelling (aya, sura, tajweed, verse, chapter), define a new term, or audit an existing codebase for names that do not follow the standard.
---

# Quranic Software Terminology

One concept, one canonical name. The name is **derived** from the vocalized
Arabic by a documented function, never chosen by taste, and every attested
spelling of it resolves to the same entry.

This skill carries the standard, its dictionary of 146 concepts and
377 spellings, the registries of the closed sets, and scripts that
answer a naming question without guessing.

> Status: 0 entries adopted, 146 still draft. A draft entry is a
> proposal, not a ruling — say so when you rely on one.
>
> Built from `quran-ws/guidelines`@`153261cf79a2`. The dictionary keeps moving, so before an
> audit that someone will act on, check the snapshot is still current:
>
> ```bash
> python3 scripts/update_check.py      # 0 current, 1 behind, 2 could not tell
> ```
>
> Being offline is not a finding: say which snapshot you used and carry on.

## Resolve before you answer

Never invent a name, and never assume a name in the code is wrong because it
looks unfamiliar. Resolve it first:

```bash
python3 scripts/lookup.py aya verse "Waqf Lazim"
python3 scripts/lookup.py --search waqf
python3 scripts/lookup.py --category qiraat
python3 scripts/lookup.py --registry surahs --member fatihah
```

`lookup.py` reads `data/terminology.json`, which holds every entry with its
`code`, `display`, Arabic, definition, purpose, boundaries, spellings, glosses
and deprecated names. Read that file directly when you need many entries at once.

Categories: `ayah_numbering`, `core`, `dabt`, `divisions`, `linguistics`, `mushaf`, `mushaf_marks`, `qiraat`, `quranic_sciences`, `recitation`, `recitation_pace`, `recitation_style`, `revelation`, `structure`, `surah_classification`, `tafsir`, `tajwid`, `text`, `translation`, `waqf`.
Registries (closed sets, one row per member): `ayah_counts`, `ayah_numbering`, `qiraat`, `sajdah`, `surahs`.

## The rules you apply most

1. **Concept before name.** Settle what is being modelled — its boundaries, what
   it excludes, why software stores it — then name it.
2. **One canonical name per concept**, used across code, APIs, databases,
   datasets and docs. Other spellings are recorded, not used.
3. **Keep the Arabic term** when it carries a Quranic or scholarly concept:
   `surah`, `ayah`, `mushaf`, `juz`, `qiraah`, `riwayah`, `tajwid`, `tafsir`.
   Use plain English for general concepts: `word`, `letter`, `page`, `line`,
   `root`, `translation`, `glyph`.
4. **Inside a compound, the technical word is transliterated and the ordinary
   word is translated**: `small_meem`, not `meem_saghirah`; `rounded_zero`, not
   `sifr_mustadir`; but `waqf_lazim` and `noon_sakinah` stay, because `lazim`
   and `sakinah` are technical.
5. **The code spelling is ASCII and derived**: no `ā ī ū ʿ ʾ`, no apostrophes,
   no doubled vowels — `tajwid`, `tafsir`, `nuzul`, `qiraah`. A final ta marbutah
   is `h` (`surah`), and `t` in a construct (`hamzat_al_wasl`). A letter's name
   is written as it is said: `noon`, `meem`, `seen`, `yaa`.
6. **`code` and `display` are different fields and may disagree.** `code` is
   derived (`tajwid`, `small_noon`); `display` is the established English form,
   measured rather than chosen (`Tajweed`, `Noon Saghirah`). Identifiers take
   `code`; prose and UI take `display`.
7. **Plurals are the code plus `s`**: `ayahs`, `surahs`, `juzs` — never `ayat`,
   never `suwar`, never the plural of a gloss.
8. **A gloss is not a name.** `verse` and `chapter` are search keys recorded in
   `english_glosses`; the names are `ayah` and `surah`.
9. **Names are snake_case in code**, clear and unabbreviated: no `srh`, `ay`,
   `wrd`, no `data`, `info`, `item`, `value` where a real name exists.
10. **Deprecated is not incorrect.** A deprecated name names a different concept
    or an abandoned one; it keeps resolving so old data is not stranded, and it
    is not written in new code.

`references/standard.md` is the full standard, section by section, with the
worked examples. Read it before ruling on anything these ten lines do not settle.

## Audit an existing codebase

```bash
python3 scripts/audit_terminology.py PATH [PATH ...]      # a report
python3 scripts/audit_terminology.py src --json           # findings as data
python3 scripts/audit_terminology.py src --strict         # exit 1 on errors, for CI
```

What it reports, each finding with file, line, the identifier and the canonical
name:

| rule | severity | what it found |
| --- | --- | --- |
| `deprecated` | error | a name the standard retired, which names another concept |
| `spelling` | error | a recorded spelling that is not the canonical one (`aya`, `sura`, `waqf-lazim`) |
| `arabic_plural` | error | an Arabic plural used as a name (`ayat`) |
| `display_in_code` | warning | the display form used as an identifier (`tajweed` in code) |
| `gloss` | warning | an English gloss standing in for a Quranic term (`verse`, `chapter`) |

It also lists any concept the tree writes more than one way, which is the
consistency rule: one name across every layer, from the database column to the
JSON field to the UI string.

**Judge the findings; do not apply them blindly.**

- A warning in prose, a UI string, or a public API you cannot break is often
  right as it stands. `display` belongs in prose and UI.
- A public API field or a database column is a compatibility surface. Propose
  the rename with a migration and an alias, or record it and leave it.
- A word can be innocent: `verse` in a music library, `page` in a paginator.
  Check what the identifier is about before reporting it.

A useful report, in order: the errors that are cheap to fix and internal; the
errors that need a migration, with what the migration costs; the warnings worth
taking; and what you deliberately left alone, with the reason.

## Enforce it going forward

- Add `audit_terminology.py --strict` to CI over the directories that model
  Quranic data.
- Resolve every new name through `lookup.py` before it is written.
- Run `scripts/update_check.py` when you pick the skill up again. When it says
  behind, refresh before ruling on a name: clone `quran-ws/guidelines`, run
  `python3 tools/generate_skill.py`, and copy `skills/quranic-terminology/`
  over this directory.
- Keep `data/terminology.json` current by regenerating the skill from the
  guidelines repository; do not edit the data by hand.

## Name a concept that has no entry

1. Search first — `lookup.py --search` over the Arabic and the English. Most
   "new" terms are spellings of an entry that exists.
2. If it is genuinely new, apply the acceptance rule in
   `references/standard.md`: state the concept, its boundaries, what it excludes,
   why software must model it, and the source establishing its definition.
3. Derive the spelling rather than choosing it. The derivation runs on the
   **vocalized** Arabic:

   ```bash
   python3 scripts/spell.py "سُورَة" "رُبْع الحِزْب"
   ```

4. Write the entry in the shape the standard gives (`data/schema.json` is the
   schema): `concept`, `names.code`, `names.display`, `names.arabic.vocalized`,
   `kind`, `category`, `origin`, `tier`, `status`, `definition`, `purpose`, and
   `definition_en` / `purpose_en` beside them. A definition says what it is
   without implementation detail and without circularity; a purpose says why we
   model it, never restating the definition.
5. Propose it upstream at <https://github.com/quran-ws/guidelines>. An entry
   with no source is not `adopted`.

Do not add a name to `data/terminology.json` yourself: it is generated, and a
name that lives only in one codebase is the problem the standard exists to fix.

## Adab

The text itself is not a naming question. Do not paste, alter, normalise or
truncate Quranic text to make an example; name the concept and reference the
ayah instead. A disputed classification — a numbering school, a Makki/Madani
call, an abrogation — is recorded with its source, never flattened into one
value the code presents as settled.

## What is in this skill

| path | what it holds |
| --- | --- |
| `references/standard.md` | the full Terminology Standard |
| `references/dictionary.md` | the 146 entries, generated from the same source |
| `references/decisions.md` | the contested decisions, with the evidence behind each |
| `data/terminology.json` | every entry, every spelling, every registry member |
| `data/registries/*.tsv` | the closed sets: the surahs, the qiraat, the numbering schools, the sajdah places |
| `data/schema.json` | the schema an entry must satisfy |
| `scripts/lookup.py` | resolve a term, search, list a category or a registry |
| `scripts/audit_terminology.py` | audit a codebase, as a report or as JSON, strict for CI |
| `scripts/spell.py` | derive the canonical code spelling from vocalized Arabic |
| `scripts/update_check.py` | ask GitHub whether this snapshot of the standard is still current |
