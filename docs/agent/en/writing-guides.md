---
title: Writing a guide
description: What a page in this repository must contain, and how it is arranged.
status: draft
sidebar:
  order: 3
---

Readers arrive with a question. A good page answers it in the first line, then explains.

Rules for the sentence itself are in [Writing style](https://github.com/quran-ws/docs/blob/main/docs/agent/en/writing-style.md).

## 1. Lead with the rule

Put the rule in the first line under the heading, not in the last paragraph.
Never make the reader infer it.

```text
Yes:  A ta marbutah gives h at the end of a name and t in a construct,
      because it is pronounced as a t when the word is bound to the next.

No:   Considering the transliteration of ta marbutah, we find that...
      and therefore it is preferable to write h in one case and t in another.
```

## 2. Give a reason only when it changes what someone does

Don't justify every rule. Give the reason when it:

- prevents a recurring mistake,
- shows when an exception is allowed,
- explains a rule that looks surprising.

A clear rule needs no reason. Adding one hides the reasons that matter.

## 3. State the page's status

Every page carries `status` in its frontmatter, so nobody has to guess what binds:

```yaml
---
title: A title describing what the reader will find
description: One line
status: draft | proposed | adopted
---
```

- `draft` — being written; don't build on it.
- `proposed` — discussed, awaiting adoption.
- `adopted` — binding on our projects.

Inside a page, mark the difference where it matters:

```markdown
**Required:** every `adopted` entry cites a source for its definition.
**Recommended:** cite the page or term number alongside the source.
```

## 4. Never copy a source of truth

`standards/` is the source; `content/` explains it. Anything generated is never
written by hand:

| Don't write in a page | Link to |
| --- | --- |
| A terminology table | `standards/terminology/concepts/` |
| A list of alternative spellings | `standards/terminology/aliases.json` |
| Unicode properties of a character | generated from the Unicode database |
| The list of mushaf marks | `standards/terminology/data/dabt_marks.tsv` |

A copied table goes stale and nobody notices, and the reader can't tell which
copy is right.

## 5. Give every rule a check

Write, alongside every rule, the thing that catches its violation. This is the
most important rule here, because a rule nobody can test is a rule nobody can be
held to:

| Rule | What checks it |
| --- | --- |
| Spelling rules, §4–§8 | `tools/test_translit.py` — the golden cases |
| Entry structure | `tools/validate.py` against `schema.json` |
| Display names follow usage | `tools/measure_display.py`, evidence recorded in the entry |
| No two concepts share a name | `tools/build_aliases.py` fails on a clash |
| Names in the prose still resolve | `tools/check_examples.py` |
| The examples are canonical and their tests pass | `tools/check_example_files.py` |

Where a rule genuinely can't be automated, give the counter-example outright:

```text
Instead of:  Use clear names.
Write:       Don't abbreviate unless the abbreviation is standard:
             surah not srh, ayah not ay.
```

## 6. Use one name for each concept

Use the name in the [dictionary](/guidelines/en/reference/dictionary/), and don't
vary it for variety. If you need a term that isn't there, add it to the
dictionary before using it in a page.

Write Arabic terms vocalised when the vocalisation is part of the point:

```text
Yes:  الوَقْف اللَّازِم    (when discussing how the name is derived)
No:   الوقف اللازم
```

## 7. Arabic and English

`content/ar` and `content/en` mirror each other file for file.

- Arabic is the source for Quranic-text and terminology pages.
- English is the source for engineering pages.
- A page in one language only is **a known gap**, not a different structure.
- A translation carries the same rule. If the two versions state different
  rules, that's an error to fix, not a difference of translation.

## 8. Quranic text in a page

- Quote only as much as the example needs.
- Write it in full Uthmani rasm; never strip the dabt to save space.
- Give the location: `(2:2)`.
- If the point is a mark, show the mark rather than only naming it:

```text
Yes:  The compulsory-stop mark: ۘ
No:   The compulsory-stop mark is a small mim.
```

## 9. Show what is better seen

Pick the form from the information:

| Information | Form |
| --- | --- |
| A rule with cases | table |
| A derived name | the derivation, run through the tool |
| A mark or character | the character itself, with its codepoint |
| Right versus wrong | one block showing both |
| Steps to perform | numbered list |

## 10. Give each page a single purpose

- The title says what the reader will find: "Writing a guide", not "Writing".
- If a page grew long because it covers two subjects, split it.
- A subheading exists so a reader can find their place, not to break up text.

## Before you publish

- [ ] The rule is in the first line, not the last paragraph.
- [ ] `status` is right, and nothing is `adopted` without a source.
- [ ] No table copied from something `standards/` can generate.
- [ ] Every rule has a check, or an explicit counter-example.
- [ ] Terms come from the dictionary, vocalised where it matters.
- [ ] The mirror page in the other language is updated, or the gap is stated.
- [ ] `python3 tools/build.py` passes.
