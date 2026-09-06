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

**Consequence:** the 28 letter names live in `letter_names.tsv`, and
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
37 marks says nothing.

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

---

## `waqf_al_muanaqah`, not `taanuq_al_waqf`

**Decision:** the mark at U+06DB is `waqf_al_muanaqah` — وَقْف المُعَانَقَة.

**Why:** it was the one waqf value that did not lead with `waqf`, so it read as
a stranger among `waqf_lazim`, `waqf_mamnu` and the three `waqf_jaiz_*`. The
cause was the naming phrase, not the spelling: `dabt_marks.tsv` gives the
registry's name as وَقْف المُعَانَقَة and records تَعَانُق الوَقْف as what the
mushaf introduction calls the mark, and the generator had taken the second.
The source ref was `standard!muanaqah` all along.

**No Arabic was edited to reach the name.** The name taken is the one the
registry already gives.

**The `al` stays, and it was not negotiated.** The first word is indefinite, so
the term is a construct and its article is part of the name — the `rubu_al_hizb`
rule. `waqf_muanaqah` was reached first by splitting the term into two parts so
that each dropped its own article. That is patching the derivation to get a
preferred string, and it was undone: the sibling prefix is worth having, a rule
bent to get it is not.

**A purpose name was rejected:** `paired_waqf` and `embracing_waqf` were
considered. Section 3 keeps a scholarly term, and `muanaqah` is a term of waqf
exactly as `lazim` is — neither is in `general_words.tsv`. `division_mark` is
not a precedent for them: it went to English because the Arabic name was wrong
about the concept, and this one is not.

**Nothing is stranded:** `taanuq_al_waqf`, `muanaqah`, `muraqabah` and
`waqf_al_muraqabah` all resolve through `aliases.json`.

---

## The tanwin marks are named by their harakah

**Decision:** `tanwin_al_fath`, `tanwin_al_kasr`, `tanwin_al_damm` — تَنْوِين
الفَتْح, تَنْوِين الكَسْر, تَنْوِين الضَّمّ.

**Why:** measurement. The case names are effectively unused in Latin script, and
lose in Arabic too:

```text
tanwin fath   618  ×  tanwin al-nasb    0
tanwin kasr   551  ×  tanwin al-jarr    0
tanwin damm   492  ×  tanwin al-rafa    0

تنوين الفتح   217  ×  تنوين النصب     184
تنوين الكسر   161  ×  تنوين الجر       21
```

**The registry agrees with the measurement:** its own file ids are `تنوين فتح`,
`تنوين كسر`, `تنوين ضم`. The case names it writes in the ضبط column stay in
`dabt` — `تَنْوِين الخَفْض — الكَسْرَتَان`.

**Two arguments were made against this and both failed.** That the triad should
name the case and not the harakah was consistency reasoning with nothing under
it; usage decides, and usage went the other way. And the choice between الجر and
الخفض, argued and settled before the measurement, was a choice between two forms
that both lose.

**Nothing is stranded:** `tanwin_al_nasb`, `tanwin_al_jarr`, `tanwin_al_khafd`,
`tanwin_al_rafa`, `fathatan`, `kasratan`, `dammatan`, and the registry's
`tanwin_fath`, `tanwin_kasr`, `tanwin_damm` all resolve.

## The standard names the Quran's own sciences, and stops there

**Decision:** `naskh`, `gharib_al_quran`, `mutashabihat` and `mawdi_al_sajdah`
are entries. `book`, `author`, `category`, `tag`, `language`, `attachment`,
`radio`, `fatwa` and `topic` are not.

**Why:** a survey of a working encyclopedia (`surveys/quranpedia-net.md`) found
77 domain tables, of which 10 resolved to an entry. The tempting reading was
that the dictionary is 87% short. It is not: most of what was missing is either
ordinary software furniture that needs no Quranic standard, or scholarship that
is not about the Quran.

**The line:** a concept is in scope when it cannot be defined without referring
to the Quran or the mushaf. `mawdi_al_sajdah` cannot; `radio` can, and a stream
of Quran audio is a stream. `fatwa` sits outside for the same reason a hadith
does — real, Islamic, and not a concept of the Quranic text.

**Alternative rejected:** naming everything an application stores. It would put
the standard in the business of general web modelling, where it has no
authority and adds no precision.

**Consequence:** a project still needs names for its books and its tags. The
standard does not give them, and says so, rather than leaving the reader to
guess whether the silence is an oversight.

---

## Ayah-numbering values keep their parent's name

**Decision:** `ayah_numbering_kufi`, `ayah_numbering_madani_awwal` — not `kufi`
and `madani_awwal`.

**Why:** two reasons, and either alone is enough.

The derivation of the Arabic name does not survive. العَدّ الكُوفِي gives
`add_kufi`, and `add` is an English verb — the same fault that made us write
`noon` rather than `nun`.

And the short name is taken. `makki` is already a value of
`revelation_classification`, so العَدّ المَكِّي cannot be `makki` without two
concepts claiming one name, which `build_aliases.py` refuses.

**This is section 14, not an exception to it:** a value's name is its parent's
name plus what distinguishes it, and the parent's name is dropped only when it
distinguishes nothing. Here it distinguishes a great deal. `waqf_jaiz_wasl_awla`
has the same shape.

**A second gain:** `kufi` alone would collide in a reader's head with the Kufic
script, which is a real term in mushaf work.

---

## `ayah_mark`, with `رَأْس الآيَة` kept in `dabt`

**Decision:** `code: ayah_mark`, `names.arabic.vocalized: عَلَامَة الآيَة`, and
the ضبط name عَلَامَة رَأْس الآيَة recorded in `dabt`.

**Why:** the derivation of the fuller name gives `ras_al_ayah_mark`. `ras` is an
ordinary word carrying no term, and it describes where the mark sits rather than
what it marks. Every other mark in the dictionary is named after what it marks —
`waqf_mark`, `sajdah_mark`, `division_mark`.

**Why this is not editing the Arabic to reach a preferred code name:** the rule
is that `arabic.vocalized` changes only on Arabic grounds. عَلَامَة الآيَة is the
mark of the ayah's boundary; رَأْس describes the position, and the source's own
name is kept in `dabt`, exactly as `sajdah_mark` keeps
`عَلَامَة مَوْضِع السَّجْدَة`.

**Why it was missing:** it is the most common mark in the mushaf and it is not
in `dabt_marks.tsv`, so the generation that produced the mushaf's marks from
that registry produced everything except this one.

---

## `naskh`, not `nasikh_mansukh`

**Decision:** one entry, `naskh`.

**Why:** the familiar title is النَّاسِخ وَالمَنْسُوخ, and it derives to
`nasikh_walmansukh` — a conjunction welded into an identifier. The science is
النَّسْخ, and الناسخ والمنسوخ are the two sides of one relation, not two concepts.

**Nothing is lost:** `nasikh_mansukh`, `nasikh_wa_mansukh` and `nasekh_mansokh`
all resolve through `aliases.json`.

---

## Token, morpheme and font were named because section 18 already named them

**Decision:** entries for `token`, `morpheme`, `stem`, `part_of_speech` and
`font`.

**Why:** section 18 tells the reader to keep `Word`, `Token` and `Morpheme`
apart, and lists `Font` under presentation. None of the four had an entry, so
the standard was naming a distinction it declined to define, and
`morphology.purpose` already used the word `token` in its own text.

**The boundary that mattered:** a token is what a splitting method produces, and
a word is what a reader recognises. Changing the method changes the token count
and not the word count. `segment`, the name the Quranic corpora use, resolves to
`morpheme`.

---

## `harf_al_mana` for the particle, because `harf` is the letter

**Decision:** the three parts of speech are `ism`, `fil` and `harf_al_mana`.

**Why:** حَرْف names two different things, and the dictionary had already given
the name to one of them — `harf` resolves to `letter`, a unit of written text.
The part of speech is حرف المعنى, as against حرف المبنى, and the tradition
already draws that line, so we did not have to invent one.

**Why only three:** the Quranic corpora tag with dozens of labels — `N`, `PN`,
`V`, `CONJ`, `NEG`. Those are data that sit under these three, not entries.
Naming forty tags would put the standard in the business of maintaining a
tagset.

**What it fixed:** `part_of_speech` had been added as a classification with no
values, which is the fault section 13 names, and the same fault that had left
`ayah_numbering_system` empty. The check now refuses it.

---

## The standard's own rules are checked, not remembered

**Decision:** `tools/check_conformance.py` runs the rules the prose states —
that a quranic code is the derivation of its Arabic name, that a classification
has values, that a plural is the code plus s, that a `related` link resolves,
that a gloss is not a spelling.

**Why:** `validate.py` checks the shape of an entry against `schema.json`, and
the schema cannot express any of the above. Everything in this list was found
the first time the check was run, on entries that had passed validation for
months: a plural taken from the English gloss, two `related` links pointing at
concepts that do not exist, and a gloss doubling as an alternative spelling.

**Two lists, kept apart.** `DOCUMENTED` holds departures this record argues for,
such as the ayah-numbering values. `TOOL_DEFECTS` holds mismatches whose cause is
in `translit.py` and whose entry is already correct. Merging them would let a
defect hide behind a decision.

**The first defect it found:** `translit.py` drops the `al` of a construct that
follows a definite head, so `الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن` derives to
`waqf_jaiz_mustawi_tarafayn` while `مُسْتَوِي الطَّرَفَيْن` on its own derives to
`mustawi_al_tarafayn`. Section 8 keeps the `al` when the first word is
indefinite, so the entry is right and the function is wrong.

---

## A closed set of members goes to a registry, not to an entry each

**Decision:** the 10 qiraat, the 20 riwayat, the 114 surahs and the 15 places
of prostration live in tab-separated files under
`standards/terminology/registries/`. The concept keeps its entry and names its
registry; the members get rows.

**Why:** an entry answers "what is this?". Hafs has no answer to that question
beyond pointing at him. Writing 49 entries for the qiraat would have tripled the
dictionary with files whose `definition` and `purpose` fields could only restate
the name, and it would have buried the 20 entries that do define something under
163 that do not.

**Alternative rejected:** an entry per member, with `kind: instance`. It puts
individuals and concepts in one list and makes "is this a concept?" a judgement
call at every new name.

**The test:** if a member needs a definition, a purpose and boundaries, it is a
concept. If everything true of it is its name, its place in the set and where it
is attested, it is a member.

**Precedent:** the 28 letter names went to `data/letter_names.tsv` on this
reasoning before the word registry was used for it.

**A registry is not a weaker record.** Every row is checked by
`tools/check_registries.py`, cites a source, and is indexed.

---

## A person's name is not derived

**Decision:** `hafs`, `warsh`, `qalun`, `ibn_dhakwan` — written as they are
commonly written, not put through sections 4 to 8.

**Why:** the derivation is there because a term is a word carrying a meaning,
and working from the vocalized Arabic keeps that meaning attached to the
identifier. A name has no such meaning, so deriving it only produces a spelling
nobody writes.

**Where the derivation was tried and failed:** `أَبُو عَمْرو` derives to
`abu_amrw`, because the waw of عمرو is orthographic and silent; `ابْن` cannot be
derived at all, because its initial alif is hamzat al-wasl and carries no vowel
to read. Two rows were added to `established_spellings.tsv` to force these
through, then removed, because patching the derivation for names it was never
meant to handle is worse than exempting them.

**The boundary:** people, and nothing else. A surah name is a word, so it is
derived, and `check_registries.py` re-derives all 114 on every run.

**Evidence, not preference.** "Commonly written" is the scholarly English form
with its diacritics dropped, and the registry carries both. Where that form
disagrees with a rule the standard already states, the rule wins — `shubah`, not
`shuba`, because section 5 governs a ta marbutah.

**Measurement was tried first and thrown out.** GitHub phrase counts decide
between `tajwid` and `tajweed` because both are terms. On names they return
noise: `susi` scored 5,185,536 and `qumbul` beat `qunbul`, because the queries
were matching tokens that have nothing to do with any reciter. The counts were
deleted rather than kept as evidence for a decision they cannot support.

---

## A member may share a name with a concept

**Decision:** `hamzah` is the mark and also the reciter; `tariq` is a step in a
chain of transmission and also a surah. Both keep the name. Member names are
indexed by kind in `registry_aliases.json`, and the bare name in `aliases.json`
goes on resolving to the concept.

**Why:** the two live in different domains in the sense of section 25 — one
`hamzah` is `dabt`, the other `qiraat` — so nothing can reach for both at once.
A name only has to be unique where it could actually be confused.

**Alternative rejected:** qualifying the newcomer, the way `ayah_numbering_makki`
was qualified when `makki` was already taken. That precedent holds for a value
whose name is built from its parent's. It does not extend to bending a person's
name, or a surah's, to dodge a collision that no caller can experience.

**Keyed by kind, not by domain:** a column does not hold "something from the
qiraat domain", it holds a riwayah, and the caller always knows which.

**The collisions are reported, not silently allowed.**
`check_registries.py` prints all three every run, so the exception stays a known
fact rather than an accident.

---

## The ayah counts are read out of the book, and proved by reconciling

**Decision:** `registries/ayah_counts.tsv` holds the count of every surah in all
six schools, generated by `tools/extract_ayah_counts.py` from al-Dani's
al-Bayan. It is never edited by hand.

**Why not a table from elsewhere:** the six schools disagree about 114 numbers,
and a table with no source cannot be argued with. al-Bayan states each surah's
count once and then gives only the part that differs — "285 in the two Madinans,
the Makkan and the Damascene, and six in the Kufan, and seven in the Basran" —
so the numbers exist in the book in a form a tool can read.

**Why it can be trusted:** it reconciles twice over. All 114 Kufi counts match
the printed mushaf surah by surah, which tests the reading of every section
rather than the arithmetic; and Kufi sums to 6236 and Basri to 6204, the totals
al-Dani himself states.

**What the reconciliation caught:** every bug, and there were five. `آيتان` is
the numeral two fused with its noun and was being skipped. `وآية` conjoined is
the numeral one, so "fifty and an ayah" is 51, while a bare `آية` after a number
is the counted noun. A later part replaces the trailing part it covers, so 110
and "nine" is 109 — but 180 and "two" is 182, because a round ten from twenty
upward takes a unit beside it while a bare ten is replaced. Two-word school
names were being split into tokens and lost. An aside inside a run of school
names — "with a variance reported from him" — was breaking the run. Totals alone
would have hidden most of these: the first pass was out by 20 in one column and
had two surahs badly wrong whose errors nearly cancelled.

**The residual is disclosed, not smoothed.** Four columns come to one more than
the total al-Dani states. Two places in the book give a count for the reading of
Abu Jafar specifically, and whether "the count of Abu Jafar" is the Madani Awwal
school or an authority beside it is a question about the source. A tool should
not decide it, so the run prints the discrepancy every time.

---

## `verified` in a registry means a specific thing, and `no` is an allowed value

**Decision:** a registry row says what has actually been checked. The sajdah
rows carry `verified: surah`, which means the surah is attested in a source and
the ayah number is not.

**Why:** the alternative is a citation that gestures at a page which does not in
fact contain the claim. That is worse than an honest blank, because it cannot be
distinguished from a real one later.

**What that produced here:** al-Itqan names all fourteen sajdah surahs and gives
the count as fourteen, which was checked against the book. Fifteen places in
fourteen surahs is not a contradiction — al-Hajj carries two. Every ayah number
is checked against the verified Kufi count for its surah, so a reference outside
its own surah cannot pass, and two of them land on the last ayah of the surah,
which the counts confirm. What no source in this repository does is enumerate
the fifteen numbers, and the file says so.

**The same rule refused a turuq registry.** The counts could be proved because
they reconcile to a total; the turuq have no such total. A scan of al-Nashr's
isnad section returns 224 distinct names at every depth of the tree with no
reliable way to attach each to its parent, and an unverifiable table looks
exactly like a verified one. `check_registries.py` reports the missing registry
on every run instead.
