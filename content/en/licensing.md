---
title: Waqf and Open Licensing
description: The default Quran.ws licences, the attribution waiver for use inside products, when attribution is still required on republication, and the purpose of the waqf.
status: draft
sidebar:
  order: 2
---

**The governing rule:** we publish code under MIT and data and content under
CC BY 4.0. Attribution is waived when the material is used inside a product, and
required when the data itself is republished as a resource in its own right.

**Version:** 1.0 — 1 September 2026  
**Applies to:** all repositories, datasets, and resources published by Quran.ws unless a specific resource states otherwise.  
**Copyright:** 2026 Quran.ws — we hold these rights to protect the waqf, and we do not use them to restrict what people may do with it.

## Summary

| | |
|---|---|
| Software and code | **MIT** (`MIT`) |
| Data and content | **CC BY 4.0** (`CC-BY-4.0`), plus a standing waiver of attribution for use inside applications and products |
| Third-party material | Retains its original licence and terms |
| Names, logos, trademarks | Not licensed |

We use the established open licences unmodified: we do not invent a licence of our own and we do not add restrictions to these ones, so that a developer or an organisation can see what they may do without interpreting a licence they have never met.

## Purpose

**This work is dedicated as a waqf for the sake of Allah, seeking His pleasure through the benefit it brings to people.**

We publish it to enable the widest possible beneficial use, with as few restrictions as possible.

We ask for attribution so that a resource stays **traceable**. Quranic and Islamic resources are reviewed, corrected, and updated over time, and the software that produces or processes them receives corrections too. When copies travel downstream, the path back to their origin should stay open so that people can verify them and find newer, corrected releases.

## Default licences

We publish what we hold the rights to under two licences: MIT for code, and
CC BY 4.0 for data and content. Anything we do not hold the rights to stays
under its owner's licence.

### Software and code — MIT

Software for which we hold the necessary rights is released under the **MIT License** (SPDX: `MIT`).

MIT permits the software to be used, copied, modified, merged, published, distributed, sublicensed, sold, and used commercially, subject to its terms, including preservation of the required copyright and licence notices.

### Data and content — CC BY 4.0

Data and content for which we hold the necessary rights are released under the **Creative Commons Attribution 4.0 International License** (SPDX: `CC-BY-4.0`), together with the additional permission set out in the next section.

### Third-party material

**We license only what we have the right to license.**

Quranic text editions and mushaf typesettings, fonts, artwork, audio recitations, third-party datasets, and vendored software components retain their original copyrights, licences, and terms. Our processing, correction, organisation, transformation, or distribution of such material does not create ownership and does not override the terms of the original rights holders.

Where a specific resource, directory, or file carries its own `LICENSE` or `NOTICE`, **that notice governs for that material** and overrides this policy. Where practical, each published resource carries a manifest identifying which parts are ours and which are third-party, with their respective licences.

## Additional permission: attribution waived for use in products

As rights holders of our original data and content, we grant to all users a **permanent, worldwide, royalty-free, irrevocable waiver** of the attribution requirement of CC BY 4.0 (Section 3(a)) **when the material is used within an application, website, service, API, bot, tool, research work, or product, whether free or commercial.**

This additional permission **expands** what users may do. It adds no restriction to CC BY 4.0, and it does not affect any other term of that licence.

**Merely using a resource to provide functionality to end users does not require displaying our name, logo, or a link.** An application that uses our data to serve its users need not credit us as a condition of that use — including when the data is bundled inside the application for offline operation.

Credit in these cases is always appreciated, but never required.

## When attribution is still required: republication

A different rule applies when the resource is not merely **used**, but the **data or content itself is made available to others as a resource in its own right**.

**The test:** can a third party obtain the data *as data* from what you distribute? If yes, this is republication and CC BY 4.0 attribution applies. If they can only obtain the functionality or the outputs, it is use, and attribution is waived.

| Republication — attribution required | Use — attribution waived |
|---|---|
| Published databases, datasets, and bulk dumps | Data bundled inside an app to make it work offline |
| Mirrors and re-hosted copies | An API that answers individual user queries |
| Downloadable copies or exports offered to users | Search, display, or analysis features built on the data |
| APIs or endpoints that serve the dataset in bulk | Derived outputs that do not reconstitute the dataset |
| Modified or derived versions published as resources | Internal use inside an organisation |
| A repository that vendors our dataset as a data file | Training machine learning models (see below) |

Where practical, we ask that attribution include a link to the **canonical source** of the resource, so that a path stays open from every redistributed copy back to its origin, its corrections, and its updates.

### Suggested attribution

> Data from *[resource name]* by Quran.ws, licensed under CC BY 4.0. Source: *[canonical URL]*. Version: *[version]*. Modified: *[yes/no]*.

## Source traceability

Every resource we publish carries what identifies where it came from, where that
is practical:

- the canonical source
- the version or `release` number
- the upstream source, where the material is derived
- the generator name and version, or the `commit`, where relevant
- a note of the relevant modifications

**Even where visible attribution is waived, we ask that these provenance fields be preserved inside the data itself**, so that a copy encountered years later can still be identified and checked against corrected releases. This is a request, not a condition.

A generated resource does not automatically inherit the licence of the software that generated it. Its licensing depends on the rights in the resource itself and in its underlying sources.

## Machine learning and AI

Use of our original data and content for training, fine-tuning, evaluating, indexing, or retrieval by machine learning and AI systems is **permitted**, and is treated as use rather than republication.

Publishing our dataset as part of a distributed training corpus is republication and follows the rule above.

We ask that systems built on this material take care not to present generated or paraphrased output as Quranic text, and preserve a path back to the verified source where practical.

## Names, logos, and trademarks

These licences grant rights in code, data, and content. **They grant no rights in our names, logos, domain names, or trademarks.**

Use of our material does not imply that we endorse, review, certify, or are affiliated with any product built on it, and our names and marks may not be used to suggest otherwise.

## Accuracy, verification, and no warranty

We work carefully on the correctness of what we publish, but the material is provided **as is, without warranty of any kind**, as stated in the MIT License and in CC BY 4.0 (Sections 5 and 6).

Quranic text, transliteration, translation, recitation, and mushaf rendering may contain errors, and releases are corrected over time. **Anyone publishing Quranic text to end users is responsible for verifying it against an authorised printed mushaf and for tracking our corrections.** We are not responsible for errors introduced downstream, nor for releases that something newer has since replaced.

Corrections and error reports are welcome at <corrections@quran.ws> and are treated as a priority.

## Contributions

Unless a contributor states otherwise in writing, contributions are offered under the same licence that applies to the material being contributed: **MIT** for code, **CC BY 4.0** for data and content. Contributors confirm that they hold the necessary rights in what they submit.

## Purpose of the waqf and adab of use

This work is a waqf for the sake of Allah, given seeking His pleasure and hoping for its reward through the benefit people draw from it in what we believe to be good.

The use intended by this waqf is the use that accords with the teachings of Islam, and we do not intend this work to be used in ways contrary to that.

That includes disrespect towards the Quran, deliberate distortion of it or misrepresentation concerning it, and using this work to promote what we believe contradicts the teachings of Islam as understood by **Ahl al-Sunnah wa al-Jama'ah**.

Whoever directs it to such use has stepped outside the purpose for which it was endowed, and carries that before God.

This is our purpose in giving and endowing this work, and the legal terms of its use remain governed by the licence that applies to it, which stays standard and unmodified.

## What checks this policy

Most of this page is policy that no tool can check; a person reviews it at each
release. The two rules that are checked automatically are in the test table of
[Repositories and releases](/guidelines/en/repositories/): every `dataset`
carries a `license` field in its manifest, and every top-level directory is
named in `LICENSE`.

## Final provisions

Where this policy and the text of the MIT License or CC BY 4.0 differ, **the licence text governs**, except for the additional permission above, which grants more than the licence requires.

This policy is published in Arabic and English. Where the two differ, the **Arabic** version governs.

Questions about licensing: <legal@quran.ws>
