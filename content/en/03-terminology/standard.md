---
title: Terminology standard
description: One canonical name per concept, and a code spelling that is derived rather than chosen.
status: draft
sidebar:
  order: 1
---

A standard for naming and defining the concepts used in Quranic software, so that
the names are clear, precise, stable and predictable, and can be used consistently in:

- code
- APIs
- databases
- datasets
- packages
- documentation

The underlying idea comes from **convention over configuration**:

> Once a developer knows the rules, they can predict the name of a concept, a
> relationship or a field, and how it is used, without going back to the
> documentation each time.

**At a glance**

1. Settle the concept before its name (§1).
2. One concept, one canonical name; two concepts never share one (§2).
3. A Quranic or scholarly concept keeps its Arabic name; a general concept takes
   its English one, inside a compound name too (§3).
4. The code spelling of an Arabic term is derived from its vocalised name by one
   function, `tools/translit.py`, not chosen (§4–§8).
5. `code` is for identifiers, `display` for readers, `arabic.vocalized` for the
   Arabic reader; the three may differ (§9).
6. Every entry has one `kind` and one `category`; values and types are entries of
   their own, members of a closed set are rows in a registry (§12–§13).
7. `definition` says what a concept is, `purpose` says why software models it,
   `boundaries` say what it excludes (§15–§17).
8. Names, spellings, glosses and deprecated names are separate fields (§19–§20).
9. The same vocabulary runs through code, APIs, databases and documentation (§26).
10. The dictionary is machine-readable, and the rules it states are checked by
    tools (§29).

**Scope.** A concept belongs in this standard when it cannot be defined without
referring to the Quran or the mushaf. Everything else an application stores is
real, and is not named here (§30).

## 1. Concept before name

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

## 2. One canonical name per concept

Every concept has one canonical name: the name used by default in code across
the projects that follow the standard.

For example:

```text
surah
ayah
word
mushaf
tajwid
```

Other names, spellings and translations are recorded, but they do not compete
with the canonical name.

A name belongs to one concept. `tools/build_aliases.py` fails the build when two
entries claim one name, in any of their spellings. The one place a name is shared
is between the values of two classifications, because a column holds the values
of one classification and never two: `makki` is a value of
`revelation_classification` and of `ayah_numbering_system`, and the two entries
have different ids (§14).

The rule:

> **One concept, one canonical name.**

## 3. When to keep the Arabic term

Keep the Arabic term when it carries a Quranic or scholarly concept, and
replacing it with an ordinary English word would lose precision or the identity
of the concept.

For example:

```text
surah
ayah
mushaf
juz
hizb
qiraah
riwayah
tajwid
tafsir
```

For general concepts that already have clear English technical names, use
natural English:

```text
word
letter
page
line
root
translation
glyph
```

So we prefer:

```text
surah → ayah → word
```

over:

```text
chapter → verse → word
```

and over:

```text
surah → ayah → kalimah
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

`saghirah` adds nothing to `small`, and helps a reader of neither language.

A translated adjective moves in front of its noun, because that is English word
order. A translated head noun moves to the end, and a chain of heads reverses:

```text
عَلَامَة الوَقْف        → waqf_mark
نَوْع عَلَامَة الوَقْف   → waqf_mark_type
```

A technical word stays transliterated, however ordinary it looks:

```text
النُّون السَّاكِنَة  → noon_sakinah    `sakinah` is a term of tajwid
الوَقْف اللَّازِم    → waqf_lazim      `lazim` is a term of waqf
```

The ordinary words are listed in `standards/terminology/data/general_words.tsv`,
each with its role: `word` stays where it stands, `head` moves to the end, and
`with_head` is translated only beside a head word and transliterated otherwise
(`العَلَامَة الإِمْلَائِيَّة → orthographic_mark`, but
`الرَّسْم الإِمْلَائِيّ → rasm_imlai`).

The rule:

> **Quran-specific concepts retain Quranic names; general concepts use natural
> technical English.**

## 4. Canonical Code Spelling

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

§4–§8 are mechanical rules, so a program can apply them. The Canonical
Code Spelling is derived from the vocalised Arabic name by one function, rather
than being left to each project's judgement.

```bash
python3 tools/translit.py "سُورَة" "رُبْع الحِزْب"
سُورَة        surah          Surah
رُبْع الحِزْب   rubu_al_hizb   Rubu al-Hizb
```

- The input is **vocalised**. Short vowels cannot be recovered from bare Arabic,
  and guessing them is the judgement call this is meant to remove. An unmarked
  hamzat al-wasl is refused rather than guessed: `اِسْتِعَاذَة` gives `istiadhah`,
  while `استعاذة` is rejected. Hamzat al-wasl is written as an alif with its
  vowel (`اِ`), never as `ٱ`.
- The function is **not reversible**, by design. Emphatic letters and their
  plain counterparts give the same Latin letter — `ص` and `س` are both `s`. The
  aim is a stable identifier, not an accurate pronunciation.
- `tools/check_conformance.py` re-derives the code of every `origin: quranic`
  entry from its `arabic.vocalized` on every build, and `tools/test_translit.py`
  holds the golden cases. When a spelling rule changes, those two show which
  names change with it.

For example:

```text
qiraah
ruku
irab
istiadhah
```

rather than:

```text
qira'ah
rukūʿ
i'rab
istiʿādhah
```

### The letter table

The consonants are written as follows. An emphatic letter and its plain
counterpart share one spelling:

```text
ب b    ت t    ث th   ج j    ح h    خ kh   د d    ذ dh   ر r    ز z
س s    ش sh   ص s    ض d    ط t    ظ z    غ gh   ف f    ق q    ك k
ل l    م m    ن n    ه h    و w    ي y    ة h (t in a construct, §5)
```

- **Hamzah and ayn** carry no letter of their own (§7).
- **Short vowels**: fathah `a`, kasrah `i`, dammah `u`.
- **Long vowels**: `ا`/`ى` → `a`, `ي` → `i`, `و` → `u`, never doubled (§6). A dagger
  alif and a maddah are long `a`.
- **Diphthongs**: `وْ` after fathah is `aw`, `يْ` after fathah is `ay`: `mawdi`,
  `awla`, `tarafayn`.
- **Shaddah** doubles the consonant: `makki`, `muqatta`, `shaddah`.
- **Tanwin** gives the short vowel alone; a case ending on the last letter is
  dropped: `هُدًى` → `huda`.
- **The definite article** is `al`, never assimilated to a sun letter (§8).

## 5. Ta marbutah

A singular Arabic term ending in ta marbutah ends in `h`:

```text
سُورَة   → surah
آيَة    → ayah
رِوَايَة  → riwayah
قِرَاءَة  → qiraah
بَسْمَلَة  → basmalah
```

So:

```text
surah     not sura
ayah      not aya
riwayah   not riwaya
```

The other forms are recorded as alternative spellings.

### Ta marbutah in a construct

A ta marbutah is pronounced as a `t` when the word is bound to the one after it,
so it is written `t`:

```text
هَمْزَة الوَصْل    → hamzat_al_wasl     not hamzah_al_wasl
سَجْدَة التِّلَاوَة  → sajdat_al_tilawah  not sajdah_al_tilawah
```

A noun followed by its own adjective is not bound to it, so its ta marbutah
stays `h`:

```text
القَلْقَلَة الصُّغْرَى  → qalqalah_sughra    not qalqalat_sughra
```

The rule is mechanical: a ta marbutah gives `t` on the head of a construct and
`h` everywhere else — at the end of a term, and before an adjective.
`tools/test_translit.py` checks it.

## 6. Long vowels

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
tajwid
tafsir
tariq
nuzul
tahqiq
tadwir
```

and not:

```text
tajweed
tafseer
tareeq
nuzool
tahqeeq
tadweer
```

These forms are not necessarily wrong in general use, but they are not the
canonical spelling in this standard.

### The nisba ya

A doubled ya at the end of a nisba gives a single `i`:

```text
مَكِّيّ     → makki      not makkiyy
مَدَنِيّ    → madani     not madaniyy
عُثْمَانِيّ  → uthmani    not uthmaniyy
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

**This applies to letter names only.** Every other term is derived by §4–§8:

```text
small_noon         a letter name, written as said
seen_al_qiraah     a letter name
tajwid             not a letter name, so derived (not tajweed)
haqiqi             not a letter name, so derived (not haqeeqi)
makki              not a letter name, so derived (not makkee)
```

The 28 letter names are in `standards/terminology/data/letter_names.tsv`, and
the function reads them from there. A letter name carries no meaning beyond its
sound; the reason and the measurement behind the rule are in the
[decision record](/guidelines/en/03-terminology/decisions/).

### `tajwid` is written by the rule

`code` holds `tajwid`, the derived form, although `tajweed` is the commoner
spelling. The reason is in the decision record.

The dominant spelling is not lost, because each concept has two name fields:

```text
code     tajwid     derived by the rule; what is written in code
display  Tajweed    measured from use; what a reader sees
```

`tajweed` is also recorded in `alternative_spellings`, so search and lookup find
it.

> **Open:** two letters share one name once emphatic and plain are merged, and
> no entry uses either name today. The question is in the
> [decision record](/guidelines/en/03-terminology/decisions/).

## 7. Hamzah and ayn

Hamzah and ayn are not represented by any special mark inside code names.

We use:

```text
qiraah
irab
istiadhah
ruku
```

and not:

```text
qira'ah
i'rab
isti'adhah
ruku'
```

A more precise transliteration belongs in `names.transliteration`, and can be
used in display or in scholarly content where it is needed.

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

A few names have settled on one form across Quranic software, so a derived form
would be correct but never used. `juz` is one: the letter rules give `juzu`, and
use gives `juz` by a wide margin.

These are recorded in `standards/terminology/data/established_spellings.tsv`,
each with the measurement behind it. A row is accepted only with a measurement
showing that the derived form is effectively unused; a term whose usage merely
leans one way does not qualify, or `tajweed` would qualify. The measurements
are in the [decision record](/guidelines/en/03-terminology/decisions/).

### Names written by a rule, not by a measurement

Two further cases are fixed by a rule rather than a count, and are kept in the
same file so that the function reads them in one place:

- **A name may not open with `al`.** `آل عِمْرَان` derives to `al_imran`, and `al`
  is what §8 reserves for the definite article, so the name is `aal_imran`.
- **A surah named by the letters it opens with is written by letter name.** The
  letter rules read `طه` as a consonant cluster and give `th`; the name is
  `taha`. Likewise `yasin`, `saad` and `qaaf`.

## 8. Compound names and `al-`

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

### When `al` is dropped

`al` is part of the name in a construct only. It is dropped in two cases.

**A leading definite article** is not part of the code name:

```text
الفَتْحَة   → fathah      not al_fathah
السُّكُون   → sukun       not al_sukun
```

**The article on an adjective** is not part of it either. When the noun is
definite and the word after it is definite, the two are one name rather than a
construct:

```text
الوَقْف اللَّازِم     → waqf_lazim      not waqf_al_lazim
النُّون السَّاكِنَة    → noon_sakinah    not noon_al_sakinah
الرَّسْم العُثْمَانِيّ   → rasm_uthmani    not rasm_al_uthmani
```

Telling the two apart is mechanical, and it is done **one pair at a time**: each
word is judged against the word immediately before it, wherever the term
opened. If the word before it carries `ال`, it is an adjective and its article is
dropped. If the word before it is indefinite, it is a construct and its `al`
stays:

```text
رُبْع الحِزْب                        → rubu_al_hizb
                                       (first word indefinite: a construct)
الوَقْف اللَّازِم                     → waqf_lazim
                                       (first word definite: an adjective)
الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن  → waqf_jaiz_mustawi_al_tarafayn
                                       (الجائز is an adjective of الوقف;
                                        الطرفين is the construct of مستوي)
```

A translated head word (§3) does not take part in the judgement. The rest of the
name is judged as if it opened the term, and English puts no article on a
qualifier:

```text
عَلَامَة الوَقْف اللَّازِم  → waqf_lazim_mark    not al_waqf_lazim_mark
```

### A preposition is a part of its own

A one-letter preposition written onto the next word — `بِ`, `لِ` — is its own
part, and the noun it governs keeps its article, because the noun opens a phrase
of its own and is never an adjective:

```text
تَفْسِير بِالرَّأْي         → tafsir_bi_al_ray
المَدّ العَارِض لِلسُّكُون  → madd_arid_li_al_sukun
```

### A connective is dropped

A word that only relates one part of a name to another — `مَعَ`, `كَوْن`,
`بِحَيْثُ`, `جَوَازًا` — says what the order of the parts already says, so it is
dropped:

```text
الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى  → waqf_jaiz_wasl_awla
```

The connectives are listed in `standards/terminology/data/connectives.tsv`. The
Arabic name keeps its connectives; only the code drops them (§14).

## 9. Code name and display name

The code name does not have to be the precise transliteration.

It can be:

```text
code:             qiraah
display:          Qiraah
transliteration:  qirāʾah
arabic:           قراءة
```

The Canonical Code Spelling stays stable, while the display form can vary by
language, audience and context.

### Name fields

We use several fields to hold the different names of a concept:

```yaml
names:
  code:            hamzah
  display:         Hamzah
  arabic:
    vocalized:     الهَمْزَة
  dabt:            الهَمْزَة — رَأْس العَيْن
  by_shape:        رَأْس عَيْن
  mushaf_introduction: null
  unicode:         ARABIC LETTER HAMZA
alternative_spellings:
  - hamza
```

#### The fields

**`code`** is the stable identifier used in code, APIs and databases. It is
generated by the rules in §4–§8, and is not changed later merely
because another name is more common.

**`display`** is the name shown to a reader in documentation and interfaces. We
take the most common English spelling and record where that came from in
**`display_evidence`**. The evidence is required before an entry is marked
`adopted`; a `draft` entry may carry a `display` with no evidence yet.

**`transliteration`** is the precise Latin transliteration, in ALA-LC or DIN
31635. It is optional, and written only where it is needed.

**`arabic.vocalized`** is the Arabic name written with its vowel marks. `code`
is derived from it, and cannot be derived without it. It is also what the Arabic
reader sees: the Arabic dictionary shows `arabic.vocalized` where the English one
shows `display`. **`arabic.singular`** and **`arabic.plural`** hold the bare
forms as linguistic information.

`arabic.vocalized` is the name we give the concept, and it can differ from the
name a source gives it. The source's name is kept in `dabt` or in
`mushaf_introduction`, so nothing is lost.

`arabic.vocalized` is changed only on Arabic grounds — that the new name fits the
boundaries of the concept better — never to reach a preferred code name.
`division_mark` is the example, and it is argued in the decision record.

A single noun carries its article (`السُّورَة`, `التَّجْوِيد`); a value that is an
adjective stays bare (`مَكِّيّ`, `مُرَتَّل`); a compound keeps the articles its
grammar gives it.

**`dabt`** is the name of the mark in the science of dabt, copied as its source
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

## 10. The shape of names in code

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

Name a classification by what it classifies, and use `_type` only for the
classification of a mark's kind, where the mark is the thing being classified:

```text
waqf_mark_type     what a drawn waqf mark points to
waqf_ruling        not waqf_type: the ruling on the place itself
recitation_style   not recitation_type
```

`audit_terminology.py --strict` reports the abbreviations and the vague names in
a codebase; the choice of a classification's own name is a rule for the writer.

## 11. Singular and plural

Use:

- the singular for one thing
- the plural for a collection

For example:

```text
ayah    → ayahs
surah   → surahs
mushaf  → mushafs
riwayah → riwayahs
```

Plurals in code follow a simple English convention: the whole code name plus
`s`, whether the name is one word or a construct:

```text
ayahs
juzs
hizbs
sajdahs
```

Arabic plurals are not used as collection names:

```text
ayat
suwar
ajza
ahzab
```

The Arabic plural is recorded in `names.arabic.plural` as linguistic
information.

`plural` is written on an entry that is stored or listed as a collection — an
entity, a unit, a piece of content — and omitted where nothing is ever a list of
it. `tools/check_conformance.py` checks that a recorded plural is the code name
plus `s`.

## 12. Every entry has a kind

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

`process` is reserved: no entry carries it today, because the operations of §23
are conventions rather than dictionary entries.

`kind` describes the **shape** of an entry rather than its domain; the domain is
carried by `category` alone. So kinds such as `textual_concept`,
`recitation_concept` or `typographic_unit` do not arise: those are all `concept`
or `unit`, differing in `category` rather than in `kind`.

Each entry has exactly one `kind`.

For example:

```text
ayah                       → entity
tajwid                     → concept
translation                → content
reciter                    → role
revelation_order           → property
revelation_classification  → classification
makki                      → classification_value
waqf_mark                  → mark
glyph                      → unit
irab                       → analysis
```

Do not treat all of these as one flat list of "terms".

### Every mark belongs to a family

The marks of dabt are not one list. Each mark belongs to a family, and that
family is its `parent`. The tree, as the entries have it:

```text
mushaf_mark
├── harakah            fathah, dammah, kasrah, sukun, shaddah
├── tanwin             tanwin_al_fath, tanwin_al_kasr, tanwin_al_damm
├── ijam               dot, two_dots, three_dots
├── orthographic_mark  hamzah, hamzat_al_wasl, maddah, omitted_alif,
│                      small_noon, small_waw, small_yaa
├── qiraah_mark        saktah_mark, seen_al_qiraah, ishmam, tashil, imalah
└── (no family)        waqf_mark, ayah_mark, sajdah_mark, sajdah_line,
                       division_mark, small_meem, rounded_zero,
                       rectangular_zero
```

`mushaf_mark` is not made the parent of every mark: one parent over every mark
in the registry says nothing. It stays the parent of the marks that have no
family.

The **waqf marks** are not in this tree. `waqf_mark` is the mark; what a given
mark points to is a value of the classification `waqf_mark_type`:

```text
waqf_mark_type
├── waqf_lazim
├── waqf_mamnu
├── waqf_jaiz_mustawi_al_tarafayn
├── waqf_jaiz_wasl_awla
├── waqf_jaiz_waqf_awla
└── waqf_al_muanaqah
```

These 6 are `classification_value`, and they are drawn, so they carry `symbol`,
`unicode` and `mark_family` like a mark. No other value does, and
`tools/check_conformance.py` refuses those fields on any other non-mark.

**`mark_family`** is the grouping of the source registry, `dabt_marks.tsv`:
`harakah`, `tanwin`, `ijam`, `imlaiyyah`, `dabt`, `waqf`, `alamat_qiraah`,
`mustaqill`. It is kept because it is what the source says, and it differs from
`parent` in two places by design: `imlaiyyah` is the registry's word for
`orthographic_mark`, and `alamat_qiraah` for `qiraah_mark`. `parent` is the
standard's taxonomy; `mark_family` is the source's.

## 13. Types and values get their own entries

When a concept has types or values that matter, defining the parent is not
enough.

The types and values get entries of their own in the dictionary, with their
real codes:

```text
revelation_classification
├── makki
├── madani
└── disputed
```

and:

```text
recitation_style
├── murattal
├── mujawwad
└── muallim
```

and:

```text
recitation_pace
├── tahqiq
├── tadwir
└── hadr
```

and:

```text
ayah_numbering_system
├── madani_first
├── madani_last
├── makki
├── basri
├── dimashqi
└── kufi
```

These 6 are entries, because each one can be defined, and their ids are
`ayah_numbering_kufi`, `ayah_numbering_makki` and so on, because `makki` alone
is already the id of the revelation value; §14 says why the code and the id
differ. What software stores is the code.

and the classifications of tajwid — the rulings, the kinds of madd, and the
relation between two letters — each with its values:

```text
tajwid_ruling           madd
├── izhar               ├── madd_tabii
├── idgham              ├── madd_muttasil
├── iqlab               ├── madd_munfasil
├── ikhfa               ├── madd_lazim
└── qalqalah            ├── madd_arid_li_al_sukun
                        ├── madd_al_lin
letter_relation         ├── madd_al_badal
├── mutamathilan        ├── madd_al_silah
└── mutajanisan         └── madd_al_iwad
```

and two classifications of waqf, one for the mark and one for the place:

```text
waqf_mark_type                     waqf_ruling
├── waqf_lazim                     ├── waqf_tamm
├── waqf_mamnu                     ├── waqf_kafi
├── waqf_jaiz_mustawi_al_tarafayn  ├── waqf_hasan
├── waqf_jaiz_wasl_awla            └── waqf_qabih
├── waqf_jaiz_waqf_awla
└── waqf_al_muanaqah
```

Each of these values gets its own entry, even when it is represented in code as
an enum value. `tools/check_conformance.py` refuses a classification with no
values.

### Members of a closed set go to a registry

A type is not the same thing as a member.

`revelation_classification` has 3 values, and each of them is a concept: a
reader can ask what `makki` means and get an answer that is not a list. But
`qiraah` does not have values in that sense. It has 10 members, and Asim is not
a concept — he is a person. Asking what Asim *means* has no answer beyond
pointing at him.

So a closed set of members does not become entries. It becomes a registry, one
tab-separated file per set in `standards/terminology/registries/`:

```text
qiraah, rawi, riwayah   → registries/qiraat.tsv        the 10 qiraat, 19 rawis, 20 riwayahs
tariq                   → registries/tariq.tsv         the 4 routes applications store
surah                   → registries/surahs.tsv        the 114 surahs
sajdah                  → registries/sajdah.tsv        the 15 sajdahs
ayah_numbering_system   → registries/ayah_numbering.tsv, ayah_counts.tsv
tajwid_ruling           → registries/tajwid_rules.tsv  the rulings of tajwid
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
attested, it is a member and it gets a row.

A registry is not a lesser thing than an entry. Every row is checked by
`tools/check_registries.py`, cites a source the way an entry does, and is
indexed so that every spelling of a member resolves. A row's `verified` column
says what has actually been checked against a source, and `no` is an allowed
value.

The registries are rendered on their own page,
[Registries](/guidelines/en/03-terminology/registries/).

### The rules of tajwid are a registry

The rulings of tajwid as an engine applies them — every case of izhar, idgham,
iqlab, ikhfa and madd, with its trigger and its source — are rows in
`registries/tajwid_rules.tsv`, generated from `data/tajweed_engine_rules.json`,
and `tajwid_ruling` names the registry. The rulings as concepts — `izhar`,
`idgham`, the kinds of `madd` — are values of their classifications and keep
their entries, as do the concepts a ruling rests on: `noon_sakinah`, `tanwin`,
`maddah`. A rule and its **occurrence** in the text are two things: the rule is
a row; an occurrence is a span of the text (§21) tagged with the rule's code.

### The letter names are a data table

The 28 letters are members too, but they are not indexed like a registry: their
names are read by the derivation itself, so they live in
`standards/terminology/data/letter_names.tsv`, beside the other spelling tables.
A letter is referred to in code by its name from that table: `noon`, `meem`,
`saad`.

### A person's name is not derived

§4–§8 derive a code name from vocalised Arabic, and every term in the
dictionary goes through them. A person's name does not:

```text
hafs        warsh        qalun        ibn_dhakwan
```

The derivation exists because a term is a word carrying a meaning, and working
from the Arabic keeps that meaning attached to the identifier. A name carries no
meaning to keep, so deriving it only produces a spelling nobody writes.

The exception covers people and nothing else. A surah name is a word, so it is
derived — `fatihah`, `baqarah`, `nisa` — and `tools/check_registries.py`
re-derives all 114 on every run.

"Commonly written" still has to be evidence rather than preference. The
registry records the scholarly English form with its diacritics, and the name
in use is that form with the diacritics dropped. Where the two disagree over
something the standard already rules on, the standard wins: `shubah`, not
`shuba`, because §5 governs a ta marbutah.

### A member's name may repeat a concept's

A member may carry the name of a concept, and neither name is changed. Hamzah is
a reciter, and `hamzah` is also the mark. Al-Tariq is a surah, and a `tariq` is a
step in a chain of transmission.

The repetition is harmless because the two live in different domains, in the
sense of §25: one `hamzah` is `dabt` and the other is `qiraat`. Nothing can
reach for both at once, so nothing has to choose between them. A name is only
required to be unique where it could actually be confused.

Member names are indexed by kind, because that is what a caller knows: a column
does not hold "something from the qiraat domain", it holds a riwayah.

```text
hamzah          → the mark
qiraah:hamzah   → the reciter
tariq           → the step in the chain
surah:tariq     → the surah
```

The bare name always belongs to the concept. Anything filling a known column
asks inside that namespace. `aliases.json` holds the concepts;
`registry_aliases.json` holds the members.

## 14. Parent and child

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

The point is that a developer knows not only what `makki` means, but also:

> makki is a kind of what?

### `parent` is *is-a*; `part_of` is containment

`parent` says what a thing is a kind of. It does not say what a thing is inside.
A rubu al-hizb is not a kind of hizb; it is a part of one. Containment is its
own field:

```yaml
concept: rubu_al_hizb
kind: entity
part_of: hizb
```

`part_of` is optional, and points at an entity. `parent` is required on every
`classification_value` and on every mark with a family.

### A value's name is derived from its parent's

The name of a value is the parent's name plus the words that distinguish it.
The Arabic name is kept whole, connectives and all; the derivation drops the
connectives (§8):

```text
الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى  → waqf_jaiz_wasl_awla
الوَقْف الجَائِز مَعَ كَوْنِ الوَقْف أَوْلَى  → waqf_jaiz_waqf_awla
الوَقْف اللَّازِم                          → waqf_lazim
```

The parent's name is not repeated when it distinguishes nothing, so the values
of `revelation_classification` stay `makki` and `madani` rather than
`revelation_classification_makki`. A value's name is unique within its
classification, not across the dictionary. The values of
`ayah_numbering_system` are `kufi`, `basri`, `dimashqi`, `makki`,
`madani_first` and `madani_last`, and `makki` is also a value of
`revelation_classification`. No column holds the values of two classifications,
so the two never collide.

Where two values do share a name, the entry's *id* becomes the parent's name
plus the code: `ayah_numbering_makki`. The id is the entry's file, its anchor
and what `related` and `parent` point at, and all 6 numbering entries carry
that form for regularity. The code is what software stores.

These 6 are the one family whose code is not derived from the Arabic: العَدّ
gives `add`, an English verb, so the code is the name of the school. The reason
is in the decision record.

`tools/check_conformance.py` checks that every classification has values and
that every `parent` and `part_of` names an entry.

## 15. Definition

Every entry has a `definition`.

The definition answers:

> **What is this concept?**

It should:

- define the concept itself
- be precise and brief
- state its boundaries where that is needed
- avoid defining the name by the name
- contain no implementation detail
- rest on a suitable source when the concept is a scholarly or technical one

For example:

```yaml
concept: ayah

definition_en: >
  A unit of the Quranic text falling within a surah and having determined boundaries.
  Its number, and some of its boundaries, may differ from one ayah numbering system to
  another.
```

and not:

```text
ayah: A Quranic verse.
```

These are rules for the writer; no tool can check them.

## 16. Purpose

Every entry also has a `purpose`.

The purpose answers:

> **Why does Quranic software need this concept?**

It explains:

- its role in the software model
- what we use to represent or link it
- why a developer needs to tell it apart from its neighbours

For example:

```yaml
concept: ayah

purpose_en: >
  Used as the basic unit for referring to the Quranic text, and for attaching
  translations, tafsir, recitations, analyses and other data to a specific place in the
  Quran.
```

### The difference

```text
definition → What is it?
purpose    → Why do we model it?
```

`purpose` does not restate `definition`, and details of software use do not go
inside `definition`. No tool checks this; the counter-example is a `purpose` that
reads "an ayah is a unit of the Quranic text", which is the definition rewritten.

If a concept has no clear purpose in software, that is a reason to review
whether it belongs in the core dictionary.

## 17. The boundaries of a concept

Where there is a real chance of confusion, the entry states what the concept
excludes, in its `boundaries` field, and names the neighbour in `related`.

For example:

```text
mushaf            ≠ quran
word              ≠ token
letter            ≠ character
glyph             ≠ character
rawi              ≠ reciter
tajwid            ≠ mujawwad
tartil            ≠ murattal
sajdah            ≠ sajdah_mark
waqf_mark_type    ≠ waqf_ruling
```

The aim is to stop one name standing for two different concepts in data and in
code, rather than to document a difference in language. No tool checks this; the
counter-example is a `boundaries` entry reading "differs from `word` in meaning",
which never says which of the two the column actually stores.

## 18. Similar concepts stay separate

Two concepts are not merged because their translations look alike. No tool checks
this; the counter-example is a schema with one `word` table holding both words
and tokens, which the `boundaries` of both entries exist to prevent.

### A mark and what it marks

A mark drawn in the mushaf is a separate concept from what it indicates:

```text
saktah_mark        the mark that is drawn      mark
saktah             the pause itself            concept

sajdah_mark        the mark of a sajdah        mark
sajdah             the place, and the          concept
                   prostration made at it

ayah_mark          the mark that is drawn      mark
ayah_ending        the ayah's ending           concept
```

The sajdah is 2 concepts, not one: the sign drawn in the mushaf, and the place
at which one prostrates. The place and the prostration are one concept, because
no software stores the act apart from its place, and "the 15 sajdahs"
names both at once; the decision record says why an earlier draft kept them
apart.

### A mark's identity is not its character

A codepoint does not work as the identifier of a mark, for two reasons fixed in
Unicode.

**One character serves two marks**, and the mark is determined by the character
together with its position:

```text
ۜ  U+06DC   ARABIC SMALL HIGH SEEN   →  saktah_mark  or  seen_al_qiraah
۬  U+06EC   ROUNDED HIGH STOP        →  ishmam       or  tashil
```

**One mark has more than one character**:

```text
sukun          ْ U+0652   and  ۡ U+06E1
tanwin_al_fath ً U+064B   and  ࣰ U+08F0
maddah         ٓ U+0653   and  ۤ U+06E4
```

So a codepoint is a property of a mark rather than a key to it.

### Text

A word, what tokenisation produces and what morphological analysis produces are
different things, and each has its own entry:

```text
word
token
morpheme
lemma
root
```

### Digital representation

A letter in the language, a character in Unicode and a shape a font draws are
5 concepts, not one:

```text
letter
character
codepoint
grapheme
glyph
```

### Quran and mushaf

The Quran is the revealed speech; the mushaf is the book it is written in.
Neither stands in for the other:

```text
quran
mushaf
```

### Content and presentation

What the text carries is not what it looks like on a page, so content concepts
and presentation concepts stay apart:

```text
content:
surah
ayah
word

presentation:
page
line
layout
font
glyph
```

### Text and analysis

A word in the text is not what analysis derives from it; analysis is a derived
layer with concepts of its own:

```text
text:
word

analysis:
root
lemma
morphology
irab
```

## 19. Name, spelling and translation are not one thing

Keep these apart:

```text
names.code
alternative_spellings
english_glosses
deprecated
```

For example:

```yaml
concept: ayah

names:
  code: ayah

alternative_spellings:
  - aya
  - ayat
  - ayaat

english_glosses:
  - Verse
```

`aya` is an alternative spelling of `ayah`.

`Verse` is an English gloss, not an alternative spelling.

Likewise:

```yaml
concept: tajwid

names:
  code: tajwid

alternative_spellings:
  - tajweed
  - tajwīd
```

There is no catch-all field mixing these relations together, and none is added.

`tools/check_conformance.py` checks that a gloss is not also recorded as an
alternative spelling.

## 20. Deprecated does not mean incorrect

We distinguish:

### Alternative

Another correct or common form:

```text
tajweed → alternative spelling of tajwid
```

### Deprecated

A name for the concept, but not recommended in new projects. It goes in
`deprecated`, and still resolves: `aliases.json` indexes spellings only, and a
deprecated name is resolved through the entry's `deprecated` field.

### Incorrect

A name that points at a different concept, or carries a wrong meaning. It is
not recorded on the entry it does not belong to; the `boundaries` of the right
entry name the confusion.

`verse` may be a correct English translation of `ayah`, but it is not the
canonical name in this standard.

### Renames are recorded, not erased

When a concept's code changes, or two entries are merged, the old code goes into
`deprecated` on the surviving entry, and `note` says when and why, pointing at
the decision record. The old name keeps resolving, so a project that adopted it
is not stranded, and a reader can see that it was once the name:

```yaml
# in sajdah_mark.yml
deprecated:
  - alamat_mawdi_al_sajdah
note: >
  Merged from alamat_mawdi_al_sajdah, which defined the same mark. Decision
  record, "Duplicated concepts are merged".
```

An entry that is withdrawn altogether is marked `status: deprecated` and kept,
so that its code never comes back with a different meaning.

## 21. Identifiers, numbers and order

Each suffix has one fixed meaning.

### `id`

`id` is the internal identifier of a database row. It joins tables to each
other, and it is never shown to a reader or used in an external reference:

```text
surah_id
ayah_id
word_id
mushaf_id
```

### `number`

`number` is the established number of a thing within its own domain. It is the
number a reader would recognise and cite:

```text
surah_number
ayah_number
page_number
```

### `position`

`position` is where an element sits inside its parent or its sequence. It counts
places, so it changes whenever the sequence changes:

```text
word_position
token_position
line_position
```

### `order`

`order` is an ordering that meaning decides. We use it where the intended order
differs from where the element happens to sit:

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

### `key`: the human-readable composite

A `key` is the established composite reference, written for humans and stable
across systems:

```text
ayah_key     2:255         surah_number:ayah_number
word_key     2:255:3       ayah_key:word_position
```

A key is only meaningful under a stated `ayah_numbering_system`; a dataset that
uses keys says which system they follow, and defaults to `kufi` when it says
nothing. A global index of the ayahs (1 to 6,236) is a `position`,
not a key, and it too is relative to a numbering system.

### Audio is keyed by the recitation and the text

A span of audio is named after the unit of text it matches, and it belongs to a
recitation:

```text
ayah_timing      one ayah's span in one recording      recitation_id, ayah_key, start_ms, end_ms
word_timing      one word's span in one recording      recitation_id, word_key, start_ms, end_ms
```

A recording is identified by its `recitation_id`, and a recitation is one
reciter, in one riwayah, in one style; those three are fields of the
recitation, not parts of the audio's name.

## 22. Relationships

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

## 23. Operations and verbs

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

The verbs are a convention of this standard, not entries in the dictionary, so
no tool checks them. The operation names keep their own spelling in code
(`normalize`); prose writes the ordinary word (normalise).

## 24. Classifications and booleans

Classifications carry domain-specific names, and each is an entry:

```text
waqf_mark_type
waqf_ruling
tajwid_ruling
madd
letter_relation
recitation_style
recitation_pace
revelation_classification
```

rather than:

```text
quran_type
item_type
data_type
```

A boolean's name shows that it asks a yes/no question:

```text
has_sajdah
is_active
is_included
```

A multi-valued classification is not modelled as a set of booleans when one
classification is more precise.

Like §21 to §23, this is a convention outside the machine-readable source.

## 25. Organising the domains

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
dabt                  dabt: vowels, tanwin and every mark of the mushaf
ayah_numbering        ayah numbering systems
revelation            revelation, its order and its classification
qiraat                qiraat, riwayahs and tariqs
recitation            recitation and reciters
recitation_pace       tahqiq, tadwir and hadr
recitation_style      murattal, mujawwad and muallim
tajwid                tajwid, its rulings, madd, and the registry of its rules
waqf                  waqf and its rulings
linguistics           root, lemma, morphology and irab
translation           translation
tafsir                tafsir
quranic_sciences      abrogation, word meanings and mutashabihat
```

A domain is not added before there are concepts that belong to it, because an
empty domain suggests coverage that does not exist.

## 26. Consistency across the layers of a system

The same canonical vocabulary is used across the layers of a system as far as
possible.

If we adopt:

```text
surah
ayah
word
```

then the expected result is:

```text
models:
Surah
Ayah
Word

database:
surahs
ayahs
words

foreign keys:
surah_id
ayah_id

API:
/surahs
/surahs/{surah_number}/ayahs
/ayahs/{ayah_key}/words
```

Avoid using:

```text
database: surah
API: chapter
package: quran_section
```

for one concept.

A user interface can translate or display the name differently, while the
canonical internal vocabulary stays fixed.

### Quote a name the project does not own, exactly as its owner writes it

A project refers to names it does not own: a supplier's package and file names,
the column headings of a file it reads, the official name of a Unicode
character, the address of another repository. These are locators. They point at
something outside the project, and changing a letter of one breaks the
reference, so they are written exactly as their owner writes them, however far
from this standard that is.

```text
UthmanicHafs-v-3.0.zip          the publisher's package: quoted
row["aya_text_emlaey"]          the publisher's column: quoted
"ARABIC START OF RUB EL HIZB"   the Unicode name of ۞: quoted
quranpedia/qiraat-ayah-map      another repository: quoted
```

What the project decides for itself is what it calls the thing once it has read
it: the field, the variable, the published key. A quoted name never becomes the
name of a concept, and a name of your own never keeps a supplier's spelling
because it came in with the data.

An audit is told which names are quoted, so that it reads past them instead of
asking for a rename that would break the reference: `external_names` in
`.terminology.json`.

### Casing per layer

The code name is `snake_case`, and each layer applies its own casing to that one
name, never to a different name:

```text
snake_case    database tables and columns, JSON keys, enum literals, file names
                ayah_numbering_system, waqf_lazim
PascalCase    classes and types            AyahNumberingSystem, WaqfMarkType
camelCase     only where the language demands it for members   ayahNumber
kebab-case    URL paths and slugs only     /waqf-marks/waqf-lazim
```

A kebab form is a rendering of the code name for a URL, not a spelling; it is
not recorded in `alternative_spellings`.

## 27. The shape of a dictionary entry

The dictionary produced by this standard uses one structure, with a file per
concept. The file is named after the concept — `ayah.yml` holds `concept: ayah` —
and `tools/validate.py` refuses a file whose name and concept disagree.

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
definition_en:
purpose_en:
```

Added where needed:

```yaml
parent:          # required when kind is classification_value, or a mark with a family
part_of:         # containment; points at an entity
registry:        # the registry that enumerates this concept's members
plural:          # the code plus s
symbol:          # the character a mark is drawn with
mark_family:     # the source registry's grouping; marks and drawn values only

names:
  display_evidence:   # required before adopted
  transliteration:    # optional; ALA-LC or DIN 31635
  arabic:
    vocalized:        # required when origin is quranic
    singular:
    plural:
  dabt:
  by_shape:
  mushaf_introduction:
  unicode:

unicode:         # generated from the Unicode database, never written by hand
alternative_spellings:
english_glosses:
deprecated:
boundaries:
boundaries_en:   # the translation of boundaries, line for line
related:
sources:
note:
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
`proposed` after discussion, then `adopted` once accepted; an entry withdrawn
after adoption becomes `deprecated` and is kept (§20). An entry with no source
is not marked `adopted`, and neither is one with no `display_evidence`.

**`arabic`** is required on every `origin: quranic` entry. A borrowed term is
given its Arabic name when it has a settled one, so that we do not coin new
Arabic terms by accident.

**`related`** links resolve to entries, and the build makes them symmetrical:
naming `waqf_mark` from `waqf_lazim` shows `waqf_lazim` from `waqf_mark`.

### The entry in two languages

There is one entry, and its prose is in two languages. Every prose field has an
English twin: `definition_en`, `purpose_en`, `boundaries_en` and `note_en`. The
English dictionary page is generated from them, as the Arabic page is generated
from the Arabic fields, so the two pages cannot say different things.

A twin is **a translation, not a second definition**. What one states, the other
states: the English adds no condition and drops none. Boundaries translate line
for line, one English line for each Arabic line, in its place, and
`tools/check_conformance.py` checks that the two lists are the same length.

Four rules hold in the translation:

- **A term is called by its canonical name**, written as prose writes it — the
  code spelling as a lowercase common noun: ayah, not verse; mushaf, not codex.
  The English in `english_glosses` is a search key, not a name to write with.
- **A code name is written as it is**, inside backticks, never translated.
- **A repeated formula is translated by a repeated formula**: the 6 ayah
  numbering entries share one purpose sentence in Arabic, so they share one in
  English, word for word.
- **No Arabic is left in an English field**, except an Arabic name the entry is
  itself talking about, which is written inside «…». `tools/check_conformance.py`
  checks this.

None of this is offered as an approved translation of a religious text. It states
a concept in a second language for whoever builds with it.

### Example

The entry `standards/terminology/concepts/waqf_lazim.yml`, as it is. The build
checks that this block and the file agree:

```yaml
concept: waqf_lazim
names:
  code: waqf_lazim
  display: Waqf Lazim
  arabic:
    vocalized: الوَقْف اللَّازِم
    singular: الوقف اللازم
  dabt: المِيم — عَلَامَة الوَقْف اللَّازِم
  by_shape: مِيم
  mushaf_introduction: عَلَامَة الوَقْف اللَّازِم
  unicode: ARABIC SMALL HIGH MEEM INITIAL FORM
kind: classification_value
category: dabt
parent: waqf_mark_type
origin: quranic
tier: core
status: draft
symbol: م
definition: الوقف اللازم علامة تدل على أن الوقف لازم، لأن وصل ما بعده بما قبله يوهم خلاف المعنى
  المراد.
definition_en: 'A compulsory stop: continuing across it would suggest a meaning other than
  the one intended.'
purpose: نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات
  بدلًا من قراءة صورة الرمز.
purpose_en: Used as a value of the waqf mark type, so that rendering, teaching and warnings
  in applications branch on it rather than on the shape of the sign.
alternative_spellings:
- waqf-lazim
related:
- waqf
- waqf_mark
unicode:
- cp: U+06D8
  name: ARABIC SMALL HIGH MEEM INITIAL FORM
  category: Mn
  combining_class: 230
  block: Arabic
  unidata: 13.0.0
mark_family: waqf
sources:
- id: hafs_svg_registry
  ref: standard!waqf-lazim
- id: quranpedia_tajweed
  ref: '122'
  url: https://tajweed.quranpedia.net/term/show/122
- id: qattan_mabahith
  ref: 1/152
```

## 28. Sources for definitions

Scholarly and technical terms rest on suitable sources.

A source documents **the concept and its definition**, and not necessarily the
choice of name in code.

A source may establish the meaning of `ayah`, while choosing:

```text
ayah
```

over:

```text
verse
```

is a decision made by this standard.

Keep the two apart:

```text
domain fact          what the source establishes
standard convention  what this standard decides
```

### Adopted sources

The sources are recorded in `standards/terminology/sources.yml`, each with the
reference form it uses: a page in a book, a term number in a dictionary. They are
not listed again here, so there is only one place to keep them current.

The build checks that every source cited — by an entry's `sources[].id` or by
a registry row's `ref` — names a source that exists in that file.

An entry with no source establishing its definition is not marked `adopted`.

## 29. The dictionary is machine-readable

The primary source of the dictionary is machine-readable: one YAML file per
concept, a JSON schema, and tab-separated registries.

From that same source we generate today:

- the two dictionary pages and the registries page
- `aliases.json` and `registry_aliases.json`, so that any spelling resolves
- the agent skill in `skills/quranic-terminology/`

and intend to generate:

- API schemas
- IDE hints
- linters
- deprecated-term warnings
- migration mappings

Human-readable documents are generated from that source wherever possible, never
kept as a separate copy.

### Versions of the dictionary

The dictionary has no version number of its own; its version is the generated
skill's snapshot. Every build stamps `skills/quranic-terminology/` with the
SHA-256 of its inputs — the entries, the registries, the spelling tables and
this standard — and a release adds the commit. A project that depends on the
dictionary records the stamp it built against, and `scripts/update_check.py` in
the skill says whether the stamp is current.

A change that renames or withdraws a code is recorded on the entry (§20) and in
the decision record, dated. That is the changelog: the decision record, read in
order. A withdrawn code still resolves through the entry's `deprecated` field,
not through `aliases.json`, which indexes spellings only.

## 30. The rule for accepting a new term

### First, whether the concept is ours to name

A concept belongs in this standard when **it cannot be defined without
referring to the Quran or the mushaf**.

Everything else an application stores is real, and is not ours:

```text
in scope:
sajdah            a place in the Quranic text at which one prostrates
ayah_timing       a span of audio matched to an ayah
word_meanings     the meaning of a Quranic word
mutashabihat      wordings repeated within the Quran

out of scope:
book, author, chapter, category, tag, language, attachment, source
radio, stream, thumbnail, user, subscription
fatwa, hadith, athar, topic
```

A stream of Quran audio is a stream; a fatwa is Islamic scholarship but not a
concept of the Quranic text; a book is already named by the language. The
standard says so plainly, because a project still needs names for its books and
its tags and this standard does not give them. The reason for the boundary, and
the alternative that was rejected, are in the
[decision record](/guidelines/en/03-terminology/decisions/).

> **The standard names the concepts of the Quranic text and its sciences. It does
> not name what an application stores besides them.**

### Extending the dictionary in a project

A project that needs names the standard does not give writes them the same way,
in a concepts directory of its own, with `origin: standard` and its own
`category` values, and runs the same tools on them. The skill's audit reads a
project's directory beside the standard's, so a local concept is checked and
not flagged. A local concept that turns out to be a concept of the Quranic text
is proposed here, through an issue, and moves into this dictionary if accepted.

A project does not redefine a concept this dictionary defines, and does not
reuse a code from it for something else.

### Then, the entry itself

Before an entry goes into the dictionary, answer:

1. What is the concept?
2. What is its definition?
3. Why does software need to model it?
4. What are its boundaries, and what might it be confused with?
5. What is its `kind`?
6. Which `category` does it belong to?
7. Does it have a `parent`, or a `part_of`?
8. Is it a Quranic concept or a general technical one?
9. What is the most suitable canonical name?
10. If it is Arabic in origin, does it follow the Canonical Code Spelling?
11. Is it ever a collection, and if so what is its plural in code?
12. What are its alternative spellings?
13. What are its translations or English glosses?
14. Are there deprecated names?
15. Does the name work naturally in code, in an API and in a database?
16. What source establishes the concept's definition?

If we cannot state the concept clearly, or say why software models it, it is not
adopted until the need becomes clear.

## 31. The underlying principles

The standard comes down to these:

1. **Concept before name.**
2. **One concept, one canonical name.**
3. **Quran-specific concepts retain Quranic names; general concepts use natural technical English.**
4. **Arabic-derived terms use one simple Canonical Code Spelling, derived and not chosen.**
5. **`definition` explains what the concept is; `purpose` explains why software models it.**
6. **Every entry has a defined `kind` and `category`.**
7. **Important types and values are first-class dictionary entries with their own definitions; members of a closed set are registry rows.**
8. **Parent–child relationships are explicit, and containment is a separate field.**
9. **Different concepts remain different even when their names or translations are similar.**
10. **Canonical names, alternative spellings, translations and deprecated names are kept separate.**
11. **The same vocabulary is used consistently across code, APIs, databases, datasets and documentation.**
12. **The dictionary is machine-readable, and its rules are checked by tools.**
