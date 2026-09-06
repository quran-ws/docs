---
title: معيار المصطلحات
description: اسم Canonical واحد لكل مفهوم، وتهجئة برمجية مشتقة لا مختارة.
status: draft
sidebar:
  order: 1
---

معيار لتوحيد تسمية المفاهيم المستخدمة في البرمجيات والتطبيقات القرآنية وتعريفها، بحيث تكون واضحة ودقيقة ومستقرة ومتوقعة، ويمكن استخدامها استخدامًا متسقًا في:

- Code
- APIs
- Databases
- Datasets
- Packages
- Documentation

الفكرة الأساسية مستوحاة من **Convention over Configuration**:

> عندما يعرف المطور قواعد المعيار، يستطيع توقع أسماء المفاهيم والعلاقات والحقول وطريقة استخدامها دون الرجوع إلى التوثيق في كل مرة.

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

الهدف ليس بناء نظام نقل حرفي دقيق مثل ALA-LC أو DIN 31635، وإنما spelling بسيط، ثابت، ومتوقع للمطورين.

## القواعد العامة

- ASCII-friendly.
- لا تستخدم علامات النقل الدقيق:
  `ā`, `ī`, `ū`, `ʿ`, `ʾ`.
- لا تستخدم `'` لتمثيل الهمزة أو العين.
- لكل مصطلح spelling واحد معتمد.
- التهجئات الشائعة الأخرى تسجل كـ`alternative_spellings`.

## كيف تُشتق التهجئة

قواعد الأقسام من 4 إلى 8 قواعد آلية يمكن تنفيذها في برنامج. لذلك نشتق
الـCanonical Code Spelling من الاسم العربي بالحركات بدالة واحدة، ولا نتركها
لاجتهاد كل مشروع.

```bash
python3 tools/translit.py "سُورَة" "رُبْع الحِزْب"
سُورَة        surah      Surah
رُبْع الحِزْب   rub_al_hizb   Rub al-Hizb
```

- يُكتب المدخل **بالحركات**، لأن الحركات القصيرة لا يمكن استنتاجها من
  النص المجرد، واستنتاجها هو الاجتهاد الذي نريد الاستغناء عنه. وألف الوصل غير المشكولة ترفض
  صراحةً ولا يخمن لها حكم: `اِسْتِعَاذَة` تعطي `istiadhah`، أما `استعاذة` فترد.
- الدالة **غير قابلة للعكس** بقصد. فالحروف المفخمة ونظائرها تعطي حرفًا
  لاتينيًا واحدًا، مثل `ص` و`س` وكلاهما `s`. الهدف هنا أن يبقى المعرف ثابتًا،
  وليس أن يكون النطق دقيقًا.
- كل مصطلح عربي الأصل في القاموس له حالة اختبار في `tools/test_translit.py`.
  فإذا تغيرت قاعدة من قواعد التهجئة، يبين ذلك الملف أي الأسماء تتغير معها.

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

## التاء المربوطة في الإضافة

التاء المربوطة تنطق تاءً إذا كانت الكلمة مضافة إلى ما بعدها، فتكتب `t` لا `h`:

```text
همزة الوصل    → hamzat_al_wasl     لا hamzah_al_wasl
علامة التحزيب → alamat_al_tahzib   لا alamah_al_tahzib
سجدة التلاوة  → sajdat_al_tilawah  لا sajdah_al_tilawah
```

والقاعدة آلية: التاء المربوطة في آخر الاسم تعطي `h`، وفي غير آخره تعطي `t`.

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

## ياء النسب

الياء المشددة في آخر الاسم المنسوب تعطي `i` واحدة:

```text
مكي     → Makki      لا Makkiyy
مدني    → Madani     لا Madaniyy
عثماني  → Uthmani    لا Uthmaniyy
```

## أسماء الحروف تكتب كما تُنطق

أسماء الحروف تكتب كما تنطق، لأن اسم الحرف هو صوته:

```text
نُون   → noon      وليس nun
مِيم   → meem      وليس mim
سِين   → seen      وليس sin
جِيم   → jeem      وليس jim
يَاء   → yaa       وليس ya
```

**القاعدة خاصة باسم الحرف وحده.** وبقية المصطلحات تشتق كما في الأقسام 4–8:

```text
noon_saghirah      اسم حرف، فيكتب كما ينطق
seen_al_qiraah     اسم حرف
tajwid             ليس اسم حرف، فيشتق (لا tajweed)
haqiqi             ليس اسم حرف، فيشتق (لا haqeeqi)
makki              ليس اسم حرف، فيشتق (لا makkee)
```

أسماء الحروف الثمانية والعشرين في
`standards/terminology/data/letter_names.tsv`، وتقرؤها الدالة منه.

> **غير محسوم:** `ت` و`ط` كلاهما يعطي `taa`، و`ح` و`ه` كلاهما يعطي `haa`،
> لأن القسم 4 يجمع المفخم والمرقق عمدًا. ولا يستعمل أي منهما اسمًا في مدخل
> اليوم، فالتصادم مسجل ولم يعالج. و`tools/build_aliases.py` يفشل إن ادعى
> مفهومان اسمًا واحدًا.

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

يمكن استخدام نقل حرفي أدق في واجهة العرض أو في المحتوى العلمي عند الحاجة.

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

## متى تحذف `al`؟

`al` جزء من الاسم في الإضافة فقط، وتحذف في حالتين:

**أداة التعريف في أول الاسم** لا تدخل في الاسم البرمجي:

```text
الفتحة   → fathah      لا al_fathah
السكون   → sukun       لا al_sukun
```

**أداة التعريف في الصفة** لا تدخل كذلك؛ فإذا كان الموصوف معرفًا والصفة معرفة
فهما اسم واحد لا إضافة:

```text
الوقف اللازم     → waqf_lazim      لا waqf_al_lazim
الصفر المستدير   → sifr_mustadir   لا sifr_al_mustadir
الواو الصغيرة    → waw_saghirah    لا waw_al_saghirah
```

والتمييز بينهما آلي. إذا كان الاسم الأول معرفًا بـ`ال` فما بعده صفة، وتحذف
أداة تعريفها. وإذا كان الاسم الأول نكرة فما بعده مضاف إليه، وتثبت فيه `al`:

```text
رُبْع الحِزْب      → rub_al_hizb   (الأول نكرة، فهي إضافة)
الوَقْف اللَّازِم   → waqf_lazim    (الأول معرفة، فهي صفة)
```

---

# 9. Code Name وDisplay Name

الاسم البرمجي لا يلزم أن يكون هو صورة النقل الدقيق.

يمكن أن يكون:

```text
Code:     qiraah
Display:  Qirāʾah
Arabic:   قراءة
```

الـCanonical Code Spelling يجب أن يبقى مستقرًا، بينما يمكن أن تختلف طريقة العرض بحسب اللغة والجمهور والسياق.

## حقول التسمية

نستخدم عدة حقول لتخزين الأسماء المختلفة للمفهوم:

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

### الحقول

**`code`** هو المعرف الثابت المستخدم في الكود والـAPI وقواعد البيانات. نولده
حسب قواعد الأقسام 4 إلى 8، ولا نغيره لاحقًا لمجرد وجود اسم أكثر شيوعًا.

**`display`** هو الاسم الذي يظهر للمستخدم في التوثيق والواجهات. نختار التهجئة
الإنجليزية الأكثر شيوعًا، ونسجل مصدر هذا الاختيار في `display_evidence`.

**`transliteration`** هو النقل الدقيق للاسم بحروف لاتينية، على نظام ALA-LC أو
DIN 31635. نكتبه عند الحاجة فقط، وهو حقل اختياري.

**`arabic.vocalized`** هو الاسم العربي مكتوبًا بالحركات. نشتق منه `code`، ولا
نستطيع اشتقاق `code` بدونه.

**`dabt`** هو اسم العلامة في علم الضبط. ننقله كما ورد في مصدره.

**`by_shape`** هو وصف صورة العلامة كما ترسم في المصحف. ننقله كما ورد في مصدره.

**`mushaf_introduction`** هو اسم العلامة كما ورد في مقدمة المصحف. نكتب `null`
إذا لم تذكر المقدمة اسمًا لها، وهذه معلومة عن المصدر نفسه.

**`unicode`** هو اسم المحرف في يونيكود. نقرؤه من قاعدة يونيكود، ولا نستخدمه
معرفًا في الكود.

**`alternative_spellings`** يحتوي على التهجئات البديلة المعروفة. نستخدمها في
البحث وربط المدخلات المختلفة بالمفهوم نفسه.

### قواعد ثابتة

- `code` و`display` قد يختلفان، وهذا مقصود.
- لا نستخدم اسم يونيكود معرفًا في الكود، لأنه يصف صورة المحرف ولا يصف وظيفته،
  وقد يخدم المحرف الواحد علامتين مختلفتين.
- خلو `mushaf_introduction` معلومة عن المصدر، وليس نقصًا في المدخل.

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

يحدد لكل Entry دوره البنيوي، من قائمة **مغلقة** لا يزاد عليها:

```text
entity                 كيان له هوية مستقلة
concept                مفهوم يمثل ولا يخزن ككيان
classification         تصنيف له قيم
classification_value   قيمة من قيم تصنيف
property               خاصية لكيان
role                   دور يقوم به شخص
process                عملية تجرى على النص
content                محتوى مرتبط بالنص
analysis               تحليل مشتق من النص
mark                   علامة مرسومة في المصحف
unit                   وحدة نصية أو كتابية أو طباعية
```

الـ`kind` يصف **شكل** الـEntry لا مجاله؛ فالمجال يحمله `category` وحده.
ولذلك لا تنشأ أنواع مثل `textual_concept` أو `recitation_concept` أو
`typographic_unit`: هذه كلها `concept` أو `unit` تختلف في `category` لا في `kind`.

ولكل Entry `kind` واحد فقط.

مثلًا:

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

## اسم القيمة يشتق من اسم الأب

اسم القيمة = اسم الأب + الكلمات المميزة لها، وتحذف حروف الربط والتوكيد
(`مع`، `كون`، `جوازًا`، `بحيث`) لأنها لا تميز شيئًا:

```text
علامة الوقف الجائز مع كون الوصل أولى  → waqf_jaiz_wasl_awla
علامة الوقف الجائز مع كون الوقف أولى  → waqf_jaiz_waqf_awla
علامة الوقف اللازم                    → waqf_lazim
```

ولا يكرر اسم الأب إذا لم يضف تمييزًا، فقيم `revelation_classification` تبقى
`makki` و`madani` وليست `revelation_classification_makki`.

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

## العلامة وما تدل عليه

العلامة المرسومة في المصحف مفهوم مستقل عما تدل عليه:

```text
alamat_al_sakt     العلامة المرسومة       mark
saktah             السكتة نفسها           concept

sajdah_mark        علامة موضع السجدة      mark
sujud_al_tilawah   السجود نفسه            concept
```

## هوية العلامة ليست هي المحرف

لا يصلح الـcodepoint معرفًا للعلامة، لسببين ثابتين في يونيكود:

**محرف واحد يخدم علامتين**، فتتحدد العلامة بالمحرف مع موضعه:

```text
U+06DC   ARABIC SMALL HIGH SEEN   →  alamat_al_sakt  أو  sin_al_qiraah
U+06EC   ROUNDED HIGH STOP        →  al_ishmam       أو  al_tashil
```

**وعلامة واحدة لها أكثر من محرف**:

```text
السكون        U+0652   و U+06E1
تنوين الفتح   U+064B   و U+08F0
المدة         U+0653   و U+06E4
```

فالـcodepoint خاصية من خصائص العلامة وليس مفتاحًا لها.

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

المجالات المعتمدة، وهي نفسها أقسام القاموس، فلا تكون قائمتان مختلفتان:

```text
core                  القرآن والمصحف
structure             السورة والآية والكلمة
text                  وحدات النص وتمثيله الرقمي
divisions             الجزء والحزب والربع
surah_classification  الطوال والمئون والمثاني والمفصل
mushaf                الطبعة والتخطيط والصفحة والرسم
dabt                  الضبط: الحركات والتنوين والعلامات
mushaf_marks          علامات المصحف
ayah_numbering        أنظمة عد الآي
revelation            النزول وترتيبه وتصنيفه
qiraat                القراءات والروايات والطرق
recitation            التلاوة والقراء
recitation_pace       التحقيق والتدوير والحدر
recitation_style      المرتل والمجود والمعلم
tajwid                أحكام التجويد
waqf                  الوقف وأحكامه
linguistics           الجذر واللمة والصرف والإعراب
translation           الترجمة
tafsir                التفسير
```

ولا يضاف مجال قبل أن توجد مفاهيم تنتمي إليه، لأن المجال الفارغ يوهم القارئ
بتغطية غير موجودة.

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

القاموس الناتج عن هذا المعيار يستخدم بنية موحدة، ملفًا لكل مفهوم.

الحد الأدنى:

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

وتضاف عند الحاجة:

```yaml
parent:          # لازم إذا كان kind قيمة تصنيف
plural:
symbol:

names:
  arabic:
  dabt:
  by_shape:
  mushaf_introduction:
  unicode:

unicode:         # مولد من قاعدة يونيكود، لا يكتب باليد
alternative_spellings:
english_glosses:
deprecated:
boundaries:
related:
sources:
```

**`origin`** يبين من أين جاء اسم المفهوم. نكتب `quranic` للمصطلح القرآني أو
الشرعي المتخصص، و`borrowed` للمصطلح العام الذي استقر تعريفه عند غيرنا،
و`standard` للمفهوم الذي حدده هذا المعيار للنمذجة ولا نظير له في التراث.

**`tier`** يبين أهمية المفهوم عمليًا. نكتب `core` لما تخزنه التطبيقات فعلًا،
و`extended` للمفهوم الثابت الذي يندر تمثيله أو تختلف حدوده.

**`status`** يبين حال المدخل. يبدأ `draft`، ثم `proposed` بعد النقاش، ثم
`adopted` بعد الاعتماد. ولا نضع `adopted` لمدخل ليس له مصدر.

**`arabic`** لازم في كل مدخل `origin: quranic`. أما المصطلح المستعار فنكتب له
الاسم العربي إذا كان له اسم مستقر، حتى لا نولّد مصطلحات عربية جديدة دون قصد.

مثال:

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

related:
  - waqf
  - waqf_mark

sources:
  - id: quranpedia_tajweed
    ref: "122"
    url: https://tajweed.quranpedia.net/term/show/122
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
Domain fact          ما يثبته المصدر
Standard convention  ما يقرره هذا المعيار
```

## المصادر المعتمدة

```text
qattan_mabahith      مباحث في علوم القرآن — مناع القطان
quranpedia_tajweed   معجم مصطلحات التجويد — 136 مصطلحًا
jamharah_dictionary  معجم المصطلحات الشرعية — الجمهرة
```

وتسجل في `standards/terminology/sources.yml` بصيغة الإحالة الخاصة بكل مصدر:
الصفحة في الكتاب، ورقم المصطلح في المعجم.

ولا يوسم مدخل بـ`adopted` وهو بلا مصدر يثبت تعريفه.

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