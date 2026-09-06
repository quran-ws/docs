# Decision record

The standard states the rule. This page states why the rule is what it is.

They are kept apart because a reader applying the standard wants the rule alone,
while a reader who wants to change it needs what the rule rests on. A rule with
no written reason gets reopened every year.

Only decisions where there was a real disagreement, or a reasonable alternative,
are recorded here. Each carries a date and a status: **settled**, **open**, or
**superseded** by a later decision. Decisions made before the record was dated
are marked *undated*. Read in order, the dated entries are the changelog of the
dictionary's names.

**Measurements.** "GitHub phrase search" is a quoted phrase query against GitHub
code search, run by `tools/measure_display.py`, which caches every count in
`tools/display_measurements.json` under the key `a | b`. Counts are point in
time: they say what the index held on the day they were taken, and are not
re-run. Where a count below has a cache key, the key is given.

---

## Letter names are written as they are said

*Undated · settled*

**Decision:** `noon`, `meem`, `seen` — not `nun`, `mim`, `sin`.

**Why:** `nun` and `sin` are English words with a meaning far from the one
intended. The measurement also shows letter names tend toward the doubled form
(cache keys `nun sakinah | noon sakinah`, `mim sakinah | meem sakinah`):

```text
noon sakinah   478  ×  nun sakinah   118
meem sakinah   308  ×  mim sakinah    57
```

**The boundary:** letter names only. A letter name carries no meaning beyond its
sound, so deriving it throws away the only thing it has; every other term is a
word with a meaning that the derivation keeps.

**Consequence:** the 28 letter names live in `letter_names.tsv`, and the function
reads them from there.

---

## Long vowels are written short

*Undated · settled*

**Decision:** `tajwid`, `sukun`, `tafsir` — not `tajweed`, `sukoon`, `tafseer`.

**Why:** usage favours the short form for terms. These counts were taken before
the cache existed and are not in it; they are point in time:

```text
sukun    289792  ×  sukoon    18432
tafsir   370688  ×  tafseer  115712
tanwin    19968  ×  tanween    4520
tartil    24736  ×  tarteel    7328
```

**Alternative rejected:** doubling everywhere. It contradicts the measurement
for most terms.

---

## `tajwid` goes against its own measurement

*Undated · settled*

**Decision:** `code: tajwid`, even though `tajweed` is about twice as common
(45,440 × 25,280; cache key `tajwid | tajweed`).

**Why:** one steady rule is worth more than an exception that opens a door for
every word.

**Nothing is lost:** `display: Tajweed` is measured from use, and `tajweed` is
recorded in `alternative_spellings`.

---

## A word-final ayn or hamzah echoes the vowel before it

*Undated · settled*

**Decision:** `rubu`, `jama`, `qata`, while `ruku` and `mamnu` stay as they are.

**Why:** deleting them cut the word short, giving `rub`, `jam` and `qat` —
unrelated English words. This is the same problem that made us write `noon`
rather than `nun`.

**Alternatives rejected:** `'` and `ʿ` do not work in identifiers, and `3`
(chat-Arabic for ayn) is not a letter.

**The boundary:** after a long vowel the word already ends in a vowel, so
nothing is added.

---

## `juz` is not derived

*Undated · settled*

**Decision:** `juz`, where the derivation gives `juzu`.

**Why:** the derived form is effectively unused. The count predates the cache:

```text
juz number  1384  ×  juzu number  1
```

**The bar:** a row in `established_spellings.tsv` is accepted only with a
measurement showing the derived form is unused. Usage merely leaning one way is
not enough, or `tajweed` would qualify.

---

## Five established rows rest on a rule, not a count

*2026-09-06 · settled*

**Decision:** `aal` (آل), `taha`, `yasin`, `saad` and `qaaf` stay in
`established_spellings.tsv`, and the standard (§7) states the two rules they
rest on: a name may not open with `al`, and a surah named by its opening
letters is written by letter name.

**Why:** the file's own bar is a measurement, and these 5 have none. For
`aal` the cache points the other way (`al imran | aal imran`: 18,368 × 519), so
the row cannot be defended as usage; it is defended because `al_imran` would
read as an article plus a name, which §8 forbids. The 4 letter-named surahs
cannot be measured at all: the derivation gives `th`, `ys`, `s` and `q`, which
nobody writes.

**Alternative rejected:** a second file for rule-based rows. The function reads
one table, and a second one buys nothing but a second place to look.

---

## The ordinary word in a compound name is translated

*Undated · settled*

**Decision:** `small_meem`, `three_dots`, `rounded_zero` — not `meem_saghirah`,
`thalath_nuqat`, `sifr_mustadir`.

**Why:** `saghirah` adds nothing to `small`. §3 gives a general concept an
English name; a compound is no exception.

**The evidence:** the source registry itself cites them in English —
`standard!dot`, `standard!two-dots`, `standard!three-dots`.

**The boundary:** a technical word stays transliterated however ordinary it
looks; `sakinah` and `lazim` are terms. The ordinary words are listed in
`general_words.tsv`.

---

## Word order in a compound follows English

*Undated · settled*

**Decision:** a translated construct head moves to the end, a translated
adjective moves in front.

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

## The article is judged one pair at a time

*2026-09-06 · settled*

**Decision:** whether a word's `al` is kept is decided against the word
immediately before it, wherever the term opened; a translated head does not
take part:

```text
الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن  → waqf_jaiz_mustawi_al_tarafayn
عَلَامَة الوَقْف اللَّازِم            → waqf_lazim_mark
```

**Why:** the earlier wording of §8 judged the whole term by its first word, so a
construct nested after an adjective lost its `al`. Judging each pair is what
Arabic grammar does, and `translit.py` now does it; the `TOOL_DEFECTS` list that
held the mismatch in `check_conformance.py` is gone.

**Alternative rejected:** keeping the first-word rule and listing the
exceptions. Every three-word name with a nested construct would be an exception.

---

## A one-letter preposition is its own part

*2026-09-06 · settled*

**Decision:** `بِ` and `لِ` written onto a noun are parts of the name, and the
noun keeps its article:

```text
تَفْسِير بِالرَّأْي         → tafsir_bi_al_ray
المَدّ العَارِض لِلسُّكُون  → madd_arid_li_al_sukun
```

**Why:** the noun after a preposition opens a phrase of its own; it is never an
adjective of what precedes, so the pairwise rule would wrongly drop its `al`.
The kasrah on the preposition is what tells `بِالرَّأْي` apart from a word that
happens to begin with `ب`.

---

## Connectives are dropped from the code, not from the Arabic

*2026-09-06 · settled · supersedes the shortened Arabic names of the waqf values*

**Decision:** `مَعَ`, `كَوْن`, `بِحَيْثُ` and `جَوَازًا` are listed in
`connectives.tsv` and dropped by the derivation. The waqf values keep their full
Arabic names: `الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى → waqf_jaiz_wasl_awla`.

**Why:** §14 had stated that connectives are dropped, but nothing implemented
it; the entries passed the derivation check only because their `arabic.vocalized`
had been shortened to the words that survive. That is editing the Arabic to reach
a code name, which §9 forbids. The rule is now in the function, and the names
are whole again.

**The boundary:** a connective is a word that relates two parts and names
nothing. `أَوْلَى` is not a connective; it is what distinguishes the value.

---

## `division_mark`, not `hizb_mark`

*Undated · settled*

**Decision:** `division_mark`.

**Why:** the mark shows the start of a juz, a hizb, and their halves and
quarters, so `hizb_mark` names one of four. The Unicode name
`ARABIC START OF RUB EL HIZB` has the same fault.

**A rule came out of this:** `arabic.vocalized` is not edited to reach a
preferred code name. The source's name is kept in `dabt`, and changing the
concept's name is accepted only on Arabic grounds.

---

## A mark's parent is its family

*Undated · settled*

**Decision:** `harakah`, `tanwin`, `ijam`, `orthographic_mark` and `qiraah_mark`
are parents; `mushaf_mark` stays the parent of what has no family.

**Why:** every mark hung off `mushaf_mark` while `mark_family` carried the real
grouping. The entry held two taxonomies that disagreed, and one parent over
every mark in the registry says nothing.

**`mark_family` stays.** It is the source registry's grouping, and it is kept as
what the source says; `parent` is the standard's taxonomy. The two differ in name
where the registry's word differs from ours (`imlaiyyah`, `alamat_qiraah`).

---

## Waqf marks are values, not marks

*Undated · settled*

**Decision:** `waqf_lazim` and its siblings are `kind: classification_value`
with `parent: waqf_mark_type`, and they carry `symbol`, `unicode` and
`mark_family` because they are drawn.

**Why:** `waqf_mark_type` was a classification with no values, and §27's own
example gives `waqf_lazim` exactly this shape. The data contradicted the
standard's own example.

**The boundary:** these 6 are the only non-marks that carry the drawing
fields, and `check_conformance.py` refuses the fields anywhere else.

---

## `waqf_ruling` and `waqf_mark_type` are two classifications

*2026-09-06 · settled*

**Decision:** `waqf_ruling` (tamm, kafi, hasan, qabih) classifies the place;
`waqf_mark_type` (lazim, mamnu, the jaiz kinds, muanaqah) classifies what a
drawn mark points to. Both are entries, and §13 and §17 name them side by side.

**Why:** the two had been treated as one "waqf type" in the standard's examples,
with English labels that matched neither. A place with no mark still has a
ruling, and a mark's type is read from the mushaf, not inferred from the
grammar, so a model needs both.

---

## `parent` is *is-a*; containment is `part_of`

*2026-09-06 · settled*

**Decision:** `parent` says what a thing is a kind of. What a thing is inside —
a rubu al-hizb in a hizb, a mushaf edition in a mushaf — is `part_of`, a new
optional field.

**Why:** 3 entries had used `parent` for containment, so a reader of the
taxonomy found a rubu al-hizb listed as a kind of hizb. One field with two
meanings cannot be checked; two fields can.

---

## Duplicated concepts are merged

*Undated · settled*

**Decision:** one entry each for `sajdah_mark` and `division_mark`.

**Why:** `alamat_mawdi_al_sajdah` and `sajdah_mark` defined the same thing, as
did `alamat_al_tahzib` and `division_mark`.

**Consequence:** the former name is recorded in `deprecated` on the surviving
entry with a `note`, and still resolves through `aliases.json`, so a project
that adopted it is not stranded (§20).

---

## A codepoint is not a mark's identity

*Undated · settled*

**Decision:** a codepoint is not used as the identifier of a mark.

**Why:** one character serves two marks, and one mark has more than one
character:

```text
U+06DC   ARABIC SMALL HIGH SEEN   →  saktah_mark  or  seen_al_qiraah
sukun    U+0652  and U+06E1
```

---

## The derivation is not reversible, by design

*Undated · settled*

**Decision:** `ص` and `س` are both `s`; `ض` and `د` are both `d`.

**Why:** the aim is a stable identifier, not an accurate pronunciation. Precise
transliteration belongs in `names.transliteration`.

---

## `taa` and `haa` name two letters each

*Undated · open*

**Question:** `ت` and `ط` both give `taa`, and `ح` and `ه` both give `haa`,
because the derivation merges emphatic and plain letters. Neither name is used
by any entry.

**Status:** open. It is decided when an entry needs one of them.
`build_aliases.py` fails if two concepts ever claim one of these names, so the
clash cannot arrive unnoticed.

---

## The plural is the code plus `s`, whatever the code

*2026-09-06 · settled*

**Decision:** the `s` is added to the whole code name, a construct included:

```text
juz              → juzs
hizb             → hizbs
mawdi_al_sajdah  → mawdi_al_sajdahs    not mawadi_al_sajdah
harf_muqatta     → harf_muqattas
```

**Why:** the plural is a collection name for code, not an English word for a
reader. Pluralising the head of a construct would need Arabic morphology in the
function, and pluralising the English gloss would need a gloss. The one rule a
reader can predict is `+ s`.

**Alternative rejected:** irregular plurals for the awkward cases. Every
exception is a lookup, and the collection name is the one name a developer
types without looking.

---

## A ta marbutah in a construct is `t`

*Undated · settled*

**Decision:** `hamzat_al_wasl`, `sajdat_al_tilawah` — not `hamzah_al_wasl`.

**Why:** the ta marbutah is pronounced `t` when the word is bound to the next,
and the code follows the sound as it does for letter names. The `h` form is
common in English writing and is recorded in `alternative_spellings`.

---

## `al-` is never assimilated

*Undated · settled*

**Decision:** one form of the article, whatever letter follows it:

```text
al-Shams            not ash-Shams
sajdat_al_tilawah   not sajdat_at_tilawah
```

**Why:** assimilation to a sun letter is a rule of pronunciation, and the code
spelling is an identifier, not a pronunciation. One form of the article means
the article can be found and removed by a program; 14 forms cannot.

---

## `origin` has three values and `tier` has two

*Undated · settled*

**Decision:** `origin` is `quranic`, `borrowed` or `standard`; `tier` is `core`
or `extended`.

**Why:** `origin` decides whether the Arabic name is required and whether the
code is derived — a borrowed term such as `glyph` has no Arabic to derive from,
and a `standard` concept such as `ayah_timing` has no Arabic name at all. `tier`
answers a different question, what applications actually store, and mixing it
into `origin` would make a rarely stored Quranic term look borrowed.

**Alternative rejected:** a single `type` field. It would answer neither
question cleanly.

---

## `mushaf_marks` is merged into `dabt`

*2026-09-06 · settled · supersedes the 20-domain list*

**Decision:** the category `mushaf_marks` is removed; every mark is `dabt`.

**Why:** the domain glossed "the marks of the mushaf" held one entry,
`mushaf_mark`, while the marks themselves were all in `dabt`. §25 says a domain
is not added before there are concepts that belong to it, and this one never had
them.

---

## The dictionary is generated from the entries

*Undated · settled*

**Decision:** the dictionary page is generated from `concepts/*.yml`.

**Why:** it had been written by hand, duplicating the source of truth, which is
what §29 forbids.

---

## `waqf_al_muanaqah`, not `taanuq_al_waqf`

*Undated · settled*

**Decision:** the mark at U+06DB is `waqf_al_muanaqah` — وَقْف المُعَانَقَة.

**Why:** `dabt_marks.tsv` names the mark وَقْف المُعَانَقَة and records
تَعَانُق الوَقْف only as what the mushaf introduction calls it. The registry's
name is the concept's name, and it puts the value beside its siblings —
`waqf_lazim`, `waqf_mamnu` and the 3 `waqf_jaiz_*` values — instead of leaving
it the one that did not lead with `waqf`.

**No Arabic was edited to reach the name.** The name taken is the one the
registry already gives.

**The `al` stays.** The first word is indefinite, so the term is a construct
and its article is part of the name — the `rubu_al_hizb` rule.

**Alternative rejected:** `waqf_muanaqah`, which drops the `al` by treating the
term as two words that each lose their own article. That patches the derivation
to reach a preferred string.

**A purpose name was rejected:** `paired_waqf` and `embracing_waqf` were
considered. §3 keeps a scholarly term, and `muanaqah` is a term of waqf exactly
as `lazim` is — neither is in `general_words.tsv`. `division_mark` is not a
precedent for them: it went to English because the Arabic name was wrong about
the concept, and this one is not.

**Nothing is stranded:** `taanuq_al_waqf`, `muanaqah`, `muraqabah` and
`waqf_al_muraqabah` all resolve through `aliases.json`.

---

## The tanwin marks are named by their harakah

*Undated · settled*

**Decision:** `tanwin_al_fath`, `tanwin_al_kasr`, `tanwin_al_damm` — تَنْوِين
الفَتْح, تَنْوِين الكَسْر, تَنْوِين الضَّمّ.

**Why:** measurement. The case names are effectively unused in Latin script, and
lose in Arabic too (cache keys `tanwin fath | tanwin al-nasb`, `tanwin kasr |
tanwin al-jarr`, `tanwin damm | tanwin al-rafa`, `تنوين الفتح | تنوين النصب`,
`تنوين الكسر | تنوين الجر`; the Arabic damm pair was rate-limited and is
uncounted):

```text
tanwin fath   618  ×  tanwin al-nasb    0
tanwin kasr   551  ×  tanwin al-jarr    0
tanwin damm   492  ×  tanwin al-rafa    0

تنوين الفتح   217  ×  تنوين النصب     184
تنوين الكسر   161  ×  تنوين الجر       21
```

**The registry agrees with the measurement:** its own file ids are `تنوين فتح`,
`تنوين كسر`, `تنوين ضم`. The case names it writes in the dabt column stay in
`dabt` — `تَنْوِين الخَفْض — الكَسْرَتَان`.

**Alternative rejected:** naming the triad by case (nasb, jarr, rafa). Usage
decides, and usage went the other way.

**Nothing is stranded:** `tanwin_al_nasb`, `tanwin_al_jarr`, `tanwin_al_khafd`,
`tanwin_al_rafa`, `fathatan`, `kasratan`, `dammatan`, and the registry's
`tanwin_fath`, `tanwin_kasr`, `tanwin_damm` all resolve.

---

## The standard names the Quran's sciences and stops there

*Undated · settled*

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
standard does not give them, and says so, and §30 says how a project extends the
dictionary locally.

---

## Ayah numbering values keep their parent's name

*Undated · settled*

**Decision:** `ayah_numbering_kufi`, `ayah_numbering_madani_awwal` — not `kufi`
and `madani_awwal`.

**Why:** two reasons, and either alone is enough.

The derivation of the Arabic name does not survive. العَدّ الكُوفِيّ gives
`add_kufi`, and `add` is an English verb — the same fault that made us write
`noon` rather than `nun`.

And the short name is taken. `makki` is already a value of
`revelation_classification`, so العَدّ المَكِّيّ cannot be `makki` without two
concepts claiming one name, which `build_aliases.py` refuses.

**This is §14, not an exception to it:** a value's name is its parent's name
plus what distinguishes it, and the parent's name is dropped only when it
distinguishes nothing. Here it distinguishes a great deal. `waqf_jaiz_wasl_awla`
has the same shape.

**A second gain:** `kufi` alone would collide in a reader's head with the Kufic
script, which is a real term in mushaf work.

---

## `ayah_mark`, with the dabt name kept in `dabt`

*Undated · settled*

**Decision:** `code: ayah_mark`, `names.arabic.vocalized: عَلَامَة الآيَة`, and
the dabt name عَلَامَة رَأْس الآيَة recorded in `dabt`.

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

*Undated · settled*

**Decision:** one entry, `naskh`.

**Why:** the familiar title is النَّاسِخ وَالمَنْسُوخ, and it derives to
`nasikh_walmansukh` — a conjunction welded into an identifier. The science is
النَّسْخ, and الناسخ والمنسوخ are the two sides of one relation, not two concepts.

**Nothing is lost:** `nasikh_mansukh`, `nasikh_wa_mansukh` and `nasekh_mansokh`
all resolve through `aliases.json`.

---

## Token, morpheme and font get entries

*Undated · settled*

**Decision:** entries for `token`, `morpheme`, `stem`, `part_of_speech` and
`font`.

**Why:** §18 tells the reader to keep `word`, `token` and `morpheme` apart, and
lists `font` under presentation. None of the 4 had an entry, so the standard
was naming a distinction it declined to define, and `morphology.purpose` already
used the word `token` in its own text.

**The boundary that mattered:** a token is what a splitting method produces, and
a word is what a reader recognises. Changing the method changes the token count
and not the word count. `segment`, the name the Quranic corpora use, resolves to
`morpheme`.

---

## `harf_al_mana` for the particle, because `harf` is the letter

*Undated · settled*

**Decision:** the three parts of speech are `ism`, `fil` and `harf_al_mana`.

**Why:** حَرْف names two different things, and the dictionary had already given
the name to one of them — `harf` resolves to `letter`, a unit of written text.
The part of speech is حرف المعنى, as against حرف المبنى, and the tradition
already draws that line, so we did not have to invent one.

**Why only 3:** the Quranic corpora tag with dozens of labels — `N`, `PN`,
`V`, `CONJ`, `NEG`. Those are data that sit under these three, not entries.
Naming 40 tags would put the standard in the business of maintaining a
tagset.

**What it fixed:** `part_of_speech` had been added as a classification with no
values, which is the fault §13 names, and the same fault that had left
`ayah_numbering_system` empty. The check now refuses it.

---

## The standard's own rules are checked, not remembered

*Undated · settled*

**Decision:** `tools/check_conformance.py` runs the rules the prose states —
that a quranic code is the derivation of its Arabic name, that a classification
has values, that a plural is the code plus `s`, that a `related`, `parent` or
`part_of` link resolves, that a gloss is not a spelling, that every cited source
exists, that the drawing fields sit only on marks and the 6 waqf values.

**Why:** `validate.py` checks the shape of an entry against `schema.json`, and
the schema cannot express any of the above. Everything in this list was found
the first time the check was run, on entries that had passed validation for
months: a plural taken from the English gloss, two `related` links pointing at
concepts that do not exist, and a gloss doubling as an alternative spelling.

**One list.** `DOCUMENTED` holds departures this record argues for, such as the
ayah numbering values. A mismatch caused by the function is a defect to fix in
the function, not a list to keep; the one such list the check once had is gone
(see "The article is judged one pair at a time").

---

## A closed set of members goes to a registry, not to an entry each

*Undated · settled*

**Decision:** the 10 qiraat, the 20 riwayahs, the 114 surahs and the 15 places
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

## The rules of tajwid are a registry, not entries

*2026-09-06 · settled*

**Decision:** the rules — izhar, idgham, iqlab, ikhfa, the kinds of madd and
the rest — are rows in `registries/tajwid_rules.tsv`; `tajwid` names the
registry. The concepts a rule rests on (`noon_sakinah`, `tanwin`, `maddah`)
stay entries.

**Why:** the standard had 5 entries in `tajwid` and a rules file
(`data/tajweed_engine_rules.json`) nobody cited, while every tajwid engine ships
its own rule ids. A rule has a name, a trigger and a source and nothing else to
say; that is the registry test. And a rule is not the place where it applies:
an occurrence is a span of text tagged with the rule's code, and belongs to the
project's data, not to the dictionary.

**Alternative rejected:** an entry per rule. There are dozens, their
definitions would restate their names, and the engines would still need a table.

---

## `rasm_imlai` keeps the name every codebase uses

*2026-09-06 · settled*

**Decision:** `rasm_imlai` — الرَّسْم الإِمْلَائِيّ — although `general_words.tsv`
translates إملائي for the mark family (`orthographic_mark`).

**Why:** the type of rasm is called `imlai` in every codebase that has one, and
`orthographic_rasm` is a name nobody writes. The table's `with_head` role says
when the word is translated: only beside a head word such as عَلَامَة. Beside
رَسْم it is transliterated, so the derivation gives `rasm_imlai` and the entry
is not an exception.

**Nothing is stranded:** `imlaei`, `imlai`, `simple` and `text_simple` resolve.

---

## `ayah_count` is a standard concept named after its registry

*2026-09-06 · settled*

**Decision:** `ayah_count`, `origin: standard`, Arabic عَدَد الآيَات, registry
`ayah_counts`.

**Why:** the derivation of the Arabic gives `adad_al_ayat`, which names the
number in Arabic and nothing in code. The concept is a modelling one — a count
per surah per numbering system — so it takes the English name its registry
already has, and sits in the `ayah_numbering_*` family it belongs to.

---

## A tariq registry at the level applications store

*2026-09-06 · settled · supersedes "the same rule refused a tariq registry"*

**Decision:** `registries/tariq.tsv` has 4 rows — `shatibiyyah`,
`tayyibat_al_nashr`, `durrah`, `taysir` — the routes a recording or a mushaf
edition actually declares.

**Why:** the ~980 routes of al-Nashr cannot be verified row by row from the
sources in this repository, so the registry was refused. But applications store
the route at the level of the transmission work, and those 4 are attested and
enumerable. A registry that stops where the evidence stops is honest; one that
enumerates 980 unverified rows is not.

**Open:** the full enumeration of the tariqs, when a source that a tool can
reconcile is found.

---

## A person's name is not derived

*Undated · settled*

**Decision:** `hafs`, `warsh`, `qalun`, `ibn_dhakwan` — written as they are
commonly written, not put through §4–§8.

**Why:** the derivation is there because a term is a word carrying a meaning,
and working from the vocalised Arabic keeps that meaning attached to the
identifier. A name has no such meaning, so deriving it only produces a spelling
nobody writes.

**Where the derivation fails on names:** `أَبُو عَمْرو` derives to `abu_amrw`,
because the waw of عمرو is orthographic and silent; `ابْن` cannot be derived at
all, because its initial alif is hamzat al-wasl and carries no vowel to read.

**Alternative rejected:** forcing names through `established_spellings.tsv`.
The derivation was never meant for names, and patching it for them is worse than
exempting them.

**The boundary:** people, and nothing else. A surah name is a word, so it is
derived, and `check_registries.py` re-derives all 114 on every run.

**Evidence, not preference.** "Commonly written" is the scholarly English form
with its diacritics dropped, and the registry carries both. Where that form
disagrees with a rule the standard already states, the rule wins — `shubah`, not
`shuba`, because §5 governs a ta marbutah.

**Alternative rejected:** GitHub phrase counts. They decide between `tajwid` and
`tajweed` because both are terms; on names they return noise (`susi` matched
5,185,536 unrelated tokens, and `qumbul` beat `qunbul`). The counts are not in
the cache and are not evidence.

---

## A member may share a name with a concept

*Undated · settled*

**Decision:** `hamzah` is the mark and also the reciter; `tariq` is a step in a
chain of transmission and also a surah. Both keep the name. Member names are
indexed by kind in `registry_aliases.json`, and the bare name in `aliases.json`
goes on resolving to the concept.

**Why:** the two live in different domains in the sense of §25 — one `hamzah` is
`dabt`, the other `qiraat` — so nothing can reach for both at once. A name only
has to be unique where it could actually be confused.

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

## Ayah counts are read from al-Bayan and reconciled

*Undated · settled*

**Decision:** `registries/ayah_counts.tsv` holds the count of every surah in all
6 numbering systems, generated by `tools/extract_ayah_counts.py` from al-Dani's
al-Bayan. It is never edited by hand.

**Why not a table from elsewhere:** the 6 systems disagree about 114 numbers,
and a table with no source cannot be argued with. Al-Bayan states each surah's
count once and then gives only the part that differs — "285 in the two Madinans,
the Makkan and the Damascene, and six in the Kufan, and seven in the Basran" —
so the numbers exist in the book in a form a tool can read.

**Why it can be trusted:** it reconciles in two ways. All 114 Kufi counts match
the printed mushaf surah by surah, which tests the reading of every section
rather than the arithmetic; and Kufi sums to 6236 and Basri to 6204, the totals
al-Dani himself states.

**What the reconciliation fixed**, each now a rule in the extractor:

- `آيتان` is the numeral two fused with its noun, and is counted.
- `وآية` conjoined is the numeral one — "fifty and an ayah" is 51 — while a bare
  `آية` after a number is the counted noun.
- A later part replaces the trailing part it covers: 110 and "nine" is 109; but
  180 and "two" is 182, because a round ten from 20 upward takes a unit beside it
  while a bare 10 is replaced.
- A two-word school name is one token.
- An aside inside a run of school names — "with a variance reported from him" —
  does not break the run.

Totals alone would have hidden most of these; the surah-by-surah check found
them.

**The residual is disclosed, not smoothed.** Four columns come to one more than
the total al-Dani states. Two places in the book give a count for the reading of
Abu Jafar specifically, and whether "the count of Abu Jafar" is the Madani Awwal
system or an authority beside it is a question about the source. A tool should
not decide it, so the run prints the discrepancy every time.

---

## `verified` says what was checked; `no` is allowed

*Undated · settled*

**Decision:** a registry row says what has actually been checked. The sajdah
rows carry `verified: surah`, which means the surah is attested in a source and
the ayah number is not.

**Why:** the alternative is a citation that gestures at a page which does not in
fact contain the claim. That is worse than an honest blank, because it cannot be
distinguished from a real one later.

**What that produced here:** al-Itqan names all 14 sajdah surahs and gives the
count as 14, which was checked against the book. 15 places in 14 surahs is not a
contradiction — al-Hajj carries two. Every ayah number is checked against the
verified Kufi count for its surah, so a reference outside its own surah cannot
pass, and two of them land on the last ayah of the surah, which the counts
confirm. What no source in this repository does is enumerate the 15 numbers,
and the file says so.

**The same rule refused a tariq registry for a time.** The counts could be
proved because they reconcile to a total; the tariqs have no such total. A scan of
al-Nashr's isnad section returns 224 distinct names at every depth of the tree
with no reliable way to attach each to its parent, and an unverifiable table
looks exactly like a verified one. `registries/tariq.tsv` now exists with
`verified` set honestly per row, and `check_registries.py` reports what remains
unverified on every run.
