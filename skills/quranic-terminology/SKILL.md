---
name: quranic-terminology
description: Name and audit the concepts of Quranic software by the Quran.ws Terminology Standard. Use whenever code, an API, a schema, a dataset or docs touch the Quran — ayah, surah, mushaf, juz, qiraah, riwayah, tajwid, waqf, tafsir, recitation — to pick the canonical name, resolve a spelling (aya, sura, tajweed, verse, chapter), audit a codebase, or draft a new term.
allowed-tools: Bash(python3 *), Read
---

# Quranic Software Terminology

One concept, one canonical name. The name is **derived** from the vocalised
Arabic by a documented function, never chosen by taste, and every attested
spelling of it resolves to the same entry.

This skill carries the standard, its dictionary of 200 concepts and
846 spellings, the registries of the closed sets, and scripts that
answer a naming question without guessing.

> Status: 0 entries adopted, 200 still draft. A draft entry is a
> proposal, not a ruling. Say so once, at the top of any report that relies on
> the dictionary — not on every finding.
>
> Snapshot `8decd2776f109cc4` of `quran-ws/guidelines`. The dictionary keeps moving, so before an
> audit that someone will act on, check the snapshot is still current:
>
> ```bash
> python3 scripts/update_check.py   # 0 current, 1 behind, 2 offline, 3 not reachable at all
> ```
>
> Only `behind` is about the skill. Offline or blocked, say which snapshot you
> used and carry on.

## Install

- **As a plugin** (updates with the repository): in Claude Code run
  `/plugin marketplace add quran-ws/guidelines`, then
  `/plugin install quranic-terminology@quran-ws`. Refresh later with
  `/plugin update quranic-terminology`.
- **As a plain skill** (a copy): put this directory at `~/.claude/skills/quranic-terminology/`
  for every project, or `<project>/.claude/skills/quranic-terminology/` for one.
  A copy does not update itself: when `update_check.py` says behind, replace
  the directory with the published `skills/quranic-terminology/`, or ask the
  maintainer for a rebuilt one.

The scripts need Python 3 and nothing else; run them from any directory.

## Resolve before you answer

Never invent a name, and never assume a name in the code is wrong because it
looks unfamiliar. Resolve it first:

```bash
python3 scripts/lookup.py aya verse "Waqf Lazim" ayat "juz'" مصحف
python3 scripts/lookup.py --search waqf
python3 scripts/lookup.py --category qiraat
python3 scripts/lookup.py --registry surahs --member fatihah
```

Any spelling resolves — an alias, a gloss, a plural, a deprecated name, or the
Arabic with or without its vowel marks — and each answer says which of those it
matched. When nothing resolves, the nearest entries are listed: read them
before concluding the term is new. `--json` works in every mode.

`lookup.py` reads `data/terminology.json`, which holds every entry with its
`code`, `display`, vocalised Arabic name, English definition, purpose,
boundaries, spellings, glosses and deprecated names. Read that file directly
when you need many entries at once.

Categories: `ayah_numbering`, `core`, `dabt`, `divisions`, `linguistics`, `mushaf`, `qiraat`, `quranic_sciences`, `recitation`, `recitation_pace`, `recitation_style`, `revelation`, `structure`, `surah_classification`, `tafsir`, `tajwid`, `text`, `translation`, `waqf`.
Registries (closed sets, one row per member): `ayah_counts`, `ayah_numbering`, `qiraat`, `sajdah`, `surahs`, `tajwid_rules`, `tariq`.

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
   no doubled vowels — `tajwid`, `tafsir`, `nuzul`, `qiraah`.
6. **Ta marbutah is `h`** at the end of a word (`surah`) and **`t` in a
   construct** (`hamzat_al_wasl`). **A letter's name is written as it is
   said**: `noon`, `meem`, `seen`, `yaa`.
7. **`code` and `display` are different fields and may disagree.** `code` is
   derived (`tajwid`, `small_noon`); `display` is the established English form,
   measured rather than chosen (`Tajweed`, `Noon Saghirah`). Identifiers take
   `code`; user interfaces and reader-facing labels take `display`; technical
   prose may write the code spelling as a common noun (ayah, tajwid), as these
   guidelines do.
8. **Plurals are the code plus `s`**: `ayahs`, `surahs`, `juzs` — never `ayat`,
   never `suwar`, never the plural of a gloss.
9. **A gloss is not a name.** `verse` and `chapter` are search keys recorded in
   `english_glosses`; the names are `ayah` and `surah`.
10. **Names are snake_case in code**, clear and unabbreviated: no `srh`, `ay`,
    `wrd`, no `data`, `info`, `item`, `value` where a real name exists.
11. **Deprecated is not incorrect.** A deprecated name names a different concept
    or an abandoned one; it keeps resolving so old data is not stranded, and it
    is not written in new code. `waqf_jaiz` is the example: it now resolves to
    `waqf_jaiz_mustawi_al_tarafayn`, the one value it used to mean.

`references/standard.md` is the full standard, numbered section by section
with a table of contents at the top; the scripts cite those numbers. Read the
section before ruling on anything these 11 rules do not settle. When a
finding is contested — `tajwid` against `tajweed`, `ayah` against `verse`, why
`page` is English and `juz` is not — `references/decisions.md` holds the
evidence behind the decision; read it before arguing the point.

## Audit an existing codebase

```bash
python3 scripts/audit_terminology.py PATH [PATH ...]      # grouped by concept
python3 scripts/audit_terminology.py src --by file        # or --by rule
python3 scripts/audit_terminology.py src --json           # findings, mixed spellings, summary
python3 scripts/audit_terminology.py src --strict         # exit 1 on errors, for CI
```

Each finding carries the file and line, the identifier, the form it matched,
the canonical name and display form, and the **layer** of the file: a
compatibility surface (migrations, schemas, wire formats), UI, prose, or
internal code. camelCase and PascalCase are split, so `getVerseById` and
`AyahNumber` are read as words.

| rule | severity | what it found |
| --- | --- | --- |
| `deprecated` | error | a name the standard retired, which names another concept |
| `spelling` | error | a recorded spelling that is not the canonical one (`aya`, `sura`, `koran`, `waqf-lazim`) |
| `arabic_plural` | error | an Arabic plural used as a name (`ayat`) |
| `display_in_code` | warning | the display form used as an identifier (`tajweed` in code) |
| `gloss` | warning | an English gloss standing in for a Quranic term (`verse`, `chapter`) |
| `generic` | warning | an ordinary word that is also a recorded spelling (`segment`); a finding only if it is about that concept |

Prose (`.md`, `.txt`) is checked for wrong spellings and deprecated names
only: it may carry the display form or the code spelling, and may quote a gloss. The report
ends with every concept the tree writes more than one way — the consistency
rule, one name across every layer from the column to the JSON field to the UI
string — and a count per layer.

**Judge the findings; do not apply them blindly.**

- A word can be innocent: `verse` in a poetry module, `page` in a paginator,
  `segment` in an audio player. Check what the identifier is about.
- A database column, a public API field, a dataset header is a compatibility
  surface. Propose the rename with a migration and an alias, or record it and
  leave it. Renaming it is a project decision, not a lint fix.
- A warning in a UI string or prose is often right as it stands: `display`
  belongs there.

Tell the audit what the project already knows, so the next run is clean and
`--strict` can go into CI: copy `assets/terminology.example.json` to
`.terminology.json` at the project root. `exclude` skips trees about something
else; `ignore_words` retires words that mean something else here;
`allow_gloss_in` permits glosses on a published API or in UI strings;
`compatibility` lists the surfaces whose findings are reported once as known
and do not fail the build. A single line is excused with a comment containing
`terminology: ignore`. Each entry in that file is a decision: say why in the
commit.

A useful report, in order:

1. one line naming the snapshot and that the entries are draft;
2. the errors that are cheap and internal, with the rename for each;
3. the errors on a compatibility surface, with what the migration costs;
4. the warnings worth taking;
5. what you deliberately left alone, and why.

## Enforce it going forward

- Commit `.terminology.json` and run `audit_terminology.py --strict` in CI over
  the directories that model Quranic data.
- Resolve every new name through `lookup.py` before it is written.
- Run `scripts/update_check.py` when you pick the skill up again; when it says
  behind, update the plugin or replace the copy before ruling on a name.
- Never edit `data/terminology.json`: it is generated from the guidelines
  repository, and a name that lives only in one codebase is the problem the
  standard exists to fix.

## Name a concept that has no entry

1. Search first — `lookup.py --search` over the Arabic and the English. Most
   "new" terms are spellings of an entry that exists.
2. If it is genuinely new, apply the acceptance rule in §30 of
   `references/standard.md`: it must be a concept that cannot be defined
   without the Quran or the mushaf; then state its boundaries, what it
   excludes, why software must model it, and the source that establishes it.
3. Let the script do the derivation, the collision check and the draft:

   ```bash
   python3 scripts/propose.py "رُبْع الحِزْب" --kind entity --category divisions
   python3 scripts/propose.py "خَتْمَة" --display Khatmah --out khatmah.yml
   ```

   The Arabic must be **vocalised**; unvocalised input is refused, because the
   short vowels are what the spelling is derived from. If the name already
   resolves, the script stops and says which entry to extend instead.
4. The draft is `assets/proposal-template.yml` filled in, with every field
   explained, and `assets/proposal-issue.md` is the checklist to answer beside
   it. The Arabic `definition` and `purpose` are the source of the entry: leave
   them `TODO` for a maintainer rather than machine-translating them. A
   definition says what the thing is without implementation detail or
   circularity; a purpose says why software models it, never restating the
   definition.
5. Send it upstream to <https://github.com/quran-ws/guidelines>. A proposal is
   `draft`; nothing is `adopted` without a source.

## Adab

The text itself is not a naming question. Do not paste, alter, normalise or
truncate Quranic text to make an example; name the concept and reference the
ayah instead. A disputed classification — a numbering system, a Makki/Madani
call, an abrogation — is recorded with its source, never flattened into one
value the code presents as settled.

## What is in this skill

| path | what it holds |
| --- | --- |
| `references/standard.md` | the full terminology standard, numbered sections, table of contents first |
| `references/dictionary.md` | the 200 entries as prose, with a lookup table; `lookup.py` is faster |
| `references/decisions.md` | the contested decisions, with the evidence behind each |
| `references/registries.md` | the closed sets as prose: every surah, qiraah, numbering system and sajdah place, with sources |
| `data/terminology.json` | every entry, every spelling, every registry member |
| `data/registries/*.tsv` | the closed sets: the surahs, the qiraat, the numbering systems, the sajdah places |
| `data/schema.json` | the schema an entry must satisfy |
| `assets/terminology.example.json` | the project configuration for the audit, every key explained |
| `assets/proposal-template.yml`, `assets/proposal-issue.md` | the draft entry and the checklist a proposal answers |
| `scripts/lookup.py` | resolve a term in any spelling or in Arabic; search; list a category or a registry |
| `scripts/audit_terminology.py` | audit a codebase, grouped by concept, file or rule; JSON; strict for CI |
| `scripts/spell.py` | derive the canonical code spelling from vocalised Arabic |
| `scripts/propose.py` | draft an entry for a new concept: derive, check for collisions, fill the template |
| `scripts/update_check.py` | ask whether this snapshot of the standard is still the published one |
