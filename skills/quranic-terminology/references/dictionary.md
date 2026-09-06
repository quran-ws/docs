# Terminology dictionary

> **This page is generated**
>
> It comes from `standards/terminology/concepts/*.yml`. Do not edit it here: edit
> the entry, then run `python3 tools/generate_dictionary.py`.

## Core — `core`

### Mushaf — المصحف

| | |
| --- | --- |
| `code` | `mushaf` |
| `plural` | `mushafs` |
| `kind` | `entity` |
| Vocalized | المُصْحَف |
| Other spellings | `mus'haf`, `muṣḥaf` |
| English gloss | `Quran Codex` |

**Definition:** The written, ordered collection of the Quran in leaves; a Mushaf is a written vessel for the Quran and not an absolute synonym for the Quran itself.

**Purpose:** Used when the properties of the written representation matter: rasm, layout, pages, lines and marks.

### Quran — القرآن

| | |
| --- | --- |
| `code` | `quran` |
| `kind` | `concept` |
| Vocalized | القُرْآن |
| Other spellings | `koran`, `qur'an`, `qur’an` |

**Definition:** The speech of Allah sent down upon Muhammad, peace be upon him, whose recitation is an act of worship. The name is used of the whole and, by context, of a part of it.

**Purpose:** Represents the Quranic content itself, independent of any particular Mushaf, layout, formatting or digital representation.


## Structure — `structure`

### Ayah — آية

| | |
| --- | --- |
| `code` | `ayah` |
| `plural` | `ayahs` |
| `kind` | `entity` |
| Vocalized | آيَة |
| Other spellings | `aya` |
| English gloss | `verse` |

**Definition:** A unit of the Quranic text falling within a surah and having determined boundaries. Its number, and some of its boundaries, may differ from one ayah numbering system to another.

**Purpose:** Used as the basic unit for referring to the Quranic text, and for attaching translations, tafsir, recitations, analyses and other data to a specific place in the Quran.

- Its position on a page or a line belongs to the Mushaf and its layout, not to the identity of the ayah.
- The fasilah is the ayah's ending, not the ayah.

### Basmalah — البسملة

| | |
| --- | --- |
| `code` | `basmalah` |
| `plural` | `basmalahs` |
| `kind` | `concept` |
| Vocalized | البَسْمَلَة |
| Other spellings | `basmala` |

**Definition:** The formula «بسم الله الرحمن الرحيم» with which the surahs open, except Surah al-Tawbah. It carries rulings and differences bound up with ayah counting.

**Purpose:** Used to identify the basmalah and to represent its position and its relation to the surah and to the ayah numbering system.

### Fasilah — الفاصلة

| | |
| --- | --- |
| `code` | `fasilah` |
| `plural` | `fasilahs` |
| `kind` | `concept` |
| Vocalized | الفَاصِلَة |
| Other spellings | `fasila` |
| English gloss | `Verse Ending` |

**Definition:** The close of an ayah or a passage as a matter of its composition; some scholars define it as the ayah's last word.

**Purpose:** Used in studies and datasets concerned with ayah endings and Quranic composition. It is never used as a synonym for `Ayah`.

### Disjointed Letter — الحرف المقطع

| | |
| --- | --- |
| `code` | `harf_muqatta` |
| `plural` | `harf_muqattas` |
| `kind` | `concept` |
| Vocalized | الحَرْف المُقَطَّع |
| English gloss | `Separated Letters`, `Disjointed Letters` |

**Definition:** Alphabetic letters that open certain surahs, such as Alif Lam Mim, Alif Lam Ra, Ha Mim and Kaf Ha Ya Ayn Sad.

**Purpose:** Used to identify these openings, keep them distinct, and tie them to their surahs and their positions in the text.

### Mawdi al-Sajdah — موضع السجدة

| | |
| --- | --- |
| `code` | `mawdi_al_sajdah` |
| `plural` | `mawdi_al_sajdahs` |
| `kind` | `concept` |
| Vocalized | مَوْضِع السَّجْدَة |
| English gloss | `Sajdah Place` |

**Definition:** The place in the text at which the reader prostrates, ending at a particular ayah. The places are countable, and some of them are disputed.

**Purpose:** Used to tie a sajdah to its place in the surah, the ayah and the page, and to keep the place apart from the mark drawn at it and from the prostration itself.

- The place is a location in the text, the sajdah mark is a sign drawn for it, and sujud al-tilawah is the act.

### Surah — السورة

| | |
| --- | --- |
| `code` | `surah` |
| `plural` | `surahs` |
| `kind` | `entity` |
| Vocalized | السُّورَة |
| Other spellings | `sura` |
| English gloss | `Chapter` |

**Definition:** A principal unit of the structure of the Quran, made up of ordered ayahs, with a name and a known place in the order of the Mushaf.

**Purpose:** Used as the principal unit for organising the text and for attaching ayahs and surah-level data.


## Text — `text`

### Character

| | |
| --- | --- |
| `code` | `character` |
| `plural` | `characters` |
| `kind` | `unit` |

**Definition:** An abstract unit of text in a digital encoding; it need not correspond to a single linguistic letter.

**Purpose:** Used when processing text programmatically at the character level.

### Codepoint

| | |
| --- | --- |
| `code` | `codepoint` |
| `plural` | `codepoints` |
| `kind` | `unit` |

**Definition:** A numeric value defined by an encoding standard such as Unicode.

**Purpose:** Used when the work concerns the exact digital representation of Quranic characters and marks.

### Glyph

| | |
| --- | --- |
| `code` | `glyph` |
| `plural` | `glyphs` |
| `kind` | `unit` |

**Definition:** The visual shape a font produces to represent a letter, a character, or a group of them.

**Purpose:** Used for fonts, rasm, rendering and the placement of visual shapes. It is never used as a synonym for `Letter` or `Character`.

### Grapheme

| | |
| --- | --- |
| `code` | `grapheme` |
| `plural` | `graphemes` |
| `kind` | `unit` |

**Definition:** A written unit that a user perceives as one unit, which may consist of more than one Unicode codepoint.

**Purpose:** Used for visual segmentation, editing and text selection, where the codepoint is not the right unit.

### Letter — الحرف

| | |
| --- | --- |
| `code` | `letter` |
| `plural` | `letters` |
| `kind` | `unit` |
| Vocalized | الحَرْف |
| Other spellings | `harf` |

**Definition:** A letter of the alphabet as a linguistic unit of writing.

**Purpose:** Used for data that deals with linguistic letters, without confusing them with their digital or visual representations.

### Token

| | |
| --- | --- |
| `code` | `token` |
| `plural` | `tokens` |
| `kind` | `unit` |
| English gloss | `Token` |

**Definition:** A unit produced by segmenting the text according to a declared method. It may equal a word, be part of one, or span more than one.

**Purpose:** Used to tie automated analysis to the text where the word boundary is not the segmentation boundary, and to keep what a segmenter produces distinct from what a reader counts as a word.

- A word is a unit the reader recognises; a token is a unit a segmentation method produces, so changing the method changes the number of tokens and not the number of words.

### Word — الكلمة

| | |
| --- | --- |
| `code` | `word` |
| `plural` | `words` |
| `kind` | `unit` |
| Vocalized | الكَلِمَة |
| Other spellings | `kalimah` |

**Definition:** A unit of the text treated as a word in its own right according to the adopted method of textual segmentation.

**Purpose:** Used to attach word-level data: root, morphology, irab, tajwid, audio alignment and visual position.


## Quran divisions — `divisions`

### Hizb — الحزب

| | |
| --- | --- |
| `code` | `hizb` |
| `plural` | `hizbs` |
| `kind` | `entity` |
| Vocalized | الحِزْب |
| Other spellings | `hezb` |

**Definition:** In the current division, half a juz, so that the Quran is sixty hizbs.

**Purpose:** Used to represent the conventional divisions, navigation, and reading plans.

### Juz — الجزء

| | |
| --- | --- |
| `code` | `juz` |
| `plural` | `juzs` |
| `kind` | `entity` |
| Vocalized | الجُزْء |
| Other spellings | `juzu` |

**Definition:** One of the thirty parts of the well-known division of the Mushaf, made to ease reading and completing it.

**Purpose:** Used for navigation, for organising reading, and for the schedules and plans built on the parts of the Quran.

### Manzil — المنزل

| | |
| --- | --- |
| `code` | `manzil` |
| `plural` | `manzils` |
| `kind` | `entity` |
| Vocalized | المَنْزِل |

**Definition:** One of seven traditional parts of the Quran, made to ease completing it in a week.

**Purpose:** Used in applications that support the manzil system and the reading plans built on it.

### Rubu al-Hizb — ربع الحزب

| | |
| --- | --- |
| `code` | `rubu_al_hizb` |
| `plural` | `rubu_al_hizbs` |
| `kind` | `entity` |
| `parent` | `hizb` |
| Vocalized | رُبْع الحِزْب |
| Other spellings | `rub_al_hizb`, `rub'_al-hizb`, `rub_el_hizb` |

**Definition:** A quarter of a hizb in the well-known division of the Mushaf.

**Purpose:** Used to represent the finer division of the hizb and where its marks fall in the Mushaf.

### Ruku — الركوع

| | |
| --- | --- |
| `code` | `ruku` |
| `plural` | `rukus` |
| `kind` | `entity` |
| Vocalized | الرُّكُوع |
| Other spellings | `ruku'`, `rukūʿ` |

**Definition:** A conventional section of the Quran used to organise reading, printed in some Mushafs.

**Purpose:** Used in the applications and Mushafs that follow the ruku division.

### Thumn — الثمن

| | |
| --- | --- |
| `code` | `thumn` |
| `plural` | `thumns` |
| `kind` | `entity` |
| `parent` | `hizb` |
| Vocalized | الثُّمْن |
| Other spellings | `thumun` |

**Definition:** An eighth of a hizb, a division used in some Mushafs and schools.

**Purpose:** Used when supporting sources or Mushafs that divide the hizb into eighths.


## Surah classification — `surah_classification`

### Mathani — المثاني

| | |
| --- | --- |
| `code` | `mathani` |
| `kind` | `classification_value` |
| `parent` | `surah_group` |
| Vocalized | المَثَانِي |

**Definition:** The group of surahs following the miun in the traditional division.

**Purpose:** Used within the traditional classification of the surahs.

### Miun — المئون

| | |
| --- | --- |
| `code` | `miun` |
| `kind` | `classification_value` |
| `parent` | `surah_group` |
| Vocalized | المِئُون |
| English gloss | `Hundred-Verse Surahs` |

**Definition:** The surahs whose ayahs come to about a hundred, a little more or a little less.

**Purpose:** Used to classify the surahs according to their traditional division.

### Mufassal — المفصل

| | |
| --- | --- |
| `code` | `mufassal` |
| `kind` | `classification_value` |
| `parent` | `surah_group` |
| Vocalized | المُفَصَّل |

**Definition:** A group of the short surahs following the mathani; scholars differ over where it begins.

**Purpose:** Used to classify the surahs of the mufassal and to attach the data and the plans that concern them.

### Saba Tiwal — السبع الطوال

| | |
| --- | --- |
| `code` | `saba_tiwal` |
| `kind` | `classification_value` |
| `parent` | `surah_group` |
| Vocalized | السَّبْع الطِّوَال |
| Other spellings | `sab_tiwal` |
| English gloss | `Seven Long Surahs` |

**Definition:** A group of the longest surahs of the Quran, at its beginning, with a known disagreement over which surah is the seventh.

**Purpose:** Used to classify the surahs according to the traditional division.

### Surah Group — تصنيف السور

| | |
| --- | --- |
| `code` | `surah_group` |
| `kind` | `classification` |
| Vocalized | تَصْنِيف السُّوَر |

**Definition:** A classification gathering surahs by inherited conventional divisions that rest on length or on their place among the groups of surahs.

**Purpose:** Gives classifications such as the tiwal, the miun, the mathani and the mufassal one parent.


## Mushaf and layout — `mushaf`

### Font — الخط

| | |
| --- | --- |
| `code` | `font` |
| `plural` | `fonts` |
| `kind` | `concept` |
| Vocalized | الخَطّ |

**Definition:** A file carrying a set of glyphs and the rules for laying them out, used to render the text of a Mushaf.

**Purpose:** Used because in many digital Mushafs the text renders correctly only in one particular font, so letter codes, their shapes and line positions are tied to it.

- A font is a means of display; the rasm is a property of the written text itself.
- A glyph is a shape inside a font; a letter is a unit of the text.

### Layout — التخطيط

| | |
| --- | --- |
| `code` | `layout` |
| `plural` | `layouts` |
| `kind` | `concept` |
| Vocalized | التَّخْطِيط |

**Definition:** The visual arrangement of the text and its elements into pages, lines and positions within a given Mushaf or view.

**Purpose:** Keeps visual data apart from the fixed textual structure of the Quran.

### Line — السطر

| | |
| --- | --- |
| `code` | `line` |
| `plural` | `lines` |
| `kind` | `unit` |
| Vocalized | السَّطْر |

**Definition:** A typeset line within a page of a Mushaf or of a given layout.

**Purpose:** Used to represent where text and shapes sit within the typeset layout.

### Mushaf Edition — طبعة المصحف

| | |
| --- | --- |
| `code` | `mushaf_edition` |
| `plural` | `mushaf_editions` |
| `kind` | `entity` |
| `parent` | `mushaf` |
| Vocalized | طَبْعَة المُصْحَف |

**Definition:** A specific published edition of the Mushaf with its own publisher, rasm, dabt, layout and other properties.

**Purpose:** Used to tell apart editions that may differ in pages, lines, marks or typographic properties.

### Page — الصفحة

| | |
| --- | --- |
| `code` | `page` |
| `plural` | `pages` |
| `kind` | `unit` |
| Vocalized | الصَّفْحَة |
| Other spellings | `safhah` |

**Definition:** A typographic unit of a given Mushaf's layout; its content and its boundaries may differ from one Mushaf or edition to another.

**Purpose:** Used for rendering, navigation and visual alignment according to the pages of a particular Mushaf.

### Rasm — الرسم

| | |
| --- | --- |
| `code` | `rasm` |
| `kind` | `concept` |
| Vocalized | الرَّسْم |

**Definition:** The way the words of the Quran are written: which letters are written and which omitted or added, and where words are joined or kept apart.

**Purpose:** Used to keep the orthographic layer of the text distinct from the font, the layout and the glyphs.

### Uthmani Rasm — الرسم العثماني

| | |
| --- | --- |
| `code` | `rasm_uthmani` |
| `kind` | `classification_value` |
| `parent` | `rasm` |
| Vocalized | الرَّسْم العُثْمَانِيّ |
| English gloss | `Uthmanic Orthography` |

**Definition:** The way the words of the Uthmani Mushafs are written, with the omission, addition, substitution, separation and joining that go with it.

**Purpose:** Used to state that a text follows the rules of the Uthmani rasm rather than another orthography.


## Dabt — `dabt`

### Ayah Mark — علامة الآية

| | |
| --- | --- |
| `code` | `ayah_mark` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | عَلَامَة الآيَة |
| Symbol | ۝ |
| Characters | `U+06DD` |
| Other spellings | `end_of_ayah`, `ayah_marker`, `ayah_separator` |

**Definition:** The circle separating one ayah from the next. It is placed at the ayah's end and, in most Mushafs, carries its number.

**Purpose:** Used to mark an ayah's boundary in the written text; it is the sign from which a renderer or an analyser reads where an ayah ends and what its number is.

- The mark is something drawn in the Mushaf; the fasilah is the ayah's ending as a matter of the text itself.
- The number inside the circle follows an ayah numbering system and is not part of the mark.

### Dammah — الضَّمَّة

| | |
| --- | --- |
| `code` | `dammah` |
| `kind` | `mark` |
| `parent` | `harakah` |
| Vocalized | الضَّمَّة |
| Symbol | ـُ |
| Characters | `U+064F` |
| Other spellings | `damma` |

**Definition:** Marks the letter as carrying the vowel u (dammah).

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

### Division Mark — عَلَامَة التَّقْسِيم

| | |
| --- | --- |
| `code` | `division_mark` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | عَلَامَة التَّقْسِيم |
| Symbol | نَجْمَة |
| Characters | `U+06DE` |
| Other spellings | `alamat_al_tahzib` |
| Deprecated names | `hizb`, `hizb` |

**Definition:** Marks the start of a juz, a hizb, or a half or quarter of one.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Dot — النُّقْطَة

| | |
| --- | --- |
| `code` | `dot` |
| `kind` | `mark` |
| `parent` | `ijam` |
| Vocalized | النُّقْطَة |
| Symbol | نُقْطَة وَاحِدَة |
| Other spellings | `nuqtah` |

**Definition:** Distinguishes a letter from others that share the same skeleton (i'jam).

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

### Fathah — الفَتْحَة

| | |
| --- | --- |
| `code` | `fathah` |
| `kind` | `mark` |
| `parent` | `harakah` |
| Vocalized | الفَتْحَة |
| Symbol | ـَ |
| Characters | `U+064E` |
| Other spellings | `fatha` |

**Definition:** Marks the letter as carrying the vowel a (fathah).

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

### Hamzah — الهَمْزَة

| | |
| --- | --- |
| `code` | `hamzah` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | الهَمْزَة |
| Symbol | ء |
| Characters | `U+0621`, `U+0654`, `U+0655` |
| Other spellings | `hamza` |

**Definition:** Marks a fully realised glottal stop (hamzat al-qat').

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Hamzat al-Wasl — هَمْزَة الوَصْل

| | |
| --- | --- |
| `code` | `hamzat_al_wasl` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | هَمْزَة الوَصْل |
| Symbol | ص صَغِيرَة فَوْق الأَلِف |
| Characters | `U+0671` |
| Other spellings | `wasla` |

**Definition:** Marks a connecting hamzah, dropped whenever the word is reached in continuation.

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Harakah — الحَرَكَة

| | |
| --- | --- |
| `code` | `harakah` |
| `kind` | `classification` |
| `parent` | `mushaf_mark` |
| Vocalized | الحَرَكَة |

**Definition:** A mark fixing a letter's vowel: fathah, dammah, kasrah or sukun.

**Purpose:** Used as the parent of the dabt marks that determine how the letter itself is pronounced.

### Ijam — الإعْجَام

| | |
| --- | --- |
| `code` | `ijam` |
| `kind` | `classification` |
| `parent` | `mushaf_mark` |
| Vocalized | الإعْجَام |

**Definition:** The dotting that distinguishes a letter from the letters that share its written shape.

**Purpose:** Used as the parent of the dot shapes, which are told apart by their number and position rather than by their function.

### Imalah — الإمَالَة

| | |
| --- | --- |
| `code` | `imalah` |
| `kind` | `mark` |
| `parent` | `qiraah_mark` |
| Vocalized | الإمَالَة |
| Symbol | نُقْطَة تَحْت الحَرْف |
| Characters | `U+06EA` |

**Definition:** Marks the major imalah — one place only (11:41).

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

### Ishmam — الإشْمَام

| | |
| --- | --- |
| `code` | `ishmam` |
| `kind` | `mark` |
| `parent` | `qiraah_mark` |
| Vocalized | الإشْمَام |
| Symbol | نُقْطَة فَوْق الحَرْف |
| Characters | `U+06EC` |

**Definition:** Marks ishmam: the lips round to point at the elided vowel, with no audible sound.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

### Kasrah — الكَسْرَة

| | |
| --- | --- |
| `code` | `kasrah` |
| `kind` | `mark` |
| `parent` | `harakah` |
| Vocalized | الكَسْرَة |
| Symbol | ـِ |
| Characters | `U+0650` |
| Other spellings | `kasra` |

**Definition:** Marks the letter as carrying the vowel i (kasrah).

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

### Maddah — المَدَّة

| | |
| --- | --- |
| `code` | `maddah` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | المَدَّة |
| Symbol | خَطّ المَدّ |
| Characters | `U+0653`, `U+06E4` |

**Definition:** Marks a lengthening beyond the natural two counts; the exact duration is a tajwid matter.

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Omitted Alif — الأَلِف المَحْذُوفَة

| | |
| --- | --- |
| `code` | `omitted_alif` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | الأَلِف المَحْذُوفَة |
| Symbol | ا صَغِيرَة قَائِمَة |
| Characters | `U+0670` |
| Other spellings | `alif_mahdhufah`, `small-alef`, `small_alef` |

**Definition:** Restores an alif omitted from the Uthmani skeleton but obligatory in pronunciation.

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Orthographic Mark — العَلَامَة الإمْلَائِيَّة

| | |
| --- | --- |
| `code` | `orthographic_mark` |
| `kind` | `classification` |
| `parent` | `mushaf_mark` |
| Vocalized | العَلَامَة الإمْلَائِيَّة |

**Definition:** A mark fixing how a word is written, such as the hamzah, the maddah and the small letters.

**Purpose:** Used as the parent of the marks that concern how a word is written, rather than its vowel or how it is stopped on.

### Qiraah Mark — عَلَامَة القِرَاءَة

| | |
| --- | --- |
| `code` | `qiraah_mark` |
| `kind` | `classification` |
| `parent` | `mushaf_mark` |
| Vocalized | عَلَامَة القِرَاءَة |

**Definition:** A mark pointing to a particular manner of delivery at its place, such as saktah, ishmam and tashil.

**Purpose:** Used as the parent of the marks that alert the reader to a particular delivery rather than to the pointing of a letter.

### Rectangular Zero — الصِّفْر المُسْتَطِيل

| | |
| --- | --- |
| `code` | `rectangular_zero` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | الصِّفْر المُسْتَطِيل |
| Symbol | مُسْتَطِيل قَائِم صَغِير |
| Characters | `U+06E0` |
| Other spellings | `sifr-mustatil`, `sifr_mustatil` |

**Definition:** Marks an alif dropped in continuation but pronounced when stopping on it.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Rounded Zero — الصِّفْر المُسْتَدِير

| | |
| --- | --- |
| `code` | `rounded_zero` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | الصِّفْر المُسْتَدِير |
| Symbol | دَائِرَة صَغِيرَة |
| Characters | `U+06DF` |
| Other spellings | `sifr-mustadir`, `sifr_mustadir` |

**Definition:** Marks a letter present in the skeleton but never pronounced — neither in continuation nor when stopping.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Sajdah Line — خَطّ السَّجْدَة

| | |
| --- | --- |
| `code` | `sajdah_line` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | خَطّ السَّجْدَة |
| Symbol | خَطّ أُفُقِيّ |
| Other spellings | `khatt_mujib_al_sajdah`, `sajdah-line` |

**Definition:** Marks the word that makes prostration due.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Sajdah Mark — عَلَامَة السَّجْدَة

| | |
| --- | --- |
| `code` | `sajdah_mark` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | عَلَامَة السَّجْدَة |
| Symbol | مِحْرَاب |
| Other spellings | `alamat_mawdi_al_sajdah`, `sajdah-sign`, `sajdah_sign` |

**Definition:** Marks the point at which the reader prostrates.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Saktah Mark — عَلَامَة السَّكْتَة

| | |
| --- | --- |
| `code` | `saktah_mark` |
| `kind` | `mark` |
| `parent` | `qiraah_mark` |
| Vocalized | عَلَامَة السَّكْتَة |
| Symbol | س |
| Characters | `U+06DC` |
| Other spellings | `alamat_al_sakt` |
| Deprecated names | `saktah`, `saktah` |

**Definition:** Marks a saktah: a brief pause without taking a breath, then continuing.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

### Seen al-Qiraah — سِين القِرَاءَة

| | |
| --- | --- |
| `code` | `seen_al_qiraah` |
| `kind` | `mark` |
| `parent` | `qiraah_mark` |
| Vocalized | سِين القِرَاءَة |
| Symbol | س |
| Characters | `U+06DC`, `U+06E3` |
| Other spellings | `seen-reading`, `seen_reading`, `sin_qiraah` |

**Definition:** A sin above the sad signals reading with sin; a sin below it signals reading with sad.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

### Shaddah — الشَّدَّة

| | |
| --- | --- |
| `code` | `shaddah` |
| `kind` | `mark` |
| `parent` | `harakah` |
| Vocalized | الشَّدَّة |
| Symbol | ـّ |
| Characters | `U+0651` |
| Other spellings | `shadda` |

**Definition:** Marks assimilation of a first letter into the second (doubling).

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

### Small Meem — المِيم الصَّغِيرَة

| | |
| --- | --- |
| `code` | `small_meem` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | المِيم الصَّغِيرَة |
| Symbol | م صَغِيرَة |
| Characters | `U+06E2`, `U+06ED` |
| Other spellings | `meem-iqlab`, `meem_iqlab`, `meem_saghirah`, `mim_saghirah` |

**Definition:** Marks iqlab — a silent nun or tanwin turning into a mim before ba.

**Purpose:** Used as a mark of the Mushaf, so that its place and what it points to are known in rendering and in analysis.

### Small Noon — النُّون الصَّغِيرَة

| | |
| --- | --- |
| `code` | `small_noon` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | النُّون الصَّغِيرَة |
| Symbol | ن صَغِيرَة |
| Characters | `U+06E8` |
| Other spellings | `noon_saghirah`, `nun_saghirah`, `small-noon` |

**Definition:** Restores a nun omitted from the skeleton but obligatory in pronunciation — one place only (21:88).

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Small Waw — الوَاو الصَّغِيرَة

| | |
| --- | --- |
| `code` | `small_waw` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | الوَاو الصَّغِيرَة |
| Symbol | و صَغِيرَة |
| Characters | `U+06E5` |
| Other spellings | `small-waw`, `waw_saghirah` |

**Definition:** Marks the silah of the pronoun ha with dammah — pronounced as a waw in continuation.

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Small Yaa — اليَاء الصَّغِيرَة

| | |
| --- | --- |
| `code` | `small_yaa` |
| `kind` | `mark` |
| `parent` | `orthographic_mark` |
| Vocalized | اليَاء الصَّغِيرَة |
| Symbol | ي صَغِيرَة |
| Characters | `U+06E6`, `U+06E7` |
| Other spellings | `small-ya`, `small_ya`, `ya_saghirah`, `yaa_saghirah` |

**Definition:** Marks the silah of the pronoun ha with kasrah — pronounced as a ya in continuation.

**Purpose:** Used as a value of the orthographic marks, so that where the rasm departs from the pronunciation of a word is known.

### Sukun — السُّكُون

| | |
| --- | --- |
| `code` | `sukun` |
| `kind` | `mark` |
| `parent` | `harakah` |
| Vocalized | السُّكُون |
| Symbol | ـْ |
| Characters | `U+0652`, `U+06E1` |

**Definition:** Marks the letter as vowelless and clearly articulated — the tongue strikes it.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

### Tanwin — التَّنْوِين

| | |
| --- | --- |
| `code` | `tanwin` |
| `kind` | `classification` |
| `parent` | `mushaf_mark` |
| Vocalized | التَّنْوِين |

**Definition:** An added vowelless noon at the end of a noun, written by doubling the shape of the vowel.

**Purpose:** Used as the parent of the three tanwin marks, gathering them instead of scattering them through one list.

### Tanwin al-Damm — تَنْوِين الضَّمّ

| | |
| --- | --- |
| `code` | `tanwin_al_damm` |
| `kind` | `mark` |
| `parent` | `tanwin` |
| Vocalized | تَنْوِين الضَّمّ |
| Symbol | ـٌ |
| Characters | `U+064C`, `U+08F1` |
| Other spellings | `dammatan`, `tanwin_al_rafa`, `tanwin_damm` |

**Definition:** Marks the un tanwin. Stacked marks signal izhar; staggered marks with a shadda on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

### Tanwin al-Fath — تَنْوِين الفَتْح

| | |
| --- | --- |
| `code` | `tanwin_al_fath` |
| `kind` | `mark` |
| `parent` | `tanwin` |
| Vocalized | تَنْوِين الفَتْح |
| Symbol | ـً |
| Characters | `U+064B`, `U+08F0` |
| Other spellings | `fathatan`, `tanwin_al_nasb`, `tanwin_fath` |

**Definition:** Marks the an tanwin. Stacked marks signal izhar; staggered marks with a shadda on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

### Tanwin al-Kasr — تَنْوِين الكَسْر

| | |
| --- | --- |
| `code` | `tanwin_al_kasr` |
| `kind` | `mark` |
| `parent` | `tanwin` |
| Vocalized | تَنْوِين الكَسْر |
| Symbol | ـٍ |
| Characters | `U+064D`, `U+08F2` |
| Other spellings | `kasratan`, `tanwin_al_jarr`, `tanwin_al_khafd`, `tanwin_kasr` |

**Definition:** Marks the in tanwin. Stacked marks signal izhar; staggered marks with a shadda on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

### Tashil — التَّسْهِيل

| | |
| --- | --- |
| `code` | `tashil` |
| `kind` | `mark` |
| `parent` | `qiraah_mark` |
| Vocalized | التَّسْهِيل |
| Symbol | نُقْطَة مَكَان الهَمْزَة |
| Characters | `U+06EC` |

**Definition:** Marks tashil: the hamzah softened to a sound between a hamzah and an alif.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

### Three Dots — الثَّلَاث نُقَط

| | |
| --- | --- |
| `code` | `three_dots` |
| `kind` | `mark` |
| `parent` | `ijam` |
| Vocalized | الثَّلَاث نُقَط |
| Symbol | ثَلَاث نُقَط |
| Other spellings | `thalath_nuqat`, `three-dots` |

**Definition:** Distinguishes a letter from others that share the same skeleton (i'jam).

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

### Two Dots — النُّقْطَتَان

| | |
| --- | --- |
| `code` | `two_dots` |
| `kind` | `mark` |
| `parent` | `ijam` |
| Vocalized | النُّقْطَتَان |
| Symbol | نُقْطَتَان |
| Other spellings | `nuqtatan`, `two-dots` |

**Definition:** Distinguishes a letter from others that share the same skeleton (i'jam).

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

### Waqf al-Muanaqah — وَقْف المُعَانَقَة

| | |
| --- | --- |
| `code` | `waqf_al_muanaqah` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | وَقْف المُعَانَقَة |
| Symbol | ثَلَاث نُقَط في مَوْضِعَيْن |
| Characters | `U+06DB` |
| Other spellings | `muanaqah`, `muraqabah`, `taanuq_al_waqf`, `waqf_al_muraqabah` |

**Definition:** Two candidate stopping points: stopping at one makes stopping at the other invalid.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.

### Waqf Jaiz Mustawi al-Tarafayn — الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن

| | |
| --- | --- |
| `code` | `waqf_jaiz_mustawi_al_tarafayn` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن |
| Symbol | ج |
| Characters | `U+06DA` |
| Deprecated names | `waqf-jaiz`, `waqf_jaiz` |

**Definition:** A permissible stop, with stopping and continuing equally sound.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.

### Waqf Jaiz Waqf Awla — الوَقْف الجَائِز الوَقْف أَوْلَى

| | |
| --- | --- |
| `code` | `waqf_jaiz_waqf_awla` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | الوَقْف الجَائِز الوَقْف أَوْلَى |
| Symbol | قلى |
| Characters | `U+06D7` |
| Other spellings | `waqf-awla`, `waqf_awla` |

**Definition:** A permissible stop, and stopping is the better choice.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.

### Waqf Jaiz Wasl Awla — الوَقْف الجَائِز الوَصْل أَوْلَى

| | |
| --- | --- |
| `code` | `waqf_jaiz_wasl_awla` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | الوَقْف الجَائِز الوَصْل أَوْلَى |
| Symbol | صلى |
| Characters | `U+06D6` |
| Other spellings | `wasl-awla`, `wasl_awla` |

**Definition:** A permissible stop, but continuing is the better choice.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.

### Waqf Lazim — الوَقْف اللَّازِم

| | |
| --- | --- |
| `code` | `waqf_lazim` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | الوَقْف اللَّازِم |
| Symbol | م |
| Characters | `U+06D8` |
| Other spellings | `waqf-lazim` |

**Definition:** A compulsory stop: continuing across it would suggest a meaning other than the one intended.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.

### Waqf Mamnu — الوَقْف المَمْنُوع

| | |
| --- | --- |
| `code` | `waqf_mamnu` |
| `kind` | `classification_value` |
| `parent` | `waqf_mark_type` |
| Vocalized | الوَقْف المَمْنُوع |
| Symbol | لا |
| Characters | `U+06D9` |
| Other spellings | `waqf-mamnu` |

**Definition:** Registered in the schema but never used in this edition — zero occurrences.

**Purpose:** Used as a value of the waqf mark type, so that rendering, instruction and warnings in applications branch on it rather than on the shape of the sign.


## Mushaf marks — `mushaf_marks`

### Mushaf Mark — علامة المصحف

| | |
| --- | --- |
| `code` | `mushaf_mark` |
| `kind` | `classification` |
| Vocalized | عَلَامَة المُصْحَف |

**Definition:** A sign or mark that is not one of a word's original letters, used in the Mushaf for reading, organisation or guidance.

**Purpose:** Gives the different marks one parent, instead of treating them as unrelated kinds.


## Ayah numbering — `ayah_numbering`

### Basri Numbering — العد البصري

| | |
| --- | --- |
| `code` | `ayah_numbering_basri` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ البَصْرِي |
| Other spellings | `basri_numbering`, `basran_numbering` |

**Definition:** The counting of the people of Basra, transmitted from Asim al-Jahdari from his predecessors among the Basrans.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Dimashqi Numbering — العد الدمشقي

| | |
| --- | --- |
| `code` | `ayah_numbering_dimashqi` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ الدِّمَشْقِي |
| Other spellings | `dimashqi_numbering`, `shami`, `shami_numbering`, `damascene_numbering` |

**Definition:** The counting of the people of Sham, transmitted from Yahya ibn al-Harith al-Dhimari from Ibn Amir; also called the Shami counting.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Kufi Numbering — العد الكوفي

| | |
| --- | --- |
| `code` | `ayah_numbering_kufi` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ الكُوفِي |
| Other spellings | `kufi_numbering`, `kufan_numbering` |

**Definition:** The counting of the people of Kufa, transmitted from Hamzah al-Zayyat from Ibn Abi Layla from Abu Abd al-Rahman al-Sulami from Ali ibn Abi Talib. It is the counting most printed Mushafs follow today.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Madani Akhir Numbering — العد المدني الأخير

| | |
| --- | --- |
| `code` | `ayah_numbering_madani_akhir` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ المَدَنِي الأَخِير |
| Other spellings | `madani_akhir`, `last_madani`, `madani_last` |

**Definition:** The counting of the people of Madinah in its later transmission, that of Ismail ibn Jafar from Sulayman ibn Jammaz.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Madani Awwal Numbering — العد المدني الأول

| | |
| --- | --- |
| `code` | `ayah_numbering_madani_awwal` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ المَدَنِي الأَوَّل |
| Other spellings | `madani_awwal`, `first_madani`, `madani_first` |

**Definition:** The counting of the people of Madinah in its earlier transmission, that of Abu Jafar Yazid ibn al-Qaqa and Shaybah ibn Nassah.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Makki Numbering — العد المكي

| | |
| --- | --- |
| `code` | `ayah_numbering_makki` |
| `kind` | `classification_value` |
| `parent` | `ayah_numbering_system` |
| Vocalized | العَدّ المَكِّي |
| Other spellings | `makki_numbering`, `meccan_numbering` |

**Definition:** The counting of the people of Makkah, transmitted from Ibn Kathir from Mujahid from Ibn Abbas from Ubayy ibn Kab.

**Purpose:** Used as a value of the ayah numbering system, so that what a Mushaf's or a dataset's ayah numbers and boundaries rest on is known, and ayah positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

### Ayah Numbering System — نظام عد الآي

| | |
| --- | --- |
| `code` | `ayah_numbering_system` |
| `plural` | `ayah_numbering_systems` |
| `kind` | `classification` |
| Vocalized | نِظَام عَدّ الآي |
| Other spellings | `ayah_counting_system` |

**Definition:** A system that fixes the boundaries of the ayahs, their totals, their numbers, and certain questions about the basmalah, according to the schools of ayah counting.

**Purpose:** Used to state which system a given dataset's or Mushaf's ayah numbers and boundaries rest on.

### Equivalent Ayah — الآية المقابلة

| | |
| --- | --- |
| `code` | `equivalent_ayah` |
| `plural` | `equivalent_ayahs` |
| `kind` | `concept` |
| Vocalized | الآيَة المُقَابِلَة |

**Definition:** The ayah in one counting system that corresponds to an ayah in another, whether or not their numbers agree, since the systems divide the text at different points.

**Purpose:** Used to map ayah numbers across counting systems, so that data built on one system is never compared with data built on another by number alone.

- This is a correspondence between two counting systems, not a similarity of wording or a repetition of text.


## Revelation — `revelation`

### Asbab al-Nuzul — أسباب النزول

| | |
| --- | --- |
| `code` | `asbab_al_nuzul` |
| `kind` | `content` |
| Vocalized | أَسْبَاب النُّزُول |
| Other spellings | `asbab_al-nozool`, `asbab_un-nuzul` |

**Definition:** The events or questions that an ayah, or several ayahs, was revealed to address or to rule on.

**Purpose:** Used to attach the narrations and the material about an ayah's occasion of revelation to the ayah itself.

### Disputed — مختلف فيه

| | |
| --- | --- |
| `code` | `disputed` |
| `kind` | `classification_value` |
| `parent` | `revelation_classification` |
| Vocalized | مُخْتَلَف فِيه |

**Definition:** What the accepted sources disagree about classifying as Makki or Madani.

**Purpose:** Keeps disputed data from being forced into `Makki` or `Madani` without recording the disagreement.

### Madani — المدني

| | |
| --- | --- |
| `code` | `madani` |
| `kind` | `classification_value` |
| `parent` | `revelation_classification` |
| Vocalized | مَدَنِيّ |
| Other spellings | `madaniyy`, `madinan` |

**Definition:** What was revealed of the Quran after the Hijrah, even if it was revealed outside Madinah.

**Purpose:** Used as a value classifying a surah or an ayah under `Revelation Classification`.

### Makki — مكي

| | |
| --- | --- |
| `code` | `makki` |
| `plural` | `makkis` |
| `kind` | `classification_value` |
| `parent` | `revelation_classification` |
| Vocalized | مَكِّيّ |
| Other spellings | `makkiyy` |
| English gloss | `meccan` |

**Definition:** What was revealed of the Quran before the Hijrah, even if it was revealed outside Makkah.

**Purpose:** Used as a value classifying surahs or ayahs under revelation_classification. It is never used for the geographical place alone.

### Nuzul — النزول

| | |
| --- | --- |
| `code` | `nuzul` |
| `kind` | `concept` |
| Vocalized | النُّزُول |
| English gloss | `Revelation` |

**Definition:** The sending down of the Quran upon the Prophet, peace be upon him, in stages over the period of the message, according to events and need.

**Purpose:** Used as the root that the order of revelation, its classification and its occasions branch from: all three are properties of the event of revelation and are known only through it.

- Revelation is an event; its order, its classification and its occasion are properties of it, not synonyms for it.

### Revelation Classification — المكي والمدني

| | |
| --- | --- |
| `code` | `revelation_classification` |
| `kind` | `classification` |
| Vocalized | تَصْنِيف النُّزُول |

**Definition:** A classification of the Quranic text by whether its revelation fell before or after the Hijrah, in the accepted usage.

**Purpose:** Used to classify surahs or ayahs by their relation to the Hijrah, without implying that the classification is only geographical.

### Revelation Order — ترتيب النزول

| | |
| --- | --- |
| `code` | `revelation_order` |
| `kind` | `property` |
| Vocalized | تَرْتِيب النُّزُول |

**Definition:** The order of the surahs or the ayahs by the time of their revelation, which may differ from one accepted source to another.

**Purpose:** Used to store the order of revelation independently of the order of the Mushaf.


## Qiraat — `qiraat`

### Muqri — المقرئ

| | |
| --- | --- |
| `code` | `muqri` |
| `plural` | `muqris` |
| `kind` | `role` |
| Vocalized | المُقْرِئ |
| Other spellings | `muqree` |

**Definition:** One who has received the recitation, mastered it, and transmits it to learners.

**Purpose:** Used to represent the role of teaching, receiving and granting the recitation, which is distinct from being a `Reciter`.

### Qiraah — القراءة

| | |
| --- | --- |
| `code` | `qiraah` |
| `plural` | `qiraahs` |
| `kind` | `concept` |
| Vocalized | القِرَاءَة |
| Other spellings | `qira'ah`, `qiraa` |
| English gloss | `Reading` |

**Definition:** One of the ways of reciting the Quran, attributed to one of the imams of the qiraat, from which the riwayahs and turuq branch.

**Purpose:** Represents the top level of the qiraat model and ties together the riwayahs, the turuq, and the texts bound to them.

### Rawi — الراوي

| | |
| --- | --- |
| `code` | `rawi` |
| `plural` | `rawis` |
| `kind` | `role` |
| Vocalized | الرَّاوِي |
| English gloss | `Transmitter` |

**Definition:** One to whom a transmission from an imam of a qiraah is attributed.

**Purpose:** Used to represent the person a `Riwayah` is bound to. It is never used for the performer of a recording merely because they recite the Quran.

### Riwayah — الرواية

| | |
| --- | --- |
| `code` | `riwayah` |
| `plural` | `riwayahs` |
| `kind` | `concept` |
| `parent` | `qiraah` |
| Vocalized | الرِّوَايَة |
| Other spellings | `riwaya` |

**Definition:** What is attributed to a transmitter from an imam of a qiraah, such as the riwayah of Hafs from Asim.

**Purpose:** Used to state which riwayah a text, a Mushaf, a recording or a dataset follows.

### Tariq — الطريق

| | |
| --- | --- |
| `code` | `tariq` |
| `plural` | `tariqs` |
| `kind` | `concept` |
| `parent` | `riwayah` |
| Vocalized | الطَّرِيق |
| Other spellings | `tareeq` |

**Definition:** A path of transmission taken from a rawi through those below him in the chain of transmission of a qiraah.

**Purpose:** Used when data needs a finer level than the riwayah to tell paths of delivery and transmission apart.

> There is no registry of the turuq of the ten yet. Al-Nashr names the turuq of each riwayah, coming to some nine hundred and eighty at the level of the tariq. The set is closed and known, but it has not been written into a registry, so the gap is recorded rather than passed over.


## Recitation — `recitation`

### Ayah Timing

| | |
| --- | --- |
| `code` | `ayah_timing` |
| `plural` | `ayah_timings` |
| `kind` | `concept` |
| Other spellings | `ayah_timestamp`, `recitation_timing` |

**Definition:** A span of time in a recitation recording, given by a start and an end, corresponding to one ayah.

**Purpose:** Used to bind text to audio; following along while listening, jumping to an ayah, repeating it and clipping it all rest on it.

- A timing is a property of the recording, not of the ayah, so it differs from one recitation to another.
- Ayah-level timing is not word-level alignment.

### Recitation — التلاوة

| | |
| --- | --- |
| `code` | `recitation` |
| `plural` | `recitations` |
| `kind` | `entity` |
| Vocalized | التِّلَاوَة |
| Other spellings | `tilawah` |

**Definition:** Reading the Quran and delivering it aloud.

**Purpose:** Used to represent the act of reciting; in software it may represent a recording bound to a performer, a qiraah, a riwayah and a style of delivery.

### Reciter — القارئ

| | |
| --- | --- |
| `code` | `reciter` |
| `plural` | `reciters` |
| `kind` | `role` |
| Vocalized | القَارِئ |
| Other spellings | `qari` |

**Definition:** The person who performs a recitation of the Quran.

**Purpose:** Used to tie audio recordings to their performer, without assuming they are an imam of a `Qiraah` or a `Rawi`.

### Tartil — الترتيل

| | |
| --- | --- |
| `code` | `tartil` |
| `kind` | `concept` |
| Vocalized | التَّرْتِيل |
| Other spellings | `tarteel` |

**Definition:** Reciting the Quran deliberately, making the letters and words distinct, observing the stops and the meaning.

**Purpose:** Used when the concept of tartil itself is meant. It is never used as an automatic synonym for the `Murattal` recording style.


## Recitation pace — `recitation_pace`

### Hadr — الحدر

| | |
| --- | --- |
| `code` | `hadr` |
| `kind` | `classification_value` |
| `parent` | `recitation_pace` |
| Vocalized | الحَدْر |
| Other spellings | `hadar` |

**Definition:** Reciting quickly while keeping the letters, the vowels and the rules of delivery intact.

**Purpose:** Used to represent the fastest of the recitation paces.

### Recitation Pace — مرتبة القراءة من حيث السرعة

| | |
| --- | --- |
| `code` | `recitation_pace` |
| `kind` | `classification` |
| Vocalized | مَرَاتِب القِرَاءَة |

**Definition:** A classification of how fast a recitation is delivered while its rules are kept.

**Purpose:** Keeps the traditional paces apart from recording styles such as `Murattal` and `Mujawwad`.

### Tadwir — التدوير

| | |
| --- | --- |
| `code` | `tadwir` |
| `kind` | `classification_value` |
| `parent` | `recitation_pace` |
| Vocalized | التَّدْوِير |
| Other spellings | `tadweer` |

**Definition:** Reciting at a middle speed between tahqiq and hadr, while keeping the rules.

**Purpose:** Used to represent the middle pace of recitation.

### Tahqiq — التحقيق

| | |
| --- | --- |
| `code` | `tahqiq` |
| `kind` | `classification_value` |
| `parent` | `recitation_pace` |
| Vocalized | التَّحْقِيق |
| Other spellings | `tahqeeq` |

**Definition:** Reciting slowly and deliberately, giving the letters and their rules their full due; much used in teaching.

**Purpose:** Used to describe the slow, exacting pace of recitation.


## Recitation style — `recitation_style`

### Instructional Ayah Repetition — تكرار الآيات للتعليم

| | |
| --- | --- |
| `code` | `instructional_ayah_repetition` |
| `kind` | `concept` |
| Vocalized | تَكْرَار الآيَات |

**Definition:** Repeating an ayah, or part of one, once or several times in a teaching pattern that helps the learner take it in and memorise it.

**Purpose:** Used to describe a feature of a teaching recording in its own right, rather than leaving it implied inside `Muallim`.

### Muallim — معلم

| | |
| --- | --- |
| `code` | `muallim` |
| `kind` | `classification_value` |
| `parent` | `recitation_style` |
| Vocalized | مُعَلِّم |

**Definition:** A recitation style meant for teaching, which may repeat ayahs or leave the learner time to repeat after the reciter.

**Purpose:** Used to classify teaching recordings and keep them apart from ordinary ones.

### Mujawwad — مجود

| | |
| --- | --- |
| `code` | `mujawwad` |
| `kind` | `classification_value` |
| `parent` | `recitation_style` |
| Vocalized | مُجَوَّد |

**Definition:** A description of a recitation or a recording published as mujawwad.

**Purpose:** Used to classify the style of a recording. It is never used as a synonym for the discipline of `Tajwid`.

### Murattal — مرتل

| | |
| --- | --- |
| `code` | `murattal` |
| `kind` | `classification_value` |
| `parent` | `recitation_style` |
| Vocalized | مُرَتَّل |

**Definition:** A description of a recitation or a recording published as murattal.

**Purpose:** Used to classify a recording. It is never used as a general synonym for the concept of `Tartil`.

### Recitation Style — نمط أداء التلاوة

| | |
| --- | --- |
| `code` | `recitation_style` |
| `plural` | `recitation_styles` |
| `kind` | `classification` |
| Vocalized | نَمَط الأَدَاء |

**Definition:** A classification describing the manner of delivery of a recitation or a recording, independent of the qiraah and the riwayah.

**Purpose:** Used to classify audio recordings by their manner of delivery or by their purpose.


## Tajwid — `tajwid`

### Istiadhah — الاستعاذة

| | |
| --- | --- |
| `code` | `istiadhah` |
| `kind` | `concept` |
| Vocalized | الاِسْتِعَاذَة |
| Other spellings | `isti'adhah`, `istiʿādhah`, `ta'awwudh` |

**Definition:** Seeking refuge with Allah from the Shaytan before reciting the Quran.

**Purpose:** Used to represent the istiadhah, its wordings, and its position relative to the start of a recitation.

### Khatmah — الختمة

| | |
| --- | --- |
| `code` | `khatmah` |
| `plural` | `khatmahs` |
| `kind` | `concept` |
| Vocalized | الخَتْمَة |
| Other spellings | `khatma` |

**Definition:** Reading the Quran in full, from its beginning to its end.

**Purpose:** Used to track completion plans, to record that a reading was finished, and to tie sessions to the course of one khatmah.

### Noon Sakinah — النون الساكنة

| | |
| --- | --- |
| `code` | `noon_sakinah` |
| `kind` | `concept` |
| Vocalized | النُّون السَّاكِنَة |
| Other spellings | `nun_sakinah`, `noon_saakinah` |
| English gloss | `Unvowelled Noon` |

**Definition:** A noon carrying no vowel, fixed in pronunciation and in writing, in continuing and in stopping.

**Purpose:** We use it as the place that the rulings of izhar, idgham, iqlab and ikhfa branch from in tajwid engines.

### Saktah — السكتة

| | |
| --- | --- |
| `code` | `saktah` |
| `plural` | `saktahs` |
| `kind` | `concept` |
| Vocalized | السَّكْتَة |
| Other spellings | `sakta` |

**Definition:** Cutting off the voice for a short moment without breathing, then continuing the recitation.

**Purpose:** Used to represent where a saktah falls and what its properties are in the text or in a recitation.

### Tajweed — تجويد

| | |
| --- | --- |
| `code` | `tajwid` |
| `kind` | `concept` |
| Vocalized | تَجْوِيد |
| Other spellings | `tajweed` |

**Definition:** The discipline of delivering the letters of the Quran from their points of articulation and giving them their due properties and rulings.

**Purpose:** Represents the field that gathers the rules of tajwid, its rulings and application annotations; rulings and rules in dictionaries and engines are attributed to it.


## Waqf — `waqf`

### Sujud al-Tilawah — سجود التلاوة

| | |
| --- | --- |
| `code` | `sujud_al_tilawah` |
| `kind` | `concept` |
| Vocalized | سُجُود التِّلَاوَة |
| Other spellings | `sajdah_al-tilawah`, `sajdat_al-tilawah` |

**Definition:** A prostration performed on reciting or hearing one of the places of sujud al-tilawah.

**Purpose:** Represents the act of worship, or its ruling, and stays independent of the mark printed in the Mushaf.

### Waqf — الوقف

| | |
| --- | --- |
| `code` | `waqf` |
| `kind` | `concept` |
| Vocalized | الوَقْف |

**Definition:** Stopping the recitation at a place in the text according to the rules of stopping and starting.

**Purpose:** Represents the general concept of stopping, while `Waqf Mark` represents the printed signs that point to it.

### Waqf Hasan — الوقف الحسن

| | |
| --- | --- |
| `code` | `waqf_hasan` |
| `kind` | `classification_value` |
| `parent` | `waqf_ruling` |
| Vocalized | الوَقْف الحَسَن |

**Definition:** A stop that yields a meaning but is connected to what follows it in wording and in meaning.

**Purpose:** Used as a value in classifying the places of stopping.

### Waqf Kafi — الوقف الكافي

| | |
| --- | --- |
| `code` | `waqf_kafi` |
| `kind` | `classification_value` |
| `parent` | `waqf_ruling` |
| Vocalized | الوَقْف الكَافِي |

**Definition:** A stop whose meaning is complete but which is connected to what follows it in meaning, not in wording.

**Purpose:** Used as a value in classifying the places of stopping.

### Waqf Mark — علامة الوقف

| | |
| --- | --- |
| `code` | `waqf_mark` |
| `plural` | `waqf_marks` |
| `kind` | `mark` |
| `parent` | `mushaf_mark` |
| Vocalized | عَلَامَة الوَقْف |

**Definition:** A mark in the Mushaf pointing the reader to the ruling on stopping or continuing at a given place.

**Purpose:** Used to represent the sign, its position and its type in an orderly way.

### Waqf Mark Type — نوع علامة الوقف

| | |
| --- | --- |
| `code` | `waqf_mark_type` |
| `kind` | `classification` |
| Vocalized | نَوْع عَلَامَة الوَقْف |

**Definition:** A classification of what a waqf mark drawn in the Mushaf points to: that stopping is compulsory, forbidden or permitted.

**Purpose:** Gives applications one set of values to branch on, instead of reading the shape of the sign itself.

### Waqf Qabih — الوقف القبيح

| | |
| --- | --- |
| `code` | `waqf_qabih` |
| `kind` | `classification_value` |
| `parent` | `waqf_ruling` |
| Vocalized | الوَقْف القَبِيح |

**Definition:** A stop that yields no meaning, or yields a meaning that is not the one intended.

**Purpose:** Used as a value in classifying the places of stopping, and to warn the learner in teaching applications.

### Waqf Ruling — حكم الوقف

| | |
| --- | --- |
| `code` | `waqf_ruling` |
| `kind` | `classification` |
| Vocalized | حُكْم الوَقْف |

**Definition:** A classification of the place itself by whether the meaning is complete there, not of the mark drawn at it.

**Purpose:** Used in teaching and in the syntactic and semantic analysis of stopping. It stays independent of `waqf_mark_type` because the two classify different things: this one the place, that one the mark.

### Waqf Tamm — الوقف التام

| | |
| --- | --- |
| `code` | `waqf_tamm` |
| `kind` | `classification_value` |
| `parent` | `waqf_ruling` |
| Vocalized | الوَقْف التَّامّ |

**Definition:** A stop whose meaning is complete and which is connected to what follows it neither in wording nor in meaning.

**Purpose:** Used as a value in classifying the places of stopping, for teaching and for analysis.


## Linguistics — `linguistics`

### Fil — الفعل

| | |
| --- | --- |
| `code` | `fil` |
| `kind` | `classification_value` |
| `parent` | `part_of_speech` |
| Vocalized | الفِعْل |
| English gloss | `Verb` |

**Definition:** A word carrying a meaning in itself bound to a time, inflecting for past, present and imperative.

**Purpose:** Used as a value of part of speech, and the morphological features specific to verbs — tense, voice and pattern — hang off it.

### Harf al-Mana — حرف المعنى

| | |
| --- | --- |
| `code` | `harf_al_mana` |
| `kind` | `classification_value` |
| `parent` | `part_of_speech` |
| Vocalized | حَرْف المَعْنَى |
| English gloss | `Particle` |

**Definition:** A word carrying a meaning in something other than itself, such as the prepositions and the particles of conjunction, negation and interrogation.

**Purpose:** Used as a value of part of speech. It takes the full name because `harf` alone is the name of the written letter, which is a unit of writing and not a part of speech.

- Harf al-mana is a part of speech; the written letter — `letter` — is a unit of the written text.

### Irab — الإعراب

| | |
| --- | --- |
| `code` | `irab` |
| `kind` | `analysis` |
| Vocalized | الإِعْرَاب |
| Other spellings | `i'rab` |
| English gloss | `Grammatical Analysis` |

**Definition:** The statement of the syntactic function of words, their case markers, and their relations within the construction.

**Purpose:** Used to attach syntactic analysis and grammatical functions to the words of an ayah.

### Ism — الاسم

| | |
| --- | --- |
| `code` | `ism` |
| `kind` | `classification_value` |
| `parent` | `part_of_speech` |
| Vocalized | الاِسْم |
| English gloss | `Noun` |

**Definition:** A word carrying a meaning in itself not bound to a time: nouns, adjectives, pronouns, demonstratives and relatives all fall under it.

**Purpose:** Used as a value of part of speech, and the detailed tags that Quranic morphology corpora use fall under it.

### Lemma

| | |
| --- | --- |
| `code` | `lemma` |
| `plural` | `lemmas` |
| `kind` | `unit` |

**Definition:** The base dictionary form that an inflected word form is referred back to.

**Purpose:** Used to gather the different inflected forms under one dictionary entry.

### Morpheme — الوحدة الصرفية

| | |
| --- | --- |
| `code` | `morpheme` |
| `plural` | `morphemes` |
| `kind` | `unit` |
| Vocalized | الوَحْدَة الصَّرْفِيَّة |
| Other spellings | `segment`, `word_segment` |

**Definition:** The smallest unit within a word carrying a meaning or a morphological function, such as a prefix, a suffix or a stem.

**Purpose:** Used to represent the division of a Quranic word into its morphological parts, which is the level that morphological features and tags are attached to in analysis corpora.

- A morpheme is a part of a word; a token is a unit of segmentation that may equal a word or span more than one.

### Morphology — الصرف

| | |
| --- | --- |
| `code` | `morphology` |
| `kind` | `analysis` |
| Vocalized | الصَّرْف |

**Definition:** The analysis of a word's structure and form and the morphological properties it carries.

**Purpose:** Used to represent the morphological features of words or tokens.

### Part of Speech — قسم الكلمة

| | |
| --- | --- |
| `code` | `part_of_speech` |
| `kind` | `classification` |
| Vocalized | قِسْم الكَلِمَة |
| Other spellings | `pos` |
| English gloss | `Part of Speech` |

**Definition:** The classification of a word or a morpheme by its grammatical class: ism, fil, harf and what branches from them.

**Purpose:** Used as the basic tag in morphological and syntactic analysis; searching by tag, filtering, and building the syntactic analysis all rest on it.

> The threefold division is the level this standard fixes. The detailed tags used by Quranic morphology corpora — dozens of them — are data falling under these three values, and are not given entries of their own in the dictionary.

### Root — الجذر

| | |
| --- | --- |
| `code` | `root` |
| `plural` | `roots` |
| `kind` | `unit` |
| Vocalized | الجَذْر |

**Definition:** The morphological origin a word is referred back to, showing its derivation and its relation to other words.

**Purpose:** Used for morphological search, linguistic analysis, and gathering words that share an origin.

### Stem — الجذع

| | |
| --- | --- |
| `code` | `stem` |
| `plural` | `stems` |
| `kind` | `unit` |
| Vocalized | الجِذْع |

**Definition:** What remains of a word once its prefixes and suffixes are removed, and what the morphological additions attach to.

**Purpose:** Used in morphological analysis as a level between the word form and its root: some corpora record the stem and not the root, and some record both.

- A root is an abstract derivational origin; a stem is a form that stands in the word once the additions are removed.


## Translation — `translation`

### Spoken Translation — الترجمة المنطوقة

| | |
| --- | --- |
| `code` | `spoken_translation` |
| `plural` | `spoken_translations` |
| `kind` | `content` |
| `parent` | `translation` |
| Vocalized | التَّرْجَمَة المَنْطُوقَة |
| Other spellings | `audio_translation` |

**Definition:** Rendering the meanings of the Quran into another language in audio or spoken material.

**Purpose:** Used to distinguish audio renderings of the meanings from written translation and from Quranic recitation.

### Translation — الترجمة

| | |
| --- | --- |
| `code` | `translation` |
| `plural` | `translations` |
| `kind` | `content` |
| Vocalized | التَّرْجَمَة |

**Definition:** Rendering the meanings of the Quran into another language. A translation is not the Quran in its wording.

**Purpose:** Used to tie translated-meaning texts to ayahs, languages, translators and sources.

### Transliteration — النقل الحرفي

| | |
| --- | --- |
| `code` | `transliteration` |
| `plural` | `transliterations` |
| `kind` | `content` |
| Vocalized | النَّقْل الحَرْفِيّ |

**Definition:** Representing the letters of one writing system with those of another by fixed rules, without translating the meaning.

**Purpose:** Used to give a readable representation in another writing system, or for systematic conversion between writing systems.


## Tafsir — `tafsir`

### Mufassir — المفسر

| | |
| --- | --- |
| `code` | `mufassir` |
| `plural` | `mufassirs` |
| `kind` | `role` |
| Vocalized | المُفَسِّر |
| English gloss | `Exegete` |

**Definition:** One to whom a tafsir of the Quran is attributed, whether by authorship or by transmission.

**Purpose:** Used to attribute a tafsir to its author, keeping the one who said it apart from the book his words were transmitted in, and from its editor and publisher.

- The mufassir is the one whose statement it is, and his statement may be transmitted in someone else's book.

### Tafsir — التفسير

| | |
| --- | --- |
| `code` | `tafsir` |
| `plural` | `tafsirs` |
| `kind` | `content` |
| Vocalized | التَّفْسِير |
| Other spellings | `tafseer` |
| English gloss | `Exegesis`, `Commentary` |

**Definition:** Stating the meanings of the Quran, explaining its wording, and the rulings and guidance it points to, according to the principles of tafsir.

**Purpose:** Used to represent tafsir works and content and to tie their passages to ayahs, surahs and sources.

### Tafsir Mathur — التفسير المأثور

| | |
| --- | --- |
| `code` | `tafsir_mathur` |
| `kind` | `content` |
| Vocalized | التَّفْسِير المَأْثُور |
| Other spellings | `tafsir_bil_mathur`, `tafsir_bialmathur`, `mathur` |
| English gloss | `Transmitted Tafsir` |

**Definition:** What the Quran has been explained by from the Quran itself, from the Sunnah, or from the sayings of the Companions and the Successors, transmitted with its chain.

**Purpose:** Used as content attached to an ayah and carrying its transmitter and the standing of the transmission with it, so it is not treated as authored tafsir text attributed to a single book.

- Tafsir mathur is transmitted with a chain; authored tafsir is the statement of the book's author.
- A single report is not a concept in this standard; the concept is the kind of content organised by ayah.

> The better-known title is «التَّفْسِير بِالمَأْثُور», whose derivation fuses the preposition to the noun and gives `tafsir_bialmathur`. The name recorded here is the descriptive form, which is Arabic and in use, and the better-known form resolves through `alternative_spellings`. This is the same reason `naskh` was given an entry rather than «الناسخ والمنسوخ».


## Quranic sciences — `quranic_sciences`

### Asma al-Surah — أسماء السورة

| | |
| --- | --- |
| `code` | `asma_al_surah` |
| `kind` | `content` |
| Vocalized | أَسْمَاء السُّورَة |
| Other spellings | `asmaa_al_surah` |
| English gloss | `Surah Names` |

**Definition:** The names a surah is known by. Most surahs carry more than one: some established by narration, others settled by usage.

**Purpose:** Used because a surah's name is not one field: Mushafs differ over the name they print, and search has to find a surah by any of its names.

- A name is not the reason for the name: the first is what the surah is called, the second is why.
- The names of a surah are not the names of the Quran itself.

### Fadail al-Quran — فضائل القرآن

| | |
| --- | --- |
| `code` | `fadail_al_quran` |
| `kind` | `content` |
| Vocalized | فَضَائِل القُرْآن |
| Other spellings | `fadail`, `fadail_al_surah` |
| English gloss | `Merits` |

**Definition:** What has been transmitted about the merit of the Quran, or of one of its surahs or ayahs, and the reward or effect that follows from reciting it.

**Purpose:** Used as content attached to the whole Quran, to a surah or to an ayah. It is kept apart from tafsir because it does not explain meaning, and from hadith because it is organised by place in the text rather than by narrator.

- The merit is attached to a place in the Quran; the hadith it comes from is a source it cites, not its location.
- Much of what is transmitted about the merits of surahs is weak or fabricated, so it is bound to its source and its grading.

### Gharib al-Quran — غريب القرآن

| | |
| --- | --- |
| `code` | `gharib_al_quran` |
| `kind` | `content` |
| Vocalized | غَرِيب القُرْآن |
| Other spellings | `gharib`, `word_meaning` |
| English gloss | `Word Meanings` |

**Definition:** The explanation of Quranic words whose meaning is obscure to most readers, whether because they are rare in use or because their sense has shifted.

**Purpose:** Used as content attached to a particular word of an ayah rather than to the whole ayah, which is what sets it apart from tafsir and its explanation of the ayah's overall meaning.

- Gharib al-Quran explains a word; tafsir explains the meaning of an ayah.
- The meaning is attributed to a particular book, so it may differ between sources.

### Maqasid al-Surah — مقاصد السورة

| | |
| --- | --- |
| `code` | `maqasid_al_surah` |
| `kind` | `content` |
| Vocalized | مَقَاصِد السُّورَة |
| Other spellings | `maqasid` |
| English gloss | `Surah Objectives` |

**Definition:** The overarching meanings a surah turns on, held together by its subject, and the single aim its ayahs are ordered around.

**Purpose:** Used as content attached to a whole surah rather than to one of its ayahs, which sets it apart from tafsir, that proceeds ayah by ayah, and from the topics, that enumerate what the surah contains.

- A maqsad is an aim that gathers the surah; a topic is one of the things it contains.

### Mutashabihat — المتشابهات

| | |
| --- | --- |
| `code` | `mutashabihat` |
| `kind` | `analysis` |
| Vocalized | المُتَشَابِهَات |
| Other spellings | `mutashabih`, `mutashabihat_lafziyyah`, `similar_ayahs` |
| English gloss | `Similar Passages` |

**Definition:** The places in the Quran where the wording of ayahs, or of parts of them, resembles one another, whether exactly or with a slight difference in a word or in order.

**Purpose:** Used above all for memorisation, revision and search tools, since a memoriser needs to know which places are confused with one another and where they differ.

- The resemblance of wording meant here is not the mutashabih that stands opposite the muhkam in the Quranic sciences.
- A resemblance is a relation between two places or more, not a property of a single ayah.

### Naskh — النسخ

| | |
| --- | --- |
| `code` | `naskh` |
| `kind` | `concept` |
| Vocalized | النَّسْخ |
| Other spellings | `nasikh_mansukh`, `nasikh_wa_mansukh`, `nasekh_mansokh` |
| English gloss | `Abrogation` |

**Definition:** The lifting of a legal ruling by a later legal proof. In the Quran it is studied by relating an abrogating ayah to an abrogated one.

**Purpose:** Used to represent the relation between two ayahs, one abrogating and one abrogated: a relation between two places in the text, not a property of a single ayah.

- Abrogation bears on the ruling, not on the text: an ayah whose ruling is abrogated stands in the Mushaf as it is.
- The relation is disputed in many places, so it is bound to its source and never presented as agreed upon.

### Sabab al-Tasmiyah — سبب التسمية

| | |
| --- | --- |
| `code` | `sabab_al_tasmiyah` |
| `kind` | `content` |
| Vocalized | سَبَب التَّسْمِيَة |
| Other spellings | `sabab_al_tasmiya` |

**Definition:** The statement of why a surah was given its name, and what has been transmitted about it by narration or on linguistic grounds.

**Purpose:** Used as content attached to a surah. It is kept apart from the occasion of revelation because it concerns the name and not the revelation, and because many surahs have more than one name and so more than one reason.

- The reason for the name concerns the surah's name; the occasion of revelation concerns the revelation of an ayah.

### Tadabbur — التدبر

| | |
| --- | --- |
| `code` | `tadabbur` |
| `plural` | `tadabburs` |
| `kind` | `content` |
| Vocalized | التَّدَبُّر |
| Other spellings | `tadabur`, `waqfat_tadabburiyyah` |
| English gloss | `Reflection` |

**Definition:** Reflecting on the meanings of the Quran and what they call for in action, and what a reader records of a pause at an ayah or a word.

**Purpose:** Used as content attached to an ayah or to a place within it. It is kept apart from tafsir because it does not undertake to state the apparent meaning, and the one who says it is not necessarily a mufassir.

- Tafsir states the meaning of an ayah by a method; tadabbur is the effect of that meaning on the one reflecting.
