---
title: Versioning and corrections
description: A dataset that carries Quranic text is released, never edited. How a release is identified, numbered, corrected and announced, and what a downstream project may rely on.
status: draft
sidebar:
  order: 0
---

[Handling Quranic text](/guidelines/en/02-quranic-text/) says that the text is
immutable source data and that a correction is never silent. This page says what
that means once the data leaves your machine: how a release is named, when its
version number moves, where a correction is written down, and what someone who
builds on your release may take for granted.

**The governing rule:** a dataset that carries Quranic text is released, never
edited. Every copy in the world can say which release it is, and every change
between two releases is listed character by character.

This page is a draft. The manifest and the erratum record below are proposals for
discussion; their field names follow the
[dictionary](/guidelines/en/03-terminology/dictionary/) where the dictionary has a
name, and are marked where it does not. Every rule is written to become a test; the
table is at the end.

## 1. What is versioned

The unit of versioning is the dataset, not the repository or the app.

- A dataset is one thing built from the text: a text edition, an ayah numbering
  table, a word segmentation, a timing file, a translation. Each has its own version.
- A dataset has an identity. It is the same tuple that
  [Handling Quranic text](/guidelines/en/02-quranic-text/) requires before an import:
  [`mushaf_edition`](/guidelines/en/03-terminology/dictionary/#mushaf_edition),
  [`riwayah`](/guidelines/en/03-terminology/dictionary/#riwayah),
  [`ayah_numbering_system`](/guidelines/en/03-terminology/dictionary/#ayah_numbering_system),
  a version, and a hash of the file.
- The identity travels with the data. Publish a `dataset.json` manifest next to
  every data file. Proposed shape:

```json
{
  "dataset": "text",
  "mushaf_edition": "madinah_hafs_1441",
  "riwayah": "hafs_an_asim",
  "ayah_numbering_system": "ayah_numbering_kufi",
  "version": "2.0.0",
  "source_hash": "sha256:…",
  "derived_from": null,
  "license": "…",
  "errata": "errata.json",
  "released": "2026-09-06"
}
```

- `version` is the number this page governs. `source_hash` is the hash of the
  published data file, and it is what a derived layer records under `derived_from`.
- The version and the repository tag are the same string. A tag that names a
  different version than the manifest is a broken release.
- The values of `mushaf_edition` and `riwayah` above are illustrations. The
  registries under `standards/terminology/registries/` are the source of the
  accepted values; never copy them into a manifest by hand.

## 2. Semantic versioning for data

The version number moves according to what changed in the data, in the form
`MAJOR.MINOR.PATCH`.

- `MAJOR` moves when any transmitted text character, ayah boundary or identifier
  changes. Fixing a typo in the Quran is always `MAJOR`, because every hash
  downstream breaks.
- `MINOR` moves when a derived layer or metadata is added without changing
  transmitted text or identifiers: a new tajwid annotation, a new translation, a
  new field in the manifest.
- `PATCH` moves when only non-text metadata changes: a description, a licence
  file, the layout of files on disk.
- The number is decided by the diff, not by how small the fix felt. A release
  script diffs the text of the previous release and refuses a `MINOR` or `PATCH`
  bump if any byte of text differs.
- Code that reads the data follows ordinary semantic versioning and has its own
  number. The two are not tied: see
  [Open source and version control](/guidelines/en/05-open-source/).

## 3. Identifiers never change meaning

A new release may add identifiers. It never reuses or renumbers one.

- `surah_number`, `ayah_number` within its numbering system, and `word_position`
  under a declared tokenisation are the identifiers this rule protects. They are
  not dictionary entries yet; the names are proposals.
- Adding a numbering system is a new table or column keyed by
  `ayah_numbering_system`, never a rewrite of existing numbers.
- The set of identifiers in release N is a subset of the set in release N+1. A
  release that fails this check is `MAJOR` at least, and the missing identifiers
  are listed in the errata.
- An identifier that turns out to be wrong is not corrected in place. The old one
  stays, marked superseded, and the new one is added.

## 4. The errata log

Every correction to the text is written down before it is merged, in one
append-only file per dataset.

- The file is `errata.json`, or `ERRATA.md` for a dataset published as prose.
  Entries are added, never edited or removed.
- One entry per correction. Proposed shape:

```json
{
  "id": "2026-0001",
  "location": { "surah_number": 2, "ayah_number": 255, "word_position": 12,
                "ayah_numbering_system": "ayah_numbering_kufi" },
  "offset": { "unit": "codepoint", "start": 38, "end": 39 },
  "before": "U+0651 U+064E",
  "after":  "U+064E U+0651",
  "kind": "transmission_error",
  "confirmed_by": "…",
  "confirmed_on": "2026-08-30",
  "fixed_in": "2.0.0"
}
```

- `location` binds the correction to a surah, an ayah and its numbering system,
  as [Handling Quranic text](/guidelines/en/02-quranic-text/) requires of every
  location.
- `before` and `after` are codepoint sequences, never rendered strings, so the
  entry can be verified without a font.
- `kind` is one of `source_error`, `transmission_error` or `display_error`, the
  three kinds of error that
  [Handling Quranic text](/guidelines/en/02-quranic-text/) distinguishes. A
  `display_error` is fixed in the renderer and produces no text diff; it is logged
  so that nobody "fixes" the text to match the screen.
- `confirmed_by` names the authority that confirmed the correction: the publisher
  of the edition, or a reviewer named in the repository. An erratum without a
  confirming authority is not merged.
- The erratum is filed before the fix is merged, in the same pull request or an
  earlier one. A text diff with no erratum is rejected in review.

## 5. Announcing a change

A `MAJOR` release is announced before or with its publication; a text update is
never silent.

- The announcement has two parts: a changelog entry a person reads, and a
  machine-readable `changes` list an app reads. The `changes` list is the errata
  entries carried by the release, by `id`. A changelog line:

```text
2.0.0 — 2026-09-06 — MAJOR — text: 1 correction (2026-0001, 2:255); ids unchanged.
```

- An app that ships the text shows the reader a visible notice when it moves to a
  new `MAJOR`, of the form "text updated in 2:255, see errata", for a window the
  app defines and states. The notice names the locations; it does not quote the
  old text.
- Silent auto-update of Quranic text is forbidden, as
  [Handling Quranic text](/guidelines/en/02-quranic-text/) already says. The app's
  update path refuses a dataset whose `MAJOR` differs from the installed one unless a
  notice record exists for the move.
- A `MINOR` or `PATCH` release needs the changelog entry only.

## 6. What downstream may rely on

Within one `MAJOR`, the text bytes, the identifiers, the ayah boundaries and
`source_hash` are stable. Across a `MAJOR`, only the identifiers not named in the
errata are.

- A derived layer names the exact release it was built from, in `derived_from`,
  as [Handling Quranic text](/guidelines/en/02-quranic-text/) requires. The build
  fails if it names a release that does not exist in the release index.
- A derived layer built on release N is not valid against release N+1 until it is
  rebuilt or its manifest says it was checked against the errata and found
  unaffected.
- Nothing else is promised: not file layout, not field order, not the wording of a
  description. A project that depends on those is depending on a `PATCH`.
- Depend on a tagged release, never on the head of a branch. Which pins we support
  is stated in [Open source and version control](/guidelines/en/05-open-source/).

## 7. Deprecation and support window

A release is never deleted. It is marked superseded.

- The release index lists every version ever published, with its `source_hash`,
  its date, and the version that superseded it if any.
- A superseded release stays downloadable, so that a derived layer built on it can
  still be verified against it.
- How long a superseded release receives errata notices is stated in the release
  index, per dataset. This page does not fix a number.
- A release found to carry a text error is not withdrawn; the erratum is filed and
  the corrected release supersedes it. Withdrawing it would break every hash that
  points at it, and would hide what was changed.

## Every rule becomes a test

A failing release test blocks the release. It never edits the data.

| Rule | What the test checks | How |
| --- | --- | --- |
| Manifest present and complete | Every published data file has a `dataset.json` beside it with every field in section 1 | Schema validation in the release script |
| Text diff means `MAJOR` | No `MINOR` or `PATCH` release differs from its predecessor in any text byte | The release script diffs the previous tag's text and refuses the bump |
| Identifier sets grow only | The identifiers of release N are a subset of those in release N+1 | Set comparison of ids across the two tags |
| Errata and diff match | Every text diff between releases has an erratum, and every erratum with `fixed_in` = this release appears in the diff | One-to-one match between diff hunks and erratum locations |
| Erratum is verifiable | The `before` sequence is found at `location` and `offset` in release N−1 | Lookup against the previous release's text |
| Derived layer names a release | Every derived-layer manifest has a `derived_from` that exists in the release index | Release index lookup at build time |
| Notice record for `MAJOR` | The app refuses a dataset whose `MAJOR` differs unless a notice record exists | Test of the update path with and without the record |
| Tag equals manifest | The git tag and `version` in the manifest are the same string | Release script compares the two |
| Release index is complete | Every tag ever published appears in the release index | Diff between tags and index |
