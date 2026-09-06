---
title: Writing a guide
description: How pages in this repository are written, and what checks that they are.
status: draft
sidebar:
  order: 2
---

Readers arrive with a question. A good page answers it in the first line, then explains.

## 1. Write for a developer, not a scholar

Most readers are developers building Quran applications. Many don't read Arabic
well, and most have never studied qira'at, tajwid, or ḍabṭ.

Keep the language plain:

```text
Yes:  A code name must stay stable; being familiar is not its job.
No:   Its requirement is stability, not familiarity.

Yes:  A copied table goes stale and nobody notices.
No:   A duplicated table silently falls into desuetude.
```

- Keep a connected thought in one sentence; don't chop it up for emphasis.
- Say it plainly instead of turning it into a slogan or a neat contrast.
- Prefer the familiar word when two are equally correct.
- Use the direct verb: "the file is generated", not "generation of the file takes place".
- Write numbers as digits in technical prose: 4, not four. Ranges use an en dash: 4–8.
- Define a scholarly or Quranic-sciences term the first time, or link it to the dictionary.
- Don't assume the reader knows a riwayah from a qira'ah, or rasm from ḍabṭ.

Plain in style, not in accuracy. The content stays exact.

## 2. Short, direct sentences

Don't pack several abstract ideas into one sentence. Name the idea, list its
parts, then state the conclusion.

```text
Avoid:  Naming has four requirements that conflict: a stable identifier, a
        familiar label, a faithful rendering of the sound, and a search
        target; no single name serves them, so each is given its own field.

Use:    Naming needs four different things: a stable identifier in code, a
        clear label for the reader, an accurate way to write the
        pronunciation, and a value suited to search. One name cannot serve
        all of these, so we give each one its own field.
```

Also avoid heavy noun phrases, inverted word order where plain order is
clearer, and formal verbs where an ordinary one works.

## 3. Write the standard, not the road to it

Readers want the rule, not how we arrived at it. State what is settled and
leave the arguments, the measurements and the rejected alternatives in the
commit log and the issues.

```text
Avoid:  The difference is deliberate. Measurement shows the first form is
        used four times as often... and had we put the familiar form in
        code, the derivation rule would collapse...

Use:    `code` and `display` may differ, and that is deliberate. `code` is
        derived; `display` is measured.
```

Where a rule needs a reason, give it one line, and put the evidence in the
field made for it, such as `display_evidence`.

## 4. Define a field in full sentences

When documenting a field or an option, follow one order: **what it is → what we
use it for → the rule that matters**. Start with a clear verb and a visible
subject. Don't compress the definition, the derivation, the exception and the
rationale into one sentence.

```text
Avoid:  `code` an identifier used in code, APIs and databases. Derived by
        sections 4 to 8 without exception, and what matters is that it stays
        stable even if unfamiliar.

Use:    `code` is the stable identifier used in code, APIs and databases. We
        generate it by the rules in sections 4 to 8, and don't change it later
        just because a more common spelling exists.
```

Also avoid: passive vagueness ("is taken from", "is recorded in"), emphasis
inside a definition ("without exception" — make it a separate rule), pronouns
whose referent isn't immediately visible, and defining a field by contrasting
it with another instead of saying what it holds.

A table is the wrong shape for field definitions: a narrow cell forces the
fragment. Tables compare; sentences define.

## 5. Don't build parallel sentences for their own sake

Explain a relationship the way people normally explain it. Don't force an idea
into a symmetrical shape or repeat a structure for effect.

```text
Avoid:  Every concept has several names, and every name has its field.
Use:    We use several fields to hold a concept's different names.
```

Headings follow the same rule: "Give each page a single purpose" is clearer
than "One page, one purpose".

## 6. State a requirement or a capability, never both at once

This is the commonest fault in standards writing. "must be able to" mixes
describing what something can do with requiring that it do it, and the reader
can't tell which was meant:

```text
Avoid:        The system must be able to display the ayah.
Capability:   The system can display the ayah.
Requirement:  The system must display the ayah.
```

The same goes for "should be capable of" and "is required to". Name the action.

## 7. Arabic-specific rules

The Arabic page carries rules that have no English equivalent: joining list
items with و rather than commas, not attaching several coordinated nouns to one
possessive, and a table of errors common in Arabic technical prose (حيث إن not
حيث أن، أثر في not أثر على، دون not بدون). Note also that Arabic **letter
names** are written as they are said — `noon_sakinah`, not `nun_sakinah` —
which the terminology standard covers in section 6. See
[كيف تكتب دليلًا](/guidelines/ar/01-intro/writing-guides/), section 3 and 4.

Reference: [دليل التحرير والصياغة العربية](https://github.com/kamalyaser31/arabic-guide),
drawn from the Saudi Aramco Arabic style guide.

## 8. Lead with the rule

Put the rule in the first line under the heading, not in the last paragraph.
Never make the reader infer it.

```text
Yes:  A ta marbutah gives h at the end of a name and t in a construct,
      because it is pronounced as a t when the word is bound to the next.

No:   Considering the transliteration of ta marbutah, we find that...
      and therefore it is preferable to write h in one case and t in another.
```

## 9. Explain why only when the reason changes what someone does

Don't justify every rule. Give the reason when it:

- prevents a recurring mistake,
- shows when an exception is allowed,
- explains a rule that looks surprising.

A clear rule stands on its own. Explaining what needs no explanation buries what does.

## 10. State the page's status

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

## 11. Never copy a source of truth

`standards/` is the source; `content/` explains it. Anything generated is never
written by hand:

| Don't write in a page | Link to |
| --- | --- |
| A terminology table | `standards/terminology/concepts/` |
| A list of alternative spellings | `standards/terminology/aliases.json` |
| Unicode properties of a character | generated from the Unicode database |
| The list of Mushaf marks | `standards/terminology/data/dabt_marks.tsv` |

A copied table goes stale and nobody notices, and the reader can't tell which
copy is right.

## 12. A rule that can't be checked can't be enforced

This is the most important rule here. If you write a rule, write the thing that
catches its violation:

| Rule | What checks it |
| --- | --- |
| Spelling rules, sections 4–8 | `tools/test_translit.py` — 49 golden cases |
| Entry structure | `tools/validate.py` against `schema.json` |
| Display names follow usage | `tools/measure_display.py`, evidence recorded in the entry |
| No two concepts share a name | `tools/build_aliases.py` fails on a clash |

Where a rule genuinely can't be automated, give the counter-example outright:

```text
Instead of:  Use clear names.
Write:       Don't abbreviate unless the abbreviation is standard:
             surah not srh, ayah not ay.
```

## 13. Use one name for each concept

Use the name in the [dictionary](../03-terminology/dictionary.md), and don't
vary it for variety. If you need a term that isn't there, add it to the
dictionary before using it in a page.

Write Arabic terms vocalized when the vocalization is part of the point:

```text
Yes:  الوَقْف اللَّازِم    (when discussing how the name is derived)
No:   الوقف اللازم
```

## 14. Arabic and English

`content/ar` and `content/en` mirror each other file for file.

- Arabic is the source for Quranic-text and terminology pages.
- English is the source for engineering pages.
- A page in one language only is **a known gap**, not a different structure.
- A translation carries the same rule. If the two versions state different
  rules, that's an error to fix, not a difference of translation.

## 15. Quranic text in a page

- Quote only as much as the example needs.
- Write it in full Uthmani rasm; never strip the ḍabṭ to save space.
- Give the location: `(2:2)`.
- If the point is a mark, show the mark rather than only naming it:

```text
Yes:  The compulsory-stop mark: ۘ
No:   The compulsory-stop mark is a small mim.
```

## 16. Show what is better seen

Pick the form from the information:

| Information | Form |
| --- | --- |
| A rule with cases | table |
| A derived name | the derivation, run through the tool |
| A mark or character | the character itself, with its codepoint |
| Right versus wrong | one block showing both |
| Steps to perform | numbered list |

## 17. Give each page a single purpose

- The title says what the reader will find: "Writing a guide", not "Writing".
- If a page grew long because it covers two subjects, split it.
- A subheading exists so a reader can find their place, not to break up text.

## Before you publish

- [ ] Plain language; no scholarly term left undefined or unlinked.
- [ ] Short sentences; no heavy noun phrases.
- [ ] Each field defined in sentences: what it is, what it's for, the rule.
- [ ] No parallel constructions or slogan-shaped headings.
- [ ] States the standard, not how it was reached.
- [ ] No "must be able to" — say what is required or what is possible.
- [ ] The rule is in the first line, not the last paragraph.
- [ ] `status` is right, and nothing is `adopted` without a source.
- [ ] No table copied from something `standards/` can generate.
- [ ] Every rule has a check, or an explicit counter-example.
- [ ] Terms come from the dictionary, vocalized where it matters.
- [ ] The mirror page in the other language is updated, or the gap is stated.
- [ ] `python3 tools/validate.py` passes if the page touches terminology.
