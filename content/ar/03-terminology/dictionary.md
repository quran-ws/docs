# Quranic Software Terminology Dictionary

معجم معياري للمفاهيم المستخدمة في البرمجيات والتطبيقات القرآنية، مبني على **Quranic Software Terminology Standard**.

لكل مصطلح:

- **Canonical**: الاسم البرمجي المعتمد، مشتقًا بقواعد الأقسام 4 إلى 8 من المعيار.
- **Kind**: دور المدخل البنيوي، من القائمة المغلقة في القسم 12.
- **Parent**: المفهوم الأب عند وجوده، ولازم في قيم التصنيفات.
- **Tier**: `core` لما تخزنه التطبيقات، و`extended` لما هو ثابت نادر النمذجة.
- **Definition**: ما هو المفهوم؟
- **Purpose**: لماذا نمثله برمجيًا؟
- **Alternative**: تهجئات أخرى للاسم نفسه.
- **English gloss**: ترجمة أو شرح إنجليزي، وليست اسمًا Canonical.
- **Mushaf introduction**: اسم العلامة كما ورد في مقدمة المصحف، وخلوه خبر عن
  المصدر لا نقص في المدخل.

> هذا القاموس مسودة. المصدر البرمجي له `standards/terminology/concepts/*.yml`،
> وهذا الملف مخرج منه، فلا يعدل فيه ما يمكن توليده.

---

# 1. Core

## Quran — القرآن

**Canonical:** `Quran`  
**Kind:** `concept`

**Definition:**  
كلام الله المنزل على محمد ﷺ والمتعبد بتلاوته، ويطلق على مجموعه وعلى بعضه بحسب السياق.

**Purpose:**  
يمثل المحتوى القرآني نفسه بصورة مستقلة عن مصحف أو تخطيط أو تنسيق أو تمثيل رقمي معين.

**Alternative spellings:** `Qur'an`, `Qur’an`, `Koran`

---

## Mushaf — المصحف

**Canonical:** `Mushaf`  
**Plural:** `Mushafs`  
**Kind:** `entity`

**Definition:**  
الصحف التي جمع فيها القرآن مكتوبًا ومرتبًا؛ فالمصحف وعاء مكتوب للقرآن وليس مرادفًا مطلقًا للقرآن نفسه.

**Purpose:**  
يستخدم عندما تكون خصائص التمثيل المكتوب للقرآن مهمة، مثل الرسم والتخطيط والصفحات والأسطر والعلامات.

**Alternative spellings:** `Mus'haf`, `Muṣḥaf`  
**English gloss:** `Quran Codex`

---


# 2. Structure

## Surah — السورة

**Canonical:** `Surah`  
**Plural:** `Surahs`  
**Kind:** `entity`

**Definition:**  
وحدة رئيسية من بنية القرآن، تتكون من آيات مرتبة ولها اسم وموضع معروف في ترتيب المصحف.

**Purpose:**  
تستخدم كوحدة رئيسية لتنظيم النص وربط الآيات والبيانات المتعلقة بالسورة.

**Alternative spelling:** `Sura`  
**English gloss:** `Chapter`

---

## Ayah — الآية

**Canonical:** `Ayah`  
**Plural:** `Ayahs`  
**Kind:** `entity`  
**Parent:** `Surah`

**Definition:**  
وحدة من النص القرآني تقع ضمن سورة ولها حدود محددة، وقد يختلف رقمها أو بعض حدودها بحسب نظام عد الآي.

**Purpose:**  
تستخدم كوحدة أساسية للإشارة إلى النص وربط التلاوات والترجمات والتفاسير والتحليلات والبيانات الأخرى بموضع قرآني محدد.

**Alternative spelling:** `Aya`  
**English gloss:** `Verse`

---

## Basmalah — البسملة

**Canonical:** `Basmalah`  
**Plural:** `Basmalahs`  
**Kind:** `textual_concept`

**Definition:**  
صيغة «بسم الله الرحمن الرحيم» التي تفتتح بها السور عدا سورة التوبة، ولها أحكام واختلافات مرتبطة بعد الآي.

**Purpose:**  
تستخدم لتمييز البسملة وتمثيل موضعها وعلاقتها بالسورة ونظام عد الآي.

**Alternative spelling:** `Basmala`

---

## Fasilah — الفاصلة

**Canonical:** `Fasilah`  
**Plural:** `Fasilahs`  
**Kind:** `textual_concept`

**Definition:**  
خاتمة الآية أو المقطع من جهة النظم، ويعرفها بعض العلماء بأنها الكلمة الأخيرة من الآية.

**Purpose:**  
تستخدم في الدراسات والبيانات التي تتناول فواصل الآيات والنظم القرآني، ولا تستخدم مرادفًا لـ`Ayah`.

**Alternative spelling:** `Fasila`  
**English gloss:** `Verse Ending`

---

## Disjointed Letter — الحرف المقطع

**Canonical:** `Disjointed Letter`  
**Plural:** `Disjointed Letters`  
**Kind:** `textual_concept`

**Definition:**  
حروف هجائية افتتحت بها بعض السور، مثل: الم، والر، وحم، وكهيعص.

**Purpose:**  
تستخدم لتعريف هذه الفواتح وتمييزها وربطها بالسور ومواضعها النصية.

**English gloss:** `Separated Letters`

---

# 3. Text

## Word — الكلمة

**Canonical:** `Word`  
**Plural:** `Words`  
**Kind:** `text_unit`

**Definition:**  
وحدة من النص تعامل بوصفها كلمة مستقلة وفق منهج التقسيم النصي المعتمد.

**Purpose:**  
تستخدم لربط البيانات على مستوى الكلمة مثل الجذر والصرف والإعراب والتجويد والمحاذاة الصوتية والموضع البصري.

**Transliteration:** `Kalimah`

**Related:** `Token`, `Lemma`, `Root`, `Morpheme`

---

## Letter — الحرف

**Canonical:** `Letter`  
**Plural:** `Letters`  
**Kind:** `text_unit`

**Definition:**  
حرف هجائي بوصفه وحدة لغوية من وحدات الكتابة.

**Purpose:**  
يستخدم للبيانات التي تتعامل مع الحروف اللغوية، دون الخلط بينها وبين التمثيلات الرقمية أو البصرية.

**Transliteration:** `Harf`

**Related:** `Character`, `Codepoint`, `Grapheme`, `Glyph`

---

## Character — المحرف

**Canonical:** `Character`  
**Plural:** `Characters`  
**Kind:** `technical_unit`

**Definition:**  
وحدة نصية مجردة في نظام تمثيل رقمي، ولا يلزم أن تطابق حرفًا لغويًا واحدًا.

**Purpose:**  
تستخدم عند معالجة النص برمجيًا على مستوى المحارف.

---

## Codepoint — نقطة الترميز

**Canonical:** `Codepoint`  
**Plural:** `Codepoints`  
**Kind:** `technical_unit`

**Definition:**  
قيمة رقمية معرفة في معيار ترميز مثل Unicode.

**Purpose:**  
تستخدم عندما يتعلق العمل بالتمثيل الرقمي الدقيق للمحارف والرموز القرآنية.

---

## Grapheme — الوحدة الكتابية

**Canonical:** `Grapheme`  
**Plural:** `Graphemes`  
**Kind:** `technical_unit`

**Definition:**  
وحدة كتابية يدركها المستخدم كوحدة واحدة، وقد تتكون من أكثر من Unicode codepoint.

**Purpose:**  
تستخدم في التقسيم البصري والتحرير واختيار النص عندما لا يكون الـcodepoint وحدة مناسبة.

---

## Glyph — الشكل الحرفي

**Canonical:** `Glyph`  
**Plural:** `Glyphs`  
**Kind:** `typographic_unit`

**Definition:**  
الشكل البصري الذي ينتجه الخط لتمثيل حرف أو محرف أو مجموعة منها.

**Purpose:**  
يستخدم في الخطوط والرسم والعرض ومواضع الأشكال البصرية، ولا يستخدم مرادفًا لـ`Letter` أو `Character`.

---

# 4. Quran Divisions

## Juz — الجزء

**Canonical:** `Juz`  
**Plural:** `Juzs`  
**Kind:** `division`

**Definition:**  
واحد من ثلاثين قسمًا في التقسيم المشهور للمصحف لتيسير القراءة والختم.

**Purpose:**  
يستخدم للتنقل وتنظيم القراءة والجداول والخطط المرتبطة بأجزاء القرآن.

**Alternative:** `Juzu`  
**Arabic plural:** `Ajza`

---

## Hizb — الحزب

**Canonical:** `Hizb`  
**Plural:** `Hizbs`  
**Kind:** `division`

**Definition:**  
في التقسيم المعاصر نصف جزء، فيكون القرآن ستين حزبًا.

**Purpose:**  
يستخدم لتمثيل التقسيمات الاصطلاحية والتنقل وخطط القراءة.

**Alternative:** `Hezb`

---

## Rub al-Hizb — ربع الحزب

**Canonical:** `Rub al-Hizb`  
**Code:** `rub_al_hizb`  
**Plural:** `Rub al-Hizbs`  
**Kind:** `division`  
**Parent:** `Hizb`

**Definition:**  
ربع الحزب في التقسيم المشهور للمصحف.

**Purpose:**  
يستخدم لتمثيل التقسيم الأدق للحزب ومواضع علاماته في المصحف.

**Alternatives:** `Rub' al-Hizb`, `Rub el Hizb`

---

## Thumn — الثمن

**Canonical:** `Thumn`  
**Plural:** `Thumns`  
**Kind:** `division`  
**Parent:** `Hizb`

**Definition:**  
ثمن الحزب، وهو تقسيم مستخدم في بعض المصاحف والمدارس.

**Purpose:**  
يستخدم عند دعم مصادر أو مصاحف تعتمد تقسيم الحزب إلى أثمان.

**Alternative:** `Thumun`

---

## Manzil — المنزل

**Canonical:** `Manzil`  
**Plural:** `Manzils`  
**Kind:** `division`

**Definition:**  
واحد من سبعة أقسام تقليدية للقرآن لتيسير ختمه في أسبوع.

**Purpose:**  
يستخدم في التطبيقات التي تدعم نظام المنازل وخطط القراءة المبنية عليه.

---

## Ruku — الركوع

**Canonical:** `Ruku`  
**Plural:** `Rukus`  
**Kind:** `division`

**Definition:**  
قسم اصطلاحي من القرآن يستخدم لتنظيم القراءة ويظهر في بعض المصاحف.

**Purpose:**  
يستخدم في التطبيقات والمصاحف التي تعتمد تقسيم الركوع.

**Alternative spellings:** `Ruku'`, `Rukūʿ`

---

# 5. Surah Classification

## Surah Group — تصنيف السور

**Canonical:** `surah_group`  
**Kind:** `classification`  
**Tier:** `extended`

**Definition:**  
تصنيف يجمع سورًا وفق تقسيمات اصطلاحية موروثة تعتمد الطول أو موضعها ضمن مجموعات السور.

**Purpose:**  
يوفر parent موحدًا لتصنيفات مثل الطوال والمئين والمثاني والمفصل.

---

## Sabe al-Tiwal — السبع الطوال

**Canonical:** `Sabe al-Tiwal`  
**Kind:** `classification_value`  
**Parent:** `surah_group`  
**Tier:** `extended`

**Definition:**  
مجموعة من أطول سور القرآن في أوله، مع خلاف معروف في تعيين السورة السابعة.

**Purpose:**  
تستخدم لتصنيف السور وفق التقسيم التراثي.

**English gloss:** `Seven Long Surahs`

---

## Miun — المئون

**Canonical:** `Miun`  
**Kind:** `classification_value`  
**Parent:** `surah_group`  
**Tier:** `extended`

**Definition:**  
السور التي تقارب آياتها المئة أو تزيد عليها أو تنقص عنها قليلًا.

**Purpose:**  
تستخدم لتصنيف السور وفق تقسيمها التراثي.

**English gloss:** `Hundred-Verse Surahs`

---

## Mathani — المثاني

**Canonical:** `Mathani`  
**Kind:** `classification_value`  
**Parent:** `surah_group`  
**Tier:** `extended`

**Definition:**  
مجموعة السور التي تلي المئين في التقسيم التقليدي.

**Purpose:**  
تستخدم ضمن تصنيف السور التراثي.

---

## Mufassal — المفصل

**Canonical:** `Mufassal`  
**Kind:** `classification_value`  
**Parent:** `surah_group`  
**Tier:** `extended`

**Definition:**  
مجموعة من قصار السور التي تلي المثاني، مع اختلاف العلماء في أولها.

**Purpose:**  
تستخدم لتصنيف سور المفصل وربط البيانات والخطط المتعلقة بها.

---

# 6. Mushaf & Layout

## Mushaf Edition — طبعة المصحف

**Canonical:** `Mushaf Edition`  
**Plural:** `Mushaf Editions`  
**Kind:** `entity`  
**Parent:** `Mushaf`

**Definition:**  
إصدار منشور محدد من المصحف له خصائص محددة من الناشر والرسم والضبط والتخطيط وغيرها.

**Purpose:**  
يستخدم لتمييز الإصدارات التي قد تختلف في الصفحات والأسطر والعلامات أو الخصائص الطباعية.

**Note:**  
لا يستخدم بدل `Layout` أو `Riwayah`؛ فكل منها مفهوم مستقل.

---

## Page — الصفحة

**Canonical:** `Page`  
**Plural:** `Pages`  
**Kind:** `layout_unit`

**Definition:**  
وحدة طباعية من تخطيط مصحف معين، وقد يختلف محتواها وحدودها باختلاف المصحف أو الطبعة.

**Purpose:**  
تستخدم في العرض والتنقل والمحاذاة البصرية بحسب صفحات مصحف معين.

**Transliteration:** `Safhah`

---

## Line — السطر

**Canonical:** `Line`  
**Plural:** `Lines`  
**Kind:** `layout_unit`

**Definition:**  
سطر طباعي داخل صفحة مصحف أو تخطيط معين.

**Purpose:**  
يستخدم لتمثيل مواقع النص والأشكال داخل التخطيط الطباعي.

---

## Layout — التخطيط

**Canonical:** `Layout`  
**Plural:** `Layouts`  
**Kind:** `presentation_concept`

**Definition:**  
تنظيم النص والعناصر بصريًا إلى صفحات وأسطر ومواضع ضمن مصحف أو عرض معين.

**Purpose:**  
يفصل البيانات البصرية عن بنية القرآن النصية الثابتة.

---

## Rasm — الرسم

**Canonical:** `Rasm`  
**Kind:** `orthographic_concept`

**Definition:**  
طريقة كتابة ألفاظ القرآن من حيث إثبات الحروف وحذفها وزيادتها وفصلها ووصلها ونحو ذلك.

**Purpose:**  
يستخدم لتمييز الطبقة الإملائية/الرسمية للنص عن الخط والتخطيط والـglyphs.

---

## Uthmani Rasm — الرسم العثماني

**Canonical:** `Uthmani Rasm`  
**Kind:** `rasm_type`  
**Parent:** `Rasm`

**Definition:**  
طريقة كتابة كلمات المصاحف العثمانية وما يتعلق بها من حذف وزيادة وبدل وفصل ووصل.

**Purpose:**  
تستخدم لتحديد أن النص يتبع قواعد الرسم العثماني بدل نظم إملائية أخرى.

**English gloss:** `Uthmanic Orthography`

---

# 7. Mushaf Marks

## Mushaf Mark — علامة المصحف

**Canonical:** `Mushaf Mark`  
**Kind:** `classification`

**Definition:**  
رمز أو علامة غير داخلة في الحروف الأصلية للكلمة، تستخدم في المصحف لأغراض القراءة أو التنظيم أو الإرشاد.

**Purpose:**  
يوفر parent موحدًا للعلامات المختلفة بدل معاملتها كأنواع غير مرتبطة.

---

## Division Mark — علامة التقسيم

**Canonical:** `Division Mark`  
**Plural:** `Division Marks`  
**Kind:** `mark`  
**Parent:** `Mushaf Mark`

**Definition:**  
علامة تنظيمية تبين بداية جزء أو حزب أو ربع أو تقسيم مشابه.

**Purpose:**  
تستخدم لتمثيل علامات التقسيم في بيانات المصحف وتخطيطه.

---

## Sajdah Mark — علامة السجدة

**Canonical:** `Sajdah Mark`  
**Plural:** `Sajdah Marks`  
**Kind:** `mark`  
**Parent:** `Mushaf Mark`

**Definition:**  
علامة توضع في المصحف للدلالة على موضع متعلق بسجود التلاوة.

**Purpose:**  
تستخدم لتمثيل العلامة البصرية بصورة مستقلة عن مفهوم `Sujud al-Tilawah` نفسه.

---

# 8. Ayah Numbering

## Ayah Numbering System — نظام عد الآي

**Canonical:** `Ayah Numbering System`  
**Plural:** `Ayah Numbering Systems`  
**Kind:** `classification`

**Definition:**  
نظام يحدد حدود الآيات وأعدادها وأرقامها وبعض المسائل المتعلقة بالبسملة وفق مدارس عد الآي.

**Purpose:**  
يستخدم لتحديد النظام الذي تستند إليه أرقام الآيات وحدودها في dataset أو Mushaf معين.

**Alternative:** `Ayah Counting System`

### Values

```text
Madani I
Madani II
Makki
Basri
Shami
Kufi
```

يجب أن يحصل كل نظام منها في النسخة الموسعة على تعريف ومصدر مستقل.

---

# 9. Revelation


## Asbab al-Nuzul — أسباب النزول

**Canonical:** `Asbab al-Nuzul`  
**Kind:** `content`

**Definition:**  
الحوادث أو الأسئلة التي نزلت آية أو آيات متحدثة عنها أو مبينة لحكم يتعلق بها.

**Purpose:**  
تستخدم لربط الآيات بالمرويات والمعلومات المتعلقة بسبب نزولها.

**Alternatives:** `Asbab al-Nozool`, `Asbab un-Nuzul`

---

## Revelation Order — ترتيب النزول

**Canonical:** `Revelation Order`  
**Kind:** `property`

**Definition:**  
ترتيب السور أو الآيات بحسب زمن نزولها، وقد يختلف بحسب المصدر المعتمد.

**Purpose:**  
يستخدم لتخزين ترتيب النزول بصورة مستقلة عن ترتيب المصحف.

---

## Revelation Classification — المكي والمدني

**Canonical:** `Revelation Classification`  
**Kind:** `classification`

**Definition:**  
تصنيف للنص القرآني بحسب وقوع نزوله قبل الهجرة أو بعدها وفق الاصطلاح المعتمد.

**Purpose:**  
يستخدم لتصنيف السور أو الآيات بحسب علاقتها بالهجرة دون الإيحاء بأن التصنيف جغرافي فقط.

---

## Makki — المكي

**Canonical:** `Makki`  
**Kind:** `classification_value`  
**Parent:** `Revelation Classification`

**Definition:**  
ما نزل من القرآن قبل الهجرة، ولو نزل خارج مكة.

**Purpose:**  
يستخدم كقيمة لتصنيف سورة أو آية ضمن `Revelation Classification`.

**Alternative:** `Makkan`, `Makkiyy`

---

## Madani — المدني

**Canonical:** `Madani`  
**Kind:** `classification_value`  
**Parent:** `Revelation Classification`

**Definition:**  
ما نزل من القرآن بعد الهجرة، ولو نزل خارج المدينة.

**Purpose:**  
يستخدم كقيمة لتصنيف سورة أو آية ضمن `Revelation Classification`.

**Alternative:** `Madinan`, `Madaniyy`

---

## Disputed — مختلف فيه

**Canonical:** `Disputed`  
**Kind:** `classification_value`  
**Parent:** `Revelation Classification`

**Definition:**  
ما اختلفت المصادر المعتمدة في تصنيفه بين المكي والمدني.

**Purpose:**  
يمنع إجبار البيانات المختلف فيها على قيمة `Makki` أو `Madani` دون توثيق الخلاف.

---

# 10. Qiraat

## Qiraah — القراءة

**Canonical:** `Qiraah`  
**Plural:** `Qiraahs`  
**Kind:** `concept`

**Definition:**  
وجه من وجوه قراءة القرآن ينسب إلى إمام من أئمة القراءات وتتفرع عنه الروايات والطرق.

**Purpose:**  
يمثل المستوى الأعلى في model القراءات ويربط الروايات والطرق والنصوص المرتبطة بها.

**Alternative spellings:** `Qira'ah`, `Qiraa`  
**English gloss:** `Reading`

---

## Riwayah — الرواية

**Canonical:** `Riwayah`  
**Plural:** `Riwayahs`  
**Kind:** `concept`  
**Parent:** `Qiraah`

**Definition:**  
ما ينسب إلى راو عن إمام القراءة؛ مثل رواية حفص عن عاصم.

**Purpose:**  
تستخدم لتحديد الرواية التي يتبعها نص أو مصحف أو تسجيل أو dataset.

**Alternative:** `Riwaya`

---

## Tariq — الطريق

**Canonical:** `Tariq`  
**Plural:** `Tariqs`  
**Kind:** `concept`  
**Parent:** `Riwayah`

**Definition:**  
وجه النقل المأخوذ عن الراوي بواسطة من دونه في سلسلة نقل القراءة.

**Purpose:**  
يستخدم عندما تحتاج البيانات إلى مستوى أدق من الرواية لتمييز طرق الأداء والنقل.

**Alternative:** `Tareeq`

---

## Rawi — الراوي

**Canonical:** `Rawi`  
**Plural:** `Rawis`  
**Kind:** `role`

**Definition:**  
من نسبت إليه الرواية عن إمام القراءة.

**Purpose:**  
يستخدم لتمثيل الشخص المرتبط بـ`Riwayah`، ولا يستخدم للدلالة على مؤدي تسجيل صوتي لمجرد أنه يقرأ القرآن.

**English gloss:** `Transmitter`

---

## Muqri — المقرئ

**Canonical:** `Muqri`  
**Plural:** `Muqris`  
**Kind:** `role`

**Definition:**  
من تلقى القراءة وأتقنها وينقلها للمتعلمين.

**Purpose:**  
يستخدم لتمثيل دور التعليم والتلقي والإقراء، ويتميز عن مجرد `Reciter`.

**Alternative:** `Muqree`

---

# 11. Recitation

## Recitation — التلاوة

**Canonical:** `Recitation`  
**Plural:** `Recitations`  
**Kind:** `entity`

**Definition:**  
قراءة القرآن وأداؤه صوتيًا.

**Purpose:**  
يستخدم لتمثيل فعل التلاوة، وبرمجيًا يمكن أن يمثل تسجيلًا مرتبطًا بمؤدٍ وقراءة ورواية ونمط أداء.

**Transliteration:** `Tilawah`

---

## Reciter — القارئ

**Canonical:** `Reciter`  
**Plural:** `Reciters`  
**Kind:** `role`

**Definition:**  
الشخص الذي يؤدي تلاوة القرآن.

**Purpose:**  
يستخدم لربط التسجيلات الصوتية بمؤديها، دون افتراض أنه إمام `Qiraah` أو `Rawi`.

**Transliteration:** `Qari`

---

## Tartil — الترتيل

**Canonical:** `Tartil`  
**Kind:** `recitation_concept`

**Definition:**  
قراءة القرآن بتؤدة وبيان للحروف والكلمات ومراعاة الوقف والمعنى.

**Purpose:**  
يستخدم عندما يكون المقصود مفهوم الترتيل نفسه، ولا يستخدم مرادفًا تلقائيًا لتصنيف تسجيل `Murattal`.

**Alternative:** `Tarteel`

---

# 12. Recitation Pace

## Recitation Pace — مرتبة القراءة من حيث السرعة

**Canonical:** `Recitation Pace`  
**Kind:** `classification`

**Definition:**  
تصنيف لسرعة أداء القراءة مع المحافظة على أحكامها.

**Purpose:**  
يفصل مراتب السرعة التقليدية عن أنماط التسجيل مثل `Murattal` و`Mujawwad`.

---

## Tahqiq — التحقيق

**Canonical:** `Tahqiq`  
**Kind:** `classification_value`  
**Parent:** `Recitation Pace`

**Definition:**  
القراءة ببطء وتؤدة مع استيفاء الحروف وأحكامها، وتستخدم كثيرًا في مقام التعليم.

**Purpose:**  
تستخدم لوصف مرتبة القراءة البطيئة الدقيقة.

**Alternative:** `Tahqeeq`

---

## Tadwir — التدوير

**Canonical:** `Tadwir`  
**Kind:** `classification_value`  
**Parent:** `Recitation Pace`

**Definition:**  
القراءة بسرعة متوسطة بين التحقيق والحدر مع المحافظة على الأحكام.

**Purpose:**  
تستخدم لتمثيل المرتبة المتوسطة لسرعة القراءة.

**Alternative:** `Tadweer`

---

## Hadr — الحدر

**Canonical:** `Hadr`  
**Kind:** `classification_value`  
**Parent:** `Recitation Pace`

**Definition:**  
الإسراع في القراءة مع المحافظة على الحروف والحركات وأحكام الأداء دون إخلال.

**Purpose:**  
تستخدم لتمثيل مرتبة القراءة الأسرع ضمن مراتب الأداء.

**Alternative:** `Hadar`

---

# 13. Recitation Style

## Recitation Style — نمط أداء التلاوة

**Canonical:** `Recitation Style`  
**Plural:** `Recitation Styles`  
**Kind:** `classification`

**Definition:**  
تصنيف يصف نمط أداء تلاوة أو تسجيل معين بصورة مستقلة عن القراءة والرواية.

**Purpose:**  
يستخدم لتصنيف التسجيلات الصوتية بحسب طريقة الأداء أو الغرض منها.

---

## Murattal — مرتل

**Canonical:** `Murattal`  
**Kind:** `classification_value`  
**Parent:** `Recitation Style`

**Definition:**  
وصف لتلاوة أو تسجيل ينشر بوصفه مرتلًا.

**Purpose:**  
يستخدم لتصنيف التسجيل، ولا يستخدم مرادفًا عامًا لمفهوم `Tartil`.

---

## Mujawwad — مجود

**Canonical:** `Mujawwad`  
**Kind:** `classification_value`  
**Parent:** `Recitation Style`

**Definition:**  
وصف لتلاوة أو تسجيل ينشر بوصفه مجودًا.

**Purpose:**  
يستخدم لتصنيف نمط التسجيل، ولا يستخدم مرادفًا لعلم `Tajwid`.

---

## Muallim — معلم

**Canonical:** `Muallim`  
**Kind:** `classification_value`  
**Parent:** `Recitation Style`

**Definition:**  
نمط تلاوة معد للتعليم وقد يتضمن تكرار الآيات أو إتاحة وقت للمتعلم للترديد.

**Purpose:**  
يستخدم لتصنيف التسجيلات التعليمية وتمييزها عن التسجيلات العادية.

---

## Instructional Ayah Repetition — تكرار الآيات للتعليم

**Canonical:** `Instructional Ayah Repetition`  
**Kind:** `recitation_feature`

**Definition:**  
إعادة آية أو جزء منها مرة أو مرات وفق نمط تعليمي يساعد على التلقي والحفظ.

**Purpose:**  
يستخدم لوصف ميزة مستقلة في التسجيل التعليمي بدل جعلها جزءًا ضمنيًا من `Muallim`.

---

# 14. Tajwid

## Tajwid — التجويد

**Canonical:** `Tajwid`  
**Kind:** `discipline`

**Definition:**  
علم أداء حروف القرآن من مخارجها وإعطائها حقوقها ومستحقاتها من الصفات والأحكام.

**Purpose:**  
يمثل المجال الجامع لقواعد وأحكام وannotations التجويد في البرمجيات.

**Alternative spelling:** `Tajweed`

`Tajwid` هو الـCanonical spelling وفق **Quranic Software Terminology Standard**؛ ولا يعني ذلك أن `Tajweed` خطأ في الاستعمال العام.

---

## Saktah — السكتة

**Canonical:** `Saktah`  
**Plural:** `Saktahs`  
**Kind:** `recitation_feature`

**Definition:**  
قطع الصوت زمنًا يسيرًا من غير تنفس ثم متابعة القراءة.

**Purpose:**  
يستخدم لتمثيل مواضع السكت وخصائصها في النص أو التلاوة.

**Alternative:** `Sakta`

---

## Istiadhah — الاستعاذة

**Canonical:** `Istiadhah`  
**Kind:** `recitation_practice`

**Definition:**  
طلب العوذ بالله من الشيطان عند إرادة تلاوة القرآن.

**Purpose:**  
يستخدم لتمثيل الاستعاذة وصيغها وموضعها بالنسبة إلى بداية التلاوة.

**Alternatives:** `Isti'adhah`, `Istiʿādhah`, `Ta'awwudh`

---

## Khatmah — الختمة

**Canonical:** `Khatmah`  
**Plural:** `Khatmahs`  
**Kind:** `recitation_concept`

**Definition:**  
قراءة القرآن كاملًا من أوله إلى آخره.

**Purpose:**  
تستخدم لتتبع خطط الختم وإتمام القراءة وربط الجلسات بمسار ختمة.

**Alternative:** `Khatma`

---

# 15. Waqf

## Waqf — الوقف

**Canonical:** `Waqf`  
**Kind:** `recitation_concept`

**Definition:**  
قطع القراءة عند موضع من النص وفق أحكام الوقف والابتداء.

**Purpose:**  
يمثل المفهوم العام للوقف، بينما تمثل `Waqf Mark` العلامات المطبوعة التي ترشد إليه.

---

## Waqf Mark — علامة الوقف

**Canonical:** `Waqf Mark`  
**Plural:** `Waqf Marks`  
**Kind:** `mark`  
**Parent:** `Mushaf Mark`

**Definition:**  
علامة في المصحف ترشد القارئ إلى حكم الوقف أو الوصل في موضع معين.

**Purpose:**  
تستخدم لتمثيل الرمز وموضعه ونوعه بصورة منظمة.

---

## Waqf Mark Type — نوع علامة الوقف

**Canonical:** `waqf_mark_type`  
**Kind:** `classification`

**Definition:**  
تصنيف لما ترشد إليه علامة الوقف المرسومة في المصحف من لزوم أو منع أو جواز.

**Purpose:**  
يوفر مجموعة قيم موحدة تتفرع عليها التطبيقات، بدل قراءة صورة الرمز نفسه.

**Note:**  
هذا تصنيف للعلامة المرسومة، ويختلف عن `waqf_ruling` الذي يصنف الموضع نفسه.

---

## Waqf Lazim — الوقف اللازم

**Canonical:** `waqf_lazim`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضع يدل على لزوم الوقف، لأن وصل ما بعده بما قبله يوهم خلاف المعنى المراد.

**Purpose:**  
يستخدم قيمةً لعلامة الوقف اللازم، وهي الميم في المصحف.

**Mushaf introduction:** عَلَامَة الوَقْف اللَّازِم  
**English gloss:** `Mandatory Waqf`

---

## Waqf Jaiz — الوقف الجائز

**Canonical:** `waqf_jaiz`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضع يجوز فيه الوقف والوصل جوازًا مستوي الطرفين، فلا يترجح أحدهما.

**Purpose:**  
يستخدم قيمةً لعلامة الجيم، وهي الجواز الذي لا تفضيل فيه.

**Mushaf introduction:** عَلَامَة الوَقْف الجَائِز جَوَازًا مُسْتَوِيَ الطَّرَفَيْن  
**English gloss:** `Permissible Waqf`

---

## Waqf Jaiz Wasl Awla — الوقف الجائز والوصل أولى

**Canonical:** `waqf_jaiz_wasl_awla`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضع يجوز فيه الوقف والوصل، مع كون الوصل أولى.

**Purpose:**  
يستخدم قيمةً لعلامة «صلى».

**Mushaf introduction:** عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَصْل أَوْلَى  
**English gloss:** `Continuation Preferred`

---

## Waqf Jaiz Waqf Awla — الوقف الجائز والوقف أولى

**Canonical:** `waqf_jaiz_waqf_awla`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضع يجوز فيه الوقف والوصل، مع كون الوقف أولى.

**Purpose:**  
يستخدم قيمةً لعلامة «قلى».

**Mushaf introduction:** عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَقْف أَوْلَى  
**English gloss:** `Waqf Preferred`

---

## Taanuq al-Waqf — تعانق الوقف

**Canonical:** `taanuq_al_waqf`  
**Code:** `taanuq_al_waqf`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضعان للوقف، إذا وُقف على أحدهما لم يصح الوقف على الآخر.

**Purpose:**  
يستخدم لربط موضعي التعانق وإظهار العلاقة بين العلامتين؛ فهي علامة واحدة
ترد في زوج، لا علامتان مستقلتان.

**Mushaf introduction:** عَلَامَة تَعَانُق الوَقْف  
**Alternative:** `waqf_al_muanaqah`  
**English gloss:** `Interchangeable Waqf`

---

## Waqf Mamnu — الوقف الممنوع

**Canonical:** `waqf_mamnu`  
**Kind:** `classification_value`  
**Parent:** `waqf_mark_type`

**Definition:**  
موضع يدل على منع الوقف الاختياري فيه.

**Purpose:**  
يستخدم قيمةً لعلامة «لا».

**Mushaf introduction:** — لم ترد في مقدمة هذه الطبعة، ولا موضع لها فيها.

**Note:**  
المصطلح ثابت في علم الضبط، والعلامة مسجلة في السجل وغير مستعملة في هذه
الطبعة. وخلو مقدمة المصحف من ذكرها خبر عن الطبعة لا نقص في المدخل.

---

## Waqf Ruling — حكم الوقف

**Canonical:** `waqf_ruling`  
**Kind:** `classification`

**Definition:**  
تصنيف الموضع نفسه من جهة تمام المعنى عنده، لا من جهة العلامة المرسومة عليه.

**Purpose:**  
يستخدم في التعليم والتحليل النحوي والدلالي للوقف، ويبقى مستقلًا عن
`waqf_mark_type` لأنهما تصنيفان لشيئين مختلفين: هذا للموضع وذاك للعلامة.

---

## Waqf Tam — الوقف التام

**Canonical:** `waqf_tam`  
**Kind:** `classification_value`  
**Parent:** `waqf_ruling`

**Definition:**  
ما تم معناه ولم يتعلق بما بعده لفظًا ولا معنى.

**Purpose:**  
يستخدم قيمةً في تصنيف مواضع الوقف تعليميًا وتحليليًا.

---

## Waqf Kafi — الوقف الكافي

**Canonical:** `waqf_kafi`  
**Kind:** `classification_value`  
**Parent:** `waqf_ruling`

**Definition:**  
ما تم معناه وتعلق بما بعده معنًى لا لفظًا.

**Purpose:**  
يستخدم قيمةً في تصنيف مواضع الوقف.

---

## Waqf Hasan — الوقف الحسن

**Canonical:** `waqf_hasan`  
**Kind:** `classification_value`  
**Parent:** `waqf_ruling`

**Definition:**  
ما أفاد معنًى وتعلق بما بعده لفظًا ومعنًى.

**Purpose:**  
يستخدم قيمةً في تصنيف مواضع الوقف.

---

## Waqf Qabih — الوقف القبيح

**Canonical:** `waqf_qabih`  
**Kind:** `classification_value`  
**Parent:** `waqf_ruling`

**Definition:**  
ما لم يفد معنًى، أو أفاد معنًى غير مراد.

**Purpose:**  
يستخدم قيمةً في تصنيف مواضع الوقف، وفي التنبيه في تطبيقات التعليم.

---

## Sujud al-Tilawah — سجود التلاوة

**Canonical:** `Sujud al-Tilawah`  
**Kind:** `practice`

**Definition:**  
سجدة تؤدى عند قراءة أو سماع موضع من مواضع سجود التلاوة.

**Purpose:**  
يمثل العبادة أو الحكم نفسه، ويظل مستقلًا عن العلامة المطبوعة في المصحف.

**Alternatives:** `Sajdah al-Tilawah`, `Sajdat al-Tilawah`

---


# 16. Linguistics

## Root — الجذر

**Canonical:** `Root`  
**Plural:** `Roots`  
**Kind:** `linguistic_unit`

**Definition:**  
الأصل الصرفي الذي ترد إليه الكلمة لبيان اشتقاقها وصلتها بالكلمات الأخرى.

**Purpose:**  
يستخدم للبحث الصرفي والتحليل اللغوي وتجميع الكلمات ذات الأصل المشترك.

---

## Lemma — المدخل المعجمي

**Canonical:** `Lemma`  
**Plural:** `Lemmas`  
**Kind:** `linguistic_unit`

**Definition:**  
الصيغة المعجمية الأساسية التي ترد إليها صورة الكلمة المصرفة.

**Purpose:**  
تستخدم لتجميع الصور التصريفية المختلفة تحت مدخل معجمي واحد.

---

## Morphology — الصرف

**Canonical:** `Morphology`  
**Kind:** `analysis`

**Definition:**  
تحليل بنية الكلمة وصيغتها وما تحمله من خصائص صرفية.

**Purpose:**  
يستخدم لتمثيل السمات الصرفية للكلمات أو الـtokens.

---

## Irab — الإعراب

**Canonical:** `Irab`  
**Kind:** `analysis`

**Definition:**  
بيان الوظائف النحوية للكلمات وعلاماتها وعلاقاتها في التركيب.

**Purpose:**  
يستخدم لربط كلمات الآيات بالتحليل النحوي والوظائف الإعرابية.

**Alternative:** `I'rab`  
**English gloss:** `Grammatical Analysis`

---

# 17. Translation

## Translation — الترجمة

**Canonical:** `Translation`  
**Plural:** `Translations`  
**Kind:** `content`

**Definition:**  
نقل معاني القرآن إلى لغة أخرى، وليست الترجمة قرآنًا بلفظه.

**Purpose:**  
تستخدم لربط نصوص ترجمة المعاني بالآيات واللغات والمترجمين والمصادر.

---

## Spoken Translation — الترجمة المنطوقة

**Canonical:** `Spoken Translation`  
**Plural:** `Spoken Translations`  
**Kind:** `content`  
**Parent:** `Translation`

**Definition:**  
نقل معاني القرآن إلى لغة أخرى في مادة صوتية أو منطوقة.

**Purpose:**  
يستخدم لتمييز المحتوى الصوتي لترجمة المعاني عن الترجمة النصية وعن التلاوة القرآنية.

**Alternative:** `Audio Translation`

---

## Transliteration — النقل الحرفي

**Canonical:** `Transliteration`  
**Plural:** `Transliterations`  
**Kind:** `content`

**Definition:**  
تمثيل حروف نظام كتابي بحروف نظام آخر وفق قواعد محددة، دون ترجمة المعنى.

**Purpose:**  
يستخدم لتوفير تمثيل قابل للقراءة بنظام كتابي آخر أو للتحويل المنهجي بين أنظمة الكتابة.

**Related:** `Romanization`

---

# 18. Tafsir

## Tafsir — التفسير

**Canonical:** `Tafsir`  
**Plural:** `Tafsirs`  
**Kind:** `content`

**Definition:**  
بيان معاني القرآن وشرح ألفاظه وما يرشد إليه من أحكام وهدايات بحسب أصول التفسير.

**Purpose:**  
يستخدم لتمثيل كتب ومحتوى التفسير وربط مقاطعه بالآيات والسور والمصادر.

**Alternative spelling:** `Tafseer`  
**English glosses:** `Exegesis`, `Commentary`

---

# 19. بنية الـEntry

بنية المدخل يحددها القسم 27 من **Quranic Software Terminology Standard**،
والمصدر البرمجي لهذا القاموس هو `standards/terminology/concepts/*.yml`،
يتحقق منه بـ`standards/terminology/schema.json`.

# 20. نقاط تحتاج مراجعة قبل اعتماد v1.0

هذه المفاهيم تحتاج نقاشًا إضافيًا قبل تثبيت الـCanonical النهائي:

```text
Fasilah
Disjointed Letter
Mushaf Edition
Rasm / Orthography
Ayah Numbering System terminology
```

وقد حسمت هذه بعد أن كانت مطروحة:

```text
Kitab                       أخرج من القاموس؛ اسم للقرآن لا مفهوم برمجي
Sabe al-Tiwal والمجموعات    نقلت إلى tier: extended لاختلاف حدودها
Recitation vs Tilawah       Recitation، والمفهوم عام لا يخصه القرآن
Reciter vs Qari             Reciter، وQari تسجل بديلًا
Waqf Lazim وأخواتها         الأسماء العربية، موافقةً لسائر قيم التصنيفات
Sujud al-Tilawah            أبقي، وفصلت عنه علامة السجدة المرسومة
```

في هذه الحالات يجب أن نختار بناء على السؤال الأساسي في المعيار:

> هل المصطلح العربي هنا يمثل مفهومًا قرآنيًا متخصصًا يجب المحافظة عليه، أم أن الاسم الإنجليزي الطبيعي ينقل المفهوم كاملًا ويجعل استخدامه البرمجي أوضح؟