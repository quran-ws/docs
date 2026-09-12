---
title: Writing style
description: How a sentence is written in this repository.
status: draft
sidebar:
  order: 2
---

Most readers are developers building Quran applications. Many don't read Arabic
well, and most have never studied qiraat, tajwid or dabt (the marks that vowel
the text). Write plainly for them, and keep the content exact.

This page is about the sentence. What a page must contain and how it is
arranged is in [Writing a guide](https://github.com/quran-ws/docs/blob/main/docs/agent/en/writing-guides.md).

## 1. Use plain words and ordinary sentences

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
- Write a count or a measurement as digits: 10 qiraat, 60 hizbs, 114 surahs; not
  ten, sixty, a hundred and fourteen.
- A small number that is not counting things — "the three may differ", "one name
  cannot serve all four" — stays a word.
- Separate thousands with a comma in prose — 6,236 ayahs — and leave a figure
  inside a code block exactly as the tool printed it. Ranges use an en dash: 4–8.
- Use British spelling: modelling, judgement, normalise. A code identifier keeps
  its own spelling: `normalize`, `tokenization`.
- Define a scholarly or Quranic-sciences term the first time, or link it to the dictionary.
- Don't assume the reader knows a riwayah from a qiraah, or rasm from dabt.

Plain language does not mean loose content. The facts stay exact.

## 2. Short, direct sentences

Don't pack several abstract ideas into one sentence. Name the idea, list its
parts, then state the conclusion.

```text
Avoid:  Naming has 4 requirements that conflict: a stable identifier, a
        familiar label, a faithful rendering of the sound, and a search
        target; no single name serves them, so each is given its own field.

Use:    Naming needs 4 different things: a stable identifier in code, a
        clear label for the reader, an accurate way to write the
        pronunciation, and a value suited to search. One name cannot serve
        all of these, so we give each one its own field.
```

Also avoid heavy noun phrases, inverted word order where plain order is
clearer, and formal verbs where an ordinary one works.

## 3. State the rule, not how it was reached

Readers want the rule, not how we arrived at it. State what is settled and
leave the arguments, the measurements and the rejected alternatives to the
decision record.

```text
Avoid:  The difference is deliberate. Measurement shows the first form is
        used four times as often... and had we put the familiar form in
        code, the derivation rule would collapse...

Use:    `code` and `display` may differ, and that is deliberate. `code` is
        derived; `display` is measured.
```

Where a rule needs a reason, give it one line, and put the evidence in the
field made for it, such as `display_evidence`.

A decision that was genuinely contested is recorded in the
[decision record](/guidelines/en/reference/decisions/) with its reason and
its evidence, because a rule with no written reason gets reopened every year.
The difference is that the record states the decision and why; it does not
narrate how we went back and forth.

A real case taken from a published survey is different: give it a sentence or
two after the rule, because it shows where the mistake actually happens. It is
sourced evidence for the rule, not the story of how the rule was reached.

## 4. Define a field in full sentences

When documenting a field or an option, follow one order: **what it is → what we
use it for → the rule that matters**. Start with a clear verb and a visible
subject. Don't compress the definition, the derivation, the exception and the
rationale into one sentence.

```text
Avoid:  `code` an identifier used in code, APIs and databases. Derived by
        §4–§8 without exception, and what matters is that it stays
        stable even if unfamiliar.

Use:    `code` is the stable identifier used in code, APIs and databases. We
        generate it by the rules in §4–§8, and don't change it later
        just because a more common spelling exists.
```

Also avoid: passive vagueness ("is taken from", "is recorded in"), emphasis
inside a definition ("without exception" — make it a separate rule), pronouns
whose referent isn't immediately visible, and defining a field by contrasting
it with another instead of saying what it holds.

A table is the wrong shape for field definitions: a narrow cell forces the
fragment. Use a table to compare things and a sentence to define one.

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

Say what is required with the verb that requires it, and say what is possible
with "can". This is the commonest fault in standards writing: "must be able to"
mixes describing what something can do with requiring that it do it, and the
reader can't tell which was meant:

```text
Avoid:        The system must be able to display the ayah.
Capability:   The system can display the ayah.
Requirement:  The system must display the ayah.
```

The same goes for "should be capable of" and "is required to". Name the action.

## 7. Write a concept by its code name in prose

In running prose, write a concept the way its `code` is spelt, as a lowercase
common noun: ayah, surah, mushaf, tajwid, waqf lazim, dabt. The `display` form
(Tajweed, Noon Saghirah) is for user interfaces, the `display` field, and entry
headings. Capitalise only at the start of a sentence, in a heading, or in a
proper name: Hafs, al-Tawbah, the Quran.

```text
Avoid:  The Mushaf carries Tajweed colouring on every Ayah.
Use:    The mushaf carries tajwid colouring on every ayah.
```

- Plurals in prose follow the code rule: riwayahs, hizbs, tariqs, rawis. `qiraat`
  is kept only as the name of the discipline.
- It is "numbering system", never "counting system" or "school", for the value;
  "the Basran school" names the transmitters, not the system.
- It is "dabt", not "ḍabṭ"; "codepoint"; "alif". Letter names are written as they
  are said: noon, meem, seen, yaa, saad, haa, baa.
- `al-` is never assimilated to a sun letter: al-Tawbah, not at-Tawbah.

## 8. Don't translate field names or their values

Field names and their values are written in English in the files, so write them
in the page exactly as they appear there, in code font. Translating them cuts
the link between what a reader reads and what they type:

```text
Avoid: | Kind | entity as an independent thing |
Use:   | `kind` | `entity` |
```

Explain what the values mean once, where the standard defines them, rather than
with every entry. The prose around them is written in the page's language.

## 9. Arabic-specific rules

The Arabic page carries rules that have no English equivalent: Western digits
and a tanwin written before its alif (§1); joining list items with و rather than
commas, and not attaching several coordinated nouns to one possessive (§7); one
settled Arabic word per concept, a Latin word set in code marks inside an Arabic
sentence, and the exception for proper names and licence names (§8); and a table
of errors common in Arabic technical prose — حيث إن not حيث أن، أثر في not أثر
على، دون not بدون (§10). See
[أسلوب الكتابة العربية](https://github.com/quran-ws/docs/blob/main/docs/agent/ar/writing-style.md), sections 1, 7, 8
and 10, plus section 11 on writing Arabic that does not read as translated
English and section 12 on the shape of an Arabic heading. Its section 13 points back here, to the rules that apply to English only.

Reference: [دليل التحرير والصياغة العربية](https://github.com/kamalyaser31/arabic-guide),
drawn from the Saudi Aramco Arabic style guide.

## Before you publish

- [ ] Plain language; no scholarly term left undefined or unlinked.
- [ ] Short sentences; no heavy noun phrases.
- [ ] Each field defined in sentences: what it is, what it's for, the rule.
- [ ] No parallel constructions or slogan-shaped headings.
- [ ] States the standard, not how it was reached.
- [ ] No "must be able to" — say what is required or what is possible.
- [ ] Field names and values in English code font, not translated.
- [ ] The rules specific to the other language are checked (§9).
- [ ] British spelling; concepts by their code spelling, lowercase, in prose.
- [ ] Counts as digits, thousands separated in prose; "numbering system", "dabt",
      "alif", letter names as said.
