# Quranic Software Terminology Standard

معيار لتوحيد تسمية وتعريف المفاهيم المستخدمة في البرمجيات والتطبيقات القرآنية، بحيث تكون واضحة، دقيقة، مستقرة، ومتوقعة، ويمكن استخدامها بشكل متسق في:

- Code
- APIs
- Databases
- Datasets
- Packages
- Documentation

الفكرة الأساسية مستوحاة من **Convention over Configuration**:

> عندما يعرف المطور قواعد المعيار، يجب أن يستطيع توقع أسماء المفاهيم والعلاقات والحقول وطريقة استخدامها دون الرجوع إلى التوثيق في كل مرة.

---

# 1. المفهوم قبل الاسم

نحدد المفهوم أولًا ثم نختار اسمه.

قبل اعتماد أي مصطلح يجب تحديد:

- ما الذي يمثله؟
- ما حدوده؟
- ما الذي لا يشمله؟
- هل يختلف عن مفهوم قريب منه؟
- ما الغرض من تمثيله برمجيًا؟

لا نبدأ من السؤال:

> كيف نترجم هذه الكلمة؟

بل من:

> ما المفهوم الذي نريد تمثيله؟

ثم نختار الاسم الأنسب له.

---

# 2. اسم Canonical واحد لكل مفهوم

لكل مفهوم اسم برمجي معياري واحد:

**Canonical Name**

وهو الاسم الذي يجب استخدامه افتراضيًا عبر المشاريع التي تتبع المعيار.

مثلًا:

```text
Surah
Ayah
Word
Mushaf
Tajwid
```

يمكن تسجيل أسماء وتهجئات وترجمات أخرى، لكنها لا تنافس الاسم الـCanonical.

القاعدة:

> **One concept, one canonical name.**

---

# 3. متى نستخدم المصطلح القرآني؟

نحتفظ بالمصطلح العربي عندما يمثل مفهومًا قرآنيًا أو علميًا متخصصًا، ويؤدي استبداله بكلمة إنجليزية عامة إلى فقدان الدقة أو هوية المفهوم.

مثل:

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

أما المفاهيم العامة التي لها أسماء تقنية إنجليزية واضحة، فنستخدم الإنجليزية الطبيعية:

```text
Word
Letter
Page
Line
Root
Translation
Glyph
```

لذلك نفضل مثلًا:

```text
Surah → Ayah → Word
```

على:

```text
Chapter → Verse → Word
```

وعلى:

```text
Surah → Ayah → Kalimah
```

وجود اسم عربي للمفهوم لا يعني أن نقله صوتيًا هو الخيار الأفضل.

القاعدة:

> **Quran-specific concepts retain Quranic names; general concepts use natural technical English.**

---

# 4. Canonical Code Spelling

عندما نقرر استخدام مصطلح عربي الأصل، يعتمد له المعيار تهجئة برمجية واحدة:

**Canonical Code Spelling**

الهدف ليس بناء نظام transliteration أكاديمي، وإنما spelling بسيط، ثابت، ومتوقع للمطورين.

## القواعد العامة

- ASCII-friendly.
- لا تستخدم العلامات الأكاديمية:
  `ā`, `ī`, `ū`, `ʿ`, `ʾ`.
- لا تستخدم `'` لتمثيل الهمزة أو العين.
- لكل مصطلح spelling واحد معتمد.
- التهجئات الشائعة الأخرى تسجل كـ`alternative_spellings`.

مثلًا:

```text
Qiraah
Ruku
Irab
Istiadhah
```

بدل:

```text
Qira'ah
Rukūʿ
I'rab
Istiʿādhah
```

---

# 5. التاء المربوطة

عند نقل مصطلح عربي مفرد ينتهي بتاء مربوطة، تعتمد `h` في النهاية:

```text
سورة   → Surah
آية    → Ayah
رواية  → Riwayah
قراءة  → Qiraah
بسملة  → Basmalah
```

لذلك:

```text
Surah     وليس Sura
Ayah      وليس Aya
Riwayah   وليس Riwaya
```

وتسجل الصور الأخرى كتهجئات بديلة.

---

# 6. حروف المد

في **Quranic Software Terminology Standard** لا نستخدم مضاعفة الحروف الإنجليزية لتمثيل طول حروف المد في الـCanonical Code Spelling.

نعتمد بصورة عامة:

```text
ا / ى → a
ي     → i
و     → u
```

وليس:

```text
aa
ee
oo
```

لذلك:

```text
Tajwid
Tafsir
Tariq
Nuzul
Tahqiq
Tadwir
```

وليس:

```text
Tajweed
Tafseer
Tareeq
Nuzool
Tahqeeq
Tadweer
```

هذه الصور ليست بالضرورة خاطئة في الاستخدام العام، لكنها ليست الـCanonical spelling في هذا المعيار.

---

# 7. الهمزة والعين

لا نمثل الهمزة أو العين بعلامات خاصة داخل أسماء الكود.

نعتمد:

```text
Qiraah
Irab
Istiadhah
Ruku
```

ولا نعتمد:

```text
Qira'ah
I'rab
Isti'adhah
Ruku'
```

يمكن استخدام transliteration علمي أدق في واجهة العرض أو المحتوى الأكاديمي عند الحاجة.

---

# 8. الأسماء المركبة و`al-`

عند الاحتفاظ بمصطلح عربي مركب نستخدم صيغة ثابتة قدر الإمكان:

```text
Rub al-Hizb
Asbab al-Nuzul
Sujud al-Tilawah
```

ولا نغير `al-` بحسب الحروف الشمسية لأغراض الـCanonical spelling.

وفي identifiers:

```text
rub_al_hizb
asbab_al_nuzul
sujud_al_tilawah
```

---

# 9. Code Name وDisplay Name

الاسم البرمجي لا يلزم أن يكون هو طريقة العرض الأكاديمية.

يمكن أن يكون:

```text
Code:     qiraah
Display:  Qirāʾah
Arabic:   قراءة
```

الـCanonical Code Spelling يجب أن يبقى مستقرًا، بينما يمكن أن تختلف طريقة العرض بحسب اللغة والجمهور والسياق العلمي.

---

# 10. شكل الأسماء في الكود

نستخدم أسماء واضحة وكاملة:

```text
surah
ayah
word
translation
```

ونتجنب الاختصارات غير المعروفة:

```text
srh
ay
wrd
trans
```

كما نتجنب الكلمات المبهمة عندما يوجد اسم أدق:

```text
data
info
item
object
value
```

ونتجنب `type` إذا كان بالإمكان تسمية التصنيف نفسه بدقة أكبر.

---

# 11. المفرد والجمع

نستخدم:

- المفرد للكيان الواحد.
- الجمع للمجموعات.

مثلًا:

```text
Ayah   → Ayahs
Surah  → Surahs
Mushaf → Mushafs
Riwayah → Riwayahs
```

الجمع البرمجي يتبع convention إنجليزيًا بسيطًا:

```text
ayahs
surahs
juzs
hizbs
```

ولا نستخدم الجمع العربي كاسم collection:

```text
ayat
suwar
ajza
ahzab
```

يمكن تسجيل الجمع العربي في القاموس كمعلومة لغوية.

---

# 12. كل Entry له Kind

ليست كل المصطلحات من النوع نفسه.

يجب تحديد طبيعة كل Entry، مثل:

```text
entity
concept
property
classification
classification_value
role
discipline
process
content
analysis
mark
text_unit
layout_unit
```

مثلًا:

```text
Ayah                       → entity
Tajwid                     → discipline
Translation                → content
Reciter                    → role
Revelation Order           → property
Revelation Classification  → classification
Makki                      → classification_value
Waqf Mark                  → mark
```

لا تعامل كل هذه الأشياء كقائمة مسطحة من "مصطلحات".

---

# 13. نفرد الأنواع والقيم

إذا كان للمفهوم أنواع أو قيم مهمة، فإن المعيار لا يكتفي بتعريف الـparent.

تفرد الأنواع والقيم في القاموس أيضًا.

مثلًا:

```text
Revelation Classification
├── Makki
├── Madani
└── Disputed
```

و:

```text
Recitation Style
├── Murattal
├── Mujawwad
└── Muallim
```

و:

```text
Recitation Pace
├── Tahqiq
├── Tadwir
└── Hadr
```

و:

```text
Waqf Type
├── Mandatory Waqf
├── Prohibited Waqf
├── Permissible Waqf
├── Continuation Preferred
├── Waqf Preferred
└── Interchangeable Waqf
```

كل واحدة من هذه القيم تحصل على Entry مستقلة، حتى لو كان تمثيلها البرمجي Enum value.

---

# 14. Parent وChild

عندما يكون المفهوم جزءًا من taxonomy، يجب تحديد علاقته بالمفهوم الأب.

مثلًا:

```yaml
concept: makki
kind: classification_value
parent: revelation_classification
```

أو:

```yaml
concept: murattal
kind: classification_value
parent: recitation_style
```

الهدف أن يعرف المطور ليس فقط معنى `Makki`، بل أيضًا:

> Makki هو نوع من ماذا؟

---

# 15. Definition

كل Entry يجب أن يحتوي على `definition`.

الـDefinition يجيب عن:

> **ما هذا المفهوم؟**

ويجب أن:

- يعرّف المفهوم نفسه.
- يكون دقيقًا ومختصرًا.
- يحدد حدوده عند الحاجة.
- لا يعتمد على الاسم نفسه في تعريف دائري.
- لا يحتوي على تفاصيل implementation.
- يستند إلى مصدر مناسب عندما يكون المفهوم علميًا أو اصطلاحيًا.

مثلًا:

```yaml
concept: ayah

definition: >
  وحدة من النص القرآني تقع ضمن سورة ولها حدود محددة،
  وقد يختلف رقمها أو بعض حدودها باختلاف نظام عد الآي.
```

وليس:

```text
Ayah: A Quranic verse.
```

---

# 16. Purpose

كل Entry يجب أن يحتوي كذلك على `purpose`.

الـPurpose يجيب عن:

> **لماذا نحتاج هذا المفهوم في البرمجيات القرآنية؟**

ويشرح:

- دوره في software model.
- ما الذي نستخدمه لتمثيله أو ربطه.
- لماذا يحتاج المطور إلى التمييز بينه وبين غيره.

مثلًا:

```yaml
concept: ayah

purpose: >
  تستخدم كوحدة أساسية للإشارة إلى النص القرآني وربط
  الترجمات والتفاسير والتلاوات والتحليلات والبيانات
  الأخرى بموضع محدد من القرآن.
```

## الفرق

```text
Definition → What is it?
Purpose    → Why do we model it?
```

لا يعيد `purpose` صياغة `definition`.

ولا نضع تفاصيل الاستخدام البرمجي داخل `definition`.

إذا لم يكن للمفهوم غرض برمجي واضح، فهذا سبب لمراجعة الحاجة إلى إدخاله في القاموس الأساسي.

---

# 17. حدود المفهوم

عند وجود احتمال حقيقي للالتباس، يجب أن يوضح التعريف أو حقل مستقل ما لا يشمله المفهوم.

مثلًا:

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

الهدف ليس توثيق الفروق اللغوية فقط، بل منع استخدام اسم واحد لمفهومين مختلفين في البيانات والكود.

---

# 18. المفاهيم المتشابهة تبقى منفصلة

لا ندمج مفهومين لأن ترجمتهما متشابهة.

## النص

```text
Word
Token
Morpheme
Lemma
Root
```

## التمثيل الرقمي

```text
Letter
Character
Codepoint
Grapheme
Glyph
```

## القرآن والمصحف

```text
Quran
Mushaf
```

## المحتوى والعرض

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

## النص والتحليل

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

# 19. الاسم والتهجئة والترجمة ليست شيئًا واحدًا

يجب التفريق بين:

```text
canonical
alternative_spellings
english_glosses
deprecated
```

مثلًا:

```yaml
concept: ayah

canonical: ayah

alternative_spellings:
  - aya

english_glosses:
  - verse
```

`Aya` تهجئة بديلة لـ`Ayah`.

أما `Verse` فهو English gloss وليس alternative spelling.

وكذلك:

```yaml
concept: tajwid

canonical: tajwid

alternative_spellings:
  - tajweed
```

لا نستخدم `aliases` كحقل عام يجمع علاقات مختلفة دون تمييز.

---

# 20. Deprecated لا يعني Incorrect

نفرق بين:

### Alternative

صيغة أخرى صحيحة أو شائعة:

```text
Tajweed → alternative spelling of Tajwid
```

### Deprecated / Discouraged

اسم مفهوم، لكنه غير موصى به في المشاريع الجديدة.

### Incorrect

اسم يشير إلى مفهوم مختلف أو يؤدي إلى معنى غير صحيح.

مثلًا قد تكون `Verse` ترجمة إنجليزية صحيحة لـ`Ayah`، لكنها ليست الـCanonical name في المعيار.

---

# 21. المعرفات والأرقام والترتيب

لكل suffix معنى ثابت.

## `id`

معرف داخلي:

```text
surah_id
ayah_id
word_id
mushaf_id
```

## `number`

رقم معتمد داخل المجال:

```text
surah_number
ayah_number
page_number
```

## `position`

موضع العنصر داخل parent أو sequence:

```text
word_position
token_position
line_position
```

## `order`

ترتيب دلالي مستقل:

```text
revelation_order
display_order
```

لا تستخدم:

```text
id
number
position
order
```

كمترادفات.

---

# 22. العلاقات

العلاقة تسمى باسم المفهوم المرتبط مباشرة.

نفضل:

```text
surah.ayahs
ayah.surah
ayah.words
mushaf.pages
page.lines
```

المفرد لعلاقة الواحد والجمع لعلاقة المتعدد.

ولا نستخدم أسماء إجرائية عندما تكون العلاقة مجرد علاقة بيانات:

```text
getAyahList()
fetchRelatedSurah()
retrieveWords()
```

إذا كان:

```text
ayahs
surah
words
```

يكفي.

---

# 23. العمليات والأفعال

كما نوحد أسماء الكيانات، نوحد أسماء العمليات المتكررة.

مثل:

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

نستخدم الفعل نفسه للعملية نفسها.

ونتجنب:

```text
process
handle
do
```

عندما يوجد فعل أدق.

مثلًا:

```text
tokenizeText()
normalizeText()
renderAyah()
validateMushaf()
```

أفضل من:

```text
processText()
handleAyah()
```

---

# 24. Classifications وBooleans

التصنيفات يجب أن تحمل أسماء domain-specific:

```text
Waqf Type
Recitation Style
Recitation Pace
Revelation Classification
Script Type
Annotation Type
```

بدل:

```text
Quran Type
Item Type
Data Type
```

أما Boolean فيجب أن يظهر من اسمه أنه سؤال نعم/لا:

```text
has_sajdah
is_active
is_included
```

ولا نمثل classification متعدد القيم بمجموعة Booleans عندما يكون classification واحد أكثر دقة.

---

# 25. تنظيم المجالات

ينظم القاموس حسب domains واضحة، وليس في قائمة واحدة مسطحة.

النسخة الأولية المقترحة:

```text
Core
Structure
Text
Mushaf
Qiraat
Recitation
Tajwid
Waqf
Revelation
Linguistics
Translation
Tafsir
Typography
Audio
Metadata
```

يمكن إضافة أو تقسيم المجالات عندما تظهر حاجة حقيقية لذلك.

---

# 26. الاتساق بين طبقات النظام

الـCanonical Vocabulary نفسه يستخدم عبر طبقات النظام قدر الإمكان.

إذا اعتمدنا:

```text
Surah
Ayah
Word
```

فيكون المتوقع:

```text
Models:
Surah
Ayah
Word

Database:
surahs
ayahs
words

Foreign Keys:
surah_id
ayah_id

API:
/surahs
/surahs/{surah}/ayahs
/ayahs/{ayah}/words
```

نتجنب استخدام:

```text
Database: surah
API: chapter
Package: quran_section
```

للمفهوم نفسه.

واجهة المستخدم يمكن أن تترجم أو تعرض الاسم بصورة مختلفة، بينما يبقى الـCanonical internal vocabulary ثابتًا.

---

# 27. بنية Entry في القاموس

القاموس الناتج عن هذا المعيار يستخدم بنية موحدة.

الحد الأدنى:

```yaml
concept:
kind:
category:

canonical:
arabic:

definition:
purpose:
```

وتضاف عند الحاجة:

```yaml
parent:

plural:
code:
symbol:

alternative_spellings:
english_glosses:
deprecated:

related:
sources:
```

مثال:

```yaml
concept: ayah
kind: entity
category: structure

canonical: ayah
plural: ayahs

arabic:
  singular: آية
  plural: آيات

definition: >
  وحدة من النص القرآني تقع ضمن سورة ولها حدود محددة،
  وقد يختلف رقمها أو بعض حدودها باختلاف نظام عد الآي.

purpose: >
  تستخدم كوحدة أساسية للإشارة إلى النص القرآني وربط
  الترجمات والتفاسير والتلاوات والتحليلات والبيانات
  الأخرى بموضع محدد من القرآن.

alternative_spellings:
  - aya

english_glosses:
  - verse

related:
  - surah
  - ayah_numbering_system

sources: []
```

---

# 28. مصادر التعريفات

المصطلحات العلمية والشرعية والاصطلاحية يجب أن تستند إلى مصادر مناسبة.

المصدر يوثق **المفهوم وتعريفه**، وليس بالضرورة اختيار الاسم البرمجي.

فمثلًا قد يثبت المصدر معنى `Ayah`، بينما اختيار:

```text
Ayah
```

بدل:

```text
Verse
```

هو قرار معياري برمجي تتخذه **Quranic Software Terminology Standard**.

يجب الفصل بين:

```text
Domain fact
```

و:

```text
Standard convention
```

---

# 29. القاموس Machine-readable

المصدر الأساسي للقاموس يجب أن يكون قابلًا للقراءة آليًا، مثل YAML أو JSON.

ومن نفس المصدر يمكن توليد:

- Documentation
- Terminology website
- API schemas
- IDE hints
- Linters
- Validation rules
- Deprecated-term warnings
- Migration mappings

الوثائق المقروءة للبشر تكون output من نفس المصدر قدر الإمكان، وليس نسخة منفصلة يصعب إبقاؤها متزامنة.

---

# 30. قاعدة قبول أي مصطلح جديد

قبل إدخال أي Entry إلى القاموس يجب الإجابة عن:

1. ما المفهوم؟
2. ما تعريفه؟
3. ما الغرض البرمجي من تمثيله؟
4. ما حدوده وما المفاهيم التي قد يختلط بها؟
5. ما `kind` الخاص به؟
6. إلى أي `category` ينتمي؟
7. هل له `parent`؟
8. هل هو مفهوم قرآني متخصص أم مفهوم تقني عام؟
9. ما الـCanonical Name الأنسب؟
10. إذا كان عربي الأصل، هل يتبع Canonical Code Spelling؟
11. ما المفرد والجمع البرمجيان؟
12. ما التهجئات البديلة؟
13. ما الترجمات أو English glosses؟
14. هل توجد أسماء Deprecated؟
15. هل الاسم يعمل بصورة طبيعية في Code وAPI وDatabase؟
16. ما المصدر الذي يثبت تعريف المفهوم؟

إذا لم نستطع تعريف المفهوم أو بيان الغرض البرمجي منه بوضوح، فلا يعتمد حتى تتضح الحاجة إليه.

---

# المبادئ الأساسية

يمكن تلخيص **Quranic Software Terminology Standard** في المبادئ التالية:

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
13. **Convention over Configuration.**