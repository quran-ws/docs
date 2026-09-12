---
title: Repositories and licensing
description: Repository layout, commits, review, releases, what a project may rely on when it depends on us, and the licences everything is published under.
status: proposed
generated: content/pages/repositories.yml
sidebar:
  order: 5
---

**The governing rule:** everything we publish can be rebuilt by someone who is
not us, from what is in the repository, under a licence that says what they
may do with it.

A Quran project publishes 3 kinds of thing: prose that explains, code and
data that a machine reads, and the Quranic text itself. Each is owned,
changed and reviewed differently, and the repository makes that difference
visible. The rules for the text itself are on the
[text page](/guidelines/en/quranic-text/), and the rules for versioning a
dataset on the [versioning page](/guidelines/en/versioning/).

## 1. Licensing

Everything we publish is licensed, and the Quranic text is covered by no licence and no claim of ownership.

**1.1** Code is MIT and data and content are CC BY 4.0, with attribution waived for use inside a product and required for republication.

The licences in full, the attribution we ask for and the attribution we waive, are in [Waqf and open licensing](/guidelines/en/licensing/).

*Checked by:* The manifest schema requires `license`, and a check that each top-level directory appears in `LICENSE`.

## 2. Repository layout

One repository holds one product or one dataset.

**2.1** A dataset that several products share is its own repository, with its own releases.

*Checked by:* A review rule; there is no tool for it.

**2.2** The machine-readable source is the source of truth, the prose explains it, and anything generated is written by the build and never by hand.

```yaml
- run: python3 tools/build.py
- run: git diff --exit-code   # a dirty tree means someone edited generated output
```

*Checked by:* CI regenerates everything and fails when the tree is dirty afterwards.

**2.3** Commit generated output only when a consumer needs it without running the build, such as a page read on GitHub or a skill an agent installs; then the build is the only thing that writes it.

*Checked by:* The same CI diff.

**2.4** `README` states, in this order: what the repository is for, how to run or install it, the licence, and the status of what it contains.

*Checked by:* A review rule.

## 3. Commits

One commit makes one change, and its subject says what changed in a plain sentence.

**3.1** The subject is a sentence a reader can act on, not a label, and the body gives the case behind the change.

```text
Yes:  Give every entry its English side, and generate the English dictionary
Yes:  Drop the case ending before deriving a name
No:   Update dictionary
No:   fix(terminology): misc
```

*Checked by:* A review rule.

**3.2** A change to Quranic text data is its own commit and never shares one with code, prose or generated output, because its reviewer reads it character by character.

*Checked by:* A hook that fails a commit touching a text data file together with any other kind of file.

**3.3** Published history is never rewritten; a mistake on `main` is fixed by a new commit that names the one it corrects.

*Checked by:* Branch protection on `main` and on every tag.

**3.4** A commit author is a person or a named bot, and every commit is signed off under the Developer Certificate of Origin (`git commit -s`).

We use the DCO rather than a contributor licence agreement, because it asks the contributor to affirm that they may contribute under the repository's licence and nothing else.

*Checked by:* A DCO bot that checks the `Signed-off-by` trailer on every commit.

## 4. Pull requests and review

A pull request answers the template, and a reviewer approves a rule, not the prose around it.

**4.1** A change to a rule or a term follows an issue where it was agreed; a typo or a one-paragraph edit needs no issue.

*Checked by:* The pull request template, which asks for the issue.

**4.2** Anything that touches Quranic text needs a second reviewer, who reads the diff as codepoints and compares the whole changed ayah with the published source.

```text
standards/            @quran-ws/terminology
data/text/            @quran-ws/text-review
```

`CODEOWNERS` names the second reviewer for the paths that carry the standard and the text, so the request is automatic. The group names are placeholders.

*Checked by:* `CODEOWNERS` covers every text data directory, and a bot refuses to merge without the second approval.

**4.3** Generated output is not reviewed by eye; the reviewer checks that the source changed and that CI regenerated it.

*Checked by:* The CI diff.

## 5. Releases and tags

A release is a tag, and a tag is immutable.

**5.1** Once published, a tag is never moved, deleted or rebuilt, and an old release stays downloadable, marked superseded.

*Checked by:* A hook that rejects a force-push to a tag or a tag deletion.

**5.2** A dataset that carries Quranic text is versioned by the [data rules](/guidelines/en/versioning/), and code by ordinary semantic versioning.

```text
git tag:        hafs-uthmani-v3.0.0
dataset.json:   { "version": "3.0.0", "riwayah": "hafs_an_asim", … }
```

*Checked by:* The release script compares the tag with `version` in the manifest and stops on a mismatch.

**5.3** Every published artefact, a dataset, a skill or a package, carries its version and the commit it was built from, so a consumer can ask whether it is behind.

The skill's `update_check.py` is the pattern; every artefact gets the same.

*Checked by:* A test that each published artefact carries `version` and the commit.

## 6. Depending on us

A downstream project pins a tagged release, never `main`.

**6.1** Within a `MAJOR` we promise the text bytes, the identifiers, the ayah boundaries and the source hash of every released dataset, and the `code` names of every `adopted` entry; we do not promise prose wording, `display` names, or anything `draft` or `proposed`.

*Checked by:* The `status` field on every page and entry.

**6.2** A project that depends on us records the pinned version in its own manifest, beside the dataset identity, so its own consumers can trace the chain.

*Checked by:* The manifest schema of the dependant.

**6.3** The `README` lists the supported pins, which releases are current, which are superseded, and for how long a superseded release stays available.

*Checked by:* A review rule.

## 7. Contributing from outside

A contribution is accepted by the same rules as our own work.

**7.1** A scholarly claim, such as a definition, a count or an attribution to a qiraah or a numbering system, cites a source listed in `sources.yml`, and a claim with no source stays `draft`.

*Checked by:* `tools/validate.py` refuses `adopted` on an entry with no source.

**7.2** A contribution that adds or changes Quranic text names the published edition it was taken from and goes through the second review.

*Checked by:* The `CODEOWNERS` rule above.

**7.3** The repository states its code of conduct in `CODE_OF_CONDUCT.md`, and whoever maintains it answers an issue with a decision or a question, never silence.

*Checked by:* A review rule.

**7.4** A scholarly claim carries the tier of its best evidence and the state of its documentation, and both are shown as recorded, never averaged into a score.

```text
tier:   primary | commentary | secondary | modern-reference | api-check
state:  uncited | secondary_only | primary_cited | primary_cited_and_reviewed | disputed | unresolved
```

An `api-check` alone never settles a claim, and a disputed position is never inferred from a total.

*Checked by:* A schema check that every claim carries both fields with a value from the list.
