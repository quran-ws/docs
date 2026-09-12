---
title: Engineering
description: Data modelling, identifiers, APIs, storage, rendering, audio, search and caching for Quranic software, with the test behind each rule.
status: proposed
generated: content/pages/engineering.yml
sidebar:
  order: 4
---

**The governing rule:** model the mushaf, not the screen. Every table, API
and file names the concept it holds by its
[dictionary](/guidelines/en/reference/dictionary/) name, carries the identity
of the text it was built from, and can be rebuilt from that text.

This page applies the [text](/guidelines/en/quranic-text/) and
[naming](/guidelines/en/naming/) rules to the parts of a system that hold the
mushaf. Where a choice is one defensible option among several, the rule says
so. The cases cited come from a
[survey of a production Quran codebase](https://github.com/quran-ws/docs/blob/main/surveys/quranpedia-net.md);
they are typical, which is why they became rules.

## 1. Data modelling

Every concept in the model is a dictionary entry, and every closed set of values is a registry.

**1.1** The core chain is `mushaf_edition` → `surah` → `ayah` → `word` → `token`, each its own table; a token is the product of a declared segmentation and never replaces the word.

```sql
CREATE TABLE mushaf_editions (
  id                        INTEGER PRIMARY KEY,
  code                      VARCHAR(64) NOT NULL UNIQUE,
  riwayah_id                INTEGER NOT NULL REFERENCES riwayahs(id),
  ayah_numbering_system_id  INTEGER NOT NULL REFERENCES ayah_numbering_systems(id),
  version                   VARCHAR(32) NOT NULL,   -- the data release
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

Column types are one defensible choice; the names and the foreign keys are not. `examples/schema/` holds the full model.

*Checked by:* Every column name resolves to a canonical `code` (`tools/check_example_files.py` on `examples/`).

**1.2** `riwayah`, `ayah_numbering_system`, `page` and `line` are entities with their own tables, not columns on `ayah`, because an ayah's number depends on the numbering system and its page on the edition.

*Checked by:* A schema check that `ayah` carries no page, line or numbering column of its own.

**1.3** A mushaf, a recording and a dataset are bound to a riwayah, never to a person; the column is `riwayah_id`, and `rawi_id` belongs on the riwayah row.

The surveyed codebase pointed `mushafs.rawi_id` at a table of people, so "every recording in Warsh" meant "every recording by the man Warsh".

*Checked by:* A schema check that no mushaf, recording or dataset table has a `rawi_id`.

**1.4** A number is stored as a number, never as a string.

The surveyed export carried `surah_number: "2"` and `words_count: "6140"`.

*Checked by:* A schema check that no numeric fact sits in a string column.

**1.5** A closed set, such as the numbering systems, the qiraat, the surahs or the sajdah places, is loaded from the [registries](/guidelines/en/reference/registries/), never written by hand as an enum in a migration.

*Checked by:* Each classification column's distinct values are a subset of its registry.

## 2. Identifiers and addressing

A location is the triple of surah number, ayah number and numbering system; the number alone locates nothing.

**2.1** The short form `ayah_key` (`2:255`) is a serialisation of the triple and is only meaningful beside a declared numbering system; never store or exchange it without one.

*Checked by:* Every table and endpoint that carries an `ayah_key` also carries `ayah_numbering_system`, directly or through the edition.

**2.2** A word is addressed by `word_key` (`2:255:3`), the ayah key plus `word_position` under a declared tokenisation, so the tokenisation is versioned with the dataset.

*Checked by:* The token count of each release, held as a golden value.

**2.3** `id` is internal, stable and opaque: never the text, never a hash of the text, and never reused after deletion.

*Checked by:* A schema check that primary keys are integers or opaque strings.

## 3. API design

Resource paths use the canonical name and the code plural, and every parameter that changes the text is explicit.

**3.1** Paths are `/surahs/{surah_number}/ayahs/{ayah_number}`, never `/chapters/{n}/verses/{m}`.

*Checked by:* An OpenAPI lint asserting that every path segment resolves in the dictionary (`examples/api/`).

**3.2** `riwayah` and `ayah_numbering_system` are parameters with a documented default, and the response repeats the value that was applied.

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

A silent default to Hafs and Kufi is wrong for every reader outside it, and no reader can see that it was applied.

*Checked by:* A contract test that every text response carries both fields.

**3.3** The `text` field is returned exactly as stored, beside `source_hash` and the dataset `version`, and a derived form such as `search_key` is a separate field.

*Checked by:* An OpenAPI lint that every schema carrying `text` also carries `source_hash` and `version`.

**3.4** Pagination never cuts an ayah; a page of results ends on an ayah boundary.

*Checked by:* A contract test on the last item of every page.

**3.5** An unknown location is a `404` that names the numbering system it was checked against, never a nearest guess.

*Checked by:* A contract test with an ayah number valid in one system and not another.

## 4. Storage and encoding

The database compares Quranic text byte for byte and changes nothing on the way in or out.

**4.1** Text columns use a binary collation, so that `'مُحَمَّد' = 'محمد'` is false.

In MySQL that is `utf8mb4_bin`; `SELECT 'مُحَمَّد' = 'محمد';` must return `0`.

*Checked by:* The collation query, run as a test against the shipped database.

**4.2** No normalisation anywhere between the file and the reader, not in the driver, the ORM, or a serialiser's "clean output" option.

*Checked by:* A lint rule banning `normalize` in the text path.

**4.3** The character allowlist is enforced at ingestion, and a character outside it fails the import.

*Checked by:* An import test with one foreign character.

**4.4** A full-text index on `text` with a collation that folds marks is a search on the wrong field; search goes through `search_key`.

*Checked by:* A schema check that no full-text index sits on a text column.

## 5. Rendering and fonts

The rasm, the dabt and the font are three layers, and only the first two are the text.

**5.1** A page-and-line layout is a dataset keyed to a `mushaf_edition`; it says which words fall on which line of which page and never carries text.

```text
layout row:  mushaf_edition = "…"   page_number = 3   line_number = 7
             word_key = "2:6:1" … "2:7:4"
```

*Checked by:* A snapshot test per page, rebuilt from the layout dataset and the text.

**5.2** A glyph-coded text, an ayah rewritten as the codepoints of one particular font, is a derived layer that names its font, its font version and the source hash.

*Checked by:* The derived-layer hash check.

**5.3** Fallback fonts are forbidden for Quranic text; a missing glyph fails the build and is never drawn by another font, because a substituted shape can read as a different mark.

*Checked by:* The `cmap` coverage test per font release, and a check that the text stack has one font.

## 6. Audio and recitation

A recording is a recitation by a reciter in a riwayah, with a style and a pace.

**6.1** A reciter is not a rawi; the performer of a recording is bound to the riwayah they recite in, not entered as its transmitter.

*Checked by:* The `rawi_id` schema check above.

**6.2** The style of performance is `recitation_style`, and how the audio was cut is a property of the files rather than of the recitation.

The surveyed codebase filed murattal, mujawwad and muallim under a `type` column and "by surah" and "by ayah" under a classification.

*Checked by:* The terminology audit, which reports `type` on a Quranic concept.

**6.3** `ayah_timing` and `word_timing` are derived layers, and each file names the hash of the audio it was aligned against, the text release and the numbering system.

```text
# ayah_timing v1
# riwayah:                hafs_an_asim
# audio_sha256:           …
# text_version:           1.2.0
# ayah_numbering_system:  kufi
ayah_key   start_ms   end_ms
1:1        0          5320
1:2        5320       9870
```

*Checked by:* A build step that verifies the audio hash and the text release in every header against the current data.

**6.4** Streams, radios and playlists are application concepts; the application names them and the standard does not.

*Checked by:* The scope rule of the standard, section 30.

**6.5** A recitation never plays without the reader's action; autoplay is off by default, and a notification or an advertisement never carries it.

*Checked by:* A review rule for the interface.

## 7. Search

The search key is derived from the text by a versioned, deterministic function, and the reader never sees it.

**7.1** The fold is the one the dataset ships, applied to the query and to the index alike, and a project never writes its own; where a dataset ships none, the project declares a function, versions it with the dataset, and strips only the dabt, the tatweel and the letter forms search should not distinguish.

```text
search_key(text), one dataset's declared fold:
  1. remove dabt marks and the tatweel (U+0640)
  2. أ إ آ ٱ → ا     ؤ → و     ئ → ي
  3. ى → ي           ة → ه
  4. collapse whitespace
```

Quran Text, Quran SVG Elements and Quran Engine each ship a fold, and the three differ; an index built with one is searched with the same one, and a query folded with another finds nothing.

*Checked by:* Golden input-to-key cases, in the pattern of `tools/test_translit.py`, and a test that the query and the index use the same fold version.

**7.2** The function has a version, a change to it is a change to the dataset, and the index is rebuilt.

*Checked by:* A test that the index version equals the function version.

**7.3** A result links to a location and to the stored `text`, never to the key.

*Checked by:* A contract test on the search response.

## 8. Caching

A cache key names everything that changes the text, and a cache of Quranic text is never invalidated by time alone.

**8.1** The key includes the dataset version, the source hash, the edition, the riwayah and the numbering system, even when two of them default to the same value today.

```text
cache key:  ayah:{version}:{source_hash:12}:{mushaf_edition}:{ayah_numbering_system}:{ayah_key}
CDN path:   /text/1.2.0/{mushaf_edition}/2/255.json
```

The source hash is what invalidates the cache when a dataset is corrected before its version moves.

*Checked by:* A test of the cache key format.

**8.2** A `MAJOR` data release invalidates every cache of text built on the previous release, and CDN objects that hold text are immutable with the version in the path, not in a query string.

*Checked by:* A test that bumping the release changes every text URL.
