---
title: Terminology
description: One name per concept, derived spellings, a machine-readable source.
status: draft
sidebar:
  order: 1
---

- [Terminology Standard](/guidelines/en/03-terminology/standard/) — how a concept is named: one canonical name, spellings derived by a documented function rather than chosen, and the fields each name lives in.
- [Decision record](/guidelines/en/03-terminology/decisions/) — the contested decisions, each with its reason and the measurement behind it.
- [Terminology dictionary](/guidelines/ar/03-terminology/dictionary/) — the concepts with their definitions and names, generated from `standards/terminology/concepts/`. The entries are written in Arabic and have no English translation yet.

The machine-readable source is language-neutral and usable now:

| file | what it holds |
| --- | --- |
| `standards/terminology/concepts/*.yml` | one file per concept |
| `standards/terminology/schema.json` | the entry schema |
| `standards/terminology/aliases.json` | every known spelling, resolved to its concept |
| `standards/terminology/sources.yml` | the sources cited by entries |
