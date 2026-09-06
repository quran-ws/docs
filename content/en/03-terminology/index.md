---
title: Terminology
description: One name per concept, derived spellings, a machine-readable source.
status: draft
sidebar:
  order: 0
---

- [Terminology standard](/guidelines/en/03-terminology/standard/) — how a concept is named: one canonical name, spellings derived by a documented function rather than chosen, and the fields each name lives in.
- [Decision record](/guidelines/en/03-terminology/decisions/) — the contested decisions, each dated, with its reason and the measurement behind it.
- [Terminology dictionary](/guidelines/en/03-terminology/dictionary/) — the concepts with their definitions and names, generated from `standards/terminology/concepts/`. Each entry is written in both languages, and each page is generated from its own side of it.
- [Registries](/guidelines/en/03-terminology/registries/) — the members of the closed sets the dictionary points at: the surahs, the qiraat and their rawis and riwayahs, the ayah numbering systems and their counts, the places of prostration.

For an AI agent, the same source is packaged as a skill in
[`skills/quranic-terminology/`](https://github.com/quran-ws/guidelines/tree/main/skills/quranic-terminology):
the standard, the dictionary, the registries, and scripts that resolve a spelling,
derive a name, and audit an existing codebase against the standard. Copy the
directory into your agent's skills directory; it is generated on every build and
stamped with a hash of its inputs, so it never drifts from the entries.

The machine-readable source is language-neutral and usable on its own:

| file | what it holds |
| --- | --- |
| `standards/terminology/concepts/*.yml` | one file per concept |
| `standards/terminology/schema.json` | the entry schema |
| `standards/terminology/registries/*.tsv` | the members of each closed set, one row each |
| `standards/terminology/data/*.tsv` | the spelling tables the derivation reads: letter names, general words, connectives, established spellings |
| `standards/terminology/aliases.json` | every known spelling of a concept, resolved to it |
| `standards/terminology/registry_aliases.json` | every known spelling of a member, resolved to it, keyed by kind |
| `standards/terminology/sources.yml` | the sources cited by entries and registry rows |
