# Terminology survey — quranpedia.net

Status: draft
Surveyed: 2026-09-06
Subject: `~/Documents/Github/quranpedia.net` (Laravel, MySQL, 267 migrations, 65 Eloquent models, 83 tables — 77 of them domain tables)
Measured against: `standards/terminology/` (117 concepts at the time; 146 after §1a) and `content/en/reference/standard.md`
See also: `OPEN.md` for what this survey raised that is still undecided; a section overtaken by a later decision says so at its head

---

## 1. Method

Terms were extracted from the four layers the standard binds (§26):

| Layer | Source | Extracted |
|---|---|---|
| Database | `database/migrations/*.php` | 83 tables, ~430 columns |
| Models | `app/Models/*.php` | 66 classes and their relations |
| Routes / API | `routes/{web,api,api-public}.php` | 292 URIs |
| Data values | `backups/quranpedia_20260301_035945.sql.gz` | lookup tables: `counts`, `qiraas`, `rawis`, `recitation_types`, `recitation_classifications`, `person_types`, `book_types`, `attachment_types`, `options`, `languages` |

Each table and model name was resolved against `standards/terminology/aliases.json`.

**Result: 10 of 77 domain tables resolve to a concept in the dictionary.**

Resolved: `ayahs`, `juzs`, `mushafs`, `qiraas`, `rawis`, `recitations`, `reciters`, `surahs`, `tafsirs`, `words`.

Unresolved: the other 67 — see §4.

That number is the headline of this survey. It does not mean quranpedia is 87% wrong; it means the dictionary today covers the Quranic text and the mushaf, and covers almost nothing of the scholarly-content layer that a Quranic encyclopedia is actually made of.

---

## 1a. What was done about it

The standard was changed on 2026-09-06. Twenty-nine entries were added and one
domain (`quranic_sciences`) was opened. The dictionary now holds 146 concepts,
and `tools/check_conformance.py` now tests the rules the standard states in
prose — which nothing had been testing.

Two screens were then walked field by field, because a survey of table names
misses what a product actually puts in front of a reader:

**The surah info card** (`resources/data/surah-info/*.json`, all 114 surahs)
carries eleven fields. Eight were covered or out of scope; three were neither,
and were added: `fadail_al_quran` (فضلها), `maqasid_al_surah` (مقاصدها) and
`asma_al_surah` (أسماؤها). Its `ayahs_count` block lists five numbering systems,
not six — العد المكي is absent — and names the Damascene one العد الشامي, which
resolves through `shami`.

**The ayah modal** has seventeen tabs (`EmbedController::VALID_TYPES`). Two were
missing and were added: `tadabbur` (الوقفات التدبرية) and `tafsir_mathur`
(موسوعة التفسير بالمأثور). The tab labels also confirmed two naming choices made
above from the table names alone: `meanings` is labelled غريب القرآن, and
`similar` is labelled المتشابهات.

| Added | Category |
|---|---|
| `token`, `morpheme`, `stem`, `part_of_speech`, `ism`, `fil`, `harf_al_mana` | `text`, `linguistics` |
| `font` | `mushaf` |
| `ayah_mark` | `dabt` |
| `mawdi_al_sajdah` | `structure` |
| `ayah_numbering_{madani_awwal, madani_akhir, makki, basri, dimashqi, kufi}`, `equivalent_ayah` | `ayah_numbering` |
| `naskh`, `gharib_al_quran`, `sabab_al_tasmiyah`, `mutashabihat` | `quranic_sciences` |
| `nuzul` | `revelation` |
| `fadail_al_quran`, `maqasid_al_surah`, `asma_al_surah`, `tadabbur` | `quranic_sciences` |
| `tafsir_mathur` | `tafsir` |
| `mufassir` | `tafsir` |
| `ayah_timing` | `recitation` |

**Declined, deliberately:** `book`, `author`, `chapter`, `attachment`,
`category`, `tag`, `language`, `source`, `radio`, `fatwa`, `note`, `topic`,
`saying`, `quran_qa`, `recitation_granularity`. A concept belongs in this
standard when it cannot be defined without referring to the Quran or the mushaf.
A stream of Quran audio is a stream; a fatwa about an ayah is a fatwa. The line
and its consequence — that a project still needs its own names for these, and
the standard says so rather than staying silent — are recorded in the decision
record under *The standard names the Quran's own sciences, and stops there*.

This changes what the 10-of-77 number means, and §4 below is now the reading to
keep: most of the gap was never the standard's to fill.

The inclusion rule is now written into the standard itself, at the head of §30:
**a concept belongs here when it cannot be defined without referring to the
Quran or the mushaf.** Seven decisions came out of the work and are written up in
`content/{ar,en}/reference/decisions.md`: the scope rule, why the numbering
values keep their parent's name, why `ayah_mark` takes the shorter Arabic name,
why `naskh` is one entry rather than two, why `token` and `font` had to be
defined, why the particle is `harf_al_mana`, and why the rules are now checked
rather than remembered.

Running that new check for the first time found four faults that had passed
`validate.py` for months, three of them older than this work: `harf_muqatta`
took its plural from its English gloss; `makki` and `tajwid` each had a
`related` link pointing at a concept that does not exist (`nuzul` — now added —
and `tilawah`, which is an alternative spelling of `recitation`); and
`part_of_speech`, added above, was a classification with no values, which is the
fault §13 names and the one this survey raised against `ayah_numbering_system`.
All four are fixed. A fifth is a defect in `translit.py`, not in an entry, and
is recorded as such.

Everything in §2 is still quranpedia's to fix, and §5's open questions are still
open.

---

## 2. Findings that are quranpedia's to fix

Naming conflicts with rules the standard already fixes. Ordered by how much they cost.

### 2.1 `rawi` is used where `riwayah` is meant — §17, §18

`mushafs.rawi_id` and `recitations.rawi_id` both point at `rawis`. A mushaf is not printed after a *person*; it is printed after a *riwayah*. The data itself says so — `rawis.translated_name` holds values like `"Rewayat Qalon A'n Nafi' Men Tariq Abi Nasheet"`, i.e. a riwayah name, and the `tariq` too, stored on a row that claims to be a person.

The standard fixes this boundary explicitly: `Rawi ≠ Reciter`, and `rawi` (role, qiraat) is a separate entry from `riwayah` (concept, qiraat).

Three concepts are collapsed into one table:

```text
rawi      the transmitter          a person
riwayah   what he transmitted      a text tradition
tariq     the route to him         a chain below the riwayah
```

Fix: `riwayahs` table keyed to `qiraahs`, with `rawi_id` pointing at `people`; `mushafs.riwayah_id` and `recitations.riwayah_id`. `tariq` gets its own column or table.

This is the one finding with a correctness consequence rather than a cosmetic one: any query that means "all recitations in Warsh" currently means "all recitations by the man Warsh", and the two stop agreeing the moment a second riwayah of the same rawi is loaded.

### 2.2 `counts` is the ayah-numbering system — §10, §21

`counts` holds المدني الأول، المدني الأخير، المكي، البصري، الدمشقي، الكوفي. That is `ayah_numbering_system`, which exists in the dictionary. `count` is exactly the vague name §10 rules out, and it collides with the ordinary meaning of a count (a number of things). `differences` and `equivalent_ayahs` hang off it and inherit the vagueness.

Fix: `ayah_numbering_systems`, `qiraahs.ayah_numbering_system_id`, and rename `differences` to something that says what differs (see §4.3 below — the concept it needs is missing from the standard too).

### 2.3 `revelation_type` stores English glosses — §3, §13, §19

```php
$table->enum('revelation_type', ['meccan', 'medinan'])
```

Three violations in one line:

- The classification is `revelation_classification`, not `..._type` (§24: name the classification, don't call it "type").
- The values are `makki` and `madani`. `meccan` / `medinan` are English glosses (§19), and glosses are not identifiers.
- The enum has no `disputed` value, though the dictionary has the entry and the disagreement is real for several surahs.

The API surfaces this to the public: `/api/v1/surahs` returns `"revelation_type": "meccan"`.

Neighbouring `revelation_order` is correct and matches the standard — worth saying, because it shows the rest was a slip rather than a different model.

### 2.4 `recitation_types` is the recitation *style* — §13, §24

`recitation_types` holds مرتل / مجود / معلم — that is the dictionary's `recitation_style`, whose three values `murattal`, `mujawwad`, `muallim` are already first-class entries.

Separately, `recitation_classifications` holds حسب السور / حسب الآيات. That is not a classification of the recitation at all; it is the granularity at which the audio is cut. Calling it a classification puts two unrelated things under one word.

quranpedia models no `recitation_pace` (تحقيق / تدوير / حدر) at all, although the dictionary carries all three. That is a gap in the app, not in the standard.

### 2.5 Canonical Code Spelling is not applied — §4–§7

| In quranpedia | Standard | Rule |
|---|---|---|
| `e3rab` (route, `options.key`, 15 occurrences) | `irab` | §7 — no digit-for-ayn |
| `tajweed` (`options`, `ayahs.tajweed`, `/tajweed-rules`) | `tajwid` | §6 — and the standard names this as its one deliberate exception |
| `Qiraa` model, `qiraas` table, `qiraa_id` | `qiraah`, `qiraahs` | §5 — ta marbutah gives `h` |
| `asbab-nuzool` (route) | `asbab_al_nuzul` | §6, §8 |
| `nasekh_and_mansokhs` (table) | `nasikh_mansukh` | §6 |
| `sabab_alnzool`, `sabab_altasmyah` (`surah_infos`) | `sabab_al_nuzul`, `sabab_al_tasmiyah` | §6, §8 |
| `tafseer` (`books.tafseer`) | `tafsir` | §6 |
| `sajda-ayahs` (route) | `sajdah` | §5 |
| `mohaqeq`, `nasher` (`books`) | `muhaqqiq`, `nashir` | §6 |
| `Meaning` / `meanings` | see §4.4 — the concept is missing | — |

`e3rab` and `tajweed` are the two that leak furthest: both are in `options.key`, which is a public feature slug, and both appear in URLs.

### 2.6 One concept, several names across the layers — §26

```text
irab:      DB —            route /e3rab        option key 'e3rab'      Arabic الإعراب
tafsir:    DB tafsirs      route /tafsir       column books.tafseer    config tafsir-books
qiraah:    DB qiraas       route /qiraat       model Qiraa
mushaf:    DB mushafs      route /mushaf, /quran/{mushaf}
```

The `/quran/{mushaf}` route is worth its own line: `Quran ≠ Mushaf` is a boundary the standard states outright (§17), and the route uses the two as one word.

### 2.7 `id`, `number`, `position`, `order` are used as synonyms — §21

- `differences.ayah_number` and `differences.surah_number` sit beside `differences.surah_id` in the same table, for the same thing.
- `tafsirs.surah_number` vs `contents`/`meanings`/`quran_translations` using `surah_id`. Both are the surah's established number 1–114; two names for one thing.
- `quran_word_segments` carries `word_index`, `word_number` *and* `segment_number`; `quran_word_syntax` carries `word_number` and `token_number`. Whether `word_index` is 0-based and `word_number` 1-based is not recoverable from the names.
- `books.index`, `topics.letter`, `contents.part` — `index` and `part` are the vague names §10 warns about.

### 2.8 Vague names — §10

`contents`, `options`, `counts`, `classifications`, `differences`, `similarities`, `sources`, `imports`, `messages`, `Content`, `Meaning`, `Saying`. Several of these are real concepts wearing a generic word; §4 proposes names for them.

---

## 2a. The two screens, field by field

§2 above is about table and column names. This section is about the two surfaces
a reader actually meets, and it is a rename list rather than a discussion:
**`surveys/quranpedia-net-renames.tsv`** — 43 fields, of which **35 change**.

Being covered by an entry and having the right name are different things. Every
row of the surah info card was "covered" in the sense that the standard has a
concept for it; only one of the eleven field names was already correct.

### The surah info card

```text
introduction  → summary                    §10   names a position, not the content
surah_number  → surah_number               §21   correct as it stands
surah_type    → revelation_classification  §24   a classification is never called `type`
words_count   → word_count                 §11   singular for the thing counted
descent       → revelation_order           §3    a literal rendering of نزول
grace         → fadail_al_quran            new   `grace` carries a sense فضل does not
prophet       → prophetic_guidance         §10   a person named as content about him
revelation    → asbab_al_nuzul             §26   holds the causes, not the revelation
topics        → topics                     —     correct, and outside the standard
purposes      → maqasid_al_surah           new   collides with the entry field `purpose`
asmaoha       → asma_al_surah              §4    an Arabic pronoun suffix in an identifier
ayahs_count   → ayah_numbering             §11   a list per system, not a count
```

Three faults are in the shape rather than the names.

**`{title, value}` wraps every field.** `title` is the Arabic label, repeated
identically across all 114 files, and `value` is one of the vague names §10 rules
out. The label is presentation; §29 says the human-readable form is generated
from the data, not stored beside it eleven times over.

**Every value is a string.** `surah_number: "2"`, `descent: "87"`,
`words_count: "6140"` — established numbers stored as text (§21).

**`surah_type` holds `"مدنية"`.** An Arabic display string standing where a
classification value belongs; the value is `madani` (§19).

And inside `ayahs_count`, `{title: "العد المدني الأول", value: 285}` uses a
display label as a key. It should be `ayah_numbering_system:
ayah_numbering_madani_awwal` with `number_of_ayahs: 285` — the second half
because **`surahs.number_of_ayahs` already names that exact fact in the same
application**, which is §26 broken inside one product rather than across two.

### The ayah modal

Nine of seventeen tab keys change:

```text
library  → books           §10        e3rab   → irab             §7
asbab    → asbab_al_nuzul  §8 §26     nasekh  → naskh            §6
meanings → gharib_al_quran §26        notes   → tadabbur         new
fatwa    → fatwas          §11        qiraat  → qiraahs          §5 §11
similar  → mutashabihat    §26        sayings → tafsir_mathur    new
tajweed  → tajwid          §6
```

`tafsir`, `topics`, `translations`, `attachments`, `surah_info` and
`surah_resources` are already right.

`qiraat → qiraahs` is the one that looks like a regression and is not: قراءات is
an Arabic plural, and §11 rules those out as collection names for the same
reason it rules out `ayat` and `suwar`.

---

## 3. Findings that are the standard's to fix

These are concepts quranpedia stores in production and the dictionary has no entry for. They are ordered by how much of the app they carry.

### 3.1 The scholarly-content layer is absent — the largest gap

*Partly closed: `naskh`, `gharib_al_quran`, `sabab_al_tasmiyah` and `mutashabihat` added under `quranic_sciences`. `fatwa`, `note`, `topic`, `saying`, `quran_qa` and `surah_info` declined as outside the standard's subject.*

The dictionary has `tafsir`, `translation`, `transliteration`, `spoken_translation`, `asbab_al_nuzul` under `content`. quranpedia stores nine more kinds of content attached to the text, all of them with their own tables, routes and public URLs:

| Concept | quranpedia | Proposed entry |
|---|---|---|
| فتوى | `fatwas` (with `question`, `answer`, `source_url`) | `fatwa` — kind `content`, category `fatwa` |
| فائدة / تعليق | `notes` | `note` |
| موضوع | `topics` (hierarchical, `parent_id`, `merged_into_id`) | `topic` |
| أثر / قول | `sayings` | `athar` or `saying` |
| ناسخ ومنسوخ | `nasekh_and_mansokhs` | `nasikh_mansukh` |
| معاني الكلمات / غريب القرآن | `meanings`, `quran_meaning_words`, `/gharib` | `word_meaning`, `gharib_al_quran` |
| سؤال وجواب | `quran_qa_items`, `quran_qa_chapters`, `quran_qa_sources` | needs a decision — see §5 |
| سبب التسمية | `surah_infos.sabab_altasmyah` | `sabab_al_tasmiyah` |
| فضائل / معلومات السورة | `surah_infos` | `surah_info` or several entries |

Without these, a project following the standard has no guidance the moment it stores anything beyond the text itself — which is most of what a Quranic application does.

### 3.2 The library layer is absent

*Declined, except `mufassir`, which is added. A book is a book; the standard has no better name for one than the language already does.*

`books`, `authors`, `people`, `chapters`, `contents`, `attachments`, `related_books`, `categories`, `sources` — 9 tables and roughly a quarter of the app. The dictionary has no `book`, `author`, `chapter`, `edition`, `manuscript`, `attachment`, `source`.

`tafsir` is in the dictionary as content, but the *book* the tafsir is published in has no entry, so `tafsirs.book_id` points at a concept the standard does not name.

Related: `person_types` in production holds مؤلف، محقق، مقدم، مراجع، قارئ، مترجم. The dictionary has three roles (`muqri`, `rawi`, `reciter`). Missing roles: `author`, `muhaqqiq`, `translator`, `reviewer`, `introducer`, `narrator`, `mufassir`. The standard has a `role` kind and §13 says values get their own entries; these qualify.

### 3.3 Mutashabihat and ayah relations are absent

*Closed: `mutashabihat` and `equivalent_ayah` added. `ayah_numbering_difference` was not: `equivalent_ayah` already carries the join, and a second entry for the same fact would be the flat list §12 warns about.*

Seven tables and no concept:

```text
mutashabihat_identical_ayahs        آيات متطابقة
mutashabihat_phrases                عبارات متكررة
mutashabihat_phrase_ayahs
shared_phrases
similar_ayahs                       with score, coverage, matched_words_count
ayah_similarities / ayah_similarity
equivalent_ayahs                    same ayah under a different numbering
```

Proposed entries: `mutashabihat` (concept), `identical_ayah`, `repeated_phrase`, `similar_ayah` (analysis), and `equivalent_ayah` — the last belonging with `ayah_numbering_system`, since it is what makes two numbering systems comparable. `differences` (§2.2 above) is `ayah_numbering_difference`.

The dictionary's `instructional_ayah_repetition` sits near this and is not the same thing; that boundary should be stated.

### 3.4 Linguistic analysis is half-covered

*Closed: `token`, `morpheme`, `stem` and `part_of_speech` added; `segment` resolves to `morpheme`. `syntax`, `constituent` and the `nahw`/`irab` question are left open — see §5.*

The dictionary has `root`, `lemma`, `morphology`, `irab`. §18 of the standard names `Token` and `Morpheme` in its "keep these apart" list — but neither has a concept file, so the standard names a distinction it does not then define.

quranpedia stores, in `quran_word_segments` and `quran_word_syntax` and `word_morphology`:

```text
token, segment, stem, pos (part of speech), tag, family, features,
pgn, mood, tense, voice, verb_form, word_case,
constituent, rel (syntactic relation), sentence, head
```

Missing entries: `token`, `morpheme`, `segment`, `stem`, `part_of_speech`, `syntax` (or `treebank`), `constituent`, `syntactic_relation`. Also `nahw` — quranpedia serves `/nahw` and `/e3rab` as two different things, and the standard has only `irab`; whether those are one concept or two is undecided.

### 3.5 Recitation and audio are thin

*Partly closed: `ayah_timing` added. `radio`, `memorial_mushaf`, bitrate and granularity declined.*

The dictionary has `recitation`, `reciter`, `muqri`, `recitation_style`, `recitation_pace`, `tartil`. quranpedia additionally stores:

```text
recitation_timings   start_time / end_time per ayah      → ayah_timing
radios               continuous streams                  → radio / stream
memorial_mushafs     مصحف مهدى إهداءً لروح فلان          → ?
recitation_classifications   by surah / by ayah          → recitation_granularity
server_128 / server_64 / server_32                        → audio_quality / bitrate
```

`ayah_timing` matters most — it is the join between text and audio that every player needs, and it has no name in the standard.

### 3.6 Presentation and mushaf gaps

*Partly closed: `font` and `ayah_mark` added. The `text` / `clean_text` / `coded_text` triple and `mushaf_rendering` were not — the evidence is one application, which is not enough to name a concept.*

- **`font`** — §18 lists Font under presentation, but there is no `font.yml`. quranpedia has `ayahs.font`, `words.font`, per-mushaf font families, and `/fonts/{filename}`.
- **Ayah end mark (۝)** — `ayahs.marker`, `words.is_marker`, and a whole `config/quran-markers.php` with named styles. The dictionary has `division_mark`, `sajdah_mark`, `waqf_mark` and 30 more marks, but not the most common mark in the mushaf. This looks like an oversight rather than a decision.
- **`coded_text` / `coded_name`** — the font-encoded form of a text, distinct from `text` and from `clean_text`. Three representations of one ayah with no names in the standard: `text`, `clean_text` (normalized, for search), `coded_text` (glyph codes for a specific font). §23 has `normalize` as an operation but the *result* has no name.
- **`layout`** exists in the dictionary; `mushafs.has_svg`, `svg_folder`, `css` suggest a `mushaf_rendering` or `mushaf_asset` concept is wanted, but this is weak evidence — flag, don't adopt.

### 3.7 Tajwid rules are almost entirely missing

*Still open. It is the largest remaining gap, and it is generation work off `data/tajweed_engine_rules.json` rather than sixteen hand-written entries.*

Category `tajwid` in the dictionary has five entries: `tajwid`, `istiadhah`, `khatmah`, `noon_sakinah`, `saktah`. quranpedia's `config/tajweed-rules.php` ships sixteen rules, each with a public page:

```text
القلقلة  الغنة  الإخفاء الحقيقي  الإخفاء الشفوي  الإقلاب
الإدغام بغنة  الإدغام بغير غنة  الإدغام الشفوي
إدغام المتجانسين  إدغام المتقاربين
المد الطبيعي  المد الواجب المتصل  المد الجائز المنفصل  المد اللازم
همزة الوصل  اللام الشمسية
```

Only `hamzat_al_wasl` of these has an entry, and it is filed under `dabt` as a mark rather than as a tajwid ruling.

The standard's own §13 argues this case: a classification's values are first-class entries. `tajwid` as a bare concept with no rulings under it is the flat list §12 warns against. `standards/terminology/data/tajweed_engine_rules.json` already exists in the repo, so the raw material is here and the generation step is what is missing.

Note the spelling trap: the app's own rule slugs are `madda_obligatory`, `madda_necessary`, `madda_permissible`, `madda_normal`, `idgham-with-ghunnah` — inconsistent between snake and kebab in the same file, and `madda` for مد. The derived forms would be `madd_wajib_muttasil`, `madd_jaiz_munfasil`, `madd_lazim`, `madd_tabii`.

### 3.8 Smaller gaps

*Closed: `mawdi_al_sajdah`. Declined: `language`, `tag`, `category`, `attachment`, `thumbnail`, `recitation_granularity`.*

- **`language`** — `languages` table, `language_id` on books and translations, `/translation-books/{language_code}`, 28+ languages in production. No entry, and the standard's `translation` category needs it.
- **`sajdah`** — `sajdahs` table with `ayah_id`, `surah_id`, `page_number`. The dictionary has `sajdah_mark` and `sujud_al_tilawah` but no entry for *the place in the text*, which is what the table stores.
- **`tag`** / **`category`** — general, but they are the backbone of the library and the standard says nothing about naming a taxonomy.
- **`recitation_granularity`**, **`attachment`**, **`thumbnail`** — application-layer, arguably out of scope; recorded so the decision is deliberate.

---

## 4. What this implies for the dictionary's shape

> **Superseded.** This section argued for five new domains. The decision went the other way: the standard names the concepts of the Quranic text and its sciences and stops there, so `library`, `content`, `audio` and `people` are a project's own to name. See *The standard names the Quran's own sciences, and stops there* in `content/{ar,en}/reference/decisions.md`. The paragraphs are kept as written, as the case the decision answered.

The 10-of-77 number is not a quality judgement on either side. It says the dictionary today is a dictionary of *the Quranic text and its mushaf*, and quranpedia is mostly an application about *scholarship attached to that text*. Two things follow.

**The `category` list needs new domains.** §25 fixes eighteen domains and says a domain is not added before there are concepts for it. quranpedia supplies the concepts for at least: `library` (book, author, chapter, edition), `content` beyond tafsir (fatwa, note, topic, athar), `analysis` (mutashabihat, similar ayah), `audio` (timing, radio, granularity), `people` (the six roles). Five new domains, each with concepts already in production behind them.

**The `tier` field will do real work.** Most of §3 is `tier: extended` at best — a project storing the Quranic text needs none of it. But `tier: core` should not mean "core to the mushaf"; `fatwa` and `book` are core to the applications that exist. That distinction should be settled before 60 entries are written under it.

---

## 5. Open questions

These need a decision before entries are written; they are not oversights. The ones still open are tracked in `OPEN.md`.

1. *Answered — data.* They are rows in `standards/terminology/registries/qiraat.tsv`; a concept with a closed set of members names its registry instead of giving each member an entry. The question as asked: **Are the ten qiraat and their rawis concepts or data?** The dictionary defines `qiraah`, `riwayah`, `tariq`, `rawi` as concepts. quranpedia stores the ten readers and their twenty rawis as rows. §13 says values of a classification get entries — do نافع، عاصم، حمزة qualify, or is a qiraah an entity with instances rather than a classification with values? The same question applies to the six ayah-numbering systems, and there the answer feels like yes.

2. **`nahw` vs `irab`** — one concept or two? quranpedia serves both.

3. *Answered.* A concept belongs when it cannot be defined without referring to the Quran or the mushaf; the rule heads the standard's "rule for accepting a new term". The question as asked: **Where does the boundary of the standard fall?** `users`, `sessions`, `subscriptions`, `imports`, `proofreader_findings`, `api_usage_logs`, `messages` are ordinary application tables and clearly outside. But `attachment`, `thumbnail`, `radio`, `source` are Quran-adjacent. The standard has no stated rule for what it declines to name, and one would settle a dozen of the items above.

4. **`quran_qa`** — quranpedia has 3 tables and a public section for Q&A on the Quran. Is that a distinct content concept, or a `fatwa` under another name? The data has separate sources, so probably distinct.

5. **Does the standard bind existing databases?** Everything in §2 is a rename in a production database with data that cannot be rebuilt from migrations (quranpedia's own `CLAUDE.md` says so, in capitals). A migration path — aliases, views, a deprecation window — is a thing the standard does not currently offer, and §29 lists "migration mappings" as an output it wants to generate. `aliases.json` is most of the machinery already.

---

## 6. Suggested order of work

**On the standard** — items 1, 2, 4 and most of 5 and 8 were done on 2026-09-06
(see §1a). What remains:

1. **The sixteen tajwid rulings**, generated from `data/tajweed_engine_rules.json`. The largest remaining gap by far: `tajwid` is a bare concept with no rulings under it, which is the flat list §12 warns against, and §13 says a classification's values are first-class entries.
2. **Sources for the twenty new entries.** All twenty are `status: draft` with `sources: []`. §28 keeps them out of `adopted` until a source establishes each definition, and `sources.yml` has three adopted sources to draw on.
3. **`syntax` / `constituent` / `syntactic_relation`**, once the `nahw` vs `irab` question (§5.2) is answered — the treebank layer quranpedia stores has no name and one of the two entries would be a duplicate.
4. **A written rule for what the standard declines to name.** §1a states the line and the decision record argues it, but the standard itself does not yet carry it, so the next reader meets the same question.
5. **A migration path** (§5.5). §29 already lists "migration mappings" as an output, and `aliases.json` is most of the machinery.

**On quranpedia**, in order of consequence. `surveys/quranpedia-net-renames.tsv`
is the machine-readable list for the two screens; the order below is for the
model underneath them:

1. `rawi` → `riwayah` (§2.1) — the only finding that is currently wrong rather than misnamed.
2. `revelation_type` → `revelation_classification` with `makki`/`madani`/`disputed` (§2.3) — small, and it is in the public API.
3. `counts` → `ayah_numbering_systems` (§2.2).
4. `e3rab` → `irab` and `tajweed` → `tajwid` in `options.key` and routes, with redirects (§2.5).
5. The two screens in §2a — 35 of 43 fields. The card is one JSON generator and 114 files, so it is a single change rather than a migration; the modal's tab keys are public URLs and need redirects.
6. Everything else in §2.5 and §2.7 — as tables are touched for other reasons, not as a campaign.
