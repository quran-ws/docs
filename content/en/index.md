---
title: Quran.ws Guidelines
description: How we build software that handles the Quran. Naming, text handling, versioning, engineering and repositories, each rule with the check behind it.
status: draft
---

How we build software that handles the Quran. Five short pages of rules, each with the check that enforces it.

| | |
| --- | --- |
| Status | Proposed — nothing adopted yet |
| Licence | CC BY 4.0 · MIT |
| Source | [quran-ws/docs](https://github.com/quran-ws/docs) |
| Languages | [العربية](../ar/index.md) · English |

## Guidelines

Every rule is one sentence, an example, and the check that catches a violation.
Read them in order the first time; after that, each page stands on its own.

1. [Naming](naming.md) — One concept, one name, the same in the model, the table, the foreign key and the API. Is it `ayah` or `verse`? It is `ayah`, and here is why.
2. [Quranic text](quranic-text.md) — The text is transmitted source data, never edited. Encoding, normalisation, tokenisation, display, and the tests that guard them.
3. [Versioning and corrections](versioning.md) — A dataset is released, never edited. Semantic versioning for data, the errata log, and how a reader is told the text changed.
4. [Engineering](engineering.md) — Model the mushaf, not the screen. Tables, identifiers, APIs, storage, fonts, audio, search and caching.
5. [Repositories and licensing](repositories.md) — Layout, commits, review, releases, what a dependant may rely on, and the licences everything is published under. See also [waqf and open licensing](licensing.md).

Every page is proposed; none is adopted.

## Reference

Looked up, not read through. The guidelines link into these where a rule needs them.

- [Dictionary](reference/dictionary.md) — Every concept with its canonical name, its definition, its spellings and its source.
- [Registries](reference/registries.md), the [terminology standard](reference/standard.md) and the [decision record](reference/decisions.md).

## Use it in your repository

The terminology audit reads a codebase and reports every name the standard would have written differently. It renames nothing.

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

Run it in CI on every pull request, and keep what your project already knows in `.terminology.json`. The [naming page](naming.md) says how.

> **Nothing is adopted yet.** Build against a page only once it is marked `adopted`. Until then these are proposals: what concerns the Quranic text itself is reviewed by qualified scholars, and what concerns engineering is one defensible choice among several.
