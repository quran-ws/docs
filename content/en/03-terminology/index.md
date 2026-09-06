---
title: Terminology
description: One name per concept, derived spellings, a machine-readable source.
status: draft
sidebar:
  order: 1
---

- [Terminology Standard](/guidelines/en/03-terminology/standard/) — how a concept is named: one canonical name, spellings derived by a documented function rather than chosen, and the fields each name lives in.
- [Decision record](/guidelines/en/03-terminology/decisions/) — the contested decisions, each with its reason and the measurement behind it.
- [Terminology dictionary](/guidelines/en/03-terminology/dictionary/) — the concepts with their definitions and names, generated from `standards/terminology/concepts/`. Each entry is written in both languages, and each page is generated from its own side of it.

For an AI agent, the same source is packaged as a skill in
[`skills/quranic-terminology/`](https://github.com/quran-ws/guidelines/tree/main/skills/quranic-terminology):
the standard, the dictionary, and scripts that resolve a spelling, derive a name,
and audit an existing codebase against the standard. It is generated on every
build, so it never drifts from the entries.

The machine-readable source is language-neutral and usable now:

| file | what it holds |
| --- | --- |
| `standards/terminology/concepts/*.yml` | one file per concept |
| `standards/terminology/schema.json` | the entry schema |
| `standards/terminology/aliases.json` | every known spelling, resolved to its concept |
| `standards/terminology/sources.yml` | the sources cited by entries |
