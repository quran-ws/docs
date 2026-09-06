---
title: Terminology
description: One name per concept, derived spellings, a machine-readable source.
status: draft
sidebar:
  order: 1
---

The terminology standard and dictionary are authored in Arabic and have no
English translation yet — a known gap, not a different structure.

- [Quranic Software Terminology Standard](/guidelines/ar/03-terminology/standard/) — how a concept is named: one canonical name, spellings derived by a documented function rather than chosen, and the fields each name lives in.
- [Terminology dictionary](/guidelines/ar/03-terminology/dictionary/) — 113 concepts, generated from `standards/terminology/concepts/`.

The machine-readable source is language-neutral and usable now:

| file | what it holds |
| --- | --- |
| `standards/terminology/concepts/*.yml` | one file per concept |
| `standards/terminology/schema.json` | the entry schema |
| `standards/terminology/aliases.json` | every known spelling, resolved to its concept |
| `standards/terminology/sources.yml` | the sources cited by entries |
