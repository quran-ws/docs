---
title: قاموس المصطلحات
description: المفاهيم المستخدمة في البرمجيات القرآنية، بتعريفاتها وأسمائها المعتمدة.
status: draft
sidebar:
  order: 2
tableOfContents:
  minHeadingLevel: 2
  maxHeadingLevel: 2
---
> مولّد من `standards/terminology/concepts/*.yml` — عدّل المدخل لا هذه الصفحة،
> ثم شغّل `python3 tools/build.py`.

## البحث السريع

مدخل لكل مفهوم، مرتبة بالاسم. اضغط الاسم للوصول إلى المدخل كاملًا.

| الاسم | العرض | العربية | النوع | المجال | التعريف |
| --- | --- | --- | --- | --- | --- |
| [`abrogation`](#abrogation) | Abrogation | النسخ | <span dir="ltr">`concept`</span> | <span dir="ltr">`quranic_sciences`</span> | النسخ هو رفع حكم شرعي بدليل شرعي جاء بعده، ويدرس في القرآن بنسبة الآية الناسخة إلى الآية المنسوخة. |
| [`asbab_al_nuzul`](#asbab_al_nuzul) | Asbab al-Nuzul | أسباب النزول | <span dir="ltr">`content`</span> | <span dir="ltr">`revelation`</span> | أسباب النزول هي الحوادث أو الأسئلة التي نزلت آية أو آيات للحديث عنها أو لبيان حكم يتعلق بها. |
| [`ayah`](#ayah) | Ayah | الآية | <span dir="ltr">`entity`</span> | <span dir="ltr">`structure`</span> | الآية وحدة من النص القرآني تقع داخل سورة ولها حدود محددة. |
| [`ayah_count`](#ayah_count) | Ayah Count | عدد الآيات | <span dir="ltr">`property`</span> | <span dir="ltr">`ayah_numbering`</span> | عدد الآيات هو عدد آيات السورة في نظام عد بعينه. |
| [`ayah_ending`](#ayah_ending) | Ayah Ending | الفاصلة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | الفاصلة هي خاتمة الآية أو المقطع من جهة النظم، ويعرفها بعض العلماء بأنها الكلمة الأخيرة من الآية. |
| [`ayah_fragment`](#ayah_fragment) | Ayah Fragment | مقطع الآية | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | مقطع الآية هو ما يظهر من آية واحدة في سطر واحد من صفحة مصحف بعينه. |
| [`ayah_key`](#ayah_key) | Ayah Key |  | <span dir="ltr">`property`</span> | <span dir="ltr">`structure`</span> | مفتاح الآية معرف نصي للآية يجمع رقم سورتها ورقمها داخلها مفصولين بنقطتين، على صورة `2:255`. |
| [`ayah_mark`](#ayah_mark) | Ayah Mark | علامة الآية | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة الآية هي الدارة الفاصلة بين الآيتين، وتوضع عند نهاية الآية ويكتب فيها رقمها في أكثر المصاحف. |
| [`ayah_numbering_basri`](#ayah_numbering_basri) | Basri Numbering | العد البصري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد البصري هو نظام عد الآي المروي عن عاصم الجحدري عن أسلافه من أهل البصرة. |
| [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi) | Dimashqi Numbering | العد الدمشقي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد الدمشقي هو نظام عد أهل الشام، المروي عن يحيى بن الحارث الذماري عن ابن عامر، ويسمى العد الشامي. |
| [`ayah_numbering_kufi`](#ayah_numbering_kufi) | Kufi Numbering | العد الكوفي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد الكوفي هو نظام عد الآي المروي عن حمزة الزيات عن ابن أبي ليلى عن أبي عبد الرحمن السلمي عن علي بن أبي طالب، وهو العد الذي تتبعه أكثر المصاحف المطبوعة اليوم. |
| [`ayah_numbering_madani_first`](#ayah_numbering_madani_first) | First Madani Numbering | العد المدني الأول | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد المدني الأول هو نظام عد أهل المدينة في روايته الأولى، وهي رواية أبي جعفر يزيد بن القعقاع وشيبة بن نصاح. |
| [`ayah_numbering_madani_last`](#ayah_numbering_madani_last) | Last Madani Numbering | العد المدني الأخير | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد المدني الأخير هو نظام عد أهل المدينة في روايته الأخيرة، وهي رواية إسماعيل بن جعفر عن سليمان بن جماز. |
| [`ayah_numbering_makki`](#ayah_numbering_makki) | Makki Numbering | العد المكي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | العد المكي هو نظام عد الآي المروي عن ابن كثير عن مجاهد عن ابن عباس عن أبي بن كعب. |
| [`ayah_numbering_system`](#ayah_numbering_system) | Ayah Numbering System | نظام عد الآي | <span dir="ltr">`classification`</span> | <span dir="ltr">`ayah_numbering`</span> | نظام عد الآي هو النظام الذي يحدد حدود الآيات وأعدادها وأرقامها وبعض المسائل المتعلقة بالبسملة، وفق إحدى مدارس عد الآي. |
| [`ayah_timing`](#ayah_timing) | Ayah Timing |  | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | توقيت الآية مدى زمني في تسجيل تلاوة، له بداية ونهاية، ويقابل آية بعينها. |
| [`basmalah`](#basmalah) | Basmalah | البسملة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | البسملة هي صيغة «بسم الله الرحمن الرحيم» التي تفتتح بها السور عدا سورة التوبة. |
| [`character`](#character) | Character |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | المحرف وحدة نصية مجردة في نظام تمثيل رقمي، ولا يلزم أن يطابق حرفًا لغويًا واحدًا. |
| [`codepoint`](#codepoint) | Codepoint |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | نقطة الترميز قيمة رقمية معرفة في معيار ترميز مثل `Unicode`. |
| [`dammah`](#dammah) | Dammah | الضمة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الضمة علامة تدل على حركة الحرف بالضم. |
| [`disputed`](#disputed) | Disputed | مختلف فيه | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | المختلف فيه هو ما اختلفت المصادر المعتمدة في تصنيفه بين المكي والمدني. |
| [`division_mark`](#division_mark) | Division Mark | علامة التقسيم | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة التقسيم علامة تدل على بداية الأجزاء والأحزاب وأنصافها وأرباعها. |
| [`dot`](#dot) | Dot | النقطة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | النقطة نقطة واحدة فوق الحرف أو تحته تميزه عن الحرف الذي يشاركه في الرسم، مثل الباء والنون والجيم والخاء والذال. |
| [`equivalent_ayah`](#equivalent_ayah) | Equivalent Ayah | الآية المقابلة | <span dir="ltr">`concept`</span> | <span dir="ltr">`ayah_numbering`</span> | الآية المقابلة هي الآية في نظام عد تقابل آية في نظام عد آخر، سواء اتفق رقماهما أو اختلفا لاختلاف مواضع الفصل بين الآي. |
| [`fathah`](#fathah) | Fathah | الفتحة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الفتحة علامة تدل على حركة الحرف بالفتح. |
| [`font`](#font) | Font | الخط | <span dir="ltr">`concept`</span> | <span dir="ltr">`mushaf`</span> | الخط ملف يحمل مجموعة من الأشكال المرسومة (`glyphs`) وقواعد إخراجها، ويُعرض به نص المصحف. |
| [`ghunnah`](#ghunnah) | Ghunnah | الغنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | الغنة صوت يخرج من الخيشوم مركب في جسم النون والميم، ولا عمل للسان فيه. |
| [`glyph`](#glyph) | Glyph |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | الشكل المرسوم هو الشكل البصري الذي ينتجه الخط لتمثيل حرف أو محرف أو مجموعة منها. |
| [`grapheme`](#grapheme) | Grapheme |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | الوحدة الكتابية وحدة يدركها المستخدم على أنها وحدة واحدة، وقد تتكون من أكثر من `codepoint`. |
| [`hadr`](#hadr) | Hadr | الحدر | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | الحدر هو الإسراع في القراءة مع المحافظة على الحروف والحركات وأحكام الأداء دون إخلال. |
| [`hamzah`](#hamzah) | Hamzah | الهمزة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الهمزة علامة تدل على همزة القطع المحققة. |
| [`hamzat_al_wasl`](#hamzat_al_wasl) | Hamzat al-Wasl | همزة الوصل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | همزة الوصل علامة تدل على سقوط الهمزة في الوصل. |
| [`harakah`](#harakah) | Harakah | الحركة | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | الحركة علامة تضبط حركة الحرف أو سكونه أو تشديده، وهي الفتحة والضمة والكسرة والسكون والشدة. |
| [`hizb`](#hizb) | Hizb | الحزب | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | الحزب في التقسيم المعاصر نصف جزء، فيكون القرآن 60 حزبًا. |
| [`idgham`](#idgham) | Idgham | الإدغام | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | الإدغام إدخال حرف ساكن في حرف متحرك بعده بحيث يصيران حرفًا واحدًا مشددًا. |
| [`ijam`](#ijam) | Ijam | الإعجام | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | الإعجام هو النقط الذي يميز الحرف عن الحروف التي تشاركه في صورة الرسم. |
| [`ikhfa`](#ikhfa) | Ikhfa | الإخفاء | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | الإخفاء هو النطق بالحرف الساكن على صفة بين الإظهار والإدغام، دون تشديد ومع بقاء الغنة. |
| [`imalah`](#imalah) | Imalah | الإمالة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة الإمالة تدل على الإمالة الكبرى، وهي نطق الفتحة مائلة إلى الكسرة، وترد في رواية حفص في موضع واحد (11:41). |
| [`instructional_ayah_repetition`](#instructional_ayah_repetition) | Instructional Ayah Repetition | تكرار الآيات | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation_style`</span> | تكرار الآيات هو إعادة آية أو جزء منها مرة أو مرات وفق نمط تعليمي يساعد على التلقي والحفظ. |
| [`iqlab`](#iqlab) | Iqlab | الإقلاب | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | الإقلاب قلب النون الساكنة أو التنوين ميمًا مخفاة بغنة عند الباء. |
| [`irab`](#irab) | Irab | الإعراب | <span dir="ltr">`analysis`</span> | <span dir="ltr">`linguistics`</span> | الإعراب بيان الوظائف النحوية للكلمات وعلاماتها وعلاقاتها في التركيب. |
| [`ishmam`](#ishmam) | Ishmam | الإشمام | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة الإشمام تدل على الإشمام، وهو ضم الشفتين إشارة إلى الضمة المحذوفة من غير صوت. |
| [`istiadhah`](#istiadhah) | Istiadhah | الاستعاذة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | الاستعاذة طلب العوذ بالله من الشيطان عند إرادة تلاوة القرآن. |
| [`izhar`](#izhar) | Izhar | الإظهار | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | الإظهار إخراج الحرف الساكن من مخرجه من غير غنة زائدة فيه، مثل إظهار النون الساكنة والتنوين عند حروف الحلق، وإظهار الميم الساكنة عند غير الباء والميم. |
| [`juz`](#juz) | Juz | الجزء | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | الجزء واحد من 30 قسمًا في التقسيم المشهور للمصحف، والغرض من هذا التقسيم تيسير القراءة والختم. |
| [`kasrah`](#kasrah) | Kasrah | الكسرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الكسرة علامة تدل على حركة الحرف بالكسر. |
| [`khatmah`](#khatmah) | Khatmah | الختمة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | الختمة قراءة القرآن كاملًا من أوله إلى آخره. |
| [`layout`](#layout) | Layout | التخطيط | <span dir="ltr">`concept`</span> | <span dir="ltr">`mushaf`</span> | التخطيط تنظيم النص والعناصر بصريًا في صفحات وأسطر ومواضع داخل مصحف أو عرض معين. |
| [`lemma`](#lemma) | Lemma |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الصيغة المعجمية هي الصيغة الأساسية التي تُرد إليها صورة الكلمة المصرفة. |
| [`letter`](#letter) | Letter | الحرف | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | الحرف هو الحرف الهجائي بوصفه وحدة لغوية من وحدات الكتابة. |
| [`letter_relation`](#letter_relation) | Letter Relation | علاقة الحرفين | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | علاقة الحرفين هي نسبة الحرفين المتجاورين أحدهما إلى الآخر في المخرج والصفة، وهي تماثل أو تجانس أو تقارب أو تباعد. |
| [`line`](#line) | Line | السطر | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | السطر هو السطر الطباعي داخل صفحة مصحف أو تخطيط معين. |
| [`madani`](#madani) | Madani | مدني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | المدني ما نزل من القرآن بعد الهجرة، ولو نزل خارج المدينة. |
| [`madd`](#madd) | Madd | المد | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | المد إطالة الصوت بحرف من حروف المد الـ3، وهي الألف الساكنة بعد فتح والواو الساكنة بعد ضم والياء الساكنة بعد كسر. |
| [`madd_al_badal`](#madd_al_badal) | Madd al-Badal | مد البدل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد البدل مد سببه همزة قبل حرف المد، وأُبدل فيه حرف المد من همزة ساكنة، مثل «آمن» و«أوتوا» و«إيمان». |
| [`madd_al_iwad`](#madd_al_iwad) | Madd al-Iwad | مد العوض | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد العوض هو مد الألف عوضًا عن تنوين الفتح عند الوقف على الكلمة، ومقداره حركتان. |
| [`madd_al_lin`](#madd_al_lin) | Madd al-Lin | مد اللين | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد اللين هو مد الواو أو الياء الساكنة المفتوح ما قبلها عند الوقف على الكلمة بسكون عارض، مثل «خوف» و«بيت». |
| [`madd_al_silah`](#madd_al_silah) | Madd al-Silah | مد الصلة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد الصلة مد ينشأ عن صلة هاء الضمير بواو أو ياء إذا وقعت بين متحركين. |
| [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun) | Madd Arid lil-Sukun | المد العارض للسكون | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد العارض للسكون مد سببه سكون عارض في الوقف بعد حرف المد، ويجوز فيه القصر والتوسط والطول. |
| [`madd_lazim`](#madd_lazim) | Madd Lazim | المد اللازم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد اللازم مد فرعي سببه سكون أصلي ثابت في الوصل والوقف بعد حرف المد، ويقع في كلمة أو في حرف من فواتح السور. |
| [`madd_munfasil`](#madd_munfasil) | Madd Munfasil | المد المنفصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد المنفصل مد فرعي سببه همزة في أول الكلمة التالية لحرف المد، وهو جائز، فيُقصر ويُمد بحسب الرواية والطريق. |
| [`madd_muttasil`](#madd_muttasil) | Madd Muttasil | المد المتصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد المتصل مد فرعي سببه همزة بعد حرف المد في كلمة واحدة، وهو واجب عند القراء جميعًا، وتختلف مقاديره بحسب الرواية والطريق. |
| [`madd_tabii`](#madd_tabii) | Madd Tabee | المد الطبيعي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد الطبيعي هو المد الذي لا تقوم ذات حرف المد إلا به، ولا يتوقف على سبب من همز أو سكون، ومقداره حركتان. |
| [`maddah`](#maddah) | Maddah | المدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | المدة علامة تدل على لزوم مد الحرف مدًّا زائدًا على المد الطبيعي. |
| [`makki`](#makki) | Makki | مكي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | المكي ما نزل من القرآن قبل الهجرة، ولو نزل خارج مكة. |
| [`manzil`](#manzil) | Manzil | المنزل | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | المنزل واحد من 7 أقسام تقليدية للقرآن، والغرض من هذا التقسيم تيسير ختمه في أسبوع. |
| [`mathani`](#mathani) | Mathani | المثاني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | المثاني هي السور التي تقل آياتها عن المئين وتليها في التقسيم التقليدي، وسميت مثاني لكثرة ما تُثنى، أي تتكرر قراءتها. |
| [`meem_sakinah`](#meem_sakinah) | Meem Sakinah | الميم الساكنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | الميم الساكنة ميم خالية من الحركة، ثابتة في اللفظ والخط، وتقع في وسط الكلمة أو آخرها. |
| [`miun`](#miun) | Miun | المئون | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | المئون هي السور التي تقارب آياتها المئة أو تزيد عليها أو تنقص عنها قليلًا. |
| [`morpheme`](#morpheme) | Morpheme | الوحدة الصرفية | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الوحدة الصرفية أصغر وحدة في الكلمة تحمل معنى أو وظيفة صرفية، مثل السابقة واللاحقة والجذع. |
| [`morphology`](#morphology) | Morphology | الصرف | <span dir="ltr">`analysis`</span> | <span dir="ltr">`linguistics`</span> | الصرف تحليل بنية الكلمة وصيغتها وما تحمله من خصائص صرفية. |
| [`muallim`](#muallim) | Muallim | معلم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | المعلم نمط تلاوة معد للتعليم، وقد يتضمن تكرار الآيات أو إتاحة وقت للمتعلم للترديد. |
| [`mufassal`](#mufassal) | Mufassal | المفصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | المفصل مجموعة من قصار السور التي تلي المثاني، ويختلف العلماء في أولها. |
| [`mufassir`](#mufassir) | Mufassir | المفسر | <span dir="ltr">`role`</span> | <span dir="ltr">`tafsir`</span> | المفسر من نُسب إليه تفسير للقرآن، تأليفًا أو رواية. |
| [`mujawwad`](#mujawwad) | Mujawwad | مجود | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | المجود نمط أداء بطيء يُمد فيه الصوت وتُستوفى أحكام التجويد بتطريب، وهو الوصف الذي تُنشر به التسجيلات المؤداة على هذا النحو. |
| [`muqatta_letter`](#muqatta_letter) | Muqatta Letter | الحرف المقطع | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | الحروف المقطعة حروف هجائية افتتحت بها بعض السور، مثل «الم» و«الر» و«حم» و«كهيعص». |
| [`muqri`](#muqri) | Muqri | المقرئ | <span dir="ltr">`role`</span> | <span dir="ltr">`qiraat`</span> | المقرئ من تلقى القراءة وأتقنها وينقلها إلى المتعلمين. |
| [`murattal`](#murattal) | Murattal | مرتل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | المرتل نمط أداء متزن دون تطريب، على مرتبة الترتيل، وهو الوصف الذي تُنشر به التسجيلات المؤداة على هذا النحو. |
| [`mushaf`](#mushaf) | Mushaf | المصحف | <span dir="ltr">`entity`</span> | <span dir="ltr">`core`</span> | المصحف هو الصحف التي جُمع فيها القرآن مكتوبًا ومرتبًا على ترتيبه المعروف. |
| [`mushaf_edition`](#mushaf_edition) | Mushaf Edition | طبعة المصحف | <span dir="ltr">`entity`</span> | <span dir="ltr">`core`</span> | طبعة المصحف إصدار منشور محدد من المصحف، له خصائص محددة مثل الناشر والرسم والضبط والتخطيط وغيرها. |
| [`mushaf_mark`](#mushaf_mark) | Mushaf Mark | علامة المصحف | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | علامة المصحف رمز أو علامة غير داخلة في الحروف الأصلية للكلمة، وتستخدم في المصحف لأغراض القراءة أو التنظيم أو الإرشاد. |
| [`mutajanisan`](#mutajanisan) | Mutajanisan | المتجانسان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المتجانسان حرفان اتحدا في المخرج واختلفا في الصفة، مثل الدال والتاء في «قد تبين». |
| [`mutamathilan`](#mutamathilan) | Mutamathilan | المتماثلان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المتماثلان حرفان اتحدا في المخرج والصفة، مثل الباء في «اضرب بعصاك». |
| [`mutashabihat`](#mutashabihat) | Mutashabihat | المتشابهات | <span dir="ltr">`analysis`</span> | <span dir="ltr">`quranic_sciences`</span> | المتشابهات هي المواضع التي يتشابه فيها لفظ الآيات أو أجزائها في القرآن، تشابهًا تامًّا أو مع اختلاف يسير في كلمة أو ترتيب. |
| [`noon_sakinah`](#noon_sakinah) | Noon Sakinah | النون الساكنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | النون الساكنة هي نون خالية من الحركة، تثبت في اللفظ والخط وفي حالي الوصل والوقف. |
| [`noun`](#noun) | Noun | الاسم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | الاسم هو ما دل على معنى في نفسه غير مقترن بزمان، وتدخل فيه الأسماء والصفات والضمائر وأسماء الإشارة والموصولات. |
| [`omitted_alif`](#omitted_alif) | Omitted Alif | الألف المحذوفة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الألف المحذوفة علامة تدل على ألف محذوفة من الرسم واجبة النطق. |
| [`orthographic_mark`](#orthographic_mark) | Orthographic Mark | العلامة الإملائية | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | العلامة الإملائية هي علامة تضبط رسم الكلمة، مثل الهمزة والمدة والحروف الصغيرة. |
| [`page`](#page) | Page | الصفحة | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | الصفحة هي وحدة طباعية من تخطيط مصحف معين، وقد يختلف محتواها وحدودها باختلاف المصحف أو الطبعة. |
| [`part_of_speech`](#part_of_speech) | Part of Speech | قسم الكلمة | <span dir="ltr">`classification`</span> | <span dir="ltr">`linguistics`</span> | قسم الكلمة هو تصنيف الكلمة أو الوحدة الصرفية بحسب بابها النحوي، مثل الاسم والفعل والحرف وما يتفرع عنها. |
| [`particle`](#particle) | Particle | حرف المعنى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | حرف المعنى هو ما دل على معنى في غيره، مثل حروف الجر والعطف والنفي والاستفهام. |
| [`qalqalah`](#qalqalah) | Qalqalah | القلقلة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | القلقلة هي اضطراب في صوت الحرف الساكن عند النطق به حتى تسمع له نبرة قوية. |
| [`qiraah`](#qiraah) | Qiraah | القراءة | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | القراءة هي وجه من وجوه قراءة القرآن ينسب إلى إمام من أئمة القراءات، وتتفرع عنه الروايات والطرق. |
| [`qiraah_mark`](#qiraah_mark) | Qiraah Mark | علامة القراءة | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | علامة القراءة هي علامة ترشد إلى وجه من وجوه الأداء في موضعها، مثل السكت والإشمام والتسهيل. |
| [`quran`](#quran) | Quran | القرآن | <span dir="ltr">`concept`</span> | <span dir="ltr">`core`</span> | القرآن هو كلام الله المنزل على محمد صلى الله عليه وسلم والمتعبد بتلاوته. |
| [`quran_merits`](#quran_merits) | Quran Merits | فضائل القرآن | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | فضائل القرآن هي ما ورد في فضل القرآن أو فضل سورة منه أو آية، وما يترتب على قراءتها من أجر أو أثر. |
| [`rasm`](#rasm) | Rasm | الرسم | <span dir="ltr">`classification`</span> | <span dir="ltr">`mushaf`</span> | الرسم هو طريقة كتابة ألفاظ القرآن من حيث إثبات الحروف وحذفها وزيادتها وفصلها ووصلها وما يشبه ذلك. |
| [`rasm_imlai`](#rasm_imlai) | Rasm Imlai | الرسم الإملائي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`mushaf`</span> | الرسم الإملائي هو كتابة ألفاظ القرآن على قواعد الإملاء المعاصرة، بإثبات ما يحذف في الرسم العثماني وحذف ما يزاد فيه، حتى تقرأ الكلمة على صورتها المألوفة. |
| [`rasm_uthmani`](#rasm_uthmani) | Rasm Uthmani | الرسم العثماني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`mushaf`</span> | الرسم العثماني هو طريقة كتابة كلمات المصاحف العثمانية وما يتعلق بها من حذف وزيادة وبدل وفصل ووصل. |
| [`rawi`](#rawi) | Rawi | الراوي | <span dir="ltr">`role`</span> | <span dir="ltr">`qiraat`</span> | الراوي هو من نسبت إليه الرواية عن إمام القراءة. |
| [`recitation`](#recitation) | Recitation | تسجيل التلاوة | <span dir="ltr">`entity`</span> | <span dir="ltr">`recitation`</span> | تسجيل التلاوة هو تسجيل منشور لتلاوة القرآن، منسوب إلى قارئ ورواية ونمط أداء. |
| [`recitation_pace`](#recitation_pace) | Recitation Pace | مراتب القراءة | <span dir="ltr">`classification`</span> | <span dir="ltr">`recitation_pace`</span> | مراتب القراءة هي تصنيف لسرعة أداء القراءة مع المحافظة على أحكامها. |
| [`recitation_style`](#recitation_style) | Recitation Style | نمط الأداء | <span dir="ltr">`classification`</span> | <span dir="ltr">`recitation_style`</span> | نمط الأداء هو تصنيف للتسجيلات والتلاوات بحسب طريقة أدائها، وهي مرتل أو مجود أو معلم، وهو مستقل عن القراءة والرواية. |
| [`reciter`](#reciter) | Reciter | القارئ | <span dir="ltr">`role`</span> | <span dir="ltr">`recitation`</span> | القارئ هو الشخص الذي يؤدي تلاوة القرآن. |
| [`rectangular_zero`](#rectangular_zero) | Rectangular Zero | الصفر المستطيل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الصفر المستطيل علامة تدل على زيادة الألف في الوصل دون الوقف، ولذلك تنطق عند الوقف عليها. |
| [`reflection`](#reflection) | Reflection | التدبر | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | التدبر هو التأمل في معاني القرآن وما يقتضيه من عمل، وما يقيده القارئ من وقفة عند آية أو لفظة. |
| [`revelation`](#revelation) | Revelation | النزول | <span dir="ltr">`concept`</span> | <span dir="ltr">`revelation`</span> | النزول هو إنزال القرآن على النبي صلى الله عليه وسلم مفرقًا على مدة الرسالة بحسب الوقائع والحاجة. |
| [`revelation_classification`](#revelation_classification) | Revelation Classification | تصنيف النزول | <span dir="ltr">`classification`</span> | <span dir="ltr">`revelation`</span> | تصنيف النزول هو تصنيف للنص القرآني بحسب وقوع نزوله قبل الهجرة أو بعدها وفق الاصطلاح المعتمد. |
| [`revelation_order`](#revelation_order) | Revelation Order | ترتيب النزول | <span dir="ltr">`property`</span> | <span dir="ltr">`revelation`</span> | ترتيب النزول هو ترتيب السور أو الآيات بحسب زمن نزولها، وقد يختلف بحسب المصدر المعتمد. |
| [`riwayah`](#riwayah) | Riwayah | الرواية | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | الرواية هي ما ينسب إلى راو عن إمام القراءة، مثل رواية حفص عن عاصم. |
| [`root`](#root) | Root | الجذر | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الجذر هو الأصل الصرفي الذي ترد إليه الكلمة لبيان اشتقاقها وصلتها بالكلمات الأخرى. |
| [`rounded_zero`](#rounded_zero) | Rounded Zero | الصفر المستدير | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الصفر المستدير علامة تدل على زيادة الحرف في الرسم، ولذلك لا ينطق في الوصل ولا في الوقف. |
| [`rubu_al_hizb`](#rubu_al_hizb) | Rubu al-Hizb | ربع الحزب | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | ربع الحزب هو الجزء الرابع من الحزب في التقسيم المشهور للمصحف. |
| [`ruku`](#ruku) | Ruku | الركوع | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | الركوع هو قسم اصطلاحي من القرآن يستخدم لتنظيم القراءة ويظهر في بعض المصاحف. |
| [`saba_tiwal`](#saba_tiwal) | Saba Tiwal | السبع الطوال | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | السبع الطوال هي مجموعة من أطول سور القرآن في أوله، مع خلاف معروف في تعيين السورة السابعة. |
| [`sajdah`](#sajdah) | Sajdah | السجدة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | السجدة موضع من مواضع سجود التلاوة في القرآن، ينتهي بآية بعينها، يسجد عنده القارئ والسامع. |
| [`sajdah_line`](#sajdah_line) | Sajdah Line | خط السجدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | خط السجدة خط فوق الكلمة يدل على أنها الكلمة الموجبة للسجدة. |
| [`sajdah_mark`](#sajdah_mark) | Sajdah Mark | علامة السجدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة السجدة علامة تدل على موضع السجود. |
| [`saktah`](#saktah) | Saktah | السكتة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | السكتة هي قطع الصوت زمنًا يسيرًا من غير تنفس ثم متابعة القراءة. |
| [`saktah_mark`](#saktah_mark) | Saktah Mark | علامة السكتة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة السكتة علامة تدل على السكت، وهو وقفة يسيرة من غير تنفس ثم الوصل بما بعده. |
| [`seen_al_qiraah`](#seen_al_qiraah) | Seen al-Qiraah | سين القراءة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | سين القراءة سين صغيرة فوق الصاد تدل على القراءة بالسين، وتحتها تدل على القراءة بالصاد. |
| [`shaddah`](#shaddah) | Shaddah | الشدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الشدة علامة تدل على تشديد الحرف، أي إدغام الأول الساكن في الثاني المتحرك حتى ينطقا حرفًا واحدًا مشددًا. |
| [`small_meem`](#small_meem) | Small Meem | الميم الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الميم الصغيرة علامة تدل على قلب النون الساكنة أو التنوين ميمًا عند الباء. |
| [`small_noon`](#small_noon) | Small Noon | النون الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | النون الصغيرة علامة تدل على نون محذوفة من الرسم واجبة النطق، وترد في موضع واحد (21:88). |
| [`small_waw`](#small_waw) | Small Waw | الواو الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الواو الصغيرة علامة تدل على صلة هاء الضمير المضمومة بواو لفظية في حال الوصل. |
| [`small_yaa`](#small_yaa) | Small Yaa | الياء الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الياء الصغيرة علامة تدل على صلة هاء الضمير المكسورة بياء لفظية في حال الوصل. |
| [`spoken_translation`](#spoken_translation) | Spoken Translation | الترجمة المنطوقة | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | الترجمة المنطوقة هي نقل معاني القرآن إلى لغة أخرى في مادة صوتية أو منطوقة. |
| [`stem`](#stem) | Stem | الجذع | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الجذع هو ما يبقى من الكلمة بعد نزع السوابق واللواحق، وتلحق به الزوائد الصرفية. |
| [`sukun`](#sukun) | Sukun | السكون | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | السكون علامة تدل على سكون الحرف وإظهاره. |
| [`surah`](#surah) | Surah | السورة | <span dir="ltr">`entity`</span> | <span dir="ltr">`structure`</span> | السورة هي وحدة رئيسية من بنية القرآن، تتكون من آيات مرتبة ولها اسم وموضع معروف في ترتيب المصحف. |
| [`surah_group`](#surah_group) | Surah Group | تصنيف السور | <span dir="ltr">`classification`</span> | <span dir="ltr">`surah_classification`</span> | تصنيف السور هو تصنيف يجمع سورًا وفق تقسيمات اصطلاحية موروثة تعتمد الطول أو موضع السورة ضمن مجموعات السور. |
| [`surah_name_reason`](#surah_name_reason) | Surah Name Reason | سبب التسمية | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | سبب التسمية هو بيان العلة التي سميت بها السورة اسمها، وما ورد في ذلك من أثر أو وجه لغوي. |
| [`surah_names`](#surah_names) | Surah Names | أسماء السورة | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | أسماء السورة هي ما سميت به السورة من أسماء. |
| [`surah_objectives`](#surah_objectives) | Surah Objectives | مقاصد السورة | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | مقاصد السورة هي المعاني الكلية التي تدور عليها السورة ويجمع بينها موضوعها، وهي الغرض الواحد الذي تنتظم به آياتها. |
| [`tadwir`](#tadwir) | Tadwir | التدوير | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | التدوير هو القراءة بسرعة متوسطة بين التحقيق والحدر مع المحافظة على الأحكام. |
| [`tafkhim`](#tafkhim) | Tafkhim | التفخيم | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | التفخيم هو سمن يدخل على صوت الحرف فيمتلئ الفم بصداه. |
| [`tafsir`](#tafsir) | Tafsir | التفسير | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | التفسير هو بيان معاني القرآن وشرح ألفاظه وما يرشد إليه من أحكام وهدايات بحسب أصول التفسير. |
| [`tafsir_al_ray`](#tafsir_al_ray) | Tafsir al-Ray | تفسير الرأي | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | تفسير الرأي هو بيان معاني القرآن بالاجتهاد والنظر بعد معرفة كلام العرب وأساليبه وأصول التفسير، سواء كان الاجتهاد محمودًا أو مذمومًا. |
| [`tafsir_mathur`](#tafsir_mathur) | Tafsir Mathur | التفسير المأثور | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | التفسير المأثور هو ما فسر به القرآن من القرآن نفسه أو من السنة أو من قول الصحابة والتابعين، منقولًا بإسناده. |
| [`tahqiq`](#tahqiq) | Tahqiq | التحقيق | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | التحقيق هو القراءة ببطء وتؤدة مع استيفاء الحروف وأحكامها، ويستخدم كثيرًا في مقام التعليم. |
| [`tajwid`](#tajwid) | Tajweed | التجويد | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | التجويد هو علم أداء حروف القرآن من مخارجها وإعطائها حقوقها ومستحقاتها من الصفات والأحكام. |
| [`tajwid_ruling`](#tajwid_ruling) | Tajwid Ruling | حكم التجويد | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | حكم التجويد هو ما تقرره قواعد التجويد في أداء الحرف في موضع بعينه من النص، عند حرف يليه أو عند سكون أو همز، مثل الإظهار والإدغام والإقلاب والإخفاء والمد والقلقلة والتفخيم والترقيق. |
| [`tanwin`](#tanwin) | Tanwin | التنوين | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | التنوين هو نون ساكنة زائدة تلحق آخر الاسم، وترسم بتكرار صورة الحركة. |
| [`tanwin_al_damm`](#tanwin_al_damm) | Tanwin al-Damm | تنوين الضم | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | تنوين الضم علامة تدل على التنوين المرفوع. |
| [`tanwin_al_fath`](#tanwin_al_fath) | Tanwin al-Fath | تنوين الفتح | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | تنوين الفتح علامة تدل على التنوين المنصوب. |
| [`tanwin_al_kasr`](#tanwin_al_kasr) | Tanwin al-Kasr | تنوين الكسر | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | تنوين الكسر علامة تدل على التنوين المخفوض. |
| [`tariq`](#tariq) | Tariq | الطريق | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | الطريق هو وجه النقل المأخوذ عن الراوي بواسطة من دونه في سلسلة نقل القراءة. |
| [`tarqiq`](#tarqiq) | Tarqiq | الترقيق | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | الترقيق هو نحول يدخل على صوت الحرف فلا يمتلئ الفم بصداه. |
| [`tartil`](#tartil) | Tartil | الترتيل | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | الترتيل هو قراءة القرآن بتؤدة وبيان للحروف والكلمات ومراعاة الوقف والمعنى. |
| [`tashil`](#tashil) | Tashil | التسهيل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة التسهيل تدل على تسهيل الهمزة بين بين، أي بينها وبين الألف. |
| [`tashkil`](#tashkil) | Tashkil | التشكيل | <span dir="ltr">`concept`</span> | <span dir="ltr">`dabt`</span> | التشكيل هو طبقة علامات الضبط الملحقة بحروف النص، من الحركات والتنوين والشدة والسكون وما يتبعها، منظورًا إليها جملة واحدة. |
| [`three_dots`](#three_dots) | Three Dots | الثلاث نقط | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الثلاث نقط ثلاث نقاط فوق الحرف تميزه عن الحرف الذي يشاركه في الرسم، مثل الثاء والشين. |
| [`thumn`](#thumn) | Thumn | الثمن | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | الثمن هو الجزء الثامن من الحزب، وهو تقسيم مستخدم في بعض المصاحف والمدارس. |
| [`tilawah`](#tilawah) | Tilawah | التلاوة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | التلاوة هي قراءة القرآن بلفظه أداء بالصوت على ما تلقاه القارئ، سواء كانت في صلاة أو درس أو تسجيل. |
| [`token`](#token) | Token |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | `token` هو وحدة ينتجها تقسيم النص وفق منهج معلن. |
| [`translation`](#translation) | Translation | الترجمة | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | الترجمة هي نقل معاني القرآن إلى لغة أخرى، وهي ليست قرآنًا بلفظه. |
| [`translator`](#translator) | Translator | المترجم | <span dir="ltr">`role`</span> | <span dir="ltr">`translation`</span> | المترجم هو من نسبت إليه ترجمة لمعاني القرآن إلى لغة أخرى، سواء كان فردًا أو هيئة. |
| [`transliteration`](#transliteration) | Transliteration | النقل الحرفي | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | النقل الحرفي هو تمثيل حروف نظام كتابي بحروف نظام آخر وفق قواعد محددة، دون ترجمة المعنى. |
| [`two_dots`](#two_dots) | Two Dots | النقطتان | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | النقطتان نقطتان فوق الحرف أو تحته تميزانه عن الحرف الذي يشاركه في الرسم، مثل التاء والياء والقاف. |
| [`verb`](#verb) | Verb | الفعل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | الفعل هو ما دل على معنى في نفسه مقترن بزمان، ويتصرف إلى الماضي والمضارع والأمر. |
| [`wajh`](#wajh) | Wajh | الوجه | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | الوجه هو كيفية من كيفيات الأداء يجوز الأخذ بأي منها في الرواية الواحدة أو الطريق الواحد، مثل أوجه المد العارض للسكون. |
| [`waqf`](#waqf) | Waqf | الوقف | <span dir="ltr">`concept`</span> | <span dir="ltr">`waqf`</span> | الوقف هو قطع القراءة عند موضع من النص وفق أحكام الوقف والابتداء. |
| [`waqf_al_muanaqah`](#waqf_al_muanaqah) | Waqf al-Muanaqah | وقف المعانقة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | وقف المعانقة علامة تدل على موضعين للوقف، إذا وقف القارئ على أحدهما لم يصح الوقف على الآخر. |
| [`waqf_hasan`](#waqf_hasan) | Waqf Hasan | الوقف الحسن | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | الوقف الحسن هو الوقف على ما أفاد معنًى وتعلق بما بعده لفظًا ومعنًى. |
| [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn) | Waqf Jaiz Mustawi al-Tarafayn | الوقف الجائز مستوي الطرفين | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف الجائز علامة تدل على أن الوقف جائز جوازًا مستوي الطرفين، فالوقف والوصل فيه سواء. |
| [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla) | Waqf Jaiz Waqf Awla | الوقف الجائز مع كون الوقف أولى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | علامة الوقف أولى تدل على أن الوقف جائز والوقف أولى. |
| [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla) | Waqf Jaiz Wasl Awla | الوقف الجائز مع كون الوصل أولى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | علامة الوصل أولى تدل على أن الوقف جائز والوصل أولى. |
| [`waqf_kafi`](#waqf_kafi) | Waqf Kafi | الوقف الكافي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | الوقف الكافي هو الوقف على ما تم معناه وتعلق بما بعده في المعنى دون اللفظ. |
| [`waqf_lazim`](#waqf_lazim) | Waqf Lazim | الوقف اللازم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف اللازم علامة تدل على أن الوقف لازم، لأن وصل ما بعده بما قبله يوهم خلاف المعنى المراد. |
| [`waqf_mamnu`](#waqf_mamnu) | Waqf Mamnu | الوقف الممنوع | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف الممنوع علامة تدل على أن الوقف ممنوع، لأن الوقف على الموضع يفسد المعنى أو يقطع ما لا ينفصل عما بعده. |
| [`waqf_mark`](#waqf_mark) | Waqf Mark | علامة الوقف | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة الوقف علامة في المصحف ترشد القارئ إلى حكم الوقف أو الوصل في موضع معين. |
| [`waqf_mark_type`](#waqf_mark_type) | Waqf Mark Type | نوع علامة الوقف | <span dir="ltr">`classification`</span> | <span dir="ltr">`waqf`</span> | نوع علامة الوقف هو تصنيف لما ترشد إليه علامة الوقف المرسومة في المصحف من لزوم أو منع أو جواز. |
| [`waqf_qabih`](#waqf_qabih) | Waqf Qabih | الوقف القبيح | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | الوقف القبيح هو الوقف على ما لم يفد معنًى، أو أفاد معنًى غير مراد. |
| [`waqf_ruling`](#waqf_ruling) | Waqf Ruling | حكم الوقف | <span dir="ltr">`classification`</span> | <span dir="ltr">`waqf`</span> | حكم الوقف هو تصنيف الموضع نفسه من جهة تمام المعنى عنده، وليس من جهة العلامة المرسومة عليه. |
| [`waqf_tamm`](#waqf_tamm) | Waqf Tamm | الوقف التام | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | الوقف التام هو الوقف على ما تم معناه ولم يتعلق بما بعده لفظًا ولا معنًى. |
| [`word`](#word) | Word | الكلمة | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | الكلمة هي وحدة من النص يعرفها القارئ كلمة واحدة، ولا يتغير عدها بتغير منهج تقسيم النص. |
| [`word_by_word_translation`](#word_by_word_translation) | Word by Word Translation |  | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | الترجمة كلمة بكلمة هي ترجمة تعطي كل كلمة من كلمات الآية معناها في لغة أخرى على حدة، بترتيب كلمات الأصل. |
| [`word_key`](#word_key) | Word Key |  | <span dir="ltr">`property`</span> | <span dir="ltr">`structure`</span> | مفتاح الكلمة هو معرف نصي للكلمة يضيف إلى مفتاح الآية موضع الكلمة فيها، على صورة `2:255:5`. |
| [`word_meanings`](#word_meanings) | Word Meanings | غريب القرآن | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | غريب القرآن هو بيان معاني الألفاظ القرآنية التي خفي معناها على أكثر القراء، لقلة استعمالها أو لتغير دلالتها. |
| [`word_timing`](#word_timing) | Word Timing |  | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | توقيت الكلمة هو مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل كلمة بعينها من آية. |

## حسب المجال

- **الأساس** — `core`: <span dir="ltr">[`mushaf`](#mushaf)، [`mushaf_edition`](#mushaf_edition)، [`quran`](#quran)</span>
- **البنية** — `structure`: <span dir="ltr">[`ayah`](#ayah)، [`ayah_ending`](#ayah_ending)، [`ayah_key`](#ayah_key)، [`basmalah`](#basmalah)، [`muqatta_letter`](#muqatta_letter)، [`sajdah`](#sajdah)، [`surah`](#surah)، [`word_key`](#word_key)</span>
- **النص** — `text`: <span dir="ltr">[`character`](#character)، [`codepoint`](#codepoint)، [`glyph`](#glyph)، [`grapheme`](#grapheme)، [`letter`](#letter)، [`token`](#token)، [`word`](#word)</span>
- **أقسام القرآن** — `divisions`: <span dir="ltr">[`hizb`](#hizb)، [`juz`](#juz)، [`manzil`](#manzil)، [`rubu_al_hizb`](#rubu_al_hizb)، [`ruku`](#ruku)، [`thumn`](#thumn)</span>
- **تصنيف السور** — `surah_classification`: <span dir="ltr">[`mathani`](#mathani)، [`miun`](#miun)، [`mufassal`](#mufassal)، [`saba_tiwal`](#saba_tiwal)، [`surah_group`](#surah_group)</span>
- **المصحف والتخطيط** — `mushaf`: <span dir="ltr">[`ayah_fragment`](#ayah_fragment)، [`font`](#font)، [`layout`](#layout)، [`line`](#line)، [`page`](#page)، [`rasm`](#rasm)، [`rasm_imlai`](#rasm_imlai)، [`rasm_uthmani`](#rasm_uthmani)</span>
- **الضبط وعلامات المصحف** — `dabt`: <span dir="ltr">[`ayah_mark`](#ayah_mark)، [`dammah`](#dammah)، [`division_mark`](#division_mark)، [`dot`](#dot)، [`fathah`](#fathah)، [`hamzah`](#hamzah)، [`hamzat_al_wasl`](#hamzat_al_wasl)، [`harakah`](#harakah)، [`ijam`](#ijam)، [`imalah`](#imalah)، [`ishmam`](#ishmam)، [`kasrah`](#kasrah)، [`maddah`](#maddah)، [`mushaf_mark`](#mushaf_mark)، [`omitted_alif`](#omitted_alif)، [`orthographic_mark`](#orthographic_mark)، [`qiraah_mark`](#qiraah_mark)، [`rectangular_zero`](#rectangular_zero)، [`rounded_zero`](#rounded_zero)، [`sajdah_line`](#sajdah_line)، [`sajdah_mark`](#sajdah_mark)، [`saktah_mark`](#saktah_mark)، [`seen_al_qiraah`](#seen_al_qiraah)، [`shaddah`](#shaddah)، [`small_meem`](#small_meem)، [`small_noon`](#small_noon)، [`small_waw`](#small_waw)، [`small_yaa`](#small_yaa)، [`sukun`](#sukun)، [`tanwin`](#tanwin)، [`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)، [`tashil`](#tashil)، [`tashkil`](#tashkil)، [`three_dots`](#three_dots)، [`two_dots`](#two_dots)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)، [`waqf_mark`](#waqf_mark)</span>
- **عد الآي** — `ayah_numbering`: <span dir="ltr">[`ayah_count`](#ayah_count)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_first`](#ayah_numbering_madani_first)، [`ayah_numbering_madani_last`](#ayah_numbering_madani_last)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_numbering_system`](#ayah_numbering_system)، [`equivalent_ayah`](#equivalent_ayah)</span>
- **النزول** — `revelation`: <span dir="ltr">[`asbab_al_nuzul`](#asbab_al_nuzul)، [`disputed`](#disputed)، [`madani`](#madani)، [`makki`](#makki)، [`revelation`](#revelation)، [`revelation_classification`](#revelation_classification)، [`revelation_order`](#revelation_order)</span>
- **القراءات** — `qiraat`: <span dir="ltr">[`muqri`](#muqri)، [`qiraah`](#qiraah)، [`rawi`](#rawi)، [`riwayah`](#riwayah)، [`tariq`](#tariq)، [`wajh`](#wajh)</span>
- **التلاوة** — `recitation`: <span dir="ltr">[`ayah_timing`](#ayah_timing)، [`istiadhah`](#istiadhah)، [`khatmah`](#khatmah)، [`recitation`](#recitation)، [`reciter`](#reciter)، [`tartil`](#tartil)، [`tilawah`](#tilawah)، [`word_timing`](#word_timing)</span>
- **مراتب القراءة** — `recitation_pace`: <span dir="ltr">[`hadr`](#hadr)، [`recitation_pace`](#recitation_pace)، [`tadwir`](#tadwir)، [`tahqiq`](#tahqiq)</span>
- **أنماط الأداء** — `recitation_style`: <span dir="ltr">[`instructional_ayah_repetition`](#instructional_ayah_repetition)، [`muallim`](#muallim)، [`mujawwad`](#mujawwad)، [`murattal`](#murattal)، [`recitation_style`](#recitation_style)</span>
- **التجويد** — `tajwid`: <span dir="ltr">[`ghunnah`](#ghunnah)، [`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`izhar`](#izhar)، [`letter_relation`](#letter_relation)، [`madd`](#madd)، [`madd_al_badal`](#madd_al_badal)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_lin`](#madd_al_lin)، [`madd_al_silah`](#madd_al_silah)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`madd_lazim`](#madd_lazim)، [`madd_munfasil`](#madd_munfasil)، [`madd_muttasil`](#madd_muttasil)، [`madd_tabii`](#madd_tabii)، [`meem_sakinah`](#meem_sakinah)، [`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)، [`noon_sakinah`](#noon_sakinah)، [`qalqalah`](#qalqalah)، [`saktah`](#saktah)، [`tafkhim`](#tafkhim)، [`tajwid`](#tajwid)، [`tajwid_ruling`](#tajwid_ruling)، [`tarqiq`](#tarqiq)</span>
- **الوقف** — `waqf`: <span dir="ltr">[`waqf`](#waqf)، [`waqf_hasan`](#waqf_hasan)، [`waqf_kafi`](#waqf_kafi)، [`waqf_mark_type`](#waqf_mark_type)، [`waqf_qabih`](#waqf_qabih)، [`waqf_ruling`](#waqf_ruling)، [`waqf_tamm`](#waqf_tamm)</span>
- **اللغة** — `linguistics`: <span dir="ltr">[`irab`](#irab)، [`lemma`](#lemma)، [`morpheme`](#morpheme)، [`morphology`](#morphology)، [`noun`](#noun)، [`part_of_speech`](#part_of_speech)، [`particle`](#particle)، [`root`](#root)، [`stem`](#stem)، [`verb`](#verb)</span>
- **الترجمة** — `translation`: <span dir="ltr">[`spoken_translation`](#spoken_translation)، [`translation`](#translation)، [`translator`](#translator)، [`transliteration`](#transliteration)، [`word_by_word_translation`](#word_by_word_translation)</span>
- **التفسير** — `tafsir`: <span dir="ltr">[`mufassir`](#mufassir)، [`tafsir`](#tafsir)، [`tafsir_al_ray`](#tafsir_al_ray)، [`tafsir_mathur`](#tafsir_mathur)</span>
- **علوم القرآن** — `quranic_sciences`: <span dir="ltr">[`abrogation`](#abrogation)، [`mutashabihat`](#mutashabihat)، [`quran_merits`](#quran_merits)، [`reflection`](#reflection)، [`surah_name_reason`](#surah_name_reason)، [`surah_names`](#surah_names)، [`surah_objectives`](#surah_objectives)، [`word_meanings`](#word_meanings)</span>

## الأساس — `core`

<a id="mushaf"></a>

### المصحف — Mushaf

<!-- source: standards/terminology/concepts/mushaf.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mushaf`</span> |
| `plural` | <span dir="ltr">`mushafs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُصْحَف |
| تهجئات أخرى | <span dir="ltr">`mus'haf`، `muṣḥaf`، `moshaf`</span> |
| مقابل إنجليزي | <span dir="ltr">`Quran Codex`</span> |

**التعريف:** المصحف هو الصحف التي جُمع فيها القرآن مكتوبًا ومرتبًا على ترتيبه المعروف.

**الغرض:** نستخدمه عندما تكون خصائص التمثيل المكتوب للقرآن مهمة، مثل الرسم والتخطيط والصفحات والأسطر والعلامات.

- المصحف وعاء مكتوب للقرآن وليس القرآن نفسه، فالمصاحف تختلف في الرسم والصفحات والعلامات والقرآن واحد.

**مرتبط به:** <span dir="ltr">[`quran`](#quran)، [`mushaf_edition`](#mushaf_edition)، [`rasm`](#rasm)، [`layout`](#layout)، [`page`](#page)، [`rasm_uthmani`](#rasm_uthmani)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/119`

<a id="mushaf_edition"></a>

### طبعة المصحف — Mushaf Edition

<!-- source: standards/terminology/concepts/mushaf_edition.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mushaf_edition`</span> |
| `plural` | <span dir="ltr">`mushaf_editions`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| جزء من | <span dir="ltr">[`mushaf`](#mushaf)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | طَبْعَة المُصْحَف |

**التعريف:** طبعة المصحف إصدار منشور محدد من المصحف، له خصائص محددة مثل الناشر والرسم والضبط والتخطيط وغيرها.

**الغرض:** نستخدمها لتمييز الطبعات التي قد تختلف في الصفحات والأسطر والعلامات أو الخصائص الطباعية.

**مرتبط به:** <span dir="ltr">[`mushaf`](#mushaf)، [`layout`](#layout)، [`page`](#page)، [`riwayah`](#riwayah)، [`font`](#font)، [`rasm`](#rasm)، [`ruku`](#ruku)</span>

<a id="quran"></a>

### القرآن — Quran

<!-- source: standards/terminology/concepts/quran.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`quran`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | القُرْآن |
| تهجئات أخرى | <span dir="ltr">`koran`، `qur'an`، `qur’an`، `quraan`، `al_quran`</span> |

**التعريف:** القرآن هو كلام الله المنزل على محمد صلى الله عليه وسلم والمتعبد بتلاوته. ويطلق الاسم على مجموعه وعلى بعضه بحسب السياق.

**الغرض:** نستخدم القرآن لتمثيل المحتوى القرآني نفسه مستقلًا عن مصحف أو تخطيط أو تنسيق أو تمثيل رقمي معين.

- القرآن هو الكلام نفسه، والمصحف هو وعاؤه المكتوب. لذلك ما يخص الصفحات والرسم والعلامات ينسب إلى المصحف وليس إلى القرآن.

**مرتبط به:** <span dir="ltr">[`mushaf`](#mushaf)، [`surah`](#surah)، [`ayah`](#ayah)، [`quran_merits`](#quran_merits)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/15`

## البنية — `structure`

<a id="ayah"></a>

### الآية — Ayah

<!-- source: standards/terminology/concepts/ayah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah`</span> |
| `plural` | <span dir="ltr">`ayahs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الآيَة |
| الجمع | آيات |
| النقحرة | <span dir="ltr">āyah</span> |
| تهجئات أخرى | <span dir="ltr">`aya`، `ayat`، `ayaat`</span> |
| مقابل إنجليزي | <span dir="ltr">`Verse`</span> |

**التعريف:** الآية وحدة من النص القرآني تقع داخل سورة ولها حدود محددة. وقد يختلف رقمها أو بعض حدودها باختلاف نظام عد الآي.

**الغرض:** نستخدمها وحدة أساسية للإشارة إلى النص القرآني، ولربط الترجمات والتفاسير والتلاوات والتحليلات والبيانات الأخرى بموضع محدد من القرآن.

- موقع الآية في صفحة أو سطر يخص المصحف أو تخطيطه، وليس جزءًا من هوية الآية نفسها.
- الفاصلة هي نهاية الآية وليست الآية نفسها.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`ayah_ending`](#ayah_ending)، [`ayah_mark`](#ayah_mark)، [`ayah_key`](#ayah_key)، [`word`](#word)، [`abrogation`](#abrogation)، [`asbab_al_nuzul`](#asbab_al_nuzul)، [`ayah_count`](#ayah_count)، [`ayah_fragment`](#ayah_fragment)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_first`](#ayah_numbering_madani_first)، [`ayah_numbering_madani_last`](#ayah_numbering_madani_last)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_timing`](#ayah_timing)، [`equivalent_ayah`](#equivalent_ayah)، [`mutashabihat`](#mutashabihat)، [`quran`](#quran)، [`quran_merits`](#quran_merits)، [`reflection`](#reflection)، [`sajdah`](#sajdah)، [`tafsir`](#tafsir)، [`tafsir_mathur`](#tafsir_mathur)، [`word_meanings`](#word_meanings)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`

<a id="ayah_ending"></a>

### الفاصلة — Ayah Ending

<!-- source: standards/terminology/concepts/ayah_ending.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_ending`</span> |
| `plural` | <span dir="ltr">`ayah_endings`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفَاصِلَة |
| تهجئات أخرى | <span dir="ltr">`fasila`</span> |
| مقابل إنجليزي | <span dir="ltr">`Verse Ending`</span> |

**التعريف:** الفاصلة هي خاتمة الآية أو المقطع من جهة النظم، ويعرفها بعض العلماء بأنها الكلمة الأخيرة من الآية.

**الغرض:** نستخدمها في الدراسات والبيانات التي تتناول فواصل الآيات والنظم القرآني، ولا نستخدمها مرادفًا لـ`ayah`.

- الفاصلة خاتمة الآية من جهة النظم، أما علامة الآية فهي رسم في المصحف يدل على الفاصلة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`ayah_mark`](#ayah_mark)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/153`

<a id="ayah_key"></a>

### Ayah Key

<!-- source: standards/terminology/concepts/ayah_key.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_key`</span> |
| `plural` | <span dir="ltr">`ayah_keys`</span> |
| `kind` | <span dir="ltr">`property`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| تهجئات أخرى | <span dir="ltr">`ayah_ref`، `ayah_reference`، `aya_key`</span> |
| مقابل إنجليزي | <span dir="ltr">`verse key`</span> |

**التعريف:** مفتاح الآية معرف نصي للآية يجمع رقم سورتها ورقمها داخلها مفصولين بنقطتين، على صورة `2:255`. ولا يُفهم المفتاح إلا مع نظام عد الآي الذي يستند إليه.

**الغرض:** نستخدمه مفتاحًا للربط بين مصادر البيانات ولنقل الإشارة إلى الآية بين الواجهات والملفات. وتقييده بنظام العد يمنع أن يشير المفتاح الواحد إلى موضعين.

- المفتاح مرجع وليس هوية، فتغيير نظام العد يغير المفتاح ولا يغير الآية.
- المفتاح ليس الرقم المتسلسل للآية في المصحف كله.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`word_key`](#word_key)</span>

<a id="basmalah"></a>

### البسملة — Basmalah

<!-- source: standards/terminology/concepts/basmalah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`basmalah`</span> |
| `plural` | <span dir="ltr">`basmalahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | البَسْمَلَة |
| تهجئات أخرى | <span dir="ltr">`basmala`، `bismillah`</span> |

**التعريف:** البسملة هي صيغة «بسم الله الرحمن الرحيم» التي تفتتح بها السور عدا سورة التوبة. ولها أحكام واختلافات مرتبطة بعد الآي.

**الغرض:** نستخدمها لتمييز البسملة وتمثيل موضعها وعلاقتها بالسورة ونظام عد الآي.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`istiadhah`](#istiadhah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/30) — `30`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/145`

<a id="muqatta_letter"></a>

### الحرف المقطع — Muqatta Letter

<!-- source: standards/terminology/concepts/muqatta_letter.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`muqatta_letter`</span> |
| `plural` | <span dir="ltr">`muqatta_letters`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحَرْف المُقَطَّع |
| مقابل إنجليزي | <span dir="ltr">`Disjointed Letters`</span> |

**التعريف:** الحروف المقطعة حروف هجائية افتتحت بها بعض السور، مثل «الم» و«الر» و«حم» و«كهيعص».

**الغرض:** نستخدمه لتعريف هذه الفواتح وتمييزها وربطها بالسور ومواضعها النصية.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/113) — `113`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/361`

<a id="sajdah"></a>

### السجدة — Sajdah

<!-- source: standards/terminology/concepts/sajdah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sajdah`</span> |
| `plural` | <span dir="ltr">`sajdahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السَّجْدَة |
| السجل | <span dir="ltr">[`sajdah`](/guidelines/ar/03-terminology/registries/#sajdah)</span> |
| تهجئات أخرى | <span dir="ltr">`sajda`، `sajdah_place`، `mawdi_al_sajdah`، `sujud_al_tilawah`، `sajdat_al_tilawah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Prostration`، `Prostration of Recitation`</span> |

**التعريف:** السجدة موضع من مواضع سجود التلاوة في القرآن، ينتهي بآية بعينها، يسجد عنده القارئ والسامع. والسجدات معدودة، 15 على المشهور، والعلماء يختلفون في عد بعضها.

**الغرض:** نستخدم السجدة لعد مواضعها وربط كل موضع بسورته وآيته وصفحته، ولربط أحكام السجود وآدابه به، ولتمييز الموضع عن العلامة التي ترسم عنده.

- السجدة موضع من النص والسجود عنده شيء واحد، أما علامة السجدة فرسم في المصحف يدل عليه.

> دُمج من `sajdah_place` و`sujud_al_tilawah`. كان القاموس يفصل الموضع عن الفعل، ولا يخزن برنامج فعلًا بمعزل عن موضعه، والاسم الشائع «السجدات الخمس عشرة» يسمي الاثنين معًا. والسبب في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`sajdah_mark`](#sajdah_mark)، [`sajdah_line`](#sajdah_line)، [`ayah`](#ayah)، [`tilawah`](#tilawah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="surah"></a>

### السورة — Surah

<!-- source: standards/terminology/concepts/surah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`surah`</span> |
| `plural` | <span dir="ltr">`surahs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السُّورَة |
| السجل | <span dir="ltr">[`surahs`](/guidelines/ar/03-terminology/registries/#surahs)</span> |
| تهجئات أخرى | <span dir="ltr">`sura`، `surat`، `soorah`، `suwar`</span> |
| مقابل إنجليزي | <span dir="ltr">`Chapter`</span> |

**التعريف:** السورة هي وحدة رئيسية من بنية القرآن، تتكون من آيات مرتبة ولها اسم وموضع معروف في ترتيب المصحف.

**الغرض:** نستخدم السورة وحدة رئيسية لتنظيم النص وربط الآيات والبيانات المتعلقة بالسورة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`surah_names`](#surah_names)، [`surah_group`](#surah_group)، [`revelation_classification`](#revelation_classification)، [`basmalah`](#basmalah)، [`ayah_count`](#ayah_count)، [`ayah_key`](#ayah_key)، [`mathani`](#mathani)، [`miun`](#miun)، [`mufassal`](#mufassal)، [`muqatta_letter`](#muqatta_letter)، [`quran`](#quran)، [`quran_merits`](#quran_merits)، [`revelation_order`](#revelation_order)، [`saba_tiwal`](#saba_tiwal)، [`surah_name_reason`](#surah_name_reason)، [`surah_objectives`](#surah_objectives)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="word_key"></a>

### Word Key

<!-- source: standards/terminology/concepts/word_key.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`word_key`</span> |
| `plural` | <span dir="ltr">`word_keys`</span> |
| `kind` | <span dir="ltr">`property`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| تهجئات أخرى | <span dir="ltr">`wid`، `data_wid`، `word_ref`، `word_position_key`</span> |

**التعريف:** مفتاح الكلمة هو معرف نصي للكلمة يضيف إلى مفتاح الآية موضع الكلمة فيها، على صورة `2:255:5`. ويعد موضع الكلمة من أول الآية بحسب منهج تقسيم معلن.

**الغرض:** نستخدم مفتاح الكلمة مفتاحًا للبيانات المرتبطة بالكلمة، مثل التوقيت والترجمة كلمة بكلمة والتحليل الصرفي والصور.

- الموضع في المفتاح هو موضع الكلمة وليس `token`، لذلك تغيير منهج التقسيم الذي يعد الكلمات يغير المفتاح.

**مرتبط به:** <span dir="ltr">[`ayah_key`](#ayah_key)، [`word`](#word)، [`word_timing`](#word_timing)، [`word_by_word_translation`](#word_by_word_translation)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `word_attributes!data-wid`

## النص — `text`

<a id="character"></a>

### Character

<!-- source: standards/terminology/concepts/character.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`character`</span> |
| `plural` | <span dir="ltr">`characters`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** المحرف وحدة نصية مجردة في نظام تمثيل رقمي، ولا يلزم أن يطابق حرفًا لغويًا واحدًا.

**الغرض:** نستخدمه حيث يلزم أن تكون الإزاحة أو الطول أو المقارنة دقيقة، مثل اختبارات مسار النص وفهارس البحث وقائمة المحارف المسموح بها.

- المحرف وحدة ترميز والحرف وحدة لغوية، فقد يُمثل الحرف الواحد بأكثر من محرف.
- المحرف ليس الشكل المرسوم (`glyph`)، فالشكل ينتجه الخط والمحرف يحمله النص.

**مرتبط به:** <span dir="ltr">[`letter`](#letter)، [`glyph`](#glyph)، [`codepoint`](#codepoint)، [`grapheme`](#grapheme)</span>

<a id="codepoint"></a>

### Codepoint

<!-- source: standards/terminology/concepts/codepoint.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`codepoint`</span> |
| `plural` | <span dir="ltr">`codepoints`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** نقطة الترميز قيمة رقمية معرفة في معيار ترميز مثل `Unicode`.

**الغرض:** نستخدمها حين يلزم الترميز الدقيق للمحرف أو العلامة، مثل قواعد التطبيع ومقابلات الخطوط وقائمة النقاط المسموح بها.

**مرتبط به:** <span dir="ltr">[`character`](#character)، [`grapheme`](#grapheme)</span>

<a id="glyph"></a>

### Glyph

<!-- source: standards/terminology/concepts/glyph.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`glyph`</span> |
| `plural` | <span dir="ltr">`glyphs`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** الشكل المرسوم هو الشكل البصري الذي ينتجه الخط لتمثيل حرف أو محرف أو مجموعة منها.

**الغرض:** نستخدمه في الخطوط والرسم والعرض ومواضع الأشكال البصرية.

- الشكل المرسوم ينتجه الخط، وليس هو الحرف ولا المحرف، فالمحرف الواحد قد يُرسم بأشكال مختلفة.

**مرتبط به:** <span dir="ltr">[`character`](#character)، [`letter`](#letter)، [`font`](#font)</span>

<a id="grapheme"></a>

### Grapheme

<!-- source: standards/terminology/concepts/grapheme.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`grapheme`</span> |
| `plural` | <span dir="ltr">`graphemes`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** الوحدة الكتابية وحدة يدركها المستخدم على أنها وحدة واحدة، وقد تتكون من أكثر من `codepoint`.

**الغرض:** نستخدمها في التقسيم البصري والتحرير واختيار النص عندما لا يكون `codepoint` وحدة مناسبة.

**مرتبط به:** <span dir="ltr">[`codepoint`](#codepoint)، [`character`](#character)</span>

<a id="letter"></a>

### الحرف — Letter

<!-- source: standards/terminology/concepts/letter.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`letter`</span> |
| `plural` | <span dir="ltr">`letters`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحَرْف |
| تهجئات أخرى | <span dir="ltr">`harf`</span> |

**التعريف:** الحرف هو الحرف الهجائي بوصفه وحدة لغوية من وحدات الكتابة.

**الغرض:** نستخدمه للبيانات التي تتعامل مع الحروف اللغوية، دون خلط بينها وبين التمثيلات الرقمية أو البصرية.

- الحرف وحدة لغوية والمحرف وحدة ترميز، فالحرف الواحد قد يُكتب بمحرف أو أكثر.
- الحرف وحدة من الكتابة، وحرف المعنى قسم من أقسام الكلمة.

**مرتبط به:** <span dir="ltr">[`character`](#character)، [`glyph`](#glyph)، [`particle`](#particle)، [`ijam`](#ijam)، [`word`](#word)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/5) — `5`

<a id="token"></a>

### Token

<!-- source: standards/terminology/concepts/token.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`token`</span> |
| `plural` | <span dir="ltr">`tokens`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** `token` هو وحدة ينتجها تقسيم النص وفق منهج معلن. وقد تطابق الكلمة، وقد تكون جزءًا منها، وقد تجمع أكثر من كلمة.

**الغرض:** نستخدم `token` لربط التحليل الآلي بالنص حين لا يكون حد الكلمة هو حد التقسيم، وليبقى ما ينتجه المقسم متميزًا عما يعده القارئ كلمة.

- الكلمة وحدة يعرفها القارئ، و`token` وحدة ينتجها منهج تقسيم. لذلك اختلاف المنهج يغير عدد `tokens` ولا يغير عدد الكلمات.

**مرتبط به:** <span dir="ltr">[`word`](#word)، [`morpheme`](#morpheme)</span>

<a id="word"></a>

### الكلمة — Word

<!-- source: standards/terminology/concepts/word.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`word`</span> |
| `plural` | <span dir="ltr">`words`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الكَلِمَة |
| تهجئات أخرى | <span dir="ltr">`kalimah`</span> |

**التعريف:** الكلمة هي وحدة من النص يعرفها القارئ كلمة واحدة، ولا يتغير عدها بتغير منهج تقسيم النص.

**الغرض:** نستخدم الكلمة لربط البيانات على مستوى الكلمة، مثل الجذر والصرف والإعراب والتجويد والمحاذاة الصوتية والموضع البصري.

- الكلمة وحدة يعرفها القارئ، و`token` وحدة ينتجها منهج تقسيم. لذلك اختلاف المنهج يغير عدد `tokens` ولا يغير عدد الكلمات.

**مرتبط به:** <span dir="ltr">[`token`](#token)، [`morpheme`](#morpheme)، [`letter`](#letter)، [`word_key`](#word_key)، [`ayah`](#ayah)، [`irab`](#irab)، [`mutashabihat`](#mutashabihat)، [`word_by_word_translation`](#word_by_word_translation)، [`word_meanings`](#word_meanings)، [`word_timing`](#word_timing)</span>

## أقسام القرآن — `divisions`

<a id="hizb"></a>

### الحزب — Hizb

<!-- source: standards/terminology/concepts/hizb.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hizb`</span> |
| `plural` | <span dir="ltr">`hizbs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحِزْب |
| تهجئات أخرى | <span dir="ltr">`hezb`</span> |

**التعريف:** الحزب في التقسيم المعاصر نصف جزء، فيكون القرآن 60 حزبًا.

**الغرض:** نستخدمه لتمثيل التقسيمات الاصطلاحية والتنقل وخطط القراءة.

**مرتبط به:** <span dir="ltr">[`juz`](#juz)، [`rubu_al_hizb`](#rubu_al_hizb)، [`thumn`](#thumn)، [`division_mark`](#division_mark)</span>

<a id="juz"></a>

### الجزء — Juz

<!-- source: standards/terminology/concepts/juz.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`juz`</span> |
| `plural` | <span dir="ltr">`juzs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الجُزْء |
| تهجئات أخرى | <span dir="ltr">`juzu`، `juz'`، `juzz`، `para`</span> |
| مقابل إنجليزي | <span dir="ltr">`Part`</span> |

**التعريف:** الجزء واحد من 30 قسمًا في التقسيم المشهور للمصحف، والغرض من هذا التقسيم تيسير القراءة والختم.

**الغرض:** نستخدمه للتنقل وتنظيم القراءة والجداول والخطط المرتبطة بأجزاء القرآن.

**مرتبط به:** <span dir="ltr">[`hizb`](#hizb)، [`manzil`](#manzil)، [`khatmah`](#khatmah)، [`division_mark`](#division_mark)، [`ruku`](#ruku)</span>

<a id="manzil"></a>

### المنزل — Manzil

<!-- source: standards/terminology/concepts/manzil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`manzil`</span> |
| `plural` | <span dir="ltr">`manzils`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَنْزِل |

**التعريف:** المنزل واحد من 7 أقسام تقليدية للقرآن، والغرض من هذا التقسيم تيسير ختمه في أسبوع.

**الغرض:** نستخدمه في التطبيقات التي تدعم نظام المنازل وخطط القراءة المبنية عليه.

**مرتبط به:** <span dir="ltr">[`juz`](#juz)، [`khatmah`](#khatmah)</span>

<a id="rubu_al_hizb"></a>

### ربع الحزب — Rubu al-Hizb

<!-- source: standards/terminology/concepts/rubu_al_hizb.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rubu_al_hizb`</span> |
| `plural` | <span dir="ltr">`rubu_al_hizbs`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| جزء من | <span dir="ltr">[`hizb`](#hizb)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | رُبْع الحِزْب |
| تهجئات أخرى | <span dir="ltr">`rub_al_hizb`، `rub'_al-hizb`، `rub_el_hizb`، `rub`، `rubu`، `rub_hizb`، `hizb_quarter`، `quarter_hizb`</span> |

**التعريف:** ربع الحزب هو الجزء الرابع من الحزب في التقسيم المشهور للمصحف.

**الغرض:** نستخدم ربع الحزب لتمثيل التقسيم الأدق للحزب ومواضع علاماته في المصحف.

**مرتبط به:** <span dir="ltr">[`hizb`](#hizb)، [`thumn`](#thumn)، [`division_mark`](#division_mark)</span>

<a id="ruku"></a>

### الركوع — Ruku

<!-- source: standards/terminology/concepts/ruku.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ruku`</span> |
| `plural` | <span dir="ltr">`rukus`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرُّكُوع |
| تهجئات أخرى | <span dir="ltr">`ruku'`، `rukūʿ`</span> |

**التعريف:** الركوع هو قسم اصطلاحي من القرآن يستخدم لتنظيم القراءة ويظهر في بعض المصاحف.

**الغرض:** نستخدم الركوع في التطبيقات والمصاحف التي تعتمد تقسيم الركوع.

**مرتبط به:** <span dir="ltr">[`juz`](#juz)، [`mushaf_edition`](#mushaf_edition)</span>

<a id="thumn"></a>

### الثمن — Thumn

<!-- source: standards/terminology/concepts/thumn.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`thumn`</span> |
| `plural` | <span dir="ltr">`thumns`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| جزء من | <span dir="ltr">[`hizb`](#hizb)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الثُّمْن |
| تهجئات أخرى | <span dir="ltr">`thumun`</span> |

**التعريف:** الثمن هو الجزء الثامن من الحزب، وهو تقسيم مستخدم في بعض المصاحف والمدارس.

**الغرض:** نستخدم الثمن عند دعم مصادر أو مصاحف تعتمد تقسيم الحزب إلى أثمان.

**مرتبط به:** <span dir="ltr">[`hizb`](#hizb)، [`rubu_al_hizb`](#rubu_al_hizb)</span>

## تصنيف السور — `surah_classification`

<a id="mathani"></a>

### المثاني — Mathani

<!-- source: standards/terminology/concepts/mathani.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mathani`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`surah_group`](#surah_group)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَثَانِي |

**التعريف:** المثاني هي السور التي تقل آياتها عن المئين وتليها في التقسيم التقليدي، وسميت مثاني لكثرة ما تُثنى، أي تتكرر قراءتها.

**الغرض:** نستخدمها قيمة من قيم تصنيف السور، فنربط بها خطط القراءة وكتب التفسير التي تعالج المجموعة وحدة واحدة.

> لا يعين المعيار أعضاء المجموعة سورة سورة، لأن المصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا يوجد بعد سجل يحصر أعضاء كل مجموعة مع مصدره.

**مرتبط به:** <span dir="ltr">[`surah_group`](#surah_group)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="miun"></a>

### المئون — Miun

<!-- source: standards/terminology/concepts/miun.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`miun`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`surah_group`](#surah_group)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المِئُون |
| مقابل إنجليزي | <span dir="ltr">`Hundred-Verse Surahs`</span> |

**التعريف:** المئون هي السور التي تقارب آياتها المئة أو تزيد عليها أو تنقص عنها قليلًا.

**الغرض:** نستخدمها قيمة من قيم تصنيف السور، فنربط بها خطط القراءة وكتب التفسير التي تعالج المجموعة وحدة واحدة.

> لا يعين المعيار أعضاء المجموعة سورة سورة، لأن المصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا يوجد بعد سجل يحصر أعضاء كل مجموعة مع مصدره.

**مرتبط به:** <span dir="ltr">[`surah_group`](#surah_group)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="mufassal"></a>

### المفصل — Mufassal

<!-- source: standards/terminology/concepts/mufassal.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mufassal`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`surah_group`](#surah_group)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُفَصَّل |

**التعريف:** المفصل مجموعة من قصار السور التي تلي المثاني، ويختلف العلماء في أولها.

**الغرض:** نستخدمها قيمة من قيم تصنيف السور، فنربط بها خطط القراءة وكتب التفسير التي تعالج المجموعة وحدة واحدة.

> لا يعين المعيار أعضاء المجموعة سورة سورة، لأن المصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا يوجد بعد سجل يحصر أعضاء كل مجموعة مع مصدره.

**مرتبط به:** <span dir="ltr">[`surah_group`](#surah_group)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/221`

<a id="saba_tiwal"></a>

### السبع الطوال — Saba Tiwal

<!-- source: standards/terminology/concepts/saba_tiwal.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`saba_tiwal`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`surah_group`](#surah_group)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السَّبْع الطِّوَال |
| تهجئات أخرى | <span dir="ltr">`sab_tiwal`</span> |
| مقابل إنجليزي | <span dir="ltr">`Seven Long Surahs`</span> |

**التعريف:** السبع الطوال هي مجموعة من أطول سور القرآن في أوله، مع خلاف معروف في تعيين السورة السابعة.

**الغرض:** نستخدم السبع الطوال قيمة من قيم تصنيف السور. ونربط بها خطط القراءة وكتب التفسير التي تعالج المجموعة وحدة واحدة.

> لا يعين المعيار أعضاء المجموعة سورة سورة، لأن المصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا يوجد بعد سجل يحصر أعضاء كل مجموعة مع مصدره.

**مرتبط به:** <span dir="ltr">[`surah_group`](#surah_group)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`

<a id="surah_group"></a>

### تصنيف السور — Surah Group

<!-- source: standards/terminology/concepts/surah_group.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`surah_group`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`mathani`](#mathani)، [`miun`](#miun)، [`mufassal`](#mufassal)، [`saba_tiwal`](#saba_tiwal)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَصْنِيف السُّوَر |

**التعريف:** تصنيف السور هو تصنيف يجمع سورًا وفق تقسيمات اصطلاحية موروثة تعتمد الطول أو موضع السورة ضمن مجموعات السور.

**الغرض:** يوفر تصنيف السور أبًا موحدًا لتصنيفات مثل الطوال والمئين والمثاني والمفصل.

**مرتبط به:** <span dir="ltr">[`saba_tiwal`](#saba_tiwal)، [`miun`](#miun)، [`mathani`](#mathani)، [`mufassal`](#mufassal)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/221`

## المصحف والتخطيط — `mushaf`

<a id="ayah_fragment"></a>

### مقطع الآية — Ayah Fragment

<!-- source: standards/terminology/concepts/ayah_fragment.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_fragment`</span> |
| `plural` | <span dir="ltr">`ayah_fragments`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَقْطَع الآيَة |
| الجمع | مقاطع الآيات |
| تهجئات أخرى | <span dir="ltr">`ayah_segment`، `ayah_part`، `line_ayah`، `g_ayah`</span> |
| مقابل إنجليزي | <span dir="ltr">`ayah fragment`</span> |

**التعريف:** مقطع الآية هو ما يظهر من آية واحدة في سطر واحد من صفحة مصحف بعينه. والآية التي تمتد على سطرين تتكون من مقطعين.

**الغرض:** نستخدمه وحدة للعرض والوسم في تخطيط الصفحة، لأن الآية قد لا تنتهي مع نهاية السطر والسطر قد لا ينتهي مع نهاية الآية. وعليه نبني المحاذاة والإبراز في المصحف المرسوم.

- المقطع صفة في تخطيط مصحف بعينه، وليس جزءًا من هوية الآية.
- المقطع ليس الكلمة، فقد يكون كلمة أو كلمات أو جزءًا من كلمة إذا وقع القطع داخلها.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`line`](#line)، [`page`](#page)، [`layout`](#layout)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `glossary!g.ayah`

<a id="font"></a>

### الخط — Font

<!-- source: standards/terminology/concepts/font.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`font`</span> |
| `plural` | <span dir="ltr">`fonts`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الخَطّ |

**التعريف:** الخط ملف يحمل مجموعة من الأشكال المرسومة (`glyphs`) وقواعد إخراجها، ويُعرض به نص المصحف.

**الغرض:** نستخدمه لتسجيل الخط الذي يعتمد عليه المصحف الرقمي، لأن كثيرًا من المصاحف لا يُعرض نصها عرضًا صحيحًا إلا بخط بعينه. وترتبط بالخط ترميز الحروف وأشكالها ومواضع الأسطر.

- الخط وسيلة عرض، والرسم صفة للنص المكتوب نفسه.
- الشكل المرسوم (`glyph`) شكل داخل الخط، والحرف وحدة من النص.

**مرتبط به:** <span dir="ltr">[`glyph`](#glyph)، [`rasm`](#rasm)، [`layout`](#layout)، [`line`](#line)، [`mushaf_edition`](#mushaf_edition)</span>

<a id="layout"></a>

### التخطيط — Layout

<!-- source: standards/terminology/concepts/layout.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`layout`</span> |
| `plural` | <span dir="ltr">`layouts`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّخْطِيط |

**التعريف:** التخطيط تنظيم النص والعناصر بصريًا في صفحات وأسطر ومواضع داخل مصحف أو عرض معين.

**الغرض:** نستخدمه لفصل البيانات البصرية عن بنية القرآن النصية الثابتة.

**مرتبط به:** <span dir="ltr">[`mushaf_edition`](#mushaf_edition)، [`page`](#page)، [`line`](#line)، [`font`](#font)، [`ayah_fragment`](#ayah_fragment)، [`mushaf`](#mushaf)</span>

<a id="line"></a>

### السطر — Line

<!-- source: standards/terminology/concepts/line.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`line`</span> |
| `plural` | <span dir="ltr">`lines`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السَّطْر |

**التعريف:** السطر هو السطر الطباعي داخل صفحة مصحف أو تخطيط معين.

**الغرض:** نستخدمه لتمثيل مواقع النص والأشكال داخل التخطيط الطباعي.

**مرتبط به:** <span dir="ltr">[`page`](#page)، [`layout`](#layout)، [`ayah_fragment`](#ayah_fragment)، [`font`](#font)</span>

<a id="page"></a>

### الصفحة — Page

<!-- source: standards/terminology/concepts/page.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`page`</span> |
| `plural` | <span dir="ltr">`pages`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الصَّفْحَة |
| تهجئات أخرى | <span dir="ltr">`safhah`</span> |

**التعريف:** الصفحة هي وحدة طباعية من تخطيط مصحف معين، وقد يختلف محتواها وحدودها باختلاف المصحف أو الطبعة.

**الغرض:** نستخدم الصفحة في العرض والتنقل والمحاذاة البصرية بحسب صفحات مصحف معين.

**مرتبط به:** <span dir="ltr">[`mushaf_edition`](#mushaf_edition)، [`layout`](#layout)، [`line`](#line)، [`ayah_fragment`](#ayah_fragment)، [`mushaf`](#mushaf)</span>

<a id="rasm"></a>

### الرسم — Rasm

<!-- source: standards/terminology/concepts/rasm.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rasm`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`rasm_imlai`](#rasm_imlai)، [`rasm_uthmani`](#rasm_uthmani)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرَّسْم |
| تهجئات أخرى | <span dir="ltr">`rasm_type`</span> |
| مقابل إنجليزي | <span dir="ltr">`orthography`</span> |

**التعريف:** الرسم هو طريقة كتابة ألفاظ القرآن من حيث إثبات الحروف وحذفها وزيادتها وفصلها ووصلها وما يشبه ذلك.

**الغرض:** نستخدم الرسم تصنيفًا يبين على أي رسم كتب النص أو المصحف أو `dataset`. ويبنى عليه البحث والمقارنة والعرض، ويميز طبقة الرسم عن الخط والتخطيط والمحارف المرسومة.

- الرسم هو إثبات الحروف وحذفها وفصلها ووصلها، أما الضبط فهو علامات النطق التي توضع على الحروف.
- الخط هو صورة الحروف في مصحف بعينه، أما الرسم فهو ما يثبت في كل مصحف كتب به.

**مرتبط به:** <span dir="ltr">[`rasm_uthmani`](#rasm_uthmani)، [`rasm_imlai`](#rasm_imlai)، [`mushaf_mark`](#mushaf_mark)، [`font`](#font)، [`mushaf`](#mushaf)، [`mushaf_edition`](#mushaf_edition)، [`omitted_alif`](#omitted_alif)، [`orthographic_mark`](#orthographic_mark)، [`tashkil`](#tashkil)</span>

<a id="rasm_imlai"></a>

### الرسم الإملائي — Rasm Imlai

<!-- source: standards/terminology/concepts/rasm_imlai.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rasm_imlai`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`rasm`](#rasm)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرَّسْم الإِمْلَائِيّ |
| تهجئات أخرى | <span dir="ltr">`imlaei`، `imlai`، `imla'i`، `imlaai`، `simple`، `text_simple`، `text_imlaei`، `rasm_imlaei`</span> |
| مقابل إنجليزي | <span dir="ltr">`modern orthography`، `standard orthography`</span> |

**التعريف:** الرسم الإملائي هو كتابة ألفاظ القرآن على قواعد الإملاء المعاصرة، بإثبات ما يحذف في الرسم العثماني وحذف ما يزاد فيه، حتى تقرأ الكلمة على صورتها المألوفة.

**الغرض:** نستخدم الرسم الإملائي لتحديد أن النص يتبع الإملاء المعاصر. وهذا هو النص الذي تبنى عليه صيغة البحث والاقتباس والعرض خارج المصحف، مقابل النص العثماني الذي يعرض به المصحف.

- الرسم الإملائي يخص الكتابة وليس القراءة، فاللفظ واحد والذي يختلف هو صورة الكلمة.
- النص الإملائي غير نص البحث المجرد من الضبط، حتى لو اشتق الثاني من الأول.

> اشتقاق الاسم بالأداة يعطي `orthographic_rasm`، لأن جدول الكلمات العامة يترجم «إملائي» إلى `orthographic` من أجل «العلامة الإملائية». والاسم المثبت هو `rasm_imlai` لأنه الاسم الذي تستعمله قواعد البيانات والواجهات، والقرار مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`rasm`](#rasm)، [`rasm_uthmani`](#rasm_uthmani)</span>

<a id="rasm_uthmani"></a>

### الرسم العثماني — Rasm Uthmani

<!-- source: standards/terminology/concepts/rasm_uthmani.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rasm_uthmani`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`rasm`](#rasm)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرَّسْم العُثْمَانِيّ |
| تهجئات أخرى | <span dir="ltr">`uthmani`، `uthmanic`، `othmani`، `rasm_othmani`</span> |
| مقابل إنجليزي | <span dir="ltr">`Uthmanic Orthography`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: rasm uthmani 100 vs uthmani rasm 65. The Arabic word order wins in English writing, and it matches the code.</span> |

**التعريف:** الرسم العثماني هو طريقة كتابة كلمات المصاحف العثمانية وما يتعلق بها من حذف وزيادة وبدل وفصل ووصل.

**الغرض:** نستخدم الرسم العثماني لتحديد أن النص يتبع قواعد الرسم العثماني وليس نظامًا إملائيًا آخر.

**مرتبط به:** <span dir="ltr">[`rasm`](#rasm)، [`rasm_imlai`](#rasm_imlai)، [`mushaf`](#mushaf)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/146`

## الضبط وعلامات المصحف — `dabt`

<a id="ayah_mark"></a>

### علامة الآية — Ayah Mark

<!-- source: standards/terminology/concepts/ayah_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_mark`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة الآيَة |
| اسمه في الضبط | عَلَامَة رَأْس الآيَة |
| اسمه بشكله | دَارَة |
| اسمه في تعريف المصحف | عَلَامَة رَأْس الآيَة |
| الرمز | ۝ |
| المحارف | <span dir="ltr">`U+06DD` ARABIC END OF AYAH</span> |
| عائلة العلامة | <span dir="ltr">`mustaqill`</span> |
| تهجئات أخرى | <span dir="ltr">`end_of_ayah`، `ayah_marker`، `ayah_separator`</span> |

**التعريف:** علامة الآية هي الدارة الفاصلة بين الآيتين، وتوضع عند نهاية الآية ويكتب فيها رقمها في أكثر المصاحف.

**الغرض:** نستخدمها لتحديد حدود الآية في النص المكتوب، فيعرف منها المحلل والعارض أين تنتهي الآية وما رقمها.

- العلامة رسم في المصحف، أما الفاصلة فهي خاتمة الآية من جهة النظم.
- رقم الآية داخل الدارة يتبع نظام عد الآي، ولا يعد جزءًا من العلامة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`ayah_ending`](#ayah_ending)، [`ayah_numbering_system`](#ayah_numbering_system)</span>

<a id="dammah"></a>

### الضمة — Dammah

<!-- source: standards/terminology/concepts/dammah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`dammah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`harakah`](#harakah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الضَّمَّة |
| اسمه في الضبط | الضَّمَّة (وتُسمَّى قديمًا الرَّفْعَة) |
| اسمه بشكله | وَاو صَغِيرَة فَوْق الحَرْف |
| الرمز | ـُ |
| المحارف | <span dir="ltr">`U+064F` ARABIC DAMMA</span> |
| عائلة العلامة | <span dir="ltr">`harakah`</span> |
| تهجئات أخرى | <span dir="ltr">`damma`</span> |

**التعريف:** الضمة علامة تدل على حركة الحرف بالضم.

**الغرض:** نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم بدلًا من قراءة صورة الشكل.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!damma`

<a id="division_mark"></a>

### علامة التقسيم — Division Mark

<!-- source: standards/terminology/concepts/division_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`division_mark`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة التَّقْسِيم |
| اسمه في الضبط | عَلَامَة التَّحْزِيب |
| اسمه بشكله | نَجْمَة مُثَمَّنَة |
| اسمه في تعريف المصحف | عَلَامَة بِدَايَة الأَجْزَاء والأَحْزَاب وأَنْصَافِها وأَرْبَاعِها |
| الرمز | نَجْمَة |
| المحارف | <span dir="ltr">`U+06DE` ARABIC START OF RUB EL HIZB</span> |
| عائلة العلامة | <span dir="ltr">`mustaqill`</span> |
| تهجئات أخرى | <span dir="ltr">`hizb_mark`، `juz_mark`، `rub_el_hizb_mark`، `rub_mark`</span> |
| أسماء متروكة | <span dir="ltr">`alamat_al_tahzib`</span> |

**التعريف:** علامة التقسيم علامة تدل على بداية الأجزاء والأحزاب وأنصافها وأرباعها.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

- علامة التقسيم رسم في المصحف، والجزء والحزب وأرباعه أقسام من النص تدل عليها.

> كان `alamat_al_tahzib` مدخلًا مستقلًا يعرف الشيء نفسه، ثم دُمج في هذا المدخل.

**مرتبط به:** <span dir="ltr">[`hizb`](#hizb)، [`rubu_al_hizb`](#rubu_al_hizb)، [`juz`](#juz)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!hizb`

<a id="dot"></a>

### النقطة — Dot

<!-- source: standards/terminology/concepts/dot.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`dot`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`ijam`](#ijam)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّقْطَة |
| اسمه في الضبط | نَقْط الإِعْجَام — النُّقْطَة |
| اسمه بشكله | نُقْطَة وَاحِدَة |
| الرمز | نُقْطَة وَاحِدَة |
| عائلة العلامة | <span dir="ltr">`ijam`</span> |
| تهجئات أخرى | <span dir="ltr">`nuqtah`</span> |

**التعريف:** النقطة نقطة واحدة فوق الحرف أو تحته تميزه عن الحرف الذي يشاركه في الرسم، مثل الباء والنون والجيم والخاء والذال.

**الغرض:** نستخدمها قيمة من قيم النقط، فنميز بها الحرف عن الحرف الذي يشاركه في الرسم في التحليل والبحث.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!dot`

<a id="fathah"></a>

### الفتحة — Fathah

<!-- source: standards/terminology/concepts/fathah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`fathah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`harakah`](#harakah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفَتْحَة |
| اسمه في الضبط | الفَتْحَة (وتُسمَّى قديمًا النَّصْبَة) |
| اسمه بشكله | أَلِف مُضْجَعَة فَوْق الحَرْف |
| الرمز | ـَ |
| المحارف | <span dir="ltr">`U+064E` ARABIC FATHA</span> |
| عائلة العلامة | <span dir="ltr">`harakah`</span> |
| تهجئات أخرى | <span dir="ltr">`fatha`</span> |

**التعريف:** الفتحة علامة تدل على حركة الحرف بالفتح.

**الغرض:** نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم بدلًا من قراءة صورة الشكل.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!fatha`

<a id="hamzah"></a>

### الهمزة — Hamzah

<!-- source: standards/terminology/concepts/hamzah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hamzah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الهَمْزَة |
| اسمه في الضبط | الهَمْزَة — رَأْس العَيْن |
| اسمه بشكله | رَأْس عَيْن |
| الرمز | ء |
| المحارف | <span dir="ltr">`U+0621` ARABIC LETTER HAMZA، `U+0654` ARABIC HAMZA ABOVE، `U+0655` ARABIC HAMZA BELOW</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`hamza`</span> |

**التعريف:** الهمزة علامة تدل على همزة القطع المحققة.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`hamzat_al_wasl`](#hamzat_al_wasl)، [`madd_al_badal`](#madd_al_badal)، [`madd_munfasil`](#madd_munfasil)، [`madd_muttasil`](#madd_muttasil)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!hamza`

<a id="hamzat_al_wasl"></a>

### همزة الوصل — Hamzat al-Wasl

<!-- source: standards/terminology/concepts/hamzat_al_wasl.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hamzat_al_wasl`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | هَمْزَة الوَصْل |
| اسمه في الضبط | رَأْس الصَّاد (من «صِلَة») — عَلَامَة هَمْزَة الوَصْل |
| اسمه بشكله | رَأْس صَاد فَوْق الأَلِف |
| اسمه في تعريف المصحف | رَأْس صَاد صَغِيرَة فَوْق أَلِف الوَصْل |
| الرمز | ص صَغِيرَة فَوْق الأَلِف |
| المحارف | <span dir="ltr">`U+0671` ARABIC LETTER ALEF WASLA</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`alif_wasl`، `hamzat_wasl`، `wasl`، `wasla`</span> |

**التعريف:** همزة الوصل علامة تدل على سقوط الهمزة في الوصل.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`hamzah`](#hamzah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!wasla`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/127) — `127`

<a id="harakah"></a>

### الحركة — Harakah

<!-- source: standards/terminology/concepts/harakah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`harakah`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| القيم | <span dir="ltr">[`dammah`](#dammah)، [`fathah`](#fathah)، [`kasrah`](#kasrah)، [`shaddah`](#shaddah)، [`sukun`](#sukun)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحَرَكَة |
| تهجئات أخرى | <span dir="ltr">`haraka`، `harakat`</span> |
| مقابل إنجليزي | <span dir="ltr">`Vowel Mark`، `diacritics`</span> |

**التعريف:** الحركة علامة تضبط حركة الحرف أو سكونه أو تشديده، وهي الفتحة والضمة والكسرة والسكون والشدة.

**الغرض:** نستخدمها أبًا لعلامات الضبط التي تحدد نطق الحرف نفسه.

**مرتبط به:** <span dir="ltr">[`mushaf_mark`](#mushaf_mark)، [`tanwin`](#tanwin)، [`tashkil`](#tashkil)، [`shaddah`](#shaddah)، [`sukun`](#sukun)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/151`

<a id="ijam"></a>

### الإعجام — Ijam

<!-- source: standards/terminology/concepts/ijam.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ijam`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| القيم | <span dir="ltr">[`dot`](#dot)، [`three_dots`](#three_dots)، [`two_dots`](#two_dots)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِعْجَام |

**التعريف:** الإعجام هو النقط الذي يميز الحرف عن الحروف التي تشاركه في صورة الرسم.

**الغرض:** نستخدمه أصلًا تندرج تحته صور النقط، وما يميز هذه الصور هو عدد النقط وموضعها وليس وظيفتها.

**مرتبط به:** <span dir="ltr">[`mushaf_mark`](#mushaf_mark)، [`letter`](#letter)، [`tashkil`](#tashkil)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/151`

<a id="imalah"></a>

### الإمالة — Imalah

<!-- source: standards/terminology/concepts/imalah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`imalah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`qiraah_mark`](#qiraah_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِمَالَة |
| اسمه في الضبط | الإِمَالَة — النُّقْطَة تَحْت الحَرْف |
| اسمه بشكله | نُقْطَة كَبِيرَة مَطْمُوسَة تَحْت الحَرْف |
| اسمه في تعريف المصحف | نُقْطَة كَبِيرَة مَطْمُوسَة الوَسَط تَحْت الحَرْف |
| الرمز | نُقْطَة تَحْت الحَرْف |
| المحارف | <span dir="ltr">`U+06EA` ARABIC EMPTY CENTRE LOW STOP</span> |
| عائلة العلامة | <span dir="ltr">`alamat_qiraah`</span> |

**التعريف:** علامة الإمالة تدل على الإمالة الكبرى، وهي نطق الفتحة مائلة إلى الكسرة، وترد في رواية حفص في موضع واحد (11:41).

**الغرض:** نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!imalah`

<a id="ishmam"></a>

### الإشمام — Ishmam

<!-- source: standards/terminology/concepts/ishmam.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ishmam`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`qiraah_mark`](#qiraah_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِشْمَام |
| اسمه في الضبط | الإِشْمَام |
| اسمه بشكله | نُقْطَة كَبِيرَة مَطْمُوسَة فَوْق الحَرْف |
| اسمه في تعريف المصحف | النُّقْطَة المَذْكُورَة فَوْق آخِر المِيم |
| الرمز | نُقْطَة فَوْق الحَرْف |
| المحارف | <span dir="ltr">`U+06EC` ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE</span> |
| عائلة العلامة | <span dir="ltr">`alamat_qiraah`</span> |

**التعريف:** علامة الإشمام تدل على الإشمام، وهو ضم الشفتين إشارة إلى الضمة المحذوفة من غير صوت.

**الغرض:** نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!ishmam`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/131) — `131`

<a id="kasrah"></a>

### الكسرة — Kasrah

<!-- source: standards/terminology/concepts/kasrah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`kasrah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`harakah`](#harakah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الكَسْرَة |
| اسمه في الضبط | الكَسْرَة (وتُسمَّى قديمًا الخَفْضَة) |
| اسمه بشكله | أَلِف مُضْجَعَة تَحْت الحَرْف |
| الرمز | ـِ |
| المحارف | <span dir="ltr">`U+0650` ARABIC KASRA</span> |
| عائلة العلامة | <span dir="ltr">`harakah`</span> |
| تهجئات أخرى | <span dir="ltr">`kasra`</span> |

**التعريف:** الكسرة علامة تدل على حركة الحرف بالكسر.

**الغرض:** نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم بدلًا من قراءة صورة الشكل.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!kasra`

<a id="maddah"></a>

### المدة — Maddah

<!-- source: standards/terminology/concepts/maddah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`maddah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدَّة |
| اسمه في الضبط | عَلَامَة المَدّ — المَدَّة |
| اسمه بشكله | خَطّ مُتَمَوِّج مَمْدُود فَوْق الحَرْف |
| اسمه في تعريف المصحف | عَلَامَة المَدّ |
| الرمز | خَطّ المَدّ |
| المحارف | <span dir="ltr">`U+0653` ARABIC MADDAH ABOVE، `U+06E4` ARABIC SMALL HIGH MADDA</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`madda`</span> |

**التعريف:** المدة علامة تدل على لزوم مد الحرف مدًّا زائدًا على المد الطبيعي.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!maddah`

<a id="mushaf_mark"></a>

### علامة المصحف — Mushaf Mark

<!-- source: standards/terminology/concepts/mushaf_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mushaf_mark`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`ayah_mark`](#ayah_mark)، [`division_mark`](#division_mark)، [`harakah`](#harakah)، [`ijam`](#ijam)، [`orthographic_mark`](#orthographic_mark)، [`qiraah_mark`](#qiraah_mark)، [`rectangular_zero`](#rectangular_zero)، [`rounded_zero`](#rounded_zero)، [`sajdah_line`](#sajdah_line)، [`sajdah_mark`](#sajdah_mark)، [`small_meem`](#small_meem)، [`tanwin`](#tanwin)، [`waqf_mark`](#waqf_mark)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة المُصْحَف |

**التعريف:** علامة المصحف رمز أو علامة غير داخلة في الحروف الأصلية للكلمة، وتستخدم في المصحف لأغراض القراءة أو التنظيم أو الإرشاد.

**الغرض:** نستخدمها أبًا موحدًا للعلامات المختلفة بدلًا من معاملتها أنواعًا غير مرتبطة.

**مرتبط به:** <span dir="ltr">[`harakah`](#harakah)، [`tanwin`](#tanwin)، [`ijam`](#ijam)، [`orthographic_mark`](#orthographic_mark)، [`qiraah_mark`](#qiraah_mark)، [`waqf_mark`](#waqf_mark)، [`rasm`](#rasm)، [`tashkil`](#tashkil)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="omitted_alif"></a>

### الألف المحذوفة — Omitted Alif

<!-- source: standards/terminology/concepts/omitted_alif.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`omitted_alif`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الأَلِف المَحْذُوفَة |
| اسمه في الضبط | الأَلِف المَحْذُوفَة — أَلِف صَغِيرَة قَائِمَة |
| اسمه بشكله | أَلِف صَغِيرَة قَائِمَة فَوْق الحَرْف |
| اسمه في تعريف المصحف | مِنَ الحُرُوف الصَّغِيرَة الدَّالَّة على المَتْرُوك مِنَ الرَّسْم |
| الرمز | ا صَغِيرَة قَائِمَة |
| المحارف | <span dir="ltr">`U+0670` ARABIC LETTER SUPERSCRIPT ALEF</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`alif_mahdhufah`، `dagger_alif`، `small-alef`، `small_alef`، `small_alif`، `superscript_alif`</span> |

**التعريف:** الألف المحذوفة علامة تدل على ألف محذوفة من الرسم واجبة النطق.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`rasm`](#rasm)، [`orthographic_mark`](#orthographic_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!small-alef`

<a id="orthographic_mark"></a>

### العلامة الإملائية — Orthographic Mark

<!-- source: standards/terminology/concepts/orthographic_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`orthographic_mark`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| القيم | <span dir="ltr">[`hamzah`](#hamzah)، [`hamzat_al_wasl`](#hamzat_al_wasl)، [`maddah`](#maddah)، [`omitted_alif`](#omitted_alif)، [`small_noon`](#small_noon)، [`small_waw`](#small_waw)، [`small_yaa`](#small_yaa)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَلَامَة الإِمْلَائِيَّة |

**التعريف:** العلامة الإملائية هي علامة تضبط رسم الكلمة، مثل الهمزة والمدة والحروف الصغيرة.

**الغرض:** نستخدم العلامة الإملائية أبًا للعلامات التي تتعلق برسم الكلمة وليس بحركتها ولا بالوقف عليها.

**مرتبط به:** <span dir="ltr">[`mushaf_mark`](#mushaf_mark)، [`rasm`](#rasm)، [`omitted_alif`](#omitted_alif)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/134) — `134`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="qiraah_mark"></a>

### علامة القراءة — Qiraah Mark

<!-- source: standards/terminology/concepts/qiraah_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`qiraah_mark`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| القيم | <span dir="ltr">[`imalah`](#imalah)، [`ishmam`](#ishmam)، [`saktah_mark`](#saktah_mark)، [`seen_al_qiraah`](#seen_al_qiraah)، [`tashil`](#tashil)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة القِرَاءَة |

**التعريف:** علامة القراءة هي علامة ترشد إلى وجه من وجوه الأداء في موضعها، مثل السكت والإشمام والتسهيل.

**الغرض:** نستخدم علامة القراءة أبًا للعلامات التي تنبه القارئ إلى أداء خاص وليس إلى ضبط الحرف.

**مرتبط به:** <span dir="ltr">[`mushaf_mark`](#mushaf_mark)، [`qiraah`](#qiraah)، [`saktah_mark`](#saktah_mark)</span>

<a id="rectangular_zero"></a>

### الصفر المستطيل — Rectangular Zero

<!-- source: standards/terminology/concepts/rectangular_zero.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rectangular_zero`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الصِّفْر المُسْتَطِيل |
| اسمه في الضبط | الصِّفْر المُسْتَطِيل القَائِم |
| اسمه بشكله | مُسْتَطِيل صَغِير قَائِم خَالِي الوَسَط |
| اسمه في تعريف المصحف | دَائِرَة قَائِمَة مُسْتَطِيلَة خَالِيَة الوَسَط |
| الرمز | مُسْتَطِيل قَائِم صَغِير |
| المحارف | <span dir="ltr">`U+06E0` ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO</span> |
| عائلة العلامة | <span dir="ltr">`dabt`</span> |
| تهجئات أخرى | <span dir="ltr">`sifr-mustatil`، `sifr_mustatil`</span> |

**التعريف:** الصفر المستطيل علامة تدل على زيادة الألف في الوصل دون الوقف، ولذلك تنطق عند الوقف عليها.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!sifr-mustatil`

<a id="rounded_zero"></a>

### الصفر المستدير — Rounded Zero

<!-- source: standards/terminology/concepts/rounded_zero.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rounded_zero`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الصِّفْر المُسْتَدِير |
| اسمه في الضبط | الصِّفْر المُسْتَدِير |
| اسمه بشكله | دَائِرَة صَغِيرَة خَالِيَة الوَسَط |
| اسمه في تعريف المصحف | دَائِرَة صَغِيرَة خَالِيَة الوَسَط |
| الرمز | دَائِرَة صَغِيرَة |
| المحارف | <span dir="ltr">`U+06DF` ARABIC SMALL HIGH ROUNDED ZERO</span> |
| عائلة العلامة | <span dir="ltr">`dabt`</span> |
| تهجئات أخرى | <span dir="ltr">`sifr-mustadir`، `sifr_mustadir`</span> |

**التعريف:** الصفر المستدير علامة تدل على زيادة الحرف في الرسم، ولذلك لا ينطق في الوصل ولا في الوقف.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!sifr-mustadir`

<a id="sajdah_line"></a>

### خط السجدة — Sajdah Line

<!-- source: standards/terminology/concepts/sajdah_line.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sajdah_line`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | خَطّ السَّجْدَة |
| اسمه في الضبط | خَطّ مُوجِب السَّجْدَة |
| اسمه بشكله | خَطّ أُفُقِيّ فَوْق الكَلِمَة |
| اسمه في تعريف المصحف | خَطّ أُفُقِيّ فَوْق الكَلِمَة الدَّالّ على مُوجِب السَّجْدَة |
| الرمز | خَطّ أُفُقِيّ |
| عائلة العلامة | <span dir="ltr">`mustaqill`</span> |
| تهجئات أخرى | <span dir="ltr">`khatt_mujib_al_sajdah`، `sajdah-line`</span> |

**التعريف:** خط السجدة خط فوق الكلمة يدل على أنها الكلمة الموجبة للسجدة.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

**مرتبط به:** <span dir="ltr">[`sajdah_mark`](#sajdah_mark)، [`sajdah`](#sajdah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!sajdah-line`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="sajdah_mark"></a>

### علامة السجدة — Sajdah Mark

<!-- source: standards/terminology/concepts/sajdah_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sajdah_mark`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة السَّجْدَة |
| اسمه في الضبط | عَلَامَة مَوْضِع السَّجْدَة — المِحْرَاب |
| اسمه بشكله | مِحْرَاب صَغِير |
| اسمه في تعريف المصحف | عَلَامَة مَوْضِع السَّجْدَة |
| الرمز | مِحْرَاب |
| عائلة العلامة | <span dir="ltr">`mustaqill`</span> |
| تهجئات أخرى | <span dir="ltr">`sajda_mark`، `sajda_sign`، `sajdah-sign`، `sajdah_sign`</span> |
| أسماء متروكة | <span dir="ltr">`alamat_mawdi_al_sajdah`</span> |

**التعريف:** علامة السجدة علامة تدل على موضع السجود.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

- علامة السجدة رسم في المصحف، والسجدة موضع من النص يسجد عنده.

> كان `alamat_mawdi_al_sajdah` مدخلًا مستقلًا يعرف الشيء نفسه، ثم دُمج في هذا المدخل.

**مرتبط به:** <span dir="ltr">[`sajdah`](#sajdah)، [`sajdah_line`](#sajdah_line)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!sajdah-sign`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="saktah_mark"></a>

### علامة السكتة — Saktah Mark

<!-- source: standards/terminology/concepts/saktah_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`saktah_mark`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`qiraah_mark`](#qiraah_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة السَّكْتَة |
| اسمه في الضبط | السِّين — عَلَامَة السَّكْت |
| اسمه بشكله | سِين |
| اسمه في تعريف المصحف | السِّين فَوْق الحَرْف الأَخِير الدَّالَّة على السَّكْت |
| الرمز | س |
| المحارف | <span dir="ltr">`U+06DC` ARABIC SMALL HIGH SEEN</span> |
| عائلة العلامة | <span dir="ltr">`alamat_qiraah`</span> |
| تهجئات أخرى | <span dir="ltr">`alamat_al_sakt`</span> |

**التعريف:** علامة السكتة علامة تدل على السكت، وهو وقفة يسيرة من غير تنفس ثم الوصل بما بعده.

**الغرض:** نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.

- علامة السكتة رسم في المصحف، والسكتة الوقفة نفسها.

**مرتبط به:** <span dir="ltr">[`saktah`](#saktah)، [`qiraah_mark`](#qiraah_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!saktah`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/126) — `126`

<a id="seen_al_qiraah"></a>

### سين القراءة — Seen al-Qiraah

<!-- source: standards/terminology/concepts/seen_al_qiraah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`seen_al_qiraah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`qiraah_mark`](#qiraah_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | سِين القِرَاءَة |
| اسمه في الضبط | السِّين الدَّالَّة على وَجْه القِرَاءَة |
| اسمه بشكله | سِين فَوْق الصَّاد أو تَحْتَهَا |
| اسمه في تعريف المصحف | السِّين فَوْق الصَّاد أو تَحْتَهَا |
| الرمز | س |
| المحارف | <span dir="ltr">`U+06DC` ARABIC SMALL HIGH SEEN، `U+06E3` ARABIC SMALL LOW SEEN</span> |
| عائلة العلامة | <span dir="ltr">`alamat_qiraah`</span> |
| تهجئات أخرى | <span dir="ltr">`seen-reading`، `seen_reading`، `sin_qiraah`</span> |
| دليل اسم العرض | <span dir="ltr">letter name; unmeasurable directly, both forms are English words</span> |

**التعريف:** سين القراءة سين صغيرة فوق الصاد تدل على القراءة بالسين، وتحتها تدل على القراءة بالصاد.

**الغرض:** نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!seen-reading`

<a id="shaddah"></a>

### الشدة — Shaddah

<!-- source: standards/terminology/concepts/shaddah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`shaddah`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`harakah`](#harakah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الشَّدَّة |
| اسمه في الضبط | الشَّدَّة — رَأْس الشِّين (من «شَدِيد») |
| اسمه بشكله | رَأْس شِين بِلَا نُقَط |
| اسمه في تعريف المصحف | الشَّدَّة الدَّالَّة على الإِدْغَام |
| الرمز | ـّ |
| المحارف | <span dir="ltr">`U+0651` ARABIC SHADDA</span> |
| عائلة العلامة | <span dir="ltr">`harakah`</span> |
| تهجئات أخرى | <span dir="ltr">`shadda`، `tashdeed`، `tashdid`</span> |

**التعريف:** الشدة علامة تدل على تشديد الحرف، أي إدغام الأول الساكن في الثاني المتحرك حتى ينطقا حرفًا واحدًا مشددًا.

**الغرض:** نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم بدلًا من قراءة صورة الشكل.

**مرتبط به:** <span dir="ltr">[`harakah`](#harakah)، [`idgham`](#idgham)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!shadda`

<a id="small_meem"></a>

### الميم الصغيرة — Small Meem

<!-- source: standards/terminology/concepts/small_meem.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`small_meem`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المِيم الصَّغِيرَة |
| اسمه في الضبط | المِيم الصَّغِيرَة — عَلَامَة القَلْب |
| اسمه بشكله | مِيم صَغِيرَة، عُلْيَا أو سُفْلَى |
| اسمه في تعريف المصحف | المِيم الصَّغِيرَة |
| الرمز | م صَغِيرَة |
| المحارف | <span dir="ltr">`U+06E2` ARABIC SMALL HIGH MEEM ISOLATED FORM، `U+06ED` ARABIC SMALL LOW MEEM</span> |
| عائلة العلامة | <span dir="ltr">`dabt`</span> |
| تهجئات أخرى | <span dir="ltr">`iqlab_meem`، `meem-iqlab`، `meem_iqlab`، `meem_saghirah`، `mim_saghirah`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: meem sakinah 308 vs mim sakinah 57</span> |

**التعريف:** الميم الصغيرة علامة تدل على قلب النون الساكنة أو التنوين ميمًا عند الباء.

**الغرض:** نستخدمها علامة من علامات المصحف، فنعرف بها موضعها ودلالتها في العرض والتحليل.

**مرتبط به:** <span dir="ltr">[`noon_sakinah`](#noon_sakinah)، [`iqlab`](#iqlab)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!meem-iqlab`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`

<a id="small_noon"></a>

### النون الصغيرة — Small Noon

<!-- source: standards/terminology/concepts/small_noon.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`small_noon`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّون الصَّغِيرَة |
| اسمه في الضبط | النُّون الصَّغِيرَة — الحَرْف المُلْحَق بالرَّسْم |
| اسمه بشكله | نُون صَغِيرَة فَوْق السَّطْر |
| اسمه في تعريف المصحف | مِنَ الحُرُوف الصَّغِيرَة الدَّالَّة على المَتْرُوك مِنَ الرَّسْم |
| الرمز | ن صَغِيرَة |
| المحارف | <span dir="ltr">`U+06E8` ARABIC SMALL HIGH NOON</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`noon_saghirah`، `nun_saghirah`، `small-noon`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: noon sakinah 478 vs nun sakinah 118</span> |

**التعريف:** النون الصغيرة علامة تدل على نون محذوفة من الرسم واجبة النطق، وترد في موضع واحد (21:88).

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!small-noon`

<a id="small_waw"></a>

### الواو الصغيرة — Small Waw

<!-- source: standards/terminology/concepts/small_waw.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`small_waw`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَاو الصَّغِيرَة |
| اسمه في الضبط | الوَاو الصَّغِيرَة — عَلَامَة صِلَة هَاء الضَّمِير |
| اسمه بشكله | وَاو صَغِيرَة بَعْد الهَاء |
| اسمه في تعريف المصحف | الوَاو الصَّغِيرَة |
| الرمز | و صَغِيرَة |
| المحارف | <span dir="ltr">`U+06E5` ARABIC SMALL WAW</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`small-waw`، `waw_saghirah`</span> |

**التعريف:** الواو الصغيرة علامة تدل على صلة هاء الضمير المضمومة بواو لفظية في حال الوصل.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`madd_al_silah`](#madd_al_silah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!small-waw`

<a id="small_yaa"></a>

### الياء الصغيرة — Small Yaa

<!-- source: standards/terminology/concepts/small_yaa.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`small_yaa`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`orthographic_mark`](#orthographic_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | اليَاء الصَّغِيرَة |
| اسمه في الضبط | اليَاء الصَّغِيرَة — عَلَامَة صِلَة هَاء الضَّمِير |
| اسمه بشكله | يَاء صَغِيرَة مَرْدُودَة بَعْد الهَاء |
| اسمه في تعريف المصحف | اليَاء الصَّغِيرَة المَرْدُودَة إِلى خَلْف |
| الرمز | ي صَغِيرَة |
| المحارف | <span dir="ltr">`U+06E6` ARABIC SMALL YEH، `U+06E7` ARABIC SMALL HIGH YEH</span> |
| عائلة العلامة | <span dir="ltr">`imlaiyyah`</span> |
| تهجئات أخرى | <span dir="ltr">`small-ya`، `small_ya`، `ya_saghirah`، `yaa_saghirah`</span> |

**التعريف:** الياء الصغيرة علامة تدل على صلة هاء الضمير المكسورة بياء لفظية في حال الوصل.

**الغرض:** نستخدمها قيمة من علامات الرسم، فنعرف بها المواضع التي يخالف فيها الرسم اللفظ في الكلمة.

**مرتبط به:** <span dir="ltr">[`madd_al_silah`](#madd_al_silah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!small-ya`

<a id="sukun"></a>

### السكون — Sukun

<!-- source: standards/terminology/concepts/sukun.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sukun`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`harakah`](#harakah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السُّكُون |
| اسمه في الضبط | السُّكُون — رَأْس الخَاء المُهْمَلَة |
| اسمه بشكله | رَأْس خَاء بِلَا نُقْطَة |
| اسمه في تعريف المصحف | رَأْس خَاء صَغِيرَة دُون نُقْطَة |
| الرمز | ـْ |
| المحارف | <span dir="ltr">`U+0652` ARABIC SUKUN، `U+06E1` ARABIC SMALL HIGH DOTLESS HEAD OF KHAH</span> |
| عائلة العلامة | <span dir="ltr">`harakah`</span> |
| تهجئات أخرى | <span dir="ltr">`sukoon`</span> |

**التعريف:** السكون علامة تدل على سكون الحرف وإظهاره.

**الغرض:** نستخدمها قيمة من قيم الحركة، فنقرأ منها نطق الحرف في التحليل والعرض والتعليم بدلًا من قراءة صورة الشكل.

**مرتبط به:** <span dir="ltr">[`harakah`](#harakah)، [`noon_sakinah`](#noon_sakinah)، [`madd_lazim`](#madd_lazim)، [`qalqalah`](#qalqalah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!sukun`

<a id="tanwin"></a>

### التنوين — Tanwin

<!-- source: standards/terminology/concepts/tanwin.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tanwin`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| القيم | <span dir="ltr">[`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّنْوِين |
| تهجئات أخرى | <span dir="ltr">`tanween`</span> |

**التعريف:** التنوين هو نون ساكنة زائدة تلحق آخر الاسم، وترسم بتكرار صورة الحركة.

**الغرض:** نستخدم التنوين أبًا لعلامات التنوين الـ3، حتى تجتمع في قائمة واحدة بدل تفريقها.

**مرتبط به:** <span dir="ltr">[`harakah`](#harakah)، [`noon_sakinah`](#noon_sakinah)، [`iqlab`](#iqlab)، [`mushaf_mark`](#mushaf_mark)، [`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="tanwin_al_damm"></a>

### تنوين الضم — Tanwin al-Damm

<!-- source: standards/terminology/concepts/tanwin_al_damm.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tanwin_al_damm`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`tanwin`](#tanwin)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَنْوِين الضَّمّ |
| اسمه في الضبط | تَنْوِين الرَّفْع — الضَّمَّتَان |
| اسمه بشكله | وَاوَان صَغِيرَتَان فَوْق الحَرْف |
| اسمه في تعريف المصحف | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| الرمز | ـٌ |
| المحارف | <span dir="ltr">`U+064C` ARABIC DAMMATAN، `U+08F1` ARABIC OPEN DAMMATAN</span> |
| عائلة العلامة | <span dir="ltr">`tanwin`</span> |
| تهجئات أخرى | <span dir="ltr">`dammatan`، `tanween_damm`، `tanwin_al_rafa`، `tanwin_damm`</span> |

**التعريف:** تنوين الضم علامة تدل على التنوين المرفوع. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد الحرف التالي يدل على الإدغام الكامل، وتتابعهما دون تشديد يدل على الإدغام الناقص أو الإخفاء.

**الغرض:** نستخدمها قيمة من قيم التنوين، فنقرأ منها نطق آخر الاسم وحكمه بدلًا من قراءة صورة الشكل.

**مرتبط به:** <span dir="ltr">[`tanwin`](#tanwin)، [`noon_sakinah`](#noon_sakinah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!dammatan`

<a id="tanwin_al_fath"></a>

### تنوين الفتح — Tanwin al-Fath

<!-- source: standards/terminology/concepts/tanwin_al_fath.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tanwin_al_fath`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`tanwin`](#tanwin)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَنْوِين الفَتْح |
| اسمه في الضبط | تَنْوِين النَّصْب — الفَتْحَتَان |
| اسمه بشكله | أَلِفَان مُضْجَعَتَان فَوْق الحَرْف |
| اسمه في تعريف المصحف | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| الرمز | ـً |
| المحارف | <span dir="ltr">`U+064B` ARABIC FATHATAN، `U+08F0` ARABIC OPEN FATHATAN</span> |
| عائلة العلامة | <span dir="ltr">`tanwin`</span> |
| تهجئات أخرى | <span dir="ltr">`fathatan`، `tanween_fath`، `tanwin_al_nasb`، `tanwin_fath`</span> |

**التعريف:** تنوين الفتح علامة تدل على التنوين المنصوب. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد الحرف التالي يدل على الإدغام الكامل، وتتابعهما دون تشديد يدل على الإدغام الناقص أو الإخفاء.

**الغرض:** نستخدمها قيمة من قيم التنوين، فنقرأ منها نطق آخر الاسم وحكمه بدلًا من قراءة صورة الشكل.

**مرتبط به:** <span dir="ltr">[`tanwin`](#tanwin)، [`noon_sakinah`](#noon_sakinah)، [`madd_al_iwad`](#madd_al_iwad)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!fathatan`

<a id="tanwin_al_kasr"></a>

### تنوين الكسر — Tanwin al-Kasr

<!-- source: standards/terminology/concepts/tanwin_al_kasr.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tanwin_al_kasr`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`tanwin`](#tanwin)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَنْوِين الكَسْر |
| اسمه في الضبط | تَنْوِين الخَفْض — الكَسْرَتَان |
| اسمه بشكله | أَلِفَان مُضْجَعَتَان تَحْت الحَرْف |
| اسمه في تعريف المصحف | الحَرَكَتَان: تَرْكِيبًا أو تَتَابُعًا |
| الرمز | ـٍ |
| المحارف | <span dir="ltr">`U+064D` ARABIC KASRATAN، `U+08F2` ARABIC OPEN KASRATAN</span> |
| عائلة العلامة | <span dir="ltr">`tanwin`</span> |
| تهجئات أخرى | <span dir="ltr">`kasratan`، `tanween_kasr`، `tanwin_al_jarr`، `tanwin_al_khafd`، `tanwin_kasr`</span> |

**التعريف:** تنوين الكسر علامة تدل على التنوين المخفوض. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد الحرف التالي يدل على الإدغام الكامل، وتتابعهما دون تشديد يدل على الإدغام الناقص أو الإخفاء.

**الغرض:** نستخدمها قيمة من قيم التنوين، فنقرأ منها نطق آخر الاسم وحكمه بدلًا من قراءة صورة الشكل.

**مرتبط به:** <span dir="ltr">[`tanwin`](#tanwin)، [`noon_sakinah`](#noon_sakinah)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!kasratan`

<a id="tashil"></a>

### التسهيل — Tashil

<!-- source: standards/terminology/concepts/tashil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tashil`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`qiraah_mark`](#qiraah_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّسْهِيل |
| اسمه في الضبط | التَّسْهِيل — الهَمْزَة بَيْنَ بَيْنَ |
| اسمه بشكله | نُقْطَة كَبِيرَة مَطْمُوسَة مَكَان الهَمْزَة |
| اسمه في تعريف المصحف | النُّقْطَة دُون الحَرَكَة مَكَان الهَمْزَة |
| الرمز | نُقْطَة مَكَان الهَمْزَة |
| المحارف | <span dir="ltr">`U+06EC` ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE</span> |
| عائلة العلامة | <span dir="ltr">`alamat_qiraah`</span> |

**التعريف:** علامة التسهيل تدل على تسهيل الهمزة بين بين، أي بينها وبين الألف.

**الغرض:** نستخدمها قيمة من علامات القراءة، فننبه بها القارئ إلى أداء خاص في موضعها.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!tashil`

<a id="tashkil"></a>

### التشكيل — Tashkil

<!-- source: standards/terminology/concepts/tashkil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tashkil`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّشْكِيل |
| تهجئات أخرى | <span dir="ltr">`tashkeel`</span> |
| مقابل إنجليزي | <span dir="ltr">`vowel marks`، `vocalization`، `vocalisation`</span> |

**التعريف:** التشكيل هو طبقة علامات الضبط الملحقة بحروف النص، من الحركات والتنوين والشدة والسكون وما يتبعها، منظورًا إليها جملة واحدة.

**الغرض:** نستخدم التشكيل حين نتعامل مع طبقة الضبط كلها وليس مع علامة بعينها، مثل إثباتها في العرض أو تجريد النص منها للبحث.

- التشكيل هو الطبقة كلها، والحركة هي العلامة الواحدة.
- الضبط هو العلم وقواعده، والتشكيل هو ما ينتج عنه على الحروف.

**مرتبط به:** <span dir="ltr">[`harakah`](#harakah)، [`mushaf_mark`](#mushaf_mark)، [`ijam`](#ijam)، [`rasm`](#rasm)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/135) — `135`

<a id="three_dots"></a>

### الثلاث نقط — Three Dots

<!-- source: standards/terminology/concepts/three_dots.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`three_dots`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`ijam`](#ijam)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الثَّلَاث نُقَط |
| اسمه في الضبط | نَقْط الإِعْجَام — الثَّلَاث نُقَط |
| اسمه بشكله | ثَلَاث نُقَط مُثَلَّثَة |
| الرمز | ثَلَاث نُقَط |
| عائلة العلامة | <span dir="ltr">`ijam`</span> |
| تهجئات أخرى | <span dir="ltr">`thalath_nuqat`، `three-dots`</span> |

**التعريف:** الثلاث نقط ثلاث نقاط فوق الحرف تميزه عن الحرف الذي يشاركه في الرسم، مثل الثاء والشين.

**الغرض:** نستخدمها قيمة من قيم النقط، فنميز بها الحرف عن الحرف الذي يشاركه في الرسم في التحليل والبحث.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!three-dots`

<a id="two_dots"></a>

### النقطتان — Two Dots

<!-- source: standards/terminology/concepts/two_dots.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`two_dots`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`ijam`](#ijam)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّقْطَتَان |
| اسمه في الضبط | نَقْط الإِعْجَام — النُّقْطَتَان |
| اسمه بشكله | نُقْطَتَان مُتَّصِلَتَان |
| الرمز | نُقْطَتَان |
| عائلة العلامة | <span dir="ltr">`ijam`</span> |
| تهجئات أخرى | <span dir="ltr">`nuqtatan`، `two-dots`</span> |

**التعريف:** النقطتان نقطتان فوق الحرف أو تحته تميزانه عن الحرف الذي يشاركه في الرسم، مثل التاء والياء والقاف.

**الغرض:** نستخدمها قيمة من قيم النقط، فنميز بها الحرف عن الحرف الذي يشاركه في الرسم في التحليل والبحث.

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!two-dots`

<a id="waqf_al_muanaqah"></a>

### وقف المعانقة — Waqf al-Muanaqah

<!-- source: standards/terminology/concepts/waqf_al_muanaqah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_al_muanaqah`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | وَقْف المُعَانَقَة |
| اسمه في الضبط | وَقْف المُعَانَقَة (ويُسمَّى وَقْف المُرَاقَبَة) |
| اسمه بشكله | ثَلَاث نُقَط تَتَكَرَّر عَلَى كَلِمَتَيْن |
| اسمه في تعريف المصحف | عَلَامَة تَعَانُق الوَقْف |
| الرمز | ثَلَاث نُقَط في مَوْضِعَيْن |
| المحارف | <span dir="ltr">`U+06DB` ARABIC SMALL HIGH THREE DOTS</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| تهجئات أخرى | <span dir="ltr">`muanaqah`، `muraqabah`، `taanuq_al_waqf`، `waqf_al_muraqabah`</span> |

**التعريف:** وقف المعانقة علامة تدل على موضعين للوقف، إذا وقف القارئ على أحدهما لم يصح الوقف على الآخر.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!muanaqah`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_mustawi_al_tarafayn"></a>

### الوقف الجائز مستوي الطرفين — Waqf Jaiz Mustawi al-Tarafayn

<!-- source: standards/terminology/concepts/waqf_jaiz_mustawi_al_tarafayn.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_jaiz_mustawi_al_tarafayn`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الجَائِز مُسْتَوِي الطَّرَفَيْن |
| اسمه في الضبط | الجِيم — عَلَامَة الوَقْف الجَائِز |
| اسمه بشكله | جِيم |
| اسمه في تعريف المصحف | عَلَامَة الوَقْف الجَائِز جَوَازًا مُسْتَوِيَ الطَّرَفَيْن |
| الرمز | ج |
| المحارف | <span dir="ltr">`U+06DA` ARABIC SMALL HIGH JEEM</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| أسماء متروكة | <span dir="ltr">`waqf-jaiz`، `waqf_jaiz`</span> |

**التعريف:** الوقف الجائز علامة تدل على أن الوقف جائز جوازًا مستوي الطرفين، فالوقف والوصل فيه سواء.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

> كان `waqf_jaiz` اسم هذه العلامة في سجل المصحف، وهو اسم يصدق على ثلاث علامات جائزة، فأُهمل.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!waqf-jaiz`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_waqf_awla"></a>

### الوقف الجائز مع كون الوقف أولى — Waqf Jaiz Waqf Awla

<!-- source: standards/terminology/concepts/waqf_jaiz_waqf_awla.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_jaiz_waqf_awla`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الجَائِز مَعَ كَوْنِ الوَقْف أَوْلَى |
| اسمه في الضبط | قلى — عَلَامَة الوَقْف أَوْلَى |
| اسمه بشكله | قلى |
| اسمه في تعريف المصحف | عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَقْف أَوْلَى |
| الرمز | قلى |
| المحارف | <span dir="ltr">`U+06D7` ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| تهجئات أخرى | <span dir="ltr">`waqf-awla`، `waqf_awla`</span> |

**التعريف:** علامة الوقف أولى تدل على أن الوقف جائز والوقف أولى.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!waqf-awla`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_jaiz_wasl_awla"></a>

### الوقف الجائز مع كون الوصل أولى — Waqf Jaiz Wasl Awla

<!-- source: standards/terminology/concepts/waqf_jaiz_wasl_awla.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_jaiz_wasl_awla`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الجَائِز مَعَ كَوْنِ الوَصْل أَوْلَى |
| اسمه في الضبط | صلى — عَلَامَة الوَصْل أَوْلَى |
| اسمه بشكله | صلى |
| اسمه في تعريف المصحف | عَلَامَة الوَقْف الجَائِز مَع كَوْن الوَصْل أَوْلَى |
| الرمز | صلى |
| المحارف | <span dir="ltr">`U+06D6` ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| تهجئات أخرى | <span dir="ltr">`wasl-awla`، `wasl_awla`</span> |

**التعريف:** علامة الوصل أولى تدل على أن الوقف جائز والوصل أولى.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!wasl-awla`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_lazim"></a>

### الوقف اللازم — Waqf Lazim

<!-- source: standards/terminology/concepts/waqf_lazim.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_lazim`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف اللَّازِم |
| اسمه في الضبط | المِيم — عَلَامَة الوَقْف اللَّازِم |
| اسمه بشكله | مِيم |
| اسمه في تعريف المصحف | عَلَامَة الوَقْف اللَّازِم |
| الرمز | م |
| المحارف | <span dir="ltr">`U+06D8` ARABIC SMALL HIGH MEEM INITIAL FORM</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| تهجئات أخرى | <span dir="ltr">`waqf-lazim`</span> |

**التعريف:** الوقف اللازم علامة تدل على أن الوقف لازم، لأن وصل ما بعده بما قبله يوهم خلاف المعنى المراد.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!waqf-lazim`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/122) — `122`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_mamnu"></a>

### الوقف الممنوع — Waqf Mamnu

<!-- source: standards/terminology/concepts/waqf_mamnu.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_mamnu`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_mark_type`](#waqf_mark_type)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف المَمْنُوع |
| اسمه في الضبط | لا — عَلَامَة الوَقْف المَمْنُوع |
| اسمه بشكله | لا |
| الرمز | لا |
| المحارف | <span dir="ltr">`U+06D9` ARABIC SMALL HIGH LAM ALEF</span> |
| عائلة العلامة | <span dir="ltr">`waqf`</span> |
| تهجئات أخرى | <span dir="ltr">`waqf-mamnu`</span> |

**التعريف:** الوقف الممنوع علامة تدل على أن الوقف ممنوع، لأن الوقف على الموضع يفسد المعنى أو يقطع ما لا ينفصل عما بعده.

**الغرض:** نستخدمها قيمة من قيم نوع علامة الوقف، فنبني عليها العرض والتلقين والتنبيه في التطبيقات بدلًا من قراءة صورة الرمز.

> مثبتة في سجل المصحف ولم ترد في هذه الطبعة البتة.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `standard!waqf-mamnu`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_mark"></a>

### علامة الوقف — Waqf Mark

<!-- source: standards/terminology/concepts/waqf_mark.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_mark`</span> |
| `plural` | <span dir="ltr">`waqf_marks`</span> |
| `kind` | <span dir="ltr">`mark`</span> |
| الأب | <span dir="ltr">[`mushaf_mark`](#mushaf_mark)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَامَة الوَقْف |

**التعريف:** علامة الوقف علامة في المصحف ترشد القارئ إلى حكم الوقف أو الوصل في موضع معين.

**الغرض:** نستخدمها لتمثيل الرمز وموضعه ونوعه على نحو منظم.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark_type`](#waqf_mark_type)، [`mushaf_mark`](#mushaf_mark)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

## عد الآي — `ayah_numbering`

<a id="ayah_count"></a>

### عدد الآيات — Ayah Count

<!-- source: standards/terminology/concepts/ayah_count.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_count`</span> |
| `plural` | <span dir="ltr">`ayah_counts`</span> |
| `kind` | <span dir="ltr">`property`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَدَد الآيَات |
| السجل | <span dir="ltr">[`ayah_counts`](/guidelines/ar/03-terminology/registries/#ayah_counts)</span> |
| تهجئات أخرى | <span dir="ltr">`ayat_count`، `number_of_ayahs`، `adad_al_ayat`، `adad_al_ay`</span> |
| مقابل إنجليزي | <span dir="ltr">`verse count`</span> |

**التعريف:** عدد الآيات هو عدد آيات السورة في نظام عد بعينه. وقد يختلف من نظام إلى نظام لأن الفواصل المعدودة تختلف.

**الغرض:** نستخدمه للتحقق من المراجع وحدود السور وبناء الفهارس. ونقرؤه من سجل العد ولا نحسبه من نص بعينه.

- العدد صفة للسورة تحت نظام عد، وليس صفة للمصحف.

> الاسم البرمجي يتبع نسق `ayah_numbering_*` واسم السجل، وليس اشتقاقًا من «عَدَد الآيَات»، لأن المفهوم من مفاهيم التمثيل وإن كان لعدد الآي أصل في علم العد.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`surah`](#surah)، [`ayah`](#ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_basri"></a>

### العد البصري — Basri Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_basri.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`basri`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ البَصْرِيّ |
| تهجئات أخرى | <span dir="ltr">`basri_numbering`، `basran`، `basran_numbering`</span> |

**التعريف:** العد البصري هو نظام عد الآي المروي عن عاصم الجحدري عن أسلافه من أهل البصرة.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `basri` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_basri`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_dimashqi"></a>

### العد الدمشقي — Dimashqi Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_dimashqi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`dimashqi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ الدِّمَشْقِيّ |
| تهجئات أخرى | <span dir="ltr">`dimashqi_numbering`، `shami`، `shami_numbering`، `damascene`، `ayah_numbering_shami`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: dimashqi numbering 0 vs shami numbering 0. No form is established, so the display follows the code; `shami` stays an alias.</span> |

**التعريف:** العد الدمشقي هو نظام عد أهل الشام، المروي عن يحيى بن الحارث الذماري عن ابن عامر، ويسمى العد الشامي.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `dimashqi` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_dimashqi`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/82`

<a id="ayah_numbering_kufi"></a>

### العد الكوفي — Kufi Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_kufi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`kufi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ الكُوفِيّ |
| تهجئات أخرى | <span dir="ltr">`kufi_numbering`، `kufan`، `kufan_numbering`</span> |

**التعريف:** العد الكوفي هو نظام عد الآي المروي عن حمزة الزيات عن ابن أبي ليلى عن أبي عبد الرحمن السلمي عن علي بن أبي طالب، وهو العد الذي تتبعه أكثر المصاحف المطبوعة اليوم.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `kufi` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_kufi`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_madani_first"></a>

### العد المدني الأول — First Madani Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_madani_first.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madani_first`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَدَنِيّ الأَوَّل |
| تهجئات أخرى | <span dir="ltr">`ayah_numbering_madani_awwal`، `madani_awwal`، `first_madani`، `first_madinan`، `madani_first_numbering`</span> |

**التعريف:** العد المدني الأول هو نظام عد أهل المدينة في روايته الأولى، وهي رواية أبي جعفر يزيد بن القعقاع وشيبة بن نصاح.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `madani_first` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_madani_first`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_madani_last"></a>

### العد المدني الأخير — Last Madani Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_madani_last.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madani_last`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَدَنِيّ الأَخِير |
| تهجئات أخرى | <span dir="ltr">`ayah_numbering_madani_akhir`، `madani_akhir`، `last_madani`، `last_madinan`، `madani_last_numbering`</span> |

**التعريف:** العد المدني الأخير هو نظام عد أهل المدينة في روايته الأخيرة، وهي رواية إسماعيل بن جعفر عن سليمان بن جماز.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `madani_last` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_madani_last`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_makki"></a>

### العد المكي — Makki Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_makki.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`makki`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَكِّيّ |
| تهجئات أخرى | <span dir="ltr">`makki_numbering`، `makkan`، `meccan_numbering`</span> |

**التعريف:** العد المكي هو نظام عد الآي المروي عن ابن كثير عن مجاهد عن ابن عباس عن أبي بن كعب.

**الغرض:** نستخدمه قيمة من قيم نظام عد الآي. وبه يبين المصحف أو `dataset` النظام الذي تستند إليه أرقام آياته وحدودها، وبه نقابل مواضع الآي بين الأنظمة.

> الاسم البرمجي `makki` وحده، لأن اسم القيمة فريد داخل تصنيفها لا في القاموس كله (§14)؛ فالعمود يحمل قيم تصنيف واحد، ولا يلتبس `makki` هنا بـ`makki` في `revelation_classification`. أما معرّف المدخل فهو `ayah_numbering_makki`، اسم الأب مع الاسم البرمجي، حتى يكون للمدخلين المشتركين في الاسم عنوانان مختلفان. ولا يشتق الاسم من «العَدّ» لأن اشتقاقه يعطي `add` وهو فعل إنجليزي. والسبب مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_system"></a>

### نظام عد الآي — Ayah Numbering System

<!-- source: standards/terminology/concepts/ayah_numbering_system.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_system`</span> |
| `plural` | <span dir="ltr">`ayah_numbering_systems`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_first`](#ayah_numbering_madani_first)، [`ayah_numbering_madani_last`](#ayah_numbering_madani_last)، [`ayah_numbering_makki`](#ayah_numbering_makki)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | نِظَام عَدّ الآي |
| السجل | <span dir="ltr">[`ayah_numbering`](/guidelines/ar/03-terminology/registries/#ayah_numbering)</span> |
| تهجئات أخرى | <span dir="ltr">`ayah_counting_system`</span> |

**التعريف:** نظام عد الآي هو النظام الذي يحدد حدود الآيات وأعدادها وأرقامها وبعض المسائل المتعلقة بالبسملة، وفق إحدى مدارس عد الآي.

**الغرض:** نستخدمه لتحديد النظام الذي تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset` معين.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)، [`basmalah`](#basmalah)، [`ayah_count`](#ayah_count)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_numbering_madani_first`](#ayah_numbering_madani_first)، [`ayah_numbering_madani_last`](#ayah_numbering_madani_last)، [`ayah_key`](#ayah_key)، [`ayah_mark`](#ayah_mark)، [`qiraah`](#qiraah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/31) — `31`
- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/225`

<a id="equivalent_ayah"></a>

### الآية المقابلة — Equivalent Ayah

<!-- source: standards/terminology/concepts/equivalent_ayah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`equivalent_ayah`</span> |
| `plural` | <span dir="ltr">`equivalent_ayahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الآيَة المُقَابِلَة |

**التعريف:** الآية المقابلة هي الآية في نظام عد تقابل آية في نظام عد آخر، سواء اتفق رقماهما أو اختلفا لاختلاف مواضع الفصل بين الآي.

**الغرض:** نستخدمها للربط بين أرقام الآيات عبر أنظمة العد، حتى لا تقارَن البيانات المبنية على نظام ببيانات مبنية على نظام آخر بالرقم وحده.

- المقابلة علاقة بين نظامي عد، وليست تشابهًا في اللفظ ولا تكرارًا للنص.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`mutashabihat`](#mutashabihat)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_first`](#ayah_numbering_madani_first)، [`ayah_numbering_madani_last`](#ayah_numbering_madani_last)، [`ayah_numbering_makki`](#ayah_numbering_makki)</span>

**المصادر:**

- [qiraat-ayah-map](https://github.com/quranpedia/qiraat-ayah-map)

## النزول — `revelation`

<a id="asbab_al_nuzul"></a>

### أسباب النزول — Asbab al-Nuzul

<!-- source: standards/terminology/concepts/asbab_al_nuzul.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`asbab_al_nuzul`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | أَسْبَاب النُّزُول |
| تهجئات أخرى | <span dir="ltr">`asbab_al-nozool`، `asbab_un-nuzul`</span> |

**التعريف:** أسباب النزول هي الحوادث أو الأسئلة التي نزلت آية أو آيات للحديث عنها أو لبيان حكم يتعلق بها.

**الغرض:** نستخدمها لربط الآيات بالمرويات والمعلومات المتعلقة بسبب نزولها.

**مرتبط به:** <span dir="ltr">[`revelation`](#revelation)، [`ayah`](#ayah)، [`surah_name_reason`](#surah_name_reason)، [`abrogation`](#abrogation)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/75`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/107`

<a id="disputed"></a>

### مختلف فيه — Disputed

<!-- source: standards/terminology/concepts/disputed.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`disputed`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`revelation_classification`](#revelation_classification)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مُخْتَلَف فِيه |
| تهجئات أخرى | <span dir="ltr">`mukhtalaf_fih`، `revelation_disputed`</span> |

**التعريف:** المختلف فيه هو ما اختلفت المصادر المعتمدة في تصنيفه بين المكي والمدني.

**الغرض:** نستخدمه حتى لا تُجبر البيانات المختلف فيها على قيمة `makki` أو `madani` دون توثيق الخلاف.

**مرتبط به:** <span dir="ltr">[`revelation_classification`](#revelation_classification)، [`makki`](#makki)، [`madani`](#madani)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="madani"></a>

### مدني — Madani

<!-- source: standards/terminology/concepts/madani.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madani`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`revelation_classification`](#revelation_classification)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَدَنِيّ |
| تهجئات أخرى | <span dir="ltr">`madaniyy`، `madinan`</span> |
| مقابل إنجليزي | <span dir="ltr">`Medinan`</span> |

**التعريف:** المدني ما نزل من القرآن بعد الهجرة، ولو نزل خارج المدينة.

**الغرض:** نستخدمه قيمة من قيم تصنيف النزول، فنوسم به السورة أو الآية.

- مدني وصف لزمن النزول بعد الهجرة، وليس لمكان النزول.

**مرتبط به:** <span dir="ltr">[`makki`](#makki)، [`revelation_classification`](#revelation_classification)، [`revelation`](#revelation)، [`disputed`](#disputed)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="makki"></a>

### مكي — Makki

<!-- source: standards/terminology/concepts/makki.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`makki`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`revelation_classification`](#revelation_classification)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَكِّيّ |
| النقحرة | <span dir="ltr">makkī</span> |
| تهجئات أخرى | <span dir="ltr">`makkiyy`، `makkan`</span> |
| مقابل إنجليزي | <span dir="ltr">`Meccan`</span> |

**التعريف:** المكي ما نزل من القرآن قبل الهجرة، ولو نزل خارج مكة.

**الغرض:** نستخدمه قيمة من قيم تصنيف النزول، فنوسم به السورة أو الآية.

- مكي وصف لزمن النزول قبل الهجرة، وليس لمكان النزول.

**مرتبط به:** <span dir="ltr">[`madani`](#madani)، [`revelation_classification`](#revelation_classification)، [`revelation`](#revelation)، [`disputed`](#disputed)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="revelation"></a>

### النزول — Revelation

<!-- source: standards/terminology/concepts/revelation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`revelation`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّزُول |

**التعريف:** النزول هو إنزال القرآن على النبي صلى الله عليه وسلم مفرقًا على مدة الرسالة بحسب الوقائع والحاجة.

**الغرض:** نستخدم النزول أصلًا يتفرع عنه ترتيب النزول وتصنيفه وأسبابه، لأن هذه الثلاثة كلها صفات لواقعة النزول ولا تفهم إلا بالرجوع إليه.

- النزول واقعة، أما ترتيب النزول وتصنيفه وسببه فهي صفات لهذه الواقعة وليست مرادفات لها.

**مرتبط به:** <span dir="ltr">[`revelation_order`](#revelation_order)، [`revelation_classification`](#revelation_classification)، [`asbab_al_nuzul`](#asbab_al_nuzul)، [`madani`](#madani)، [`makki`](#makki)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/100`

<a id="revelation_classification"></a>

### تصنيف النزول — Revelation Classification

<!-- source: standards/terminology/concepts/revelation_classification.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`revelation_classification`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`disputed`](#disputed)، [`madani`](#madani)، [`makki`](#makki)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَصْنِيف النُّزُول |

**التعريف:** تصنيف النزول هو تصنيف للنص القرآني بحسب وقوع نزوله قبل الهجرة أو بعدها وفق الاصطلاح المعتمد.

**الغرض:** نستخدم تصنيف النزول لتصنيف السور أو الآيات بحسب علاقتها بالهجرة دون الإيحاء بأن التصنيف جغرافي فقط.

**مرتبط به:** <span dir="ltr">[`makki`](#makki)، [`madani`](#madani)، [`disputed`](#disputed)، [`revelation`](#revelation)، [`surah`](#surah)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="revelation_order"></a>

### ترتيب النزول — Revelation Order

<!-- source: standards/terminology/concepts/revelation_order.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`revelation_order`</span> |
| `kind` | <span dir="ltr">`property`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَرْتِيب النُّزُول |

**التعريف:** ترتيب النزول هو ترتيب السور أو الآيات بحسب زمن نزولها، وقد يختلف بحسب المصدر المعتمد.

**الغرض:** نستخدم ترتيب النزول لتخزين ترتيب نزول السور أو الآيات مستقلًا عن ترتيب المصحف.

- ترتيب النزول غير ترتيب المصحف، ورقم السورة يعبر عن ترتيب المصحف.

**مرتبط به:** <span dir="ltr">[`revelation`](#revelation)، [`surah`](#surah)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/93`

## القراءات — `qiraat`

<a id="muqri"></a>

### المقرئ — Muqri

<!-- source: standards/terminology/concepts/muqri.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`muqri`</span> |
| `plural` | <span dir="ltr">`muqris`</span> |
| `kind` | <span dir="ltr">`role`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُقْرِئ |
| تهجئات أخرى | <span dir="ltr">`muqree`</span> |

**التعريف:** المقرئ من تلقى القراءة وأتقنها وينقلها إلى المتعلمين.

**الغرض:** نستخدمه لتمثيل دور التعليم والتلقي والإقراء، ويتميز عن مجرد `reciter`.

**مرتبط به:** <span dir="ltr">[`reciter`](#reciter)، [`rawi`](#rawi)، [`qiraah`](#qiraah)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/268`

<a id="qiraah"></a>

### القراءة — Qiraah

<!-- source: standards/terminology/concepts/qiraah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`qiraah`</span> |
| `plural` | <span dir="ltr">`qiraahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | القِرَاءَة |
| السجل | <span dir="ltr">[`qiraat`](/guidelines/ar/03-terminology/registries/#qiraat)</span> |
| تهجئات أخرى | <span dir="ltr">`qira'ah`، `qiraa`، `qiraat`، `qira'at`</span> |
| مقابل إنجليزي | <span dir="ltr">`Reading`</span> |

**التعريف:** القراءة هي وجه من وجوه قراءة القرآن ينسب إلى إمام من أئمة القراءات، وتتفرع عنه الروايات والطرق.

**الغرض:** تمثل القراءة المستوى الأعلى في نموذج القراءات، وتربط الروايات والطرق والنصوص المرتبطة بها.

**مرتبط به:** <span dir="ltr">[`riwayah`](#riwayah)، [`rawi`](#rawi)، [`tariq`](#tariq)، [`muqri`](#muqri)، [`ayah_numbering_system`](#ayah_numbering_system)، [`qiraah_mark`](#qiraah_mark)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`

<a id="rawi"></a>

### الراوي — Rawi

<!-- source: standards/terminology/concepts/rawi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`rawi`</span> |
| `plural` | <span dir="ltr">`rawis`</span> |
| `kind` | <span dir="ltr">`role`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرَّاوِي |
| السجل | <span dir="ltr">[`qiraat`](/guidelines/ar/03-terminology/registries/#qiraat)</span> |
| مقابل إنجليزي | <span dir="ltr">`Transmitter`</span> |

**التعريف:** الراوي هو من نسبت إليه الرواية عن إمام القراءة.

**الغرض:** نستخدم الراوي لتمثيل الشخص المرتبط بـ`riwayah`.

- الراوي هو من نسبت إليه الرواية عن إمام القراءة، والقارئ هو مؤدي التسجيل. لذلك لا يسمى مؤدي التسجيل راويًا لمجرد أنه يقرأ برواية.

**مرتبط به:** <span dir="ltr">[`riwayah`](#riwayah)، [`qiraah`](#qiraah)، [`reciter`](#reciter)، [`muqri`](#muqri)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`

<a id="riwayah"></a>

### الرواية — Riwayah

<!-- source: standards/terminology/concepts/riwayah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`riwayah`</span> |
| `plural` | <span dir="ltr">`riwayahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| جزء من | <span dir="ltr">[`qiraah`](#qiraah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الرِّوَايَة |
| السجل | <span dir="ltr">[`qiraat`](/guidelines/ar/03-terminology/registries/#qiraat)</span> |
| تهجئات أخرى | <span dir="ltr">`riwaya`، `rewaya`، `riwayat`</span> |

**التعريف:** الرواية هي ما ينسب إلى راو عن إمام القراءة، مثل رواية حفص عن عاصم.

**الغرض:** نستخدم الرواية لتحديد الرواية التي يتبعها نص أو مصحف أو تسجيل أو `dataset`.

**مرتبط به:** <span dir="ltr">[`qiraah`](#qiraah)، [`rawi`](#rawi)، [`tariq`](#tariq)، [`recitation`](#recitation)، [`mushaf_edition`](#mushaf_edition)، [`wajh`](#wajh)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/171`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`

<a id="tariq"></a>

### الطريق — Tariq

<!-- source: standards/terminology/concepts/tariq.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tariq`</span> |
| `plural` | <span dir="ltr">`tariqs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| جزء من | <span dir="ltr">[`riwayah`](#riwayah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الطَّرِيق |
| السجل | <span dir="ltr">[`tariq`](/guidelines/ar/03-terminology/registries/#tariq)</span> |
| تهجئات أخرى | <span dir="ltr">`tareeq`</span> |

**التعريف:** الطريق هو وجه النقل المأخوذ عن الراوي بواسطة من دونه في سلسلة نقل القراءة.

**الغرض:** نستخدم الطريق عندما تحتاج البيانات إلى مستوى أدق من الرواية لتمييز طرق الأداء والنقل.

> الطرق الـ4 التي تخزنها التطبيقات، وهي الشاطبية وطيبة النشر والدرة والتيسير، مسجلة في `registries/tariq.tsv`. أما حصر طرق النشر كلها، وعددها نحو 980 طريقًا، فلا يزال مفتوحًا.

**مرتبط به:** <span dir="ltr">[`riwayah`](#riwayah)، [`qiraah`](#qiraah)، [`wajh`](#wajh)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/146`

<a id="wajh"></a>

### الوجه — Wajh

<!-- source: standards/terminology/concepts/wajh.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`wajh`</span> |
| `plural` | <span dir="ltr">`wajhs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَجْه |
| الجمع | أَوْجُه |
| تهجئات أخرى | <span dir="ltr">`wajh_al_ada`، `awjuh`، `wujuh`، `wajh_qiraah`</span> |
| مقابل إنجليزي | <span dir="ltr">`permitted variant`</span> |

**التعريف:** الوجه هو كيفية من كيفيات الأداء يجوز الأخذ بأي منها في الرواية الواحدة أو الطريق الواحد، مثل أوجه المد العارض للسكون.

**الغرض:** نستخدم الوجه حين يحتاج التسجيل أو التعليم إلى تعيين الوجه المأخوذ به من أوجه جائزة، من غير أن ينسب الاختلاف إلى رواية أو طريق.

- الوجه لا يغير نسبة القراءة، والطريق يغيرها.

**مرتبط به:** <span dir="ltr">[`tariq`](#tariq)، [`riwayah`](#riwayah)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)</span>

## التلاوة — `recitation`

<a id="ayah_timing"></a>

### Ayah Timing

<!-- source: standards/terminology/concepts/ayah_timing.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_timing`</span> |
| `plural` | <span dir="ltr">`ayah_timings`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| تهجئات أخرى | <span dir="ltr">`ayah_timestamp`، `recitation_timing`، `timing`، `verse_timing`</span> |

**التعريف:** توقيت الآية مدى زمني في تسجيل تلاوة، له بداية ونهاية، ويقابل آية بعينها.

**الغرض:** نستخدمه لربط النص بالصوت. وعليه يقوم تتبع النص في أثناء الاستماع والانتقال إلى آية وتكرارها واقتطاعها.

- التوقيت صفة للتسجيل وليس للآية، فيختلف باختلاف التلاوة.
- التوقيت على مستوى الآية يختلف عن المحاذاة على مستوى الكلمة.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`ayah`](#ayah)، [`reciter`](#reciter)، [`word_timing`](#word_timing)</span>

<a id="istiadhah"></a>

### الاستعاذة — Istiadhah

<!-- source: standards/terminology/concepts/istiadhah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`istiadhah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الاِسْتِعَاذَة |
| تهجئات أخرى | <span dir="ltr">`isti'adhah`، `istiʿādhah`، `ta'awwudh`، `istiadha`، `istiaadhah`، `taawwudh`</span> |

**التعريف:** الاستعاذة طلب العوذ بالله من الشيطان عند إرادة تلاوة القرآن.

**الغرض:** نستخدمها لتمثيل الاستعاذة وصيغها وموضعها بالنسبة إلى بداية التلاوة.

**مرتبط به:** <span dir="ltr">[`basmalah`](#basmalah)، [`recitation`](#recitation)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/27) — `27`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/243`

<a id="khatmah"></a>

### الختمة — Khatmah

<!-- source: standards/terminology/concepts/khatmah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`khatmah`</span> |
| `plural` | <span dir="ltr">`khatmahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الخَتْمَة |
| تهجئات أخرى | <span dir="ltr">`khatma`</span> |

**التعريف:** الختمة قراءة القرآن كاملًا من أوله إلى آخره.

**الغرض:** نستخدمها لتتبع خطط الختم وإتمام القراءة وربط الجلسات بمسار ختمة.

**مرتبط به:** <span dir="ltr">[`juz`](#juz)، [`manzil`](#manzil)، [`recitation`](#recitation)</span>

<a id="recitation"></a>

### تسجيل التلاوة — Recitation

<!-- source: standards/terminology/concepts/recitation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`recitation`</span> |
| `plural` | <span dir="ltr">`recitations`</span> |
| `kind` | <span dir="ltr">`entity`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَسْجِيل التِّلَاوَة |

**التعريف:** تسجيل التلاوة هو تسجيل منشور لتلاوة القرآن، منسوب إلى قارئ ورواية ونمط أداء.

**الغرض:** نستخدم تسجيل التلاوة لتمثيل التسجيل الذي تربط به التوقيتات ونمط الأداء ومرتبة السرعة. وينسب التسجيل إلى قارئ ورواية، ويبقى مستقلًا عن فعل التلاوة.

- تسجيل التلاوة هو التسجيل المنشور المنسوب إلى قارئ ورواية ونمط أداء، أما التلاوة فهي الفعل نفسه.

**مرتبط به:** <span dir="ltr">[`reciter`](#reciter)، [`riwayah`](#riwayah)، [`recitation_style`](#recitation_style)، [`recitation_pace`](#recitation_pace)، [`ayah_timing`](#ayah_timing)، [`word_timing`](#word_timing)، [`tilawah`](#tilawah)، [`istiadhah`](#istiadhah)، [`khatmah`](#khatmah)، [`spoken_translation`](#spoken_translation)، [`tajwid`](#tajwid)، [`tartil`](#tartil)</span>

<a id="reciter"></a>

### القارئ — Reciter

<!-- source: standards/terminology/concepts/reciter.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`reciter`</span> |
| `plural` | <span dir="ltr">`reciters`</span> |
| `kind` | <span dir="ltr">`role`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | القَارِئ |
| تهجئات أخرى | <span dir="ltr">`qari`، `qaari`</span> |

**التعريف:** القارئ هو الشخص الذي يؤدي تلاوة القرآن.

**الغرض:** نستخدم القارئ لربط التسجيلات الصوتية بمؤديها.

- القارئ هو مؤدي التلاوة في التسجيل، وليس إمام قراءة ولا راويًا.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`rawi`](#rawi)، [`muqri`](#muqri)، [`ayah_timing`](#ayah_timing)، [`tilawah`](#tilawah)</span>

<a id="tartil"></a>

### الترتيل — Tartil

<!-- source: standards/terminology/concepts/tartil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tartil`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّرْتِيل |
| تهجئات أخرى | <span dir="ltr">`tarteel`</span> |

**التعريف:** الترتيل هو قراءة القرآن بتؤدة وبيان للحروف والكلمات ومراعاة الوقف والمعنى.

**الغرض:** نستخدم الترتيل صفة للأداء في وصف التسجيل والتعليم، وليس اسمًا للنمط الذي ينشر به التسجيل.

- الترتيل صفة الأداء نفسه، والمرتل نمط تسجيل، ولا يستعمل أحد الاسمين مكان الآخر.

**مرتبط به:** <span dir="ltr">[`murattal`](#murattal)، [`recitation`](#recitation)، [`recitation_pace`](#recitation_pace)، [`tilawah`](#tilawah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/21) — `21`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="tilawah"></a>

### التلاوة — Tilawah

<!-- source: standards/terminology/concepts/tilawah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tilawah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التِّلَاوَة |
| تهجئات أخرى | <span dir="ltr">`tilaawah`، `tilawa`، `tilawat`</span> |

**التعريف:** التلاوة هي قراءة القرآن بلفظه أداء بالصوت على ما تلقاه القارئ، سواء كانت في صلاة أو درس أو تسجيل.

**الغرض:** نستخدم التلاوة للدلالة على فعل القراءة نفسه حيث يقصد، مثل أحكام التلاوة وآدابها وسجدتها وتعلمها. ويبقى التسجيل المنشور لها `recitation`.

- التلاوة هي الفعل، و`recitation` هو التسجيل المنشور المنسوب إلى قارئ ورواية ونمط أداء.
- الترتيل صفة في التلاوة وليس التلاوة نفسها.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`tartil`](#tartil)، [`sajdah`](#sajdah)، [`reciter`](#reciter)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/16) — `16`

<a id="word_timing"></a>

### Word Timing

<!-- source: standards/terminology/concepts/word_timing.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`word_timing`</span> |
| `plural` | <span dir="ltr">`word_timings`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| تهجئات أخرى | <span dir="ltr">`word_timestamp`، `word_alignment`، `word_segment_timing`، `timing_segment`، `audio_segment`، `word_timings`</span> |

**التعريف:** توقيت الكلمة هو مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل كلمة بعينها من آية.

**الغرض:** نستخدم توقيت الكلمة لإبراز الكلمة المتلوة في أثناء الاستماع، ولمحاذاة النص مع الصوت على مستوى أدق من الآية، ولتقطيع التسجيل عند كلمة.

- توقيت الكلمة يقع داخل توقيت آيتها ولا يتجاوزه.
- تسمي واجهات الصوت هذا المفهوم `segment`، أما الاسم في هذا المعيار فهو `word_timing`، لأن `segment` في مدونات التحليل اللغوي اسم للوحدة الصرفية.

**مرتبط به:** <span dir="ltr">[`ayah_timing`](#ayah_timing)، [`word`](#word)، [`word_key`](#word_key)، [`recitation`](#recitation)</span>

## مراتب القراءة — `recitation_pace`

<a id="hadr"></a>

### الحدر — Hadr

<!-- source: standards/terminology/concepts/hadr.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hadr`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_pace`](#recitation_pace)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحَدْر |
| تهجئات أخرى | <span dir="ltr">`hadar`</span> |

**التعريف:** الحدر هو الإسراع في القراءة مع المحافظة على الحروف والحركات وأحكام الأداء دون إخلال.

**الغرض:** نستخدمه قيمة من قيم مراتب القراءة، فنوسم به التسجيل أو جلسة التعليم ونصفي به.

**مرتبط به:** <span dir="ltr">[`recitation_pace`](#recitation_pace)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/24) — `24`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="recitation_pace"></a>

### مراتب القراءة — Recitation Pace

<!-- source: standards/terminology/concepts/recitation_pace.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`recitation_pace`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`hadr`](#hadr)، [`tadwir`](#tadwir)، [`tahqiq`](#tahqiq)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَرَاتِب القِرَاءَة |

**التعريف:** مراتب القراءة هي تصنيف لسرعة أداء القراءة مع المحافظة على أحكامها.

**الغرض:** نستخدم مراتب القراءة لفصل مراتب السرعة التقليدية عن أنماط التسجيل مثل `murattal` و`mujawwad`.

**مرتبط به:** <span dir="ltr">[`tahqiq`](#tahqiq)، [`tadwir`](#tadwir)، [`hadr`](#hadr)، [`recitation_style`](#recitation_style)، [`tartil`](#tartil)، [`recitation`](#recitation)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

<a id="tadwir"></a>

### التدوير — Tadwir

<!-- source: standards/terminology/concepts/tadwir.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tadwir`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_pace`](#recitation_pace)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّدْوِير |
| تهجئات أخرى | <span dir="ltr">`tadweer`</span> |

**التعريف:** التدوير هو القراءة بسرعة متوسطة بين التحقيق والحدر مع المحافظة على الأحكام.

**الغرض:** نستخدم التدوير قيمة من قيم مراتب القراءة، نوسم بها التسجيل أو جلسة التعليم ونصفي بها.

**مرتبط به:** <span dir="ltr">[`recitation_pace`](#recitation_pace)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/25) — `25`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/207`

<a id="tahqiq"></a>

### التحقيق — Tahqiq

<!-- source: standards/terminology/concepts/tahqiq.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tahqiq`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_pace`](#recitation_pace)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّحْقِيق |
| تهجئات أخرى | <span dir="ltr">`tahqeeq`</span> |

**التعريف:** التحقيق هو القراءة ببطء وتؤدة مع استيفاء الحروف وأحكامها، ويستخدم كثيرًا في مقام التعليم.

**الغرض:** نستخدم التحقيق قيمة من قيم مراتب القراءة، نوسم بها التسجيل أو جلسة التعليم ونصفي بها.

**مرتبط به:** <span dir="ltr">[`recitation_pace`](#recitation_pace)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/26) — `26`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/205`

## أنماط الأداء — `recitation_style`

<a id="instructional_ayah_repetition"></a>

### تكرار الآيات — Instructional Ayah Repetition

<!-- source: standards/terminology/concepts/instructional_ayah_repetition.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`instructional_ayah_repetition`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَكْرَار الآيَات |

**التعريف:** تكرار الآيات هو إعادة آية أو جزء منها مرة أو مرات وفق نمط تعليمي يساعد على التلقي والحفظ.

**الغرض:** نستخدمه لوصف ميزة مستقلة في التسجيل التعليمي ولا نجعله جزءًا ضمنيًا من `muallim`.

**مرتبط به:** <span dir="ltr">[`muallim`](#muallim)، [`recitation_style`](#recitation_style)</span>

<a id="muallim"></a>

### معلم — Muallim

<!-- source: standards/terminology/concepts/muallim.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`muallim`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_style`](#recitation_style)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مُعَلِّم |

**التعريف:** المعلم نمط تلاوة معد للتعليم، وقد يتضمن تكرار الآيات أو إتاحة وقت للمتعلم للترديد.

**الغرض:** نستخدمه لتصنيف التسجيل بحسب نمطه.

**مرتبط به:** <span dir="ltr">[`recitation_style`](#recitation_style)، [`instructional_ayah_repetition`](#instructional_ayah_repetition)</span>

<a id="mujawwad"></a>

### مجود — Mujawwad

<!-- source: standards/terminology/concepts/mujawwad.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mujawwad`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_style`](#recitation_style)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مُجَوَّد |

**التعريف:** المجود نمط أداء بطيء يُمد فيه الصوت وتُستوفى أحكام التجويد بتطريب، وهو الوصف الذي تُنشر به التسجيلات المؤداة على هذا النحو.

**الغرض:** نستخدمه لتصنيف التسجيل بحسب نمطه.

- المجود نمط تسجيل، والتجويد علم يؤدى به كل نمط، لذلك لا يستعمل أحد الاسمين مكان الآخر.

**مرتبط به:** <span dir="ltr">[`recitation_style`](#recitation_style)، [`murattal`](#murattal)، [`tajwid`](#tajwid)</span>

<a id="murattal"></a>

### مرتل — Murattal

<!-- source: standards/terminology/concepts/murattal.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`murattal`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`recitation_style`](#recitation_style)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مُرَتَّل |

**التعريف:** المرتل نمط أداء متزن دون تطريب، على مرتبة الترتيل، وهو الوصف الذي تُنشر به التسجيلات المؤداة على هذا النحو.

**الغرض:** نستخدمه لتصنيف التسجيل بحسب نمطه.

- المرتل نمط تسجيل، والترتيل صفة الأداء نفسه، لذلك لا يستعمل أحد الاسمين مكان الآخر.

**مرتبط به:** <span dir="ltr">[`recitation_style`](#recitation_style)، [`mujawwad`](#mujawwad)، [`tartil`](#tartil)</span>

<a id="recitation_style"></a>

### نمط الأداء — Recitation Style

<!-- source: standards/terminology/concepts/recitation_style.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`recitation_style`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`muallim`](#muallim)، [`mujawwad`](#mujawwad)، [`murattal`](#murattal)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | نَمَط الأَدَاء |

**التعريف:** نمط الأداء هو تصنيف للتسجيلات والتلاوات بحسب طريقة أدائها، وهي مرتل أو مجود أو معلم، وهو مستقل عن القراءة والرواية.

**الغرض:** نستخدم نمط الأداء لتصنيف التسجيلات الصوتية بحسب طريقة الأداء أو الغرض منها.

**مرتبط به:** <span dir="ltr">[`murattal`](#murattal)، [`mujawwad`](#mujawwad)، [`muallim`](#muallim)، [`recitation`](#recitation)، [`recitation_pace`](#recitation_pace)، [`instructional_ayah_repetition`](#instructional_ayah_repetition)</span>

## التجويد — `tajwid`

<a id="ghunnah"></a>

### الغنة — Ghunnah

<!-- source: standards/terminology/concepts/ghunnah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ghunnah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الغُنَّة |
| تهجئات أخرى | <span dir="ltr">`ghunna`، `gunnah`، `ghunnah_sound`</span> |
| مقابل إنجليزي | <span dir="ltr">`nasalisation`</span> |

**التعريف:** الغنة صوت يخرج من الخيشوم مركب في جسم النون والميم، ولا عمل للسان فيه. ويختلف مقدارها بحسب الحكم، فهي أكمل ما تكون في المشدد والمدغم، ثم في المخفى، ثم في الساكن المظهر.

**الغرض:** نستخدمها صفة نوسم بها مواضع النص التي تُمد فيها الغنة، مثل النون والميم المشددتين والإدغام بغنة والإخفاء والإقلاب، حتى تُتبع في التلوين والتعليم، ولأن مقدارها يختلف باختلاف الطريق.

- الغنة صفة صوت وليست حكمًا في نفسها، فهي تلحق الإدغام والإخفاء والإقلاب ولا تقابلها.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/85) — `85`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `noon-mushaddadah`

<a id="idgham"></a>

### الإدغام — Idgham

<!-- source: standards/terminology/concepts/idgham.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`idgham`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`tajwid_ruling`](#tajwid_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِدْغَام |
| تهجئات أخرى | <span dir="ltr">`idghaam`، `idgam`، `edgham`، `idgham_bighunnah`، `idgham_bila_ghunnah`، `idgham_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`assimilation`، `merging`</span> |

**التعريف:** الإدغام إدخال حرف ساكن في حرف متحرك بعده بحيث يصيران حرفًا واحدًا مشددًا. ويكون الإدغام كاملًا أو ناقصًا، وبغنة أو بغير غنة.

**الغرض:** نستخدمه قيمة من قيم حكم التجويد، فنوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإدغام حكم، أما التماثل والتجانس والتقارب فعلاقة بين الحرفين يقع الإدغام بسببها.

**مرتبط به:** <span dir="ltr">[`izhar`](#izhar)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`ghunnah`](#ghunnah)، [`letter_relation`](#letter_relation)، [`mutamathilan`](#mutamathilan)، [`mutajanisan`](#mutajanisan)، [`meem_sakinah`](#meem_sakinah)، [`noon_sakinah`](#noon_sakinah)، [`shaddah`](#shaddah)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/57) — `57`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/60) — `60`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/61) — `61`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/63) — `63`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `idgham-bi-ghunnah-noon`

<a id="ikhfa"></a>

### الإخفاء — Ikhfa

<!-- source: standards/terminology/concepts/ikhfa.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ikhfa`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`tajwid_ruling`](#tajwid_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِخْفَاء |
| تهجئات أخرى | <span dir="ltr">`ikhfaa`، `ikhfa'`، `ekhfa`، `ikhfa_haqiqi`، `ikhfa_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`concealment`</span> |

**التعريف:** الإخفاء هو النطق بالحرف الساكن على صفة بين الإظهار والإدغام، دون تشديد ومع بقاء الغنة. ويكون حقيقيًّا في النون الساكنة والتنوين عند حروفه الـ15، وشفويًّا في الميم الساكنة عند الباء.

**الغرض:** نستخدمه قيمة من قيم حكم التجويد، فنوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

**مرتبط به:** <span dir="ltr">[`izhar`](#izhar)، [`idgham`](#idgham)، [`ghunnah`](#ghunnah)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/67) — `67`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/68) — `68`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `ikhfa-haqiqi-noon`

<a id="iqlab"></a>

### الإقلاب — Iqlab

<!-- source: standards/terminology/concepts/iqlab.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`iqlab`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`tajwid_ruling`](#tajwid_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِقْلَاب |
| تهجئات أخرى | <span dir="ltr">`iqlaab`، `qalb`، `iqlab_qalb`، `eqlab`</span> |
| مقابل إنجليزي | <span dir="ltr">`conversion`</span> |

**التعريف:** الإقلاب قلب النون الساكنة أو التنوين ميمًا مخفاة بغنة عند الباء.

**الغرض:** نستخدمه قيمة من قيم حكم التجويد، فنوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإقلاب حكم في النطق، والميم الصغيرة هي العلامة التي يُرسم بها في المصحف.

**مرتبط به:** <span dir="ltr">[`noon_sakinah`](#noon_sakinah)، [`tanwin`](#tanwin)، [`ghunnah`](#ghunnah)، [`small_meem`](#small_meem)، [`idgham`](#idgham)، [`izhar`](#izhar)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `iqlab-noon`

<a id="izhar"></a>

### الإظهار — Izhar

<!-- source: standards/terminology/concepts/izhar.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`izhar`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`tajwid_ruling`](#tajwid_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِظْهَار |
| تهجئات أخرى | <span dir="ltr">`izhaar`، `idhhar`، `idhar`، `ithhar`، `izhar_halqi`، `izhar_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`clear pronunciation`</span> |

**التعريف:** الإظهار إخراج الحرف الساكن من مخرجه من غير غنة زائدة فيه، مثل إظهار النون الساكنة والتنوين عند حروف الحلق، وإظهار الميم الساكنة عند غير الباء والميم.

**الغرض:** نستخدمه قيمة من قيم حكم التجويد، فنوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإظهار حكم يقابل الإدغام والإخفاء، وليس غياب الحكم. فالموضع الموسوم به موضع تحقق فيه سبب الحكم ثم لم يقع فيه إدغام ولا إخفاء.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`letter_relation`](#letter_relation)، [`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/64) — `64`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/65) — `65`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-halqi-noon`

<a id="letter_relation"></a>

### علاقة الحرفين — Letter Relation

<!-- source: standards/terminology/concepts/letter_relation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`letter_relation`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَاقَة الحَرْفَيْن |
| تهجئات أخرى | <span dir="ltr">`letter_relations`، `alaqat_al_huruf`، `ilaqat_al_harfayn`</span> |
| مقابل إنجليزي | <span dir="ltr">`relation of two letters`</span> |

**التعريف:** علاقة الحرفين هي نسبة الحرفين المتجاورين أحدهما إلى الآخر في المخرج والصفة، وهي تماثل أو تجانس أو تقارب أو تباعد. وعليها يُبنى إدغام الأول في الثاني أو إظهاره.

**الغرض:** نستخدمها تصنيفًا نوسم به الموضع الذي يقع فيه إدغام الحرفين أو إظهارهما، حتى يُعرف سبب الحكم وليس الحكم وحده.

- العلاقة سبب، والإدغام والإظهار حكم يترتب عليها.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`izhar`](#izhar)، [`mutamathilan`](#mutamathilan)، [`mutajanisan`](#mutajanisan)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/59) — `59`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/62) — `62`

<a id="madd"></a>

### المد — Madd

<!-- source: standards/terminology/concepts/madd.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`madd_al_badal`](#madd_al_badal)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_lin`](#madd_al_lin)، [`madd_al_silah`](#madd_al_silah)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`madd_lazim`](#madd_lazim)، [`madd_munfasil`](#madd_munfasil)، [`madd_muttasil`](#madd_muttasil)، [`madd_tabii`](#madd_tabii)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ |
| الجمع | مدود |
| تهجئات أخرى | <span dir="ltr">`mad`، `madd_rule`، `mudud`، `mudood`، `madd_type`</span> |
| مقابل إنجليزي | <span dir="ltr">`prolongation`، `lengthening`</span> |

**التعريف:** المد إطالة الصوت بحرف من حروف المد الـ3، وهي الألف الساكنة بعد فتح والواو الساكنة بعد ضم والياء الساكنة بعد كسر. ويكون المد أصليًّا لا يقوم الحرف إلا به، أو فرعيًّا بسبب همز أو سكون.

**الغرض:** نستخدمه تصنيفًا تتفرع عليه أنواع المد، فنوسم به موضع النص مع نوعه ومقداره. ولأن مقادير المدود تختلف باختلاف الطريق، فإنها تُبين في وصف التسجيل والمصحف.

- حروف المد غير حروف اللين وإن اشتركتا في الواو والياء، فحرف المد ساكن بعد حركة تجانسه، وحرف اللين ساكن بعد فتح.
- المد هو الحكم، والمدة هي العلامة التي تدل عليه في المصحف.

**مرتبط به:** <span dir="ltr">[`maddah`](#maddah)، [`madd_tabii`](#madd_tabii)، [`madd_muttasil`](#madd_muttasil)، [`madd_munfasil`](#madd_munfasil)، [`madd_lazim`](#madd_lazim)، [`madd_al_badal`](#madd_al_badal)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_silah`](#madd_al_silah)، [`madd_al_lin`](#madd_al_lin)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/90) — `90`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/92) — `92`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/99) — `99`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/107) — `107`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/108) — `108`

<a id="madd_al_badal"></a>

### مد البدل — Madd al-Badal

<!-- source: standards/terminology/concepts/madd_al_badal.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_al_badal`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَدّ البَدَل |
| تهجئات أخرى | <span dir="ltr">`madd_badal`، `badal`، `mad_badal`</span> |
| مقابل إنجليزي | <span dir="ltr">`substitution madd`</span> |

**التعريف:** مد البدل مد سببه همزة قبل حرف المد، وأُبدل فيه حرف المد من همزة ساكنة، مثل «آمن» و«أوتوا» و«إيمان». ومقداره حركتان عند حفص، ويزيد عند ورش.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`hamzah`](#hamzah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/98) — `98`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-badal`

<a id="madd_al_iwad"></a>

### مد العوض — Madd al-Iwad

<!-- source: standards/terminology/concepts/madd_al_iwad.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_al_iwad`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَدّ العِوَض |
| تهجئات أخرى | <span dir="ltr">`madd_iwad`، `madd_al_ewad`، `madd_ewad`، `iwad`، `mad_iwad`</span> |
| مقابل إنجليزي | <span dir="ltr">`compensation madd`</span> |

**التعريف:** مد العوض هو مد الألف عوضًا عن تنوين الفتح عند الوقف على الكلمة، ومقداره حركتان.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`tanwin_al_fath`](#tanwin_al_fath)، [`waqf`](#waqf)، [`madd_tabii`](#madd_tabii)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/105) — `105`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-iwad`

<a id="madd_al_lin"></a>

### مد اللين — Madd al-Lin

<!-- source: standards/terminology/concepts/madd_al_lin.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_al_lin`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَدّ اللِّين |
| تهجئات أخرى | <span dir="ltr">`madd_lin`، `madd_leen`، `madd_al_leen`، `lin`، `leen`، `mad_leen`</span> |
| مقابل إنجليزي | <span dir="ltr">`soft madd`</span> |

**التعريف:** مد اللين هو مد الواو أو الياء الساكنة المفتوح ما قبلها عند الوقف على الكلمة بسكون عارض، مثل «خوف» و«بيت».

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/106) — `106`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/93) — `93`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `leen-waw`

<a id="madd_al_silah"></a>

### مد الصلة — Madd al-Silah

<!-- source: standards/terminology/concepts/madd_al_silah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_al_silah`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَدّ الصِّلَة |
| تهجئات أخرى | <span dir="ltr">`madd_silah`، `silah`، `madd_al_sila`، `madd_silah_sughra`، `madd_silah_kubra`، `mad_silah`</span> |
| مقابل إنجليزي | <span dir="ltr">`pronoun madd`</span> |

**التعريف:** مد الصلة مد ينشأ عن صلة هاء الضمير بواو أو ياء إذا وقعت بين متحركين. ويكون صغرى إذا لم يقع بعدها همز، وكبرى إذا وقع.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`small_waw`](#small_waw)، [`small_yaa`](#small_yaa)، [`madd_tabii`](#madd_tabii)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/97) — `97`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/96) — `96`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/95) — `95`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-silah-sughra`

<a id="madd_arid_li_al_sukun"></a>

### المد العارض للسكون — Madd Arid lil-Sukun

<!-- source: standards/terminology/concepts/madd_arid_li_al_sukun.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_arid_li_al_sukun`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ العَارِض لِلسُّكُون |
| تهجئات أخرى | <span dir="ltr">`madd_arid_lilsukun`، `madd_arid_lil_sukun`، `madd_arid`، `arid_lil_sukun`، `madd_aarid`، `madd_arid_lissukun`</span> |
| مقابل إنجليزي | <span dir="ltr">`incidental madd`</span> |
| دليل اسم العرض | <span dir="ltr">No dominant English form; «lil-Sukun» is how the phrase is written in English tajwid teaching, and the hyphenated preposition follows the display rule for the article.</span> |

**التعريف:** المد العارض للسكون مد سببه سكون عارض في الوقف بعد حرف المد، ويجوز فيه القصر والتوسط والطول.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

> الاشتقاق يعطي `madd_arid_li_al_sukun` بفصل لام الجر عن أداة التعريف، كما يقرره القسم 8. والصورة الملحومة `lilsukun` تُحال في `alternative_spellings`.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_al_lin`](#madd_al_lin)، [`waqf`](#waqf)، [`wajh`](#wajh)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/109) — `109`

<a id="madd_lazim"></a>

### المد اللازم — Madd Lazim

<!-- source: standards/terminology/concepts/madd_lazim.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_lazim`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ اللَّازِم |
| تهجئات أخرى | <span dir="ltr">`madd_laazim`، `lazim`، `madd_lazim_kalimi`، `madd_lazim_harfi`، `mad_lazim`</span> |
| مقابل إنجليزي | <span dir="ltr">`necessary madd`</span> |

**التعريف:** المد اللازم مد فرعي سببه سكون أصلي ثابت في الوصل والوقف بعد حرف المد، ويقع في كلمة أو في حرف من فواتح السور. ويكون مثقلًا بالإدغام أو مخففًا، ومقداره 6 حركات.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`sukun`](#sukun)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/103) — `103`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/110) — `110`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/111) — `111`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/112) — `112`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-lazim-harfi`

<a id="madd_munfasil"></a>

### المد المنفصل — Madd Munfasil

<!-- source: standards/terminology/concepts/madd_munfasil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_munfasil`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ المُنْفَصِل |
| تهجئات أخرى | <span dir="ltr">`madd_jaiz_munfasil`، `munfasil`، `madd_munfasil_jaiz`، `mad_munfasil`</span> |
| مقابل إنجليزي | <span dir="ltr">`separated madd`</span> |

**التعريف:** المد المنفصل مد فرعي سببه همزة في أول الكلمة التالية لحرف المد، وهو جائز، فيُقصر ويُمد بحسب الرواية والطريق.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_muttasil`](#madd_muttasil)، [`hamzah`](#hamzah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/102) — `102`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-munfasil`

<a id="madd_muttasil"></a>

### المد المتصل — Madd Muttasil

<!-- source: standards/terminology/concepts/madd_muttasil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_muttasil`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ المُتَّصِل |
| تهجئات أخرى | <span dir="ltr">`madd_wajib_muttasil`، `muttasil`، `madd_muttasil_wajib`، `mad_muttasil`، `madd_mutasil`</span> |
| مقابل إنجليزي | <span dir="ltr">`connected madd`</span> |

**التعريف:** المد المتصل مد فرعي سببه همزة بعد حرف المد في كلمة واحدة، وهو واجب عند القراء جميعًا، وتختلف مقاديره بحسب الرواية والطريق.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_munfasil`](#madd_munfasil)، [`hamzah`](#hamzah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/101) — `101`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-muttasil`

<a id="madd_tabii"></a>

### المد الطبيعي — Madd Tabee

<!-- source: standards/terminology/concepts/madd_tabii.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`madd_tabii`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`madd`](#madd)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَدّ الطَّبِيعِيّ |
| تهجئات أخرى | <span dir="ltr">`madd_tabee`، `madd_tabi'i`، `madd_tabiee`، `madd_asli`</span> |
| مقابل إنجليزي | <span dir="ltr">`natural madd`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: madd tabee 111 vs madd tabii 63. The display follows the dominant English form; the code stays derived.</span> |

**التعريف:** المد الطبيعي هو المد الذي لا تقوم ذات حرف المد إلا به، ولا يتوقف على سبب من همز أو سكون، ومقداره حركتان.

**الغرض:** نستخدمه قيمة من قيم المد، فنوسم به موضع النص مع مقداره، ونقرأ منه ما يختلف باختلاف الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_silah`](#madd_al_silah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/100) — `100`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-tabee-kalimi`

<a id="meem_sakinah"></a>

### الميم الساكنة — Meem Sakinah

<!-- source: standards/terminology/concepts/meem_sakinah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`meem_sakinah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المِيم السَّاكِنَة |
| تهجئات أخرى | <span dir="ltr">`mim_sakinah`، `meem_saakinah`، `meem_sakina`</span> |
| مقابل إنجليزي | <span dir="ltr">`unvowelled meem`</span> |
| دليل اسم العرض | <span dir="ltr">tools/display_measurements.json: meem sakinah 308 vs mim sakinah 57. Letter names are written as they are said, so the derivation gives meem.</span> |

**التعريف:** الميم الساكنة ميم خالية من الحركة، ثابتة في اللفظ والخط، وتقع في وسط الكلمة أو آخرها.

**الغرض:** نستخدمها موضعًا تتفرع عليه الأحكام الشفوية الـ3 في محركات التجويد، وهي الإدغام والإخفاء والإظهار.

- الميم الساكنة غير الميم المقلوبة عن النون في الإقلاب وإن اتحد صوتهما.

**مرتبط به:** <span dir="ltr">[`noon_sakinah`](#noon_sakinah)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`ghunnah`](#ghunnah)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/63) — `63`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/68) — `68`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-shafawi-meem`

<a id="mutajanisan"></a>

### المتجانسان — Mutajanisan

<!-- source: standards/terminology/concepts/mutajanisan.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutajanisan`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`letter_relation`](#letter_relation)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَجَانِسَان |
| تهجئات أخرى | <span dir="ltr">`mutajanisain`، `mutajanisayn`، `mutajanisan_saghir`</span> |

**التعريف:** المتجانسان حرفان اتحدا في المخرج واختلفا في الصفة، مثل الدال والتاء في «قد تبين».

**الغرض:** نستخدمه قيمة من قيم علاقة الحرفين، فنقرأ منه سبب الإدغام أو الإظهار في الموضع بدلًا من استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`letter_relation`](#letter_relation)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/59) — `59`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `mutajanisain-idgham-naqis`

<a id="mutamathilan"></a>

### المتماثلان — Mutamathilan

<!-- source: standards/terminology/concepts/mutamathilan.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutamathilan`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`letter_relation`](#letter_relation)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَمَاثِلَان |
| تهجئات أخرى | <span dir="ltr">`mutamathilain`، `mutamathilayn`، `mithlayn`، `mutamathilan_saghir`</span> |

**التعريف:** المتماثلان حرفان اتحدا في المخرج والصفة، مثل الباء في «اضرب بعصاك».

**الغرض:** نستخدمه قيمة من قيم علاقة الحرفين، فنقرأ منه سبب الإدغام أو الإظهار في الموضع بدلًا من استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`letter_relation`](#letter_relation)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `mutamathilain-idgham-kamil`

<a id="noon_sakinah"></a>

### النون الساكنة — Noon Sakinah

<!-- source: standards/terminology/concepts/noon_sakinah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`noon_sakinah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّون السَّاكِنَة |
| النقحرة | <span dir="ltr">nūn sākinah</span> |
| تهجئات أخرى | <span dir="ltr">`nun_sakinah`، `noon_saakinah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Unvowelled Noon`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: noon sakinah 478 vs nun sakinah 118. Letter names are written as they are said, so the derivation gives noon rather than nun.</span> |

**التعريف:** النون الساكنة هي نون خالية من الحركة، تثبت في اللفظ والخط وفي حالي الوصل والوقف.

**الغرض:** نستخدم النون الساكنة موضعًا تبنى عليه أحكام الإظهار والإدغام والإقلاب والإخفاء في محركات التجويد.

**مرتبط به:** <span dir="ltr">[`tajwid`](#tajwid)، [`tanwin`](#tanwin)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`iqlab`](#iqlab)، [`ikhfa`](#ikhfa)، [`meem_sakinah`](#meem_sakinah)، [`ghunnah`](#ghunnah)، [`small_meem`](#small_meem)، [`sukun`](#sukun)، [`tajwid_ruling`](#tajwid_ruling)، [`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)</span>

**المصادر:**

- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `noon-tanween`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/64) — `64`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/57) — `57`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/86) — `86`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/67) — `67`

<a id="qalqalah"></a>

### القلقلة — Qalqalah

<!-- source: standards/terminology/concepts/qalqalah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`qalqalah`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`tajwid_ruling`](#tajwid_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | القَلْقَلَة |
| تهجئات أخرى | <span dir="ltr">`qalqala`، `qalqalah_sughra`، `qalqalah_kubra`، `qalqalh`</span> |
| مقابل إنجليزي | <span dir="ltr">`echoing`</span> |

**التعريف:** القلقلة هي اضطراب في صوت الحرف الساكن عند النطق به حتى تسمع له نبرة قوية. وتقع في حروف «قطب جد»، وتقوى بحسب موضع الحرف من الكلمة والوقف عليه.

**الغرض:** نستخدم القلقلة قيمة من قيم حكم التجويد. نوسم بها موضع النص في التحليل والتلوين والتعليم، وتندرج تحتها أنواعها في سجل الأحكام.

- القلقلة صفة من صفات الحروف التي لا ضد لها، وتعد حكمًا حين نوسم بها الموضع الذي تظهر فيه.

**مرتبط به:** <span dir="ltr">[`sukun`](#sukun)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/78) — `78`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `qalqalah-sughra`

<a id="saktah"></a>

### السكتة — Saktah

<!-- source: standards/terminology/concepts/saktah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`saktah`</span> |
| `plural` | <span dir="ltr">`saktahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | السَّكْتَة |
| تهجئات أخرى | <span dir="ltr">`sakta`، `sakt`</span> |

**التعريف:** السكتة هي قطع الصوت زمنًا يسيرًا من غير تنفس ثم متابعة القراءة.

**الغرض:** نستخدم السكتة لتمثيل مواضع السكت وخصائصها في النص أو التلاوة.

- السكتة هي الوقفة نفسها، وعلامة السكتة رسم في المصحف يدل عليها.

**مرتبط به:** <span dir="ltr">[`saktah_mark`](#saktah_mark)، [`waqf`](#waqf)، [`tajwid`](#tajwid)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/126) — `126`

<a id="tafkhim"></a>

### التفخيم — Tafkhim

<!-- source: standards/terminology/concepts/tafkhim.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tafkhim`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّفْخِيم |
| تهجئات أخرى | <span dir="ltr">`tafkheem`، `tafkhem`، `tafkhim_rule`</span> |
| مقابل إنجليزي | <span dir="ltr">`heavy pronunciation`، `velarisation`</span> |
| دليل اسم العرض | <span dir="ltr">tools/display_measurements.json: tafkhim 900 vs tafkheem 539; the derived form is also the dominant one.</span> |

**التعريف:** التفخيم هو سمن يدخل على صوت الحرف فيمتلئ الفم بصداه. وهو لازم في حروف الاستعلاء، وعارض في الراء ولام لفظ الجلالة والألف تبعًا لما قبلها.

**الغرض:** نستخدم التفخيم لوسم مواضع الحروف المفخمة تفخيمًا عارضًا في التلوين والتعليم، وإليه تنسب مراتب التفخيم في سجل الأحكام.

- التفخيم صفة في صوت الحرف، أما الاستعلاء فهو صفة المخرج التي ينتج عنها التفخيم.

**مرتبط به:** <span dir="ltr">[`tarqiq`](#tarqiq)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/87) — `87`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/89) — `89`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `tafkheem-rank-1-jazari`

<a id="tajwid"></a>

### التجويد — Tajweed

<!-- source: standards/terminology/concepts/tajwid.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tajwid`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّجْوِيد |
| النقحرة | <span dir="ltr">tajwīd</span> |
| السجل | <span dir="ltr">[`tajwid_rules`](/guidelines/ar/03-terminology/registries/#tajwid_rules)</span> |
| تهجئات أخرى | <span dir="ltr">`tajweed`، `tajwīd`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: tajweed 45,440 vs tajwid 25,280. The doubled form is dominant in English writing, so it is what readers see; the code name stays derived, because the doubling in general use is lexical and not a rule.</span> |

**التعريف:** التجويد هو علم أداء حروف القرآن من مخارجها وإعطائها حقوقها ومستحقاتها من الصفات والأحكام.

**الغرض:** نستخدم التجويد لتمثيل العلم الذي تنتمي إليه قواعد التجويد وأحكامه وتلوينات العرض في التطبيقات، وتنسب إليه القاعدة في المحرك أو القاموس.

- التجويد علم، والمجود نمط تسجيل، ولا يستعمل أحد الاسمين مكان الآخر.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`waqf`](#waqf)، [`mujawwad`](#mujawwad)، [`noon_sakinah`](#noon_sakinah)، [`tajwid_ruling`](#tajwid_ruling)، [`saktah`](#saktah)</span>

**المصادر:**

- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/190`

<a id="tajwid_ruling"></a>

### حكم التجويد — Tajwid Ruling

<!-- source: standards/terminology/concepts/tajwid_ruling.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tajwid_ruling`</span> |
| `plural` | <span dir="ltr">`tajwid_rulings`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`izhar`](#izhar)، [`qalqalah`](#qalqalah)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | حُكْم التَّجْوِيد |
| الجمع | أَحْكَام التَّجْوِيد |
| السجل | <span dir="ltr">[`tajwid_rules`](/guidelines/ar/03-terminology/registries/#tajwid_rules)</span> |
| تهجئات أخرى | <span dir="ltr">`hukm`، `hukum`، `ahkam_al_tajwid`، `ahkam_al_tajweed`، `tajwid_rule`، `tajweed_rule`، `tajweed_ruling`</span> |
| مقابل إنجليزي | <span dir="ltr">`tajwid ruling`</span> |

**التعريف:** حكم التجويد هو ما تقرره قواعد التجويد في أداء الحرف في موضع بعينه من النص، عند حرف يليه أو عند سكون أو همز، مثل الإظهار والإدغام والإقلاب والإخفاء والمد والقلقلة والتفخيم والترقيق.

**الغرض:** نستخدم حكم التجويد أبًا لأحكام التجويد ووعاء لسجلها. وتنسب إليه مواضع النص التي يقع فيها حكم، ويشار إلى الحكم بعينه بصف من السجل بدل اسم حر يختلف من محرك إلى محرك.

- الحكم هو ما يقع في الموضع، والتجويد هو العلم الذي يقرره.
- الحكم غير القاعدة، فالقاعدة هي شرط الحكم، والحكم هو أثر القاعدة في الموضع.

**مرتبط به:** <span dir="ltr">[`tajwid`](#tajwid)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`iqlab`](#iqlab)، [`ikhfa`](#ikhfa)، [`qalqalah`](#qalqalah)، [`madd`](#madd)، [`ghunnah`](#ghunnah)، [`tafkhim`](#tafkhim)، [`tarqiq`](#tarqiq)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)

<a id="tarqiq"></a>

### الترقيق — Tarqiq

<!-- source: standards/terminology/concepts/tarqiq.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tarqiq`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّرْقِيق |
| تهجئات أخرى | <span dir="ltr">`tarqeeq`، `tarqiq_rule`</span> |
| مقابل إنجليزي | <span dir="ltr">`light pronunciation`</span> |
| دليل اسم العرض | <span dir="ltr">tools/display_measurements.json: tarqiq 1156 vs tarqeeq 286; the derived form is also the dominant one.</span> |

**التعريف:** الترقيق هو نحول يدخل على صوت الحرف فلا يمتلئ الفم بصداه. وهو لازم في حروف الاستفال، وعارض في الراء ولام لفظ الجلالة.

**الغرض:** نستخدم الترقيق لوسم مواضع الحروف المرققة ترقيقًا عارضًا في التلوين والتعليم، وهو مقابل التفخيم.

**مرتبط به:** <span dir="ltr">[`tafkhim`](#tafkhim)، [`tajwid_ruling`](#tajwid_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/88) — `88`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `raa-tarqeeq`

## الوقف — `waqf`

<a id="waqf"></a>

### الوقف — Waqf

<!-- source: standards/terminology/concepts/waqf.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف |
| مقابل إنجليزي | <span dir="ltr">`Stop`، `Pause`</span> |

**التعريف:** الوقف هو قطع القراءة عند موضع من النص وفق أحكام الوقف والابتداء.

**الغرض:** نستخدم الوقف مفهومًا عامًا لقطع القراءة، أما `waqf_mark` فتمثل العلامات المطبوعة التي ترشد إليه.

**مرتبط به:** <span dir="ltr">[`waqf_mark`](#waqf_mark)، [`waqf_ruling`](#waqf_ruling)، [`waqf_mark_type`](#waqf_mark_type)، [`tajwid`](#tajwid)، [`saktah`](#saktah)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_lin`](#madd_al_lin)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_hasan`](#waqf_hasan)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_kafi`](#waqf_kafi)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)، [`waqf_qabih`](#waqf_qabih)، [`waqf_tamm`](#waqf_tamm)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/282`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_hasan"></a>

### الوقف الحسن — Waqf Hasan

<!-- source: standards/terminology/concepts/waqf_hasan.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_hasan`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_ruling`](#waqf_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الحَسَن |

**التعريف:** الوقف الحسن هو الوقف على ما أفاد معنًى وتعلق بما بعده لفظًا ومعنًى.

**الغرض:** نستخدم الوقف الحسن قيمة من قيم حكم الوقف، ونوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/124) — `124`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_kafi"></a>

### الوقف الكافي — Waqf Kafi

<!-- source: standards/terminology/concepts/waqf_kafi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_kafi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_ruling`](#waqf_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الكَافِي |

**التعريف:** الوقف الكافي هو الوقف على ما تم معناه وتعلق بما بعده في المعنى دون اللفظ.

**الغرض:** نستخدم الوقف الكافي قيمة من قيم حكم الوقف، ونوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/123) — `123`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_mark_type"></a>

### نوع علامة الوقف — Waqf Mark Type

<!-- source: standards/terminology/concepts/waqf_mark_type.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_mark_type`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | نَوْع عَلَامَة الوَقْف |

**التعريف:** نوع علامة الوقف هو تصنيف لما ترشد إليه علامة الوقف المرسومة في المصحف من لزوم أو منع أو جواز.

**الغرض:** يوفر نوع علامة الوقف مجموعة قيم موحدة تبني عليها التطبيقات، بدل قراءة صورة الرمز نفسه.

- نوع العلامة هو ما ترشد إليه العلامة المرسومة، أما حكم الوقف فهو صفة الموضع نفسه حتى لو لم ترسم عليه علامة.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark`](#waqf_mark)، [`waqf_ruling`](#waqf_ruling)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/152`

<a id="waqf_qabih"></a>

### الوقف القبيح — Waqf Qabih

<!-- source: standards/terminology/concepts/waqf_qabih.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_qabih`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_ruling`](#waqf_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف القَبِيح |

**التعريف:** الوقف القبيح هو الوقف على ما لم يفد معنًى، أو أفاد معنًى غير مراد.

**الغرض:** نستخدم الوقف القبيح قيمة من قيم حكم الوقف، ونوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/125) — `125`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_ruling"></a>

### حكم الوقف — Waqf Ruling

<!-- source: standards/terminology/concepts/waqf_ruling.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_ruling`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`waqf_hasan`](#waqf_hasan)، [`waqf_kafi`](#waqf_kafi)، [`waqf_qabih`](#waqf_qabih)، [`waqf_tamm`](#waqf_tamm)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | حُكْم الوَقْف |

**التعريف:** حكم الوقف هو تصنيف الموضع نفسه من جهة تمام المعنى عنده، وليس من جهة العلامة المرسومة عليه.

**الغرض:** نستخدم حكم الوقف في التعليم والتحليل النحوي والدلالي للوقف.

- حكم الوقف صفة الموضع، ونوع علامة الوقف هو ما ترشد إليه العلامة المرسومة. وقد يكون للموضع حكم ولا علامة عليه.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark_type`](#waqf_mark_type)، [`waqf_tamm`](#waqf_tamm)، [`waqf_kafi`](#waqf_kafi)، [`waqf_hasan`](#waqf_hasan)، [`waqf_qabih`](#waqf_qabih)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_tamm"></a>

### الوقف التام — Waqf Tamm

<!-- source: standards/terminology/concepts/waqf_tamm.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_tamm`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`waqf_ruling`](#waqf_ruling)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف التَّامّ |

**التعريف:** الوقف التام هو الوقف على ما تم معناه ولم يتعلق بما بعده لفظًا ولا معنًى.

**الغرض:** نستخدم الوقف التام قيمة من قيم حكم الوقف، ونوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/121) — `121`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

## اللغة — `linguistics`

<a id="irab"></a>

### الإعراب — Irab

<!-- source: standards/terminology/concepts/irab.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`irab`</span> |
| `kind` | <span dir="ltr">`analysis`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِعْرَاب |
| تهجئات أخرى | <span dir="ltr">`i'rab`</span> |
| مقابل إنجليزي | <span dir="ltr">`Grammatical Analysis`</span> |

**التعريف:** الإعراب بيان الوظائف النحوية للكلمات وعلاماتها وعلاقاتها في التركيب.

**الغرض:** نستخدمه لربط كلمات الآيات بالتحليل النحوي والوظائف الإعرابية.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`morphology`](#morphology)، [`word`](#word)</span>

<a id="lemma"></a>

### Lemma

<!-- source: standards/terminology/concepts/lemma.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`lemma`</span> |
| `plural` | <span dir="ltr">`lemmas`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |

**التعريف:** الصيغة المعجمية هي الصيغة الأساسية التي تُرد إليها صورة الكلمة المصرفة.

**الغرض:** نستخدمها لتجميع الصور التصريفية المختلفة تحت مدخل معجمي واحد.

**مرتبط به:** <span dir="ltr">[`root`](#root)، [`stem`](#stem)، [`morphology`](#morphology)</span>

<a id="morpheme"></a>

### الوحدة الصرفية — Morpheme

<!-- source: standards/terminology/concepts/morpheme.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`morpheme`</span> |
| `plural` | <span dir="ltr">`morphemes`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَحْدَة الصَّرْفِيَّة |
| تهجئات أخرى | <span dir="ltr">`word_segment`</span> |

**التعريف:** الوحدة الصرفية أصغر وحدة في الكلمة تحمل معنى أو وظيفة صرفية، مثل السابقة واللاحقة والجذع.

**الغرض:** نستخدمها لتمثيل تقسيم الكلمة القرآنية إلى أجزائها الصرفية، وهو المستوى الذي تُنسب إليه السمات الصرفية والوسوم في مدونات التحليل.

- الوحدة الصرفية جزء من الكلمة، أما `token` فوحدة تقسيم قد تساوي الكلمة أو تزيد عليها.

> الاسم `segment` يعني في مدونات الصرف القرآني الوحدة الصرفية، ويعني في واجهات الصوت توقيت الكلمة. لذلك لا يكفي الاسم وحده لتعيين المفهوم، ويُقصد بـ`word_segment` هذا المدخل، ويُقصد بالمعنى الصوتي `word_timing`.

**مرتبط به:** <span dir="ltr">[`word`](#word)، [`token`](#token)، [`stem`](#stem)، [`morphology`](#morphology)، [`part_of_speech`](#part_of_speech)</span>

<a id="morphology"></a>

### الصرف — Morphology

<!-- source: standards/terminology/concepts/morphology.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`morphology`</span> |
| `kind` | <span dir="ltr">`analysis`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الصَّرْف |

**التعريف:** الصرف تحليل بنية الكلمة وصيغتها وما تحمله من خصائص صرفية.

**الغرض:** نستخدمه لتمثيل السمات الصرفية للكلمات أو `tokens`.

**مرتبط به:** <span dir="ltr">[`morpheme`](#morpheme)، [`root`](#root)، [`lemma`](#lemma)، [`stem`](#stem)، [`part_of_speech`](#part_of_speech)، [`irab`](#irab)، [`verb`](#verb)</span>

<a id="noun"></a>

### الاسم — Noun

<!-- source: standards/terminology/concepts/noun.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`noun`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الاِسْم |

**التعريف:** الاسم هو ما دل على معنى في نفسه غير مقترن بزمان، وتدخل فيه الأسماء والصفات والضمائر وأسماء الإشارة والموصولات.

**الغرض:** نستخدمه قيمة من قيم قسم الكلمة، وتندرج تحته الوسوم التفصيلية التي تستعملها مدونات الصرف القرآني.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)</span>

<a id="part_of_speech"></a>

### قسم الكلمة — Part of Speech

<!-- source: standards/terminology/concepts/part_of_speech.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`part_of_speech`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`noun`](#noun)، [`particle`](#particle)، [`verb`](#verb)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | قِسْم الكَلِمَة |
| تهجئات أخرى | <span dir="ltr">`pos`</span> |

**التعريف:** قسم الكلمة هو تصنيف الكلمة أو الوحدة الصرفية بحسب بابها النحوي، مثل الاسم والفعل والحرف وما يتفرع عنها.

**الغرض:** نستخدم قسم الكلمة وسمًا أساسيًا في التحليل الصرفي والنحوي، ويقوم عليه البحث بالوسم والتصفية وبناء التحليل الإعرابي.

> المعيار يثبت القسمة الثلاثية فقط. أما الوسوم التفصيلية التي تستعملها مدونات الصرف القرآني، وعددها عشرات، فهي بيانات تندرج تحت هذه القيم الثلاث ولا تفرد لها مداخل في القاموس.

**مرتبط به:** <span dir="ltr">[`morphology`](#morphology)، [`irab`](#irab)، [`morpheme`](#morpheme)، [`noun`](#noun)، [`particle`](#particle)، [`verb`](#verb)</span>

<a id="particle"></a>

### حرف المعنى — Particle

<!-- source: standards/terminology/concepts/particle.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`particle`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | حَرْف المَعْنَى |

**التعريف:** حرف المعنى هو ما دل على معنى في غيره، مثل حروف الجر والعطف والنفي والاستفهام.

**الغرض:** نستخدمه قيمة من قيم قسم الكلمة، وتندرج تحته وسوم الحروف التفصيلية في مدونات الصرف القرآني.

- حرف المعنى قسم من أقسام الكلمة، وحرف المبنى (`letter`) وحدة من النص المكتوب.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`letter`](#letter)</span>

<a id="root"></a>

### الجذر — Root

<!-- source: standards/terminology/concepts/root.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`root`</span> |
| `plural` | <span dir="ltr">`roots`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الجَذْر |

**التعريف:** الجذر هو الأصل الصرفي الذي ترد إليه الكلمة لبيان اشتقاقها وصلتها بالكلمات الأخرى.

**الغرض:** نستخدم الجذر في البحث الصرفي والتحليل اللغوي وتجميع الكلمات ذات الأصل المشترك.

**مرتبط به:** <span dir="ltr">[`lemma`](#lemma)، [`stem`](#stem)، [`morphology`](#morphology)</span>

<a id="stem"></a>

### الجذع — Stem

<!-- source: standards/terminology/concepts/stem.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`stem`</span> |
| `plural` | <span dir="ltr">`stems`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الجِذْع |

**التعريف:** الجذع هو ما يبقى من الكلمة بعد نزع السوابق واللواحق، وتلحق به الزوائد الصرفية.

**الغرض:** نستخدم الجذع في التحليل الصرفي مستوى وسطًا بين صورة الكلمة وجذرها. بعض المدونات تسجل الجذع ولا تسجل الجذر، وبعضها تسجلهما معًا.

- الجذر أصل اشتقاقي مجرد، أما الجذع فهو صورة قائمة في الكلمة بعد نزع الزوائد.

**مرتبط به:** <span dir="ltr">[`root`](#root)، [`lemma`](#lemma)، [`morpheme`](#morpheme)، [`morphology`](#morphology)</span>

<a id="verb"></a>

### الفعل — Verb

<!-- source: standards/terminology/concepts/verb.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`verb`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفِعْل |

**التعريف:** الفعل هو ما دل على معنى في نفسه مقترن بزمان، ويتصرف إلى الماضي والمضارع والأمر.

**الغرض:** نستخدمه قيمة من قيم قسم الكلمة، ونعلق عليه السمات الصرفية الخاصة بالفعل، مثل الزمن والبناء للمعلوم أو المجهول والوزن.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`morphology`](#morphology)</span>

## الترجمة — `translation`

<a id="spoken_translation"></a>

### الترجمة المنطوقة — Spoken Translation

<!-- source: standards/terminology/concepts/spoken_translation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`spoken_translation`</span> |
| `plural` | <span dir="ltr">`spoken_translations`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأب | <span dir="ltr">[`translation`](#translation)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّرْجَمَة المَنْطُوقَة |
| تهجئات أخرى | <span dir="ltr">`audio_translation`</span> |

**التعريف:** الترجمة المنطوقة هي نقل معاني القرآن إلى لغة أخرى في مادة صوتية أو منطوقة.

**الغرض:** نستخدم الترجمة المنطوقة لتمييز المحتوى الصوتي لترجمة المعاني عن الترجمة النصية وعن التلاوة القرآنية.

**مرتبط به:** <span dir="ltr">[`translation`](#translation)، [`recitation`](#recitation)</span>

<a id="translation"></a>

### الترجمة — Translation

<!-- source: standards/terminology/concepts/translation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`translation`</span> |
| `plural` | <span dir="ltr">`translations`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأبناء | <span dir="ltr">[`spoken_translation`](#spoken_translation)، [`word_by_word_translation`](#word_by_word_translation)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّرْجَمَة |

**التعريف:** الترجمة هي نقل معاني القرآن إلى لغة أخرى، وهي ليست قرآنًا بلفظه.

**الغرض:** نستخدم الترجمة لربط نصوص ترجمة المعاني بالآيات واللغات والمترجمين والمصادر.

**مرتبط به:** <span dir="ltr">[`transliteration`](#transliteration)، [`spoken_translation`](#spoken_translation)، [`translator`](#translator)، [`word_by_word_translation`](#word_by_word_translation)، [`tafsir`](#tafsir)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/324`

<a id="translator"></a>

### المترجم — Translator

<!-- source: standards/terminology/concepts/translator.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`translator`</span> |
| `plural` | <span dir="ltr">`translators`</span> |
| `kind` | <span dir="ltr">`role`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَرْجِم |
| تهجئات أخرى | <span dir="ltr">`mutarjim`</span> |

**التعريف:** المترجم هو من نسبت إليه ترجمة لمعاني القرآن إلى لغة أخرى، سواء كان فردًا أو هيئة.

**الغرض:** نستخدم المترجم لنسبة الترجمة إلى صاحبها، ولتمييزه عن الناشر والمراجع ومصدر النص.

- المترجم غير المفسر حتى لو استند في ترجمته إلى تفسير.

**مرتبط به:** <span dir="ltr">[`translation`](#translation)، [`mufassir`](#mufassir)</span>

<a id="transliteration"></a>

### النقل الحرفي — Transliteration

<!-- source: standards/terminology/concepts/transliteration.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`transliteration`</span> |
| `plural` | <span dir="ltr">`transliterations`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النَّقْل الحَرْفِيّ |

**التعريف:** النقل الحرفي هو تمثيل حروف نظام كتابي بحروف نظام آخر وفق قواعد محددة، دون ترجمة المعنى.

**الغرض:** نستخدم النقل الحرفي لتوفير تمثيل قابل للقراءة بنظام كتابي آخر أو للتحويل المنهجي بين أنظمة الكتابة.

**مرتبط به:** <span dir="ltr">[`translation`](#translation)</span>

<a id="word_by_word_translation"></a>

### Word by Word Translation

<!-- source: standards/terminology/concepts/word_by_word_translation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`word_by_word_translation`</span> |
| `plural` | <span dir="ltr">`word_by_word_translations`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأب | <span dir="ltr">[`translation`](#translation)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| تهجئات أخرى | <span dir="ltr">`wbw`، `word_by_word`، `wbw_translation`، `word_translation`، `wordbyword`</span> |

**التعريف:** الترجمة كلمة بكلمة هي ترجمة تعطي كل كلمة من كلمات الآية معناها في لغة أخرى على حدة، بترتيب كلمات الأصل.

**الغرض:** نستخدم الترجمة كلمة بكلمة في العرض التعليمي والتعلم، ونربطها بالكلمة بمفتاحها وليس بالآية.

- ترجمة الكلمة على حدة ليست ترجمة للآية، ولا تُعرض مكانها.

**مرتبط به:** <span dir="ltr">[`translation`](#translation)، [`word`](#word)، [`word_key`](#word_key)</span>

## التفسير — `tafsir`

<a id="mufassir"></a>

### المفسر — Mufassir

<!-- source: standards/terminology/concepts/mufassir.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mufassir`</span> |
| `plural` | <span dir="ltr">`mufassirs`</span> |
| `kind` | <span dir="ltr">`role`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُفَسِّر |
| مقابل إنجليزي | <span dir="ltr">`Exegete`</span> |

**التعريف:** المفسر من نُسب إليه تفسير للقرآن، تأليفًا أو رواية.

**الغرض:** نستخدمه لنسبة التفسير إلى صاحبه، فيتميز صاحب القول عن الكتاب الذي نُقل فيه وعن محققه وناشره.

- المفسر صاحب القول، وقد يُنقل قوله في كتاب لغيره.

**مرتبط به:** <span dir="ltr">[`tafsir`](#tafsir)، [`translator`](#translator)، [`tafsir_al_ray`](#tafsir_al_ray)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/200`

<a id="tafsir"></a>

### التفسير — Tafsir

<!-- source: standards/terminology/concepts/tafsir.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tafsir`</span> |
| `plural` | <span dir="ltr">`tafsirs`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّفْسِير |
| تهجئات أخرى | <span dir="ltr">`tafseer`</span> |
| مقابل إنجليزي | <span dir="ltr">`Exegesis`، `Commentary`</span> |

**التعريف:** التفسير هو بيان معاني القرآن وشرح ألفاظه وما يرشد إليه من أحكام وهدايات بحسب أصول التفسير.

**الغرض:** نستخدم التفسير لتمثيل كتب التفسير ومحتواه وربط مقاطعه بالآيات والسور والمصادر.

**مرتبط به:** <span dir="ltr">[`tafsir_mathur`](#tafsir_mathur)، [`tafsir_al_ray`](#tafsir_al_ray)، [`mufassir`](#mufassir)، [`word_meanings`](#word_meanings)، [`ayah`](#ayah)، [`reflection`](#reflection)، [`surah_objectives`](#surah_objectives)، [`translation`](#translation)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/334`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/192`

<a id="tafsir_al_ray"></a>

### تفسير الرأي — Tafsir al-Ray

<!-- source: standards/terminology/concepts/tafsir_al_ray.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tafsir_al_ray`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَفْسِير الرَّأْي |
| تهجئات أخرى | <span dir="ltr">`tafsir_bil_ray`، `tafsir_bialray`، `tafsir_al_raay`، `tafsir_bir_ray`</span> |
| مقابل إنجليزي | <span dir="ltr">`reasoned tafsir`</span> |

**التعريف:** تفسير الرأي هو بيان معاني القرآن بالاجتهاد والنظر بعد معرفة كلام العرب وأساليبه وأصول التفسير، سواء كان الاجتهاد محمودًا أو مذمومًا.

**الغرض:** نستخدم تفسير الرأي نوعًا للمحتوى المؤلف الذي ينسب إلى صاحبه قولًا، حتى يتميز عما ينقل بإسناد.

- تفسير الرأي قول صاحبه، والتفسير المأثور منقول بإسناد.

**مرتبط به:** <span dir="ltr">[`tafsir_mathur`](#tafsir_mathur)، [`tafsir`](#tafsir)، [`mufassir`](#mufassir)</span>

<a id="tafsir_mathur"></a>

### التفسير المأثور — Tafsir Mathur

<!-- source: standards/terminology/concepts/tafsir_mathur.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tafsir_mathur`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّفْسِير المَأْثُور |
| تهجئات أخرى | <span dir="ltr">`tafsir_bil_mathur`، `tafsir_bialmathur`، `mathur`</span> |
| مقابل إنجليزي | <span dir="ltr">`Transmitted Tafsir`</span> |

**التعريف:** التفسير المأثور هو ما فسر به القرآن من القرآن نفسه أو من السنة أو من قول الصحابة والتابعين، منقولًا بإسناده.

**الغرض:** نستخدم التفسير المأثور محتوى يربط بالآية ويحمل معه ناقله ودرجة النقل. ولذلك لا يعامل معاملة نص التفسير المؤلف الذي ينسب إلى كتاب واحد.

- التفسير المأثور منقول بإسناد، والتفسير المؤلف قول صاحب الكتاب.
- الأثر الواحد ليس مفهومًا في هذا المعيار، والمفهوم هو نوع المحتوى المرتب على الآية.

> العنوان الأشهر هو «التَّفْسِير بِالمَأْثُور»، واشتقاقه يلصق حرف الجر بالاسم فيعطي `tafsir_bialmathur`. لذلك الاسم المثبت هو الصورة الوصفية، وهي عربية مستعملة، والصورة الأشهر مسجلة في `alternative_spellings`. وللسبب نفسه أفرد `abrogation` بدل «الناسخ والمنسوخ».

**مرتبط به:** <span dir="ltr">[`tafsir`](#tafsir)، [`ayah`](#ayah)، [`tafsir_al_ray`](#tafsir_al_ray)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/358`

## علوم القرآن — `quranic_sciences`

<a id="abrogation"></a>

### النسخ — Abrogation

<!-- source: standards/terminology/concepts/abrogation.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`abrogation`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النَّسْخ |
| تهجئات أخرى | <span dir="ltr">`nasikh_mansukh`، `nasikh_wa_mansukh`، `nasekh_mansokh`</span> |

**التعريف:** النسخ هو رفع حكم شرعي بدليل شرعي جاء بعده، ويدرس في القرآن بنسبة الآية الناسخة إلى الآية المنسوخة.

**الغرض:** نستخدم النسخ لتمثيل العلاقة بين آيتين إحداهما ناسخة والأخرى منسوخة. وهذه علاقة بين موضعين من النص وليست صفة في آية واحدة.

- النسخ يقع على الحكم وليس على النص، فالآية التي نسخ حكمها تبقى ثابتة في المصحف.
- العلماء يختلفون في نسبة النسخ في كثير من المواضع، لذلك تقيد كل نسبة بمصدرها ولا تعرض على أنها حكم مجمع عليه.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`asbab_al_nuzul`](#asbab_al_nuzul)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/237`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/66`

<a id="mutashabihat"></a>

### المتشابهات — Mutashabihat

<!-- source: standards/terminology/concepts/mutashabihat.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutashabihat`</span> |
| `kind` | <span dir="ltr">`analysis`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَشَابِهَات |
| تهجئات أخرى | <span dir="ltr">`mutashabih`، `mutashabihat_lafziyyah`، `similar_ayahs`</span> |
| مقابل إنجليزي | <span dir="ltr">`Similar Passages`</span> |

**التعريف:** المتشابهات هي المواضع التي يتشابه فيها لفظ الآيات أو أجزائها في القرآن، تشابهًا تامًّا أو مع اختلاف يسير في كلمة أو ترتيب.

**الغرض:** نستخدمها أساسًا لأدوات الحفظ والمراجعة والبحث، لأن الحافظ يحتاج إلى معرفة المواضع التي يلتبس بعضها ببعض وموضع الفرق بينها.

- التشابه اللفظي المقصود هنا غير المتشابه المقابل للمحكم في علوم القرآن.
- التشابه علاقة بين موضعين أو أكثر، وليس صفة في آية واحدة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`word`](#word)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/390`

<a id="quran_merits"></a>

### فضائل القرآن — Quran Merits

<!-- source: standards/terminology/concepts/quran_merits.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`quran_merits`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | فَضَائِل القُرْآن |
| تهجئات أخرى | <span dir="ltr">`fadail`، `fadail_al_surah`</span> |

**التعريف:** فضائل القرآن هي ما ورد في فضل القرآن أو فضل سورة منه أو آية، وما يترتب على قراءتها من أجر أو أثر.

**الغرض:** نستخدمها محتوى يُربط بالقرآن كله أو بسورة أو آية. ونفصلها عن التفسير لأنها لا تفسر المعنى، وعن الحديث لأنها مرتبة على الموضع من القرآن وليس على الراوي.

- الفضل مرتب على الموضع من القرآن، والحديث الذي ورد فيه مصدر يُنقل عنه وليس موضعًا له.
- كثير مما يُروى في فضائل السور ضعيف أو موضوع، لذلك يُقيد كل فضل بمصدره ودرجته.

**مرتبط به:** <span dir="ltr">[`quran`](#quran)، [`surah`](#surah)، [`ayah`](#ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/136`

<a id="reflection"></a>

### التدبر — Reflection

<!-- source: standards/terminology/concepts/reflection.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`reflection`</span> |
| `plural` | <span dir="ltr">`reflections`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّدَبُّر |
| تهجئات أخرى | <span dir="ltr">`tadabur`، `waqfat_tadabburiyyah`</span> |

**التعريف:** التدبر هو التأمل في معاني القرآن وما يقتضيه من عمل، وما يقيده القارئ من وقفة عند آية أو لفظة.

**الغرض:** نستخدم التدبر محتوى يربط بآية أو بموضع منها. ونفصله عن التفسير لأنه لا يلتزم بيان المعنى الظاهر، ولأن قائله ليس بالضرورة مفسرًا.

- التفسير بيان لمعنى الآية على منهج، أما التدبر فهو أثر المعنى في المتدبر.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`tafsir`](#tafsir)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/29) — `29`

<a id="surah_name_reason"></a>

### سبب التسمية — Surah Name Reason

<!-- source: standards/terminology/concepts/surah_name_reason.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`surah_name_reason`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | سَبَب التَّسْمِيَة |
| تهجئات أخرى | <span dir="ltr">`sabab_al_tasmiya`</span> |

**التعريف:** سبب التسمية هو بيان العلة التي سميت بها السورة اسمها، وما ورد في ذلك من أثر أو وجه لغوي.

**الغرض:** نستخدم سبب التسمية محتوى يربط بالسورة. ونفصله عن سبب النزول لأنه يخص الاسم وليس النزول، ولأن كثيرًا من السور لها أكثر من اسم ولذلك أكثر من سبب تسمية.

- سبب التسمية يخص اسم السورة، وسبب النزول يخص نزول الآية.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`asbab_al_nuzul`](#asbab_al_nuzul)، [`surah_names`](#surah_names)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="surah_names"></a>

### أسماء السورة — Surah Names

<!-- source: standards/terminology/concepts/surah_names.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`surah_names`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | أَسْمَاء السُّورَة |
| تهجئات أخرى | <span dir="ltr">`asmaa_al_surah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Surah Names`</span> |

**التعريف:** أسماء السورة هي ما سميت به السورة من أسماء. وأكثر السور لها أكثر من اسم، منها ما ثبت بالأثر ومنها ما جرى به الاصطلاح.

**الغرض:** نستخدم أسماء السورة لحفظ كل ما تعرف به السورة من أسماء، لأن المصاحف تختلف في الاسم المثبت، ولأن البحث يحتاج أن يجد السورة بأي اسم من أسمائها.

- اسم السورة غير سبب تسميتها به.
- أسماء السورة غير أسماء القرآن نفسه.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`surah_name_reason`](#surah_name_reason)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="surah_objectives"></a>

### مقاصد السورة — Surah Objectives

<!-- source: standards/terminology/concepts/surah_objectives.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`surah_objectives`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَقَاصِد السُّورَة |
| تهجئات أخرى | <span dir="ltr">`maqasid`</span> |

**التعريف:** مقاصد السورة هي المعاني الكلية التي تدور عليها السورة ويجمع بينها موضوعها، وهي الغرض الواحد الذي تنتظم به آياتها.

**الغرض:** نستخدمها محتوى يُربط بالسورة كلها وليس بآية منها. وبذلك تتميز عن التفسير الذي يسير على الآيات آية آية، وعن الموضوعات التي تعدد ما ورد في السورة.

- المقصد غرض جامع للسورة، والموضوع واحد من الموضوعات التي وردت فيها.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`tafsir`](#tafsir)</span>

<a id="word_meanings"></a>

### غريب القرآن — Word Meanings

<!-- source: standards/terminology/concepts/word_meanings.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`word_meanings`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | غَرِيب القُرْآن |
| تهجئات أخرى | <span dir="ltr">`gharib`، `word_meaning`</span> |

**التعريف:** غريب القرآن هو بيان معاني الألفاظ القرآنية التي خفي معناها على أكثر القراء، لقلة استعمالها أو لتغير دلالتها.

**الغرض:** نستخدمه محتوى يُربط بكلمة بعينها من الآية وليس بالآية كلها، وبذلك يتميز عن التفسير الذي يفسر المعنى الكلي.

- غريب القرآن بيان لمعنى لفظة، والتفسير بيان لمعنى الآية.
- المعنى منسوب إلى كتاب بعينه، وقد يختلف بين المصادر.

**مرتبط به:** <span dir="ltr">[`word`](#word)، [`tafsir`](#tafsir)، [`ayah`](#ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `2/3`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/8`
