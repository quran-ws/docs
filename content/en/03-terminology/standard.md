---
title: Terminology Standard
description: One canonical name per concept, and a code spelling that is derived rather than chosen.
status: draft
sidebar:
  order: 1
---

A standard for naming and defining the concepts used in Quranic software, so that
the names are clear, precise, stable and predictable, and can be used consistently in:

- Code
- APIs
- Databases
- Datasets
- Packages
- Documentation

The underlying idea comes from **Convention over Configuration**:

> Once a developer knows the rules, they can predict the name of a concept, a
> relationship or a field, and how it is used, without going back to the
> documentation each time.

---

## Concept before name

Settle the concept first, then choose its name.

Before adopting a term, decide:

- What does it represent?
- What are its boundaries?
- What does it exclude?
- Does it differ from a neighbouring concept?
- Why does software need to model it?

The starting question is not:

> How do we translate this word?

It is:

> What concept are we modelling?

The name follows from the answer.

---

## One canonical name per concept

Every concept has one standard name in code:

**Canonical Name**

This is the name to use by default across projects that follow the standard.

For example:

```text
Surah
Ayah
Word
Mushaf
Tajwid
```

Other names, spellings and translations are recorded, but they do not compete
with the canonical name.

The rule:

> **One concept, one canonical name.**

---

## When do we keep the Arabic term?

Keep the Arabic term when it carries a Quranic or scholarly concept, and
replacing it with an ordinary English word would lose precision or the identity
of the concept.

For example:

```text
Surah
Ayah
Mushaf
Juz
Hizb
Qiraah
Riwayah
Tajwid
Tafsir
```

For general concepts that already have clear English technical names, use
natural English:

```text
Word
Letter
Page
Line
Root
Translation
Glyph
```

So we prefer:

```text
Surah → Ayah → Word
```

over:

```text
Chapter → Verse → Word
```

and over:

```text
Surah → Ayah → Kalimah
```

A concept having an Arabic name does not make transliterating it the better
choice.

### The same rule inside a compound name

A compound name can join a technical word to an ordinary one. The technical word
is transliterated and the ordinary one is translated:

```text
المِيم الصَّغِيرَة    → small_meem        not meem_saghirah
الصِّفْر المُسْتَدِير → rounded_zero      not sifr_mustadir
الثَّلَاث نُقَط      → three_dots        not thalath_nuqat
الأَلِف المَحْذُوفَة  → omitted_alif      not alif_mahdhufah
```

`saghirah` adds nothing to `small`, and a reader of either language loses by it.

A translated adjective moves in front of its noun, because that is English word
order.

A technical word stays transliterated, however ordinary it looks:

```text
النُّون السَّاكِنَة  → noon_sakinah    `sakinah` is a term of tajwid
الوَقْف اللَّازِم    → waqf_lazim      `lazim` is a term of waqf
```

The ordinary words are listed in
`standards/terminology/data/general_words.tsv`, and are translated wherever they
appear.

The rule:

> **Quran-specific concepts retain Quranic names; general concepts use natural
> technical English.**

---

## Canonical Code Spelling

Once we decide to use a term of Arabic origin, the standard fixes one spelling
for it in code:

**Canonical Code Spelling**

The goal is not a precise transliteration system such as ALA-LC or DIN 31635.
It is a simple, stable spelling that a developer can predict.

### General rules

- ASCII-friendly.
- No precise transliteration marks: `ā`, `ī`, `ū`, `ʿ`, `ʾ`.
- No `'` standing for hamzah or ayn.
- One adopted spelling per term.
- Other common spellings are recorded in `alternative_spellings`.

### How the spelling is derived

Sections 4 to 8 are mechanical rules, so a program can apply them. The Canonical
Code Spelling is derived from the vocalized Arabic name by one function, rather
than being left to each project's judgement.

```bash
python3 tools/translit.py "سُورَة" "رُبْع الحِزْب"
سُورَة        surah          Surah
رُبْع الحِزْب   rubu_al_hizb   Rubu al-Hizb
```

- The input is **vocalized**. Short vowels cannot be recovered from bare Arabic,
  and guessing them is the judgement call this is meant to remove. An unmarked
  alif al-wasl is refused rather than guessed: `اِسْتِعَاذَة` gives `istiadhah`,
  while `استعاذة` is rejected.
- The function is **not reversible**, by design. Emphatic letters and their
  plain counterparts give the same Latin letter — `ص` and `س` are both `s`. The
  aim is a stable identifier, not an accurate pronunciation.
- Every Arabic-derived term in the dictionary has a case in
  `tools/test_translit.py`. When a spelling rule changes, that file shows which
  names change with it.

For example:

```text
Qiraah
Ruku
Irab
Istiadhah
```

rather than:

```text
Qira'ah
Rukūʿ
I'rab
Istiʿādhah
```

---

## Ta marbutah

A singular Arabic term ending in ta marbutah ends in `h`:

```text
سورة   → Surah
آية    → Ayah
رواية  → Riwayah
قراءة  → Qiraah
بسملة  → Basmalah
```

So:

```text
Surah     not Sura
Ayah      not Aya
Riwayah   not Riwaya
```

The other forms are recorded as alternative spellings.

### Ta marbutah in a construct

A ta marbutah is pronounced as a `t` when the word is bound to the one after it,
so it is written `t`:

```text
همزة الوصل    → hamzat_al_wasl     not hamzah_al_wasl
سجدة التلاوة  → sajdat_al_tilawah  not sajdah_al_tilawah
```

The rule is mechanical: a ta marbutah at the end of a term gives `h`, and
anywhere else gives `t`. `tools/test_translit.py` checks it.

---

## Long vowels

The Canonical Code Spelling does not double English letters to show the length
of an Arabic long vowel.

In general:

```text
ا / ى → a
ي     → i
و     → u
```

and not:

```text
aa
ee
oo
```

So:

```text
Tajwid
Tafsir
Tariq
Nuzul
Tahqiq
Tadwir
```

and not:

```text
Tajweed
Tafseer
Tareeq
Nuzool
Tahqeeq
Tadweer
```

These forms are not necessarily wrong in general use, but they are not the
canonical spelling in this standard.

### The nisba ya

A doubled ya at the end of a nisba gives a single `i`:

```text
مكي     → Makki      not Makkiyy
مدني    → Madani     not Madaniyy
عثماني  → Uthmani    not Uthmaniyy
```

### Letter names are written as they are said

The name of a letter is written as it is pronounced, because a letter name is
its sound:

```text
نُون   → noon      not nun
مِيم   → meem      not mim
سِين   → seen      not sin
جِيم   → jeem      not jim
يَاء   → yaa       not ya
```

**This applies to letter names only.** Every other term is derived by sections 4
to 8:

```text
small_noon         a letter name, written as said
seen_al_qiraah     a letter name
tajwid             not a letter name, so derived (not tajweed)
haqiqi             not a letter name, so derived (not haqeeqi)
makki              not a letter name, so derived (not makkee)
```

The 28 letter names are in `standards/terminology/data/letter_names.tsv`, and
the function reads them from there. The reason is that a letter name carries no
meaning beyond its sound; the exception and the measurement behind it are in the
[decision record](/guidelines/en/03-terminology/decisions/).

### `tajwid` is written by the rule

`code` holds `tajwid` even though `tajweed` is the commoner spelling, because
one steady rule is worth more than an exception that opens a door for every
word.

The dominant spelling is not lost, because each concept has two name fields:

```text
code     tajwid     derived by the rule; what is written in code
display  Tajweed    measured from use; what a reader sees
```

`tajweed` is also recorded in `alternative_spellings`, so search and lookup find
it.

> **Unresolved:** `ت` and `ط` both give `taa`, and `ح` and `ه` both give `haa`,
> because section 4 deliberately merges emphatic and plain letters. Neither is
> used as a name in any entry today, so the clash is recorded and left
> unresolved. `tools/build_aliases.py` fails if two concepts claim one name.

---

## Hamzah and ayn

Hamzah and ayn are not represented by any special mark inside code names.

We use:

```text
Qiraah
Irab
Istiadhah
Ruku
```

and not:

```text
Qira'ah
I'rab
Isti'adhah
Ruku'
```

A more precise transliteration can be used in display or in scholarly content
where it is needed.

### Hamzah and ayn at the end of a word

Deleting them at the end of a word cuts the word short: `ربع` becomes `rub` and
`جمع` becomes `jam`, which are unrelated English words.

So when a hamzah or ayn falls at the end of a word and the letter before it has
no vowel of its own, the preceding vowel is repeated:

```text
رُبْع    → rubu
جَمْع    → jama
قَطْع    → qata
الرَّفْع → rafa
```

When a long vowel comes before it, the word already ends in a vowel and nothing
is added:

```text
الرُّكُوع  → ruku
المَمْنُوع → mamnu
المُقَطَّع → muqatta
مَوْضِع    → mawdi
```

A hamzah or ayn inside a word is dropped as described above, and its own vowel
remains: `muallim`, `qiraah`. Each of these cases has a case in
`tools/test_translit.py`.

### Established names

A few names have settled on one form across Quranic software, so deriving a
different one would be correct and useless. `juz` is one: the derivation gives
`juzu`, and use gives `juz` by a wide margin.

These are recorded in `standards/terminology/data/established_spellings.tsv`. A
row is accepted only with a measurement showing that the derived form is
effectively unused, and a term whose usage merely leans one way does not
qualify — otherwise `tajweed` would qualify. The measurements behind both cases
are in the [decision record](/guidelines/en/03-terminology/decisions/).

---

## Compound names and `al-`

For a compound Arabic term we use one steady form:

```text
Rubu al-Hizb
Asbab al-Nuzul
Sujud al-Tilawah
```

`al-` is not assimilated to a sun letter for the canonical spelling.

In identifiers:

```text
rubu_al_hizb
asbab_al_nuzul
sujud_al_tilawah
```

### When is `al` dropped?

`al` is part of the name in a construct only. It is dropped in two cases.

**A leading definite article** is not part of the code name:

```text
الفتحة   → fathah      not al_fathah
السكون   → sukun       not al_sukun
```

**The article on an adjective** is not part of it either. When the noun is
definite and the word after it is definite, the two are one name rather than a
construct:

```text
الوقف اللازم     → waqf_lazim      not waqf_al_lazim
النون الساكنة    → noon_sakinah    not noon_al_sakinah
الرسم العثماني   → rasm_uthmani    not rasm_al_uthmani
```

Telling the two apart is mechanical. If the first word carries `ال`, what
follows is an adjective and its article is dropped. If the first word is
indefinite, what follows is a construct and its `al` stays:

```text
رُبْع الحِزْب      → rubu_al_hizb   (first word indefinite, so a construct)
الوَقْف اللَّازِم   → waqf_lazim     (first word definite, so an adjective)
```

---

## Code name and display name

The code name does not have to be the precise transliteration.

It can be:

```text
Code:     qiraah
Display:  Qirāʾah
Arabic:   قراءة
```

The Canonical Code Spelling stays stable, while the display form can vary by
language, audience and context.

### Name fields

We use several fields to hold the different names of a concept:

```yaml
names:
  code:            noon_sakinah
  display:         Noon Sakinah
  transliteration: nūn sākinah
  arabic:
    vocalized:     النُّون السَّاكِنَة
  dabt:            النُّون السَّاكِنَة
  by_shape:        نُون بِلَا حَرَكَة
  mushaf_introduction: null
  unicode:         ARABIC LETTER NOON
alternative_spellings:
  - nun_sakinah
  - noon_saakinah
```

#### The fields

**`code`** is the stable identifier used in code, APIs and databases. It is
generated by the rules in sections 4 to 8, and is not changed later merely
because another name is more common.

**`display`** is the name shown to a reader in documentation and interfaces. We
choose the most common English spelling and record where that came from in
`display_evidence`.

**`transliteration`** is the precise Latin transliteration, in ALA-LC or DIN
31635. It is optional, and written only where it is needed.

**`arabic.vocalized`** is the Arabic name written with its vowel marks. `code`
is derived from it, and cannot be derived without it.

It is the name we give the concept, and it can differ from the name a source
gives it. The source's name is kept in `dabt` or in `mushaf_introduction`, so
nothing is lost.

`arabic.vocalized` is not edited to reach a preferred code name. Editing it
changes the Arabic name itself, and is accepted only on Arabic grounds: that the
new name fits the boundaries of the concept better. `division_mark` is the
example — the mark shows the start of a juz, a hizb, and their halves and
quarters, so التقسيم covers what التحزيب leaves out.

**`dabt`** is the name of the mark in the science of ḍabṭ, copied as its source
gives it.

**`by_shape`** describes the mark as it is drawn in the mushaf, copied as its
source gives it.

**`mushaf_introduction`** is the name the mushaf's own introduction gives the
mark. We write `null` when the introduction names no mark, which is a fact about
the source.

**`unicode`** is the character's name in Unicode. We read it from the Unicode
database, and do not use it as an identifier in code.

**`alternative_spellings`** holds the known alternative spellings. We use them
in search, and to resolve different inputs to the same concept.

#### Fixed rules

- `code` and `display` may differ, and that is intended.
- A Unicode name is not used as an identifier in code: it describes the shape of
  a character rather than its function, and one character can serve two
  different marks.
- An empty `mushaf_introduction` is a fact about the source, not a gap in the
  entry.

---

## The shape of names in code

Use clear, complete names:

```text
surah
ayah
word
translation
```

Avoid unfamiliar abbreviations:

```text
srh
ay
wrd
trans
```

Avoid vague words when a more precise name exists:

```text
data
info
item
object
value
```

Avoid `type` when the classification itself can be named more precisely.

---

## Singular and plural

Use:

- The singular for one thing.
- The plural for a collection.

For example:

```text
Ayah    → Ayahs
Surah   → Surahs
Mushaf  → Mushafs
Riwayah → Riwayahs
```

Plurals in code follow a simple English convention:

```text
ayahs
surahs
juzs
hizbs
```

Arabic plurals are not used as collection names:

```text
ayat
suwar
ajza
ahzab
```

The Arabic plural can be recorded in the dictionary as linguistic information.

`tools/check_conformance.py` checks that a plural is the code name plus s.

---

## Every entry has a kind

Not every term is the same sort of thing.

Each entry is given its structural role, from a **closed** list. The list lives
in `standards/terminology/schema.json` and is checked by `tools/validate.py`:

```text
entity                 has an identity of its own
concept                represented, but not stored as an entity
classification         a classification that has values
classification_value   one value of a classification
property               a property of an entity
role                   a role a person fills
process                an operation applied to the text
content                content attached to the text
analysis               an analysis derived from the text
mark                   a mark drawn in the mushaf
unit                   a textual, orthographic or typographic unit
```

### Every mark belongs to a family

The marks of ḍabṭ are not one list. Each mark belongs to a family, and that
family is its parent:

```text
mushaf_mark
├── harakah            fathah, dammah, kasrah, sukun, shaddah
├── tanwin             tanwin al-damm, al-fath, al-kasr
├── ijam               dot, two_dots, three_dots
├── orthographic_mark  hamzah, maddah, the small letters
├── qiraah_mark        saktah, ishmam, tashil, imalah
└── waqf_mark_type     lazim, mamnu, and the permissible kinds
```

`mushaf_mark` is not made the parent of every mark: one parent over 37 marks
says nothing. It stays the parent of the marks that have no
family.

---

`kind` describes the **shape** of an entry rather than its domain; the domain is
carried by `category` alone. So kinds such as `textual_concept`,
`recitation_concept` or `typographic_unit` do not arise: those are all `concept`
or `unit`, differing in `category` rather than in `kind`.

Each entry has exactly one `kind`.

For example:

```text
Ayah                       → entity
Tajwid                     → concept
Translation                → content
Reciter                    → role
Revelation Order           → property
Revelation Classification  → classification
Makki                      → classification_value
Waqf Mark                  → mark
Glyph                      → unit
Irab                       → analysis
```

Do not treat all of these as one flat list of "terms".

---

## Types and values get their own entries

When a concept has types or values that matter, defining the parent is not
enough.

The types and values get entries of their own in the dictionary.

For example:

```text
Revelation Classification
├── Makki
├── Madani
└── Disputed
```

and:

```text
Recitation Style
├── Murattal
├── Mujawwad
└── Muallim
```

and:

```text
Ayah Numbering System
├── Madani Awwal
├── Madani Akhir
├── Makki
├── Basri
├── Dimashqi
└── Kufi
```

and:

```text
Recitation Pace
├── Tahqiq
├── Tadwir
└── Hadr
```

and:

```text
Waqf Type
├── Mandatory Waqf
├── Prohibited Waqf
├── Permissible Waqf
├── Continuation Preferred
├── Waqf Preferred
└── Interchangeable Waqf
```

Each of these values gets its own entry, even when it is represented in code as
an enum value.

### Members of a closed set go to a registry

A type is not the same thing as a member.

`Revelation Classification` has three values, and each of them is a concept: a
reader can ask what `Makki` means and get an answer that is not a list. But
`Qiraah` does not have values in that sense. It has 10 members, and Hafs is
not a concept — he is a person. Asking what Hafs *means* has no answer beyond
pointing at him.

So a closed set of members does not become entries. It becomes a registry, one
tab-separated file per set in `standards/terminology/registries/`:

```text
Qiraah          → registries/qiraat.tsv        10 readings, 19 ruwat, 20 riwayat
Surah           → registries/surahs.tsv        114 surahs
Mawdi al-Sajdah → registries/sajdah.tsv        15 places
```

The concept keeps its entry and names its registry:

```yaml
concept: qiraah
kind: concept
registry: qiraat
```

The test is whether a member has anything to say for itself. If it needs a
definition, a purpose and boundaries, it is a concept and it gets an entry. If
everything true of it is its name, its place in the set and where it is
attested, it is a member and it gets a row. The 28 letter names went to
`data/letter_names.tsv` for this reason long before there were registries.

A registry is not a lesser thing than an entry. Every row is checked by
`tools/check_registries.py`, cites a source the way an entry does, and is
indexed so that every spelling of a member resolves.

### A person's name is not derived

Sections 4 to 8 derive a code name from vocalized Arabic, and every term in the
dictionary goes through them. A person's name does not.

The derivation exists because a term is a word carrying a meaning, and working
from the Arabic keeps that meaning attached to the identifier. A name carries no
meaning to keep, so deriving it only produces a spelling nobody writes.

So the name of a reciter is written the way it is commonly written. The
exception covers people and nothing else. A surah name is a word, so it is
derived — `fatihah`, `baqarah`, `nisa` — and `tools/check_registries.py`
re-derives all 114 on every run.

"Commonly written" still has to be evidence rather than preference. The
registry records the scholarly English form with its diacritics, and the name
in use is that form with the diacritics dropped. Where the two disagree over
something the standard already rules on, the standard wins: `shubah`, not
`shuba`, because section 5 governs a ta marbutah.

### A member's name may repeat a concept's

A member may carry the name of a concept, and neither name is changed. Hamzah is
a reciter, and `hamzah` is also the mark. Al-Tariq is a surah, and a `tariq` is a
step in a chain of transmission.

The reason the repetition is harmless is that the two live in different
domains, in the sense of section 25. One `hamzah` is `dabt` and the other is
`qiraat`; one `tariq` is `qiraat` and the other is `structure`. Nothing can
reach for both at once, so nothing has to choose between them. A name is only
required to be unique where it could actually be confused.

The index is keyed by kind rather than by domain, because that is the finer of
the two and it is what a caller knows: a column does not hold "something from
the qiraat domain", it holds a riwayah.

So member names are indexed by kind rather than in one flat namespace:

```text
hamzah          → the mark
qiraah:hamzah   → the reciter
tariq           → the step in the chain
surah:tariq     → the surah
```

The bare name always belongs to the concept. Anything filling a known column —
and a caller always knows which column it is filling — asks inside that
namespace. `aliases.json` stays as it is, for concepts; `registry_aliases.json`
holds the members.

---

## Parent and child

When a concept sits inside a taxonomy, its relation to the parent is stated.

For example:

```yaml
concept: makki
kind: classification_value
parent: revelation_classification
```

or:

```yaml
concept: murattal
kind: classification_value
parent: recitation_style
```

The point is that a developer knows not only what `Makki` means, but also:

> Makki is a kind of what?

### A value's name is derived from its parent's

The name of a value is the parent's name plus the words that distinguish it.
Connecting and emphasising words (`مع`, `كون`, `جوازًا`, `بحيث`) are dropped,
because they distinguish nothing:

```text
علامة الوقف الجائز مع كون الوصل أولى  → waqf_jaiz_wasl_awla
علامة الوقف الجائز مع كون الوقف أولى  → waqf_jaiz_waqf_awla
علامة الوقف اللازم                    → waqf_lazim
```

The parent's name is not repeated when it distinguishes nothing, so the values
of `revelation_classification` stay `makki` and `madani` rather than
`revelation_classification_makki`.

`tools/check_conformance.py` checks that every classification has values.

---

## Definition

Every entry has a `definition`.

The definition answers:

> **What is this concept?**

It should:

- Define the concept itself.
- Be precise and brief.
- State its boundaries where that is needed.
- Avoid defining the name by the name.
- Contain no implementation detail.
- Rest on a suitable source when the concept is a scholarly or technical one.

For example:

```yaml
concept: ayah

definition: >
  A unit of the Quranic text that falls within a surah and has defined
  boundaries; its number, and some of its boundaries, can differ between
  ayah-numbering systems.
```

and not:

```text
Ayah: A Quranic verse.
```

---

## Purpose

Every entry also has a `purpose`.

The purpose answers:

> **Why does Quranic software need this concept?**

It explains:

- Its role in the software model.
- What we use to represent or link it.
- Why a developer needs to tell it apart from its neighbours.

For example:

```yaml
concept: ayah

purpose: >
  Used as the basic unit for referring to the Quranic text, and for linking
  translations, tafsir, recitations, analyses and other data to a specific
  place in the Quran.
```

### The difference

```text
Definition → What is it?
Purpose    → Why do we model it?
```

`purpose` does not restate `definition`.

Details of software use do not go inside `definition`.

If a concept has no clear purpose in software, that is a reason to review
whether it belongs in the core dictionary.

---

## The boundaries of a concept

Where there is a real chance of confusion, the definition or a separate field
states what the concept excludes.

For example:

```text
Mushaf ≠ Quran
Word ≠ Token
Letter ≠ Character
Glyph ≠ Character
Rawi ≠ Reciter
Tajwid ≠ Mujawwad
Tartil ≠ Murattal
Sujud al-Tilawah ≠ Sajdah Mark
```

The aim is not only to document a difference in language, but to stop one name
standing for two different concepts in data and in code.

---

## Similar concepts stay separate

Two concepts are not merged because their translations look alike.

### A mark and what it marks

A mark drawn in the mushaf is a separate concept from what it indicates:

```text
saktah_mark        the mark that is drawn      mark
saktah             the pause itself            concept

sajdah_mark        the mark of a sajdah place  mark
mawdi_al_sajdah    the place itself            concept
sujud_al_tilawah   the prostration itself      concept

ayah_mark          the mark that is drawn      mark
fasilah            the ayah's ending           concept
```

The sajdah is three concepts, not one: a mark, a place in the text, and an act.
Collapsing them puts a page number on a prostration.

### A mark's identity is not its character

A codepoint does not work as the identifier of a mark, for two reasons fixed in
Unicode.

**One character serves two marks**, and the mark is determined by the character
together with its position:

```text
U+06DC   ARABIC SMALL HIGH SEEN   →  saktah_mark  or  seen_al_qiraah
U+06EC   ROUNDED HIGH STOP        →  al_ishmam       or  al_tashil
```

**One mark has more than one character**:

```text
sukun         U+0652   and U+06E1
tanwin fath   U+064B   and U+08F0
maddah        U+0653   and U+06E4
```

So a codepoint is a property of a mark rather than a key to it.

### Text

```text
Word
Token
Morpheme
Lemma
Root
```

### Digital representation

```text
Letter
Character
Codepoint
Grapheme
Glyph
```

### Quran and mushaf

```text
Quran
Mushaf
```

### Content and presentation

```text
Content:
Surah
Ayah
Word
Text

Presentation:
Page
Line
Layout
Font
Glyph
```

### Text and analysis

```text
Text:
Word

Analysis:
Root
Lemma
Morphology
Irab
```

---

## Name, spelling and translation are not one thing

Keep these apart:

```text
canonical
alternative_spellings
english_glosses
deprecated
```

For example:

```yaml
concept: ayah

canonical: ayah

alternative_spellings:
  - aya

english_glosses:
  - verse
```

`Aya` is an alternative spelling of `Ayah`.

`Verse` is an English gloss, not an alternative spelling.

Likewise:

```yaml
concept: tajwid

canonical: tajwid

alternative_spellings:
  - tajweed
```

`aliases` is not used as a catch-all field mixing different relations together.

`tools/check_conformance.py` checks that a gloss is not also recorded as an
alternative spelling.

---

## Deprecated does not mean incorrect

We distinguish:

#### Alternative

Another correct or common form:

```text
Tajweed → alternative spelling of Tajwid
```

#### Deprecated / discouraged

A name for the concept, but not recommended in new projects.

#### Incorrect

A name that points at a different concept, or carries a wrong meaning.

`Verse` may be a correct English translation of `Ayah`, but it is not the
canonical name in this standard.

---

## Identifiers, numbers and order

Each suffix has one fixed meaning.

### `id`

An internal identifier:

```text
surah_id
ayah_id
word_id
mushaf_id
```

### `number`

An established number within the domain:

```text
surah_number
ayah_number
page_number
```

### `position`

The position of an element within a parent or a sequence:

```text
word_position
token_position
line_position
```

### `order`

A separate meaningful ordering:

```text
revelation_order
display_order
```

Do not use:

```text
id
number
position
order
```

as synonyms.

---

## Relationships

A relationship is named after the concept it links to.

We prefer:

```text
surah.ayahs
ayah.surah
ayah.words
mushaf.pages
page.lines
```

Singular for a to-one relationship, plural for a to-many one.

Do not use procedural names when the relationship is only a data relationship:

```text
getAyahList()
fetchRelatedSurah()
retrieveWords()
```

when:

```text
ayahs
surah
words
```

is enough.

---

## Operations and verbs

We standardise the names of recurring operations, as we do the names of
entities:

```text
normalize
parse
tokenize
segment
transliterate
annotate
render
validate
compare
convert
```

The same verb is used for the same operation.

Avoid:

```text
process
handle
do
```

when a more precise verb exists.

For example:

```text
tokenizeText()
normalizeText()
renderAyah()
validateMushaf()
```

is better than:

```text
processText()
handleAyah()
```

---

## Classifications and booleans

Classifications carry domain-specific names:

```text
Waqf Type
Recitation Style
Recitation Pace
Revelation Classification
Script Type
Annotation Type
```

rather than:

```text
Quran Type
Item Type
Data Type
```

A boolean's name shows that it asks a yes/no question:

```text
has_sajdah
is_active
is_included
```

A multi-valued classification is not modelled as a set of booleans when one
classification is more precise.

---

## Organising the domains

The dictionary is organised by clear domains rather than as one flat list.

These are the adopted domains, and they are also the dictionary's own sections,
so there are never two different lists. They live in
`standards/terminology/schema.json` and are checked by `tools/validate.py`:

```text
core                  the Quran and the mushaf
structure             surah, ayah and word
text                  units of text and its digital representation
divisions             juz, hizb and rubu
surah_classification  tiwal, miun, mathani and mufassal
mushaf                edition, layout, page and rasm
dabt                  ḍabṭ: vowels, tanwin and marks
mushaf_marks          the marks of the mushaf
ayah_numbering        ayah-numbering systems
revelation            revelation, its order and its classification
qiraat                qiraat, riwayat and turuq
recitation            recitation and reciters
recitation_pace       tahqiq, tadwir and hadr
recitation_style      murattal, mujawwad and muallim
tajwid                the rulings of tajwid
waqf                  waqf and its rulings
linguistics           root, lemma, morphology and irab
translation           translation
tafsir                tafsir
quranic_sciences      naskh, gharib al-Quran and mutashabihat
```

A domain is not added before there are concepts that belong to it, because an
empty domain suggests coverage that does not exist.

---

## Consistency across the layers of a system

The same canonical vocabulary is used across the layers of a system as far as
possible.

If we adopt:

```text
Surah
Ayah
Word
```

then the expected result is:

```text
Models:
Surah
Ayah
Word

Database:
surahs
ayahs
words

Foreign keys:
surah_id
ayah_id

API:
/surahs
/surahs/{surah}/ayahs
/ayahs/{ayah}/words
```

Avoid using:

```text
Database: surah
API: chapter
Package: quran_section
```

for one concept.

A user interface can translate or display the name differently, while the
canonical internal vocabulary stays fixed.

---

## The shape of a dictionary entry

The dictionary produced by this standard uses one structure, with a file per
concept.

The minimum:

```yaml
concept:
kind:
category:
origin:
tier:
status:

names:
  code:
  display:

definition:
purpose:
```

Added where needed:

```yaml
parent:          # required when kind is a classification value
plural:
symbol:

names:
  arabic:
  dabt:
  by_shape:
  mushaf_introduction:
  unicode:

unicode:         # generated from the Unicode database, never written by hand
alternative_spellings:
english_glosses:
deprecated:
boundaries:
related:
sources:

definition_en:   # the translation of definition; the English dictionary is generated from it
purpose_en:      # the translation of purpose
boundaries_en:   # the translation of boundaries, line for line
note_en:         # the translation of note
```

**`origin`** says where the concept's name came from. We write `quranic` for a
Quranic or scholarly term, `borrowed` for a general term whose definition is
settled elsewhere, and `standard` for a concept this standard defines for
modelling, with no counterpart in the tradition.

**`tier`** says how much the concept matters in practice. We write `core` for
what applications actually store, and `extended` for a settled concept that is
rarely represented or whose boundaries differ.

**`status`** says where the entry stands. It starts as `draft`, becomes
`proposed` after discussion, then `adopted` once accepted. An entry with no
source is not marked `adopted`.

**`arabic`** is required on every `origin: quranic` entry. A borrowed term is
given its Arabic name when it has a settled one, so that we do not coin new
Arabic terms by accident.

### The entry in two languages

There is one entry, and its prose is in two languages. Every prose field has an
English twin: `definition_en`, `purpose_en`, `boundaries_en` and `note_en`. The
English dictionary page is generated from them, as the Arabic page is generated
from the Arabic fields, so the two pages cannot say different things.

A twin is **a translation, not a second definition**. What one states, the other
states: the English adds no condition and drops none. Boundaries translate line
for line, one English line for each Arabic line, in its place.

Four rules hold in the translation:

- **A term is called by its adopted name**, the `display` in its own entry: Ayah,
  not verse; Mushaf, not codex. The English in `english_glosses` is a search key,
  not a name to write with.
- **A code name is written as it is**, inside backticks, never translated.
- **A repeated formula is translated by a repeated formula**: the six ayah
  numbering entries share one purpose sentence in Arabic, so they share one in
  English, word for word.
- **No Arabic is left in an English field**, except an Arabic name the entry is
  itself talking about, which is written inside «…». `tools/check_conformance.py`
  checks this.

None of this is offered as an approved translation of a religious text. It states
a concept in a second language for whoever builds with it.

Example:

```yaml
concept: waqf_lazim
kind: classification_value
category: waqf
parent: waqf_mark_type
origin: quranic
tier: core
status: draft

names:
  code: waqf_lazim
  display: Waqf Lazim
  arabic: الوَقْف اللَّازِم
  dabt: المِيم — عَلَامَة الوَقْف اللَّازِم
  by_shape: مِيم
  mushaf_introduction: عَلَامَة الوَقْف اللَّازِم
  unicode: ARABIC SMALL HIGH MEEM INITIAL FORM

symbol: ۘ

unicode:
  - cp: "U+06D8"
    name: ARABIC SMALL HIGH MEEM INITIAL FORM
    category: Mn
    combining_class: 230
    block: Arabic
  chart: https://unicode.org/charts/PDF/U0600.pdf

definition: >
  علامة تدل على لزوم الوقف في موضعها، لأن وصل ما بعدها بما قبلها
  يوهم خلاف المعنى المراد.

purpose: >
  تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين
  والتنبيه في التطبيقات بدل قراءة صورة الرمز.

definition_en: >
  A compulsory stop: continuing across it would suggest a meaning other
  than the one intended.

purpose_en: >
  Used as a value of the waqf mark type, so that rendering, instruction and
  warnings in applications branch on it rather than on the shape of the sign.

related:
  - waqf
  - waqf_mark

sources:
  - id: quranpedia_tajweed
    ref: "122"
    url: https://tajweed.quranpedia.net/term/show/122
```

---

## Sources for definitions

Scholarly and technical terms rest on suitable sources.

A source documents **the concept and its definition**, and not necessarily the
choice of name in code.

A source may establish the meaning of `Ayah`, while choosing:

```text
Ayah
```

over:

```text
Verse
```

is a decision made by this standard.

Keep the two apart:

```text
Domain fact          what the source establishes
Standard convention  what this standard decides
```

### Adopted sources

The sources are recorded in `standards/terminology/sources.yml`, each with the
reference form it uses: a page in a book, a term number in a dictionary. They are
not listed again here, so there is only one place to keep them current.

`tools/check_registries.py` checks that every reference names a source that
exists in that file.

An entry with no source establishing its definition is not marked `adopted`.

---

## The dictionary is machine-readable

The primary source of the dictionary is machine-readable, such as YAML or JSON.

From that same source we can generate:

- Documentation
- A terminology website
- API schemas
- IDE hints
- Linters
- Validation rules
- Deprecated-term warnings
- Migration mappings

Human-readable documents are output from that source as far as possible, rather
than a separate copy that is hard to keep in step.

---

## The rule for accepting a new term

### First, is the concept ours to name?

A concept belongs in this standard when **it cannot be defined without
referring to the Quran or the mushaf**.

Everything else an application stores is real, and is not ours:

```text
In scope:
mawdi_al_sajdah   a place in the Quranic text
ayah_timing       a span of audio matched to an ayah
gharib_al_quran   the meaning of a Quranic word
mutashabihat      wordings repeated within the Quran

Out of scope:
book, author, chapter, category, tag, language, attachment, source
radio, stream, thumbnail, user, subscription
fatwa, hadith, athar, topic
```

`radio` fails the test: a stream of Quran audio is a stream, and nothing about
it needs a Quranic definition. `fatwa` fails it the way a hadith does — real,
Islamic, and not a concept of the Quranic text. `book` fails it because the
language already names a book as well as we could.

The standard says so plainly, because a project still needs names for its books
and its tags and this standard does not give them. The reason for the boundary,
and the alternative that was rejected, are in the
[decision record](/guidelines/en/03-terminology/decisions/).

> **We name the Quran's own sciences, and stop there.**

### Then, the entry itself

Before an entry goes into the dictionary, answer:

1. What is the concept?
2. What is its definition?
3. Why does software need to model it?
4. What are its boundaries, and what might it be confused with?
5. What is its `kind`?
6. Which `category` does it belong to?
7. Does it have a `parent`?
8. Is it a Quranic concept or a general technical one?
9. What is the most suitable canonical name?
10. If it is Arabic in origin, does it follow the Canonical Code Spelling?
11. What are its singular and plural in code?
12. What are its alternative spellings?
13. What are its translations or English glosses?
14. Are there deprecated names?
15. Does the name work naturally in code, in an API and in a database?
16. What source establishes the concept's definition?

If we cannot state the concept clearly, or say why software models it, it is not
adopted until the need becomes clear.

---

## The underlying principles

The standard comes down to these:

1. **Concept before name.**
2. **One concept, one canonical name.**
3. **Quran-specific concepts retain Quranic names; general concepts use natural technical English.**
4. **Arabic-derived terms use one simple Canonical Code Spelling.**
5. **Definition explains what the concept is; Purpose explains why software models it.**
6. **Every entry has a defined Kind and Category.**
7. **Important types and values are first-class dictionary entries with their own definitions.**
8. **Parent-child relationships are explicit.**
9. **Different concepts remain different even when their names or translations are similar.**
10. **Canonical names, alternative spellings, translations, and deprecated names are kept separate.**
11. **The same vocabulary is used consistently across code, APIs, databases, datasets, and documentation.**
12. **The dictionary is machine-readable and enforceable.**
