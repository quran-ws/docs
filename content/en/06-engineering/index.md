---
title: Engineering
description: Data modelling, identifiers, APIs, storage, rendering, audio, search and caching for Quranic software, with the test behind each rule.
status: draft
sidebar:
  order: 0
---

**The governing rule:** model the mushaf, not the screen. Every table, API and
file names the concept it holds by its
[dictionary](/guidelines/en/03-terminology/dictionary/) name, carries the identity
of the text it was built from, and can be rebuilt from that text.

This page is a draft. It takes the rules of
[Handling Quranic text](/guidelines/en/02-quranic-text/) and the
[terminology standard](/guidelines/en/03-terminology/standard/) and applies them
to the parts of a system that hold the mushaf: tables, identifiers, APIs, files,
fonts, audio and caches. Where a choice is one defensible option among several,
the page says so. The rules that are not optional are the ones the test table at
the end checks.

The cases cited below come from a
[survey of a production Quran codebase](https://github.com/quran-ws/guidelines/blob/main/surveys/quranpedia-net.md),
written in Laravel. They are typical, not exceptional, which is why they became
rules.

## 1. Data modelling

Every concept in the data model is a dictionary entry, and every closed set of
values is a registry.

- The core chain is
  [`mushaf_edition`](/guidelines/en/03-terminology/dictionary/#mushaf_edition) →
  [`surah`](/guidelines/en/03-terminology/dictionary/#surah) →
  [`ayah`](/guidelines/en/03-terminology/dictionary/#ayah) →
  [`word`](/guidelines/en/03-terminology/dictionary/#word) →
  [`token`](/guidelines/en/03-terminology/dictionary/#token). Each is its own
  table; a token is a product of a declared segmentation, so it never replaces
  the word.
- [`riwayah`](/guidelines/en/03-terminology/dictionary/#riwayah),
  [`ayah_numbering_system`](/guidelines/en/03-terminology/dictionary/#ayah_numbering_system),
  [`page`](/guidelines/en/03-terminology/dictionary/#page) and
  [`line`](/guidelines/en/03-terminology/dictionary/#line) are entities with
  their own tables, not columns on `ayah`. An ayah's number depends on the
  numbering system and its page depends on the edition; a column for either on
  the ayah row bakes one edition into the text.
- The [`basmalah`](/guidelines/en/03-terminology/dictionary/#basmalah) is its own
  field, because whether it counts as an ayah is a property of the numbering
  system (text page, section 5).
- A mushaf, a recording and a dataset are bound to a riwayah, never to a person:
  the column is `riwayah_id`, and `rawi_id` belongs on the riwayah row. The
  surveyed codebase pointed `mushafs.rawi_id` at a table of people whose rows
  held riwayah names, so a query meaning "every recording in Warsh" meant "every
  recording by the man Warsh".
- A classification column stores member codes —
  [`makki`](/guidelines/en/03-terminology/dictionary/#makki),
  [`madani`](/guidelines/en/03-terminology/dictionary/#madani),
  [`disputed`](/guidelines/en/03-terminology/dictionary/#disputed) — never a
  display string. The surveyed schema had
  `enum('revelation_type', ['meccan', 'medinan'])` and a JSON export with
  `surah_type: "مدنية"`: an English gloss as a value, an Arabic label as a
  value, and no room for the disputed surahs.
- A number is stored as a number. The same export carried
  `surah_number: "2"` and `words_count: "6140"` as strings.
- A closed set — the numbering systems, the qiraat, the surahs, the sajdah
  places — is loaded from
  [`standards/terminology/registries/`](https://github.com/quran-ws/guidelines/tree/main/standards/terminology/registries),
  never written by hand as an enum in a migration.

A minimal model, with the canonical column names. Column types are one defensible
choice; the names and the foreign keys are not:

```sql
CREATE TABLE ayah_numbering_systems (
  id    INTEGER PRIMARY KEY,
  code  VARCHAR(64) NOT NULL UNIQUE      -- from registries/ayah_numbering.tsv
);

CREATE TABLE mushaf_editions (
  id                        INTEGER PRIMARY KEY,
  code                      VARCHAR(64) NOT NULL UNIQUE,
  riwayah_id                INTEGER NOT NULL REFERENCES riwayahs(id),
  ayah_numbering_system_id  INTEGER NOT NULL REFERENCES ayah_numbering_systems(id),
  version                   VARCHAR(32) NOT NULL,   -- the data release; see the versioning page
  source_hash               CHAR(64) NOT NULL       -- sha256 of the source file
);

CREATE TABLE ayahs (
  id                        INTEGER PRIMARY KEY,
  mushaf_edition_id         INTEGER NOT NULL REFERENCES mushaf_editions(id),
  surah_number              SMALLINT NOT NULL,
  ayah_number               SMALLINT NOT NULL,
  text                      TEXT NOT NULL COLLATE utf8mb4_bin,
  has_basmalah              BOOLEAN NOT NULL,
  UNIQUE (mushaf_edition_id, surah_number, ayah_number)
);
```

**Check:** every column name resolves to a canonical `code` (the checker used on
`examples/`), and every classification column's values are a subset of its
registry.

## 2. Identifiers and addressing

A location in the text is the triple `(surah_number, ayah_number,
ayah_numbering_system)`; the number alone locates nothing.

- The short form `ayah_key` (`2:255`) is a serialisation of that triple, and is
  only meaningful beside a declared numbering system. Never store or exchange it
  without one.
- A word is addressed by `word_key` (`2:255:3`): the ayah key plus
  `word_position`, under a declared tokenisation (text page, section 4). Change
  the tokenisation and every word key after the first changed word moves, so the
  tokenisation is versioned with the dataset.
- `id` is internal, stable and opaque. It is never the text, never a hash of the
  text, and never reused after deletion.
- The suffixes `id`, `number`, `position` and `order` each have one meaning
  (standard §21). The surveyed schema carried `word_index`,
  `word_number` and `segment_number` in one table, and whether `word_index` was
  0-based could not be recovered from the names.

**Check:** every table that holds Quranic text or refers to a location has an
`ayah_numbering_system_id` — directly or through `mushaf_edition_id` — and a
foreign key to the edition it was built from.

## 3. API design

Resource paths use the canonical name and the code plural, and every parameter
that changes the text is explicit.

- `/surahs/{surah_number}/ayahs/{ayah_number}`, never `/chapters/{n}/verses/{m}`.
  Glosses are search keys, not names (standard §19).
- `riwayah` and `ayah_numbering_system` are parameters with a documented default,
  and the response repeats the value that was applied. A silent default to Hafs and Kufi
  is wrong for every reader outside it, and no reader can see that it was applied.
- The `text` field is returned exactly as stored, beside `source_hash` and the
  dataset `version`. A client can then prove which text it is showing.
- A derived form — `search_key`, or a glyph-coded text — is a separate field,
  never returned in place of `text`.
- Pagination never cuts an ayah; a page of results ends on an ayah boundary
  (text page, section 7).
- An unknown location is a `404` that names the numbering system it was checked
  against, never a nearest guess.

```text
GET /surahs/2/ayahs/255?riwayah=hafs_an_asim&ayah_numbering_system=kufi

{
  "ayah_key": "2:255",
  "surah_number": 2,
  "ayah_number": 255,
  "riwayah": "hafs_an_asim",
  "ayah_numbering_system": "kufi",
  "mushaf_edition": "…",
  "version": "1.2.0",
  "source_hash": "sha256:…",
  "text": "…",
  "search_key": "…"
}
```

**Check:** an OpenAPI lint asserting that every path segment resolves in the
dictionary and that every schema carrying `text` also carries `source_hash` and
`version`.

## 4. Storage and encoding

The database compares Quranic text byte for byte and changes nothing on the way
in or out.

- One encoding end to end: `UTF-8` in the file, the column, the API and the page
  (text page, section 2).
- Text columns use a binary collation. In MySQL that is `utf8mb4_bin`; the
  choice of collation is one among several; what is required is that
  `'مُحَمَّد' = 'محمد'` returns `0`.
- No normalisation anywhere between the file and the reader: not in the driver,
  not in the ORM, not in a serialiser's "clean output" option.
- The character allowlist is enforced at ingestion, and a character outside it
  fails the import.
- A full-text index on `text` with a collation that folds marks is a search on
  the wrong field. Search goes through `search_key` (section 7 below).

**Check:** the collation test from the text page, section 9, and a lint rule
banning `normalize(` in the text path.

## 5. Mushaf rendering and fonts

The rasm, the dabt and the font are three layers, and only the first two are the
text (text page, section 3).

- A page-and-line [`layout`](/guidelines/en/03-terminology/dictionary/#layout) is
  a dataset keyed to a `mushaf_edition`. It says which words fall on which line
  of which page; it never carries text.
- A glyph-coded text — the form of an ayah rewritten as the codepoints of one
  particular [`font`](/guidelines/en/03-terminology/dictionary/#font) — is a
  derived layer that names its font and font version and stores the source hash.
  The dictionary has no entry for it yet; until it does, `coded_text` is the
  name in use.
- Every font release is checked against the character allowlist through its
  `cmap` before it ships.
- Fallback fonts are forbidden for Quranic text. A missing
  [`glyph`](/guidelines/en/03-terminology/dictionary/#glyph) fails the build; it
  is never drawn by another font, because a substituted shape can read as a
  different mark.

```text
layout row:  mushaf_edition = "…"   page_number = 3   line_number = 7
             word_key = "2:6:1" … "2:7:4"
```

**Check:** the font coverage test from the text page, section 9, and a snapshot
test per page of the layout.

## 6. Audio and recitation

A recording is a
[`recitation`](/guidelines/en/03-terminology/dictionary/#recitation) by a
[`reciter`](/guidelines/en/03-terminology/dictionary/#reciter) in a `riwayah`,
with a
[`recitation_style`](/guidelines/en/03-terminology/dictionary/#recitation_style)
and a
[`recitation_pace`](/guidelines/en/03-terminology/dictionary/#recitation_pace).

- A reciter is not a rawi. The performer of a recording is bound to the riwayah
  they recite in, not entered as its transmitter.
- The style of performance is stored as `recitation_style`, and how the audio was
  cut is a property of the files rather than of the recitation. The surveyed
  codebase had a `recitation_types` table holding murattal, mujawwad and muallim
  — `type` is the vague name the standard rules out (standard §24) — and filed
  "by surah" and "by ayah" under `recitation_classification`.
- [`ayah_timing`](/guidelines/en/03-terminology/dictionary/#ayah_timing) and
  `word_timing` are derived layers. Each timing file names the hash of the audio
  it was aligned against, the text release and the numbering system, so a file
  aligned to a different cut of the audio is detectable.
- Streams, radios and playlists are application concepts. The application names
  them; the standard does not (standard §30).

```text
# ayah_timing v1
# recitation:             …
# reciter:                …
# riwayah:                hafs_an_asim
# audio_sha256:           …
# text_version:           1.2.0
# ayah_numbering_system:  kufi
ayah_key   start_ms   end_ms
1:1        0          5320
1:2        5320       9870
```

**Check:** every timing file carries the audio hash and the text release in its
header, and a build step verifies both against the current data.

## 7. Search

The `search_key` is derived from `text` by a versioned, deterministic function,
and the reader never sees it (text page, section 6).

- The derivation strips the dabt and the tatweel, unifies the hamzah forms with
  their alif, yaa or waw seat, unifies alif maqsurah with yaa and taa marbutah
  with haa where the search should not distinguish them, and nothing else. Which forms
  it unifies is a decision for the project to write down; that it is one
  versioned function is not open to choice.
- The function has a version. A change to it is a change to the dataset, and
  the index is rebuilt.
- A result links to a location and to the stored `text`, never to the key.

```text
search_key(text):
  1. remove dabt marks and the tatweel (U+0640)
  2. أ إ آ ٱ → ا     ؤ → و     ئ → ي
  3. ى → ي           ة → ه
  4. collapse whitespace
```

**Check:** golden cases for the derivation — an input and its expected key — in
the pattern of `tools/test_translit.py`, and a test that the current index was
built by the current function version.

## 8. Performance and caching

A cache key names everything that changes the text; a cache of Quranic text is
never invalidated by time alone.

- The key includes the dataset version, the edition, the riwayah and the
  numbering system. Two of those defaulting to the same value today is not a
  reason to omit them.
- A `MAJOR` data release (see [Versioning](/guidelines/en/04-versioning/))
  invalidates every cache of text built on the previous release.
- CDN objects that hold text are immutable, and the version is in the path, not
  in a query string that an intermediary may drop.

```text
cache key:  ayah:{version}:{mushaf_edition}:{ayah_numbering_system}:{ayah_key}
            ayah:1.2.0:…:kufi:2:255

CDN path:   /text/1.2.0/{mushaf_edition}/2/255.json
```

**Check:** a test of the cache key format, and a test that bumping the release
changes every text URL.

## 9. Naming in code

The terminology standard binds the four layers — model, table, foreign key, API
— to one vocabulary (standard §26).

```text
Model:        Ayah            Riwayah
Table:        ayahs           riwayahs
Foreign key:  ayah_id         riwayah_id
API:          /ayahs          /riwayahs
```

- The surveyed codebase named one concept three ways: a truncated spelling in
  the model, that spelling with an `s` on the table, and the Arabic plural
  `/qiraat` in the route. The canonical spelling is `qiraah` and the collection
  is `qiraahs`; an Arabic plural is not a collection name (standard §11).
- A user interface may translate or display a name differently; the four layers
  do not.
- Run the audit in CI:
  `python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict`.
  It reports the deprecated name, the non-canonical spelling, the gloss and the
  Arabic plural, with the section behind each; it renames nothing.

**Check:** the audit script itself, run with `--strict`, on every pull request.

## Every rule becomes a test

A failing test blocks the release. It never rewrites the data.

| What it tests | How |
| --- | --- |
| Schema names are canonical | Every table and column name resolves to a dictionary `code` |
| Classification values are registry members | Each classification column's distinct values ⊆ its registry |
| Numbers are numbers | No numeric fact stored in a string column |
| Riwayah, not rawi | No `rawi_id` on a mushaf, a recording or a dataset |
| Numbering system is explicit | Every text table and every text endpoint carries `ayah_numbering_system` |
| Text responses carry their identity | Every schema with `text` also has `source_hash` and `version` |
| Binary collation | `SELECT 'مُحَمَّد' = 'محمد';` returns `0` |
| No normalisation in the text path | A `lint` rule banning `normalize(` between file and reader |
| Font coverage | `cmap` of each font release covers the allowlist; no fallback font in the text stack |
| Layout matches the text | A snapshot per page, rebuilt from the layout dataset and the text |
| Timing files name their sources | Header carries `audio_sha256` and `text_version`, both verified |
| Search key derivation | Golden input → key cases; index version equals function version |
| Cache key includes the version | Format test; a release bump changes every text URL |
| Names across the four layers | `audit_terminology.py --strict` passes |
