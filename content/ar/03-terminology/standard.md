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

## المفهوم قبل الاسم

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

## اسم Canonical واحد لكل مفهوم

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

## متى نستخدم المصطلح القرآني؟

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

### القاعدة نفسها داخل الاسم المركب

الاسم المركب قد يجمع كلمة اصطلاحية وكلمة عامة. فننقل الاصطلاحية ونترجم العامة:

```text
المِيم الصَّغِيرَة    → small_meem        لا meem_saghirah
الصِّفْر المُسْتَدِير → rounded_zero      لا sifr_mustadir
الثَّلَاث نُقَط      → three_dots        لا thalath_nuqat
الأَلِف المَحْذُوفَة  → omitted_alif      لا alif_mahdhufah
```

`saghirah` لا تزيد شيئًا على `small`، والقارئ العربي والإنجليزي كلاهما يخسر بها.

والصفة المترجمة تتقدم على موصوفها، لأن هذا ترتيب الإنجليزية.

أما الكلمة الاصطلاحية فتبقى منقولة، ولو بدت مألوفة:

```text
النُّون السَّاكِنَة  → noon_sakinah    فـ«ساكنة» مصطلح تجويدي
الوَقْف اللَّازِم    → waqf_lazim      فـ«لازم» مصطلح في الوقف
```

الكلمات العامة مسجلة في `standards/terminology/data/general_words.tsv`،
وتترجم حيثما وردت.

القاعدة:

> **Quran-specific concepts retain Quranic names; general concepts use natural technical English.**

---

## Canonical Code Spelling

عندما نقرر استخدام مصطلح عربي الأصل، يعتمد له المعيار تهجئة برمجية واحدة:

**Canonical Code Spelling**

الهدف ليس بناء نظام نقل حرفي دقيق مثل ALA-LC أو DIN 31635، وإنما spelling بسيط، ثابت، ومتوقع للمطورين.

### القواعد العامة

- ASCII-friendly.
- لا تستخدم علامات النقل الدقيق:
  `ā`, `ī`, `ū`, `ʿ`, `ʾ`.
- لا تستخدم `'` لتمثيل الهمزة أو العين.
- لكل مصطلح spelling واحد معتمد.
- التهجئات الشائعة الأخرى تسجل كـ`alternative_spellings`.

### كيف تُشتق التهجئة

قواعد الأقسام من 4 إلى 8 قواعد آلية يمكن تنفيذها في برنامج. لذلك نشتق
الـCanonical Code Spelling من الاسم العربي بالحركات بدالة واحدة، ولا نتركها
لاجتهاد كل مشروع.

```bash
python3 tools/translit.py "سُورَة" "رُبْع الحِزْب"
سُورَة        surah      Surah
رُبْع الحِزْب   rubu_al_hizb   Rubu al-Hizb
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

## التاء المربوطة

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

### التاء المربوطة في الإضافة

التاء المربوطة تنطق تاءً إذا كانت الكلمة مضافة إلى ما بعدها، فتكتب `t` لا `h`:

```text
همزة الوصل    → hamzat_al_wasl     لا hamzah_al_wasl
سجدة التلاوة  → sajdat_al_tilawah  لا sajdah_al_tilawah
```

والقاعدة آلية: التاء المربوطة في آخر الاسم تعطي `h`، وفي غير آخره تعطي `t`.
ويتحقق منها `tools/test_translit.py`.

---

## حروف المد

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

### ياء النسب

الياء المشددة في آخر الاسم المنسوب تعطي `i` واحدة:

```text
مكي     → Makki      لا Makkiyy
مدني    → Madani     لا Madaniyy
عثماني  → Uthmani    لا Uthmaniyy
```

### أسماء الحروف تكتب كما تُنطق

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
small_noon         اسم حرف، فيكتب كما ينطق
seen_al_qiraah     اسم حرف
tajwid             ليس اسم حرف، فيشتق (لا tajweed)
haqiqi             ليس اسم حرف، فيشتق (لا haqeeqi)
makki              ليس اسم حرف، فيشتق (لا makkee)
```

أسماء الحروف الـ28 في `standards/terminology/data/letter_names.tsv`، وتقرؤها
الدالة منه. والسبب أن اسم الحرف لا يحمل معنى غير صوته، وسبب الاستثناء وقياسه في
[سجل القرارات](/guidelines/ar/03-terminology/decisions/).

### `tajwid` يكتب بالقاعدة

نكتب `tajwid` في حقل `code` مع أن `tajweed` أكثر استعمالًا، لأن القاعدة الواحدة
المطردة أنفع من استثناء يفتح لكل كلمة بابًا.

ولا يضيع الاستعمال الغالب، لأن لكل مفهوم حقلين:

```text
code     tajwid     مشتق بالقاعدة، وهو ما يكتب في الشفرة
display  Tajweed    مقيس بالاستعمال، وهو ما يقرؤه القارئ
```

ونسجل `tajweed` كذلك في `alternative_spellings`، فيجدها البحث والمرادفات.

> **غير محسوم:** `ت` و`ط` كلاهما يعطي `taa`، و`ح` و`ه` كلاهما يعطي `haa`،
> لأن القسم 4 يجمع المفخم والمرقق عمدًا. ولا يستعمل أي منهما اسمًا في مدخل
> اليوم، فالتصادم مسجل ولم يعالج. و`tools/build_aliases.py` يفشل إن ادعى
> مفهومان اسمًا واحدًا.

---

## الهمزة والعين

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

### الهمزة والعين في آخر الكلمة

الحذف في آخر الكلمة يقطعها قبل موضعها، فيصير `ربع` هو `rub` و`جمع` هو `jam`،
وهذه كلمات إنجليزية أخرى لا صلة لها بالمعنى.

لذلك إذا وقعت الهمزة أو العين في آخر الكلمة، وكان ما قبلها ساكنًا، كررنا الحركة
التي قبلها:

```text
رُبْع    → rubu
جَمْع    → jama
قَطْع    → qata
الرَّفْع → rafa
```

وإذا كان ما قبلها حرف مد فالكلمة منتهية بحركة أصلًا، فلا نزيد شيئًا:

```text
الرُّكُوع  → ruku
المَمْنُوع → mamnu
المُقَطَّع → muqatta
مَوْضِع    → mawdi
```

والهمزة والعين في وسط الكلمة تحذفان كما سبق، وتبقى حركتهما: `muallim`،
`qiraah`. ولكل حالة من هذه الحالات اختبار في `tools/test_translit.py`.

### الأسماء المستقرة

بعض الأسماء استقرت في البرمجيات القرآنية على صورة واحدة، فاشتقاق غيرها صحيح
وغير مفيد. مثال ذلك `juz`: الاشتقاق يعطي `juzu`، والاستعمال يعطي `juz` بفارق
كبير.

هذه الأسماء مسجلة في `standards/terminology/data/established_spellings.tsv`،
ولا يقبل فيها سطر إلا ومعه قياس يثبت أن الصورة المشتقة لا تكاد تستعمل. ورجحان
الاستعمال وحده لا يكفي، وإلا دخل `tajweed`. والقياس الذي بنيت عليه الحالتان في
[سجل القرارات](/guidelines/ar/03-terminology/decisions/).

---

## الأسماء المركبة و`al-`

عند الاحتفاظ بمصطلح عربي مركب نستخدم صيغة ثابتة قدر الإمكان:

```text
Rubu al-Hizb
Asbab al-Nuzul
Sujud al-Tilawah
```

ولا نغير `al-` بحسب الحروف الشمسية لأغراض الـCanonical spelling.

وفي identifiers:

```text
rubu_al_hizb
asbab_al_nuzul
sujud_al_tilawah
```

### متى تحذف `al`؟

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
النون الساكنة    → noon_sakinah    لا noon_al_sakinah
الرسم العثماني   → rasm_uthmani    لا rasm_al_uthmani
```

والتمييز بينهما آلي. إذا كان الاسم الأول معرفًا بـ`ال` فما بعده صفة، وتحذف
أداة تعريفها. وإذا كان الاسم الأول نكرة فما بعده مضاف إليه، وتثبت فيه `al`:

```text
رُبْع الحِزْب      → rubu_al_hizb   (الأول نكرة، فهي إضافة)
الوَقْف اللَّازِم   → waqf_lazim    (الأول معرفة، فهي صفة)
```

---

## Code Name وDisplay Name

الاسم البرمجي لا يلزم أن يكون هو صورة النقل الدقيق.

يمكن أن يكون:

```text
Code:     qiraah
Display:  Qirāʾah
Arabic:   قراءة
```

الـCanonical Code Spelling يجب أن يبقى مستقرًا، بينما يمكن أن تختلف طريقة العرض بحسب اللغة والجمهور والسياق.

### حقول التسمية

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

#### الحقول

**`code`** هو المعرف الثابت المستخدم في الكود والـAPI وقواعد البيانات. نولده
حسب قواعد الأقسام 4 إلى 8، ولا نغيره لاحقًا لمجرد وجود اسم أكثر شيوعًا.

**`display`** هو الاسم الذي يظهر للمستخدم في التوثيق والواجهات. نختار التهجئة
الإنجليزية الأكثر شيوعًا، ونسجل مصدر هذا الاختيار في `display_evidence`.

**`transliteration`** هو النقل الدقيق للاسم بحروف لاتينية، على نظام ALA-LC أو
DIN 31635. نكتبه عند الحاجة فقط، وهو حقل اختياري.

**`arabic.vocalized`** هو الاسم العربي مكتوبًا بالحركات. نشتق منه `code`، ولا
نستطيع اشتقاق `code` بدونه.

وهو اسم المفهوم عندنا، وقد يخالف اسم المصدر له. فاسم المصدر يحفظ في `dabt`
أو في `mushaf_introduction`، ولا يضيع.

ولا يعدل `arabic.vocalized` للوصول إلى اسم برمجي مرغوب، فتعديله تغيير للاسم
العربي نفسه، ولا يقبل إلا بحجة عربية: أن الاسم الجديد أدل على حدود المفهوم.
مثاله `division_mark`: العلامة تدل على بداية الجزء والحزب ونصفه وربعه، فاسم
«التقسيم» أوسع من «التحزيب» وأدل على ما تدل عليه العلامة.

**`dabt`** هو اسم العلامة في علم الضبط. ننقله كما ورد في مصدره.

**`by_shape`** هو وصف صورة العلامة كما ترسم في المصحف. ننقله كما ورد في مصدره.

**`mushaf_introduction`** هو اسم العلامة كما ورد في مقدمة المصحف. نكتب `null`
إذا لم تذكر المقدمة اسمًا لها، وهذه معلومة عن المصدر نفسه.

**`unicode`** هو اسم المحرف في يونيكود. نقرؤه من قاعدة يونيكود، ولا نستخدمه
معرفًا في الكود.

**`alternative_spellings`** يحتوي على التهجئات البديلة المعروفة. نستخدمها في
البحث وربط المدخلات المختلفة بالمفهوم نفسه.

#### قواعد ثابتة

- `code` و`display` قد يختلفان، وهذا مقصود.
- لا نستخدم اسم يونيكود معرفًا في الكود، لأنه يصف صورة المحرف ولا يصف وظيفته،
  وقد يخدم المحرف الواحد علامتين مختلفتين.
- خلو `mushaf_introduction` معلومة عن المصدر، وليس نقصًا في المدخل.

---

## شكل الأسماء في الكود

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

## المفرد والجمع

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

ويفحص `tools/check_conformance.py` أن الجمع هو الاسم البرمجي وسين.

---

## كل Entry له Kind

ليست كل المصطلحات من النوع نفسه.

يحدد لكل Entry دوره البنيوي، من قائمة **مغلقة** لا يزاد عليها. والقائمة
مسجلة في `standards/terminology/schema.json`، ويفحصها `tools/validate.py`:

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

### كل علامة تتبع عائلتها

علامات الضبط ليست قائمة واحدة، فلكل علامة عائلة تنتمي إليها، وهي أبوها:

```text
mushaf_mark
├── harakah            الفتحة والضمة والكسرة والسكون والشدة
├── tanwin             تنوين الضم والفتح والكسر
├── ijam               النقطة والنقطتان والثلاث نقط
├── orthographic_mark  الهمزة والمدة والحروف الصغيرة
├── qiraah_mark        السكت والإشمام والتسهيل والإمالة
└── waqf_mark_type     اللازم والممنوع والجائز بأنواعه
```

ولا نجعل `mushaf_mark` أبًا لكل علامة، لأن الأب الواحد فوق 37 علامة لا يفيد
شيئًا. ويبقى أبًا للعلامات التي لا عائلة لها.

---

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

## نفرد الأنواع والقيم

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
Ayah Numbering System
├── Madani Awwal
├── Madani Akhir
├── Makki
├── Basri
├── Dimashqi
└── Kufi
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

### أفراد المجموعة المغلقة تذهب إلى سجل

المجموعة المغلقة لا تفرد entries، بل تجعل سجلًا: ملفًا مفصولًا بالجدولة لكل
مجموعة في `standards/terminology/registries/`، سطرًا لكل فرد.

والفرق بين النوع والفرد أن قيم النوع مفاهيم. فلـ`Revelation Classification`
3 قيم، ويسأل القارئ ما معنى `Makki` فيجد جوابًا ليس تعدادًا. أما `Qiraah`
فليست له قيم بهذا المعنى، بل له 10 أفراد، وحفص رجل لا مفهوم، ولا جواب للسؤال
عن معناه غير الإشارة إليه.

```text
Qiraah          → registries/qiraat.tsv        10 قراءات، 19 راويًا، 20 رواية
Surah           → registries/surahs.tsv        114 سورة
Mawdi al-Sajdah → registries/sajdah.tsv        15 موضعًا
```

ويبقى للمفهوم entry تسمي سجله:

```yaml
concept: qiraah
kind: concept
registry: qiraat
```

ونفرق بينهما بسؤال واحد: هل عند الفرد ما يقوله عن نفسه؟ فإذا احتاج إلى
`definition` و`purpose` و`boundaries` فهو مفهوم يفرد له entry، وإذا كان كل ما
نقوله فيه اسمه وموقعه من المجموعة وموضع وروده فهو فرد يأخذ سطرًا. ولهذا وضعنا
أسماء الحروف الـ28 في `data/letter_names.tsv` قبل أن تكون هناك سجلات.

والسجل ليس أدنى مرتبة من الـentry. فكل سطر فيه يفحصه
`tools/check_registries.py`، وله مصدر كما للـentry مصدر، ويفهرس حتى تحل كل
تهجئة لفرد إلى موضعه.

### اسم الشخص لا يشتق

اسم الشخص يكتب كما جرت كتابته، ولا يمر بالأقسام 4 إلى 8 التي تشتق الاسم البرمجي
من العربية المشكولة:

```text
hafs        warsh        qalun        ibn_dhakwan
```

والسبب أن الاشتقاق وضع للمصطلح، وهو كلمة تحمل معنى يبقيه الاشتقاق موصولًا
بالمعرف. أما اسم الشخص فلا معنى فيه، واشتقاقه يعطي تهجئة لا يكتبها أحد.

وهذا الاستثناء يشمل الأشخاص وحدهم. أما اسم السورة فكلمة تشتق — `fatihah`
و`baqarah` و`nisa` — ويعيد `tools/check_registries.py` اشتقاق السور الـ114 في
كل تشغيل.

و«كما جرت كتابته» تحتاج إلى شاهد. فالسجل يسجل الصورة العلمية الإنجليزية
بعلاماتها، والاسم المستعمل هو تلك الصورة بلا علامات. وإذا خالفت هذه الصورة
قاعدة نص عليها المعيار فالقاعدة مقدمة: `shubah` لا `shuba`، لأن القسم 5 يحكم
التاء المربوطة.

### قد يشترك الفرد والمفهوم في الاسم

يجوز أن يحمل الفرد اسم مفهوم، ولا نغير أحد الاسمين. فحمزة مقرئ، و`hamzah` هي
العلامة كذلك. والطارق سورة، و`tariq` درجة في سلسلة النقل.

والاشتراك لا يضر لأن الاسمين في domain مختلفين، بالمعنى المذكور في القسم 25.
فأحد الحمزتين `dabt` والآخر `qiraat`، وأحد الطريقين `qiraat` والآخر
`structure`، ولا يطلبهما طلب واحد. وإنما يلزم تفرد الاسم حيث يمكن أن يقع اللبس.

ونفهرس أسماء الأفراد بحسب الـkind لا بحسب الـdomain، لأن الـkind أدق ولأنه ما
يعرفه من يقرأ البيانات: فالعمود لا يحمل «شيئًا من domain القراءات»، بل يحمل
رواية.

```text
hamzah          → العلامة
qiraah:hamzah   → المقرئ
tariq           → درجة النقل
surah:tariq     → السورة
```

والاسم المجرد يحل إلى المفهوم دائمًا. ومن يملأ عمودًا معلومًا يسأل داخل الـ
namespace الخاص به. ويبقى `aliases.json` للمفاهيم، و`registry_aliases.json`
للأفراد.

---

## Parent وChild

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

### اسم القيمة يشتق من اسم الأب

اسم القيمة = اسم الأب + الكلمات المميزة لها، وتحذف حروف الربط والتوكيد
(`مع`، `كون`، `جوازًا`، `بحيث`) لأنها لا تميز شيئًا:

```text
علامة الوقف الجائز مع كون الوصل أولى  → waqf_jaiz_wasl_awla
علامة الوقف الجائز مع كون الوقف أولى  → waqf_jaiz_waqf_awla
علامة الوقف اللازم                    → waqf_lazim
```

ولا يكرر اسم الأب إذا لم يضف تمييزًا، فقيم `revelation_classification` تبقى
`makki` و`madani` وليست `revelation_classification_makki`.

ويفحص `tools/check_conformance.py` أن لكل تصنيف قيمًا تنتمي إليه.

---

## Definition

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

## Purpose

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

### الفرق

```text
Definition → What is it?
Purpose    → Why do we model it?
```

لا يعيد `purpose` صياغة `definition`.

ولا نضع تفاصيل الاستخدام البرمجي داخل `definition`.

إذا لم يكن للمفهوم غرض برمجي واضح، فهذا سبب لمراجعة الحاجة إلى إدخاله في القاموس الأساسي.

---

## حدود المفهوم

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

## المفاهيم المتشابهة تبقى منفصلة

لا ندمج مفهومين لأن ترجمتهما متشابهة.

### العلامة وما تدل عليه

العلامة المرسومة في المصحف مفهوم مستقل عما تدل عليه:

```text
saktah_mark        العلامة المرسومة       mark
saktah             السكتة نفسها           concept

sajdah_mark        علامة موضع السجدة      mark
mawdi_al_sajdah    الموضع نفسه            concept
sujud_al_tilawah   السجود نفسه            concept

ayah_mark          العلامة المرسومة       mark
fasilah            خاتمة الآية            concept
```

فالسجدة ثلاثة مفاهيم لا واحد: علامة، وموضع من النص، وفعل. وجمعها في اسم واحد
يجعل للسجود رقم صفحة.

### هوية العلامة ليست هي المحرف

لا يصلح الـcodepoint معرفًا للعلامة، لسببين ثابتين في يونيكود:

**محرف واحد يخدم علامتين**، فتتحدد العلامة بالمحرف مع موضعه:

```text
U+06DC   ARABIC SMALL HIGH SEEN   →  saktah_mark  أو  seen_al_qiraah
U+06EC   ROUNDED HIGH STOP        →  al_ishmam       أو  al_tashil
```

**وعلامة واحدة لها أكثر من محرف**:

```text
السكون        U+0652   و U+06E1
تنوين الفتح   U+064B   و U+08F0
المدة         U+0653   و U+06E4
```

فالـcodepoint خاصية من خصائص العلامة وليس مفتاحًا لها.

### النص

```text
Word
Token
Morpheme
Lemma
Root
```

### التمثيل الرقمي

```text
Letter
Character
Codepoint
Grapheme
Glyph
```

### القرآن والمصحف

```text
Quran
Mushaf
```

### المحتوى والعرض

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

### النص والتحليل

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

## الاسم والتهجئة والترجمة ليست شيئًا واحدًا

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

ويفحص `tools/check_conformance.py` أن المقابل الإنجليزي غير مسجل تهجئةً بديلة.

---

## Deprecated لا يعني Incorrect

نفرق بين:

#### Alternative

صيغة أخرى صحيحة أو شائعة:

```text
Tajweed → alternative spelling of Tajwid
```

#### Deprecated / Discouraged

اسم مفهوم، لكنه غير موصى به في المشاريع الجديدة.

#### Incorrect

اسم يشير إلى مفهوم مختلف أو يؤدي إلى معنى غير صحيح.

مثلًا قد تكون `Verse` ترجمة إنجليزية صحيحة لـ`Ayah`، لكنها ليست الـCanonical name في المعيار.

---

## المعرفات والأرقام والترتيب

لكل suffix معنى ثابت.

### `id`

معرف داخلي:

```text
surah_id
ayah_id
word_id
mushaf_id
```

### `number`

رقم معتمد داخل المجال:

```text
surah_number
ayah_number
page_number
```

### `position`

موضع العنصر داخل parent أو sequence:

```text
word_position
token_position
line_position
```

### `order`

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

## العلاقات

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

## العمليات والأفعال

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

## Classifications وBooleans

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

## تنظيم المجالات

ينظم القاموس حسب domains واضحة، وليس في قائمة واحدة مسطحة.

المجالات المعتمدة، وهي نفسها أقسام القاموس، فلا تكون قائمتان مختلفتان. وهي
مسجلة في `standards/terminology/schema.json`، ويفحصها `tools/validate.py`:

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
quranic_sciences      النسخ وغريب القرآن والمتشابهات
```

ولا يضاف مجال قبل أن توجد مفاهيم تنتمي إليه، لأن المجال الفارغ يوهم القارئ
بتغطية غير موجودة.

---

## الاتساق بين طبقات النظام

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

## بنية Entry في القاموس

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

definition_en:   # ترجمة definition، والقاموس الإنجليزي يولد منها
purpose_en:      # ترجمة purpose
boundaries_en:   # ترجمة boundaries، سطرًا بسطر
note_en:         # ترجمة note
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

### المدخل بلغتين

المدخل واحد، ونصه بلغتين. كل حقل نثري له توأم إنجليزي: `definition_en`
و`purpose_en` و`boundaries_en` و`note_en`. ومنه تولد صفحة القاموس
الإنجليزية، كما تولد العربية من الحقول العربية، فلا يفترق النصان.

والتوأم **ترجمة لا تعريف ثانٍ**. فما يقرره أحدهما يقرره الآخر، ولا يزيد
الإنجليزي قيدًا ولا يسقط قيدًا. وحدود المفهوم تترجم سطرًا بسطر، لكل سطر عربي
سطر إنجليزي في موضعه.

وفي الترجمة نلتزم أربعة أمور:

- **المصطلح يذكر باسمه المعتمد**، أي بـ`display` الذي في مدخله: نكتب Ayah لا
  verse، وMushaf لا codex. والمقابل الإنجليزي في `english_glosses` مدخل بحث،
  لا اسم يستعمل في النص.
- **الاسم البرمجي يكتب كما هو** بين علامتي `` ` ``، فلا يترجم ولا يعرّب.
- **الصيغة المكررة تترجم بصيغة مكررة**: مداخل عد الآي الستة تشترك في جملة غرض
  واحدة بالعربية، فتشترك في واحدة بالإنجليزية بلفظها.
- **لا يبقى في الحقل الإنجليزي نص عربي** إلا اسمًا عربيًا يتحدث عنه المدخل
  نفسه، فيوضع بين «…». و`tools/check_conformance.py` يتحقق من ذلك.

ولا يعرض هذا على أنه ترجمة معتمدة للنص الشرعي؛ إنما هو بيان المفهوم بلغة
ثانية لمن يبني به.

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

## مصادر التعريفات

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

### المصادر المعتمدة

المصادر مسجلة في `standards/terminology/sources.yml`، ومعها صيغة الإحالة الخاصة
بكل مصدر: الصفحة في الكتاب، ورقم المصطلح في المعجم. ولا تكتب قائمتها في هذه
الصفحة حتى لا يكون لها موضعان.

ويفحص `tools/check_registries.py` أن كل إحالة تسمي مصدرًا موجودًا في الملف.

ولا يوسم مدخل بـ`adopted` وهو بلا مصدر يثبت تعريفه.

---

## القاموس Machine-readable

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

## قاعدة قبول أي مصطلح جديد

### أولًا: هل المفهوم لنا أن نسميه؟

يدخل المفهوم في هذا المعيار إذا **لم يمكن تعريفه دون الرجوع إلى القرآن أو
المصحف**.

وما سوى ذلك مما يخزنه التطبيق فحق، وليس لنا:

```text
داخل:
mawdi_al_sajdah   موضع من النص القرآني
ayah_timing       مدى من الصوت يقابل آية
gharib_al_quran   معنى لفظة قرآنية
mutashabihat      ألفاظ تتكرر داخل القرآن

خارج:
book, author, chapter, category, tag, language, attachment, source
radio, stream, thumbnail, user, subscription
fatwa, hadith, athar, topic
```

فـ`radio` يخرج لأن بث التلاوة بث، وليس فيه ما يحتاج إلى تعريف قرآني. و`fatwa`
يخرج كما يخرج الحديث، فهو علم إسلامي وليس مفهومًا من مفاهيم النص القرآني.
و`book` يخرج لأن اللغة سمت الكتاب كتابًا، ولا نزيد على ذلك.

ونقول ذلك صراحة، لأن المشروع يبقى محتاجًا إلى أسماء لكتبه ووسومه، والمعيار لا
يعطيه إياها. وسبب هذا الحد وبديله المرفوض في
[سجل القرارات](/guidelines/ar/03-terminology/decisions/).

> **نسمي علوم القرآن، ونقف عندها.**

### ثانيًا: المدخل نفسه

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

## المبادئ الأساسية

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