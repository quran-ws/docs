---
title: Writing style
description: How a sentence is written in this repository.
status: draft
sidebar:
  order: 2
---

Most readers are developers building Quran applications. Many don't read Arabic
well, and most have never studied qira'at, tajwid, or ḍabṭ. Write plainly for
them, and keep the content exact.

This page is about the sentence. What a page must contain and how it is
arranged is in [Writing a guide](./writing-guides/).

## 1. Plain words, ordinary sentences

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
[أسلوب الكتابة العربية](/guidelines/ar/01-intro/writing-style/), sections 7 and 8.

Reference: [دليل التحرير والصياغة العربية](https://github.com/kamalyaser31/arabic-guide),
drawn from the Saudi Aramco Arabic style guide.

## Before you publish

- [ ] Plain language; no scholarly term left undefined or unlinked.
- [ ] Short sentences; no heavy noun phrases.
- [ ] Each field defined in sentences: what it is, what it's for, the rule.
- [ ] No parallel constructions or slogan-shaped headings.
- [ ] States the standard, not how it was reached.
- [ ] No "must be able to" — say what is required or what is possible.
