---
title: Terminology dictionary
description: The concepts used in Quranic software, with their definitions and their adopted names.
status: draft
sidebar:
  order: 2
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
> Generated from `standards/terminology/concepts/*.yml` — edit the entry, not
> this page, then run `python3 tools/build.py`.

## Lookup

One row per concept, sorted by code. Follow the code to the full entry.

| code | display | Arabic | kind | category | definition |
| --- | --- | --- | --- | --- | --- |
| [`alaqat_al_harfayn`](#alaqat_al_harfayn) | Alaqat al-Harfayn | علاقة الحرفين | `classification` | `tajwid` | The relation of two adjacent letters to each other in point of articulation and attribute: identical, of one kind, close, or distant; the merging of the first into the second, or its clear sounding, is built on it. |
| [`asbab_al_nuzul`](#asbab_al_nuzul) | Asbab al-Nuzul | أسباب النزول | `content` | `revelation` | The events or questions that an ayah, or several ayahs, was revealed to address or to rule on. |
| [`asma_al_surah`](#asma_al_surah) | Asma al-Surah | أسماء السورة | `content` | `quranic_sciences` | The names a surah is known by. |
| [`ayah`](#ayah) | Ayah | الآية | `entity` | `structure` | A unit of the Quranic text falling within a surah and having determined boundaries. |
| [`ayah_count`](#ayah_count) | Ayah Count | عدد الآيات | `property` | `ayah_numbering` | The number of ayahs in a surah under a given numbering system; it may differ from one system to another as the counted fasilahs differ. |
| [`ayah_key`](#ayah_key) | Ayah Key |  | `property` | `structure` | A textual identifier of an ayah joining its surah number and its number within it with a colon, in the form `2:255`; it is read only in the light of the ayah numbering system it rests on. |
| [`ayah_mark`](#ayah_mark) | Ayah Mark | علامة الآية | `mark` | `dabt` | The circle separating one ayah from the next. |
| [`ayah_numbering_basri`](#ayah_numbering_basri) | Basri Numbering | العد البصري | `classification_value` | `ayah_numbering` | The Basran numbering system, transmitted from Asim al-Jahdari and the Basran authorities before him. |
| [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi) | Dimashqi Numbering | العد الدمشقي | `classification_value` | `ayah_numbering` | The Damascene numbering system, transmitted from Yahya ibn al-Harith al-Dhimari from Ibn Amir; also called the Shami numbering. |
| [`ayah_numbering_kufi`](#ayah_numbering_kufi) | Kufi Numbering | العد الكوفي | `classification_value` | `ayah_numbering` | The Kufan numbering system, transmitted from Hamzah al-Zayyat from Ibn Abi Layla from Abu Abd al-Rahman al-Sulami from Ali ibn Abi Talib. |
| [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir) | Madani Akhir Numbering | العد المدني الأخير | `classification_value` | `ayah_numbering` | The later Madinan numbering system, that of Ismail ibn Jafar from Sulayman ibn Jammaz. |
| [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal) | Madani Awwal Numbering | العد المدني الأول | `classification_value` | `ayah_numbering` | The earlier Madinan numbering system, that of Abu Jafar Yazid ibn al-Qaqa and Shaybah ibn Nassah. |
| [`ayah_numbering_makki`](#ayah_numbering_makki) | Makki Numbering | العد المكي | `classification_value` | `ayah_numbering` | The Makkan numbering system, transmitted from Ibn Kathir from Mujahid from Ibn Abbas from Ubayy ibn Kab. |
| [`ayah_numbering_system`](#ayah_numbering_system) | Ayah Numbering System | نظام عد الآي | `classification` | `ayah_numbering` | A system that fixes the boundaries of the ayahs, their totals and their numbers, and certain questions about the basmalah, as transmitted by one of the schools of ayah counting. |
| [`ayah_timing`](#ayah_timing) | Ayah Timing |  | `concept` | `recitation` | A span of time in a recitation recording, given by a start and an end, corresponding to one ayah. |
| [`basmalah`](#basmalah) | Basmalah | البسملة | `concept` | `structure` | The formula «بسم الله الرحمن الرحيم» with which the surahs open, except surah al-Tawbah. |
| [`character`](#character) | Character |  | `unit` | `text` | An abstract unit of text in a digital encoding; it need not correspond to a single linguistic letter. |
| [`codepoint`](#codepoint) | Codepoint |  | `unit` | `text` | A numeric value defined by an encoding standard such as Unicode. |
| [`dammah`](#dammah) | Dammah | الضمة | `mark` | `dabt` | The mark for the short vowel u on the letter. |
| [`disputed`](#disputed) | Disputed | مختلف فيه | `classification_value` | `revelation` | A surah or ayah that the accepted sources do not agree to classify as makki or madani. |
| [`division_mark`](#division_mark) | Division Mark | علامة التقسيم | `mark` | `dabt` | Marks the start of a juz, a hizb, or a half or quarter of one. |
| [`dot`](#dot) | Dot | النقطة | `mark` | `dabt` | One dot, above or below, distinguishing a letter from the others that share its skeleton (ijam): baa, noon, jeem, khaa, dhaal. |
| [`equivalent_ayah`](#equivalent_ayah) | Equivalent Ayah | الآية المقابلة | `concept` | `ayah_numbering` | The ayah in one numbering system that corresponds to an ayah in another. |
| [`fadail_al_quran`](#fadail_al_quran) | Fadail al-Quran | فضائل القرآن | `content` | `quranic_sciences` | What has been transmitted about the merit of the Quran, or of one of its surahs or ayahs, and the reward or effect that follows from reciting it. |
| [`farsh`](#farsh) | Farsh | الفرش | `concept` | `qiraat` | The words the readers differ on at particular places in the surahs, where the difference follows no general rule but each place is named on its own, arranged by surah. |
| [`fasilah`](#fasilah) | Fasilah | الفاصلة | `concept` | `structure` | The close of an ayah or a passage as a matter of its composition; some scholars define it as the ayah's last word. |
| [`fathah`](#fathah) | Fathah | الفتحة | `mark` | `dabt` | The mark for the short vowel a on the letter. |
| [`fil`](#fil) | Fil | الفعل | `classification_value` | `linguistics` | A verb: a word whose meaning is tied to a time, with past, present and imperative forms. |
| [`font`](#font) | Font | الخط | `concept` | `mushaf` | A file carrying a set of glyphs and the rules for laying them out, used to render the text of a mushaf. |
| [`gharib_al_quran`](#gharib_al_quran) | Gharib al-Quran | غريب القرآن | `content` | `quranic_sciences` | The explanation of Quranic words whose meaning is obscure to most readers, whether because they are rare in use or because their sense has shifted. |
| [`ghunnah`](#ghunnah) | Ghunnah | الغنة | `concept` | `tajwid` | A sound from the nasal cavity built into the body of noon and meem, in which the tongue plays no part; its length differs by ruling, fullest in the doubled and the merged letter, then in the concealed, then in the vowelless letter sounded clearly. |
| [`glyph`](#glyph) | Glyph |  | `unit` | `text` | The visual shape a font produces to represent a letter, a character, or a group of them. |
| [`grapheme`](#grapheme) | Grapheme |  | `unit` | `text` | A written unit that a user perceives as one unit, which may consist of more than one `codepoint`. |
| [`hadr`](#hadr) | Hadr | الحدر | `classification_value` | `recitation_pace` | Reciting quickly while keeping the letters, the vowels and the rules of delivery intact. |
| [`hamzah`](#hamzah) | Hamzah | الهمزة | `mark` | `dabt` | Marks a fully realised hamzah (hamzat al-qat). |
| [`hamzat_al_wasl`](#hamzat_al_wasl) | Hamzat al-Wasl | همزة الوصل | `mark` | `dabt` | Marks a connecting hamzah, dropped whenever the word is reached in continuation. |
| [`harakah`](#harakah) | Harakah | الحركة | `classification` | `dabt` | A mark fixing a letter's vowel, its absence or its doubling: fathah, dammah, kasrah, sukun and shaddah. |
| [`harf_al_mana`](#harf_al_mana) | Harf al-Mana | حرف المعنى | `classification_value` | `linguistics` | A particle: a word with no meaning of its own that gives meaning to the words around it, such as prepositions and the particles of conjunction, negation and interrogation. |
| [`harf_muqatta`](#harf_muqatta) | Harf Muqatta | الحرف المقطع | `concept` | `structure` | Alphabetic letters that open certain surahs, such as Alif Laam Meem, Alif Laam Raa, Haa Meem and Kaaf Haa Yaa Ayn Saad. |
| [`hifz`](#hifz) | Hifz | الحفظ | `concept` | `recitation` | Committing the Quran, in whole or in part, to memory, so that it is recited without looking in the mushaf. |
| [`hizb`](#hizb) | Hizb | الحزب | `entity` | `divisions` | In the current division, half a juz, so that the Quran is 60 hizbs. |
| [`hukm_al_tajwid`](#hukm_al_tajwid) | Hukm al-Tajwid | حكم التجويد | `classification` | `tajwid` | What is due in delivering a letter before the letter that follows it, or at a sukun or a hamzah: izhar, idgham, iqlab, ikhfa, madd, qalqalah, tafkhim or tarqiq, as the rules of tajwid settle it at a given place in the text. |
| [`huruf_muqattaah`](#huruf_muqattaah) | Huruf Muqattaah | الحروف المقطعة | `concept` | `structure` | The group of alphabetic letters that open 29 surahs, read by the names of the letters and not by their sounds, such as «الم» and «كهيعص». |
| [`idgham`](#idgham) | Idgham | الإدغام | `classification_value` | `tajwid` | Merging a vowelless letter into a vowelled letter after it so that the two become one doubled letter, whether the merging is complete or partial, with ghunnah or without it. |
| [`ijam`](#ijam) | Ijam | الإعجام | `classification` | `dabt` | The dotting that distinguishes a letter from the letters that share its written shape. |
| [`ikhfa`](#ikhfa) | Ikhfa | الإخفاء | `classification_value` | `tajwid` | Pronouncing a vowelless letter in a manner between izhar and idgham, without doubling and with the ghunnah kept: haqiqi in noon sakinah and tanwin before its 15 letters, and shafawi in meem sakinah before a baa. |
| [`imalah`](#imalah) | Imalah | الإمالة | `mark` | `dabt` | Marks the major imalah: a fathah pronounced leaning toward kasrah. |
| [`instructional_ayah_repetition`](#instructional_ayah_repetition) | Instructional Ayah Repetition | تكرار الآيات | `concept` | `recitation_style` | Repeating an ayah, or part of one, once or several times in a teaching pattern that helps the learner take it in and memorise it. |
| [`iqlab`](#iqlab) | Iqlab | الإقلاب | `classification_value` | `tajwid` | Turning noon sakinah or tanwin into a meem, concealed with ghunnah, before a baa. |
| [`irab`](#irab) | Irab | الإعراب | `analysis` | `linguistics` | The statement of the syntactic function of words, their case markers, and their relations within the construction. |
| [`ishmam`](#ishmam) | Ishmam | الإشمام | `mark` | `dabt` | Marks ishmam: the lips are rounded to hint at a dropped dammah, without any sound. |
| [`ism`](#ism) | Ism | الاسم | `classification_value` | `linguistics` | A noun in the Arabic sense: a word whose meaning is not tied to a time. |
| [`istiadhah`](#istiadhah) | Istiadhah | الاستعاذة | `concept` | `recitation` | Seeking refuge with Allah from the Shaytan before reciting the Quran. |
| [`izhar`](#izhar) | Izhar | الإظهار | `classification_value` | `tajwid` | Sounding a vowelless letter from its point of articulation with no added ghunnah, as noon sakinah and tanwin are sounded before the throat letters, and meem sakinah before any letter other than baa and meem. |
| [`juz`](#juz) | Juz | الجزء | `entity` | `divisions` | One of the 30 parts of the well-known division of the mushaf, made to ease reading and completing it. |
| [`kasrah`](#kasrah) | Kasrah | الكسرة | `mark` | `dabt` | The mark for the short vowel i on the letter. |
| [`khatmah`](#khatmah) | Khatmah | الختمة | `concept` | `recitation` | Reading the Quran in full, from its beginning to its end. |
| [`lahn`](#lahn) | Lahn | اللحن | `classification` | `tajwid` | Error in reciting the Quran and departure from what is correct, whether plain or subtle. |
| [`lahn_jali`](#lahn_jali) | Lahn Jali | اللحن الجلي | `classification_value` | `tajwid` | An error in the wording that damages its form or its meaning, such as one letter put for another or one vowel for another; the learned and the unlearned alike notice it. |
| [`lahn_khafi`](#lahn_khafi) | Lahn Khafi | اللحن الخفي | `classification_value` | `tajwid` | An error in the wording that damages the perfection of delivery without touching form or meaning, such as dropping the ghunnah or shortening a madd; only those trained in the discipline notice it. |
| [`layout`](#layout) | Layout | التخطيط | `concept` | `mushaf` | The visual arrangement of the text and its elements into pages, lines and positions within a given mushaf or view. |
| [`lemma`](#lemma) | Lemma |  | `unit` | `linguistics` | The base dictionary form that an inflected word form is referred back to. |
| [`letter`](#letter) | Letter | الحرف | `unit` | `text` | A letter of the alphabet as a linguistic unit of writing. |
| [`line`](#line) | Line | السطر | `unit` | `mushaf` | A typeset line within a page of a mushaf or of a given layout. |
| [`madani`](#madani) | Madani | مدني | `classification_value` | `revelation` | The part of the Quran revealed after the Hijrah, even where it was revealed outside Madinah. |
| [`madd`](#madd) | Madd | المد | `classification` | `tajwid` | Prolonging the sound on one of the three letters of madd: a vowelless alif after a fathah, a vowelless waw after a dammah, a vowelless yaa after a kasrah; whether the madd is original, without which the letter does not stand, or secondary, caused by a hamzah or a sukun. |
| [`madd_al_badal`](#madd_al_badal) | Madd al-Badal | مد البدل | `classification_value` | `tajwid` | A madd caused by a hamzah before the letter of madd, where the letter of madd was substituted for a vowelless hamzah, as in «آمن», «أوتوا» and «إيمان»; its length is 2 counts for Hafs, more for Warsh. |
| [`madd_al_iwad`](#madd_al_iwad) | Madd al-Iwad | مد العوض | `classification_value` | `tajwid` | Lengthening an alif in place of tanwin al-fath when stopping on the word; its length is 2 counts. |
| [`madd_al_lin`](#madd_al_lin) | Madd al-Lin | مد اللين | `classification_value` | `tajwid` | Lengthening a vowelless waw or yaa preceded by a fathah when stopping on the word with an incidental sukun, as in «خوف» and «بيت». |
| [`madd_al_silah`](#madd_al_silah) | Madd al-Silah | مد الصلة | `classification_value` | `tajwid` | A madd arising from joining the pronoun haa to a waw or a yaa when it falls between two vowelled letters; sughra when no hamzah follows, kubra when one does. |
| [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun) | Madd Arid lil-Sukun | المد العارض للسكون | `classification_value` | `tajwid` | A madd caused by an incidental sukun in stopping after the letter of madd; shortening, middle length and full length are all permitted in it. |
| [`madd_lazim`](#madd_lazim) | Madd Lazim | المد اللازم | `classification_value` | `tajwid` | A secondary madd caused by an original sukun, fixed in continuing and in stopping, after the letter of madd, in a word or in a letter of the surah openings, whether heavy with idgham or light; its length is 6 counts. |
| [`madd_munfasil`](#madd_munfasil) | Madd Munfasil | المد المنفصل | `classification_value` | `tajwid` | A secondary madd caused by a hamzah at the start of the word following the letter of madd; it is permissible, shortened or lengthened by riwayah and tariq. |
| [`madd_muttasil`](#madd_muttasil) | Madd Muttasil | المد المتصل | `classification_value` | `tajwid` | A secondary madd caused by a hamzah after the letter of madd within one word; it is obligatory for all the readers, and its lengths differ by riwayah and tariq. |
| [`madd_tabii`](#madd_tabii) | Madd Tabee | المد الطبيعي | `classification_value` | `tajwid` | The madd without which the letter of madd itself does not stand, depending on no cause of hamzah or sukun; its length is 2 counts. |
| [`maddah`](#maddah) | Maddah | المدة | `mark` | `dabt` | Marks that the letter is lengthened beyond the natural madd. |
| [`makhraj`](#makhraj) | Makhraj | المخرج | `concept` | `tajwid` | The place a letter issues from and is distinguished by: the oral cavity, the throat, the tongue, the lips or the nasal cavity. |
| [`makki`](#makki) | Makki | مكي | `classification_value` | `revelation` | The part of the Quran revealed before the Hijrah, even where it was revealed outside Makkah. |
| [`manzil`](#manzil) | Manzil | المنزل | `entity` | `divisions` | One of 7 traditional parts of the Quran, made to ease completing it in a week. |
| [`maqasid_al_surah`](#maqasid_al_surah) | Maqasid al-Surah | مقاصد السورة | `content` | `quranic_sciences` | The overarching meanings a surah turns on, held together by its subject, and the single aim its ayahs are ordered around. |
| [`maqta_al_ayah`](#maqta_al_ayah) | Maqta al-Ayah | مقطع الآية | `unit` | `mushaf` | What appears of one ayah on one line of a page of a given mushaf; an ayah that runs over two lines is two maqtas. |
| [`mathani`](#mathani) | Mathani | المثاني | `classification_value` | `surah_classification` | The surahs shorter than the miun, coming after them in the traditional division; called mathani because they are recited more often. |
| [`mawdi_al_sajdah`](#mawdi_al_sajdah) | Mawdi al-Sajdah | موضع السجدة | `concept` | `structure` | The place in the text at which the reader prostrates, ending at a particular ayah. |
| [`meem_sakinah`](#meem_sakinah) | Meem Sakinah | الميم الساكنة | `concept` | `tajwid` | A meem carrying no vowel, fixed in pronunciation and in writing, falling in the middle of a word or at its end. |
| [`miun`](#miun) | Miun | المئون | `classification_value` | `surah_classification` | The surahs whose ayahs come to about 100, a little more or a little less. |
| [`morpheme`](#morpheme) | Morpheme | الوحدة الصرفية | `unit` | `linguistics` | The smallest unit within a word carrying a meaning or a morphological function, such as a prefix, a suffix or a stem. |
| [`morphology`](#morphology) | Morphology | الصرف | `analysis` | `linguistics` | The analysis of a word's structure and form and the morphological properties it carries. |
| [`muallim`](#muallim) | Muallim | معلم | `classification_value` | `recitation_style` | A recitation style meant for teaching, which may repeat ayahs or leave the learner time to repeat after the reciter. |
| [`mufassal`](#mufassal) | Mufassal | المفصل | `classification_value` | `surah_classification` | A group of the short surahs following the mathani; scholars differ over where it begins. |
| [`mufassir`](#mufassir) | Mufassir | المفسر | `role` | `tafsir` | One to whom a tafsir of the Quran is attributed, whether by authorship or by transmission. |
| [`mujawwad`](#mujawwad) | Mujawwad | مجود | `classification_value` | `recitation_style` | A recitation style that is slow and melodic, with the tajwid rules drawn out; the label given to recordings delivered that way. |
| [`muqri`](#muqri) | Muqri | المقرئ | `role` | `qiraat` | One who has received the recitation, mastered it, and transmits it to learners. |
| [`murattal`](#murattal) | Murattal | مرتل | `classification_value` | `recitation_style` | A recitation style that is measured and unadorned, at a reading pace; the label given to recordings delivered that way. |
| [`mushaf`](#mushaf) | Mushaf | المصحف | `entity` | `core` | The Quran as a written, bound book, in its established order. |
| [`mushaf_edition`](#mushaf_edition) | Mushaf Edition | طبعة المصحف | `entity` | `core` | A specific published edition of the mushaf with its own publisher, rasm, dabt, layout and other properties. |
| [`mushaf_mark`](#mushaf_mark) | Mushaf Mark | علامة المصحف | `classification` | `dabt` | A sign or mark that is not one of a word's original letters, used in the mushaf for reading, organisation or guidance. |
| [`mutabaidan`](#mutabaidan) | Mutabaidan | المتباعدان | `classification_value` | `tajwid` | Two letters distant in point of articulation and differing in attribute; no idgham falls between them. |
| [`mutajanisan`](#mutajanisan) | Mutajanisan | المتجانسان | `classification_value` | `tajwid` | Two letters of one point of articulation differing in attribute, like the dal and the taa in «قد تبين». |
| [`mutamathilan`](#mutamathilan) | Mutamathilan | المتماثلان | `classification_value` | `tajwid` | Two letters identical in point of articulation and in attribute, like the two baas in «اضرب بعصاك». |
| [`mutaqariban`](#mutaqariban) | Mutaqariban | المتقاربان | `classification_value` | `tajwid` | Two letters close in point of articulation, in attribute, or in both, like the lam and the raa in «قل رب». |
| [`mutashabihat`](#mutashabihat) | Mutashabihat | المتشابهات | `analysis` | `quranic_sciences` | The places in the Quran where the wording of ayahs, or of parts of them, resembles one another, whether exactly or with a slight difference in a word or in order. |
| [`naskh`](#naskh) | Naskh | النسخ | `concept` | `quranic_sciences` | The lifting of a legal ruling by a later legal proof. |
| [`noon_sakinah`](#noon_sakinah) | Noon Sakinah | النون الساكنة | `concept` | `tajwid` | A noon carrying no vowel, fixed in pronunciation and in writing, in continuing and in stopping. |
| [`nuzul`](#nuzul) | Nuzul | النزول | `concept` | `revelation` | The revelation of the Quran to the Prophet, peace be upon him, in stages over the years of his mission, as events and needs arose. |
| [`omitted_alif`](#omitted_alif) | Omitted Alif | الألف المحذوفة | `mark` | `dabt` | Restores an alif omitted from the Uthmani skeleton but obligatory in pronunciation. |
| [`orthographic_mark`](#orthographic_mark) | Orthographic Mark | العلامة الإملائية | `classification` | `dabt` | A mark fixing how a word is written, such as the hamzah, the maddah and the small letters. |
| [`page`](#page) | Page | الصفحة | `unit` | `mushaf` | A typographic unit of a given mushaf's layout; its content and its boundaries may differ from one mushaf or edition to another. |
| [`part_of_speech`](#part_of_speech) | Part of Speech | قسم الكلمة | `classification` | `linguistics` | The classification of a word or a morpheme by its grammatical class: ism, fil, harf and what branches from them. |
| [`qalqalah`](#qalqalah) | Qalqalah | القلقلة | `classification_value` | `tajwid` | A disturbance in the sound of a vowelless letter as it is pronounced, so that a strong beat is heard, in the letters of «قطب جد»; it grows stronger by the letter's place in the word and by stopping on it. |
| [`qiraah`](#qiraah) | Qiraah | القراءة | `concept` | `qiraat` | One of the ways of reciting the Quran, attributed to one of the imams of the qiraat, from which the riwayahs and tariqs branch. |
| [`qiraah_mark`](#qiraah_mark) | Qiraah Mark | علامة القراءة | `classification` | `dabt` | A mark pointing to a particular manner of delivery at its place, such as saktah, ishmam and tashil. |
| [`quran`](#quran) | Quran | القرآن | `concept` | `core` | The speech of Allah revealed to Muhammad, peace be upon him, whose recitation is worship. |
| [`rasm`](#rasm) | Rasm | الرسم | `classification` | `mushaf` | The way the words of the Quran are written: which letters are written and which omitted or added, and where words are joined or kept apart. |
| [`rasm_imlai`](#rasm_imlai) | Rasm Imlai | الرسم الإملائي | `classification_value` | `mushaf` | Writing the words of the Quran by the rules of modern orthography, writing what the Uthmani rasm omits and omitting what it adds, so that they read in their familiar form. |
| [`rasm_uthmani`](#rasm_uthmani) | Rasm Uthmani | الرسم العثماني | `classification_value` | `mushaf` | The way the words of the Uthmani mushafs are written, with the omission, addition, substitution, separation and joining that go with it. |
| [`rawi`](#rawi) | Rawi | الراوي | `role` | `qiraat` | One to whom a transmission from an imam of a qiraah is attributed. |
| [`recitation`](#recitation) | Recitation | تسجيل التلاوة | `entity` | `recitation` | A published recording of a recitation of the Quran, attributed to a reciter, a riwayah and a style of delivery. |
| [`recitation_pace`](#recitation_pace) | Recitation Pace | مراتب القراءة | `classification` | `recitation_pace` | A classification of how fast a recitation is delivered while its rules are kept. |
| [`recitation_style`](#recitation_style) | Recitation Style | نمط الأداء | `classification` | `recitation_style` | A classification of recordings and recitations by how they are delivered, murattal, mujawwad or muallim, independent of the qiraah and the riwayah. |
| [`reciter`](#reciter) | Reciter | القارئ | `role` | `recitation` | The person who performs a recitation of the Quran. |
| [`rectangular_zero`](#rectangular_zero) | Rectangular Zero | الصفر المستطيل | `mark` | `dabt` | Marks an alif dropped in continuation but pronounced when stopping on it. |
| [`revelation_classification`](#revelation_classification) | Revelation Classification | تصنيف النزول | `classification` | `revelation` | A classification of the Quranic text by whether its revelation fell before or after the Hijrah, in the accepted usage. |
| [`revelation_order`](#revelation_order) | Revelation Order | ترتيب النزول | `property` | `revelation` | The order of the surahs or the ayahs by the time of their revelation, which may differ from one accepted source to another. |
| [`riwayah`](#riwayah) | Riwayah | الرواية | `concept` | `qiraat` | What is attributed to a transmitter from an imam of a qiraah, such as the riwayah of Hafs from Asim. |
| [`root`](#root) | Root | الجذر | `unit` | `linguistics` | The morphological origin a word is referred back to, showing its derivation and its relation to other words. |
| [`rounded_zero`](#rounded_zero) | Rounded Zero | الصفر المستدير | `mark` | `dabt` | Marks a letter present in the skeleton but never pronounced — neither in continuation nor when stopping. |
| [`rubu_al_hizb`](#rubu_al_hizb) | Rubu al-Hizb | ربع الحزب | `entity` | `divisions` | A quarter of a hizb in the well-known division of the mushaf. |
| [`ruku`](#ruku) | Ruku | الركوع | `entity` | `divisions` | A conventional section of the Quran used to organise reading, printed in some mushafs. |
| [`saba_tiwal`](#saba_tiwal) | Saba Tiwal | السبع الطوال | `classification_value` | `surah_classification` | A group of the longest surahs of the Quran, at its beginning, with a known disagreement over which surah is the seventh. |
| [`sabab_al_tasmiyah`](#sabab_al_tasmiyah) | Sabab al-Tasmiyah | سبب التسمية | `content` | `quranic_sciences` | The statement of why a surah was given its name, and what has been transmitted about it by narration or on linguistic grounds. |
| [`sabab_al_waqf`](#sabab_al_waqf) | Sabab al-Waqf | سبب الوقف | `classification` | `waqf` | The division of waqf by what moved the reader to it: necessity, testing, waiting, or choice. |
| [`sajdah_line`](#sajdah_line) | Sajdah Line | خط السجدة | `mark` | `dabt` | Marks the word that makes prostration due. |
| [`sajdah_mark`](#sajdah_mark) | Sajdah Mark | علامة السجدة | `mark` | `dabt` | Marks the point at which the reader prostrates. |
| [`saktah`](#saktah) | Saktah | السكتة | `concept` | `tajwid` | Cutting off the voice for a short moment without breathing, then continuing the recitation. |
| [`saktah_mark`](#saktah_mark) | Saktah Mark | علامة السكتة | `mark` | `dabt` | Marks a saktah: a brief pause without taking a breath, then continuing. |
| [`seen_al_qiraah`](#seen_al_qiraah) | Seen al-Qiraah | سين القراءة | `mark` | `dabt` | A small seen above a saad marks reading it as seen; below it, reading it as saad. |
| [`shaddah`](#shaddah) | Shaddah | الشدة | `mark` | `dabt` | Marks a doubled letter: the first, vowelless, is merged into the second and the two are pronounced as one stressed letter. |
| [`sifat_al_huruf`](#sifat_al_huruf) | Sifat al-Huruf | صفات الحروف | `concept` | `tajwid` | Manners that attend a letter as it is pronounced and distinguish it from a letter sharing its point of articulation; some have an opposite, such as hams and jahr, shiddah and rakhawah, and some have none, such as safir and qalqalah. |
| [`small_meem`](#small_meem) | Small Meem | الميم الصغيرة | `mark` | `dabt` | Marks iqlab: a vowelless noon or tanwin pronounced as meem before baa. |
| [`small_noon`](#small_noon) | Small Noon | النون الصغيرة | `mark` | `dabt` | Restores a noon omitted from the skeleton but obligatory in pronunciation, at one place only (21:88). |
| [`small_waw`](#small_waw) | Small Waw | الواو الصغيرة | `mark` | `dabt` | Marks the silah of the pronoun haa with dammah, pronounced as a waw in continuation. |
| [`small_yaa`](#small_yaa) | Small Yaa | الياء الصغيرة | `mark` | `dabt` | Marks the silah of the pronoun haa with kasrah, pronounced as a yaa in continuation. |
| [`spoken_translation`](#spoken_translation) | Spoken Translation | الترجمة المنطوقة | `content` | `translation` | Rendering the meanings of the Quran into another language in audio or spoken material. |
| [`stem`](#stem) | Stem | الجذع | `unit` | `linguistics` | What remains of a word once its prefixes and suffixes are removed, and what the morphological additions attach to. |
| [`sujud_al_tilawah`](#sujud_al_tilawah) | Sujud al-Tilawah | سجود التلاوة | `concept` | `recitation` | A prostration performed on reciting or hearing one of the places of sujud al-tilawah. |
| [`sukun`](#sukun) | Sukun | السكون | `mark` | `dabt` | Marks a letter that carries no vowel and is articulated clearly. |
| [`surah`](#surah) | Surah | السورة | `entity` | `structure` | A principal unit of the structure of the Quran, made up of ordered ayahs, with a name and a known place in the order of the mushaf. |
| [`surah_group`](#surah_group) | Surah Group | تصنيف السور | `classification` | `surah_classification` | A classification gathering surahs by inherited conventional divisions that rest on length or on their place among the groups of surahs. |
| [`tadabbur`](#tadabbur) | Tadabbur | التدبر | `content` | `quranic_sciences` | Reflecting on the meanings of the Quran and what they call for in action, and what a reader records of a pause at an ayah or a word. |
| [`tadwir`](#tadwir) | Tadwir | التدوير | `classification_value` | `recitation_pace` | Reciting at a middle speed between tahqiq and hadr, while keeping the rules. |
| [`tafkhim`](#tafkhim) | Tafkhim | التفخيم | `concept` | `tajwid` | A fullness entering the sound of a letter so that the mouth fills with its echo; inherent in the letters of istila, and incidental in the raa, the lam of the name of Allah and the alif, following what precedes them. |
| [`tafsir`](#tafsir) | Tafsir | التفسير | `content` | `tafsir` | Stating the meanings of the Quran, explaining its wording, and the rulings and guidance it points to, according to the principles of tafsir. |
| [`tafsir_al_ray`](#tafsir_al_ray) | Tafsir al-Ray | تفسير الرأي | `content` | `tafsir` | Explaining the meanings of the Quran by reasoning and reflection, after knowledge of the speech of the Arabs, its styles and the principles of tafsir, whether the reasoning is approved or censured. |
| [`tafsir_mathur`](#tafsir_mathur) | Tafsir Mathur | التفسير المأثور | `content` | `tafsir` | Tafsir transmitted with a chain of narration: explanation of the Quran drawn from the Quran itself, from the Sunnah, or from the sayings of the Companions and Successors. |
| [`tahqiq`](#tahqiq) | Tahqiq | التحقيق | `classification_value` | `recitation_pace` | Reciting slowly and deliberately, giving the letters and their rules their full due; much used in teaching. |
| [`tajwid`](#tajwid) | Tajweed | التجويد | `concept` | `tajwid` | The discipline of delivering the letters of the Quran from their points of articulation and giving them their due properties and rulings. |
| [`takbir`](#takbir) | Takbir | التكبير | `concept` | `recitation` | Saying «الله أكبر» between the surahs from the end of al-Duha to the end of al-Nas, transmitted from the people of Makkah in the riwayah of al-Bazzi from Ibn Kathir, and done at a khatmah in other riwayahs. |
| [`tanwin`](#tanwin) | Tanwin | التنوين | `classification` | `dabt` | An added vowelless noon at the end of a noun, written by doubling the shape of the vowel. |
| [`tanwin_al_damm`](#tanwin_al_damm) | Tanwin al-Damm | تنوين الضم | `mark` | `dabt` | Marks the un tanwin. |
| [`tanwin_al_fath`](#tanwin_al_fath) | Tanwin al-Fath | تنوين الفتح | `mark` | `dabt` | Marks the an tanwin. |
| [`tanwin_al_kasr`](#tanwin_al_kasr) | Tanwin al-Kasr | تنوين الكسر | `mark` | `dabt` | Marks the in tanwin. |
| [`tariq`](#tariq) | Tariq | الطريق | `concept` | `qiraat` | A path of transmission taken from a rawi through those below him in the chain of transmission of a qiraah. |
| [`tarqiq`](#tarqiq) | Tarqiq | الترقيق | `concept` | `tajwid` | A thinness entering the sound of a letter so that the mouth does not fill with its echo; inherent in the letters of istifal, and incidental in the raa and the lam of the name of Allah. |
| [`tartib_al_mushaf`](#tartib_al_mushaf) | Tartib al-Mushaf | ترتيب المصحف | `property` | `structure` | The order of the surahs as settled in the Uthmani mushaf, from al-Fatihah to al-Nas; it is the order the surahs are numbered by. |
| [`tartil`](#tartil) | Tartil | الترتيل | `concept` | `recitation` | Reciting the Quran deliberately, making the letters and words distinct, observing the stops and the meaning. |
| [`tashil`](#tashil) | Tashil | التسهيل | `mark` | `dabt` | Marks tashil: the hamzah softened to a sound between a hamzah and an alif. |
| [`tashkil`](#tashkil) | Tashkil | التشكيل | `concept` | `dabt` | The layer of dabt marks attached to the letters of the text, the harakat, tanwin, shaddah, sukun and what goes with them, taken as a whole. |
| [`three_dots`](#three_dots) | Three Dots | الثلاث نقط | `mark` | `dabt` | Three dots above the letter, distinguishing it from the others that share its skeleton (ijam): thaa, sheen. |
| [`thumn`](#thumn) | Thumn | الثمن | `entity` | `divisions` | An eighth of a hizb, a division used in some mushafs and schools. |
| [`tilawah`](#tilawah) | Tilawah | التلاوة | `concept` | `recitation` | Reading the Quran in its wording, delivered aloud as the reader received it, whether in prayer, in a lesson or in a recording. |
| [`token`](#token) | Token |  | `unit` | `text` | A unit produced by segmenting the text according to a declared method. |
| [`translation`](#translation) | Translation | الترجمة | `content` | `translation` | Rendering the meanings of the Quran into another language. |
| [`translator`](#translator) | Translator | المترجم | `role` | `translation` | One to whom a translation of the meanings of the Quran into another language is attributed, whether a person or a body. |
| [`transliteration`](#transliteration) | Transliteration | النقل الحرفي | `content` | `translation` | Representing the letters of one writing system with those of another by fixed rules, without translating the meaning. |
| [`two_dots`](#two_dots) | Two Dots | النقطتان | `mark` | `dabt` | Two dots, above or below, distinguishing a letter from the others that share its skeleton (ijam): taa, yaa, qaaf. |
| [`usul`](#usul) | Usul | الأصول | `concept` | `qiraat` | The general rules of a reading that apply to everything meeting their condition, such as madd, hamzah, imalah, idgham and the pronoun haa. |
| [`wajh`](#wajh) | Wajh | الوجه | `concept` | `qiraat` | One of several manners of delivery, any of which may be taken within one riwayah or one tariq, such as the wajhs of madd arid li al-sukun. |
| [`waqf`](#waqf) | Waqf | الوقف | `concept` | `waqf` | Stopping the recitation at a place in the text according to the rules of stopping and starting. |
| [`waqf_al_muanaqah`](#waqf_al_muanaqah) | Waqf al-Muanaqah | وقف المعانقة | `classification_value` | `dabt` | Two candidate stopping points: stopping at one makes stopping at the other not allowed. |
| [`waqf_hasan`](#waqf_hasan) | Waqf Hasan | الوقف الحسن | `classification_value` | `waqf` | A stop that yields a meaning but is connected to what follows it in wording and in meaning. |
| [`waqf_idtirari`](#waqf_idtirari) | Waqf Idtirari | الوقف الاضطراري | `classification_value` | `waqf` | A stop forced on the reader by something that compels it, such as shortness of breath, a sneeze or forgetting; the reader stops on any word and then begins again where beginning is sound. |
| [`waqf_ikhtibari`](#waqf_ikhtibari) | Waqf Ikhtibari | الوقف الاختباري | `classification_value` | `waqf` | A stop made to show what is cut and what is joined, what is written and what is omitted in the rasm, at a question or in teaching. |
| [`waqf_ikhtiyari`](#waqf_ikhtiyari) | Waqf Ikhtiyari | الوقف الاختياري | `classification_value` | `waqf` | A stop the reader makes by choice with no cause arising; it is the one the rulings of tamm, kafi, hasan and qabih apply to. |
| [`waqf_intizari`](#waqf_intizari) | Waqf Intizari | الوقف الانتظاري | `classification_value` | `waqf` | A stop made on a word the qiraat differ on, so that the reader covers its wajhs when gathering the readings. |
| [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn) | Waqf Jaiz Mustawi al-Tarafayn | الوقف الجائز مستوي الطرفين | `classification_value` | `dabt` | A permissible stop, with stopping and continuing equally sound. |
| [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla) | Waqf Jaiz Waqf Awla | الوقف الجائز مع كون الوقف أولى | `classification_value` | `dabt` | A permissible stop, and stopping is the better choice. |
| [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla) | Waqf Jaiz Wasl Awla | الوقف الجائز مع كون الوصل أولى | `classification_value` | `dabt` | A permissible stop, but continuing is the better choice. |
| [`waqf_kafi`](#waqf_kafi) | Waqf Kafi | الوقف الكافي | `classification_value` | `waqf` | A stop whose meaning is complete but which is connected to what follows it in meaning, not in wording. |
| [`waqf_lazim`](#waqf_lazim) | Waqf Lazim | الوقف اللازم | `classification_value` | `dabt` | A compulsory stop: continuing across it would suggest a meaning other than the one intended. |
| [`waqf_mamnu`](#waqf_mamnu) | Waqf Mamnu | الوقف الممنوع | `classification_value` | `dabt` | A forbidden stop: stopping here would break the meaning or attach what follows to the wrong clause. |
| [`waqf_mark`](#waqf_mark) | Waqf Mark | علامة الوقف | `mark` | `dabt` | A mark in the mushaf pointing the reader to the ruling on stopping or continuing at a given place. |
| [`waqf_mark_type`](#waqf_mark_type) | Waqf Mark Type | نوع علامة الوقف | `classification` | `waqf` | A classification of what a waqf mark drawn in the mushaf points to: that stopping is compulsory, forbidden or permitted. |
| [`waqf_qabih`](#waqf_qabih) | Waqf Qabih | الوقف القبيح | `classification_value` | `waqf` | A stop that yields no meaning, or yields a meaning that is not the one intended. |
| [`waqf_ruling`](#waqf_ruling) | Waqf Ruling | حكم الوقف | `classification` | `waqf` | A classification of the place itself by whether the meaning is complete there, not of the mark drawn at it. |
| [`waqf_tamm`](#waqf_tamm) | Waqf Tamm | الوقف التام | `classification_value` | `waqf` | A stop whose meaning is complete and which is connected to what follows it neither in wording nor in meaning. |
| [`wazn`](#wazn) | Wazn | الوزن | `unit` | `linguistics` | The morphological form of a word represented by the letters of «فعل» with whatever affixes attach to them, showing its structure regardless of its root. |
| [`word`](#word) | Word | الكلمة | `unit` | `text` | A unit of the text that a reader recognises as one word, independent of how a segmenter splits the text. |
| [`word_by_word_translation`](#word_by_word_translation) | Word by Word Translation |  | `content` | `translation` | A translation giving each word of the ayah its meaning in another language on its own, in the order of the original words. |
| [`word_key`](#word_key) | Word Key |  | `property` | `structure` | A textual identifier of a word that adds the word's position within the ayah to the ayah key, in the form `2:255:5`; the position is counted from the start of the ayah by a declared segmentation method. |
| [`word_timing`](#word_timing) | Word Timing |  | `concept` | `recitation` | A span of time in a recitation recording, given by a start and an end, corresponding to one word of an ayah. |

## By category

- **Core** — `core`: [`mushaf`](#mushaf), [`mushaf_edition`](#mushaf_edition), [`quran`](#quran)
- **Structure** — `structure`: [`ayah`](#ayah), [`ayah_key`](#ayah_key), [`basmalah`](#basmalah), [`fasilah`](#fasilah), [`harf_muqatta`](#harf_muqatta), [`huruf_muqattaah`](#huruf_muqattaah), [`mawdi_al_sajdah`](#mawdi_al_sajdah), [`surah`](#surah), [`tartib_al_mushaf`](#tartib_al_mushaf), [`word_key`](#word_key)
- **Text** — `text`: [`character`](#character), [`codepoint`](#codepoint), [`glyph`](#glyph), [`grapheme`](#grapheme), [`letter`](#letter), [`token`](#token), [`word`](#word)
- **Quran divisions** — `divisions`: [`hizb`](#hizb), [`juz`](#juz), [`manzil`](#manzil), [`rubu_al_hizb`](#rubu_al_hizb), [`ruku`](#ruku), [`thumn`](#thumn)
- **Surah classification** — `surah_classification`: [`mathani`](#mathani), [`miun`](#miun), [`mufassal`](#mufassal), [`saba_tiwal`](#saba_tiwal), [`surah_group`](#surah_group)
- **Mushaf and layout** — `mushaf`: [`font`](#font), [`layout`](#layout), [`line`](#line), [`maqta_al_ayah`](#maqta_al_ayah), [`page`](#page), [`rasm`](#rasm), [`rasm_imlai`](#rasm_imlai), [`rasm_uthmani`](#rasm_uthmani)
- **Dabt and Mushaf marks** — `dabt`: [`ayah_mark`](#ayah_mark), [`dammah`](#dammah), [`division_mark`](#division_mark), [`dot`](#dot), [`fathah`](#fathah), [`hamzah`](#hamzah), [`hamzat_al_wasl`](#hamzat_al_wasl), [`harakah`](#harakah), [`ijam`](#ijam), [`imalah`](#imalah), [`ishmam`](#ishmam), [`kasrah`](#kasrah), [`maddah`](#maddah), [`mushaf_mark`](#mushaf_mark), [`omitted_alif`](#omitted_alif), [`orthographic_mark`](#orthographic_mark), [`qiraah_mark`](#qiraah_mark), [`rectangular_zero`](#rectangular_zero), [`rounded_zero`](#rounded_zero), [`sajdah_line`](#sajdah_line), [`sajdah_mark`](#sajdah_mark), [`saktah_mark`](#saktah_mark), [`seen_al_qiraah`](#seen_al_qiraah), [`shaddah`](#shaddah), [`small_meem`](#small_meem), [`small_noon`](#small_noon), [`small_waw`](#small_waw), [`small_yaa`](#small_yaa), [`sukun`](#sukun), [`tanwin`](#tanwin), [`tanwin_al_damm`](#tanwin_al_damm), [`tanwin_al_fath`](#tanwin_al_fath), [`tanwin_al_kasr`](#tanwin_al_kasr), [`tashil`](#tashil), [`tashkil`](#tashkil), [`three_dots`](#three_dots), [`two_dots`](#two_dots), [`waqf_al_muanaqah`](#waqf_al_muanaqah), [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn), [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla), [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla), [`waqf_lazim`](#waqf_lazim), [`waqf_mamnu`](#waqf_mamnu), [`waqf_mark`](#waqf_mark)
- **Ayah numbering** — `ayah_numbering`: [`ayah_count`](#ayah_count), [`ayah_numbering_basri`](#ayah_numbering_basri), [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi), [`ayah_numbering_kufi`](#ayah_numbering_kufi), [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir), [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal), [`ayah_numbering_makki`](#ayah_numbering_makki), [`ayah_numbering_system`](#ayah_numbering_system), [`equivalent_ayah`](#equivalent_ayah)
- **Revelation** — `revelation`: [`asbab_al_nuzul`](#asbab_al_nuzul), [`disputed`](#disputed), [`madani`](#madani), [`makki`](#makki), [`nuzul`](#nuzul), [`revelation_classification`](#revelation_classification), [`revelation_order`](#revelation_order)
- **Qiraat** — `qiraat`: [`farsh`](#farsh), [`muqri`](#muqri), [`qiraah`](#qiraah), [`rawi`](#rawi), [`riwayah`](#riwayah), [`tariq`](#tariq), [`usul`](#usul), [`wajh`](#wajh)
- **Recitation** — `recitation`: [`ayah_timing`](#ayah_timing), [`hifz`](#hifz), [`istiadhah`](#istiadhah), [`khatmah`](#khatmah), [`recitation`](#recitation), [`reciter`](#reciter), [`sujud_al_tilawah`](#sujud_al_tilawah), [`takbir`](#takbir), [`tartil`](#tartil), [`tilawah`](#tilawah), [`word_timing`](#word_timing)
- **Recitation pace** — `recitation_pace`: [`hadr`](#hadr), [`recitation_pace`](#recitation_pace), [`tadwir`](#tadwir), [`tahqiq`](#tahqiq)
- **Recitation style** — `recitation_style`: [`instructional_ayah_repetition`](#instructional_ayah_repetition), [`muallim`](#muallim), [`mujawwad`](#mujawwad), [`murattal`](#murattal), [`recitation_style`](#recitation_style)
- **Tajwid** — `tajwid`: [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`ghunnah`](#ghunnah), [`hukm_al_tajwid`](#hukm_al_tajwid), [`idgham`](#idgham), [`ikhfa`](#ikhfa), [`iqlab`](#iqlab), [`izhar`](#izhar), [`lahn`](#lahn), [`lahn_jali`](#lahn_jali), [`lahn_khafi`](#lahn_khafi), [`madd`](#madd), [`madd_al_badal`](#madd_al_badal), [`madd_al_iwad`](#madd_al_iwad), [`madd_al_lin`](#madd_al_lin), [`madd_al_silah`](#madd_al_silah), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`madd_lazim`](#madd_lazim), [`madd_munfasil`](#madd_munfasil), [`madd_muttasil`](#madd_muttasil), [`madd_tabii`](#madd_tabii), [`makhraj`](#makhraj), [`meem_sakinah`](#meem_sakinah), [`mutabaidan`](#mutabaidan), [`mutajanisan`](#mutajanisan), [`mutamathilan`](#mutamathilan), [`mutaqariban`](#mutaqariban), [`noon_sakinah`](#noon_sakinah), [`qalqalah`](#qalqalah), [`saktah`](#saktah), [`sifat_al_huruf`](#sifat_al_huruf), [`tafkhim`](#tafkhim), [`tajwid`](#tajwid), [`tarqiq`](#tarqiq)
- **Waqf** — `waqf`: [`sabab_al_waqf`](#sabab_al_waqf), [`waqf`](#waqf), [`waqf_hasan`](#waqf_hasan), [`waqf_idtirari`](#waqf_idtirari), [`waqf_ikhtibari`](#waqf_ikhtibari), [`waqf_ikhtiyari`](#waqf_ikhtiyari), [`waqf_intizari`](#waqf_intizari), [`waqf_kafi`](#waqf_kafi), [`waqf_mark_type`](#waqf_mark_type), [`waqf_qabih`](#waqf_qabih), [`waqf_ruling`](#waqf_ruling), [`waqf_tamm`](#waqf_tamm)
- **Linguistics** — `linguistics`: [`fil`](#fil), [`harf_al_mana`](#harf_al_mana), [`irab`](#irab), [`ism`](#ism), [`lemma`](#lemma), [`morpheme`](#morpheme), [`morphology`](#morphology), [`part_of_speech`](#part_of_speech), [`root`](#root), [`stem`](#stem), [`wazn`](#wazn)
- **Translation** — `translation`: [`spoken_translation`](#spoken_translation), [`translation`](#translation), [`translator`](#translator), [`transliteration`](#transliteration), [`word_by_word_translation`](#word_by_word_translation)
- **Tafsir** — `tafsir`: [`mufassir`](#mufassir), [`tafsir`](#tafsir), [`tafsir_al_ray`](#tafsir_al_ray), [`tafsir_mathur`](#tafsir_mathur)
- **Quranic sciences** — `quranic_sciences`: [`asma_al_surah`](#asma_al_surah), [`fadail_al_quran`](#fadail_al_quran), [`gharib_al_quran`](#gharib_al_quran), [`maqasid_al_surah`](#maqasid_al_surah), [`mutashabihat`](#mutashabihat), [`naskh`](#naskh), [`sabab_al_tasmiyah`](#sabab_al_tasmiyah), [`tadabbur`](#tadabbur)

## Core — `core`

<a id="mushaf"></a>

### Mushaf — المصحف

<!-- source: standards/terminology/concepts/mushaf.yml -->

| field | value |
| --- | --- |
| `code` | `mushaf` |
| `plural` | `mushafs` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المُصْحَف |
| Other spellings | `mus'haf`, `muṣḥaf`, `moshaf` |
| English gloss | `Quran Codex` |

**Definition:** The Quran as a written, bound book, in its established order.

**Purpose:** Used when the properties of the written representation matter: rasm, layout, pages, lines and marks.

- A mushaf is a written vessel for the Quran, not the Quran itself: mushafs differ in rasm, pages and marks while the Quran is one.

**Related:** [`quran`](#quran), [`mushaf_edition`](#mushaf_edition), [`rasm`](#rasm), [`layout`](#layout), [`page`](#page), [`rasm_uthmani`](#rasm_uthmani)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/119`

<a id="mushaf_edition"></a>

### Mushaf Edition — طبعة المصحف

<!-- source: standards/terminology/concepts/mushaf_edition.yml -->

| field | value |
| --- | --- |
| `code` | `mushaf_edition` |
| `plural` | `mushaf_editions` |
| `kind` | `entity` |
| Part of | [`mushaf`](#mushaf) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | طَبْعَة المُصْحَف |

**Definition:** A specific published edition of the mushaf with its own publisher, rasm, dabt, layout and other properties.

**Purpose:** Used to tell apart editions that may differ in pages, lines, marks or typographic properties.

**Related:** [`mushaf`](#mushaf), [`layout`](#layout), [`page`](#page), [`riwayah`](#riwayah), [`font`](#font), [`rasm`](#rasm), [`ruku`](#ruku)

<a id="quran"></a>

### Quran — القرآن

<!-- source: standards/terminology/concepts/quran.yml -->

| field | value |
| --- | --- |
| `code` | `quran` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | القُرْآن |
| Other spellings | `koran`, `qur'an`, `qur’an`, `quraan`, `al_quran` |

**Definition:** The speech of Allah revealed to Muhammad, peace be upon him, whose recitation is worship. The name covers the whole and, by context, any part of it.

**Purpose:** Represents the Quranic content itself, independent of any particular mushaf, layout, formatting or digital representation.

- The Quran is the speech itself; the mushaf is its written vessel. Pages, rasm and marks belong to the mushaf, not to the Quran.

**Related:** [`mushaf`](#mushaf), [`surah`](#surah), [`ayah`](#ayah), [`fadail_al_quran`](#fadail_al_quran)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/15`

## Structure — `structure`

<a id="ayah"></a>

### Ayah — الآية

<!-- source: standards/terminology/concepts/ayah.yml -->

| field | value |
| --- | --- |
| `code` | `ayah` |
| `plural` | `ayahs` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الآيَة |
| Arabic plural | آيات |
| Transliteration | āyah |
| Other spellings | `aya`, `ayat`, `ayaat` |
| English gloss | `Verse` |

**Definition:** A unit of the Quranic text falling within a surah and having determined boundaries. Its number, and some of its boundaries, may differ from one ayah numbering system to another.

**Purpose:** Used as the basic unit for referring to the Quranic text, and for attaching translations, tafsir, recitations, analyses and other data to a specific place in the Quran.

- Its position on a page or a line belongs to the mushaf and its layout, not to the identity of the ayah.
- The fasilah is the ayah's ending, not the ayah.

**Related:** [`surah`](#surah), [`ayah_numbering_system`](#ayah_numbering_system), [`fasilah`](#fasilah), [`ayah_mark`](#ayah_mark), [`ayah_key`](#ayah_key), [`word`](#word), [`asbab_al_nuzul`](#asbab_al_nuzul), [`ayah_count`](#ayah_count), [`ayah_numbering_basri`](#ayah_numbering_basri), [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi), [`ayah_numbering_kufi`](#ayah_numbering_kufi), [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir), [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal), [`ayah_numbering_makki`](#ayah_numbering_makki), [`ayah_timing`](#ayah_timing), [`equivalent_ayah`](#equivalent_ayah), [`fadail_al_quran`](#fadail_al_quran), [`gharib_al_quran`](#gharib_al_quran), [`maqta_al_ayah`](#maqta_al_ayah), [`mawdi_al_sajdah`](#mawdi_al_sajdah), [`mutashabihat`](#mutashabihat), [`naskh`](#naskh), [`quran`](#quran), [`tadabbur`](#tadabbur), [`tafsir`](#tafsir), [`tafsir_mathur`](#tafsir_mathur)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`

<a id="ayah_key"></a>

### Ayah Key

<!-- source: standards/terminology/concepts/ayah_key.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_key` |
| `plural` | `ayah_keys` |
| `kind` | `property` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Other spellings | `ayah_ref`, `ayah_reference`, `aya_key` |
| English gloss | `verse key` |

**Definition:** A textual identifier of an ayah joining its surah number and its number within it with a colon, in the form `2:255`; it is read only in the light of the ayah numbering system it rests on.

**Purpose:** Used as the key that joins data sources and carries a reference to an ayah between APIs and files; binding it to a numbering system stops one key from pointing at two places.

- The key is a reference, not an identity: changing the numbering system changes the key and not the ayah.
- The key is not the running number of the ayah across the whole mushaf.

**Related:** [`ayah`](#ayah), [`surah`](#surah), [`ayah_numbering_system`](#ayah_numbering_system), [`word_key`](#word_key), [`tartib_al_mushaf`](#tartib_al_mushaf)

<a id="basmalah"></a>

### Basmalah — البسملة

<!-- source: standards/terminology/concepts/basmalah.yml -->

| field | value |
| --- | --- |
| `code` | `basmalah` |
| `plural` | `basmalahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | البَسْمَلَة |
| Other spellings | `basmala`, `bismillah` |

**Definition:** The formula «بسم الله الرحمن الرحيم» with which the surahs open, except surah al-Tawbah. It carries rulings and differences bound up with ayah counting.

**Purpose:** Used to identify the basmalah and to represent its position and its relation to the surah and to the ayah numbering system.

**Related:** [`surah`](#surah), [`ayah_numbering_system`](#ayah_numbering_system), [`istiadhah`](#istiadhah), [`takbir`](#takbir)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/30) — `30`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/145`

<a id="fasilah"></a>

### Fasilah — الفاصلة

<!-- source: standards/terminology/concepts/fasilah.yml -->

| field | value |
| --- | --- |
| `code` | `fasilah` |
| `plural` | `fasilahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الفَاصِلَة |
| Other spellings | `fasila` |
| English gloss | `Verse Ending` |

**Definition:** The close of an ayah or a passage as a matter of its composition; some scholars define it as the ayah's last word.

**Purpose:** Used in studies and datasets concerned with ayah endings and Quranic composition. It is never used as a synonym for `ayah`.

- The fasilah is the ayah's ending as a matter of the text; the ayah mark is the sign drawn in the mushaf for it.

**Related:** [`ayah`](#ayah), [`ayah_mark`](#ayah_mark)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/153`

<a id="harf_muqatta"></a>

### Harf Muqatta — الحرف المقطع

<!-- source: standards/terminology/concepts/harf_muqatta.yml -->

| field | value |
| --- | --- |
| `code` | `harf_muqatta` |
| `plural` | `harf_muqattas` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحَرْف المُقَطَّع |
| English gloss | `Disjointed Letters`, `Separated Letters` |

**Definition:** Alphabetic letters that open certain surahs, such as Alif Laam Meem, Alif Laam Raa, Haa Meem and Kaaf Haa Yaa Ayn Saad.

**Purpose:** Used to identify these openings, keep them distinct, and tie them to their surahs and their positions in the text.

**Related:** [`surah`](#surah), [`huruf_muqattaah`](#huruf_muqattaah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/113) — `113`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/361`

<a id="huruf_muqattaah"></a>

### Huruf Muqattaah — الحروف المقطعة

<!-- source: standards/terminology/concepts/huruf_muqattaah.yml -->

| field | value |
| --- | --- |
| `code` | `huruf_muqattaah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحُرُوف المُقَطَّعَة |
| Other spellings | `muqattaat`, `al_muqattaat`, `huruf_muqattaat`, `huroof_muqattaat`, `fawatih_al_suwar` |
| English gloss | `disjointed letters`, `mysterious letters` |

**Definition:** The group of alphabetic letters that open 29 surahs, read by the names of the letters and not by their sounds, such as «الم» and «كهيعص».

**Purpose:** Used to tag the surah openings that are read by the names of their letters, so that recitation, madd, search and translation treat them in their own way.

- A single letter is a `harf_muqatta`; this is the opening as a group.
- The opening is an ayah or part of one depending on the numbering system, and is not the name of the surah.

**Related:** [`harf_muqatta`](#harf_muqatta), [`madd_lazim`](#madd_lazim), [`surah`](#surah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/113) — `113`

<a id="mawdi_al_sajdah"></a>

### Mawdi al-Sajdah — موضع السجدة

<!-- source: standards/terminology/concepts/mawdi_al_sajdah.yml -->

| field | value |
| --- | --- |
| `code` | `mawdi_al_sajdah` |
| `plural` | `mawdi_al_sajdahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَوْضِع السَّجْدَة |
| Registry | [`sajdah`](/guidelines/en/03-terminology/registries/#sajdah) |
| Other spellings | `sajdah`, `sajda`, `sajdah_place` |
| English gloss | `Prostration` |

**Definition:** The place in the text at which the reader prostrates, ending at a particular ayah. The places are countable, and some of them are disputed.

**Purpose:** Used to tie a sajdah to its place in the surah, the ayah and the page, and to keep the place apart from the mark drawn at it and from the prostration itself.

- The place is a location in the text, the sajdah mark is a sign drawn for it, and sujud al-tilawah is the act.

**Related:** [`sajdah_mark`](#sajdah_mark), [`sujud_al_tilawah`](#sujud_al_tilawah), [`ayah`](#ayah), [`sajdah_line`](#sajdah_line)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="surah"></a>

### Surah — السورة

<!-- source: standards/terminology/concepts/surah.yml -->

| field | value |
| --- | --- |
| `code` | `surah` |
| `plural` | `surahs` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | السُّورَة |
| Registry | [`surahs`](/guidelines/en/03-terminology/registries/#surahs) |
| Other spellings | `sura`, `surat`, `soorah`, `suwar` |
| English gloss | `Chapter` |

**Definition:** A principal unit of the structure of the Quran, made up of ordered ayahs, with a name and a known place in the order of the mushaf.

**Purpose:** Used as the principal unit for organising the text and for attaching ayahs and surah-level data.

**Related:** [`ayah`](#ayah), [`asma_al_surah`](#asma_al_surah), [`surah_group`](#surah_group), [`revelation_classification`](#revelation_classification), [`basmalah`](#basmalah), [`ayah_count`](#ayah_count), [`ayah_key`](#ayah_key), [`fadail_al_quran`](#fadail_al_quran), [`harf_muqatta`](#harf_muqatta), [`huruf_muqattaah`](#huruf_muqattaah), [`maqasid_al_surah`](#maqasid_al_surah), [`mathani`](#mathani), [`miun`](#miun), [`mufassal`](#mufassal), [`quran`](#quran), [`revelation_order`](#revelation_order), [`saba_tiwal`](#saba_tiwal), [`sabab_al_tasmiyah`](#sabab_al_tasmiyah), [`tartib_al_mushaf`](#tartib_al_mushaf)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="tartib_al_mushaf"></a>

### Tartib al-Mushaf — ترتيب المصحف

<!-- source: standards/terminology/concepts/tartib_al_mushaf.yml -->

| field | value |
| --- | --- |
| `code` | `tartib_al_mushaf` |
| `kind` | `property` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَرْتِيب المُصْحَف |
| Other spellings | `surah_order`, `uthmani_order`, `tartib_al_suwar` |
| English gloss | `Mushaf order` |

**Definition:** The order of the surahs as settled in the Uthmani mushaf, from al-Fatihah to al-Nas; it is the order the surahs are numbered by.

**Purpose:** Used as the default order of surahs in display and navigation; a surah's number in it is its number in the key, and it is named where the revelation order stands opposite it.

- The mushaf order is not the revelation order: a surah has one number in the mushaf, and its rank in revelation may differ by source.

**Related:** [`revelation_order`](#revelation_order), [`surah`](#surah), [`ayah_key`](#ayah_key)

<a id="word_key"></a>

### Word Key

<!-- source: standards/terminology/concepts/word_key.yml -->

| field | value |
| --- | --- |
| `code` | `word_key` |
| `plural` | `word_keys` |
| `kind` | `property` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Other spellings | `wid`, `data_wid`, `word_ref`, `word_position_key` |

**Definition:** A textual identifier of a word that adds the word's position within the ayah to the ayah key, in the form `2:255:5`; the position is counted from the start of the ayah by a declared segmentation method.

**Purpose:** Used as the key for data attached to the word: timing, word-by-word translation, morphological analysis and images.

- The position in the key is the word's, not the token's; changing the segmentation method that counts the words changes the key.

**Related:** [`ayah_key`](#ayah_key), [`word`](#word), [`word_timing`](#word_timing), [`word_by_word_translation`](#word_by_word_translation)

**Sources:**

- مصحف حفص — كلمة كلمة — `word_attributes!data-wid`

## Text — `text`

<a id="character"></a>

### Character

<!-- source: standards/terminology/concepts/character.yml -->

| field | value |
| --- | --- |
| `code` | `character` |
| `plural` | `characters` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** An abstract unit of text in a digital encoding; it need not correspond to a single linguistic letter.

**Purpose:** Used where an offset, a length or a comparison must be exact: text-path tests, search indexes and the allowlist of permitted characters.

- A character is a unit of encoding; a letter is a linguistic unit, and one letter may be carried by more than one character.
- A character is not a glyph: the glyph is produced by the font, the character is carried by the text.

**Related:** [`letter`](#letter), [`glyph`](#glyph), [`codepoint`](#codepoint), [`grapheme`](#grapheme)

<a id="codepoint"></a>

### Codepoint

<!-- source: standards/terminology/concepts/codepoint.yml -->

| field | value |
| --- | --- |
| `code` | `codepoint` |
| `plural` | `codepoints` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** A numeric value defined by an encoding standard such as Unicode.

**Purpose:** Used where the exact encoding of a character or mark matters: normalisation rules, font mappings and the allowlist of permitted codepoints.

**Related:** [`character`](#character), [`grapheme`](#grapheme)

<a id="glyph"></a>

### Glyph

<!-- source: standards/terminology/concepts/glyph.yml -->

| field | value |
| --- | --- |
| `code` | `glyph` |
| `plural` | `glyphs` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** The visual shape a font produces to represent a letter, a character, or a group of them.

**Purpose:** Used for fonts, rasm, rendering and the placement of visual shapes.

- A glyph is produced by the font; it is neither the letter nor the character, and one character may be drawn by many glyphs.

**Related:** [`character`](#character), [`letter`](#letter), [`font`](#font)

<a id="grapheme"></a>

### Grapheme

<!-- source: standards/terminology/concepts/grapheme.yml -->

| field | value |
| --- | --- |
| `code` | `grapheme` |
| `plural` | `graphemes` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** A written unit that a user perceives as one unit, which may consist of more than one `codepoint`.

**Purpose:** Used for visual segmentation, editing and text selection, where the codepoint is not the right unit.

**Related:** [`codepoint`](#codepoint), [`character`](#character)

<a id="letter"></a>

### Letter — الحرف

<!-- source: standards/terminology/concepts/letter.yml -->

| field | value |
| --- | --- |
| `code` | `letter` |
| `plural` | `letters` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحَرْف |
| Other spellings | `harf` |

**Definition:** A letter of the alphabet as a linguistic unit of writing.

**Purpose:** Used for data that deals with linguistic letters, without confusing them with their digital or visual representations.

- A letter is a linguistic unit; a character is a unit of encoding, and one letter may be written with one character or more.
- A letter is a unit of writing; harf al-mana is a part of speech.

**Related:** [`character`](#character), [`glyph`](#glyph), [`harf_al_mana`](#harf_al_mana), [`ijam`](#ijam), [`makhraj`](#makhraj), [`word`](#word)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/5) — `5`

<a id="token"></a>

### Token

<!-- source: standards/terminology/concepts/token.yml -->

| field | value |
| --- | --- |
| `code` | `token` |
| `plural` | `tokens` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** A unit produced by segmenting the text according to a declared method. It may equal a word, be part of one, or span more than one.

**Purpose:** Used to tie automated analysis to the text where the word boundary is not the segmentation boundary, and to keep what a segmenter produces distinct from what a reader counts as a word.

- A word is a unit the reader recognises; a token is a unit a segmentation method produces, so changing the method changes the number of tokens and not the number of words.

**Related:** [`word`](#word), [`morpheme`](#morpheme)

<a id="word"></a>

### Word — الكلمة

<!-- source: standards/terminology/concepts/word.yml -->

| field | value |
| --- | --- |
| `code` | `word` |
| `plural` | `words` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الكَلِمَة |
| Other spellings | `kalimah` |

**Definition:** A unit of the text that a reader recognises as one word, independent of how a segmenter splits the text.

**Purpose:** Used to attach word-level data: root, morphology, irab, tajwid, audio alignment and visual position.

- A word is a unit the reader recognises; a token is a unit a segmentation method produces, so changing the method changes the number of tokens and not the number of words.

**Related:** [`token`](#token), [`morpheme`](#morpheme), [`letter`](#letter), [`word_key`](#word_key), [`ayah`](#ayah), [`gharib_al_quran`](#gharib_al_quran), [`irab`](#irab), [`mutashabihat`](#mutashabihat), [`word_by_word_translation`](#word_by_word_translation), [`word_timing`](#word_timing)

## Quran divisions — `divisions`

<a id="hizb"></a>

### Hizb — الحزب

<!-- source: standards/terminology/concepts/hizb.yml -->

| field | value |
| --- | --- |
| `code` | `hizb` |
| `plural` | `hizbs` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحِزْب |
| Other spellings | `hezb` |

**Definition:** In the current division, half a juz, so that the Quran is 60 hizbs.

**Purpose:** Used to represent the conventional divisions, navigation, and reading plans.

**Related:** [`juz`](#juz), [`rubu_al_hizb`](#rubu_al_hizb), [`thumn`](#thumn), [`division_mark`](#division_mark)

<a id="juz"></a>

### Juz — الجزء

<!-- source: standards/terminology/concepts/juz.yml -->

| field | value |
| --- | --- |
| `code` | `juz` |
| `plural` | `juzs` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الجُزْء |
| Other spellings | `juzu`, `juz'`, `juzz`, `para` |
| English gloss | `Part` |

**Definition:** One of the 30 parts of the well-known division of the mushaf, made to ease reading and completing it.

**Purpose:** Used for navigation, for organising reading, and for the schedules and plans built on the parts of the Quran.

**Related:** [`hizb`](#hizb), [`manzil`](#manzil), [`khatmah`](#khatmah), [`division_mark`](#division_mark), [`ruku`](#ruku)

<a id="manzil"></a>

### Manzil — المنزل

<!-- source: standards/terminology/concepts/manzil.yml -->

| field | value |
| --- | --- |
| `code` | `manzil` |
| `plural` | `manzils` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَنْزِل |

**Definition:** One of 7 traditional parts of the Quran, made to ease completing it in a week.

**Purpose:** Used in applications that support the manzil system and the reading plans built on it.

**Related:** [`juz`](#juz), [`khatmah`](#khatmah)

<a id="rubu_al_hizb"></a>

### Rubu al-Hizb — ربع الحزب

<!-- source: standards/terminology/concepts/rubu_al_hizb.yml -->

| field | value |
| --- | --- |
| `code` | `rubu_al_hizb` |
| `plural` | `rubu_al_hizbs` |
| `kind` | `entity` |
| Part of | [`hizb`](#hizb) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | رُبْع الحِزْب |
| Other spellings | `rub_al_hizb`, `rub'_al-hizb`, `rub_el_hizb`, `rub`, `rubu`, `rub_hizb`, `hizb_quarter`, `quarter_hizb` |

**Definition:** A quarter of a hizb in the well-known division of the mushaf.

**Purpose:** Used to represent the finer division of the hizb and where its marks fall in the mushaf.

**Related:** [`hizb`](#hizb), [`thumn`](#thumn), [`division_mark`](#division_mark)

<a id="ruku"></a>

### Ruku — الركوع

<!-- source: standards/terminology/concepts/ruku.yml -->

| field | value |
| --- | --- |
| `code` | `ruku` |
| `plural` | `rukus` |
| `kind` | `entity` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرُّكُوع |
| Other spellings | `ruku'`, `rukūʿ` |

**Definition:** A conventional section of the Quran used to organise reading, printed in some mushafs.

**Purpose:** Used in the applications and mushafs that follow the ruku division.

**Related:** [`juz`](#juz), [`mushaf_edition`](#mushaf_edition)

<a id="thumn"></a>

### Thumn — الثمن

<!-- source: standards/terminology/concepts/thumn.yml -->

| field | value |
| --- | --- |
| `code` | `thumn` |
| `plural` | `thumns` |
| `kind` | `entity` |
| Part of | [`hizb`](#hizb) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الثُّمْن |
| Other spellings | `thumun` |

**Definition:** An eighth of a hizb, a division used in some mushafs and schools.

**Purpose:** Used when supporting sources or mushafs that divide the hizb into eighths.

**Related:** [`hizb`](#hizb), [`rubu_al_hizb`](#rubu_al_hizb)

## Surah classification — `surah_classification`

<a id="mathani"></a>

### Mathani — المثاني

<!-- source: standards/terminology/concepts/mathani.yml -->

| field | value |
| --- | --- |
| `code` | `mathani` |
| `kind` | `classification_value` |
| Parent | [`surah_group`](#surah_group) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المَثَانِي |

**Definition:** The surahs shorter than the miun, coming after them in the traditional division; called mathani because they are recited more often.

**Purpose:** Used as a value of surah group, so that reading plans and the tafsir works that treat the group as a unit can refer to it.

> The standard does not list the group's members surah by surah: the sources differ over the seventh of the tiwal and the start of the mufassal, and no registry yet enumerates each group's members with its source.

**Related:** [`surah_group`](#surah_group), [`surah`](#surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="miun"></a>

### Miun — المئون

<!-- source: standards/terminology/concepts/miun.yml -->

| field | value |
| --- | --- |
| `code` | `miun` |
| `kind` | `classification_value` |
| Parent | [`surah_group`](#surah_group) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المِئُون |
| English gloss | `Hundred-Verse Surahs` |

**Definition:** The surahs whose ayahs come to about 100, a little more or a little less.

**Purpose:** Used as a value of surah group, so that reading plans and the tafsir works that treat the group as a unit can refer to it.

> The standard does not list the group's members surah by surah: the sources differ over the seventh of the tiwal and the start of the mufassal, and no registry yet enumerates each group's members with its source.

**Related:** [`surah_group`](#surah_group), [`surah`](#surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="mufassal"></a>

### Mufassal — المفصل

<!-- source: standards/terminology/concepts/mufassal.yml -->

| field | value |
| --- | --- |
| `code` | `mufassal` |
| `kind` | `classification_value` |
| Parent | [`surah_group`](#surah_group) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المُفَصَّل |

**Definition:** A group of the short surahs following the mathani; scholars differ over where it begins.

**Purpose:** Used as a value of surah group, so that reading plans and the tafsir works that treat the group as a unit can refer to it.

> The standard does not list the group's members surah by surah: the sources differ over the seventh of the tiwal and the start of the mufassal, and no registry yet enumerates each group's members with its source.

**Related:** [`surah_group`](#surah_group), [`surah`](#surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/221`

<a id="saba_tiwal"></a>

### Saba Tiwal — السبع الطوال

<!-- source: standards/terminology/concepts/saba_tiwal.yml -->

| field | value |
| --- | --- |
| `code` | `saba_tiwal` |
| `kind` | `classification_value` |
| Parent | [`surah_group`](#surah_group) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | السَّبْع الطِّوَال |
| Other spellings | `sab_tiwal` |
| English gloss | `Seven Long Surahs` |

**Definition:** A group of the longest surahs of the Quran, at its beginning, with a known disagreement over which surah is the seventh.

**Purpose:** Used as a value of surah group, so that reading plans and the tafsir works that treat the group as a unit can refer to it.

> The standard does not list the group's members surah by surah: the sources differ over the seventh of the tiwal and the start of the mufassal, and no registry yet enumerates each group's members with its source.

**Related:** [`surah_group`](#surah_group), [`surah`](#surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="surah_group"></a>

### Surah Group — تصنيف السور

<!-- source: standards/terminology/concepts/surah_group.yml -->

| field | value |
| --- | --- |
| `code` | `surah_group` |
| `kind` | `classification` |
| Values | [`mathani`](#mathani), [`miun`](#miun), [`mufassal`](#mufassal), [`saba_tiwal`](#saba_tiwal) |
| Origin | `standard` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | تَصْنِيف السُّوَر |

**Definition:** A classification gathering surahs by inherited conventional divisions that rest on length or on their place among the groups of surahs.

**Purpose:** Gives classifications such as the tiwal, the miun, the mathani and the mufassal one parent.

**Related:** [`saba_tiwal`](#saba_tiwal), [`miun`](#miun), [`mathani`](#mathani), [`mufassal`](#mufassal), [`surah`](#surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/221`

## Mushaf and layout — `mushaf`

<a id="font"></a>

### Font — الخط

<!-- source: standards/terminology/concepts/font.yml -->

| field | value |
| --- | --- |
| `code` | `font` |
| `plural` | `fonts` |
| `kind` | `concept` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الخَطّ |

**Definition:** A file carrying a set of glyphs and the rules for laying them out, used to render the text of a mushaf.

**Purpose:** Used to record which font a digital mushaf depends on, since in many of them the text renders correctly in one font only, so letter codes, their shapes and line positions are tied to it.

- A font is a means of display; the rasm is a property of the written text itself.
- A glyph is a shape inside a font; a letter is a unit of the text.

**Related:** [`glyph`](#glyph), [`rasm`](#rasm), [`layout`](#layout), [`line`](#line), [`mushaf_edition`](#mushaf_edition)

<a id="layout"></a>

### Layout — التخطيط

<!-- source: standards/terminology/concepts/layout.yml -->

| field | value |
| --- | --- |
| `code` | `layout` |
| `plural` | `layouts` |
| `kind` | `concept` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّخْطِيط |

**Definition:** The visual arrangement of the text and its elements into pages, lines and positions within a given mushaf or view.

**Purpose:** Keeps visual data apart from the fixed textual structure of the Quran.

**Related:** [`mushaf_edition`](#mushaf_edition), [`page`](#page), [`line`](#line), [`font`](#font), [`maqta_al_ayah`](#maqta_al_ayah), [`mushaf`](#mushaf)

<a id="line"></a>

### Line — السطر

<!-- source: standards/terminology/concepts/line.yml -->

| field | value |
| --- | --- |
| `code` | `line` |
| `plural` | `lines` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | السَّطْر |

**Definition:** A typeset line within a page of a mushaf or of a given layout.

**Purpose:** Used to represent where text and shapes sit within the typeset layout.

**Related:** [`page`](#page), [`layout`](#layout), [`maqta_al_ayah`](#maqta_al_ayah), [`font`](#font)

<a id="maqta_al_ayah"></a>

### Maqta al-Ayah — مقطع الآية

<!-- source: standards/terminology/concepts/maqta_al_ayah.yml -->

| field | value |
| --- | --- |
| `code` | `maqta_al_ayah` |
| `plural` | `maqta_al_ayahs` |
| `kind` | `unit` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَقْطَع الآيَة |
| Arabic plural | مقاطع الآيات |
| Other spellings | `ayah_segment`, `ayah_part`, `line_ayah`, `g_ayah` |
| English gloss | `ayah fragment` |

**Definition:** What appears of one ayah on one line of a page of a given mushaf; an ayah that runs over two lines is two maqtas.

**Purpose:** Used as the unit of display and tagging in the page layout, because an ayah does not keep to a line nor a line to an ayah; alignment and highlighting in a drawn mushaf are built on it.

- A maqta belongs to the layout of one mushaf and is no part of the identity of the ayah.
- A maqta is not a word: it may be a word, several words, or part of a word where the break falls inside one.

**Related:** [`ayah`](#ayah), [`line`](#line), [`page`](#page), [`layout`](#layout)

**Sources:**

- مصحف حفص — كلمة كلمة — `glossary!g.ayah`

<a id="page"></a>

### Page — الصفحة

<!-- source: standards/terminology/concepts/page.yml -->

| field | value |
| --- | --- |
| `code` | `page` |
| `plural` | `pages` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الصَّفْحَة |
| Other spellings | `safhah` |

**Definition:** A typographic unit of a given mushaf's layout; its content and its boundaries may differ from one mushaf or edition to another.

**Purpose:** Used for rendering, navigation and visual alignment according to the pages of a particular mushaf.

**Related:** [`mushaf_edition`](#mushaf_edition), [`layout`](#layout), [`line`](#line), [`maqta_al_ayah`](#maqta_al_ayah), [`mushaf`](#mushaf)

<a id="rasm"></a>

### Rasm — الرسم

<!-- source: standards/terminology/concepts/rasm.yml -->

| field | value |
| --- | --- |
| `code` | `rasm` |
| `kind` | `classification` |
| Values | [`rasm_imlai`](#rasm_imlai), [`rasm_uthmani`](#rasm_uthmani) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرَّسْم |
| Other spellings | `rasm_type` |
| English gloss | `orthography` |

**Definition:** The way the words of the Quran are written: which letters are written and which omitted or added, and where words are joined or kept apart.

**Purpose:** Used as a classification stating which rasm a text, a mushaf or a dataset is written in, so that search, comparison and rendering branch on it; and it keeps the layer of the rasm distinct from the font, the layout and the drawn glyphs.

- The rasm is which letters are written, omitted, joined or kept apart; the dabt is the marks of pronunciation placed on the letters.
- The script is the shape of the letters in one mushaf; the rasm is what holds in every mushaf written in it.

**Related:** [`rasm_uthmani`](#rasm_uthmani), [`rasm_imlai`](#rasm_imlai), [`mushaf_mark`](#mushaf_mark), [`font`](#font), [`mushaf`](#mushaf), [`mushaf_edition`](#mushaf_edition), [`omitted_alif`](#omitted_alif), [`orthographic_mark`](#orthographic_mark), [`tashkil`](#tashkil)

<a id="rasm_imlai"></a>

### Rasm Imlai — الرسم الإملائي

<!-- source: standards/terminology/concepts/rasm_imlai.yml -->

| field | value |
| --- | --- |
| `code` | `rasm_imlai` |
| `kind` | `classification_value` |
| Parent | [`rasm`](#rasm) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرَّسْم الإِمْلَائِيّ |
| Other spellings | `imlaei`, `imlai`, `imla'i`, `imlaai`, `simple`, `text_simple`, `text_imlaei`, `rasm_imlaei` |
| English gloss | `modern orthography`, `standard orthography` |

**Definition:** Writing the words of the Quran by the rules of modern orthography, writing what the Uthmani rasm omits and omitting what it adds, so that they read in their familiar form.

**Purpose:** Used to state that a text follows modern orthography, which is the text that search, quotation and display outside the mushaf are built on, as against the Uthmani text the mushaf is displayed in.

- The imlai rasm is a writing and not a reading: the wording is one, and what differs is the form of the word.
- The imlai text is not the search text stripped of dabt, though the second is derived from the first.

> Deriving the name with the tool gives `orthographic_rasm`, because the general-words table translates «إملائي» to `orthographic` for the sake of «العلامة الإملائية»; the recorded name is `rasm_imlai`, which is what databases and APIs use, and the decision is in the decision record.

**Related:** [`rasm`](#rasm), [`rasm_uthmani`](#rasm_uthmani)

<a id="rasm_uthmani"></a>

### Rasm Uthmani — الرسم العثماني

<!-- source: standards/terminology/concepts/rasm_uthmani.yml -->

| field | value |
| --- | --- |
| `code` | `rasm_uthmani` |
| `kind` | `classification_value` |
| Parent | [`rasm`](#rasm) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرَّسْم العُثْمَانِيّ |
| Other spellings | `uthmani`, `uthmanic`, `othmani`, `rasm_othmani` |
| English gloss | `Uthmanic Orthography` |
| Display evidence | GitHub phrase search: rasm uthmani 100 vs uthmani rasm 65. The Arabic word order wins in English writing, and it matches the code. |

**Definition:** The way the words of the Uthmani mushafs are written, with the omission, addition, substitution, separation and joining that go with it.

**Purpose:** Used to state that a text follows the rules of the Uthmani rasm rather than another orthography.

**Related:** [`rasm`](#rasm), [`rasm_imlai`](#rasm_imlai), [`mushaf`](#mushaf)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/146`

## Dabt and Mushaf marks — `dabt`

<a id="ayah_mark"></a>

### Ayah Mark — علامة الآية

<!-- source: standards/terminology/concepts/ayah_mark.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_mark` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة الآيَة |
| Dabt name | عَلَامَة رَأْس الآيَة |
| Name by shape | دَارَة |
| Mushaf introduction name | عَلَامَة رَأْس الآيَة |
| Symbol | ۝ |
| Characters | `U+06DD` ARABIC END OF AYAH |
| Mark family | `mustaqill` |
| Other spellings | `end_of_ayah`, `ayah_marker`, `ayah_separator` |

**Definition:** The circle separating one ayah from the next. It is placed at the ayah's end and, in most mushafs, carries its number.

**Purpose:** Used to mark an ayah's boundary in the written text; it is the sign from which a renderer or an analyser reads where an ayah ends and what its number is.

- The mark is something drawn in the mushaf; the fasilah is the ayah's ending as a matter of the text itself.
- The number inside the circle follows an ayah numbering system and is not part of the mark.

**Related:** [`ayah`](#ayah), [`fasilah`](#fasilah), [`ayah_numbering_system`](#ayah_numbering_system)

<a id="dammah"></a>

### Dammah — الضمة

<!-- source: standards/terminology/concepts/dammah.yml -->

| field | value |
| --- | --- |
| `code` | `dammah` |
| `kind` | `mark` |
| Parent | [`harakah`](#harakah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الضَّمَّة |
| Dabt name | الضَّمَّة (وتُسمَّى قديمًا الرَّفْعَة) |
| Name by shape | وَاو صَغِيرَة فَوْق الحَرْف |
| Symbol | ـُ |
| Characters | `U+064F` ARABIC DAMMA |
| Mark family | `harakah` |
| Other spellings | `damma` |

**Definition:** The mark for the short vowel u on the letter.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!damma`

<a id="division_mark"></a>

### Division Mark — علامة التقسيم

<!-- source: standards/terminology/concepts/division_mark.yml -->

| field | value |
| --- | --- |
| `code` | `division_mark` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة التَّقْسِيم |
| Dabt name | عَلَامَة التَّحْزِيب |
| Name by shape | نَجْمَة مُثَمَّنَة |
| Mushaf introduction name | عَلَامَة بِدَايَة الأَجْزَاء والأَحْزَاب وأَنْصَافِها وأَرْبَاعِها |
| Symbol | نَجْمَة |
| Characters | `U+06DE` ARABIC START OF RUB EL HIZB |
| Mark family | `mustaqill` |
| Other spellings | `hizb_mark`, `juz_mark`, `rub_el_hizb_mark`, `rub_mark` |
| Deprecated names | `alamat_al_tahzib` |

**Definition:** Marks the start of a juz, a hizb, or a half or quarter of one.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

- The division mark is a sign in the mushaf; the juz, the hizb and its quarters are divisions of the text it points to.

> `alamat_al_tahzib` was a separate entry defining the same thing; it was merged into this one.

**Related:** [`hizb`](#hizb), [`rubu_al_hizb`](#rubu_al_hizb), [`juz`](#juz)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!hizb`

<a id="dot"></a>

### Dot — النقطة

<!-- source: standards/terminology/concepts/dot.yml -->

| field | value |
| --- | --- |
| `code` | `dot` |
| `kind` | `mark` |
| Parent | [`ijam`](#ijam) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النُّقْطَة |
| Dabt name | نَقْط الإِعْجَام — النُّقْطَة |
| Name by shape | نُقْطَة وَاحِدَة |
| Symbol | نُقْطَة وَاحِدَة |
| Mark family | `ijam` |
| Other spellings | `nuqtah` |

**Definition:** One dot, above or below, distinguishing a letter from the others that share its skeleton (ijam): baa, noon, jeem, khaa, dhaal.

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!dot`

<a id="fathah"></a>

### Fathah — الفتحة

<!-- source: standards/terminology/concepts/fathah.yml -->

| field | value |
| --- | --- |
| `code` | `fathah` |
| `kind` | `mark` |
| Parent | [`harakah`](#harakah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الفَتْحَة |
| Dabt name | الفَتْحَة (وتُسمَّى قديمًا النَّصْبَة) |
| Name by shape | أَلِف مُضْجَعَة فَوْق الحَرْف |
| Symbol | ـَ |
| Characters | `U+064E` ARABIC FATHA |
| Mark family | `harakah` |
| Other spellings | `fatha` |

**Definition:** The mark for the short vowel a on the letter.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!fatha`

<a id="hamzah"></a>

### Hamzah — الهمزة

<!-- source: standards/terminology/concepts/hamzah.yml -->

| field | value |
| --- | --- |
| `code` | `hamzah` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الهَمْزَة |
| Dabt name | الهَمْزَة — رَأْس العَيْن |
| Name by shape | رَأْس عَيْن |
| Symbol | ء |
| Characters | `U+0621` ARABIC LETTER HAMZA, `U+0654` ARABIC HAMZA ABOVE, `U+0655` ARABIC HAMZA BELOW |
| Mark family | `imlaiyyah` |
| Other spellings | `hamza` |

**Definition:** Marks a fully realised hamzah (hamzat al-qat).

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`hamzat_al_wasl`](#hamzat_al_wasl), [`madd_al_badal`](#madd_al_badal), [`madd_munfasil`](#madd_munfasil), [`madd_muttasil`](#madd_muttasil)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!hamza`

<a id="hamzat_al_wasl"></a>

### Hamzat al-Wasl — همزة الوصل

<!-- source: standards/terminology/concepts/hamzat_al_wasl.yml -->

| field | value |
| --- | --- |
| `code` | `hamzat_al_wasl` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | هَمْزَة الوَصْل |
| Dabt name | رَأْس الصَّاد (من «صِلَة») — عَلَامَة هَمْزَة الوَصْل |
| Name by shape | رَأْس صَاد فَوْق الأَلِف |
| Mushaf introduction name | رَأْس صَاد صَغِيرَة فَوْق أَلِف الوَصْل |
| Symbol | ص صَغِيرَة فَوْق الأَلِف |
| Characters | `U+0671` ARABIC LETTER ALEF WASLA |
| Mark family | `imlaiyyah` |
| Other spellings | `alif_wasl`, `hamzat_wasl`, `wasl`, `wasla` |

**Definition:** Marks a connecting hamzah, dropped whenever the word is reached in continuation.

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`hamzah`](#hamzah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!wasla`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/127) — `127`

<a id="harakah"></a>

### Harakah — الحركة

<!-- source: standards/terminology/concepts/harakah.yml -->

| field | value |
| --- | --- |
| `code` | `harakah` |
| `kind` | `classification` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Values | [`dammah`](#dammah), [`fathah`](#fathah), [`kasrah`](#kasrah), [`shaddah`](#shaddah), [`sukun`](#sukun) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحَرَكَة |
| Other spellings | `haraka`, `harakat` |
| English gloss | `Vowel Mark`, `diacritics` |

**Definition:** A mark fixing a letter's vowel, its absence or its doubling: fathah, dammah, kasrah, sukun and shaddah.

**Purpose:** Used as the parent of the dabt marks that determine how the letter itself is pronounced.

**Related:** [`mushaf_mark`](#mushaf_mark), [`tanwin`](#tanwin), [`tashkil`](#tashkil), [`shaddah`](#shaddah), [`sukun`](#sukun)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/151`

<a id="ijam"></a>

### Ijam — الإعجام

<!-- source: standards/terminology/concepts/ijam.yml -->

| field | value |
| --- | --- |
| `code` | `ijam` |
| `kind` | `classification` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Values | [`dot`](#dot), [`three_dots`](#three_dots), [`two_dots`](#two_dots) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِعْجَام |

**Definition:** The dotting that distinguishes a letter from the letters that share its written shape.

**Purpose:** Used as the parent of the dot shapes, which are told apart by their number and position rather than by their function.

**Related:** [`mushaf_mark`](#mushaf_mark), [`letter`](#letter), [`tashkil`](#tashkil)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/151`

<a id="imalah"></a>

### Imalah — الإمالة

<!-- source: standards/terminology/concepts/imalah.yml -->

| field | value |
| --- | --- |
| `code` | `imalah` |
| `kind` | `mark` |
| Parent | [`qiraah_mark`](#qiraah_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِمَالَة |
| Dabt name | الإِمَالَة — النُّقْطَة تَحْت الحَرْف |
| Name by shape | نُقْطَة كَبِيرَة مَطْمُوسَة تَحْت الحَرْف |
| Mushaf introduction name | نُقْطَة كَبِيرَة مَطْمُوسَة الوَسَط تَحْت الحَرْف |
| Symbol | نُقْطَة تَحْت الحَرْف |
| Characters | `U+06EA` ARABIC EMPTY CENTRE LOW STOP |
| Mark family | `alamat_qiraah` |

**Definition:** Marks the major imalah: a fathah pronounced leaning toward kasrah. In the riwayah of Hafs it occurs at one place only (11:41).

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

**Related:** [`usul`](#usul)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!imalah`

<a id="ishmam"></a>

### Ishmam — الإشمام

<!-- source: standards/terminology/concepts/ishmam.yml -->

| field | value |
| --- | --- |
| `code` | `ishmam` |
| `kind` | `mark` |
| Parent | [`qiraah_mark`](#qiraah_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِشْمَام |
| Dabt name | الإِشْمَام |
| Name by shape | نُقْطَة كَبِيرَة مَطْمُوسَة فَوْق الحَرْف |
| Mushaf introduction name | النُّقْطَة المَذْكُورَة فَوْق آخِر المِيم |
| Symbol | نُقْطَة فَوْق الحَرْف |
| Characters | `U+06EC` ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE |
| Mark family | `alamat_qiraah` |

**Definition:** Marks ishmam: the lips are rounded to hint at a dropped dammah, without any sound.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!ishmam`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/131) — `131`

<a id="kasrah"></a>

### Kasrah — الكسرة

<!-- source: standards/terminology/concepts/kasrah.yml -->

| field | value |
| --- | --- |
| `code` | `kasrah` |
| `kind` | `mark` |
| Parent | [`harakah`](#harakah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الكَسْرَة |
| Dabt name | الكَسْرَة (وتُسمَّى قديمًا الخَفْضَة) |
| Name by shape | أَلِف مُضْجَعَة تَحْت الحَرْف |
| Symbol | ـِ |
| Characters | `U+0650` ARABIC KASRA |
| Mark family | `harakah` |
| Other spellings | `kasra` |

**Definition:** The mark for the short vowel i on the letter.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!kasra`

<a id="maddah"></a>

### Maddah — المدة

<!-- source: standards/terminology/concepts/maddah.yml -->

| field | value |
| --- | --- |
| `code` | `maddah` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدَّة |
| Dabt name | عَلَامَة المَدّ — المَدَّة |
| Name by shape | خَطّ مُتَمَوِّج مَمْدُود فَوْق الحَرْف |
| Mushaf introduction name | عَلَامَة المَدّ |
| Symbol | خَطّ المَدّ |
| Characters | `U+0653` ARABIC MADDAH ABOVE, `U+06E4` ARABIC SMALL HIGH MADDA |
| Mark family | `imlaiyyah` |
| Other spellings | `madda` |

**Definition:** Marks that the letter is lengthened beyond the natural madd.

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`madd`](#madd)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!maddah`

<a id="mushaf_mark"></a>

### Mushaf Mark — علامة المصحف

<!-- source: standards/terminology/concepts/mushaf_mark.yml -->

| field | value |
| --- | --- |
| `code` | `mushaf_mark` |
| `kind` | `classification` |
| Values | [`ayah_mark`](#ayah_mark), [`division_mark`](#division_mark), [`harakah`](#harakah), [`ijam`](#ijam), [`orthographic_mark`](#orthographic_mark), [`qiraah_mark`](#qiraah_mark), [`rectangular_zero`](#rectangular_zero), [`rounded_zero`](#rounded_zero), [`sajdah_line`](#sajdah_line), [`sajdah_mark`](#sajdah_mark), [`small_meem`](#small_meem), [`tanwin`](#tanwin), [`waqf_mark`](#waqf_mark) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة المُصْحَف |

**Definition:** A sign or mark that is not one of a word's original letters, used in the mushaf for reading, organisation or guidance.

**Purpose:** Gives the different marks one parent, instead of treating them as unrelated kinds.

**Related:** [`harakah`](#harakah), [`tanwin`](#tanwin), [`ijam`](#ijam), [`orthographic_mark`](#orthographic_mark), [`qiraah_mark`](#qiraah_mark), [`waqf_mark`](#waqf_mark), [`rasm`](#rasm), [`tashkil`](#tashkil)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="omitted_alif"></a>

### Omitted Alif — الألف المحذوفة

<!-- source: standards/terminology/concepts/omitted_alif.yml -->

| field | value |
| --- | --- |
| `code` | `omitted_alif` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الأَلِف المَحْذُوفَة |
| Dabt name | الأَلِف المَحْذُوفَة — أَلِف صَغِيرَة قَائِمَة |
| Name by shape | أَلِف صَغِيرَة قَائِمَة فَوْق الحَرْف |
| Mushaf introduction name | مِنَ الحُرُوف الصَّغِيرَة الدَّالَّة على المَتْرُوك مِنَ الرَّسْم |
| Symbol | ا صَغِيرَة قَائِمَة |
| Characters | `U+0670` ARABIC LETTER SUPERSCRIPT ALEF |
| Mark family | `imlaiyyah` |
| Other spellings | `alif_mahdhufah`, `dagger_alif`, `small-alef`, `small_alef`, `small_alif`, `superscript_alif` |

**Definition:** Restores an alif omitted from the Uthmani skeleton but obligatory in pronunciation.

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`rasm`](#rasm), [`orthographic_mark`](#orthographic_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!small-alef`

<a id="orthographic_mark"></a>

### Orthographic Mark — العلامة الإملائية

<!-- source: standards/terminology/concepts/orthographic_mark.yml -->

| field | value |
| --- | --- |
| `code` | `orthographic_mark` |
| `kind` | `classification` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Values | [`hamzah`](#hamzah), [`hamzat_al_wasl`](#hamzat_al_wasl), [`maddah`](#maddah), [`omitted_alif`](#omitted_alif), [`small_noon`](#small_noon), [`small_waw`](#small_waw), [`small_yaa`](#small_yaa) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَلَامَة الإِمْلَائِيَّة |

**Definition:** A mark fixing how a word is written, such as the hamzah, the maddah and the small letters.

**Purpose:** Used as the parent of the marks that concern how a word is written, rather than its vowel or how it is stopped on.

**Related:** [`mushaf_mark`](#mushaf_mark), [`rasm`](#rasm), [`omitted_alif`](#omitted_alif)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/134) — `134`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="qiraah_mark"></a>

### Qiraah Mark — علامة القراءة

<!-- source: standards/terminology/concepts/qiraah_mark.yml -->

| field | value |
| --- | --- |
| `code` | `qiraah_mark` |
| `kind` | `classification` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Values | [`imalah`](#imalah), [`ishmam`](#ishmam), [`saktah_mark`](#saktah_mark), [`seen_al_qiraah`](#seen_al_qiraah), [`tashil`](#tashil) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة القِرَاءَة |

**Definition:** A mark pointing to a particular manner of delivery at its place, such as saktah, ishmam and tashil.

**Purpose:** Used as the parent of the marks that alert the reader to a particular delivery rather than to the pointing of a letter.

**Related:** [`mushaf_mark`](#mushaf_mark), [`qiraah`](#qiraah), [`saktah_mark`](#saktah_mark)

<a id="rectangular_zero"></a>

### Rectangular Zero — الصفر المستطيل

<!-- source: standards/terminology/concepts/rectangular_zero.yml -->

| field | value |
| --- | --- |
| `code` | `rectangular_zero` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الصِّفْر المُسْتَطِيل |
| Dabt name | الصِّفْر المُسْتَطِيل القَائِم |
| Name by shape | مُسْتَطِيل صَغِير قَائِم خَالِي الوَسَط |
| Mushaf introduction name | دَائِرَة قَائِمَة مُسْتَطِيلَة خَالِيَة الوَسَط |
| Symbol | مُسْتَطِيل قَائِم صَغِير |
| Characters | `U+06E0` ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO |
| Mark family | `dabt` |
| Other spellings | `sifr-mustatil`, `sifr_mustatil` |

**Definition:** Marks an alif dropped in continuation but pronounced when stopping on it.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!sifr-mustatil`

<a id="rounded_zero"></a>

### Rounded Zero — الصفر المستدير

<!-- source: standards/terminology/concepts/rounded_zero.yml -->

| field | value |
| --- | --- |
| `code` | `rounded_zero` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الصِّفْر المُسْتَدِير |
| Dabt name | الصِّفْر المُسْتَدِير |
| Name by shape | دَائِرَة صَغِيرَة خَالِيَة الوَسَط |
| Mushaf introduction name | دَائِرَة صَغِيرَة خَالِيَة الوَسَط |
| Symbol | دَائِرَة صَغِيرَة |
| Characters | `U+06DF` ARABIC SMALL HIGH ROUNDED ZERO |
| Mark family | `dabt` |
| Other spellings | `sifr-mustadir`, `sifr_mustadir` |

**Definition:** Marks a letter present in the skeleton but never pronounced — neither in continuation nor when stopping.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!sifr-mustadir`

<a id="sajdah_line"></a>

### Sajdah Line — خط السجدة

<!-- source: standards/terminology/concepts/sajdah_line.yml -->

| field | value |
| --- | --- |
| `code` | `sajdah_line` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | خَطّ السَّجْدَة |
| Dabt name | خَطّ مُوجِب السَّجْدَة |
| Name by shape | خَطّ أُفُقِيّ فَوْق الكَلِمَة |
| Mushaf introduction name | خَطّ أُفُقِيّ فَوْق الكَلِمَة الدَّالّ على مُوجِب السَّجْدَة |
| Symbol | خَطّ أُفُقِيّ |
| Mark family | `mustaqill` |
| Other spellings | `khatt_mujib_al_sajdah`, `sajdah-line` |

**Definition:** Marks the word that makes prostration due.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

**Related:** [`sajdah_mark`](#sajdah_mark), [`mawdi_al_sajdah`](#mawdi_al_sajdah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!sajdah-line`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="sajdah_mark"></a>

### Sajdah Mark — علامة السجدة

<!-- source: standards/terminology/concepts/sajdah_mark.yml -->

| field | value |
| --- | --- |
| `code` | `sajdah_mark` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة السَّجْدَة |
| Dabt name | عَلَامَة مَوْضِع السَّجْدَة — المِحْرَاب |
| Name by shape | مِحْرَاب صَغِير |
| Mushaf introduction name | عَلَامَة مَوْضِع السَّجْدَة |
| Symbol | مِحْرَاب |
| Mark family | `mustaqill` |
| Other spellings | `sajda_mark`, `sajda_sign`, `sajdah-sign`, `sajdah_sign` |
| Deprecated names | `alamat_mawdi_al_sajdah` |

**Definition:** Marks the point at which the reader prostrates.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

- The sajdah mark is a sign in the mushaf; mawdi al-sajdah is the place in the text; sujud al-tilawah is the act.

> `alamat_mawdi_al_sajdah` was a separate entry defining the same thing; it was merged into this one.

**Related:** [`mawdi_al_sajdah`](#mawdi_al_sajdah), [`sujud_al_tilawah`](#sujud_al_tilawah), [`sajdah_line`](#sajdah_line)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!sajdah-sign`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="saktah_mark"></a>

### Saktah Mark — علامة السكتة

<!-- source: standards/terminology/concepts/saktah_mark.yml -->

| field | value |
| --- | --- |
| `code` | `saktah_mark` |
| `kind` | `mark` |
| Parent | [`qiraah_mark`](#qiraah_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة السَّكْتَة |
| Dabt name | السِّين — عَلَامَة السَّكْت |
| Name by shape | سِين |
| Mushaf introduction name | السِّين فَوْق الحَرْف الأَخِير الدَّالَّة على السَّكْت |
| Symbol | س |
| Characters | `U+06DC` ARABIC SMALL HIGH SEEN |
| Mark family | `alamat_qiraah` |
| Other spellings | `alamat_al_sakt` |

**Definition:** Marks a saktah: a brief pause without taking a breath, then continuing.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

- The saktah mark is a sign in the mushaf; the saktah is the pause itself.

**Related:** [`saktah`](#saktah), [`qiraah_mark`](#qiraah_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!saktah`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/126) — `126`

<a id="seen_al_qiraah"></a>

### Seen al-Qiraah — سين القراءة

<!-- source: standards/terminology/concepts/seen_al_qiraah.yml -->

| field | value |
| --- | --- |
| `code` | `seen_al_qiraah` |
| `kind` | `mark` |
| Parent | [`qiraah_mark`](#qiraah_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | سِين القِرَاءَة |
| Dabt name | السِّين الدَّالَّة على وَجْه القِرَاءَة |
| Name by shape | سِين فَوْق الصَّاد أو تَحْتَهَا |
| Mushaf introduction name | السِّين فَوْق الصَّاد أو تَحْتَهَا |
| Symbol | س |
| Characters | `U+06DC` ARABIC SMALL HIGH SEEN, `U+06E3` ARABIC SMALL LOW SEEN |
| Mark family | `alamat_qiraah` |
| Other spellings | `seen-reading`, `seen_reading`, `sin_qiraah` |
| Display evidence | letter name; unmeasurable directly, both forms are English words |

**Definition:** A small seen above a saad marks reading it as seen; below it, reading it as saad.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!seen-reading`

<a id="shaddah"></a>

### Shaddah — الشدة

<!-- source: standards/terminology/concepts/shaddah.yml -->

| field | value |
| --- | --- |
| `code` | `shaddah` |
| `kind` | `mark` |
| Parent | [`harakah`](#harakah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الشَّدَّة |
| Dabt name | الشَّدَّة — رَأْس الشِّين (من «شَدِيد») |
| Name by shape | رَأْس شِين بِلَا نُقَط |
| Mushaf introduction name | الشَّدَّة الدَّالَّة على الإِدْغَام |
| Symbol | ـّ |
| Characters | `U+0651` ARABIC SHADDA |
| Mark family | `harakah` |
| Other spellings | `shadda`, `tashdeed`, `tashdid` |

**Definition:** Marks a doubled letter: the first, vowelless, is merged into the second and the two are pronounced as one stressed letter.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

**Related:** [`harakah`](#harakah), [`idgham`](#idgham)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!shadda`

<a id="small_meem"></a>

### Small Meem — الميم الصغيرة

<!-- source: standards/terminology/concepts/small_meem.yml -->

| field | value |
| --- | --- |
| `code` | `small_meem` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المِيم الصَّغِيرَة |
| Dabt name | المِيم الصَّغِيرَة — عَلَامَة القَلْب |
| Name by shape | مِيم صَغِيرَة، عُلْيَا أو سُفْلَى |
| Mushaf introduction name | المِيم الصَّغِيرَة |
| Symbol | م صَغِيرَة |
| Characters | `U+06E2` ARABIC SMALL HIGH MEEM ISOLATED FORM, `U+06ED` ARABIC SMALL LOW MEEM |
| Mark family | `dabt` |
| Other spellings | `iqlab_meem`, `meem-iqlab`, `meem_iqlab`, `meem_saghirah`, `mim_saghirah` |
| Display evidence | GitHub phrase search: meem sakinah 308 vs mim sakinah 57 |

**Definition:** Marks iqlab: a vowelless noon or tanwin pronounced as meem before baa.

**Purpose:** Used as a mark of the mushaf, so that rendering and analysis know where it sits and what it points to.

**Related:** [`noon_sakinah`](#noon_sakinah), [`iqlab`](#iqlab)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!meem-iqlab`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`

<a id="small_noon"></a>

### Small Noon — النون الصغيرة

<!-- source: standards/terminology/concepts/small_noon.yml -->

| field | value |
| --- | --- |
| `code` | `small_noon` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النُّون الصَّغِيرَة |
| Dabt name | النُّون الصَّغِيرَة — الحَرْف المُلْحَق بالرَّسْم |
| Name by shape | نُون صَغِيرَة فَوْق السَّطْر |
| Mushaf introduction name | مِنَ الحُرُوف الصَّغِيرَة الدَّالَّة على المَتْرُوك مِنَ الرَّسْم |
| Symbol | ن صَغِيرَة |
| Characters | `U+06E8` ARABIC SMALL HIGH NOON |
| Mark family | `imlaiyyah` |
| Other spellings | `noon_saghirah`, `nun_saghirah`, `small-noon` |
| Display evidence | GitHub phrase search: noon sakinah 478 vs nun sakinah 118 |

**Definition:** Restores a noon omitted from the skeleton but obligatory in pronunciation, at one place only (21:88).

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!small-noon`

<a id="small_waw"></a>

### Small Waw — الواو الصغيرة

<!-- source: standards/terminology/concepts/small_waw.yml -->

| field | value |
| --- | --- |
| `code` | `small_waw` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَاو الصَّغِيرَة |
| Dabt name | الوَاو الصَّغِيرَة — عَلَامَة صِلَة هَاء الضَّمِير |
| Name by shape | وَاو صَغِيرَة بَعْد الهَاء |
| Mushaf introduction name | الوَاو الصَّغِيرَة |
| Symbol | و صَغِيرَة |
| Characters | `U+06E5` ARABIC SMALL WAW |
| Mark family | `imlaiyyah` |
| Other spellings | `small-waw`, `waw_saghirah` |

**Definition:** Marks the silah of the pronoun haa with dammah, pronounced as a waw in continuation.

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`madd_al_silah`](#madd_al_silah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!small-waw`

<a id="small_yaa"></a>

### Small Yaa — الياء الصغيرة

<!-- source: standards/terminology/concepts/small_yaa.yml -->

| field | value |
| --- | --- |
| `code` | `small_yaa` |
| `kind` | `mark` |
| Parent | [`orthographic_mark`](#orthographic_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | اليَاء الصَّغِيرَة |
| Dabt name | اليَاء الصَّغِيرَة — عَلَامَة صِلَة هَاء الضَّمِير |
| Name by shape | يَاء صَغِيرَة مَرْدُودَة بَعْد الهَاء |
| Mushaf introduction name | اليَاء الصَّغِيرَة المَرْدُودَة إِلى خَلْف |
| Symbol | ي صَغِيرَة |
| Characters | `U+06E6` ARABIC SMALL YEH, `U+06E7` ARABIC SMALL HIGH YEH |
| Mark family | `imlaiyyah` |
| Other spellings | `small-ya`, `small_ya`, `ya_saghirah`, `yaa_saghirah` |

**Definition:** Marks the silah of the pronoun haa with kasrah, pronounced as a yaa in continuation.

**Purpose:** Used as a value of the orthographic marks, so that software can tell where the rasm departs from the pronunciation.

**Related:** [`madd_al_silah`](#madd_al_silah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!small-ya`

<a id="sukun"></a>

### Sukun — السكون

<!-- source: standards/terminology/concepts/sukun.yml -->

| field | value |
| --- | --- |
| `code` | `sukun` |
| `kind` | `mark` |
| Parent | [`harakah`](#harakah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | السُّكُون |
| Dabt name | السُّكُون — رَأْس الخَاء المُهْمَلَة |
| Name by shape | رَأْس خَاء بِلَا نُقْطَة |
| Mushaf introduction name | رَأْس خَاء صَغِيرَة دُون نُقْطَة |
| Symbol | ـْ |
| Characters | `U+0652` ARABIC SUKUN, `U+06E1` ARABIC SMALL HIGH DOTLESS HEAD OF KHAH |
| Mark family | `harakah` |
| Other spellings | `sukoon` |

**Definition:** Marks a letter that carries no vowel and is articulated clearly.

**Purpose:** Used as a value of harakah, so that a letter's pronunciation is read from it in analysis, rendering and teaching rather than from the shape of the mark.

**Related:** [`harakah`](#harakah), [`noon_sakinah`](#noon_sakinah), [`madd_lazim`](#madd_lazim), [`qalqalah`](#qalqalah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!sukun`

<a id="tanwin"></a>

### Tanwin — التنوين

<!-- source: standards/terminology/concepts/tanwin.yml -->

| field | value |
| --- | --- |
| `code` | `tanwin` |
| `kind` | `classification` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Values | [`tanwin_al_damm`](#tanwin_al_damm), [`tanwin_al_fath`](#tanwin_al_fath), [`tanwin_al_kasr`](#tanwin_al_kasr) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّنْوِين |
| Other spellings | `tanween` |

**Definition:** An added vowelless noon at the end of a noun, written by doubling the shape of the vowel.

**Purpose:** Used as the parent of the three tanwin marks, gathering them instead of scattering them through one list.

**Related:** [`harakah`](#harakah), [`noon_sakinah`](#noon_sakinah), [`iqlab`](#iqlab), [`mushaf_mark`](#mushaf_mark), [`tanwin_al_damm`](#tanwin_al_damm), [`tanwin_al_fath`](#tanwin_al_fath), [`tanwin_al_kasr`](#tanwin_al_kasr)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="tanwin_al_damm"></a>

### Tanwin al-Damm — تنوين الضم

<!-- source: standards/terminology/concepts/tanwin_al_damm.yml -->

| field | value |
| --- | --- |
| `code` | `tanwin_al_damm` |
| `kind` | `mark` |
| Parent | [`tanwin`](#tanwin) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَنْوِين الضَّمّ |
| Dabt name | تَنْوِين الرَّفْع — الضَّمَّتَان |
| Name by shape | وَاوَان صَغِيرَتَان فَوْق الحَرْف |
| Mushaf introduction name | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| Symbol | ـٌ |
| Characters | `U+064C` ARABIC DAMMATAN, `U+08F1` ARABIC OPEN DAMMATAN |
| Mark family | `tanwin` |
| Other spellings | `dammatan`, `tanween_damm`, `tanwin_al_rafa`, `tanwin_damm` |

**Definition:** Marks the un tanwin. Stacked marks signal izhar; staggered marks with a shaddah on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

**Related:** [`tanwin`](#tanwin), [`noon_sakinah`](#noon_sakinah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!dammatan`

<a id="tanwin_al_fath"></a>

### Tanwin al-Fath — تنوين الفتح

<!-- source: standards/terminology/concepts/tanwin_al_fath.yml -->

| field | value |
| --- | --- |
| `code` | `tanwin_al_fath` |
| `kind` | `mark` |
| Parent | [`tanwin`](#tanwin) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَنْوِين الفَتْح |
| Dabt name | تَنْوِين النَّصْب — الفَتْحَتَان |
| Name by shape | أَلِفَان مُضْجَعَتَان فَوْق الحَرْف |
| Mushaf introduction name | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| Symbol | ـً |
| Characters | `U+064B` ARABIC FATHATAN, `U+08F0` ARABIC OPEN FATHATAN |
| Mark family | `tanwin` |
| Other spellings | `fathatan`, `tanween_fath`, `tanwin_al_nasb`, `tanwin_fath` |

**Definition:** Marks the an tanwin. Stacked marks signal izhar; staggered marks with a shaddah on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

**Related:** [`tanwin`](#tanwin), [`noon_sakinah`](#noon_sakinah), [`madd_al_iwad`](#madd_al_iwad)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!fathatan`

<a id="tanwin_al_kasr"></a>

### Tanwin al-Kasr — تنوين الكسر

<!-- source: standards/terminology/concepts/tanwin_al_kasr.yml -->

| field | value |
| --- | --- |
| `code` | `tanwin_al_kasr` |
| `kind` | `mark` |
| Parent | [`tanwin`](#tanwin) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَنْوِين الكَسْر |
| Dabt name | تَنْوِين الخَفْض — الكَسْرَتَان |
| Name by shape | أَلِفَان مُضْجَعَتَان تَحْت الحَرْف |
| Mushaf introduction name | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| Symbol | ـٍ |
| Characters | `U+064D` ARABIC KASRATAN, `U+08F2` ARABIC OPEN KASRATAN |
| Mark family | `tanwin` |
| Other spellings | `kasratan`, `tanween_kasr`, `tanwin_al_jarr`, `tanwin_al_khafd`, `tanwin_kasr` |

**Definition:** Marks the in tanwin. Stacked marks signal izhar; staggered marks with a shaddah on the next letter signal complete idgham, and without one, incomplete idgham or ikhfa.

**Purpose:** Used as a value of tanwin, so that the pronunciation of the noun's ending and its ruling are read from it rather than from the shape of the mark.

**Related:** [`tanwin`](#tanwin), [`noon_sakinah`](#noon_sakinah)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!kasratan`

<a id="tashil"></a>

### Tashil — التسهيل

<!-- source: standards/terminology/concepts/tashil.yml -->

| field | value |
| --- | --- |
| `code` | `tashil` |
| `kind` | `mark` |
| Parent | [`qiraah_mark`](#qiraah_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّسْهِيل |
| Dabt name | التَّسْهِيل — الهَمْزَة بَيْنَ بَيْنَ |
| Name by shape | نُقْطَة كَبِيرَة مَطْمُوسَة مَكَان الهَمْزَة |
| Mushaf introduction name | النُّقْطَة دُون الحَرَكَة مَكَان الهَمْزَة |
| Symbol | نُقْطَة مَكَان الهَمْزَة |
| Characters | `U+06EC` ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE |
| Mark family | `alamat_qiraah` |

**Definition:** Marks tashil: the hamzah softened to a sound between a hamzah and an alif.

**Purpose:** Used as a value of the qiraah marks, so that the reader is alerted to a particular delivery at its place.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!tashil`

<a id="tashkil"></a>

### Tashkil — التشكيل

<!-- source: standards/terminology/concepts/tashkil.yml -->

| field | value |
| --- | --- |
| `code` | `tashkil` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّشْكِيل |
| Other spellings | `tashkeel` |
| English gloss | `vowel marks`, `vocalization`, `vocalisation` |

**Definition:** The layer of dabt marks attached to the letters of the text, the harakat, tanwin, shaddah, sukun and what goes with them, taken as a whole.

**Purpose:** Used when the whole layer of dabt is handled at once, kept in display or stripped from the text for search, rather than one mark.

- Tashkil is the layer; a harakah is one mark.
- Dabt is the discipline and its rules; tashkil is what it produces on the letters.

**Related:** [`harakah`](#harakah), [`mushaf_mark`](#mushaf_mark), [`ijam`](#ijam), [`rasm`](#rasm)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="three_dots"></a>

### Three Dots — الثلاث نقط

<!-- source: standards/terminology/concepts/three_dots.yml -->

| field | value |
| --- | --- |
| `code` | `three_dots` |
| `kind` | `mark` |
| Parent | [`ijam`](#ijam) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الثَّلَاث نُقَط |
| Dabt name | نَقْط الإِعْجَام — الثَّلَاث نُقَط |
| Name by shape | ثَلَاث نُقَط مُثَلَّثَة |
| Symbol | ثَلَاث نُقَط |
| Mark family | `ijam` |
| Other spellings | `thalath_nuqat`, `three-dots` |

**Definition:** Three dots above the letter, distinguishing it from the others that share its skeleton (ijam): thaa, sheen.

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!three-dots`

<a id="two_dots"></a>

### Two Dots — النقطتان

<!-- source: standards/terminology/concepts/two_dots.yml -->

| field | value |
| --- | --- |
| `code` | `two_dots` |
| `kind` | `mark` |
| Parent | [`ijam`](#ijam) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النُّقْطَتَان |
| Dabt name | نَقْط الإِعْجَام — النُّقْطَتَان |
| Name by shape | نُقْطَتَان مُتَّصِلَتَان |
| Symbol | نُقْطَتَان |
| Mark family | `ijam` |
| Other spellings | `nuqtatan`, `two-dots` |

**Definition:** Two dots, above or below, distinguishing a letter from the others that share its skeleton (ijam): taa, yaa, qaaf.

**Purpose:** Used as a value of ijam, so that a letter is told apart from those sharing its skeleton in analysis and in search.

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!two-dots`

<a id="waqf_al_muanaqah"></a>

### Waqf al-Muanaqah — وقف المعانقة

<!-- source: standards/terminology/concepts/waqf_al_muanaqah.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_al_muanaqah` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | وَقْف المُعَانَقَة |
| Dabt name | وَقْف المُعَانَقَة (ويُسمَّى وَقْف المُرَاقَبَة) |
| Name by shape | ثَلَاث نُقَط تَتَكَرَّر عَلَى كَلِمَتَيْن |
| Mushaf introduction name | عَلَامَة تَعَانُق الوَقْف |
| Symbol | ثَلَاث نُقَط في مَوْضِعَيْن |
| Characters | `U+06DB` ARABIC SMALL HIGH THREE DOTS |
| Mark family | `waqf` |
| Other spellings | `muanaqah`, `muraqabah`, `taanuq_al_waqf`, `waqf_al_muraqabah` |

**Definition:** Two candidate stopping points: stopping at one makes stopping at the other not allowed.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!muanaqah`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_mustawi_al_tarafayn"></a>

### Waqf Jaiz Mustawi al-Tarafayn — الوقف الجائز مستوي الطرفين

<!-- source: standards/terminology/concepts/waqf_jaiz_mustawi_al_tarafayn.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_jaiz_mustawi_al_tarafayn` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن |
| Dabt name | الجِيم — عَلَامَة الوَقْف الجَائِز |
| Name by shape | جِيم |
| Mushaf introduction name | عَلَامَة الوَقْف الجَائِز جَوَازًا مُسْتَوِيَ الطَّرَفَيْن |
| Symbol | ج |
| Characters | `U+06DA` ARABIC SMALL HIGH JEEM |
| Mark family | `waqf` |
| Deprecated names | `waqf-jaiz`, `waqf_jaiz` |

**Definition:** A permissible stop, with stopping and continuing equally sound.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

> `waqf_jaiz` was this mark's id in the mushaf registry; it fits three permissible marks, so it is deprecated.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!waqf-jaiz`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_waqf_awla"></a>

### Waqf Jaiz Waqf Awla — الوقف الجائز مع كون الوقف أولى

<!-- source: standards/terminology/concepts/waqf_jaiz_waqf_awla.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_jaiz_waqf_awla` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف الجَائِز مَعَ كَوْنِ الوَقْف أَوْلَى |
| Dabt name | قلى — عَلَامَة الوَقْف أَوْلَى |
| Name by shape | قلى |
| Mushaf introduction name | عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَقْف أَوْلَى |
| Symbol | قلى |
| Characters | `U+06D7` ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA |
| Mark family | `waqf` |
| Other spellings | `waqf-awla`, `waqf_awla` |

**Definition:** A permissible stop, and stopping is the better choice.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!waqf-awla`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_wasl_awla"></a>

### Waqf Jaiz Wasl Awla — الوقف الجائز مع كون الوصل أولى

<!-- source: standards/terminology/concepts/waqf_jaiz_wasl_awla.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_jaiz_wasl_awla` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى |
| Dabt name | صلى — عَلَامَة الوَصْل أَوْلَى |
| Name by shape | صلى |
| Mushaf introduction name | عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَصْل أَوْلَى |
| Symbol | صلى |
| Characters | `U+06D6` ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA |
| Mark family | `waqf` |
| Other spellings | `wasl-awla`, `wasl_awla` |

**Definition:** A permissible stop, but continuing is the better choice.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!wasl-awla`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_lazim"></a>

### Waqf Lazim — الوقف اللازم

<!-- source: standards/terminology/concepts/waqf_lazim.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_lazim` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف اللَّازِم |
| Dabt name | المِيم — عَلَامَة الوَقْف اللَّازِم |
| Name by shape | مِيم |
| Mushaf introduction name | عَلَامَة الوَقْف اللَّازِم |
| Symbol | م |
| Characters | `U+06D8` ARABIC SMALL HIGH MEEM INITIAL FORM |
| Mark family | `waqf` |
| Other spellings | `waqf-lazim` |

**Definition:** A compulsory stop: continuing across it would suggest a meaning other than the one intended.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!waqf-lazim`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/122) — `122`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_mamnu"></a>

### Waqf Mamnu — الوقف الممنوع

<!-- source: standards/terminology/concepts/waqf_mamnu.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_mamnu` |
| `kind` | `classification_value` |
| Parent | [`waqf_mark_type`](#waqf_mark_type) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف المَمْنُوع |
| Dabt name | لا — عَلَامَة الوَقْف المَمْنُوع |
| Name by shape | لا |
| Symbol | لا |
| Characters | `U+06D9` ARABIC SMALL HIGH LAM ALEF |
| Mark family | `waqf` |
| Other spellings | `waqf-mamnu` |

**Definition:** A forbidden stop: stopping here would break the meaning or attach what follows to the wrong clause.

**Purpose:** Used as a value of the waqf mark type, so that rendering, teaching and warnings in applications branch on it rather than on the shape of the sign.

> Registered in the mushaf registry but never used in this edition: zero occurrences.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark)

**Sources:**

- مصحف حفص — كلمة كلمة — `standard!waqf-mamnu`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_mark"></a>

### Waqf Mark — علامة الوقف

<!-- source: standards/terminology/concepts/waqf_mark.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_mark` |
| `plural` | `waqf_marks` |
| `kind` | `mark` |
| Parent | [`mushaf_mark`](#mushaf_mark) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَلَامَة الوَقْف |

**Definition:** A mark in the mushaf pointing the reader to the ruling on stopping or continuing at a given place.

**Purpose:** Used to represent the sign, its position and its type in an orderly way.

**Related:** [`waqf`](#waqf), [`waqf_mark_type`](#waqf_mark_type), [`mushaf_mark`](#mushaf_mark), [`sabab_al_waqf`](#sabab_al_waqf), [`waqf_al_muanaqah`](#waqf_al_muanaqah), [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn), [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla), [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla), [`waqf_lazim`](#waqf_lazim), [`waqf_mamnu`](#waqf_mamnu)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

## Ayah numbering — `ayah_numbering`

<a id="ayah_count"></a>

### Ayah Count — عدد الآيات

<!-- source: standards/terminology/concepts/ayah_count.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_count` |
| `plural` | `ayah_counts` |
| `kind` | `property` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | عَدَد الآيَات |
| Registry | [`ayah_counts`](/guidelines/en/03-terminology/registries/#ayah_counts) |
| Other spellings | `ayat_count`, `number_of_ayahs`, `adad_al_ayat`, `adad_al_ay` |
| English gloss | `verse count` |

**Definition:** The number of ayahs in a surah under a given numbering system; it may differ from one system to another as the counted fasilahs differ.

**Purpose:** Used to check references and surah boundaries and to build indexes; it is read from the registry of counts, not computed from one text.

- The count belongs to the surah under a numbering system, not to the mushaf.

> The code name follows `ayah_numbering_*` and the registry's name, not a derivation of «عَدَد الآيَات»; the concept is one of modelling, though the count of ayahs has its origin in the science of counting.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`surah`](#surah), [`ayah`](#ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_basri"></a>

### Basri Numbering — العد البصري

<!-- source: standards/terminology/concepts/ayah_numbering_basri.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_basri` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ البَصْرِيّ |
| Other spellings | `basri_numbering`, `basran_numbering`, `basri` |

**Definition:** The Basran numbering system, transmitted from Asim al-Jahdari and the Basran authorities before him.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_dimashqi"></a>

### Dimashqi Numbering — العد الدمشقي

<!-- source: standards/terminology/concepts/ayah_numbering_dimashqi.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_dimashqi` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ الدِّمَشْقِيّ |
| Other spellings | `dimashqi_numbering`, `shami`, `shami_numbering`, `damascene_numbering`, `dimashqi` |
| Display evidence | GitHub phrase search: dimashqi numbering 0 vs shami numbering 0. No form is established, so the display follows the code; `shami` stays an alias. |

**Definition:** The Damascene numbering system, transmitted from Yahya ibn al-Harith al-Dhimari from Ibn Amir; also called the Shami numbering.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/82`

<a id="ayah_numbering_kufi"></a>

### Kufi Numbering — العد الكوفي

<!-- source: standards/terminology/concepts/ayah_numbering_kufi.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_kufi` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ الكُوفِيّ |
| Other spellings | `kufi_numbering`, `kufan_numbering`, `kufi` |

**Definition:** The Kufan numbering system, transmitted from Hamzah al-Zayyat from Ibn Abi Layla from Abu Abd al-Rahman al-Sulami from Ali ibn Abi Talib. It is the numbering most printed mushafs follow today.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_madani_akhir"></a>

### Madani Akhir Numbering — العد المدني الأخير

<!-- source: standards/terminology/concepts/ayah_numbering_madani_akhir.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_madani_akhir` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ المَدَنِيّ الأَخِير |
| Other spellings | `madani_akhir`, `last_madani`, `madani_last` |

**Definition:** The later Madinan numbering system, that of Ismail ibn Jafar from Sulayman ibn Jammaz.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_madani_awwal"></a>

### Madani Awwal Numbering — العد المدني الأول

<!-- source: standards/terminology/concepts/ayah_numbering_madani_awwal.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_madani_awwal` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ المَدَنِيّ الأَوَّل |
| Other spellings | `madani_awwal`, `first_madani`, `madani_first` |

**Definition:** The earlier Madinan numbering system, that of Abu Jafar Yazid ibn al-Qaqa and Shaybah ibn Nassah.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_makki"></a>

### Makki Numbering — العد المكي

<!-- source: standards/terminology/concepts/ayah_numbering_makki.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_makki` |
| `kind` | `classification_value` |
| Parent | [`ayah_numbering_system`](#ayah_numbering_system) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | العَدّ المَكِّيّ |
| Other spellings | `makki_numbering`, `meccan_numbering` |

**Definition:** The Makkan numbering system, transmitted from Ibn Kathir from Mujahid from Ibn Abbas from Ubayy ibn Kab.

**Purpose:** Used as a value of the ayah numbering system, so that a mushaf or dataset states which numbering its ayah numbers and boundaries follow, and positions can be mapped between systems.

> The code name here is the name of the school and what distinguishes the value, not a derivation of the Arabic name: deriving from «العَدّ» gives `add`, an English verb, and `makki` is already a value of `revelation_classification`. The reasoning is in the decision record.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_system"></a>

### Ayah Numbering System — نظام عد الآي

<!-- source: standards/terminology/concepts/ayah_numbering_system.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_numbering_system` |
| `plural` | `ayah_numbering_systems` |
| `kind` | `classification` |
| Values | [`ayah_numbering_basri`](#ayah_numbering_basri), [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi), [`ayah_numbering_kufi`](#ayah_numbering_kufi), [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir), [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal), [`ayah_numbering_makki`](#ayah_numbering_makki) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | نِظَام عَدّ الآي |
| Registry | [`ayah_numbering`](/guidelines/en/03-terminology/registries/#ayah_numbering) |
| Other spellings | `ayah_counting_system` |

**Definition:** A system that fixes the boundaries of the ayahs, their totals and their numbers, and certain questions about the basmalah, as transmitted by one of the schools of ayah counting.

**Purpose:** Used to state which numbering system a mushaf's or a dataset's ayah numbers and boundaries follow.

**Related:** [`ayah`](#ayah), [`equivalent_ayah`](#equivalent_ayah), [`basmalah`](#basmalah), [`ayah_count`](#ayah_count), [`ayah_numbering_kufi`](#ayah_numbering_kufi), [`ayah_numbering_basri`](#ayah_numbering_basri), [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi), [`ayah_numbering_makki`](#ayah_numbering_makki), [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal), [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir), [`ayah_key`](#ayah_key), [`ayah_mark`](#ayah_mark), [`qiraah`](#qiraah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/31) — `31`
- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/225`

<a id="equivalent_ayah"></a>

### Equivalent Ayah — الآية المقابلة

<!-- source: standards/terminology/concepts/equivalent_ayah.yml -->

| field | value |
| --- | --- |
| `code` | `equivalent_ayah` |
| `plural` | `equivalent_ayahs` |
| `kind` | `concept` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الآيَة المُقَابِلَة |

**Definition:** The ayah in one numbering system that corresponds to an ayah in another. Their numbers may differ, because the systems divide the text at different points.

**Purpose:** Used to map ayah numbers across numbering systems, so that data built on one system is never compared with data built on another by number alone.

- This is a correspondence between two numbering systems, not a similarity of wording or a repetition of text.

**Related:** [`ayah_numbering_system`](#ayah_numbering_system), [`ayah`](#ayah), [`mutashabihat`](#mutashabihat), [`ayah_numbering_basri`](#ayah_numbering_basri), [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi), [`ayah_numbering_kufi`](#ayah_numbering_kufi), [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir), [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal), [`ayah_numbering_makki`](#ayah_numbering_makki)

**Sources:**

- [qiraat-ayah-map](https://github.com/quranpedia/qiraat-ayah-map)

## Revelation — `revelation`

<a id="asbab_al_nuzul"></a>

### Asbab al-Nuzul — أسباب النزول

<!-- source: standards/terminology/concepts/asbab_al_nuzul.yml -->

| field | value |
| --- | --- |
| `code` | `asbab_al_nuzul` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | أَسْبَاب النُّزُول |
| Other spellings | `asbab_al-nozool`, `asbab_un-nuzul` |

**Definition:** The events or questions that an ayah, or several ayahs, was revealed to address or to rule on.

**Purpose:** Used to attach the narrations and the material about an ayah's occasion of revelation to the ayah itself.

**Related:** [`nuzul`](#nuzul), [`ayah`](#ayah), [`sabab_al_tasmiyah`](#sabab_al_tasmiyah), [`naskh`](#naskh)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/75`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/107`

<a id="disputed"></a>

### Disputed — مختلف فيه

<!-- source: standards/terminology/concepts/disputed.yml -->

| field | value |
| --- | --- |
| `code` | `disputed` |
| `kind` | `classification_value` |
| Parent | [`revelation_classification`](#revelation_classification) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مُخْتَلَف فِيه |
| Other spellings | `mukhtalaf_fih`, `revelation_disputed` |

**Definition:** A surah or ayah that the accepted sources do not agree to classify as makki or madani.

**Purpose:** Keeps disputed data from being forced into `makki` or `madani` without recording the disagreement.

**Related:** [`revelation_classification`](#revelation_classification), [`makki`](#makki), [`madani`](#madani)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="madani"></a>

### Madani — مدني

<!-- source: standards/terminology/concepts/madani.yml -->

| field | value |
| --- | --- |
| `code` | `madani` |
| `kind` | `classification_value` |
| Parent | [`revelation_classification`](#revelation_classification) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَدَنِيّ |
| Other spellings | `madaniyy`, `madinan` |
| English gloss | `Medinan` |

**Definition:** The part of the Quran revealed after the Hijrah, even where it was revealed outside Madinah.

**Purpose:** Used as a value of revelation classification, tagging a surah or an ayah with it.

- Madani describes the time of revelation, after the Hijrah, not the place of revelation.

**Related:** [`makki`](#makki), [`revelation_classification`](#revelation_classification), [`nuzul`](#nuzul), [`disputed`](#disputed)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="makki"></a>

### Makki — مكي

<!-- source: standards/terminology/concepts/makki.yml -->

| field | value |
| --- | --- |
| `code` | `makki` |
| `kind` | `classification_value` |
| Parent | [`revelation_classification`](#revelation_classification) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَكِّيّ |
| Transliteration | makkī |
| Other spellings | `makkiyy`, `makkan` |
| English gloss | `Meccan` |

**Definition:** The part of the Quran revealed before the Hijrah, even where it was revealed outside Makkah.

**Purpose:** Used as a value of revelation classification, tagging a surah or an ayah with it.

- Makki describes the time of revelation, before the Hijrah, not the place of revelation.

**Related:** [`madani`](#madani), [`revelation_classification`](#revelation_classification), [`nuzul`](#nuzul), [`disputed`](#disputed)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="nuzul"></a>

### Nuzul — النزول

<!-- source: standards/terminology/concepts/nuzul.yml -->

| field | value |
| --- | --- |
| `code` | `nuzul` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النُّزُول |
| English gloss | `Revelation` |

**Definition:** The revelation of the Quran to the Prophet, peace be upon him, in stages over the years of his mission, as events and needs arose.

**Purpose:** Used as the root that the order of revelation, its classification and its occasions branch from: all three are properties of the event of revelation and are known only through it.

- Revelation is an event; its order, its classification and its occasion are properties of it, not synonyms for it.

**Related:** [`revelation_order`](#revelation_order), [`revelation_classification`](#revelation_classification), [`asbab_al_nuzul`](#asbab_al_nuzul), [`madani`](#madani), [`makki`](#makki)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/100`

<a id="revelation_classification"></a>

### Revelation Classification — تصنيف النزول

<!-- source: standards/terminology/concepts/revelation_classification.yml -->

| field | value |
| --- | --- |
| `code` | `revelation_classification` |
| `kind` | `classification` |
| Values | [`disputed`](#disputed), [`madani`](#madani), [`makki`](#makki) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَصْنِيف النُّزُول |

**Definition:** A classification of the Quranic text by whether its revelation fell before or after the Hijrah, in the accepted usage.

**Purpose:** Used to classify surahs or ayahs by their relation to the Hijrah, without implying that the classification is only geographical.

**Related:** [`makki`](#makki), [`madani`](#madani), [`disputed`](#disputed), [`nuzul`](#nuzul), [`surah`](#surah)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="revelation_order"></a>

### Revelation Order — ترتيب النزول

<!-- source: standards/terminology/concepts/revelation_order.yml -->

| field | value |
| --- | --- |
| `code` | `revelation_order` |
| `kind` | `property` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَرْتِيب النُّزُول |

**Definition:** The order of the surahs or the ayahs by the time of their revelation, which may differ from one accepted source to another.

**Purpose:** Used to store the order of revelation independently of the order of the mushaf.

- Revelation order is not mushaf order: `surah_number` is the mushaf order.

**Related:** [`nuzul`](#nuzul), [`surah`](#surah), [`tartib_al_mushaf`](#tartib_al_mushaf)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/93`

## Qiraat — `qiraat`

<a id="farsh"></a>

### Farsh — الفرش

<!-- source: standards/terminology/concepts/farsh.yml -->

| field | value |
| --- | --- |
| `code` | `farsh` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الفَرْش |
| Other spellings | `farsh_al_huruf`, `farshiyyah`, `farshiyyat` |
| English gloss | `word-specific differences` |

**Definition:** The words the readers differ on at particular places in the surahs, where the difference follows no general rule but each place is named on its own, arranged by surah.

**Purpose:** Used to tag the differences between qiraat that are stored word by word at their place, as against the usul, which are stored as a rule and applied wherever their condition holds.

- Farsh and usul are the two divisions of the differences between qiraat; a wajh is what is permitted within one riwayah.

**Related:** [`usul`](#usul), [`qiraah`](#qiraah), [`wajh`](#wajh)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `2/206`

<a id="muqri"></a>

### Muqri — المقرئ

<!-- source: standards/terminology/concepts/muqri.yml -->

| field | value |
| --- | --- |
| `code` | `muqri` |
| `plural` | `muqris` |
| `kind` | `role` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المُقْرِئ |
| Other spellings | `muqree` |

**Definition:** One who has received the recitation, mastered it, and transmits it to learners.

**Purpose:** Used to represent the role of teaching, receiving and granting the recitation, which is distinct from being a `reciter`.

**Related:** [`reciter`](#reciter), [`rawi`](#rawi), [`qiraah`](#qiraah)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/268`

<a id="qiraah"></a>

### Qiraah — القراءة

<!-- source: standards/terminology/concepts/qiraah.yml -->

| field | value |
| --- | --- |
| `code` | `qiraah` |
| `plural` | `qiraahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | القِرَاءَة |
| Registry | [`qiraat`](/guidelines/en/03-terminology/registries/#qiraat) |
| Other spellings | `qira'ah`, `qiraa`, `qiraat`, `qira'at` |
| English gloss | `Reading` |

**Definition:** One of the ways of reciting the Quran, attributed to one of the imams of the qiraat, from which the riwayahs and tariqs branch.

**Purpose:** Represents the top level of the qiraat model and ties together the riwayahs, the tariqs and the texts bound to them.

**Related:** [`riwayah`](#riwayah), [`rawi`](#rawi), [`tariq`](#tariq), [`muqri`](#muqri), [`ayah_numbering_system`](#ayah_numbering_system), [`farsh`](#farsh), [`qiraah_mark`](#qiraah_mark), [`usul`](#usul)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`

<a id="rawi"></a>

### Rawi — الراوي

<!-- source: standards/terminology/concepts/rawi.yml -->

| field | value |
| --- | --- |
| `code` | `rawi` |
| `plural` | `rawis` |
| `kind` | `role` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرَّاوِي |
| Registry | [`qiraat`](/guidelines/en/03-terminology/registries/#qiraat) |
| English gloss | `Transmitter` |

**Definition:** One to whom a transmission from an imam of a qiraah is attributed.

**Purpose:** Used to represent the person a `riwayah` is bound to.

- A rawi is the transmitter a riwayah is attributed to; a reciter is the performer of a recording. A performer is not a rawi merely because they recite in his riwayah.

**Related:** [`riwayah`](#riwayah), [`qiraah`](#qiraah), [`reciter`](#reciter), [`muqri`](#muqri)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`

<a id="riwayah"></a>

### Riwayah — الرواية

<!-- source: standards/terminology/concepts/riwayah.yml -->

| field | value |
| --- | --- |
| `code` | `riwayah` |
| `plural` | `riwayahs` |
| `kind` | `concept` |
| Part of | [`qiraah`](#qiraah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الرِّوَايَة |
| Registry | [`qiraat`](/guidelines/en/03-terminology/registries/#qiraat) |
| Other spellings | `riwaya`, `rewaya`, `riwayat` |

**Definition:** What is attributed to a transmitter from an imam of a qiraah, such as the riwayah of Hafs from Asim.

**Purpose:** Used to state which riwayah a text, a mushaf, a recording or a dataset follows.

**Related:** [`qiraah`](#qiraah), [`rawi`](#rawi), [`tariq`](#tariq), [`recitation`](#recitation), [`mushaf_edition`](#mushaf_edition), [`wajh`](#wajh)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`

<a id="tariq"></a>

### Tariq — الطريق

<!-- source: standards/terminology/concepts/tariq.yml -->

| field | value |
| --- | --- |
| `code` | `tariq` |
| `plural` | `tariqs` |
| `kind` | `concept` |
| Part of | [`riwayah`](#riwayah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الطَّرِيق |
| Registry | [`tariq`](/guidelines/en/03-terminology/registries/#tariq) |
| Other spellings | `tareeq` |

**Definition:** A path of transmission taken from a rawi through those below him in the chain of transmission of a qiraah.

**Purpose:** Used when data needs a finer level than the riwayah to tell paths of delivery and transmission apart.

> The four named routes applications store — shatibiyyah, tayyibat_al_nashr, durrah, taysir — are in `registries/tariq.tsv`; the full enumeration, some 980 turuq of al-Nashr, is still open.

**Related:** [`riwayah`](#riwayah), [`qiraah`](#qiraah), [`wajh`](#wajh)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/146`

<a id="usul"></a>

### Usul — الأصول

<!-- source: standards/terminology/concepts/usul.yml -->

| field | value |
| --- | --- |
| `code` | `usul` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الأُصُول |
| Other spellings | `usool`, `usul_al_qiraah`, `usul_al_qiraat` |
| English gloss | `general rules` |

**Definition:** The general rules of a reading that apply to everything meeting their condition, such as madd, hamzah, imalah, idgham and the pronoun haa.

**Purpose:** Used to tag the differences between qiraat that are stored as a rule rather than a place, and applied to the text wherever their condition holds.

- Usul are the rules of a reading; farsh is its particular places.

**Related:** [`farsh`](#farsh), [`qiraah`](#qiraah), [`madd`](#madd), [`imalah`](#imalah)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/30`

<a id="wajh"></a>

### Wajh — الوجه

<!-- source: standards/terminology/concepts/wajh.yml -->

| field | value |
| --- | --- |
| `code` | `wajh` |
| `plural` | `wajhs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَجْه |
| Arabic plural | أَوْجُه |
| Other spellings | `wajh_al_ada`, `awjuh`, `wujuh`, `wajh_qiraah` |
| English gloss | `permitted variant` |

**Definition:** One of several manners of delivery, any of which may be taken within one riwayah or one tariq, such as the wajhs of madd arid li al-sukun.

**Purpose:** Used when a recording or a lesson needs to state which of the permitted wajhs was taken, without attributing the difference to a riwayah or a tariq.

- A wajh does not change what the reading is attributed to; a tariq does.

**Related:** [`tariq`](#tariq), [`riwayah`](#riwayah), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`lahn`](#lahn), [`farsh`](#farsh)

## Recitation — `recitation`

<a id="ayah_timing"></a>

### Ayah Timing

<!-- source: standards/terminology/concepts/ayah_timing.yml -->

| field | value |
| --- | --- |
| `code` | `ayah_timing` |
| `plural` | `ayah_timings` |
| `kind` | `concept` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Other spellings | `ayah_timestamp`, `recitation_timing`, `timing`, `verse_timing` |

**Definition:** A span of time in a recitation recording, given by a start and an end, corresponding to one ayah.

**Purpose:** Used to bind text to audio; following along while listening, jumping to an ayah, repeating it and clipping it all rest on it.

- A timing is a property of the recording, not of the ayah, so it differs from one recitation to another.
- Ayah-level timing is not word-level alignment.

**Related:** [`recitation`](#recitation), [`ayah`](#ayah), [`reciter`](#reciter), [`word_timing`](#word_timing)

<a id="hifz"></a>

### Hifz — الحفظ

<!-- source: standards/terminology/concepts/hifz.yml -->

| field | value |
| --- | --- |
| `code` | `hifz` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الحِفْظ |
| Other spellings | `hifdh`, `hifz_al_quran` |
| English gloss | `memorising the Quran`, `memorization`, `memorisation` |

**Definition:** Committing the Quran, in whole or in part, to memory, so that it is recited without looking in the mushaf.

**Purpose:** Used as the field of memorisation and revision tools, which attach their plans and repetitions to the ayah, the page and the mutashabihat.

- Hifz is a state of the reader and not an attribute of the text; the text is not tagged with it, only what is built for it.

**Related:** [`mutashabihat`](#mutashabihat), [`instructional_ayah_repetition`](#instructional_ayah_repetition), [`tilawah`](#tilawah), [`khatmah`](#khatmah)

<a id="istiadhah"></a>

### Istiadhah — الاستعاذة

<!-- source: standards/terminology/concepts/istiadhah.yml -->

| field | value |
| --- | --- |
| `code` | `istiadhah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الاِسْتِعَاذَة |
| Other spellings | `isti'adhah`, `istiʿādhah`, `ta'awwudh`, `istiadha`, `istiaadhah`, `taawwudh` |

**Definition:** Seeking refuge with Allah from the Shaytan before reciting the Quran.

**Purpose:** Used to represent the istiadhah, its wordings, and its position relative to the start of a recitation.

**Related:** [`basmalah`](#basmalah), [`recitation`](#recitation), [`takbir`](#takbir)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/27) — `27`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/243`

<a id="khatmah"></a>

### Khatmah — الختمة

<!-- source: standards/terminology/concepts/khatmah.yml -->

| field | value |
| --- | --- |
| `code` | `khatmah` |
| `plural` | `khatmahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الخَتْمَة |
| Other spellings | `khatma` |

**Definition:** Reading the Quran in full, from its beginning to its end.

**Purpose:** Used to track completion plans, to record that a reading was finished, and to tie sessions to the course of one khatmah.

**Related:** [`juz`](#juz), [`manzil`](#manzil), [`recitation`](#recitation), [`hifz`](#hifz), [`takbir`](#takbir)

<a id="recitation"></a>

### Recitation — تسجيل التلاوة

<!-- source: standards/terminology/concepts/recitation.yml -->

| field | value |
| --- | --- |
| `code` | `recitation` |
| `plural` | `recitations` |
| `kind` | `entity` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَسْجِيل التِّلَاوَة |

**Definition:** A published recording of a recitation of the Quran, attributed to a reciter, a riwayah and a style of delivery.

**Purpose:** Used to represent the recording that timings, style and pace are attached to; it is attributed to a reciter and a riwayah and kept apart from the act of tilawah.

- A recitation is the published recording attributed to a reciter, a riwayah and a style; tilawah is the act.

**Related:** [`reciter`](#reciter), [`riwayah`](#riwayah), [`recitation_style`](#recitation_style), [`recitation_pace`](#recitation_pace), [`ayah_timing`](#ayah_timing), [`word_timing`](#word_timing), [`tilawah`](#tilawah), [`istiadhah`](#istiadhah), [`khatmah`](#khatmah), [`spoken_translation`](#spoken_translation), [`tajwid`](#tajwid), [`takbir`](#takbir), [`tartil`](#tartil)

<a id="reciter"></a>

### Reciter — القارئ

<!-- source: standards/terminology/concepts/reciter.yml -->

| field | value |
| --- | --- |
| `code` | `reciter` |
| `plural` | `reciters` |
| `kind` | `role` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | القَارِئ |
| Other spellings | `qari`, `qaari` |

**Definition:** The person who performs a recitation of the Quran.

**Purpose:** Used to tie audio recordings to their performer.

- A reciter performs the recitation in a recording; they are neither an imam of a qiraah nor a rawi.

**Related:** [`recitation`](#recitation), [`rawi`](#rawi), [`muqri`](#muqri), [`ayah_timing`](#ayah_timing), [`tilawah`](#tilawah)

<a id="sujud_al_tilawah"></a>

### Sujud al-Tilawah — سجود التلاوة

<!-- source: standards/terminology/concepts/sujud_al_tilawah.yml -->

| field | value |
| --- | --- |
| `code` | `sujud_al_tilawah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | سُجُود التِّلَاوَة |
| Other spellings | `sajdah_al-tilawah`, `sajdat_al-tilawah` |

**Definition:** A prostration performed on reciting or hearing one of the places of sujud al-tilawah.

**Purpose:** Used to attach the rulings and manner of the prostration to its place, and to keep the act apart from the mark and the place in data.

- Sujud al-tilawah is an act; the sajdah mark is a sign in the mushaf; mawdi al-sajdah is a place in the text.

**Related:** [`mawdi_al_sajdah`](#mawdi_al_sajdah), [`sajdah_mark`](#sajdah_mark), [`tilawah`](#tilawah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="takbir"></a>

### Takbir — التكبير

<!-- source: standards/terminology/concepts/takbir.yml -->

| field | value |
| --- | --- |
| `code` | `takbir` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | التَّكْبِير |
| Other spellings | `takbeer`, `takbir_al_khatm`, `takbir_al_khatmah` |

**Definition:** Saying «الله أكبر» between the surahs from the end of al-Duha to the end of al-Nas, transmitted from the people of Makkah in the riwayah of al-Bazzi from Ibn Kathir, and done at a khatmah in other riwayahs.

**Purpose:** Used to tag the takbir between surahs in a recording, so that it is neither counted against an ayah nor lost when clipping.

- The takbir is no part of the Quran or of the surah, so it has no ayah and no ayah timing.

**Related:** [`khatmah`](#khatmah), [`recitation`](#recitation), [`basmalah`](#basmalah), [`istiadhah`](#istiadhah)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `2/405`

<a id="tartil"></a>

### Tartil — الترتيل

<!-- source: standards/terminology/concepts/tartil.yml -->

| field | value |
| --- | --- |
| `code` | `tartil` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّرْتِيل |
| Other spellings | `tarteel` |

**Definition:** Reciting the Quran deliberately, making the letters and words distinct, observing the stops and the meaning.

**Purpose:** Used as a quality of delivery in describing a recording or a lesson, not as the name of the style a recording is published under.

- Tartil is a quality of the delivery itself; murattal is a recording style. Neither name stands for the other.

**Related:** [`murattal`](#murattal), [`recitation`](#recitation), [`recitation_pace`](#recitation_pace), [`tilawah`](#tilawah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/21) — `21`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="tilawah"></a>

### Tilawah — التلاوة

<!-- source: standards/terminology/concepts/tilawah.yml -->

| field | value |
| --- | --- |
| `code` | `tilawah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التِّلَاوَة |
| Other spellings | `tilaawah`, `tilawa`, `tilawat` |

**Definition:** Reading the Quran in its wording, delivered aloud as the reader received it, whether in prayer, in a lesson or in a recording.

**Purpose:** Used for the act of reading itself where that is what is meant, as in the rulings of tilawah, its etiquette, its prostration and its teaching; the published recording of it stays `recitation`.

- Tilawah is the act; `recitation` is the published recording attributed to a reciter, a riwayah and a style of delivery.
- Tartil is an attribute of tilawah, not tilawah.

**Related:** [`recitation`](#recitation), [`tartil`](#tartil), [`sujud_al_tilawah`](#sujud_al_tilawah), [`reciter`](#reciter), [`hifz`](#hifz), [`lahn`](#lahn)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/16) — `16`

<a id="word_timing"></a>

### Word Timing

<!-- source: standards/terminology/concepts/word_timing.yml -->

| field | value |
| --- | --- |
| `code` | `word_timing` |
| `plural` | `word_timings` |
| `kind` | `concept` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Other spellings | `word_timestamp`, `word_alignment`, `word_segment_timing`, `timing_segment`, `audio_segment`, `word_timings` |

**Definition:** A span of time in a recitation recording, given by a start and an end, corresponding to one word of an ayah.

**Purpose:** Used to highlight the word being recited while listening, to align text with audio at a level finer than the ayah, and to cut a recording at a word.

- A word timing falls inside the timing of its ayah and does not cross it.
- Audio APIs call this concept `segment`; the name in this standard is `word_timing`, because in linguistic corpora `segment` names the morpheme.

**Related:** [`ayah_timing`](#ayah_timing), [`word`](#word), [`word_key`](#word_key), [`recitation`](#recitation)

## Recitation pace — `recitation_pace`

<a id="hadr"></a>

### Hadr — الحدر

<!-- source: standards/terminology/concepts/hadr.yml -->

| field | value |
| --- | --- |
| `code` | `hadr` |
| `kind` | `classification_value` |
| Parent | [`recitation_pace`](#recitation_pace) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الحَدْر |
| Other spellings | `hadar` |

**Definition:** Reciting quickly while keeping the letters, the vowels and the rules of delivery intact.

**Purpose:** Used as a value of recitation pace, so that a recording or a teaching session is tagged by its pace and filtered by it.

**Related:** [`recitation_pace`](#recitation_pace)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/24) — `24`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="recitation_pace"></a>

### Recitation Pace — مراتب القراءة

<!-- source: standards/terminology/concepts/recitation_pace.yml -->

| field | value |
| --- | --- |
| `code` | `recitation_pace` |
| `kind` | `classification` |
| Values | [`hadr`](#hadr), [`tadwir`](#tadwir), [`tahqiq`](#tahqiq) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَرَاتِب القِرَاءَة |

**Definition:** A classification of how fast a recitation is delivered while its rules are kept.

**Purpose:** Keeps the traditional paces apart from recording styles such as `murattal` and `mujawwad`.

**Related:** [`tahqiq`](#tahqiq), [`tadwir`](#tadwir), [`hadr`](#hadr), [`recitation_style`](#recitation_style), [`tartil`](#tartil), [`recitation`](#recitation)

**Sources:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="tadwir"></a>

### Tadwir — التدوير

<!-- source: standards/terminology/concepts/tadwir.yml -->

| field | value |
| --- | --- |
| `code` | `tadwir` |
| `kind` | `classification_value` |
| Parent | [`recitation_pace`](#recitation_pace) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّدْوِير |
| Other spellings | `tadweer` |

**Definition:** Reciting at a middle speed between tahqiq and hadr, while keeping the rules.

**Purpose:** Used as a value of recitation pace, so that a recording or a teaching session is tagged by its pace and filtered by it.

**Related:** [`recitation_pace`](#recitation_pace)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/25) — `25`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/207`

<a id="tahqiq"></a>

### Tahqiq — التحقيق

<!-- source: standards/terminology/concepts/tahqiq.yml -->

| field | value |
| --- | --- |
| `code` | `tahqiq` |
| `kind` | `classification_value` |
| Parent | [`recitation_pace`](#recitation_pace) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّحْقِيق |
| Other spellings | `tahqeeq` |

**Definition:** Reciting slowly and deliberately, giving the letters and their rules their full due; much used in teaching.

**Purpose:** Used as a value of recitation pace, so that a recording or a teaching session is tagged by its pace and filtered by it.

**Related:** [`recitation_pace`](#recitation_pace)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/26) — `26`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

## Recitation style — `recitation_style`

<a id="instructional_ayah_repetition"></a>

### Instructional Ayah Repetition — تكرار الآيات

<!-- source: standards/terminology/concepts/instructional_ayah_repetition.yml -->

| field | value |
| --- | --- |
| `code` | `instructional_ayah_repetition` |
| `kind` | `concept` |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَكْرَار الآيَات |

**Definition:** Repeating an ayah, or part of one, once or several times in a teaching pattern that helps the learner take it in and memorise it.

**Purpose:** Used to describe a feature of a teaching recording in its own right, rather than leaving it implied inside `muallim`.

**Related:** [`muallim`](#muallim), [`recitation_style`](#recitation_style), [`hifz`](#hifz)

<a id="muallim"></a>

### Muallim — معلم

<!-- source: standards/terminology/concepts/muallim.yml -->

| field | value |
| --- | --- |
| `code` | `muallim` |
| `kind` | `classification_value` |
| Parent | [`recitation_style`](#recitation_style) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مُعَلِّم |

**Definition:** A recitation style meant for teaching, which may repeat ayahs or leave the learner time to repeat after the reciter.

**Purpose:** Used to classify a recording by its style.

**Related:** [`recitation_style`](#recitation_style), [`instructional_ayah_repetition`](#instructional_ayah_repetition)

<a id="mujawwad"></a>

### Mujawwad — مجود

<!-- source: standards/terminology/concepts/mujawwad.yml -->

| field | value |
| --- | --- |
| `code` | `mujawwad` |
| `kind` | `classification_value` |
| Parent | [`recitation_style`](#recitation_style) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مُجَوَّد |

**Definition:** A recitation style that is slow and melodic, with the tajwid rules drawn out; the label given to recordings delivered that way.

**Purpose:** Used to classify a recording by its style.

- Mujawwad is a recording style; tajwid is the discipline every style is delivered by. Neither name stands for the other.

**Related:** [`recitation_style`](#recitation_style), [`murattal`](#murattal), [`tajwid`](#tajwid)

<a id="murattal"></a>

### Murattal — مرتل

<!-- source: standards/terminology/concepts/murattal.yml -->

| field | value |
| --- | --- |
| `code` | `murattal` |
| `kind` | `classification_value` |
| Parent | [`recitation_style`](#recitation_style) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مُرَتَّل |

**Definition:** A recitation style that is measured and unadorned, at a reading pace; the label given to recordings delivered that way.

**Purpose:** Used to classify a recording by its style.

- Murattal is a recording style; tartil is a quality of the delivery itself. Neither name stands for the other.

**Related:** [`recitation_style`](#recitation_style), [`mujawwad`](#mujawwad), [`tartil`](#tartil)

<a id="recitation_style"></a>

### Recitation Style — نمط الأداء

<!-- source: standards/terminology/concepts/recitation_style.yml -->

| field | value |
| --- | --- |
| `code` | `recitation_style` |
| `kind` | `classification` |
| Values | [`muallim`](#muallim), [`mujawwad`](#mujawwad), [`murattal`](#murattal) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | نَمَط الأَدَاء |

**Definition:** A classification of recordings and recitations by how they are delivered, murattal, mujawwad or muallim, independent of the qiraah and the riwayah.

**Purpose:** Used to classify audio recordings by their manner of delivery or by their purpose.

**Related:** [`murattal`](#murattal), [`mujawwad`](#mujawwad), [`muallim`](#muallim), [`recitation`](#recitation), [`recitation_pace`](#recitation_pace), [`instructional_ayah_repetition`](#instructional_ayah_repetition)

## Tajwid — `tajwid`

<a id="alaqat_al_harfayn"></a>

### Alaqat al-Harfayn — علاقة الحرفين

<!-- source: standards/terminology/concepts/alaqat_al_harfayn.yml -->

| field | value |
| --- | --- |
| `code` | `alaqat_al_harfayn` |
| `kind` | `classification` |
| Values | [`mutabaidan`](#mutabaidan), [`mutajanisan`](#mutajanisan), [`mutamathilan`](#mutamathilan), [`mutaqariban`](#mutaqariban) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | عَلَاقَة الحَرْفَيْن |
| Other spellings | `letter_relations`, `alaqat_al_huruf`, `ilaqat_al_harfayn` |
| English gloss | `relation of two letters` |

**Definition:** The relation of two adjacent letters to each other in point of articulation and attribute: identical, of one kind, close, or distant; the merging of the first into the second, or its clear sounding, is built on it.

**Purpose:** Used as a classification tagging the place where two letters are merged or sounded apart, so that the cause of the ruling is known and not only the ruling.

- The relation is a cause; idgham and izhar are the ruling that follows from it.

**Related:** [`idgham`](#idgham), [`izhar`](#izhar), [`makhraj`](#makhraj), [`sifat_al_huruf`](#sifat_al_huruf), [`mutamathilan`](#mutamathilan), [`mutajanisan`](#mutajanisan), [`mutaqariban`](#mutaqariban), [`mutabaidan`](#mutabaidan)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/59) — `59`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/62) — `62`

<a id="ghunnah"></a>

### Ghunnah — الغنة

<!-- source: standards/terminology/concepts/ghunnah.yml -->

| field | value |
| --- | --- |
| `code` | `ghunnah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الغُنَّة |
| Other spellings | `ghunna`, `gunnah`, `ghunnah_sound` |
| English gloss | `nasalisation` |

**Definition:** A sound from the nasal cavity built into the body of noon and meem, in which the tongue plays no part; its length differs by ruling, fullest in the doubled and the merged letter, then in the concealed, then in the vowelless letter sounded clearly.

**Purpose:** Used as an attribute tagging the places in the text where the ghunnah is held, such as the two doubled letters, idgham with ghunnah, ikhfa and iqlab, so that it is followed in colouring and instruction, and because its length is among what differs by tariq.

- Ghunnah is an attribute of sound and not a ruling in itself: it accompanies idgham, ikhfa and iqlab and does not stand opposite them.

**Related:** [`idgham`](#idgham), [`ikhfa`](#ikhfa), [`iqlab`](#iqlab), [`noon_sakinah`](#noon_sakinah), [`meem_sakinah`](#meem_sakinah), [`hukm_al_tajwid`](#hukm_al_tajwid), [`lahn_khafi`](#lahn_khafi)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/85) — `85`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `noon-mushaddadah`

<a id="hukm_al_tajwid"></a>

### Hukm al-Tajwid — حكم التجويد

<!-- source: standards/terminology/concepts/hukm_al_tajwid.yml -->

| field | value |
| --- | --- |
| `code` | `hukm_al_tajwid` |
| `plural` | `hukm_al_tajwids` |
| `kind` | `classification` |
| Values | [`idgham`](#idgham), [`ikhfa`](#ikhfa), [`iqlab`](#iqlab), [`izhar`](#izhar), [`qalqalah`](#qalqalah) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | حُكْم التَّجْوِيد |
| Arabic plural | أَحْكَام التَّجْوِيد |
| Registry | [`tajwid_rules`](/guidelines/en/03-terminology/registries/#tajwid_rules) |
| Other spellings | `hukm`, `hukum`, `ahkam_al_tajwid`, `ahkam_al_tajweed`, `tajwid_rule`, `tajweed_rule`, `tajweed_ruling` |
| English gloss | `tajwid ruling` |

**Definition:** What is due in delivering a letter before the letter that follows it, or at a sukun or a hamzah: izhar, idgham, iqlab, ikhfa, madd, qalqalah, tafkhim or tarqiq, as the rules of tajwid settle it at a given place in the text.

**Purpose:** Used as the parent of the rulings of tajwid and the holder of their registry, so that the places in the text where a ruling falls are attributed to it, and a particular ruling is named by a row of the registry rather than by a free name that differs from one engine to another.

- The ruling is what falls at the place; tajwid is the discipline that settles it.
- A ruling is not a rule: the rule is the condition, and the ruling is its effect at the place.

**Related:** [`tajwid`](#tajwid), [`izhar`](#izhar), [`idgham`](#idgham), [`iqlab`](#iqlab), [`ikhfa`](#ikhfa), [`qalqalah`](#qalqalah), [`madd`](#madd), [`ghunnah`](#ghunnah), [`tafkhim`](#tafkhim), [`tarqiq`](#tarqiq), [`noon_sakinah`](#noon_sakinah), [`meem_sakinah`](#meem_sakinah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)

<a id="idgham"></a>

### Idgham — الإدغام

<!-- source: standards/terminology/concepts/idgham.yml -->

| field | value |
| --- | --- |
| `code` | `idgham` |
| `kind` | `classification_value` |
| Parent | [`hukm_al_tajwid`](#hukm_al_tajwid) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِدْغَام |
| Other spellings | `idghaam`, `idgam`, `edgham`, `idgham_bighunnah`, `idgham_bila_ghunnah`, `idgham_shafawi` |
| English gloss | `assimilation`, `merging` |

**Definition:** Merging a vowelless letter into a vowelled letter after it so that the two become one doubled letter, whether the merging is complete or partial, with ghunnah or without it.

**Purpose:** Used as a value of the tajwid ruling, so that a place in the text is tagged with it in analysis, colouring and instruction, and its kinds branch under it in the registry of rulings.

- Idgham is a ruling; mutamathilan, mutajanisan and mutaqariban are the relation between the two letters because of which it falls.

**Related:** [`izhar`](#izhar), [`ikhfa`](#ikhfa), [`iqlab`](#iqlab), [`ghunnah`](#ghunnah), [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`mutamathilan`](#mutamathilan), [`mutajanisan`](#mutajanisan), [`mutaqariban`](#mutaqariban), [`hukm_al_tajwid`](#hukm_al_tajwid), [`meem_sakinah`](#meem_sakinah), [`mutabaidan`](#mutabaidan), [`noon_sakinah`](#noon_sakinah), [`shaddah`](#shaddah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/57) — `57`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/60) — `60`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/61) — `61`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/63) — `63`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `idgham-bi-ghunnah-noon`

<a id="ikhfa"></a>

### Ikhfa — الإخفاء

<!-- source: standards/terminology/concepts/ikhfa.yml -->

| field | value |
| --- | --- |
| `code` | `ikhfa` |
| `kind` | `classification_value` |
| Parent | [`hukm_al_tajwid`](#hukm_al_tajwid) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِخْفَاء |
| Other spellings | `ikhfaa`, `ikhfa'`, `ekhfa`, `ikhfa_haqiqi`, `ikhfa_shafawi` |
| English gloss | `concealment` |

**Definition:** Pronouncing a vowelless letter in a manner between izhar and idgham, without doubling and with the ghunnah kept: haqiqi in noon sakinah and tanwin before its 15 letters, and shafawi in meem sakinah before a baa.

**Purpose:** Used as a value of the tajwid ruling, so that a place in the text is tagged with it in analysis, colouring and instruction, and its kinds branch under it in the registry of rulings.

**Related:** [`izhar`](#izhar), [`idgham`](#idgham), [`ghunnah`](#ghunnah), [`noon_sakinah`](#noon_sakinah), [`meem_sakinah`](#meem_sakinah), [`hukm_al_tajwid`](#hukm_al_tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/67) — `67`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/68) — `68`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `ikhfa-haqiqi-noon`

<a id="iqlab"></a>

### Iqlab — الإقلاب

<!-- source: standards/terminology/concepts/iqlab.yml -->

| field | value |
| --- | --- |
| `code` | `iqlab` |
| `kind` | `classification_value` |
| Parent | [`hukm_al_tajwid`](#hukm_al_tajwid) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِقْلَاب |
| Other spellings | `iqlaab`, `qalb`, `iqlab_qalb`, `eqlab` |
| English gloss | `conversion` |

**Definition:** Turning noon sakinah or tanwin into a meem, concealed with ghunnah, before a baa.

**Purpose:** Used as a value of the tajwid ruling, so that a place in the text is tagged with it in analysis, colouring and instruction, and its kinds branch under it in the registry of rulings.

- Iqlab is a ruling of pronunciation; the small meem is the mark the mushaf draws it with.

**Related:** [`noon_sakinah`](#noon_sakinah), [`tanwin`](#tanwin), [`ghunnah`](#ghunnah), [`small_meem`](#small_meem), [`hukm_al_tajwid`](#hukm_al_tajwid), [`idgham`](#idgham), [`izhar`](#izhar)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `iqlab-noon`

<a id="izhar"></a>

### Izhar — الإظهار

<!-- source: standards/terminology/concepts/izhar.yml -->

| field | value |
| --- | --- |
| `code` | `izhar` |
| `kind` | `classification_value` |
| Parent | [`hukm_al_tajwid`](#hukm_al_tajwid) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِظْهَار |
| Other spellings | `izhaar`, `idhhar`, `idhar`, `ithhar`, `izhar_halqi`, `izhar_shafawi` |
| English gloss | `clear pronunciation` |

**Definition:** Sounding a vowelless letter from its point of articulation with no added ghunnah, as noon sakinah and tanwin are sounded before the throat letters, and meem sakinah before any letter other than baa and meem.

**Purpose:** Used as a value of the tajwid ruling, so that a place in the text is tagged with it in analysis, colouring and instruction, and its kinds branch under it in the registry of rulings.

- Izhar is a ruling standing opposite idgham and ikhfa, not the absence of a ruling: a place tagged with it is one where a cause was present and neither idgham nor ikhfa fell.

**Related:** [`idgham`](#idgham), [`ikhfa`](#ikhfa), [`iqlab`](#iqlab), [`noon_sakinah`](#noon_sakinah), [`meem_sakinah`](#meem_sakinah), [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`hukm_al_tajwid`](#hukm_al_tajwid), [`mutabaidan`](#mutabaidan), [`mutajanisan`](#mutajanisan), [`mutamathilan`](#mutamathilan), [`mutaqariban`](#mutaqariban)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/64) — `64`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/65) — `65`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-halqi-noon`

<a id="lahn"></a>

### Lahn — اللحن

<!-- source: standards/terminology/concepts/lahn.yml -->

| field | value |
| --- | --- |
| `code` | `lahn` |
| `kind` | `classification` |
| Values | [`lahn_jali`](#lahn_jali), [`lahn_khafi`](#lahn_khafi) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | اللَّحْن |
| Other spellings | `lahn_error`, `tajwid_error` |
| English gloss | `recitation error` |

**Definition:** Error in reciting the Quran and departure from what is correct, whether plain or subtle.

**Purpose:** Used as a classification of what recitation-assessment tools report, separating what damages the form or the meaning from what damages the perfection of delivery.

- Lahn is an error in delivery; a wajh is a permitted variation in it.

**Related:** [`lahn_jali`](#lahn_jali), [`lahn_khafi`](#lahn_khafi), [`tajwid`](#tajwid), [`tilawah`](#tilawah), [`wajh`](#wajh)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/8) — `8`

<a id="lahn_jali"></a>

### Lahn Jali — اللحن الجلي

<!-- source: standards/terminology/concepts/lahn_jali.yml -->

| field | value |
| --- | --- |
| `code` | `lahn_jali` |
| `kind` | `classification_value` |
| Parent | [`lahn`](#lahn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | اللَّحْن الجَلِيّ |
| Other spellings | `lahn_jaliy`, `lahn_jalee`, `clear_error` |
| English gloss | `plain error` |

**Definition:** An error in the wording that damages its form or its meaning, such as one letter put for another or one vowel for another; the learned and the unlearned alike notice it.

**Purpose:** Used as a value of lahn, so that assessment reports single out the error every reciter must correct.

**Related:** [`lahn`](#lahn), [`lahn_khafi`](#lahn_khafi)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/9) — `9`

<a id="lahn_khafi"></a>

### Lahn Khafi — اللحن الخفي

<!-- source: standards/terminology/concepts/lahn_khafi.yml -->

| field | value |
| --- | --- |
| `code` | `lahn_khafi` |
| `kind` | `classification_value` |
| Parent | [`lahn`](#lahn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | اللَّحْن الخَفِيّ |
| Other spellings | `lahn_khafiy`, `lahn_khafee` |
| English gloss | `subtle error` |

**Definition:** An error in the wording that damages the perfection of delivery without touching form or meaning, such as dropping the ghunnah or shortening a madd; only those trained in the discipline notice it.

**Purpose:** Used as a value of lahn, so that assessment reports keep what concerns mastery of tajwid apart from what concerns the correctness of the wording.

**Related:** [`lahn`](#lahn), [`lahn_jali`](#lahn_jali), [`ghunnah`](#ghunnah), [`madd`](#madd)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/10) — `10`

<a id="madd"></a>

### Madd — المد

<!-- source: standards/terminology/concepts/madd.yml -->

| field | value |
| --- | --- |
| `code` | `madd` |
| `kind` | `classification` |
| Values | [`madd_al_badal`](#madd_al_badal), [`madd_al_iwad`](#madd_al_iwad), [`madd_al_lin`](#madd_al_lin), [`madd_al_silah`](#madd_al_silah), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`madd_lazim`](#madd_lazim), [`madd_munfasil`](#madd_munfasil), [`madd_muttasil`](#madd_muttasil), [`madd_tabii`](#madd_tabii) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ |
| Arabic plural | مدود |
| Other spellings | `mad`, `madd_rule`, `mudud`, `mudood`, `madd_type` |
| English gloss | `prolongation`, `lengthening` |

**Definition:** Prolonging the sound on one of the three letters of madd: a vowelless alif after a fathah, a vowelless waw after a dammah, a vowelless yaa after a kasrah; whether the madd is original, without which the letter does not stand, or secondary, caused by a hamzah or a sukun.

**Purpose:** Used as a classification that the kinds of madd branch from, so that a place in the text is tagged with its kind and its length; and because the lengths of the madds are among what differs by tariq, they are part of describing a recording or a mushaf.

- The letters of madd are not the letters of lin, though waw and yaa belong to both: a letter of madd is vowelless after the vowel of its own kind, a letter of lin is vowelless after a fathah.
- Madd is the ruling; the maddah is the mark that points to it in the mushaf.

**Related:** [`maddah`](#maddah), [`madd_tabii`](#madd_tabii), [`madd_muttasil`](#madd_muttasil), [`madd_munfasil`](#madd_munfasil), [`madd_lazim`](#madd_lazim), [`madd_al_badal`](#madd_al_badal), [`madd_al_iwad`](#madd_al_iwad), [`madd_al_silah`](#madd_al_silah), [`madd_al_lin`](#madd_al_lin), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`hukm_al_tajwid`](#hukm_al_tajwid), [`lahn_khafi`](#lahn_khafi), [`usul`](#usul)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/90) — `90`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/92) — `92`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/99) — `99`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/107) — `107`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/108) — `108`

<a id="madd_al_badal"></a>

### Madd al-Badal — مد البدل

<!-- source: standards/terminology/concepts/madd_al_badal.yml -->

| field | value |
| --- | --- |
| `code` | `madd_al_badal` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَدّ البَدَل |
| Other spellings | `madd_badal`, `badal`, `mad_badal` |
| English gloss | `substitution madd` |

**Definition:** A madd caused by a hamzah before the letter of madd, where the letter of madd was substituted for a vowelless hamzah, as in «آمن», «أوتوا» and «إيمان»; its length is 2 counts for Hafs, more for Warsh.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`hamzah`](#hamzah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/98) — `98`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-badal`

<a id="madd_al_iwad"></a>

### Madd al-Iwad — مد العوض

<!-- source: standards/terminology/concepts/madd_al_iwad.yml -->

| field | value |
| --- | --- |
| `code` | `madd_al_iwad` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَدّ العِوَض |
| Other spellings | `madd_iwad`, `madd_al_ewad`, `madd_ewad`, `iwad`, `mad_iwad` |
| English gloss | `compensation madd` |

**Definition:** Lengthening an alif in place of tanwin al-fath when stopping on the word; its length is 2 counts.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`tanwin_al_fath`](#tanwin_al_fath), [`waqf`](#waqf), [`madd_tabii`](#madd_tabii)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/105) — `105`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-iwad`

<a id="madd_al_lin"></a>

### Madd al-Lin — مد اللين

<!-- source: standards/terminology/concepts/madd_al_lin.yml -->

| field | value |
| --- | --- |
| `code` | `madd_al_lin` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَدّ اللِّين |
| Other spellings | `madd_lin`, `madd_leen`, `madd_al_leen`, `lin`, `leen`, `mad_leen` |
| English gloss | `soft madd` |

**Definition:** Lengthening a vowelless waw or yaa preceded by a fathah when stopping on the word with an incidental sukun, as in «خوف» and «بيت».

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/106) — `106`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/93) — `93`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `leen-waw`

<a id="madd_al_silah"></a>

### Madd al-Silah — مد الصلة

<!-- source: standards/terminology/concepts/madd_al_silah.yml -->

| field | value |
| --- | --- |
| `code` | `madd_al_silah` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | مَدّ الصِّلَة |
| Other spellings | `madd_silah`, `silah`, `madd_al_sila`, `madd_silah_sughra`, `madd_silah_kubra`, `mad_silah` |
| English gloss | `pronoun madd` |

**Definition:** A madd arising from joining the pronoun haa to a waw or a yaa when it falls between two vowelled letters; sughra when no hamzah follows, kubra when one does.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`small_waw`](#small_waw), [`small_yaa`](#small_yaa), [`madd_tabii`](#madd_tabii)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/97) — `97`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/96) — `96`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/95) — `95`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-silah-sughra`

<a id="madd_arid_li_al_sukun"></a>

### Madd Arid lil-Sukun — المد العارض للسكون

<!-- source: standards/terminology/concepts/madd_arid_li_al_sukun.yml -->

| field | value |
| --- | --- |
| `code` | `madd_arid_li_al_sukun` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ العَارِض لِلسُّكُون |
| Other spellings | `madd_arid_lilsukun`, `madd_arid_lil_sukun`, `madd_arid`, `arid_lil_sukun`, `madd_aarid`, `madd_arid_lissukun` |
| English gloss | `incidental madd` |
| Display evidence | No dominant English form; «lil-Sukun» is how the phrase is written in English tajwid teaching, and the hyphenated preposition follows the display rule for the article. |

**Definition:** A madd caused by an incidental sukun in stopping after the letter of madd; shortening, middle length and full length are all permitted in it.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

> The derivation gives `madd_arid_li_al_sukun`, separating the preposition from the article as section 8 requires; the fused form `lilsukun` resolves through `alternative_spellings`.

**Related:** [`madd`](#madd), [`madd_al_lin`](#madd_al_lin), [`waqf`](#waqf), [`wajh`](#wajh)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/109) — `109`

<a id="madd_lazim"></a>

### Madd Lazim — المد اللازم

<!-- source: standards/terminology/concepts/madd_lazim.yml -->

| field | value |
| --- | --- |
| `code` | `madd_lazim` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ اللَّازِم |
| Other spellings | `madd_laazim`, `lazim`, `madd_lazim_kalimi`, `madd_lazim_harfi`, `mad_lazim` |
| English gloss | `necessary madd` |

**Definition:** A secondary madd caused by an original sukun, fixed in continuing and in stopping, after the letter of madd, in a word or in a letter of the surah openings, whether heavy with idgham or light; its length is 6 counts.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`huruf_muqattaah`](#huruf_muqattaah), [`sukun`](#sukun)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/103) — `103`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/110) — `110`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/111) — `111`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/112) — `112`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-lazim-harfi`

<a id="madd_munfasil"></a>

### Madd Munfasil — المد المنفصل

<!-- source: standards/terminology/concepts/madd_munfasil.yml -->

| field | value |
| --- | --- |
| `code` | `madd_munfasil` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ المُنْفَصِل |
| Other spellings | `madd_jaiz_munfasil`, `munfasil`, `madd_munfasil_jaiz`, `mad_munfasil` |
| English gloss | `separated madd` |

**Definition:** A secondary madd caused by a hamzah at the start of the word following the letter of madd; it is permissible, shortened or lengthened by riwayah and tariq.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`madd_muttasil`](#madd_muttasil), [`hamzah`](#hamzah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/102) — `102`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-munfasil`

<a id="madd_muttasil"></a>

### Madd Muttasil — المد المتصل

<!-- source: standards/terminology/concepts/madd_muttasil.yml -->

| field | value |
| --- | --- |
| `code` | `madd_muttasil` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ المُتَّصِل |
| Other spellings | `madd_wajib_muttasil`, `muttasil`, `madd_muttasil_wajib`, `mad_muttasil`, `madd_mutasil` |
| English gloss | `connected madd` |

**Definition:** A secondary madd caused by a hamzah after the letter of madd within one word; it is obligatory for all the readers, and its lengths differ by riwayah and tariq.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`madd_munfasil`](#madd_munfasil), [`hamzah`](#hamzah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/101) — `101`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-muttasil`

<a id="madd_tabii"></a>

### Madd Tabee — المد الطبيعي

<!-- source: standards/terminology/concepts/madd_tabii.yml -->

| field | value |
| --- | --- |
| `code` | `madd_tabii` |
| `kind` | `classification_value` |
| Parent | [`madd`](#madd) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المَدّ الطَّبِيعِيّ |
| Other spellings | `madd_tabee`, `madd_tabi'i`, `madd_tabiee`, `madd_asli` |
| English gloss | `natural madd` |
| Display evidence | GitHub phrase search: madd tabee 111 vs madd tabii 63. The display follows the dominant English form; the code stays derived. |

**Definition:** The madd without which the letter of madd itself does not stand, depending on no cause of hamzah or sukun; its length is 2 counts.

**Purpose:** Used as a value of madd, so that a place in the text is tagged with it and with its length, and what differs by tariq is read from it in describing a recording or a mushaf.

**Related:** [`madd`](#madd), [`madd_al_iwad`](#madd_al_iwad), [`madd_al_silah`](#madd_al_silah)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/100) — `100`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-tabee-kalimi`

<a id="makhraj"></a>

### Makhraj — المخرج

<!-- source: standards/terminology/concepts/makhraj.yml -->

| field | value |
| --- | --- |
| `code` | `makhraj` |
| `plural` | `makhrajs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المَخْرَج |
| Arabic plural | مخارج |
| Other spellings | `makhraj_al_harf`, `makharij`, `makhaarij` |
| English gloss | `point of articulation` |

**Definition:** The place a letter issues from and is distinguished by: the oral cavity, the throat, the tongue, the lips or the nasal cavity.

**Purpose:** Used in instruction and in the analysis of pronunciation, and to settle the relation between two adjacent letters that idgham is built on.

**Related:** [`sifat_al_huruf`](#sifat_al_huruf), [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`letter`](#letter)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/6) — `6`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/40) — `40`

<a id="meem_sakinah"></a>

### Meem Sakinah — الميم الساكنة

<!-- source: standards/terminology/concepts/meem_sakinah.yml -->

| field | value |
| --- | --- |
| `code` | `meem_sakinah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المِيم السَّاكِنَة |
| Other spellings | `mim_sakinah`, `meem_saakinah`, `meem_sakina` |
| English gloss | `unvowelled meem` |
| Display evidence | tools/display_measurements.json: meem sakinah 308 vs mim sakinah 57. Letter names are written as they are said, so the derivation gives meem. |

**Definition:** A meem carrying no vowel, fixed in pronunciation and in writing, falling in the middle of a word or at its end.

**Purpose:** Used as the trigger of the three labial rulings, idgham, ikhfa and izhar, in tajwid engines.

- Meem sakinah is not the meem that noon turns into in iqlab, though the two sound the same.

**Related:** [`noon_sakinah`](#noon_sakinah), [`izhar`](#izhar), [`idgham`](#idgham), [`ikhfa`](#ikhfa), [`ghunnah`](#ghunnah), [`hukm_al_tajwid`](#hukm_al_tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/63) — `63`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/68) — `68`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-shafawi-meem`

<a id="mutabaidan"></a>

### Mutabaidan — المتباعدان

<!-- source: standards/terminology/concepts/mutabaidan.yml -->

| field | value |
| --- | --- |
| `code` | `mutabaidan` |
| `kind` | `classification_value` |
| Parent | [`alaqat_al_harfayn`](#alaqat_al_harfayn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المُتَبَاعِدَان |
| Other spellings | `mutabaidain`, `mutabaidayn`, `mutaba'idan` |

**Definition:** Two letters distant in point of articulation and differing in attribute; no idgham falls between them.

**Purpose:** Used as a value of the relation of two letters, so that the cause of idgham or izhar at the place is read from it rather than worked out from the two letters every time.

**Related:** [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`idgham`](#idgham), [`izhar`](#izhar)

<a id="mutajanisan"></a>

### Mutajanisan — المتجانسان

<!-- source: standards/terminology/concepts/mutajanisan.yml -->

| field | value |
| --- | --- |
| `code` | `mutajanisan` |
| `kind` | `classification_value` |
| Parent | [`alaqat_al_harfayn`](#alaqat_al_harfayn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المُتَجَانِسَان |
| Other spellings | `mutajanisain`, `mutajanisayn`, `mutajanisan_saghir` |

**Definition:** Two letters of one point of articulation differing in attribute, like the dal and the taa in «قد تبين».

**Purpose:** Used as a value of the relation of two letters, so that the cause of idgham or izhar at the place is read from it rather than worked out from the two letters every time.

**Related:** [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`idgham`](#idgham), [`izhar`](#izhar)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/59) — `59`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `mutajanisain-idgham-naqis`

<a id="mutamathilan"></a>

### Mutamathilan — المتماثلان

<!-- source: standards/terminology/concepts/mutamathilan.yml -->

| field | value |
| --- | --- |
| `code` | `mutamathilan` |
| `kind` | `classification_value` |
| Parent | [`alaqat_al_harfayn`](#alaqat_al_harfayn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المُتَمَاثِلَان |
| Other spellings | `mutamathilain`, `mutamathilayn`, `mithlayn`, `mutamathilan_saghir` |

**Definition:** Two letters identical in point of articulation and in attribute, like the two baas in «اضرب بعصاك».

**Purpose:** Used as a value of the relation of two letters, so that the cause of idgham or izhar at the place is read from it rather than worked out from the two letters every time.

**Related:** [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`idgham`](#idgham), [`izhar`](#izhar)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `mutamathilain-idgham-kamil`

<a id="mutaqariban"></a>

### Mutaqariban — المتقاربان

<!-- source: standards/terminology/concepts/mutaqariban.yml -->

| field | value |
| --- | --- |
| `code` | `mutaqariban` |
| `kind` | `classification_value` |
| Parent | [`alaqat_al_harfayn`](#alaqat_al_harfayn) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | المُتَقَارِبَان |
| Other spellings | `mutaqaribain`, `mutaqaribayn`, `mutaqariban_saghir` |

**Definition:** Two letters close in point of articulation, in attribute, or in both, like the lam and the raa in «قل رب».

**Purpose:** Used as a value of the relation of two letters, so that the cause of idgham or izhar at the place is read from it rather than worked out from the two letters every time.

**Related:** [`alaqat_al_harfayn`](#alaqat_al_harfayn), [`idgham`](#idgham), [`izhar`](#izhar)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/62) — `62`

<a id="noon_sakinah"></a>

### Noon Sakinah — النون الساكنة

<!-- source: standards/terminology/concepts/noon_sakinah.yml -->

| field | value |
| --- | --- |
| `code` | `noon_sakinah` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النُّون السَّاكِنَة |
| Transliteration | nūn sākinah |
| Other spellings | `nun_sakinah`, `noon_saakinah` |
| English gloss | `Unvowelled Noon` |
| Display evidence | GitHub phrase search: noon sakinah 478 vs nun sakinah 118. Letter names are written as they are said, so the derivation gives noon rather than nun. |

**Definition:** A noon carrying no vowel, fixed in pronunciation and in writing, in continuing and in stopping.

**Purpose:** Used as the trigger of the four rulings, izhar, idgham, iqlab and ikhfa, in tajwid engines.

**Related:** [`tajwid`](#tajwid), [`tanwin`](#tanwin), [`izhar`](#izhar), [`idgham`](#idgham), [`iqlab`](#iqlab), [`ikhfa`](#ikhfa), [`meem_sakinah`](#meem_sakinah), [`ghunnah`](#ghunnah), [`hukm_al_tajwid`](#hukm_al_tajwid), [`small_meem`](#small_meem), [`sukun`](#sukun), [`tanwin_al_damm`](#tanwin_al_damm), [`tanwin_al_fath`](#tanwin_al_fath), [`tanwin_al_kasr`](#tanwin_al_kasr)

**Sources:**

- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `noon-tanween`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/64) — `64`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/57) — `57`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/67) — `67`

<a id="qalqalah"></a>

### Qalqalah — القلقلة

<!-- source: standards/terminology/concepts/qalqalah.yml -->

| field | value |
| --- | --- |
| `code` | `qalqalah` |
| `kind` | `classification_value` |
| Parent | [`hukm_al_tajwid`](#hukm_al_tajwid) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | القَلْقَلَة |
| Other spellings | `qalqala`, `qalqalah_sughra`, `qalqalah_kubra`, `qalqalh` |
| English gloss | `echoing` |

**Definition:** A disturbance in the sound of a vowelless letter as it is pronounced, so that a strong beat is heard, in the letters of «قطب جد»; it grows stronger by the letter's place in the word and by stopping on it.

**Purpose:** Used as a value of the tajwid ruling, so that a place in the text is tagged with it in analysis, colouring and instruction, and its kinds branch under it in the registry of rulings.

- Qalqalah is one of the attributes of the letters that have no opposite; it counts as a ruling when the place where it appears is tagged with it.

**Related:** [`sukun`](#sukun), [`sifat_al_huruf`](#sifat_al_huruf), [`hukm_al_tajwid`](#hukm_al_tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/78) — `78`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `qalqalah-sughra`

<a id="saktah"></a>

### Saktah — السكتة

<!-- source: standards/terminology/concepts/saktah.yml -->

| field | value |
| --- | --- |
| `code` | `saktah` |
| `plural` | `saktahs` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | السَّكْتَة |
| Other spellings | `sakta`, `sakt` |

**Definition:** Cutting off the voice for a short moment without breathing, then continuing the recitation.

**Purpose:** Used to represent where a saktah falls and what its properties are in the text or in a recitation.

- The saktah is the pause itself; the saktah mark is the sign drawn in the mushaf for it.

**Related:** [`saktah_mark`](#saktah_mark), [`waqf`](#waqf), [`tajwid`](#tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/126) — `126`

<a id="sifat_al_huruf"></a>

### Sifat al-Huruf — صفات الحروف

<!-- source: standards/terminology/concepts/sifat_al_huruf.yml -->

| field | value |
| --- | --- |
| `code` | `sifat_al_huruf` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | صِفَات الحُرُوف |
| Other spellings | `sifat`, `sifaat`, `sifat_al_hurouf`, `sifaat_al_huroof` |
| English gloss | `attributes of the letters` |

**Definition:** Manners that attend a letter as it is pronounced and distinguish it from a letter sharing its point of articulation; some have an opposite, such as hams and jahr, shiddah and rakhawah, and some have none, such as safir and qalqalah.

**Purpose:** Used in instruction and in the analysis of pronunciation, and to settle whether two letters are mutajanisan or mutaqariban.

- An attribute is what attends the letter at its point of articulation; tafkhim and tarqiq are an effect that follows from some attributes.

**Related:** [`makhraj`](#makhraj), [`qalqalah`](#qalqalah), [`tafkhim`](#tafkhim), [`tarqiq`](#tarqiq), [`alaqat_al_harfayn`](#alaqat_al_harfayn)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/7) — `7`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/69) — `69`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/70) — `70`

<a id="tafkhim"></a>

### Tafkhim — التفخيم

<!-- source: standards/terminology/concepts/tafkhim.yml -->

| field | value |
| --- | --- |
| `code` | `tafkhim` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّفْخِيم |
| Other spellings | `tafkheem`, `tafkhem`, `tafkhim_rule` |
| English gloss | `heavy pronunciation`, `velarisation` |
| Display evidence | tools/display_measurements.json: tafkhim 900 vs tafkheem 539; the derived form is also the dominant one. |

**Definition:** A fullness entering the sound of a letter so that the mouth fills with its echo; inherent in the letters of istila, and incidental in the raa, the lam of the name of Allah and the alif, following what precedes them.

**Purpose:** Used to tag the places of letters carrying incidental tafkhim in colouring and instruction, and the ranks of tafkhim in the registry of rulings are attributed to it.

- Tafkhim is an attribute of the letter's sound; istila is the attribute of articulation from which tafkhim follows.

**Related:** [`tarqiq`](#tarqiq), [`sifat_al_huruf`](#sifat_al_huruf), [`hukm_al_tajwid`](#hukm_al_tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/87) — `87`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/89) — `89`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `tafkheem-rank-1-jazari`

<a id="tajwid"></a>

### Tajweed — التجويد

<!-- source: standards/terminology/concepts/tajwid.yml -->

| field | value |
| --- | --- |
| `code` | `tajwid` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّجْوِيد |
| Transliteration | tajwīd |
| Registry | [`tajwid_rules`](/guidelines/en/03-terminology/registries/#tajwid_rules) |
| Other spellings | `tajweed`, `tajwīd` |
| Display evidence | GitHub phrase search: tajweed 45,440 vs tajwid 25,280. The doubled form is dominant in English writing, so it is what readers see; the code name stays derived, because the doubling in general use is lexical and not a rule. |

**Definition:** The discipline of delivering the letters of the Quran from their points of articulation and giving them their due properties and rulings.

**Purpose:** Used as the discipline that tajwid rules, rulings and colour annotations belong to, so that a rule in an engine or a dictionary is attributed to it.

- Tajwid is a discipline; mujawwad is a recording style. Neither name stands for the other.

**Related:** [`recitation`](#recitation), [`waqf`](#waqf), [`mujawwad`](#mujawwad), [`noon_sakinah`](#noon_sakinah), [`hukm_al_tajwid`](#hukm_al_tajwid), [`lahn`](#lahn), [`saktah`](#saktah)

**Sources:**

- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/190`

<a id="tarqiq"></a>

### Tarqiq — الترقيق

<!-- source: standards/terminology/concepts/tarqiq.yml -->

| field | value |
| --- | --- |
| `code` | `tarqiq` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّرْقِيق |
| Other spellings | `tarqeeq`, `tarqiq_rule` |
| English gloss | `light pronunciation` |
| Display evidence | tools/display_measurements.json: tarqiq 1156 vs tarqeeq 286; the derived form is also the dominant one. |

**Definition:** A thinness entering the sound of a letter so that the mouth does not fill with its echo; inherent in the letters of istifal, and incidental in the raa and the lam of the name of Allah.

**Purpose:** Used to tag the places of letters carrying incidental tarqiq in colouring and instruction, as the counterpart of tafkhim.

**Related:** [`tafkhim`](#tafkhim), [`sifat_al_huruf`](#sifat_al_huruf), [`hukm_al_tajwid`](#hukm_al_tajwid)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/88) — `88`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `raa-tarqeeq`

## Waqf — `waqf`

<a id="sabab_al_waqf"></a>

### Sabab al-Waqf — سبب الوقف

<!-- source: standards/terminology/concepts/sabab_al_waqf.yml -->

| field | value |
| --- | --- |
| `code` | `sabab_al_waqf` |
| `kind` | `classification` |
| Values | [`waqf_idtirari`](#waqf_idtirari), [`waqf_ikhtibari`](#waqf_ikhtibari), [`waqf_ikhtiyari`](#waqf_ikhtiyari), [`waqf_intizari`](#waqf_intizari) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | سَبَب الوَقْف |
| Other spellings | `waqf_cause`, `aqsam_al_waqf`, `waqf_by_cause` |
| English gloss | `cause of the stop` |

**Definition:** The division of waqf by what moved the reader to it: necessity, testing, waiting, or choice.

**Purpose:** Used as a classification of a stop that occurred in a tilawah or a recording, so that it is known whether it was deliberate or incidental; it is neither the ruling of the place nor its mark.

- The cause of a stop belongs to the stop that occurred; the waqf ruling belongs to the place; the waqf mark is what the mushaf draws.

**Related:** [`waqf`](#waqf), [`waqf_ruling`](#waqf_ruling), [`waqf_mark`](#waqf_mark), [`waqf_idtirari`](#waqf_idtirari), [`waqf_ikhtibari`](#waqf_ikhtibari), [`waqf_intizari`](#waqf_intizari), [`waqf_ikhtiyari`](#waqf_ikhtiyari)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`

<a id="waqf"></a>

### Waqf — الوقف

<!-- source: standards/terminology/concepts/waqf.yml -->

| field | value |
| --- | --- |
| `code` | `waqf` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف |
| English gloss | `Stop`, `Pause` |

**Definition:** Stopping the recitation at a place in the text according to the rules of stopping and starting.

**Purpose:** Represents the general concept of stopping, while `waqf_mark` represents the printed signs that point to it.

**Related:** [`waqf_mark`](#waqf_mark), [`waqf_ruling`](#waqf_ruling), [`waqf_mark_type`](#waqf_mark_type), [`tajwid`](#tajwid), [`saktah`](#saktah), [`madd_al_iwad`](#madd_al_iwad), [`madd_al_lin`](#madd_al_lin), [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun), [`sabab_al_waqf`](#sabab_al_waqf), [`waqf_al_muanaqah`](#waqf_al_muanaqah), [`waqf_hasan`](#waqf_hasan), [`waqf_idtirari`](#waqf_idtirari), [`waqf_ikhtibari`](#waqf_ikhtibari), [`waqf_ikhtiyari`](#waqf_ikhtiyari), [`waqf_intizari`](#waqf_intizari), [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn), [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla), [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla), [`waqf_kafi`](#waqf_kafi), [`waqf_lazim`](#waqf_lazim), [`waqf_mamnu`](#waqf_mamnu), [`waqf_qabih`](#waqf_qabih), [`waqf_tamm`](#waqf_tamm)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/282`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_hasan"></a>

### Waqf Hasan — الوقف الحسن

<!-- source: standards/terminology/concepts/waqf_hasan.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_hasan` |
| `kind` | `classification_value` |
| Parent | [`waqf_ruling`](#waqf_ruling) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف الحَسَن |

**Definition:** A stop that yields a meaning but is connected to what follows it in wording and in meaning.

**Purpose:** Used as a value of the waqf ruling, so that a place is tagged with it in teaching and analysis.

**Related:** [`waqf_ruling`](#waqf_ruling), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/124) — `124`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_idtirari"></a>

### Waqf Idtirari — الوقف الاضطراري

<!-- source: standards/terminology/concepts/waqf_idtirari.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_idtirari` |
| `kind` | `classification_value` |
| Parent | [`sabab_al_waqf`](#sabab_al_waqf) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَقْف الاِضْطِرَارِيّ |
| Other spellings | `idtirari`, `waqf_idtirary`, `waqf_idhtirari` |

**Definition:** A stop forced on the reader by something that compels it, such as shortness of breath, a sneeze or forgetting; the reader stops on any word and then begins again where beginning is sound.

**Purpose:** Used as a value of the cause of the stop, tagging a stop that occurred in a tilawah when it is analysed or taught.

**Related:** [`sabab_al_waqf`](#sabab_al_waqf), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/117) — `117`

<a id="waqf_ikhtibari"></a>

### Waqf Ikhtibari — الوقف الاختباري

<!-- source: standards/terminology/concepts/waqf_ikhtibari.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_ikhtibari` |
| `kind` | `classification_value` |
| Parent | [`sabab_al_waqf`](#sabab_al_waqf) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَقْف الاِخْتِبَارِيّ |
| Other spellings | `ikhtibari`, `waqf_ikhtibary` |

**Definition:** A stop made to show what is cut and what is joined, what is written and what is omitted in the rasm, at a question or in teaching.

**Purpose:** Used as a value of the cause of the stop, tagging a stop that occurred in a tilawah when it is analysed or taught.

**Related:** [`sabab_al_waqf`](#sabab_al_waqf), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/119) — `119`

<a id="waqf_ikhtiyari"></a>

### Waqf Ikhtiyari — الوقف الاختياري

<!-- source: standards/terminology/concepts/waqf_ikhtiyari.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_ikhtiyari` |
| `kind` | `classification_value` |
| Parent | [`sabab_al_waqf`](#sabab_al_waqf) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَقْف الاِخْتِيَارِيّ |
| Other spellings | `ikhtiyari`, `waqf_ikhtiyary` |

**Definition:** A stop the reader makes by choice with no cause arising; it is the one the rulings of tamm, kafi, hasan and qabih apply to.

**Purpose:** Used as a value of the cause of the stop, tagging a stop that occurred in a tilawah when it is analysed or taught.

**Related:** [`sabab_al_waqf`](#sabab_al_waqf), [`waqf`](#waqf), [`waqf_ruling`](#waqf_ruling)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/120) — `120`

<a id="waqf_intizari"></a>

### Waqf Intizari — الوقف الانتظاري

<!-- source: standards/terminology/concepts/waqf_intizari.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_intizari` |
| `kind` | `classification_value` |
| Parent | [`sabab_al_waqf`](#sabab_al_waqf) |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَقْف الاِنْتِظَارِيّ |
| Other spellings | `intizari`, `waqf_intizary`, `waqf_intidhari` |

**Definition:** A stop made on a word the qiraat differ on, so that the reader covers its wajhs when gathering the readings.

**Purpose:** Used as a value of the cause of the stop, tagging a stop that occurred in a tilawah when it is analysed or taught.

**Related:** [`sabab_al_waqf`](#sabab_al_waqf), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/118) — `118`

<a id="waqf_kafi"></a>

### Waqf Kafi — الوقف الكافي

<!-- source: standards/terminology/concepts/waqf_kafi.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_kafi` |
| `kind` | `classification_value` |
| Parent | [`waqf_ruling`](#waqf_ruling) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف الكَافِي |

**Definition:** A stop whose meaning is complete but which is connected to what follows it in meaning, not in wording.

**Purpose:** Used as a value of the waqf ruling, so that a place is tagged with it in teaching and analysis.

**Related:** [`waqf_ruling`](#waqf_ruling), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/123) — `123`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_mark_type"></a>

### Waqf Mark Type — نوع علامة الوقف

<!-- source: standards/terminology/concepts/waqf_mark_type.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_mark_type` |
| `kind` | `classification` |
| Values | [`waqf_al_muanaqah`](#waqf_al_muanaqah), [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn), [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla), [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla), [`waqf_lazim`](#waqf_lazim), [`waqf_mamnu`](#waqf_mamnu) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | نَوْع عَلَامَة الوَقْف |

**Definition:** A classification of what a waqf mark drawn in the mushaf points to: that stopping is compulsory, forbidden or permitted.

**Purpose:** Gives applications one set of values to branch on, instead of reading the shape of the sign itself.

- The mark type is what a drawn mark points to; the waqf ruling belongs to the place itself, even where no mark is drawn on it.

**Related:** [`waqf`](#waqf), [`waqf_mark`](#waqf_mark), [`waqf_ruling`](#waqf_ruling)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_qabih"></a>

### Waqf Qabih — الوقف القبيح

<!-- source: standards/terminology/concepts/waqf_qabih.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_qabih` |
| `kind` | `classification_value` |
| Parent | [`waqf_ruling`](#waqf_ruling) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف القَبِيح |

**Definition:** A stop that yields no meaning, or yields a meaning that is not the one intended.

**Purpose:** Used as a value of the waqf ruling, so that a place is tagged with it in teaching and analysis.

**Related:** [`waqf_ruling`](#waqf_ruling), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/125) — `125`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_ruling"></a>

### Waqf Ruling — حكم الوقف

<!-- source: standards/terminology/concepts/waqf_ruling.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_ruling` |
| `kind` | `classification` |
| Values | [`waqf_hasan`](#waqf_hasan), [`waqf_kafi`](#waqf_kafi), [`waqf_qabih`](#waqf_qabih), [`waqf_tamm`](#waqf_tamm) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | حُكْم الوَقْف |

**Definition:** A classification of the place itself by whether the meaning is complete there, not of the mark drawn at it.

**Purpose:** Used in teaching and in the syntactic and semantic analysis of stopping.

- The waqf ruling belongs to the place; the waqf mark type is what a drawn mark points to, and a place may have a ruling with no mark on it.

**Related:** [`waqf`](#waqf), [`waqf_mark_type`](#waqf_mark_type), [`waqf_tamm`](#waqf_tamm), [`waqf_kafi`](#waqf_kafi), [`waqf_hasan`](#waqf_hasan), [`waqf_qabih`](#waqf_qabih), [`sabab_al_waqf`](#sabab_al_waqf), [`waqf_ikhtiyari`](#waqf_ikhtiyari)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_tamm"></a>

### Waqf Tamm — الوقف التام

<!-- source: standards/terminology/concepts/waqf_tamm.yml -->

| field | value |
| --- | --- |
| `code` | `waqf_tamm` |
| `kind` | `classification_value` |
| Parent | [`waqf_ruling`](#waqf_ruling) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَقْف التَّامّ |

**Definition:** A stop whose meaning is complete and which is connected to what follows it neither in wording nor in meaning.

**Purpose:** Used as a value of the waqf ruling, so that a place is tagged with it in teaching and analysis.

**Related:** [`waqf_ruling`](#waqf_ruling), [`waqf`](#waqf)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/121) — `121`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

## Linguistics — `linguistics`

<a id="fil"></a>

### Fil — الفعل

<!-- source: standards/terminology/concepts/fil.yml -->

| field | value |
| --- | --- |
| `code` | `fil` |
| `kind` | `classification_value` |
| Parent | [`part_of_speech`](#part_of_speech) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الفِعْل |
| English gloss | `Verb` |

**Definition:** A verb: a word whose meaning is tied to a time, with past, present and imperative forms.

**Purpose:** Used as a value of part of speech, and the morphological features specific to verbs — tense, voice and pattern — hang off it.

**Related:** [`part_of_speech`](#part_of_speech), [`morphology`](#morphology)

<a id="harf_al_mana"></a>

### Harf al-Mana — حرف المعنى

<!-- source: standards/terminology/concepts/harf_al_mana.yml -->

| field | value |
| --- | --- |
| `code` | `harf_al_mana` |
| `kind` | `classification_value` |
| Parent | [`part_of_speech`](#part_of_speech) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | حَرْف المَعْنَى |
| English gloss | `Particle` |

**Definition:** A particle: a word with no meaning of its own that gives meaning to the words around it, such as prepositions and the particles of conjunction, negation and interrogation.

**Purpose:** Used as a value of part of speech, and the detailed particle tags of Quranic morphology corpora fall under it.

- Harf al-mana is a part of speech; the written letter — `letter` — is a unit of the written text.

> It takes the full name because `harf` alone is the name of the written letter, a unit of writing and not a part of speech; the decision is in the decision record.

**Related:** [`part_of_speech`](#part_of_speech), [`letter`](#letter)

<a id="irab"></a>

### Irab — الإعراب

<!-- source: standards/terminology/concepts/irab.yml -->

| field | value |
| --- | --- |
| `code` | `irab` |
| `kind` | `analysis` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الإِعْرَاب |
| Other spellings | `i'rab` |
| English gloss | `Grammatical Analysis` |

**Definition:** The statement of the syntactic function of words, their case markers, and their relations within the construction.

**Purpose:** Used to attach syntactic analysis and grammatical functions to the words of an ayah.

**Related:** [`part_of_speech`](#part_of_speech), [`morphology`](#morphology), [`word`](#word)

<a id="ism"></a>

### Ism — الاسم

<!-- source: standards/terminology/concepts/ism.yml -->

| field | value |
| --- | --- |
| `code` | `ism` |
| `kind` | `classification_value` |
| Parent | [`part_of_speech`](#part_of_speech) |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الاِسْم |
| English gloss | `Noun` |

**Definition:** A noun in the Arabic sense: a word whose meaning is not tied to a time. Nouns, adjectives, pronouns, demonstratives and relatives are all ism.

**Purpose:** Used as a value of part of speech, and the detailed tags that Quranic morphology corpora use fall under it.

**Related:** [`part_of_speech`](#part_of_speech)

<a id="lemma"></a>

### Lemma

<!-- source: standards/terminology/concepts/lemma.yml -->

| field | value |
| --- | --- |
| `code` | `lemma` |
| `plural` | `lemmas` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |

**Definition:** The base dictionary form that an inflected word form is referred back to.

**Purpose:** Used to gather the different inflected forms under one dictionary entry.

**Related:** [`root`](#root), [`stem`](#stem), [`morphology`](#morphology), [`wazn`](#wazn)

<a id="morpheme"></a>

### Morpheme — الوحدة الصرفية

<!-- source: standards/terminology/concepts/morpheme.yml -->

| field | value |
| --- | --- |
| `code` | `morpheme` |
| `plural` | `morphemes` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الوَحْدَة الصَّرْفِيَّة |
| Other spellings | `word_segment` |

**Definition:** The smallest unit within a word carrying a meaning or a morphological function, such as a prefix, a suffix or a stem.

**Purpose:** Used to represent the division of a Quranic word into its morphological parts, which is the level that morphological features and tags are attached to in analysis corpora.

- A morpheme is a part of a word; a token is a unit of segmentation that may equal a word or span more than one.

> In Quranic morphology corpora `segment` means the morpheme; in audio APIs it means a word timing. The bare name resolves to nothing, `word_segment` resolves here, and the audio sense is `word_timing`.

**Related:** [`word`](#word), [`token`](#token), [`stem`](#stem), [`morphology`](#morphology), [`part_of_speech`](#part_of_speech)

<a id="morphology"></a>

### Morphology — الصرف

<!-- source: standards/terminology/concepts/morphology.yml -->

| field | value |
| --- | --- |
| `code` | `morphology` |
| `kind` | `analysis` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الصَّرْف |

**Definition:** The analysis of a word's structure and form and the morphological properties it carries.

**Purpose:** Used to represent the morphological features of words or tokens.

**Related:** [`morpheme`](#morpheme), [`root`](#root), [`lemma`](#lemma), [`stem`](#stem), [`part_of_speech`](#part_of_speech), [`wazn`](#wazn), [`fil`](#fil), [`irab`](#irab)

<a id="part_of_speech"></a>

### Part of Speech — قسم الكلمة

<!-- source: standards/terminology/concepts/part_of_speech.yml -->

| field | value |
| --- | --- |
| `code` | `part_of_speech` |
| `kind` | `classification` |
| Values | [`fil`](#fil), [`harf_al_mana`](#harf_al_mana), [`ism`](#ism) |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | قِسْم الكَلِمَة |
| Other spellings | `pos` |

**Definition:** The classification of a word or a morpheme by its grammatical class: ism, fil, harf and what branches from them.

**Purpose:** Used as the basic tag in morphological and syntactic analysis; searching by tag, filtering, and building the syntactic analysis all rest on it.

> The threefold division is the level this standard fixes. The detailed tags used by Quranic morphology corpora — dozens of them — are data falling under these three values, and are not given entries of their own in the dictionary.

**Related:** [`morphology`](#morphology), [`irab`](#irab), [`morpheme`](#morpheme), [`fil`](#fil), [`harf_al_mana`](#harf_al_mana), [`ism`](#ism)

<a id="root"></a>

### Root — الجذر

<!-- source: standards/terminology/concepts/root.yml -->

| field | value |
| --- | --- |
| `code` | `root` |
| `plural` | `roots` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الجَذْر |

**Definition:** The morphological origin a word is referred back to, showing its derivation and its relation to other words.

**Purpose:** Used for morphological search, linguistic analysis, and gathering words that share an origin.

**Related:** [`lemma`](#lemma), [`stem`](#stem), [`morphology`](#morphology), [`wazn`](#wazn)

<a id="stem"></a>

### Stem — الجذع

<!-- source: standards/terminology/concepts/stem.yml -->

| field | value |
| --- | --- |
| `code` | `stem` |
| `plural` | `stems` |
| `kind` | `unit` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | الجِذْع |

**Definition:** What remains of a word once its prefixes and suffixes are removed, and what the morphological additions attach to.

**Purpose:** Used in morphological analysis as a level between the word form and its root: some corpora record the stem and not the root, and some record both.

- A root is an abstract derivational origin; a stem is a form that stands in the word once the additions are removed.

**Related:** [`root`](#root), [`lemma`](#lemma), [`morpheme`](#morpheme), [`morphology`](#morphology), [`wazn`](#wazn)

<a id="wazn"></a>

### Wazn — الوزن

<!-- source: standards/terminology/concepts/wazn.yml -->

| field | value |
| --- | --- |
| `code` | `wazn` |
| `plural` | `wazns` |
| `kind` | `unit` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | الوَزْن |
| Arabic plural | أَوْزَان |
| Other spellings | `wazan`, `awzan` |
| English gloss | `morphological pattern`, `pattern` |

**Definition:** The morphological form of a word represented by the letters of «فعل» with whatever affixes attach to them, showing its structure regardless of its root.

**Purpose:** Used in morphological analysis and in searching by structure, so that words of one pattern are gathered though their roots differ.

- The wazn is the form of the structure, the root is its material, and the stem is the word stripped of its affixes.

**Related:** [`root`](#root), [`stem`](#stem), [`morphology`](#morphology), [`lemma`](#lemma)

## Translation — `translation`

<a id="spoken_translation"></a>

### Spoken Translation — الترجمة المنطوقة

<!-- source: standards/terminology/concepts/spoken_translation.yml -->

| field | value |
| --- | --- |
| `code` | `spoken_translation` |
| `plural` | `spoken_translations` |
| `kind` | `content` |
| Parent | [`translation`](#translation) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّرْجَمَة المَنْطُوقَة |
| Other spellings | `audio_translation` |

**Definition:** Rendering the meanings of the Quran into another language in audio or spoken material.

**Purpose:** Used to distinguish audio renderings of the meanings from written translation and from Quranic recitation.

**Related:** [`translation`](#translation), [`recitation`](#recitation)

<a id="translation"></a>

### Translation — الترجمة

<!-- source: standards/terminology/concepts/translation.yml -->

| field | value |
| --- | --- |
| `code` | `translation` |
| `plural` | `translations` |
| `kind` | `content` |
| Children | [`spoken_translation`](#spoken_translation), [`word_by_word_translation`](#word_by_word_translation) |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّرْجَمَة |

**Definition:** Rendering the meanings of the Quran into another language. A translation is not the Quran in its wording.

**Purpose:** Used to tie translated-meaning texts to ayahs, languages, translators and sources.

**Related:** [`transliteration`](#transliteration), [`spoken_translation`](#spoken_translation), [`translator`](#translator), [`word_by_word_translation`](#word_by_word_translation), [`tafsir`](#tafsir)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/324`

<a id="translator"></a>

### Translator — المترجم

<!-- source: standards/terminology/concepts/translator.yml -->

| field | value |
| --- | --- |
| `code` | `translator` |
| `plural` | `translators` |
| `kind` | `role` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المُتَرْجِم |
| Other spellings | `mutarjim` |

**Definition:** One to whom a translation of the meanings of the Quran into another language is attributed, whether a person or a body.

**Purpose:** Used to attribute a translation to its author, keeping the author apart from the publisher, the reviewer and the source of the text.

- The translator is not the mufassir, though the translation may rest on a tafsir.

**Related:** [`translation`](#translation), [`mufassir`](#mufassir)

<a id="transliteration"></a>

### Transliteration — النقل الحرفي

<!-- source: standards/terminology/concepts/transliteration.yml -->

| field | value |
| --- | --- |
| `code` | `transliteration` |
| `plural` | `transliterations` |
| `kind` | `content` |
| Origin | `borrowed` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | النَّقْل الحَرْفِيّ |

**Definition:** Representing the letters of one writing system with those of another by fixed rules, without translating the meaning.

**Purpose:** Used to give a readable representation in another writing system, or for systematic conversion between writing systems.

**Related:** [`translation`](#translation)

<a id="word_by_word_translation"></a>

### Word by Word Translation

<!-- source: standards/terminology/concepts/word_by_word_translation.yml -->

| field | value |
| --- | --- |
| `code` | `word_by_word_translation` |
| `plural` | `word_by_word_translations` |
| `kind` | `content` |
| Parent | [`translation`](#translation) |
| Origin | `standard` |
| Tier | `core` |
| Status | `draft` |
| Other spellings | `wbw`, `word_by_word`, `wbw_translation`, `word_translation`, `wordbyword` |

**Definition:** A translation giving each word of the ayah its meaning in another language on its own, in the order of the original words.

**Purpose:** Used in instructional display and in learning, and attached to the word by its key rather than to the ayah.

- The translation of a word on its own is not a translation of the ayah, and is not shown in its place.

**Related:** [`translation`](#translation), [`word`](#word), [`word_key`](#word_key)

## Tafsir — `tafsir`

<a id="mufassir"></a>

### Mufassir — المفسر

<!-- source: standards/terminology/concepts/mufassir.yml -->

| field | value |
| --- | --- |
| `code` | `mufassir` |
| `plural` | `mufassirs` |
| `kind` | `role` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المُفَسِّر |
| English gloss | `Exegete` |

**Definition:** One to whom a tafsir of the Quran is attributed, whether by authorship or by transmission.

**Purpose:** Used to attribute a tafsir to its author, keeping the one who said it apart from the book his words were transmitted in, and from its editor and publisher.

- The mufassir is the one whose statement it is, and his statement may be transmitted in someone else's book.

**Related:** [`tafsir`](#tafsir), [`translator`](#translator), [`tafsir_al_ray`](#tafsir_al_ray)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/200`

<a id="tafsir"></a>

### Tafsir — التفسير

<!-- source: standards/terminology/concepts/tafsir.yml -->

| field | value |
| --- | --- |
| `code` | `tafsir` |
| `plural` | `tafsirs` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّفْسِير |
| Other spellings | `tafseer` |
| English gloss | `Exegesis`, `Commentary` |

**Definition:** Stating the meanings of the Quran, explaining its wording, and the rulings and guidance it points to, according to the principles of tafsir.

**Purpose:** Used to represent tafsir works and content and to tie their passages to ayahs, surahs and sources.

**Related:** [`tafsir_mathur`](#tafsir_mathur), [`tafsir_al_ray`](#tafsir_al_ray), [`mufassir`](#mufassir), [`gharib_al_quran`](#gharib_al_quran), [`ayah`](#ayah), [`maqasid_al_surah`](#maqasid_al_surah), [`tadabbur`](#tadabbur), [`translation`](#translation)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/334`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/192`

<a id="tafsir_al_ray"></a>

### Tafsir al-Ray — تفسير الرأي

<!-- source: standards/terminology/concepts/tafsir_al_ray.yml -->

| field | value |
| --- | --- |
| `code` | `tafsir_al_ray` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | تَفْسِير الرَّأْي |
| Other spellings | `tafsir_bil_ray`, `tafsir_bialray`, `tafsir_al_raay`, `tafsir_bir_ray` |
| English gloss | `reasoned tafsir` |

**Definition:** Explaining the meanings of the Quran by reasoning and reflection, after knowledge of the speech of the Arabs, its styles and the principles of tafsir, whether the reasoning is approved or censured.

**Purpose:** Used as the kind of authored content attributed to its author as his statement, kept apart from what is transmitted with a chain.

- Tafsir al-ray is the statement of its author; tafsir mathur is transmitted with a chain.

**Related:** [`tafsir_mathur`](#tafsir_mathur), [`tafsir`](#tafsir), [`mufassir`](#mufassir)

<a id="tafsir_mathur"></a>

### Tafsir Mathur — التفسير المأثور

<!-- source: standards/terminology/concepts/tafsir_mathur.yml -->

| field | value |
| --- | --- |
| `code` | `tafsir_mathur` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّفْسِير المَأْثُور |
| Other spellings | `tafsir_bil_mathur`, `tafsir_bialmathur`, `mathur` |
| English gloss | `Transmitted Tafsir` |

**Definition:** Tafsir transmitted with a chain of narration: explanation of the Quran drawn from the Quran itself, from the Sunnah, or from the sayings of the Companions and Successors.

**Purpose:** Used as content attached to an ayah and carrying its transmitter and the standing of the transmission with it, so it is not treated as authored tafsir text attributed to a single book.

- Tafsir mathur is transmitted with a chain; authored tafsir is the statement of the book's author.
- A single report is not a concept in this standard; the concept is the kind of content organised by ayah.

> The better-known title is «التَّفْسِير بِالمَأْثُور», whose derivation fuses the preposition to the noun and gives `tafsir_bialmathur`. The name recorded here is the descriptive form, which is Arabic and in use, and the better-known form resolves through `alternative_spellings`. This is the same reason `naskh` was given an entry rather than «الناسخ والمنسوخ».

**Related:** [`tafsir`](#tafsir), [`ayah`](#ayah), [`tafsir_al_ray`](#tafsir_al_ray)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/358`

## Quranic sciences — `quranic_sciences`

<a id="asma_al_surah"></a>

### Asma al-Surah — أسماء السورة

<!-- source: standards/terminology/concepts/asma_al_surah.yml -->

| field | value |
| --- | --- |
| `code` | `asma_al_surah` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | أَسْمَاء السُّورَة |
| Other spellings | `asmaa_al_surah` |
| English gloss | `Surah Names` |

**Definition:** The names a surah is known by. Most surahs carry more than one: some established by narration, others settled by usage.

**Purpose:** Used to hold every name a surah is known by, because mushafs differ over the name they print and search must find a surah by any of them.

- The name of a surah is one thing; the reason it was given that name (sabab al-tasmiyah) is another.
- The names of a surah are not the names of the Quran itself.

**Related:** [`surah`](#surah), [`sabab_al_tasmiyah`](#sabab_al_tasmiyah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="fadail_al_quran"></a>

### Fadail al-Quran — فضائل القرآن

<!-- source: standards/terminology/concepts/fadail_al_quran.yml -->

| field | value |
| --- | --- |
| `code` | `fadail_al_quran` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | فَضَائِل القُرْآن |
| Other spellings | `fadail`, `fadail_al_surah` |
| English gloss | `Merits` |

**Definition:** What has been transmitted about the merit of the Quran, or of one of its surahs or ayahs, and the reward or effect that follows from reciting it.

**Purpose:** Used as content attached to the whole Quran, to a surah or to an ayah. It is kept apart from tafsir because it does not explain meaning, and from hadith because it is organised by place in the text rather than by narrator.

- The merit is attached to a place in the Quran; the hadith it comes from is a source it cites, not its location.
- Much of what is transmitted about the merits of surahs is weak or fabricated, so it is bound to its source and its grading.

**Related:** [`quran`](#quran), [`surah`](#surah), [`ayah`](#ayah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/136`

<a id="gharib_al_quran"></a>

### Gharib al-Quran — غريب القرآن

<!-- source: standards/terminology/concepts/gharib_al_quran.yml -->

| field | value |
| --- | --- |
| `code` | `gharib_al_quran` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | غَرِيب القُرْآن |
| Other spellings | `gharib`, `word_meaning` |
| English gloss | `Word Meanings` |

**Definition:** The explanation of Quranic words whose meaning is obscure to most readers, whether because they are rare in use or because their sense has shifted.

**Purpose:** Used as content attached to a particular word of an ayah rather than to the whole ayah, which is what sets it apart from tafsir and its explanation of the ayah's overall meaning.

- Gharib al-Quran explains a word; tafsir explains the meaning of an ayah.
- The meaning is attributed to a particular book, so it may differ between sources.

**Related:** [`word`](#word), [`tafsir`](#tafsir), [`ayah`](#ayah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `2/3`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/8`

<a id="maqasid_al_surah"></a>

### Maqasid al-Surah — مقاصد السورة

<!-- source: standards/terminology/concepts/maqasid_al_surah.yml -->

| field | value |
| --- | --- |
| `code` | `maqasid_al_surah` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | مَقَاصِد السُّورَة |
| Other spellings | `maqasid` |
| English gloss | `Surah Objectives` |

**Definition:** The overarching meanings a surah turns on, held together by its subject, and the single aim its ayahs are ordered around.

**Purpose:** Used as content attached to a whole surah rather than to one of its ayahs, which sets it apart from tafsir, which proceeds ayah by ayah, and from a topic index, which lists what the surah contains.

- A maqsad is an aim that gathers the surah; a topic is one of the things it contains.

**Related:** [`surah`](#surah), [`tafsir`](#tafsir)

<a id="mutashabihat"></a>

### Mutashabihat — المتشابهات

<!-- source: standards/terminology/concepts/mutashabihat.yml -->

| field | value |
| --- | --- |
| `code` | `mutashabihat` |
| `kind` | `analysis` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | المُتَشَابِهَات |
| Other spellings | `mutashabih`, `mutashabihat_lafziyyah`, `similar_ayahs` |
| English gloss | `Similar Passages` |

**Definition:** The places in the Quran where the wording of ayahs, or of parts of them, resembles one another, whether exactly or with a slight difference in a word or in order.

**Purpose:** Used above all for memorisation, revision and search tools, since a memoriser needs to know which places are confused with one another and where they differ.

- The resemblance of wording meant here is not the mutashabih that stands opposite the muhkam in the Quranic sciences.
- A resemblance is a relation between two places or more, not a property of a single ayah.

**Related:** [`ayah`](#ayah), [`word`](#word), [`hifz`](#hifz), [`equivalent_ayah`](#equivalent_ayah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/390`

<a id="naskh"></a>

### Naskh — النسخ

<!-- source: standards/terminology/concepts/naskh.yml -->

| field | value |
| --- | --- |
| `code` | `naskh` |
| `kind` | `concept` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | النَّسْخ |
| Other spellings | `nasikh_mansukh`, `nasikh_wa_mansukh`, `nasekh_mansokh` |
| English gloss | `Abrogation` |

**Definition:** The lifting of a legal ruling by a later legal proof. In the Quran it is studied by relating an abrogating ayah to an abrogated one.

**Purpose:** Used to represent the relation between two ayahs, one abrogating and one abrogated: a relation between two places in the text, not a property of a single ayah.

- Abrogation bears on the ruling, not on the text: an ayah whose ruling is abrogated stands in the mushaf as it is.
- The relation is disputed in many places, so it is bound to its source and never presented as agreed upon.

**Related:** [`ayah`](#ayah), [`asbab_al_nuzul`](#asbab_al_nuzul)

**Sources:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/237`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/66`

<a id="sabab_al_tasmiyah"></a>

### Sabab al-Tasmiyah — سبب التسمية

<!-- source: standards/terminology/concepts/sabab_al_tasmiyah.yml -->

| field | value |
| --- | --- |
| `code` | `sabab_al_tasmiyah` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `extended` |
| Status | `draft` |
| Vocalized | سَبَب التَّسْمِيَة |
| Other spellings | `sabab_al_tasmiya` |

**Definition:** The statement of why a surah was given its name, and what has been transmitted about it by narration or on linguistic grounds.

**Purpose:** Used as content attached to a surah. It is kept apart from the occasion of revelation because it concerns the name and not the revelation, and because many surahs have more than one name and so more than one reason.

- The reason for the name concerns the surah's name; the occasion of revelation concerns the revelation of an ayah.

**Related:** [`surah`](#surah), [`asbab_al_nuzul`](#asbab_al_nuzul), [`asma_al_surah`](#asma_al_surah)

**Sources:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="tadabbur"></a>

### Tadabbur — التدبر

<!-- source: standards/terminology/concepts/tadabbur.yml -->

| field | value |
| --- | --- |
| `code` | `tadabbur` |
| `plural` | `tadabburs` |
| `kind` | `content` |
| Origin | `quranic` |
| Tier | `core` |
| Status | `draft` |
| Vocalized | التَّدَبُّر |
| Other spellings | `tadabur`, `waqfat_tadabburiyyah` |
| English gloss | `Reflection` |

**Definition:** Reflecting on the meanings of the Quran and what they call for in action, and what a reader records of a pause at an ayah or a word.

**Purpose:** Used as content attached to an ayah or to a place within it. It is kept apart from tafsir because it does not undertake to state the apparent meaning, and the one who says it is not necessarily a mufassir.

- Tafsir states the meaning of an ayah by a method; tadabbur is the effect of that meaning on the one reflecting.

**Related:** [`ayah`](#ayah), [`tafsir`](#tafsir)

**Sources:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/29) — `29`
