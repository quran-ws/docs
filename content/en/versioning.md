---
title: Versioning and corrections
description: A dataset that carries Quranic text is released, never edited. How a release is named, when its version moves, where a correction is written down, and what downstream may rely on.
status: proposed
generated: content/pages/versioning.yml
sidebar:
  order: 3
---

**The governing rule:** a dataset that carries Quranic text is released, never
edited. Every copy in the world can say which release it is, and every change
between two releases is listed character by character.

The [text page](/guidelines/en/quranic-text/) says that the text is immutable
and that a correction is never silent. This page says what that means once the
data leaves your machine. The manifest and the erratum record below are
proposals; their field names follow the
[dictionary](/guidelines/en/reference/dictionary/) where it has a name.

## 1. What is versioned

The unit of versioning is the dataset, not the repository or the app.

**1.1** A dataset is one thing built from the text, such as a text edition, a numbering table, a segmentation, a timing file or a translation, and each has its own version.

*Checked by:* One manifest per data file, validated by the release script.

**1.2** The identity travels with the data: publish a `dataset.json` manifest beside every data file, carrying the edition, the riwayah, the numbering system, the version and the source hash.

```json
{
  "dataset": "text",
  "mushaf_edition": "madinah_hafs_1441",
  "riwayah": "hafs_an_asim",
  "ayah_numbering_system": "kufi",
  "version": "2.0.0",
  "source_hash": "sha256:…",
  "derived_from": null,
  "license": "…",
  "errata": "errata.json",
  "released": "2026-09-06"
}
```

The values of `mushaf_edition` and `riwayah` come from the registries under `standards/terminology/registries/`, never typed by hand.

*Checked by:* Schema validation of the manifest in the release script, with every field required.

**1.3** The version in the manifest and the repository tag are the same string.

*Checked by:* The release script compares the tag with `version` in the manifest and stops on a mismatch.

## 2. Semantic versioning for data

The number is decided by the diff, not by how small the fix felt.

**2.1** `MAJOR` moves when any transmitted character, ayah boundary or identifier changes, including a correction of what looks like a spelling error.

Every hash built on the text breaks, so a one-character correction is a `MAJOR`.

*Checked by:* The release script diffs the previous tag's text and refuses a `MINOR` or `PATCH` bump if any byte of text differs.

**2.2** `MINOR` moves when a derived layer or metadata is added without changing transmitted text or identifiers.

*Checked by:* The same diff, which allows the bump when the text is unchanged.

**2.3** `PATCH` moves when only non-text metadata changes: a description, a licence file, the layout of files on disk.

*Checked by:* The same diff.

**2.4** Code that reads the data follows ordinary semantic versioning and has its own number; the two are not tied.

*Checked by:* The [repositories page](/guidelines/en/repositories/), which versions code and data separately.

## 3. Identifiers never change meaning

A release may add identifiers; it never reuses or renumbers one.

**3.1** The set of identifiers in release N is a subset of the set in release N+1; a release that fails this is `MAJOR` at least, and the missing identifiers are listed in the errata.

*Checked by:* A set comparison of identifiers across the two tags in the release script.

**3.2** Adding a numbering system is a new table or column keyed by `ayah_numbering_system`, never a rewrite of existing numbers.

*Checked by:* The identifier set comparison.

**3.3** An identifier that turns out to be wrong is not corrected in place; the old one stays, marked superseded, and the new one is added.

*Checked by:* The identifier set comparison.

## 4. The errata log

Every correction is written down before it is merged, in one append-only file per dataset.

**4.1** The file is `errata.json`, or `ERRATA.md` for a dataset published as prose, and entries are added, never edited or removed.

```json
{
  "id": "2026-0001",
  "location": { "surah_number": 2, "ayah_number": 255, "word_position": 12,
                "ayah_numbering_system": "kufi" },
  "offset": { "unit": "codepoint", "start": 38, "end": 39 },
  "before": "U+0651 U+064E",
  "after":  "U+064E U+0651",
  "kind": "transmission_error",
  "confirmed_by": "…",
  "confirmed_on": "2026-08-30",
  "fixed_in": "2.0.0"
}
```

*Checked by:* A one-to-one match between the text diff of a release and the errata that name it in `fixed_in`.

**4.2** `before` and `after` are codepoint sequences, never rendered strings, so the entry can be verified without a font.

*Checked by:* A lookup that finds the `before` sequence at `location` and `offset` in the previous release.

**4.3** `kind` is one of `source_error`, `transmission_error` or `display_error`; a display error is fixed in the renderer, produces no text diff, and is logged so nobody "fixes" the text to match the screen.

*Checked by:* Schema validation of the erratum.

**4.4** `confirmed_by` names the authority that confirmed the correction, the publisher of the edition or a reviewer named in the repository; an erratum without one is not merged.

*Checked by:* Schema validation, and the second reviewer of every text change.

**4.5** The erratum is filed before the fix is merged, in the same pull request or an earlier one; a text diff with no erratum is rejected in review.

*Checked by:* The diff-to-errata match, run on every pull request that touches text.

## 5. Announcing a change

A text update is never silent.

**5.1** A `MAJOR` release is announced before or with its publication, in two parts: a changelog entry a person reads, and a machine-readable list of the errata it carries.

```text
2.0.0 — 2026-09-06 — MAJOR — text: 1 correction (2026-0001, 2:255); ids unchanged.
```

*Checked by:* The release script refuses a `MAJOR` tag without a changelog entry and an errata list.

**5.2** An app that ships the text shows the reader a visible notice when it moves to a new `MAJOR`, naming the locations and never quoting the old text.

*Checked by:* A test of the update path, with and without a notice record.

**5.3** The app's update path refuses a dataset whose `MAJOR` differs from the installed one unless a notice record exists for the move.

*Checked by:* The same update-path test.

**5.4** A `MINOR` or `PATCH` release needs the changelog entry only.

*Checked by:* The release script.

## 6. What downstream may rely on

Within one `MAJOR`, the text bytes, the identifiers, the ayah boundaries and the source hash are stable, and nothing else is promised.

**6.1** A derived layer names the exact release it was built from in `derived_from`, and the build fails if it names a release that does not exist.

*Checked by:* A lookup in the release index at build time.

**6.2** A derived layer built on release N is not valid against release N+1 until it is rebuilt, or its manifest says it was checked against the errata and found unaffected.

*Checked by:* The `derived_from` check against the current release.

**6.3** Depend on a tagged release, never on the head of a branch.

*Checked by:* The pinned version recorded in the dependant's own manifest.

## 7. Superseded releases

A release is never deleted; it is marked superseded.

**7.1** The release index lists every version ever published, with its source hash, its date, and the version that superseded it if any.

*Checked by:* A diff between the tags of the repository and the index.

**7.2** A superseded release stays downloadable, so a derived layer built on it can still be verified against it, and the index says how long it receives errata notices.

*Checked by:* A hook that rejects a tag deletion or a force-push to a tag.

**7.3** A release found to carry a text error is not withdrawn; the erratum is filed and the corrected release supersedes it.

Withdrawing it would break every hash that points at it and hide what was changed.

*Checked by:* The same hook.

## 8. Until there is a tag

The rules above describe a released dataset; most of ours have no tag yet, and a reader needs to know what holds in the meantime.

**8.1** Until a dataset has a tag, the commit is its version; a consumer pins the commit, records it, and reads every file at that ref.

A script that resolves the head of a branch at build time is not pinned to anything.

*Checked by:* The consumer's manifest names a commit, and a build step reads the data at that commit and nowhere else.

**8.2** Three things can be pinned and they answer different questions; the commit pins the tree, the digest of a release asset pins the archive, and the content digest inside the data pins the text an annotation was computed against.

*Checked by:* Review of what a manifest records.

**8.3** A `format_version` describes the shape of a file, a `schema_version` its schema, a tag a release and a content digest the text; a stable `format_version` is no evidence that the data has not changed.

*Checked by:* The consumer verifies a digest, never a version number alone.

**8.4** A pin promises the bytes and nothing else; a released bundle may not be reproducible from its commits, a correction may land before a number moves, and a digest does not travel with a re-export, so the consumer keeps the source digest and the source reference in its own records.

*Checked by:* Review of what a consumer stores beside its copy of the data.
