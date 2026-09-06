---
title: الهندسة
description: نمذجة البيانات والمعرفات والـ`APIs` والتخزين والعرض والصوت والبحث والتخزين المؤقت في البرمجيات القرآنية، مع الاختبار الذي يقف خلف كل قاعدة.
status: draft
sidebar:
  order: 0
---

هذه الصفحة مسودة. تأخذ قواعد
[أدبيات التعامل مع النص القرآني](/guidelines/ar/02-quranic-text/)
و[معيار المصطلحات](/guidelines/ar/03-terminology/standard/) وتطبقها على أجزاء
النظام التي تحمل المصحف: الجداول والمعرفات والـ`APIs` والملفات والخطوط والصوت
والذاكرة المؤقتة. وحيث يكون الاختيار واحدًا من خيارات عدة يمكن الدفاع عنها، تقول
الصفحة ذلك صراحةً. أما القواعد التي لا خيار فيها فهي التي يفحصها جدول الاختبارات
في آخر الصفحة.

**القاعدة الأم:** نمذج المصحف لا الشاشة. كل جدول وكل `API` وكل ملف يسمي المفهوم
الذي يحمله باسمه في [القاموس](/guidelines/ar/03-terminology/dictionary/)، ويحمل
هوية النص الذي بني منه، ويمكن إعادة بنائه من ذلك النص.

والحالات المذكورة أدناه مأخوذة من
[مسح لقاعدة كود قرآنية في الإنتاج](https://github.com/quran-ws/guidelines/blob/main/surveys/quranpedia-net.md)
مكتوبة بـ`Laravel`. وهي حالات شائعة لا استثنائية، ولهذا صارت قواعد.

## 1. نمذجة البيانات

كل مفهوم في نموذج البيانات مدخل في القاموس، وكل مجموعة مغلقة من القيم سجل
(`registry`).

- السلسلة الأساسية هي
  [`mushaf_edition`](/guidelines/ar/03-terminology/dictionary/#mushaf_edition) ←
  [`surah`](/guidelines/ar/03-terminology/dictionary/#surah) ←
  [`ayah`](/guidelines/ar/03-terminology/dictionary/#ayah) ←
  [`word`](/guidelines/ar/03-terminology/dictionary/#word) ←
  [`token`](/guidelines/ar/03-terminology/dictionary/#token). لكل واحد منها
  جدوله. والـ`token` ناتج تقسيم معلن، فلا يحل محل الكلمة أبدًا.
- [`riwayah`](/guidelines/ar/03-terminology/dictionary/#riwayah)
  و[`ayah_numbering_system`](/guidelines/ar/03-terminology/dictionary/#ayah_numbering_system)
  و[`page`](/guidelines/ar/03-terminology/dictionary/#page)
  و[`line`](/guidelines/ar/03-terminology/dictionary/#line) كيانات لها جداولها،
  لا أعمدة في جدول `ayah`. فرقم الآية يتبع نظام العد، وصفحتها تتبع الطبعة، وعمود
  لأي منهما في صف الآية يثبّت طبعة واحدة داخل النص.
- [`basmalah`](/guidelines/ar/03-terminology/dictionary/#basmalah) حقل مستقل،
  لأن عدها آية صفة في نظام العد (صفحة النص، القسم 5).
- المصحف والتسجيل والـ`dataset` تُربط بالرواية لا بشخص. في قاعدة الكود
  المفحوصة كان `mushafs.rawi_id` و`recitations.rawi_id` يشيران إلى جدول أشخاص
  تحمل صفوفه أسماء روايات، فصار الاستعلام الذي يقصد «كل التسجيلات برواية ورش»
  يعني «كل التسجيلات للرجل ورش»، والاثنان يفترقان بمجرد تحميل رواية ثانية عن
  الراوي نفسه. العمود هو `riwayah_id`، أما `rawi_id` فمكانه صف الرواية.
- عمود التصنيف يخزن أسماء `code` للأعضاء —
  [`makki`](/guidelines/ar/03-terminology/dictionary/#makki)
  و[`madani`](/guidelines/ar/03-terminology/dictionary/#madani)
  و[`disputed`](/guidelines/ar/03-terminology/dictionary/#disputed) — لا نصوص
  عرض. في المخطط المفحوص وجدنا
  `enum('revelation_type', ['meccan', 'medinan'])` وتصديرًا بصيغة JSON فيه
  `surah_type: "مدنية"`: ترجمة إنجليزية بوصفها قيمة، وتسمية عربية بوصفها قيمة،
  ولا موضع للسور المختلف فيها.
- الرقم يخزن رقمًا. التصدير نفسه حمل `surah_number: "2"` و`words_count: "6140"`
  نصوصًا.
- المجموعة المغلقة — أنظمة العد، والقراءات، والسور، ومواضع السجدة — تحمَّل من
  [`standards/terminology/registries/`](https://github.com/quran-ws/guidelines/tree/main/standards/terminology/registries)،
  ولا تكتب باليد `enum` في `migration`.

نموذج أدنى بأسماء الأعمدة القياسية. أنواع الأعمدة خيار من خيارات عدة، أما الأسماء
والمفاتيح الأجنبية فليست كذلك:

```sql
CREATE TABLE ayah_numbering_systems (
  id    INTEGER PRIMARY KEY,
  code  VARCHAR(64) NOT NULL UNIQUE      -- من registries/ayah_numbering.tsv
);

CREATE TABLE mushaf_editions (
  id                        INTEGER PRIMARY KEY,
  code                      VARCHAR(64) NOT NULL UNIQUE,
  riwayah_id                INTEGER NOT NULL REFERENCES riwayahs(id),
  ayah_numbering_system_id  INTEGER NOT NULL REFERENCES ayah_numbering_systems(id),
  version                   VARCHAR(32) NOT NULL,   -- إصدار البيانات، انظر 04
  source_hash               CHAR(64) NOT NULL       -- sha256 لملف المصدر
);

CREATE TABLE ayahs (
  id                        INTEGER PRIMARY KEY,
  mushaf_edition_id         INTEGER NOT NULL REFERENCES mushaf_editions(id),
  surah_number              SMALLINT NOT NULL,
  ayah_number               SMALLINT NOT NULL,
  text                      TEXT NOT NULL COLLATE utf8mb4_bin,
  has_basmalah              BOOLEAN NOT NULL,
  UNIQUE (mushaf_edition_id, surah_number, ayah_number)
);
```

**الفحص:** كل اسم عمود يقابل `code` قياسيًا (الفاحص المستخدم على `examples/`)،
وقيم كل عمود تصنيف مجموعة جزئية من سجله.

## 2. المعرفات والعنونة

موضع في النص هو الثلاثية `(surah_number, ayah_number, ayah_numbering_system)`،
والرقم وحده لا يحدد شيئًا.

- الصيغة المختصرة `ayah_key` (مثل `2:255`) تمثيل نصي لتلك الثلاثية، ولا معنى لها
  إلا بجانب نظام عد معلن. لا تخزنها ولا تتبادلها دونه.
- الكلمة تعنون بـ`word_key` (مثل `2:255:3`): مفتاح الآية مع `word_position`، وفق
  تقسيم معلن (صفحة النص، القسم 4). وإذا تغير التقسيم انتقل كل مفتاح كلمة بعد
  أول كلمة تغيرت، ولهذا يرقّم التقسيم مع الـ`dataset`.
- `id` داخلي وثابت ومبهم. ليس النص، ولا بصمة النص، ولا يعاد استعماله بعد الحذف.
- اللواحق `id` و`number` و`position` و`order` لكل واحدة منها معنى واحد (المعيار،
  القسم 21). المخطط المفحوص حمل `word_index` و`word_number` و`segment_number` في
  جدول واحد، ولم يكن يُعرف من الأسماء هل `word_index` يبدأ من الصفر.

**الفحص:** كل جدول يحمل نصًا قرآنيًا أو يشير إلى موضع فيه عمود
`ayah_numbering_system_id` — مباشرةً أو عبر `mushaf_edition_id` — ومفتاح أجنبي
إلى الطبعة التي بني منها.

## 3. تصميم الـ`API`

مسارات الموارد تستخدم الاسم القياسي والجمع البرمجي، وكل معامل يغير النص يذكر
صراحةً.

- `/surahs/{surah_number}/ayahs/{ayah_number}`، لا `/chapters/{n}/verses/{m}`.
  الترجمات مفاتيح بحث لا أسماء (المعيار، القسم 19).
- `riwayah` و`ayah_numbering_system` معاملان لهما قيمة افتراضية موثقة، والاستجابة
  تعيد القيمة التي طبقت. والافتراض الصامت لحفص والعد الكوفي خطأ لكل قارئ خارجهما،
  وخفي عن كل قارئ داخلهما.
- حقل `text` يعاد كما خزن تمامًا، وبجانبه `source_hash` و`version` الـ`dataset`.
  وبهذا يستطيع العميل إثبات أي نص يعرض.
- الصورة المشتقة — `search_key` أو نص مرمّز بالخط — حقل مستقل، ولا تعاد مكان
  `text` أبدًا.
- الترقيم الصفحي (`pagination`) لا يقطع آية، وصفحة النتائج تنتهي عند حد آية
  (صفحة النص، القسم 7).
- الموضع المجهول يُرد عليه بـ`404` يسمي نظام العد الذي فُحص عليه، لا بأقرب تخمين.

```text
GET /surahs/2/ayahs/255?riwayah=hafs_an_asim&ayah_numbering_system=ayah_numbering_kufi

{
  "ayah_key": "2:255",
  "surah_number": 2,
  "ayah_number": 255,
  "riwayah": "hafs_an_asim",
  "ayah_numbering_system": "ayah_numbering_kufi",
  "mushaf_edition": "…",
  "version": "1.2.0",
  "source_hash": "sha256:…",
  "text": "…",
  "search_key": "…"
}
```

**الفحص:** `lint` على ملف `OpenAPI` يتأكد أن كل مقطع مسار يقابل مدخلًا في
القاموس، وأن كل مخطط يحمل `text` يحمل معه `source_hash` و`version`.

## 4. التخزين والترميز

قاعدة البيانات تقارن النص القرآني بايتًا بايتًا، ولا تغير فيه شيئًا في الدخول
ولا في الخروج.

- ترميز واحد من أول الطريق إلى آخره: `UTF-8` في الملف والعمود والـ`API` والصفحة
  (صفحة النص، القسم 2).
- أعمدة النص تستخدم `collation` ثنائيًا. في MySQL هو `utf8mb4_bin`؛ واختيار
  الـ`collation` واحد من خيارات عدة، أما المطلوب فأن يعيد
  `'مُحَمَّد' = 'محمد'` القيمة `0`.
- لا تطبيع في أي موضع بين الملف والقارئ: لا في الـ`driver`، ولا في الـ`ORM`، ولا في
  خيار «تنظيف المخرجات» في أي `serializer`.
- قائمة المحارف المسموح بها (`whitelist`) تفرض عند الإدخال، والمحرف الخارج عنها
  يفشل الاستيراد.
- فهرس نصي كامل على `text` بـ`collation` يسقط الحركات بحث في الحقل الخطأ. البحث
  يمر عبر `search_key` (القسم 7).

**الفحص:** اختبار الـ`collation` من صفحة النص، القسم 9، وقاعدة `lint` تمنع
`normalize(` في مسار النص.

## 5. عرض المصحف والخطوط

الرسم والضبط والخط ثلاث طبقات، والطبقتان الأوليان وحدهما هما النص (صفحة النص، القسم 3).

- تخطيط الصفحات والأسطر
  ([`layout`](/guidelines/ar/03-terminology/dictionary/#layout)) `dataset`
  مفتاحه `mushaf_edition`. يقول أي الكلمات تقع في أي سطر من أي صفحة، ولا يحمل
  نصًا أبدًا.
- النص المرمّز بالخط — صورة الآية معادةً كتابتها بـ`codepoints` خط
  ([`font`](/guidelines/ar/03-terminology/dictionary/#font)) بعينه — طبقة مشتقة
  تسمي خطها وإصدار الخط وتخزن بصمة المصدر. وليس له مدخل في القاموس بعد، وإلى أن
  يضاف فالاسم المستعمل هو `coded_text`.
- كل إصدار من الخط يقابل بقائمة المحارف عبر جدول `cmap` قبل نشره.
- الخطوط البديلة (`fallback fonts`) ممنوعة على النص القرآني. الشكل
  ([`glyph`](/guidelines/ar/03-terminology/dictionary/#glyph)) المفقود يفشل
  البناء، ولا يرسم بخط آخر أبدًا، لأن الشكل المستبدل قد يُقرأ علامةً أخرى.

```text
صف التخطيط:  mushaf_edition = "…"   page_number = 3   line_number = 7
             word_key = "2:6:1" … "2:7:4"
```

**الفحص:** اختبار تغطية الخط من صفحة النص، القسم 9، واختبار لقطة (`snapshot`)
لكل صفحة من التخطيط.

## 6. الصوت والتلاوة

التسجيل [`recitation`](/guidelines/ar/03-terminology/dictionary/#recitation)
يؤديه [`reciter`](/guidelines/ar/03-terminology/dictionary/#reciter) في
`riwayah`، ولها
[`recitation_style`](/guidelines/ar/03-terminology/dictionary/#recitation_style)
و[`recitation_pace`](/guidelines/ar/03-terminology/dictionary/#recitation_pace).

- القارئ ليس راويًا. مؤدي التسجيل يربط بالرواية التي يقرأ بها، ولا يدخل بوصفه
  راويها.
- قاعدة الكود المفحوصة سمت جدولًا `recitation_types` وملأته بـ«مرتل» و«مجود»
  و«معلم». هذا نمط الأداء، وكلمة `type` هي الاسم المبهم الذي يمنعه المعيار
  (القسم 24). والتطبيق نفسه صنف التسجيلات «حسب السور» و«حسب الآيات» تحت
  `recitation_classification`، وهذه كيفية تقطيع الصوت، وهي صفة في الملفات لا في
  التلاوة.
- [`ayah_timing`](/guidelines/ar/03-terminology/dictionary/#ayah_timing)
  و`word_timing` طبقتان مشتقتان. وكل ملف توقيت يسمي بصمة الصوت الذي جرت محاذاته عليه،
  وإصدار النص، ونظام العد، حتى ينكشف الملف المحاذى على تقطيع آخر للصوت.
- البث والإذاعات وقوائم التشغيل مفاهيم تطبيقية. التطبيق يسميها، والمعيار لا يفعل
  (المعيار، القسم 30).

```text
# ayah_timing v1
# recitation:             …
# reciter:                …
# riwayah:                hafs_an_asim
# audio_sha256:           …
# text_version:           1.2.0
# ayah_numbering_system:  ayah_numbering_kufi
ayah_key   start_ms   end_ms
1:1        0          5320
1:2        5320       9870
```

**الفحص:** كل ملف توقيت يحمل بصمة الصوت وإصدار النص في ترويسته، وخطوة في البناء
تتحقق منهما على البيانات الحالية.

## 7. البحث

`search_key` يشتق من `text` بدالة حتمية (`deterministic`) مرقّمة الإصدار، ولا
يراه القارئ أبدًا (صفحة النص، القسم 6).

- الاشتقاق يحذف الضبط والتطويل، ويوحد صور الهمزة مع كرسيها من الألف أو الياء أو
  الواو، ويوحد الألف المقصورة مع الياء والتاء المربوطة مع الهاء حيث لا ينبغي
  للبحث أن يفرق بينها، ولا شيء غير ذلك. وما توحده الدالة قرار يكتب، أما كونها
  دالة واحدة فليس قرارًا.
- للدالة إصدار. وتغييرها تغيير في الـ`dataset`، ويعاد بناء الفهرس.
- النتيجة تربط بموضع وبالنص المخزن `text`، لا بالمفتاح أبدًا.

```text
search_key(text):
  1. حذف علامات الضبط والتطويل (U+0640)
  2. أ إ آ ٱ ← ا     ؤ ← و     ئ ← ي
  3. ى ← ي           ة ← ه
  4. دمج المسافات المتتالية
```

**الفحص:** حالات ذهبية للاشتقاق — مدخل ومفتاحه المتوقع — على نمط
`tools/test_translit.py`، واختبار يتأكد أن الفهرس الحالي بني بإصدار الدالة
الحالي.

## 8. الأداء والتخزين المؤقت

مفتاح الذاكرة المؤقتة يسمي كل ما يغير النص، والذاكرة المؤقتة للنص القرآني لا
تبطل بمرور الوقت وحده أبدًا.

- المفتاح يتضمن إصدار الـ`dataset` والطبعة والرواية ونظام العد. وكون اثنين منها
  يأخذان القيمة الافتراضية نفسها اليوم ليس سببًا لحذفهما.
- إصدار بيانات من درجة `MAJOR` (انظر
  [الإصدارات والتصحيحات](/guidelines/ar/04-versioning/)) يبطل كل ذاكرة مؤقتة
  لنص بني على الإصدار السابق.
- كائنات الـ`CDN` التي تحمل النص ثابتة لا تعدل، والإصدار في المسار لا في
  `query string` قد يسقطه وسيط.

```text
مفتاح الذاكرة المؤقتة:  ayah:{version}:{mushaf_edition}:{ayah_numbering_system}:{ayah_key}
                        ayah:1.2.0:…:ayah_numbering_kufi:2:255

مسار الـCDN:            /text/1.2.0/{mushaf_edition}/2/255.json
```

**الفحص:** اختبار لصيغة مفتاح الذاكرة المؤقتة، واختبار يتأكد أن رفع الإصدار يغير
كل روابط النص.

## 9. التسمية في الكود

معيار المصطلحات يلزم الطبقات الأربع — النموذج والجدول والمفتاح الأجنبي والـ`API` —
بمفردات واحدة (المعيار، القسم 26).

```text
النموذج:         Ayah            Riwayah
الجدول:          ayahs           riwayahs
المفتاح الأجنبي:  ayah_id         riwayah_id
الـAPI:          /ayahs          /riwayahs
```

- قاعدة الكود المفحوصة سمت مفهومًا واحدًا بثلاث صور: تهجئة مبتورة في النموذج،
  والتهجئة نفسها مع `s` على الجدول، والجمع العربي `/qiraat` في المسار. التهجئة
  القياسية `qiraah` والمجموعة `qiraahs`، والجمع العربي ليس اسم مجموعة (المعيار،
  القسم 11).
- واجهة المستخدم قد تترجم الاسم أو تعرضه بصورة مختلفة، أما الطبقات الأربع فلا.
- شغّل الفحص في الـ`CI`:
  `python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict`.
  يبلّغ عن الاسم المهجور، والتهجئة غير القياسية، والترجمة، والجمع العربي، مع
  القسم الذي يقف خلف كل واحد منها، ولا يعيد تسمية شيء.

**الفحص:** سكربت الفحص نفسه، بخيار `--strict`، على كل `pull request`.

## كل قاعدة تصير اختبارًا

الاختبار الذي يفشل يوقف النشر، ولا يعيد كتابة البيانات أبدًا.

| ما يختبر | كيف |
| --- | --- |
| أسماء المخطط قياسية | كل اسم جدول وعمود يقابل `code` في القاموس |
| قيم التصنيف أعضاء في السجل | القيم المميزة لكل عمود تصنيف ⊆ سجله |
| الأرقام أرقام | لا حقيقة رقمية مخزنة في عمود نصي |
| رواية لا راوٍ | لا `rawi_id` على مصحف ولا تسجيل ولا `dataset` |
| نظام العد صريح | كل جدول نص وكل نقطة نهاية للنص تحمل `ayah_numbering_system` |
| استجابات النص تحمل هويتها | كل مخطط فيه `text` فيه `source_hash` و`version` |
| `collation` ثنائي | `SELECT 'مُحَمَّد' = 'محمد';` يعيد `0` |
| لا تطبيع في مسار النص | قاعدة `lint` تمنع `normalize(` بين الملف والقارئ |
| الخط يغطي النص | جدول `cmap` لكل إصدار من الخط يغطي القائمة، ولا خط بديل في مسار النص |
| التخطيط يطابق النص | لقطة لكل صفحة، تعاد من `dataset` التخطيط والنص |
| ملفات التوقيت تسمي مصادرها | الترويسة تحمل `audio_sha256` و`text_version`، وكلاهما يتحقق منه |
| اشتقاق مفتاح البحث | حالات ذهبية مدخل ← مفتاح، وإصدار الفهرس يساوي إصدار الدالة |
| مفتاح الذاكرة المؤقتة يتضمن الإصدار | اختبار للصيغة، ورفع الإصدار يغير كل روابط النص |
| الأسماء عبر الطبقات الأربع | `audit_terminology.py --strict` يمر |
