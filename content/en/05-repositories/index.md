---
title: Repositories and releases
description: Repository layout, commits, review, releases, and what a project may rely on when it depends on us.
status: draft
sidebar:
  order: 1
---

A Quran project publishes three kinds of thing: prose that explains, code and
data that a machine reads, and the Quranic text itself. Each is owned
differently, changed differently and reviewed differently, and the repository
has to make the difference visible to someone who is not us.

**The governing rule:** everything we publish can be rebuilt by someone who is
not us, from what is in the repository, under a licence that says what they may
do with it.

This page is a draft. It generalises what this repository already does — its
`LICENSE`, its `CONTRIBUTING.md`, its build and its commit history — into rules
a second project can follow. Where a rule is not yet enforced by a tool, the
test table at the end says what the tool would check. The rules for the text
itself are in [Handling Quranic text](/guidelines/en/02-quranic-text/), and the
rules for versioning a dataset are in
[Versioning and corrections](/guidelines/en/04-versioning/).

## 1. Licences, and what each covers

The licences everything we publish falls under, the attribution we ask for
and the attribution we waive, are in
[Waqf and Open Licensing](/guidelines/en/05-repositories/licensing/).

## 2. Repository layout

One repository holds one product or one dataset. A dataset that several
products share is its own repository, with its own releases.

- `standards/` is the source of truth; `content/` explains it; anything
  generated is written by the build and never by hand.
- Commit generated output only when a consumer needs it without running the
  build — a dictionary page a reader opens on GitHub, a skill an agent
  installs. Then the build is the only thing that writes it.
- `README` states, in this order: what the repository is for, how to run or
  install it, the licence, and the `status` of what it contains.
- A bilingual `README` puts Arabic first when Arabic is the authoring language
  of the repository, and English first otherwise.
- CI regenerates everything and fails when the tree is dirty afterwards. A
  hand-edited generated file is caught here, not in review:

```yaml
- run: python3 tools/build.py
- run: git diff --exit-code   # a dirty tree means someone edited generated output
```

## 3. Naming

A repository, a package and a directory are named by the dictionary's `code`
name, the same as a table or a field. The terminology standard applies to the
repository name too.

- Repository and package names are kebab-case: `qiraat-ayah-map`,
  `mushaf-layout`, `ayah-timing`.
- Directory, file and identifier names inside the code are snake_case:
  `ayah_numbering_system`, `mushaf_edition`.
- Plurals follow the standard's rule (`ayahs`, `riwayahs`), never the Arabic
  plural transliterated as a collection name.
- A name that isn't in the [dictionary](/guidelines/en/03-terminology/dictionary/)
  is added there before the repository is created, not after.
- `audit_terminology.py --strict` runs over the tree in CI and blocks a merge
  on an error.

## 4. Commits

One commit makes one change, and its subject says what changed and why it
matters, in a plain sentence.

- The subject is a sentence a reader can act on, not a label. Compare:

```text
Yes:  Give every entry its English side, and generate the English dictionary
Yes:  Drop the case ending before deriving a name
No:   Update dictionary
No:   fix(terminology): misc
```

- The body, when there is one, gives the case behind the change: which
  project, which place, what was ambiguous. A rule with no case behind it
  doesn't get adopted, and a commit with no case behind it is hard to review.
- A change to Quranic text data is its own commit. It never shares a commit
  with code, prose or generated output, because its reviewer reads it
  character by character and must not be asked to read anything else at the
  same time.
- A commit that touches a text data file and a code file together fails a
  hook.
- Published history is never rewritten. A mistake on `main` is fixed by a new
  commit that names the one it corrects.
- A commit author is a person or a named bot. A commit signed off under the
  Developer Certificate of Origin says who is answerable for the change
  (section 8 below).

## 5. Pull requests and review

A pull request answers the template: the change, the case that prompted it,
and the checklist. A reviewer approves a rule, not the prose around it.

- Every PR follows an issue where the change was agreed. A PR that changes an
  `adopted` page or entry links the issue where the agreement was recorded.
- Anything that touches Quranic text needs a second reviewer. That reviewer
  reads the diff character by character in a codepoint view — `U+0651`
  followed by `U+064E`, not "a shaddah and a fathah" — because a line diff
  hides a reordered mark and a substituted look-alike.
- The reviewer of a text change checks the whole changed ayah against the
  published source, not only the changed characters.
- Generated output is not reviewed by eye. The reviewer checks that the source
  changed and that CI regenerated it.
- The checklist a text-touching PR answers:

```markdown
- [ ] Discussed in an issue before this PR.
- [ ] Text data changes are in their own commit.
- [ ] A second reviewer read the text diff as codepoints.
- [ ] The changed ayah was compared with the published source.
- [ ] `python3 tools/build.py` passes; no generated file was edited by hand.
- [ ] Arabic and English pages did not diverge, or the divergence is stated.
```

- `CODEOWNERS` names the second reviewer for the paths that carry the standard
  and the text, so the request is automatic:

```text
standards/            @quran-ws/terminology
content/*/02-*/       @quran-ws/text-review
data/text/            @quran-ws/text-review
```

The group names are placeholders; a project fills in its own.

## 6. Releases and tags

A release is a tag, and a tag is immutable. Once published, it is never moved,
deleted or rebuilt.

- A dataset that carries Quranic text is versioned by the data rules in
  [Versioning and corrections](/guidelines/en/04-versioning/): `MAJOR` when a
  transmitted character, an ayah boundary or an identifier changes, `MINOR`
  when a derived layer or metadata is added, `PATCH` when only non-text
  metadata changes. Code is versioned by ordinary semantic versioning.
- The tag, the manifest and the changelog agree on the version. A tag whose
  manifest says a different version fails the release script:

```text
git tag:        hafs-uthmani-v3.0.0
dataset.json:   { "version": "3.0.0",
                  "mushaf_edition": "...",
                  "riwayah": "hafs_an_asim",
                  "ayah_numbering_system": "kufi",
                  "source_hash": "sha256:…",
                  "license": "..." }
```

- A `MAJOR` data release carries its changelog and the errata it applies,
  listed character by character, in the release notes and as a
  machine-readable file next to the data.
- A release is announced before or with its publication, never after a
  consumer notices.
- An old release stays downloadable. It is marked superseded, never removed.

## 7. Depending on us

A downstream project pins a tagged release, never `main`. `main` is where the
next release is being prepared, and nothing on it is promised.

- What we promise within a `MAJOR`: the text bytes, the identifiers, the ayah
  boundaries and the `source_hash` of every released dataset; the `code` names
  of every `adopted` entry.
- What we don't promise: the wording of any prose, the `display` names, and
  anything whose `status` is `draft` or `proposed`. A `draft` page promises
  nothing, and its frontmatter says so.
- Every artefact we publish — a dataset, a skill, a package — carries its
  version and the commit it was built from, so a consumer can ask whether it
  is behind. The skill's `update_check.py` is the pattern; every artefact gets
  the same.
- A project that depends on us records the pinned version in its own
  manifest, next to the dataset identity, so its own consumers can trace the
  chain.
- The `README` lists the supported pins: which releases are current, which
  are superseded, and for how long a superseded release stays available.

## 8. Contributing from outside

A contribution is accepted by the same rules as our own work: an issue, an
agreement, a PR that answers the checklist.

- Sign-off follows the Developer Certificate of Origin (`git commit -s`). We
  recommend DCO over a contributor licence agreement, because it asks the
  contributor to affirm that they may contribute the change under the
  repository's licence, and asks nothing else. A DCO bot checks the trailer.
- A scholarly claim — a definition, a count, an attribution to a qiraah or a
  numbering system — cites a source that is listed in `sources.yml`. A claim
  with no source stays `draft`.
- A contribution that adds Quranic text or changes it names the published
  edition it was taken from, and goes through the second review of section 5.
- The repository states its code of conduct in `CODE_OF_CONDUCT.md`, and
  review comments follow it.
- Whoever maintains the repository answers an issue with a decision or a
  question, not silence. An open question is stated as a question.

## Every rule becomes a test

A failing check blocks the merge or the release. It never edits the tree.

| What it tests | How |
| --- | --- |
| The build reproduces committed output | `python3 tools/build.py && git diff --exit-code` in CI |
| Every dataset has a licence | The manifest schema requires `license`; validation fails without it |
| Every top-level directory is licensed | A check that each directory in the tree appears in `LICENSE` |
| Names resolve in the dictionary | `audit_terminology.py --strict` over the tree, including the repository name |
| Text commits are isolated | A hook fails a commit that touches a text data file together with any other kind of file |
| Text changes reach the second reviewer | `CODEOWNERS` covers `standards/`, the text pages and every text data directory |
| Text diffs are read as codepoints | The PR checklist item is confirmed by the second reviewer, and a bot refuses to merge without it |
| Tag equals manifest version | The release script compares the tag with `version` in `dataset.json` and stops on a mismatch |
| A release is immutable | A hook rejects a force-push to a tag or a tag deletion |
| Every artefact names its build | Each published artefact carries `version` and the commit it was built from; `update_check.py` reads them |
| Contributions are signed off | A DCO bot checks the `Signed-off-by` trailer on every commit |
| Claims have sources | `validate.py` refuses `adopted` on an entry with no source in `sources.yml` |
