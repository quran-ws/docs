---
title: Decision Record
description: The contested decisions in the terminology standard, with their reasons and evidence.
status: draft
sidebar:
  order: 3
---

The standard states the rule. This page states why the rule is what it is.

They are kept apart because a reader applying the standard wants the rule alone,
while a reader who wants to change it needs what the rule rests on. A rule with
no written reason gets reopened every year.

Only decisions where there was a real disagreement, or a reasonable alternative,
are recorded here.

---

## Letter names are written as they are said

**Decision:** `noon`, `meem`, `seen` — not `nun`, `mim`, `sin`.

**Why:** `nun` and `sin` are English words with a meaning far from the one
intended. And the measurement shows letter names tend toward the doubled form:

```text
noon sakinah   478  ×  nun sakinah   118
meem sakinah   308  ×  mim sakinah    57
```

**The boundary:** letter names only. A letter name carries no meaning beyond its
sound, so deriving it throws away the only thing it has; every other term is a
word with a meaning that the derivation keeps.

**Consequence:** the twenty-eight letter names live in `letter_names.tsv`, and
the function reads them from there.

---

## Long vowels are written short

**Decision:** `tajwid`, `sukun`, `tafsir` — not `tajweed`, `sukoon`, `tafseer`.

**Why:** usage favours the short form for terms:

```text
sukun    289792  ×  sukoon    18432
tafsir   370688  ×  tafseer  115712
tanwin    19968  ×  tanween    4520
tartil    24736  ×  tarteel    7328
```

**Alternative rejected:** doubling everywhere. It contradicts the measurement
for most terms.

---

## `tajwid` goes against its own measurement, and the rule still holds

**Decision:** `code: tajwid`, even though `tajweed` is about twice as common
(45,440 × 25,280).

**Why:** one steady rule is worth more than an exception that opens a door for
every word.

**Nothing is lost:** `display: Tajweed` is measured from use, and `tajweed` is
recorded in `alternative_spellings`.

---

## A word-final ayn or hamzah echoes the vowel before it

**Decision:** `rubu`, `jama`, `qata`, while `ruku` and `mamnu` stay as they are.

**Why:** deleting them cut the word short, giving `rub`, `jam`, `qat` and `bad`
— unrelated English words. This is the same problem that made us write `noon`
rather than `nun`.

**Alternatives rejected:** `'` and `ʿ` do not work in identifiers, and `3` is
not writing.

**The boundary:** after a long vowel the word already ends in a vowel, so
nothing is added.

---

## `juz` is not derived

**Decision:** `juz`, where the derivation gives `juzu`.

**Why:** the derived form is effectively unused:

```text
juz number  1384  ×  juzu number  1
```

**The bar:** a row in `established_spellings.tsv` is accepted only with a
measurement showing the derived form is unused. Usage merely leaning one way is
not enough, or `tajweed` would qualify.

---

## The ordinary word in a compound name is translated

**Decision:** `small_meem`, `three_dots`, `rounded_zero` — not `meem_saghirah`,
`thalath_nuqat`, `sifr_mustadir`.

**Why:** `saghirah` adds nothing to `small`. Section 3 already said a general
concept takes an English name, but it never spoke about compound names, so these
slipped through.

**The evidence:** the source registry itself cites them in English —
`standard!dot`, `standard!two-dots`, `standard!three-dots`.

**The boundary:** a technical word stays transliterated however ordinary it
looks; `sakinah` and `lazim` are terms. The ordinary words are listed in
`general_words.tsv`.

---

## The derived English name matched the hand-written one

**Decision:** word order in a compound follows English — a construct head moves
to the end, an adjective moves in front.

**The evidence:** with the rule applied, the derivation produced the names that
had already been written by hand:

```text
عَلَامَة الوَقْف        → waqf_mark
عَلَامَة السَّجْدَة      → sajdah_mark
نَوْع عَلَامَة الوَقْف   → waqf_mark_type
```

**Consequence:** `general_words.tsv` carries a role column, so a numeral stays
where it stands — `three_dots`, not `dots_three`.

---

## `division_mark`, not `hizb_mark`

**Decision:** `division_mark`.

**Why:** the mark shows the start of a juz, a hizb, and their halves and
quarters, so `hizb_mark` names one of four. The Unicode name
`ARABIC START OF RUB EL HIZB` has the same fault.

**A rule came out of this:** `arabic.vocalized` is not edited to reach a
preferred code name. The source's name is kept in `dabt`, and changing the
concept's name is accepted only on Arabic grounds.

---

## A mark's parent is its family

**Decision:** `harakah`, `tanwin`, `ijam`, `orthographic_mark` and `qiraah_mark`
are parents; `mushaf_mark` stays the parent of what has no family.

**Why:** every mark hung off `mushaf_mark` while `mark_family` carried the real
grouping. The entry held two taxonomies that disagreed, and one parent over
thirty-seven marks says nothing.

---

## Waqf marks are values, not marks

**Decision:** `waqf_lazim` and its siblings are `kind: classification_value`
with `parent: waqf_mark_type`.

**Why:** `waqf_mark_type` was a classification with no values, and section 27
gives `waqf_lazim` exactly this shape. The data contradicted the standard's own
example.

---

## Duplicated concepts are merged

**Decision:** one entry each for `sajdah_mark` and `division_mark`.

**Why:** `alamat_mawdi_al_sajdah` and `sajdah_mark` defined the same thing, as
did `alamat_al_tahzib` and `division_mark`.

**Consequence:** the former name still resolves through `aliases.json`, so a
project that adopted it is not stranded.

---

## A codepoint is not a mark's identity

**Decision:** a codepoint is not used as the identifier of a mark.

**Why:** one character serves two marks, and one mark has more than one
character:

```text
U+06DC   ARABIC SMALL HIGH SEEN   →  saktah_mark  or  seen_al_qiraah
sukun    U+0652  and U+06E1
```

---

## The derivation is not reversible, by design

**Decision:** `ص` and `س` are both `s`; `ض` and `د` are both `d`.

**Why:** the aim is a stable identifier, not an accurate pronunciation. Precise
transliteration belongs in `names.transliteration`.

---

## The dictionary is generated from the entries

**Decision:** the dictionary page is generated from `concepts/*.yml`.

**Why:** it had been written by hand, duplicating the source of truth, which is
what section 29 forbids.
