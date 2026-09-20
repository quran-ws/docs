# Quranic vocabulary naming standard

**Contents** — the scripts cite these numbers

- 1. [Define the concept before naming it](#define-the-concept-before-naming-it)
- 2. [One canonical name per concept](#one-canonical-name-per-concept)
- 3. [Translation and compound names](#translation-and-compound-names)
- 4. [Canonical code spelling](#canonical-code-spelling)
- 5. [Spelling: name format](#spelling-name-format)
- 6. [Spelling: consonants and vowels](#spelling-consonants-and-vowels)
- 7. [Spelling: ta marbutah](#spelling-ta-marbutah)
- 8. [Spelling: long vowels and letter names](#spelling-long-vowels-and-letter-names)
- 9. [Spelling: hamzah, ayn and exceptions](#spelling-hamzah-ayn-and-exceptions)
- 10. [Spelling: articles and connecting words](#spelling-articles-and-connecting-words)
- 11. [Forms of a name](#forms-of-a-name)
- 12. [Relationships between names](#relationships-between-names)
- 13. [Deprecated names](#deprecated-names)
- 14. [Singular and plural](#singular-and-plural)
- 15. [Classification and value names](#classification-and-value-names)
- 16. [Surah and personal names](#surah-and-personal-names)
- 17. [Distinguishing concepts](#distinguishing-concepts)
- 18. [Numbers, references and timing](#numbers-references-and-timing)
- 19. [Using names in software](#using-names-in-software)

This standard sets the naming rules for concepts used in Quranic software. First define the concept, its meaning and its boundaries; then choose its name and derive its spelling using these rules. Record the resulting names in the [terminology dictionary](dictionary.md).

The standard names concepts that cannot be defined without reference to the Quran or mushaf. Users, subscriptions, files and other general application concepts remain outside its dictionary. The software naming guidance here applies when using its vocabulary.

The provisions of this standard are conformance requirements unless identified as recommendations or permitted options. “Must” indicates a requirement, “should” a recommendation, and “may” permission. Definitions explain meanings; examples illustrate the requirements.

The underlying idea follows `convention over configuration`:

> Once developers know the standard's rules, they can predict concept, relationship and field names and how to use them without consulting the documentation every time.

## Define the concept before naming it

Define the concept first, then choose its name.

Before adopting a term, establish:

- What does it represent?
- What are its boundaries?
- What does it exclude?
- Does it differ from a neighbouring concept?
- Why does software need to model it?

Then choose the most suitable name using the following rules.

## One canonical name per concept

<a id="rule-001"></a>

### 001. One code name per concept

After defining a concept, choose one code name for it according to this standard and record it in the dictionary. Use the same vocabulary wherever the standard applies, as far as possible.

**Examples**

| Concept | Canonical name | Names that do not replace it |
| --- | --- | --- |
| السورة | `surah` | `chapter`, `quran_section` |

## Translation and compound names

<a id="rule-002"></a>

### 002. Transliterating specialised terms

Retain the Arabic name of a specialised Quranic or scholarly concept and write it in Latin letters when a general translation would lose its precision or identity.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| سورة | `surah` |
| آية | `ayah` |
| تجويد | `tajwid` |

<a id="rule-003"></a>

### 003. Translating general concepts

Use the natural English name for a general concept that has a clear technical name.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| كلمة | `word` |
| صفحة | `page` |
| حرف | `letter` |

<a id="rule-004"></a>

### 004. Forming compound names

In a compound name, transliterate the complete term originating in the Quran or its sciences, and translate the general words added to it into English. Whether a word is translated or transliterated depends on its meaning within the term.

**Examples**

| Arabic name | Canonical form |
| --- | --- |
| الرَّسْم الإِمْلَائِيّ | `rasm_imlai` |
| النُّون السَّاكِنَة | `noon_sakinah` |
| الوَقْف اللَّازِم | `waqf_lazim` |
| المِيم الصَّغِيرَة | `small_meem` |

The form for «المِيم الصَّغِيرَة» is `small_meem`, not `meem_saghirah`.

<a id="rule-005"></a>

### 005. Order of translated adjectives

An adjective translated into English precedes the noun it describes.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| الأَلِف المَحْذُوفَة | `omitted_alif` |

<a id="rule-006"></a>

### 006. Order of translated head nouns

A translated general head noun goes at the end of the English construction. Reverse the order of successive translated head nouns.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| عَلَامَة الوَقْف | `waqf_mark` |
| نَوْع عَلَامَة الوَقْف | `waqf_mark_type` |

<a id="rule-007"></a>

### 007. Technical meaning within a compound

A word's technical meaning within the compound determines its spelling: translate «إملائية» with «علامة», but transliterate it with «رسم».

**Examples**

| Arabic name | Canonical form |
| --- | --- |
| العَلَامَة الإِمْلَائِيَّة | `orthographic_mark` |
| الرَّسْم الإِمْلَائِيّ | `rasm_imlai` |

## Canonical code spelling

After choosing an Arabic term, determine how to write it in code. This form is its `Canonical Code Spelling`. Derive it from vocalised Arabic using the following rules so that developers arrive at the same spelling rather than each project choosing its own.

The aim is a simple, stable and predictable spelling rather than a precise scholarly rendering of pronunciation. Use `ASCII` without scholarly transliteration marks. Two Arabic letters may share one Latin equivalent, such as س and ص, both written `s`. Keep the original Arabic separately because the code spelling alone cannot reconstruct it.

The project's shared tools can check spellings. The [contribution instructions](dictionary.md#contributing) explain how to check names before proposing a change.

## Spelling: name format

<a id="rule-008"></a>

### 008. Code-name format

Write the canonical code name in lowercase Latin letters, separating words in a compound with underscores: `snake_case`.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| نظام عد الآي | `ayah_numbering_system` |
| الوقف اللازم | `waqf_lazim` |

## Spelling: consonants and vowels

<a id="rule-009"></a>

### 009. Characters in code spelling

Write code names using `ASCII`, without scholarly transliteration marks or an apostrophe representing hamzah or ayn.

**Examples**

| Canonical code spelling | Form not used in code |
| --- | --- |
| `qiraah` | `qirāʾah` |
| `irab` | `i'rab` |

<a id="rule-010"></a>

### 010. Source of the derived spelling

Derive the spelling of an Arabic term from its vocalised name according to this standard.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| سُورَة | `surah` |

<a id="rule-011"></a>

### 011. Vocalising the Arabic name

Use vocalised Arabic when deriving a spelling. Write hamzat al-wasl as an alif carrying its vowel, and do not assume an unrecorded vowel.

**Examples**

| Vocalised Arabic name | Derived form |
| --- | --- |
| اِسْتِعَاذَة | `istiadhah` |

Unvocalised «استعاذة» is insufficient to determine the spelling. Write اِ rather than ٱ.

<a id="rule-012"></a>

### 012. Reconstructing the Arabic name

Do not rely on the code name to reconstruct the original Arabic letters.

**Examples**

| Arabic letter | Latin equivalent |
| --- | --- |
| ص | `s` |
| س | `s` |

Store the original Arabic separately; `s` alone does not identify which of the two letters occurred in the name.

<a id="rule-013"></a>

### 013. Consonant correspondences

Transliterate consonants using the correspondences in the example.

**Examples**

| Arabic letter | Latin equivalent |
| --- | --- |
| ب | `b` |
| ت | `t` |
| ث | `th` |
| ج | `j` |
| ح | `h` |
| خ | `kh` |
| د | `d` |
| ذ | `dh` |
| ر | `r` |
| ز | `z` |
| س | `s` |
| ش | `sh` |
| ص | `s` |
| ض | `d` |
| ط | `t` |
| ظ | `z` |
| غ | `gh` |
| ف | `f` |
| ق | `q` |
| ك | `k` |
| ل | `l` |
| م | `m` |
| ن | `n` |
| ه | `h` |
| و | `w` |
| ي | `y` |
| ة | `h` |

<a id="rule-014"></a>

### 014. Short vowels

Represent short vowels as `a` for fathah, `i` for kasrah and `u` for dammah.

**Examples**

| Vowel | Latin equivalent |
| --- | --- |
| Fathah (َ) | `a` |
| Kasrah (ِ) | `i` |
| Dammah (ُ) | `u` |

<a id="rule-015"></a>

### 015. Forms of long alif

Treat alif maqsura, dagger alif and maddah as long alif.

**Examples**

| Arabic form | Latin equivalent |
| --- | --- |
| ا / ى / dagger alif / maddah | `a` |

<a id="rule-016"></a>

### 016. Diphthongs

Write waw with sukun following a fathah as `aw`, and yaa with sukun following a fathah as `ay`.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| مَوْضِع | `mawdi` |
| أَوْلَى | `awla` |
| طَرَفَيْن | `tarafayn` |

<a id="rule-017"></a>

### 017. Doubled consonants

Double the consonant carrying a shaddah. The nisbah ending is covered in [rule 022](#rule-022).

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| شَدَّة | `shaddah` |
| مُقَطَّع | `muqatta` |

<a id="rule-018"></a>

### 018. Tanwin and case endings

Keep only the short vowel of tanwin, and drop the grammatical case vowel at the end of a word.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| هُدًى | `huda` |

## Spelling: ta marbutah

<a id="rule-019"></a>

### 019. Ta marbutah outside idafah

Write ta marbutah as `h` at the end of a name or before an adjective when the word is not the first member of an idafah construction.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| سُورَة | `surah` |
| القَلْقَلَة الصُّغْرَى | `qalqalah_sughra` |

A following word alone does not turn ta marbutah into `t`: «الصغرى» is an adjective, so write `qalqalah_sughra`, not `qalqalat_sughra`.

<a id="rule-020"></a>

### 020. Ta marbutah in idafah

Write ta marbutah as `t` when its word is the first member of an idafah construction, a noun construction expressing a relationship such as possession.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| هَمْزَة الوَصْل | `hamzat_al_wasl` |
| سَجْدَة التِّلَاوَة | `sajdat_al_tilawah` |

Ta marbutah is pronounced as a taa in idafah, so write `hamzat_al_wasl`, not `hamzah_al_wasl`.

## Spelling: long vowels and letter names

<a id="rule-021"></a>

### 021. Long vowels

Write long vowels with a single Latin letter: `a`, `i` or `u`. Letter names have canonical spellings in [rule 023](#rule-023).

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| تَجْوِيد | `tajwid` |
| تَفْسِير | `tafsir` |
| نُزُول | `nuzul` |

Do not double letters to represent vowel length: write `tajwid` and `nuzul`, not `tajweed` and `nuzool`. Other forms may be used for display or search, as explained in [rule 024](#rule-024).

<a id="rule-022"></a>

### 022. The nisbah ending

Write the doubled yaa of a final nisbah ending, an Arabic adjective ending indicating affiliation, as a single `i`.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| مَكِّيّ | `makki` |
| مَدَنِيّ | `madani` |
| عُثْمَانِيّ | `uthmani` |

This applies specifically to the final nisbah yaa: write `makki`, not `makkiyy` or `makkee`. The doubled kaf remains `kk` under [rule 017](#rule-017).

<a id="rule-023"></a>

### 023. Letter-name spellings

Use the spellings recorded in the [letter-name table](https://github.com/quran-ws/docs/blob/79e3c6bb2b52dd1df81b3e64debfebf9dd5f8ea5/standards/terminology/data/letter_names.tsv#L13-L40), whether the letter name occurs alone or in a compound.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| نُون | `noon` |
| مِيم | `meem` |
| سِين | `seen` |
| جِيم | `jeem` |
| يَاء | `yaa` |
| صَاد | `saad` |
| المِيم الصَّغِيرَة | `small_meem` |
| سِين القِرَاءَة | `seen_al_qiraah` |

Letter names are exceptions to shortened long vowels in [rule 021](#rule-021): write `noon` and `meem`, not `nun` and `mim`. The exception applies to the letter name even within a compound; it does not extend to terms such as `tajwid`. See the [decision record](decisions.md) for the reasoning and the shared spellings of some letter names.

<a id="rule-024"></a>

### 024. Common spelling and the derived form

When a common spelling differs from the derived form, use the common spelling for display and search, while keeping the derived form as the code name.

**Examples**

| Name form | Spelling |
| --- | --- |
| Code name | `tajwid` |
| Display name | `Tajweed` |
| Alternative spelling for search | `tajweed` |

In the dictionary, `code` holds the derived form `tajwid`, `display` holds `Tajweed`, and `alternative_spellings` records `tajweed` for search. This keeps code spelling predictable while accommodating common usage. The [decision record](decisions.md) explains the distinction.

## Spelling: hamzah, ayn and exceptions

<a id="rule-025"></a>

### 025. Hamzah and ayn

Omit letters or special marks representing hamzah and ayn, retaining their vowels within a word.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| قِرَاءَة | `qiraah` |
| مُعَلِّم | `muallim` |

Omit the mark representing the consonant, not its vowel: write `qiraah`, not `qira'ah`, and retain the fathah in `muallim`. When precise scholarly transliteration is needed, store it in `names.transliteration` for display or scholarly content without changing the code name.

<a id="rule-026"></a>

### 026. Final hamzah and ayn after a consonant with sukun

Repeat the preceding vowel when a word ends in hamzah or ayn preceded by a consonant with sukun.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| رُبْع | `rubu` |
| جَمْع | `jama` |
| قَطْع | `qata` |

Repeating the vowel avoids shortening the ending to forms such as `rub` and `jam`, which are English words with other meanings. If hamzah or ayn follows a long vowel, add nothing: write `رُكُوع` → `ruku` and `مَمْنُوع` → `mamnu`, because the spelling already ends in a vowel.

<a id="rule-027"></a>

### 027. Established-spelling exceptions

When a term has a documented exception in the established-spellings table, use that recorded spelling instead of the derived result. Add a usage-based exception only with measurements showing that the derived result is very rarely used.

**Examples**

| Arabic name | Canonical established spelling | Derived result replaced |
| --- | --- | --- |
| الجزء | `juz` | `juzu` |

A spelling being more common is not sufficient for an exception; otherwise `tajweed` would replace `tajwid`. The exception concerns a derived form almost absent from usage. Exceptions and measurements are recorded in the [established-spellings table](https://github.com/quran-ws/docs/blob/79e3c6bb2b52dd1df81b3e64debfebf9dd5f8ea5/standards/terminology/data/established_spellings.tsv), with explanations in the [decision record](decisions.md).

<a id="rule-028"></a>

### 028. The name of surah Aal Imran

Write the surah name Aal Imran as `aal_imran` to distinguish «آل» from the definite article `al`.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| آل عِمْرَان | `aal_imran` |

<a id="rule-029"></a>

### 029. Surahs named after their opening letters

Use the recorded names for the surahs Taha, Yasin, Saad and Qaaf, which are named after their opening letters.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| طه | `taha` |
| يس | `yasin` |
| ص | `saad` |
| ق | `qaaf` |

## Spelling: articles and connecting words

<a id="rule-030"></a>

### 030. The definite article and sun letters

When the definite article remains inside a compound, write it consistently as `al`; do not change it before sun letters, the consonants that assimilate its pronunciation.

**Examples**

| Arabic name | Code name | Display name |
| --- | --- | --- |
| أسباب النزول | `asbab_al_nuzul` | `Asbab al-Nuzul` |

<a id="rule-031"></a>

### 031. The definite article at the beginning

Omit the definite article at the beginning of a code name.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| الفَتْحَة | `fathah` |
| السُّكُون | `sukun` |

<a id="rule-032"></a>

### 032. The definite article on an adjective

Omit the definite article from an adjective following a definite noun.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| الرَّسْم العُثْمَانِيّ | `rasm_uthmani` |
| الوَقْف اللَّازِم | `waqf_lazim` |

<a id="rule-033"></a>

### 033. The definite article in idafah

Retain `al` on the second member of an idafah construction, determining the idafah or adjective relationship between each adjacent pair of words.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| رُبْع الحِزْب | `rubu_al_hizb` |
| الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن | `waqf_jaiz_mustawi_al_tarafayn` |

<a id="rule-034"></a>

### 034. The definite article after translating a head noun

Exclude a translated head noun when deciding whether to retain the definite article in the rest of the name.

**Examples**

| Arabic name | Canonical form | Form that violates the rule |
| --- | --- | --- |
| عَلَامَة الوَقْف اللَّازِم | `waqf_lazim_mark` | `al_waqf_lazim_mark` |

<a id="rule-035"></a>

### 035. Attached prepositions

When بِ or لِ is attached to a word inside a term, represent the preposition as a separate part of the code name and retain the definite article on the noun following it.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| تَفْسِير بِالرَّأْي | `tafsir_bi_al_ray` |
| المَدّ العَارِض لِلسُّكُون | `madd_arid_li_al_sukun` |

<a id="rule-036"></a>

### 036. Connecting words

Omit مَعَ, كَوْن, بِحَيْثُ and جَوَازًا from the code name when they only connect its parts, while keeping the Arabic name complete.

**Examples**

| Arabic name | Code spelling |
| --- | --- |
| الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى | `waqf_jaiz_wasl_awla` |

## Forms of a name

One concept may have different name forms because each serves a different use: a stable code name, a user-facing name, vocalised Arabic, and names preserved from sources. Different forms do not imply different concepts.

The [dictionary reader guide](dictionary.md#reading-entries) explains naming fields and entry structure. The [dictionary contribution section](dictionary.md#contributing) explains how to propose a term or change its definition.

<a id="rule-037"></a>

### 037. Code-name stability

Use the canonical code name unchanged; do not change it merely because a more common spelling appears.

**Examples**

| Use | Name |
| --- | --- |
| Stable code name | `tajwid` |
| Common display spelling | `Tajweed` |

`tajwid` remains the code name even when `Tajweed` is common in display.

<a id="rule-038"></a>

### 038. Choosing the display name

Choose the most common English spelling for display and document the evidence in `names.display_evidence` before marking the entry `adopted`. A `draft` may have a display name before its evidence is complete. The display name is what readers see in interfaces and documentation, and it may differ from the code name.

**Examples**

| Name form | Spelling |
| --- | --- |
| Code name | `tajwid` |
| Display name | `Tajweed` |

<a id="rule-039"></a>

### 039. The vocalised Arabic name

Retain the vocalised Arabic name of a Quranic or scholarly Arabic term for derivation and Arabic display.

**Examples**

| Arabic name | Code name |
| --- | --- |
| الهَمْزَة | `hamzah` |

<a id="rule-040"></a>

### 040. Source names and the standard's name

Distinguish the standard's name from a source's name or shape description. Preserve the source's wording and attribute it. This applies when a mark's name or classification differs between the standard and the science of mushaf marks, a mushaf introduction or another source.

**Examples**

| Name type | Example |
| --- | --- |
| Name from the science of mushaf marks | المِيم — عَلَامَة الوَقْف اللَّازِم |
| Shape description from the source | رَأْس عَيْن |
| Source classification | `imlaiyyah` |
| Standard name | `orthographic_mark` |

<a id="rule-041"></a>

### 041. Changing the Arabic name

Change the vocalised Arabic name only for a linguistic reason that clarifies the concept, never to obtain a preferred code name.

**Examples**

| Case | Arabic name |
| --- | --- |
| Full name in the example | الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى |
| Proposed shortening solely to shorten the code name | الوَقْف الجَائِز |

Do not shorten a waqf value's Arabic name merely to shorten its code name. In this example, the shortened name omits that continuing is preferable.

<a id="rule-042"></a>

### 042. Definite articles in Arabic names

Write singular Arabic nouns with the definite article, and classification values expressed as adjectives without it.

**Examples**

| Name type | Arabic form |
| --- | --- |
| Singular noun with the definite article | السُّورَة |
| Singular noun with the definite article | التَّجْوِيد |
| Classification value expressed as an adjective | مَكِّيّ |
| Classification value expressed as an adjective | مُرَتَّل |

<a id="rule-043"></a>

### 043. Unicode character names

Preserve the official Unicode character name as given; do not use it as the code name of the concept the character represents.

**Examples**

| Name type | Form |
| --- | --- |
| Unicode character name | `ARABIC LETTER HAMZA` |
| Concept's code name | `hamzah` |

<a id="rule-044"></a>

### 044. Alternative spellings

Treat different written forms of the same name as alternative spellings for search. Changes to letter case or separators are not alternative spellings.

**Examples**

| Canonical form | Other form | Relationship |
| --- | --- | --- |
| `hamzah` | `hamza` | Alternative spelling |
| `waqf_lazim` | `waqf-lazim` | Separator change; not an alternative spelling |

## Relationships between names

<a id="rule-045"></a>

### 045. Relationships between names

Distinguish a canonical name, alternative spelling, English equivalent and deprecated name; these are different relationships between names.

**Examples**

| Name | Relationship to the canonical name |
| --- | --- |
| `ayah` | Canonical name |
| `aya` | Alternative spelling of `ayah` |
| `Verse` | English equivalent of `ayah` |
| `alamat_mawdi_al_sajdah` | Deprecated name for `sajdah_mark` |

## Deprecated names

<a id="rule-046"></a>

### 046. Deprecated names

Distinguish a valid name no longer recommended for new projects from an alternative spelling, and identify it as a deprecated name referring to the same concept.

**Examples**

| Deprecated name | Canonical name for the same concept |
| --- | --- |
| `alamat_mawdi_al_sajdah` | `sajdah_mark` |

<a id="rule-047"></a>

### 047. References from former names

When a concept is renamed or names for the same concept are merged, preserve the old names and their references to the surviving name, with the date and reason. This also applies when a name is withdrawn from the standard.

**Examples**

| Former name | Name it refers to |
| --- | --- |
| `alamat_mawdi_al_sajdah` | `sajdah_mark` |

Record the reason for the merge alongside the reference.

## Singular and plural

<a id="rule-048"></a>

### 048. Singular and plural

Use the singular for one item and the plural for a collection.

**Examples**

| Meaning | Form |
| --- | --- |
| One ayah | `ayah` |
| A collection of ayahs | `ayahs` |

<a id="rule-049"></a>

### 049. Forming the code plural

Form the code plural by adding `s` to the complete code name, including compound names.

**Examples**

```text
ayahs
juzs
hizbs
mushafs
```

Do not use Arabic plurals such as `ayat` and `suwar` as code collection names; write `ayahs` and `surahs`. Preserve the Arabic plural as linguistic information in the dictionary.

## Classification and value names

<a id="rule-050"></a>

### 050. Classification names and the `_type` suffix

Name a classification after what it classifies, and reserve the `_type` suffix for classifications of mark types.

**Examples**

| Meaning | Canonical name | Name not used for this classification |
| --- | --- | --- |
| Waqf mark type | `waqf_mark_type` | — |
| Waqf ruling | `waqf_ruling` | `waqf_type` |
| Recitation style | `recitation_style` | `recitation_type` |

<a id="rule-051"></a>

### 051. The mark, its indication and the waqf ruling

Use `waqf_mark` for the drawn mark, `waqf_mark_type` to classify what the marks indicate, and `waqf_ruling` to classify the ruling on stopping at a location.

**Examples**

| Meaning | Example values |
| --- | --- |
| A mark's indication | `waqf_lazim` or `waqf_mamnu` |
| Ruling on stopping at the location | `waqf_tamm` or `waqf_kafi` |

<a id="rule-052"></a>

### 052. Naming and defining classification values

Give each meaningful type or classification value its own code name and definition; defining only the overall classification is insufficient.

**Examples**

| Classification | Example values |
| --- | --- |
| `recitation_style` | `murattal`, `mujawwad`, `muallim` |
| `recitation_pace` | `tahqiq`, `tadwir`, `hadr` |
| `revelation_classification` | `makki`, `madani`, `disputed` |

<a id="rule-053"></a>

### 053. Distinguishing classification-value names

Add the distinguishing concept name to a classification value's name when needed, retaining the words that distinguish it from other values.

**Examples**

```text
waqf_lazim
waqf_jaiz_wasl_awla
```

<a id="rule-054"></a>

### 054. Uniqueness within a classification

A value name may occur in two different classifications when its classification is known. It must be unique within its own classification.

**Examples**

| Classification | Value name |
| --- | --- |
| Revelation classification | `makki` |
| Ayah numbering systems | `makki` |

<a id="rule-055"></a>

### 055. Ayah numbering system names

Use the school's name as the code value for an ayah numbering system, rather than deriving the full Arabic name.

**Examples**

```text
kufi
basri
dimashqi
makki
madani_first
madani_last
```

## Surah and personal names

<a id="rule-056"></a>

### 056. Personal names

Write the names of qiraah transmitters, rawis and other people associated with Quranic terminology using the scholarly English form with transliteration marks removed, supported by evidence for that form. If it conflicts with an explicit rule of the standard, the rule takes precedence: write `shubah`, not `shuba`, following the ta marbutah rule.

**Examples**

```text
hafs
warsh
qalun
ibn_dhakwan
```

<a id="rule-057"></a>

### 057. Deriving surah names

Derive surah names from their Arabic names using the general spelling rules.

**Examples**

```text
fatihah
baqarah
nisa
```

<a id="rule-058"></a>

### 058. A concept and an individual sharing a name

A concept and an individual may share a name when the individual's kind is known and no confusion arises; the bare name refers to the concept. This applies when a reciter or surah shares a name with a Quranic concept.

**Examples**

| Meaning | Name with its context |
| --- | --- |
| Hamzah mark | `hamzah` |
| Hamzah the qiraah transmitter | `qiraah:hamzah` |
| A level in the transmission chain | `tariq` |
| Surah al-Tariq | `surah:tariq` |

## Distinguishing concepts

<a id="rule-059"></a>

### 059. Distinguishing neighbouring concepts

Similar names or translations are not a reason to merge different concepts, and one concept's name must not be assigned to another.

**Examples**

| Name | Meaning |
| --- | --- |
| `word` | A word in the text |
| `token` | A unit produced by segmentation |

They may coincide in an example, but that does not make the names synonyms.

<a id="rule-060"></a>

### 060. A mark and what it signifies

Give a drawn mushaf mark a name that distinguishes it from the concept it signifies.

**Examples**

| Drawn mark | What it signifies |
| --- | --- |
| Saktah mark: `saktah_mark` | The pause: `saktah` |
| Sajdah mark: `sajdah_mark` | The prostration and its location: `sajdah` |
| Ayah mark: `ayah_mark` | The ayah ending: `ayah_ending` |

<a id="rule-061"></a>

### 061. Sajdah and its mark

Use `sajdah` for a location of recitation prostration and the prostration there, and `sajdah_mark` for the drawn mark.

**Examples**

| Meaning | Name |
| --- | --- |
| The location and prostration there | `sajdah` |
| Drawn mark | `sajdah_mark` |

<a id="rule-062"></a>

### 062. Naming a mark in context

Identify a Quranic mark by its meaning at its location; its codepoint alone does not determine its name.

**Examples**

| Codepoint | Name according to meaning |
| --- | --- |
| `U+06DC` | `saktah_mark` or `seen_al_qiraah`, depending on the location |
| `U+0652` and `U+06E1` | `sukun` |

<a id="rule-063"></a>

### 063. Words and their analysis units

Use `word` for a word in the text, `token` for a unit produced by segmentation, and morphological-analysis names for what is derived from the word. Do not use these names interchangeably.

**Examples**

| Name | Meaning |
| --- | --- |
| `word` | The word recognised by the reader |
| `token` | A unit produced by a segmentation method |
| `morpheme` | A unit carrying meaning or a morphological function |
| `lemma` | Dictionary form |
| `root` | Root |
| `morphology` | Morphological analysis |
| `irab` | Grammatical analysis |

<a id="rule-064"></a>

### 064. Text units and their representation

Choose a text-unit name according to what is meant: a linguistic letter, character, codepoint, grapheme or drawn glyph.

**Examples**

| Name | Meaning |
| --- | --- |
| `letter` | Linguistic letter |
| `character` | A character, an abstract textual unit |
| `codepoint` | A numeric value in the encoding system |
| `grapheme` | A written unit perceived as one by the reader |
| `glyph` | The shape drawn by the font |

<a id="rule-065"></a>

### 065. The Quran and the mushaf

Use `quran` for the Quran and `mushaf` for the book in which it is written; do not substitute one name for the other.

**Examples**

| Meaning | Name |
| --- | --- |
| The Quran | `quran` |
| The mushaf | `mushaf` |

<a id="rule-066"></a>

### 066. Content and presentation

Use content-unit names for what the text contains, and presentation names for how it appears on the page.

**Examples**

| Domain | Example names |
| --- | --- |
| Content | `surah`, `ayah`, `word` |
| Presentation | `page`, `line`, `layout`, `font`, `glyph` |

## Numbers, references and timing

<a id="rule-067"></a>

### 067. Internal identifiers

Use `id` for an internal identifier linking records; do not show it to readers or build external references on it. Use `number` for the number readers recognise and cite.

**Examples**

| Name | Meaning |
| --- | --- |
| `ayah_id` | Internal identifier |
| `ayah_number` | Ayah number within the surah |

<a id="rule-068"></a>

### 068. Reference numbers

Use `number` for an item's recognised number within its domain, displayed to readers and used in citations.

**Examples**

```text
surah_number
ayah_number
page_number
```

<a id="rule-069"></a>

### 069. Position in a sequence

Use `position` for an item's location within a parent or sequence; it is not a stable reference if the sequence changes.

**Examples**

```text
word_position
token_position
line_position
```

<a id="rule-070"></a>

### 070. Semantic order

Use `order` for an intended semantic ordering when it differs from position in the sequence.

**Examples**

```text
revelation_order
display_order
```

<a id="rule-071"></a>

### 071. Composite references

Use `key` for a readable composite reference: `ayah_key` combines surah and ayah numbers, and `word_key` combines the ayah key and word position.

**Examples**

```text
ayah_key = surah_number:ayah_number
2:255

word_key = ayah_key:word_position
2:255:3
```

<a id="rule-072"></a>

### 072. The numbering system of a reference

The meaning of `ayah_key` and `word_key` depends on the ayah numbering system. This standard uses `kufi` as the default when none is stated.

**Examples**

```text
ayah_key: 2:255
```

Interpret references within the declared numbering system, defaulting to `kufi`. The sequential index of ayahs across the whole mushaf is a `position` and also depends on the numbering system. The numbering system alone does not make `word_key` stable when the text or segmentation differs; identify the text and segmentation method when exchanging word references.

<a id="rule-073"></a>

### 073. Naming audio timings

Within a particular recitation recording, name an audio span after the text unit it corresponds to: `ayah_timing` for an ayah and `word_timing` for a word, without including the reciter, riwayah or style in the name.

**Examples**

| Name | Meaning |
| --- | --- |
| `ayah_timing` | An ayah span in one recording |
| `word_timing` | A word span in one recording |


## Using names in software

These guidelines supplement the terminology rules when using names in a model, database or API.

### Clear names

Use a complete, familiar name such as `surah`, `ayah` or `word`, avoiding abbreviations such as `srh`, `ay` and `wrd`. Choose a name that identifies the data rather than `data` or `item` when its kind is known.

### Relationship names

Name a relationship after the linked concept, using singular for a to-one relationship and plural for a to-many relationship: `ayah.surah`, `surah.ayahs` and `ayah.words`. For a data relationship, `ayahs` is sufficient; `getAyahList()` describes an operation that retrieves it.

### Operation names

Use the same verb for the same operation: `normalize`, `parse`, `tokenize`, `segment`, `transliterate`, `annotate`, `render`, `validate`, `compare` and `convert`. `tokenizeText()` explains the work more clearly than `processText()`, and `renderAyah()` is more precise than `handleAyah()` when the operation displays an ayah. These are operation names and do not need separate dictionary entries.

### Boolean names

Make a boolean field's name a yes/no question, such as `has_sajdah` or `is_active`. When choosing a value from a classification with several values, use that classification field rather than multiple booleans whose values could conflict.

### The same vocabulary across system layers

Keep canonical vocabulary in models, databases and APIs, adapting letter case to the layer. For example, the `Surah` model corresponds to the `surahs` table and `surah_id` linking field; it does not become `chapter` in another layer. The interface may display an appropriate translation for the reader.

| Form | Use | Example |
| --- | --- | --- |
| `snake_case` | Tables, columns, `JSON` keys, `enum` values and filenames | `ayah_numbering_system` |
| `PascalCase` | Classes and types | `AyahNumberingSystem` |
| `camelCase` | Fields and functions where required by the language | `ayahNumber` |
| `kebab-case` | URL paths | `/waqf-marks/waqf-lazim` |

Changing letter case or separators does not create a new alternative spelling in the dictionary.

### Names owned by an external source

Preserve external package, file and column names exactly as their owner writes them, because changing them breaks the reference. For example, retain `row["aya_text_emlaey"]` when reading a publisher's file. Fields created inside your project after reading it follow the standard. Declare these external names to the auditor through `external_names` in `.terminology.json`.

### Link timings to their recording

`ayah_timing` carries `recitation_id`, `ayah_key`, `start_ms` and `end_ms`; `word_timing` uses `word_key` instead of the ayah key. `recitation_id` identifies the recording the times belong to. Store the reciter, riwayah and style on the recitation, without adding them to the audio-span name.
