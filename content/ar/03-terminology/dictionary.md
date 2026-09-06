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
| [`alaqat_al_harfayn`](#alaqat_al_harfayn) | Alaqat al-Harfayn | علاقة الحرفين | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | نسبة الحرفين المتجاورين أحدهما إلى الآخر في المخرج والصفة: تماثل أو تجانس أو تقارب أو تباعد؛ وعليها يُبنى إدغام الأول في الثاني أو إظهاره. |
| [`asbab_al_nuzul`](#asbab_al_nuzul) | Asbab al-Nuzul | أسباب النزول | <span dir="ltr">`content`</span> | <span dir="ltr">`revelation`</span> | الحوادث أو الأسئلة التي نزلت آية أو آيات متحدثة عنها أو مبينة لحكم يتعلق بها. |
| [`asma_al_surah`](#asma_al_surah) | Asma al-Surah | أسماء السورة | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | ما سميت به السورة من أسماء، وأكثر السور لها أكثر من اسم، منها ما ثبت بالأثر ومنها ما جرى به الاصطلاح. |
| [`ayah`](#ayah) | Ayah | الآية | <span dir="ltr">`entity`</span> | <span dir="ltr">`structure`</span> | وحدة من النص القرآني تقع ضمن سورة ولها حدود محددة، وقد يختلف رقمها أو بعض حدودها باختلاف نظام عد الآي. |
| [`ayah_count`](#ayah_count) | Ayah Count | عدد الآيات | <span dir="ltr">`property`</span> | <span dir="ltr">`ayah_numbering`</span> | عدد آيات السورة في نظام عد بعينه، وقد يختلف من نظام إلى نظام باختلاف الفواصل المعدودة. |
| [`ayah_key`](#ayah_key) | Ayah Key |  | <span dir="ltr">`property`</span> | <span dir="ltr">`structure`</span> | معرف نصي للآية يجمع رقم سورتها ورقمها فيها مفصولين بنقطتين، على صورة `2:255`، ولا يُقرأ إلا في ضوء نظام عد الآي الذي يستند إليه. |
| [`ayah_mark`](#ayah_mark) | Ayah Mark | علامة الآية | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدَّارَة الفاصلة بين الآيتين، توضع عند نهاية الآية ويكتب فيها رقمها في أكثر المصاحف. |
| [`ayah_numbering_basri`](#ayah_numbering_basri) | Basri Numbering | العد البصري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل البصرة، المروي عن عاصم الجحدري عن أسلافه من أهل البصرة. |
| [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi) | Dimashqi Numbering | العد الدمشقي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل الشام، المروي عن يحيى بن الحارث الذماري عن ابن عامر، ويسمى العد الشامي. |
| [`ayah_numbering_kufi`](#ayah_numbering_kufi) | Kufi Numbering | العد الكوفي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل الكوفة، المروي عن حمزة الزيات عن ابن أبي ليلى عن أبي عبد الرحمن السلمي عن علي بن أبي طالب، وهو العد الذي يجري عليه أكثر المصاحف المطبوعة اليوم. |
| [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir) | Madani Akhir Numbering | العد المدني الأخير | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل المدينة في روايته الأخيرة، وهي رواية إسماعيل بن جعفر عن سليمان بن جماز. |
| [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal) | Madani Awwal Numbering | العد المدني الأول | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل المدينة في روايته الأولى، وهي رواية أبي جعفر يزيد بن القعقاع وشيبة بن نصاح. |
| [`ayah_numbering_makki`](#ayah_numbering_makki) | Makki Numbering | العد المكي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`ayah_numbering`</span> | عد أهل مكة، المروي عن ابن كثير عن مجاهد عن ابن عباس عن أبي بن كعب. |
| [`ayah_numbering_system`](#ayah_numbering_system) | Ayah Numbering System | نظام عد الآي | <span dir="ltr">`classification`</span> | <span dir="ltr">`ayah_numbering`</span> | نظام يحدد حدود الآيات وأعدادها وأرقامها وبعض المسائل المتعلقة بالبسملة وفق مدارس عد الآي. |
| [`ayah_timing`](#ayah_timing) | Ayah Timing |  | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل آية بعينها. |
| [`basmalah`](#basmalah) | Basmalah | البسملة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | صيغة «بسم الله الرحمن الرحيم» التي تفتتح بها السور عدا سورة التوبة، ولها أحكام واختلافات مرتبطة بعد الآي. |
| [`character`](#character) | Character |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | وحدة نصية مجردة في نظام تمثيل رقمي، ولا يلزم أن تطابق حرفًا لغويًا واحدًا. |
| [`codepoint`](#codepoint) | Codepoint |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | قيمة رقمية معرفة في معيار ترميز مثل `Unicode`. |
| [`dammah`](#dammah) | Dammah | الضمة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على حركة الحرف بالضم |
| [`disputed`](#disputed) | Disputed | مختلف فيه | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | ما اختلفت المصادر المعتمدة في تصنيفه بين المكي والمدني. |
| [`division_mark`](#division_mark) | Division Mark | علامة التقسيم | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على بداية الأجزاء والأحزاب وأنصافها وأرباعها |
| [`dot`](#dot) | Dot | النقطة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | نقطة واحدة فوق الحرف أو تحته تميزه عما يشاركه في الرسم، كالباء والنون والجيم والخاء والذال |
| [`equivalent_ayah`](#equivalent_ayah) | Equivalent Ayah | الآية المقابلة | <span dir="ltr">`concept`</span> | <span dir="ltr">`ayah_numbering`</span> | الآية في نظام عد تقابل آيةً في نظام آخر، سواء اتفق رقماهما أو اختلفا لاختلاف مواضع الفصل بين الآي. |
| [`fadail_al_quran`](#fadail_al_quran) | Fadail al-Quran | فضائل القرآن | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | ما ورد في فضل القرآن أو فضل سورة منه أو آية، وما يترتب على قراءتها من أجر أو أثر. |
| [`farsh`](#farsh) | Farsh | الفرش | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | ما اختلف فيه القراء من الكلمات في مواضع بأعيانها من السور، لا يطرد الخلاف فيه على قاعدة، بل يُذكر كل موضع بنفسه مرتبًا على السور. |
| [`fasilah`](#fasilah) | Fasilah | الفاصلة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | خاتمة الآية أو المقطع من جهة النظم، ويعرفها بعض العلماء بأنها الكلمة الأخيرة من الآية. |
| [`fathah`](#fathah) | Fathah | الفتحة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على حركة الحرف بالفتح |
| [`fil`](#fil) | Fil | الفعل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | ما دل على معنى في نفسه مقترن بزمان، ويتصرف بالماضي والمضارع والأمر. |
| [`font`](#font) | Font | الخط | <span dir="ltr">`concept`</span> | <span dir="ltr">`mushaf`</span> | ملف يحمل مجموعة من الأشكال المرسومة (`glyphs`) وقواعد إخراجها، يعرض به نص المصحف. |
| [`gharib_al_quran`](#gharib_al_quran) | Gharib al-Quran | غريب القرآن | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | بيان معاني الألفاظ القرآنية التي خفي معناها على أكثر القراء، لقلة دورانها في الاستعمال أو لتغير دلالتها. |
| [`ghunnah`](#ghunnah) | Ghunnah | الغنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | صوت يخرج من الخيشوم مركب في جسم النون والميم لا عمل للسان فيه، ويختلف مقداره بحسب الحكم: أكمل ما يكون في المشدد والمدغم، ثم في المخفى، ثم في الساكن المظهر. |
| [`glyph`](#glyph) | Glyph |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | الشكل البصري الذي ينتجه الخط لتمثيل حرف أو محرف أو مجموعة منها. |
| [`grapheme`](#grapheme) | Grapheme |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | وحدة كتابية يدركها المستخدم كوحدة واحدة، وقد تتكون من أكثر من `codepoint`. |
| [`hadr`](#hadr) | Hadr | الحدر | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | الإسراع في القراءة مع المحافظة على الحروف والحركات وأحكام الأداء دون إخلال. |
| [`hamzah`](#hamzah) | Hamzah | الهمزة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على همزة القطع المحققة |
| [`hamzat_al_wasl`](#hamzat_al_wasl) | Hamzat al-Wasl | همزة الوصل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على سقوط الهمزة وصلًا |
| [`harakah`](#harakah) | Harakah | الحركة | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | علامة تضبط حركة الحرف أو سكونه أو تشديده: الفتحة والضمة والكسرة والسكون والشدة. |
| [`harf_al_mana`](#harf_al_mana) | Harf al-Mana | حرف المعنى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | ما دل على معنى في غيره، كحروف الجر والعطف والنفي والاستفهام. |
| [`harf_muqatta`](#harf_muqatta) | Harf Muqatta | الحرف المقطع | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | حروف هجائية افتتحت بها بعض السور، مثل: الم، والر، وحم، وكهيعص. |
| [`hifz`](#hifz) | Hifz | الحفظ | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | استظهار القرآن كله أو بعضه عن ظهر قلب، على وجه يُتلى به من غير نظر في المصحف. |
| [`hizb`](#hizb) | Hizb | الحزب | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | في التقسيم المعاصر نصف جزء، فيكون القرآن ستين حزبًا. |
| [`hukm_al_tajwid`](#hukm_al_tajwid) | Hukm al-Tajwid | حكم التجويد | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | ما يجب في أداء الحرف عند حرف يليه أو عند سكون أو همز، من إظهار أو إدغام أو إقلاب أو إخفاء أو مد أو قلقلة أو تفخيم أو ترقيق، مما تقرره قواعد التجويد في موضع بعينه من النص. |
| [`huruf_muqattaah`](#huruf_muqattaah) | Huruf Muqattaah | الحروف المقطعة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | مجموعة الحروف الهجائية التي افتُتحت بها 29 سورة، تُقرأ بأسماء الحروف لا بمسمياتها، مثل «الم» و«كهيعص». |
| [`idgham`](#idgham) | Idgham | الإدغام | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | إدخال حرف ساكن في حرف متحرك بعده بحيث يصيران حرفًا واحدًا مشددًا، كاملًا كان الإدغام أو ناقصًا، بغنة أو بغير غنة. |
| [`ijam`](#ijam) | Ijam | الإعجام | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | النقط الذي يميز الحرف عما يشاركه في صورة الرسم. |
| [`ikhfa`](#ikhfa) | Ikhfa | الإخفاء | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | النطق بالحرف الساكن على صفة بين الإظهار والإدغام، عاريًا عن التشديد مع بقاء الغنة؛ حقيقيًّا في النون الساكنة والتنوين عند حروفه الخمسة عشر، وشفويًّا في الميم الساكنة عند الباء. |
| [`imalah`](#imalah) | Imalah | الإمالة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على الإمالة الكبرى: نطق الفتحة مائلة إلى الكسرة، وهي في رواية حفص في موضع واحد (11:41) |
| [`instructional_ayah_repetition`](#instructional_ayah_repetition) | Instructional Ayah Repetition | تكرار الآيات | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation_style`</span> | إعادة آية أو جزء منها مرة أو مرات وفق نمط تعليمي يساعد على التلقي والحفظ. |
| [`iqlab`](#iqlab) | Iqlab | الإقلاب | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | قلب النون الساكنة أو التنوين ميمًا مخفاة بغنة عند الباء. |
| [`irab`](#irab) | Irab | الإعراب | <span dir="ltr">`analysis`</span> | <span dir="ltr">`linguistics`</span> | بيان الوظائف النحوية للكلمات وعلاماتها وعلاقاتها في التركيب. |
| [`ishmam`](#ishmam) | Ishmam | الإشمام | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على الإشمام: ضم الشفتين إشارة إلى الضمة المحذوفة من غير صوت |
| [`ism`](#ism) | Ism | الاسم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`linguistics`</span> | ما دل على معنى في نفسه غير مقترن بزمان، وتدخل فيه الأسماء والصفات والضمائر وأسماء الإشارة والموصولات. |
| [`istiadhah`](#istiadhah) | Istiadhah | الاستعاذة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | طلب العوذ بالله من الشيطان عند إرادة تلاوة القرآن. |
| [`izhar`](#izhar) | Izhar | الإظهار | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | إخراج الحرف الساكن من مخرجه من غير غنة زائدة فيه، كإظهار النون الساكنة والتنوين عند حروف الحلق، وإظهار الميم الساكنة عند غير الباء والميم. |
| [`juz`](#juz) | Juz | الجزء | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | واحد من ثلاثين قسمًا في التقسيم المشهور للمصحف لتيسير القراءة والختم. |
| [`kasrah`](#kasrah) | Kasrah | الكسرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على حركة الحرف بالكسر |
| [`khatmah`](#khatmah) | Khatmah | الختمة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | قراءة القرآن كاملًا من أوله إلى آخره. |
| [`lahn`](#lahn) | Lahn | اللحن | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | الخطأ في قراءة القرآن والميل بها عن الصواب، جليًّا كان أو خفيًّا. |
| [`lahn_jali`](#lahn_jali) | Lahn Jali | اللحن الجلي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | خطأ يطرأ على اللفظ فيخل بالمبنى أو المعنى، كإبدال حرف بحرف أو حركة بحركة، ويدركه العالم وغيره. |
| [`lahn_khafi`](#lahn_khafi) | Lahn Khafi | اللحن الخفي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | خطأ يطرأ على اللفظ فيخل بكمال الأداء دون المبنى والمعنى، كترك الغنة أو تقصير المد، ولا يدركه إلا أهل الفن. |
| [`layout`](#layout) | Layout | التخطيط | <span dir="ltr">`concept`</span> | <span dir="ltr">`mushaf`</span> | تنظيم النص والعناصر بصريًا إلى صفحات وأسطر ومواضع ضمن مصحف أو عرض معين. |
| [`lemma`](#lemma) | Lemma |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الصيغة المعجمية الأساسية التي ترد إليها صورة الكلمة المصرفة. |
| [`letter`](#letter) | Letter | الحرف | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | حرف هجائي بوصفه وحدة لغوية من وحدات الكتابة. |
| [`line`](#line) | Line | السطر | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | سطر طباعي داخل صفحة مصحف أو تخطيط معين. |
| [`madani`](#madani) | Madani | مدني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | ما نزل من القرآن بعد الهجرة، ولو نزل خارج المدينة. |
| [`madd`](#madd) | Madd | المد | <span dir="ltr">`classification`</span> | <span dir="ltr">`tajwid`</span> | إطالة الصوت بحرف من حروف المد الثلاثة: الألف الساكنة بعد فتح، والواو الساكنة بعد ضم، والياء الساكنة بعد كسر؛ أصليًّا كان المد لا يقوم الحرف إلا به، أو فرعيًّا بسبب همز أو سكون. |
| [`madd_al_badal`](#madd_al_badal) | Madd al-Badal | مد البدل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد سببه همزة قبل حرف المد، أُبدل فيه حرف المد من همزة ساكنة، كما في «آمن» و«أوتوا» و«إيمان»؛ ومقداره حركتان عند حفص، ويُزاد عند ورش. |
| [`madd_al_iwad`](#madd_al_iwad) | Madd al-Iwad | مد العوض | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد الألف عوضًا عن تنوين الفتح عند الوقف على الكلمة، ومقداره حركتان. |
| [`madd_al_lin`](#madd_al_lin) | Madd al-Lin | مد اللين | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد الواو أو الياء الساكنة المفتوح ما قبلها عند الوقف على الكلمة بسكون عارض، كما في «خوف» و«بيت». |
| [`madd_al_silah`](#madd_al_silah) | Madd al-Silah | مد الصلة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد ناشئ عن صلة هاء الضمير بواو أو ياء إذا وقعت بين متحركين؛ صغرى إن لم يقع بعدها همز، وكبرى إن وقع. |
| [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun) | Madd Arid lil-Sukun | المد العارض للسكون | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد سببه سكون عارض في الوقف بعد حرف المد، ويجوز فيه القصر والتوسط والطول. |
| [`madd_lazim`](#madd_lazim) | Madd Lazim | المد اللازم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد فرعي سببه سكون أصلي ثابت وصلًا ووقفًا بعد حرف المد، في كلمة أو في حرف من فواتح السور، مثقلًا كان بالإدغام أو مخففًا؛ ومقداره ست حركات. |
| [`madd_munfasil`](#madd_munfasil) | Madd Munfasil | المد المنفصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد فرعي سببه همزة في أول الكلمة التالية لحرف المد، وهو جائز: يُقصر ويُمد بحسب الرواية والطريق. |
| [`madd_muttasil`](#madd_muttasil) | Madd Muttasil | المد المتصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | مد فرعي سببه همزة بعد حرف المد في كلمة واحدة، وهو واجب عند القراء جميعًا، وتختلف مقاديره بحسب الرواية والطريق. |
| [`madd_tabii`](#madd_tabii) | Madd Tabee | المد الطبيعي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | المد الذي لا تقوم ذات حرف المد إلا به، ولا يتوقف على سبب من همز أو سكون، ومقداره حركتان. |
| [`maddah`](#maddah) | Maddah | المدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على لزوم مد الحرف مدًّا زائدًا على المد الطبيعي |
| [`makhraj`](#makhraj) | Makhraj | المخرج | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | موضع خروج الحرف الذي يتميز به عن غيره، من الجوف أو الحلق أو اللسان أو الشفتين أو الخيشوم. |
| [`makki`](#makki) | Makki | مكي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`revelation`</span> | ما نزل من القرآن قبل الهجرة، ولو نزل خارج مكة. |
| [`manzil`](#manzil) | Manzil | المنزل | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | واحد من سبعة أقسام تقليدية للقرآن لتيسير ختمه في أسبوع. |
| [`maqasid_al_surah`](#maqasid_al_surah) | Maqasid al-Surah | مقاصد السورة | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | المعاني الكلية التي تدور عليها السورة ويجمع بينها موضوعها، وما تنتظم به آياتها من غرض واحد. |
| [`maqta_al_ayah`](#maqta_al_ayah) | Maqta al-Ayah | مقطع الآية | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | ما ظهر من آية واحدة في سطر واحد من صفحة مصحف بعينه؛ فالآية التي تمتد على سطرين مقطعان. |
| [`mathani`](#mathani) | Mathani | المثاني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | السور التي تقصر عن المئين وتليها في التقسيم التقليدي، وسميت مثاني لكثرة ما تثنى، أي تكرر قراءتها. |
| [`mawdi_al_sajdah`](#mawdi_al_sajdah) | Mawdi al-Sajdah | موضع السجدة | <span dir="ltr">`concept`</span> | <span dir="ltr">`structure`</span> | الموضع من النص الذي يسجد عنده القارئ، وينتهي بآية بعينها، ومواضعه معدودة مختلف في عد بعضها. |
| [`meem_sakinah`](#meem_sakinah) | Meem Sakinah | الميم الساكنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | ميم خالية من الحركة، ثابتة لفظًا وخطًّا، تقع في وسط الكلمة أو آخرها. |
| [`miun`](#miun) | Miun | المئون | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | السور التي تقارب آياتها المئة أو تزيد عليها أو تنقص عنها قليلًا. |
| [`morpheme`](#morpheme) | Morpheme | الوحدة الصرفية | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | أصغر وحدة في الكلمة تحمل معنى أو وظيفة صرفية، كالسابقة واللاحقة والجذع. |
| [`morphology`](#morphology) | Morphology | الصرف | <span dir="ltr">`analysis`</span> | <span dir="ltr">`linguistics`</span> | تحليل بنية الكلمة وصيغتها وما تحمله من خصائص صرفية. |
| [`muallim`](#muallim) | Muallim | معلم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | نمط تلاوة معد للتعليم وقد يتضمن تكرار الآيات أو إتاحة وقت للمتعلم للترديد. |
| [`mufassal`](#mufassal) | Mufassal | المفصل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | مجموعة من قصار السور التي تلي المثاني، مع اختلاف العلماء في أولها. |
| [`mufassir`](#mufassir) | Mufassir | المفسر | <span dir="ltr">`role`</span> | <span dir="ltr">`tafsir`</span> | من نسب إليه تفسير للقرآن، تأليفًا أو رواية. |
| [`mujawwad`](#mujawwad) | Mujawwad | مجود | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | نمط أداء بطيء يمد فيه الصوت وتستوفى أحكام التجويد بتطريب، وهو الوصف الذي تنشر به التسجيلات المؤداة على هذا النحو. |
| [`muqri`](#muqri) | Muqri | المقرئ | <span dir="ltr">`role`</span> | <span dir="ltr">`qiraat`</span> | من تلقى القراءة وأتقنها وينقلها للمتعلمين. |
| [`murattal`](#murattal) | Murattal | مرتل | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_style`</span> | نمط أداء متزن دون تطريب، على مرتبة الترتيل، وهو الوصف الذي تنشر به التسجيلات المؤداة على هذا النحو. |
| [`mushaf`](#mushaf) | Mushaf | المصحف | <span dir="ltr">`entity`</span> | <span dir="ltr">`core`</span> | الصحف التي جمع فيها القرآن مكتوبًا ومرتبًا على ترتيبه المعروف. |
| [`mushaf_edition`](#mushaf_edition) | Mushaf Edition | طبعة المصحف | <span dir="ltr">`entity`</span> | <span dir="ltr">`core`</span> | إصدار منشور محدد من المصحف له خصائص محددة من الناشر والرسم والضبط والتخطيط وغيرها. |
| [`mushaf_mark`](#mushaf_mark) | Mushaf Mark | علامة المصحف | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | رمز أو علامة غير داخلة في الحروف الأصلية للكلمة، تستخدم في المصحف لأغراض القراءة أو التنظيم أو الإرشاد. |
| [`mutabaidan`](#mutabaidan) | Mutabaidan | المتباعدان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | حرفان تباعدا مخرجًا واختلفا صفة، ولا إدغام بينهما. |
| [`mutajanisan`](#mutajanisan) | Mutajanisan | المتجانسان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | حرفان اتحدا مخرجًا واختلفا صفة، كالدال والتاء في «قد تبين». |
| [`mutamathilan`](#mutamathilan) | Mutamathilan | المتماثلان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | حرفان اتحدا مخرجًا وصفة، كالباء في «اضرب بعصاك». |
| [`mutaqariban`](#mutaqariban) | Mutaqariban | المتقاربان | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | حرفان تقاربا مخرجًا أو صفة أو فيهما معًا، كاللام والراء في «قل رب». |
| [`mutashabihat`](#mutashabihat) | Mutashabihat | المتشابهات | <span dir="ltr">`analysis`</span> | <span dir="ltr">`quranic_sciences`</span> | المواضع التي يتشابه فيها لفظ الآيات أو أجزاؤها في القرآن، تشابهًا تامًّا أو مع اختلاف يسير في كلمة أو ترتيب. |
| [`naskh`](#naskh) | Naskh | النسخ | <span dir="ltr">`concept`</span> | <span dir="ltr">`quranic_sciences`</span> | رفع حكم شرعي بدليل شرعي متأخر عنه، ويبحث في القرآن بنسبة الآية الناسخة إلى الآية المنسوخة. |
| [`noon_sakinah`](#noon_sakinah) | Noon Sakinah | النون الساكنة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | نون خالية من الحركة، تثبت لفظًا وخطًا ووصلًا ووقفًا. |
| [`nuzul`](#nuzul) | Nuzul | النزول | <span dir="ltr">`concept`</span> | <span dir="ltr">`revelation`</span> | إنزال القرآن على النبي صلى الله عليه وسلم منجمًا في مدة الرسالة، على حسب الوقائع والحاجة. |
| [`omitted_alif`](#omitted_alif) | Omitted Alif | الألف المحذوفة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على ألف محذوفة من الرسم واجبة النطق |
| [`orthographic_mark`](#orthographic_mark) | Orthographic Mark | العلامة الإملائية | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | علامة تضبط رسم الكلمة، كالهمزة والمدة والحروف الصغيرة. |
| [`page`](#page) | Page | الصفحة | <span dir="ltr">`unit`</span> | <span dir="ltr">`mushaf`</span> | وحدة طباعية من تخطيط مصحف معين، وقد يختلف محتواها وحدودها باختلاف المصحف أو الطبعة. |
| [`part_of_speech`](#part_of_speech) | Part of Speech | قسم الكلمة | <span dir="ltr">`classification`</span> | <span dir="ltr">`linguistics`</span> | تصنيف الكلمة أو الوحدة الصرفية بحسب بابها النحوي، كالاسم والفعل والحرف وما يتفرع عنها. |
| [`qalqalah`](#qalqalah) | Qalqalah | القلقلة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`tajwid`</span> | اضطراب في صوت الحرف الساكن عند النطق به حتى تُسمع له نبرة قوية، في حروف «قطب جد»، ويقوى بحسب موضع الحرف من الكلمة والوقف عليه. |
| [`qiraah`](#qiraah) | Qiraah | القراءة | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | وجه من وجوه قراءة القرآن ينسب إلى إمام من أئمة القراءات وتتفرع عنه الروايات والطرق. |
| [`qiraah_mark`](#qiraah_mark) | Qiraah Mark | علامة القراءة | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | علامة ترشد إلى وجه من وجوه الأداء في موضعها، كالسكت والإشمام والتسهيل. |
| [`quran`](#quran) | Quran | القرآن | <span dir="ltr">`concept`</span> | <span dir="ltr">`core`</span> | كلام الله المنزل على محمد صلى الله عليه وسلم والمتعبد بتلاوته، ويطلق على مجموعه وعلى بعضه بحسب السياق. |
| [`rasm`](#rasm) | Rasm | الرسم | <span dir="ltr">`classification`</span> | <span dir="ltr">`mushaf`</span> | طريقة كتابة ألفاظ القرآن من حيث إثبات الحروف وحذفها وزيادتها وفصلها ووصلها ونحو ذلك. |
| [`rasm_imlai`](#rasm_imlai) | Rasm Imlai | الرسم الإملائي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`mushaf`</span> | كتابة ألفاظ القرآن على قواعد الإملاء المعاصرة، بإثبات ما يُحذف في الرسم العثماني وحذف ما يُزاد فيه، لتُقرأ على صورتها المألوفة. |
| [`rasm_uthmani`](#rasm_uthmani) | Rasm Uthmani | الرسم العثماني | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`mushaf`</span> | طريقة كتابة كلمات المصاحف العثمانية وما يتعلق بها من حذف وزيادة وبدل وفصل ووصل. |
| [`rawi`](#rawi) | Rawi | الراوي | <span dir="ltr">`role`</span> | <span dir="ltr">`qiraat`</span> | من نسبت إليه الرواية عن إمام القراءة. |
| [`recitation`](#recitation) | Recitation | تسجيل التلاوة | <span dir="ltr">`entity`</span> | <span dir="ltr">`recitation`</span> | تسجيل منشور لتلاوة القرآن، منسوب إلى قارئ ورواية ونمط أداء. |
| [`recitation_pace`](#recitation_pace) | Recitation Pace | مراتب القراءة | <span dir="ltr">`classification`</span> | <span dir="ltr">`recitation_pace`</span> | تصنيف لسرعة أداء القراءة مع المحافظة على أحكامها. |
| [`recitation_style`](#recitation_style) | Recitation Style | نمط الأداء | <span dir="ltr">`classification`</span> | <span dir="ltr">`recitation_style`</span> | تصنيف للتسجيلات والتلاوات بحسب طريقة أدائها: مرتل أو مجود أو معلم، مستقل عن القراءة والرواية. |
| [`reciter`](#reciter) | Reciter | القارئ | <span dir="ltr">`role`</span> | <span dir="ltr">`recitation`</span> | الشخص الذي يؤدي تلاوة القرآن. |
| [`rectangular_zero`](#rectangular_zero) | Rectangular Zero | الصفر المستطيل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على زيادة الألف وصلًا لا وقفًا؛ فتنطق عند الوقف عليها |
| [`revelation_classification`](#revelation_classification) | Revelation Classification | تصنيف النزول | <span dir="ltr">`classification`</span> | <span dir="ltr">`revelation`</span> | تصنيف للنص القرآني بحسب وقوع نزوله قبل الهجرة أو بعدها وفق الاصطلاح المعتمد. |
| [`revelation_order`](#revelation_order) | Revelation Order | ترتيب النزول | <span dir="ltr">`property`</span> | <span dir="ltr">`revelation`</span> | ترتيب السور أو الآيات بحسب زمن نزولها، وقد يختلف بحسب المصدر المعتمد. |
| [`riwayah`](#riwayah) | Riwayah | الرواية | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | ما ينسب إلى راو عن إمام القراءة؛ مثل رواية حفص عن عاصم. |
| [`root`](#root) | Root | الجذر | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | الأصل الصرفي الذي ترد إليه الكلمة لبيان اشتقاقها وصلتها بالكلمات الأخرى. |
| [`rounded_zero`](#rounded_zero) | Rounded Zero | الصفر المستدير | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على زيادة الحرف رسمًا؛ فلا ينطق وصلًا ولا وقفًا |
| [`rubu_al_hizb`](#rubu_al_hizb) | Rubu al-Hizb | ربع الحزب | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | ربع الحزب في التقسيم المشهور للمصحف. |
| [`ruku`](#ruku) | Ruku | الركوع | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | قسم اصطلاحي من القرآن يستخدم لتنظيم القراءة ويظهر في بعض المصاحف. |
| [`saba_tiwal`](#saba_tiwal) | Saba Tiwal | السبع الطوال | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`surah_classification`</span> | مجموعة من أطول سور القرآن في أوله، مع خلاف معروف في تعيين السورة السابعة. |
| [`sabab_al_tasmiyah`](#sabab_al_tasmiyah) | Sabab al-Tasmiyah | سبب التسمية | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | بيان العلة التي سميت بها السورة اسمها، وما ورد في ذلك من أثر أو وجه لغوي. |
| [`sabab_al_waqf`](#sabab_al_waqf) | Sabab al-Waqf | سبب الوقف | <span dir="ltr">`classification`</span> | <span dir="ltr">`waqf`</span> | تقسيم الوقف باعتبار ما دعا القارئ إليه: اضطرار، أو اختبار، أو انتظار، أو اختيار. |
| [`sajdah_line`](#sajdah_line) | Sajdah Line | خط السجدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على الكلمة الموجبة للسجدة |
| [`sajdah_mark`](#sajdah_mark) | Sajdah Mark | علامة السجدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على موضع السجود |
| [`saktah`](#saktah) | Saktah | السكتة | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | قطع الصوت زمنًا يسيرًا من غير تنفس ثم متابعة القراءة. |
| [`saktah_mark`](#saktah_mark) | Saktah Mark | علامة السكتة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على السكت: وقفة يسيرة من غير تنفس ثم الوصل بما بعده |
| [`seen_al_qiraah`](#seen_al_qiraah) | Seen al-Qiraah | سين القراءة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | السين فوق الصاد تدل على القراءة بالسين، والسين تحتها تدل على القراءة بالصاد |
| [`shaddah`](#shaddah) | Shaddah | الشدة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على تشديد الحرف بإدغام الأول الساكن في الثاني المتحرك، فينطقان حرفًا واحدًا مشددًا |
| [`sifat_al_huruf`](#sifat_al_huruf) | Sifat al-Huruf | صفات الحروف | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | كيفيات تعرض للحرف عند النطق به فتميزه عن مشاركه في المخرج؛ منها ما له ضد كالهمس والجهر والشدة والرخاوة، ومنها ما لا ضد له كالصفير والقلقلة. |
| [`small_meem`](#small_meem) | Small Meem | الميم الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على قلب النون الساكنة أو التنوين ميمًا عند الباء |
| [`small_noon`](#small_noon) | Small Noon | النون الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على نون محذوفة من الرسم واجبة النطق، في موضع واحد (21:88) وحده |
| [`small_waw`](#small_waw) | Small Waw | الواو الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على صلة هاء الضمير المضمومة بواو لفظية في حال الوصل |
| [`small_yaa`](#small_yaa) | Small Yaa | الياء الصغيرة | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على صلة هاء الضمير المكسورة بياء لفظية في حال الوصل |
| [`spoken_translation`](#spoken_translation) | Spoken Translation | الترجمة المنطوقة | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | نقل معاني القرآن إلى لغة أخرى في مادة صوتية أو منطوقة. |
| [`stem`](#stem) | Stem | الجذع | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | ما يبقى من الكلمة بعد نزع السوابق واللواحق، وتلحق به الزوائد الصرفية. |
| [`sujud_al_tilawah`](#sujud_al_tilawah) | Sujud al-Tilawah | سجود التلاوة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | سجدة تؤدى عند قراءة أو سماع موضع من مواضع سجود التلاوة. |
| [`sukun`](#sukun) | Sukun | السكون | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على سكون الحرف وإظهاره |
| [`surah`](#surah) | Surah | السورة | <span dir="ltr">`entity`</span> | <span dir="ltr">`structure`</span> | وحدة رئيسية من بنية القرآن، تتكون من آيات مرتبة ولها اسم وموضع معروف في ترتيب المصحف. |
| [`surah_group`](#surah_group) | Surah Group | تصنيف السور | <span dir="ltr">`classification`</span> | <span dir="ltr">`surah_classification`</span> | تصنيف يجمع سورًا وفق تقسيمات اصطلاحية موروثة تعتمد الطول أو موضعها ضمن مجموعات السور. |
| [`tadabbur`](#tadabbur) | Tadabbur | التدبر | <span dir="ltr">`content`</span> | <span dir="ltr">`quranic_sciences`</span> | التأمل في معاني القرآن وما يقتضيه من عمل، وما يقيده القارئ من وقفة عند آية أو لفظة. |
| [`tadwir`](#tadwir) | Tadwir | التدوير | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | القراءة بسرعة متوسطة بين التحقيق والحدر مع المحافظة على الأحكام. |
| [`tafkhim`](#tafkhim) | Tafkhim | التفخيم | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | سِمَن يدخل على صوت الحرف فيمتلئ الفم بصداه؛ لازم في حروف الاستعلاء، وعارض في الراء ولام لفظ الجلالة والألف تبعًا لما قبلها. |
| [`tafsir`](#tafsir) | Tafsir | التفسير | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | بيان معاني القرآن وشرح ألفاظه وما يرشد إليه من أحكام وهدايات بحسب أصول التفسير. |
| [`tafsir_al_ray`](#tafsir_al_ray) | Tafsir al-Ray | تفسير الرأي | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | بيان معاني القرآن بالاجتهاد والنظر بعد معرفة كلام العرب وأساليبه وأصول التفسير، محمودًا كان الاجتهاد أو مذمومًا. |
| [`tafsir_mathur`](#tafsir_mathur) | Tafsir Mathur | التفسير المأثور | <span dir="ltr">`content`</span> | <span dir="ltr">`tafsir`</span> | ما فسر به القرآن من القرآن نفسه، أو من السنة، أو من قول الصحابة والتابعين، منقولًا بإسناده. |
| [`tahqiq`](#tahqiq) | Tahqiq | التحقيق | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`recitation_pace`</span> | القراءة ببطء وتؤدة مع استيفاء الحروف وأحكامها، وتستخدم كثيرًا في مقام التعليم. |
| [`tajwid`](#tajwid) | Tajweed | التجويد | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | علم أداء حروف القرآن من مخارجها وإعطائها حقوقها ومستحقاتها من الصفات والأحكام. |
| [`takbir`](#takbir) | Takbir | التكبير | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | قول «الله أكبر» بين السور، من آخر «الضحى» إلى آخر «الناس»، مرويًّا عن أهل مكة في رواية البزي عن ابن كثير، ويُفعل عند الختم على غيرها. |
| [`tanwin`](#tanwin) | Tanwin | التنوين | <span dir="ltr">`classification`</span> | <span dir="ltr">`dabt`</span> | نون ساكنة زائدة تلحق آخر الاسم، وترسم بتكرار صورة الحركة. |
| [`tanwin_al_damm`](#tanwin_al_damm) | Tanwin al-Damm | تنوين الضم | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على التنوين المرفوع. |
| [`tanwin_al_fath`](#tanwin_al_fath) | Tanwin al-Fath | تنوين الفتح | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على التنوين المنصوب. |
| [`tanwin_al_kasr`](#tanwin_al_kasr) | Tanwin al-Kasr | تنوين الكسر | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على التنوين المخفوض. |
| [`tariq`](#tariq) | Tariq | الطريق | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | وجه النقل المأخوذ عن الراوي بواسطة من دونه في سلسلة نقل القراءة. |
| [`tarqiq`](#tarqiq) | Tarqiq | الترقيق | <span dir="ltr">`concept`</span> | <span dir="ltr">`tajwid`</span> | نحول يدخل على صوت الحرف فلا يمتلئ الفم بصداه؛ لازم في حروف الاستفال، وعارض في الراء ولام لفظ الجلالة. |
| [`tartib_al_mushaf`](#tartib_al_mushaf) | Tartib al-Mushaf | ترتيب المصحف | <span dir="ltr">`property`</span> | <span dir="ltr">`structure`</span> | ترتيب السور كما استقر عليه المصحف العثماني، من الفاتحة إلى الناس، وهو الترتيب الذي تُرقم به السور. |
| [`tartil`](#tartil) | Tartil | الترتيل | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | قراءة القرآن بتؤدة وبيان للحروف والكلمات ومراعاة الوقف والمعنى. |
| [`tashil`](#tashil) | Tashil | التسهيل | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | الدلالة على تسهيل الهمزة بين بين، أي بينها وبين الألف |
| [`tashkil`](#tashkil) | Tashkil | التشكيل | <span dir="ltr">`concept`</span> | <span dir="ltr">`dabt`</span> | طبقة علامات الضبط الملحقة بحروف النص، من الحركات والتنوين والشدة والسكون وما يتبعها، منظورًا إليها جملةً. |
| [`three_dots`](#three_dots) | Three Dots | الثلاث نقط | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | ثلاث نقاط فوق الحرف تميزه عما يشاركه في الرسم، كالثاء والشين |
| [`thumn`](#thumn) | Thumn | الثمن | <span dir="ltr">`entity`</span> | <span dir="ltr">`divisions`</span> | ثمن الحزب، وهو تقسيم مستخدم في بعض المصاحف والمدارس. |
| [`tilawah`](#tilawah) | Tilawah | التلاوة | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | قراءة القرآن بلفظه أداءً بالصوت على ما تلقاه القارئ، في صلاة كانت أو درس أو تسجيل. |
| [`token`](#token) | Token |  | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | وحدة ينتجها تقسيم النص وفق منهج معلن، وقد تطابق الكلمة، وقد تكون جزءًا منها، وقد تجمع أكثر من كلمة. |
| [`translation`](#translation) | Translation | الترجمة | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | نقل معاني القرآن إلى لغة أخرى، وليست الترجمة قرآنًا بلفظه. |
| [`translator`](#translator) | Translator | المترجم | <span dir="ltr">`role`</span> | <span dir="ltr">`translation`</span> | من نُسبت إليه ترجمة لمعاني القرآن إلى لغة أخرى، فردًا كان أو هيئة. |
| [`transliteration`](#transliteration) | Transliteration | النقل الحرفي | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | تمثيل حروف نظام كتابي بحروف نظام آخر وفق قواعد محددة، دون ترجمة المعنى. |
| [`two_dots`](#two_dots) | Two Dots | النقطتان | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | نقطتان فوق الحرف أو تحته تميزانه عما يشاركه في الرسم، كالتاء والياء والقاف |
| [`usul`](#usul) | Usul | الأصول | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | القواعد المطردة في القراءة التي يجري عليها كل ما تحقق فيه شرطها، كالمد والهمز والإمالة والإدغام وهاء الكناية. |
| [`wajh`](#wajh) | Wajh | الوجه | <span dir="ltr">`concept`</span> | <span dir="ltr">`qiraat`</span> | كيفية من كيفيات الأداء يجوز الأخذ بأي منها في الرواية الواحدة أو الطريق الواحد، كأوجه المد العارض للسكون. |
| [`waqf`](#waqf) | Waqf | الوقف | <span dir="ltr">`concept`</span> | <span dir="ltr">`waqf`</span> | قطع القراءة عند موضع من النص وفق أحكام الوقف والابتداء. |
| [`waqf_al_muanaqah`](#waqf_al_muanaqah) | Waqf al-Muanaqah | وقف المعانقة | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | موضعان للوقف، إذا وقف على أحدهما لم يصح الوقف على الآخر |
| [`waqf_hasan`](#waqf_hasan) | Waqf Hasan | الوقف الحسن | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما أفاد معنًى وتعلق بما بعده لفظًا ومعنًى. |
| [`waqf_idtirari`](#waqf_idtirari) | Waqf Idtirari | الوقف الاضطراري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما يعرض للقارئ بسبب يضطره إلى الوقف، من ضيق نفس أو عطاس أو نسيان، فيقف على أي كلمة ثم يبتدئ بما يصح الابتداء به. |
| [`waqf_ikhtibari`](#waqf_ikhtibari) | Waqf Ikhtibari | الوقف الاختباري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما يقع لبيان المقطوع والموصول والثابت والمحذوف من الرسم، عند سؤال أو تعليم. |
| [`waqf_ikhtiyari`](#waqf_ikhtiyari) | Waqf Ikhtiyari | الوقف الاختياري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما يقصده القارئ باختياره من غير سبب يعرض، وهو الذي تجري عليه أحكام التام والكافي والحسن والقبيح. |
| [`waqf_intizari`](#waqf_intizari) | Waqf Intizari | الوقف الانتظاري | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما يقع على الكلمة التي فيها خلاف بين القراءات، ليستوفي القارئ أوجهها عند جمع القراءات. |
| [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn) | Waqf Jaiz Mustawi al-Tarafayn | الوقف الجائز مستوي الطرفين | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف جائز جوازًا مستوي الطرفين، فالوقف والوصل سواء |
| [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla) | Waqf Jaiz Waqf Awla | الوقف الجائز مع كون الوقف أولى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف جائز مع كون الوقف أولى |
| [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla) | Waqf Jaiz Wasl Awla | الوقف الجائز مع كون الوصل أولى | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف جائز مع كون الوصل أولى |
| [`waqf_kafi`](#waqf_kafi) | Waqf Kafi | الوقف الكافي | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما تم معناه وتعلق بما بعده معنًى لا لفظًا. |
| [`waqf_lazim`](#waqf_lazim) | Waqf Lazim | الوقف اللازم | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف لازم، لأن وصل ما بعده بما قبله يوهم خلاف المعنى المراد |
| [`waqf_mamnu`](#waqf_mamnu) | Waqf Mamnu | الوقف الممنوع | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`dabt`</span> | الوقف ممنوع، لأن الوقف على الموضع يفسد المعنى أو يقطع ما لا ينفصل عما بعده |
| [`waqf_mark`](#waqf_mark) | Waqf Mark | علامة الوقف | <span dir="ltr">`mark`</span> | <span dir="ltr">`dabt`</span> | علامة في المصحف ترشد القارئ إلى حكم الوقف أو الوصل في موضع معين. |
| [`waqf_mark_type`](#waqf_mark_type) | Waqf Mark Type | نوع علامة الوقف | <span dir="ltr">`classification`</span> | <span dir="ltr">`waqf`</span> | تصنيف لما ترشد إليه علامة الوقف المرسومة في المصحف من لزوم أو منع أو جواز. |
| [`waqf_qabih`](#waqf_qabih) | Waqf Qabih | الوقف القبيح | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما لم يفد معنًى، أو أفاد معنًى غير مراد. |
| [`waqf_ruling`](#waqf_ruling) | Waqf Ruling | حكم الوقف | <span dir="ltr">`classification`</span> | <span dir="ltr">`waqf`</span> | تصنيف الموضع نفسه من جهة تمام المعنى عنده، لا من جهة العلامة المرسومة عليه. |
| [`waqf_tamm`](#waqf_tamm) | Waqf Tamm | الوقف التام | <span dir="ltr">`classification_value`</span> | <span dir="ltr">`waqf`</span> | ما تم معناه ولم يتعلق بما بعده لفظًا ولا معنًى. |
| [`wazn`](#wazn) | Wazn | الوزن | <span dir="ltr">`unit`</span> | <span dir="ltr">`linguistics`</span> | صورة الكلمة الصرفية ممثلةً بحروف «فعل» وما يلحقها من زوائد، تبين بناءها بصرف النظر عن جذرها. |
| [`word`](#word) | Word | الكلمة | <span dir="ltr">`unit`</span> | <span dir="ltr">`text`</span> | وحدة من النص يعرفها القارئ كلمة واحدة، ولا يتغير عدها بتغير منهج تقسيم النص. |
| [`word_by_word_translation`](#word_by_word_translation) | Word by Word Translation |  | <span dir="ltr">`content`</span> | <span dir="ltr">`translation`</span> | ترجمة تعطي كل كلمة من كلمات الآية معناها في لغة أخرى على حدة، بترتيب كلمات الأصل. |
| [`word_key`](#word_key) | Word Key |  | <span dir="ltr">`property`</span> | <span dir="ltr">`structure`</span> | معرف نصي للكلمة يضيف إلى مفتاح الآية موضع الكلمة فيها، على صورة `2:255:5`، وموضع الكلمة يُعد من أول الآية بحسب منهج تقسيم معلن. |
| [`word_timing`](#word_timing) | Word Timing |  | <span dir="ltr">`concept`</span> | <span dir="ltr">`recitation`</span> | مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل كلمة بعينها من آية. |

## حسب المجال

- **الأساس** — `core`: <span dir="ltr">[`mushaf`](#mushaf)، [`mushaf_edition`](#mushaf_edition)، [`quran`](#quran)</span>
- **البنية** — `structure`: <span dir="ltr">[`ayah`](#ayah)، [`ayah_key`](#ayah_key)، [`basmalah`](#basmalah)، [`fasilah`](#fasilah)، [`harf_muqatta`](#harf_muqatta)، [`huruf_muqattaah`](#huruf_muqattaah)، [`mawdi_al_sajdah`](#mawdi_al_sajdah)، [`surah`](#surah)، [`tartib_al_mushaf`](#tartib_al_mushaf)، [`word_key`](#word_key)</span>
- **النص** — `text`: <span dir="ltr">[`character`](#character)، [`codepoint`](#codepoint)، [`glyph`](#glyph)، [`grapheme`](#grapheme)، [`letter`](#letter)، [`token`](#token)، [`word`](#word)</span>
- **أقسام القرآن** — `divisions`: <span dir="ltr">[`hizb`](#hizb)، [`juz`](#juz)، [`manzil`](#manzil)، [`rubu_al_hizb`](#rubu_al_hizb)، [`ruku`](#ruku)، [`thumn`](#thumn)</span>
- **تصنيف السور** — `surah_classification`: <span dir="ltr">[`mathani`](#mathani)، [`miun`](#miun)، [`mufassal`](#mufassal)، [`saba_tiwal`](#saba_tiwal)، [`surah_group`](#surah_group)</span>
- **المصحف والتخطيط** — `mushaf`: <span dir="ltr">[`font`](#font)، [`layout`](#layout)، [`line`](#line)، [`maqta_al_ayah`](#maqta_al_ayah)، [`page`](#page)، [`rasm`](#rasm)، [`rasm_imlai`](#rasm_imlai)، [`rasm_uthmani`](#rasm_uthmani)</span>
- **الضبط وعلامات المصحف** — `dabt`: <span dir="ltr">[`ayah_mark`](#ayah_mark)، [`dammah`](#dammah)، [`division_mark`](#division_mark)، [`dot`](#dot)، [`fathah`](#fathah)، [`hamzah`](#hamzah)، [`hamzat_al_wasl`](#hamzat_al_wasl)، [`harakah`](#harakah)، [`ijam`](#ijam)، [`imalah`](#imalah)، [`ishmam`](#ishmam)، [`kasrah`](#kasrah)، [`maddah`](#maddah)، [`mushaf_mark`](#mushaf_mark)، [`omitted_alif`](#omitted_alif)، [`orthographic_mark`](#orthographic_mark)، [`qiraah_mark`](#qiraah_mark)، [`rectangular_zero`](#rectangular_zero)، [`rounded_zero`](#rounded_zero)، [`sajdah_line`](#sajdah_line)، [`sajdah_mark`](#sajdah_mark)، [`saktah_mark`](#saktah_mark)، [`seen_al_qiraah`](#seen_al_qiraah)، [`shaddah`](#shaddah)، [`small_meem`](#small_meem)، [`small_noon`](#small_noon)، [`small_waw`](#small_waw)، [`small_yaa`](#small_yaa)، [`sukun`](#sukun)، [`tanwin`](#tanwin)، [`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)، [`tashil`](#tashil)، [`tashkil`](#tashkil)، [`three_dots`](#three_dots)، [`two_dots`](#two_dots)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)، [`waqf_mark`](#waqf_mark)</span>
- **عد الآي** — `ayah_numbering`: <span dir="ltr">[`ayah_count`](#ayah_count)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir)، [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_numbering_system`](#ayah_numbering_system)، [`equivalent_ayah`](#equivalent_ayah)</span>
- **النزول** — `revelation`: <span dir="ltr">[`asbab_al_nuzul`](#asbab_al_nuzul)، [`disputed`](#disputed)، [`madani`](#madani)، [`makki`](#makki)، [`nuzul`](#nuzul)، [`revelation_classification`](#revelation_classification)، [`revelation_order`](#revelation_order)</span>
- **القراءات** — `qiraat`: <span dir="ltr">[`farsh`](#farsh)، [`muqri`](#muqri)، [`qiraah`](#qiraah)، [`rawi`](#rawi)، [`riwayah`](#riwayah)، [`tariq`](#tariq)، [`usul`](#usul)، [`wajh`](#wajh)</span>
- **التلاوة** — `recitation`: <span dir="ltr">[`ayah_timing`](#ayah_timing)، [`hifz`](#hifz)، [`istiadhah`](#istiadhah)، [`khatmah`](#khatmah)، [`recitation`](#recitation)، [`reciter`](#reciter)، [`sujud_al_tilawah`](#sujud_al_tilawah)، [`takbir`](#takbir)، [`tartil`](#tartil)، [`tilawah`](#tilawah)، [`word_timing`](#word_timing)</span>
- **مراتب القراءة** — `recitation_pace`: <span dir="ltr">[`hadr`](#hadr)، [`recitation_pace`](#recitation_pace)، [`tadwir`](#tadwir)، [`tahqiq`](#tahqiq)</span>
- **أنماط الأداء** — `recitation_style`: <span dir="ltr">[`instructional_ayah_repetition`](#instructional_ayah_repetition)، [`muallim`](#muallim)، [`mujawwad`](#mujawwad)، [`murattal`](#murattal)، [`recitation_style`](#recitation_style)</span>
- **التجويد** — `tajwid`: <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`ghunnah`](#ghunnah)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`izhar`](#izhar)، [`lahn`](#lahn)، [`lahn_jali`](#lahn_jali)، [`lahn_khafi`](#lahn_khafi)، [`madd`](#madd)، [`madd_al_badal`](#madd_al_badal)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_lin`](#madd_al_lin)، [`madd_al_silah`](#madd_al_silah)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`madd_lazim`](#madd_lazim)، [`madd_munfasil`](#madd_munfasil)، [`madd_muttasil`](#madd_muttasil)، [`madd_tabii`](#madd_tabii)، [`makhraj`](#makhraj)، [`meem_sakinah`](#meem_sakinah)، [`mutabaidan`](#mutabaidan)، [`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)، [`mutaqariban`](#mutaqariban)، [`noon_sakinah`](#noon_sakinah)، [`qalqalah`](#qalqalah)، [`saktah`](#saktah)، [`sifat_al_huruf`](#sifat_al_huruf)، [`tafkhim`](#tafkhim)، [`tajwid`](#tajwid)، [`tarqiq`](#tarqiq)</span>
- **الوقف** — `waqf`: <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)، [`waqf`](#waqf)، [`waqf_hasan`](#waqf_hasan)، [`waqf_idtirari`](#waqf_idtirari)، [`waqf_ikhtibari`](#waqf_ikhtibari)، [`waqf_ikhtiyari`](#waqf_ikhtiyari)، [`waqf_intizari`](#waqf_intizari)، [`waqf_kafi`](#waqf_kafi)، [`waqf_mark_type`](#waqf_mark_type)، [`waqf_qabih`](#waqf_qabih)، [`waqf_ruling`](#waqf_ruling)، [`waqf_tamm`](#waqf_tamm)</span>
- **اللغة** — `linguistics`: <span dir="ltr">[`fil`](#fil)، [`harf_al_mana`](#harf_al_mana)، [`irab`](#irab)، [`ism`](#ism)، [`lemma`](#lemma)، [`morpheme`](#morpheme)، [`morphology`](#morphology)، [`part_of_speech`](#part_of_speech)، [`root`](#root)، [`stem`](#stem)، [`wazn`](#wazn)</span>
- **الترجمة** — `translation`: <span dir="ltr">[`spoken_translation`](#spoken_translation)، [`translation`](#translation)، [`translator`](#translator)، [`transliteration`](#transliteration)، [`word_by_word_translation`](#word_by_word_translation)</span>
- **التفسير** — `tafsir`: <span dir="ltr">[`mufassir`](#mufassir)، [`tafsir`](#tafsir)، [`tafsir_al_ray`](#tafsir_al_ray)، [`tafsir_mathur`](#tafsir_mathur)</span>
- **علوم القرآن** — `quranic_sciences`: <span dir="ltr">[`asma_al_surah`](#asma_al_surah)، [`fadail_al_quran`](#fadail_al_quran)، [`gharib_al_quran`](#gharib_al_quran)، [`maqasid_al_surah`](#maqasid_al_surah)، [`mutashabihat`](#mutashabihat)، [`naskh`](#naskh)، [`sabab_al_tasmiyah`](#sabab_al_tasmiyah)، [`tadabbur`](#tadabbur)</span>

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

**التعريف:** الصحف التي جمع فيها القرآن مكتوبًا ومرتبًا على ترتيبه المعروف.

**الغرض:** يستخدم عندما تكون خصائص التمثيل المكتوب للقرآن مهمة، مثل الرسم والتخطيط والصفحات والأسطر والعلامات.

- المصحف وعاء مكتوب للقرآن وليس القرآن نفسه؛ فتختلف المصاحف في الرسم والصفحات والعلامات والقرآن واحد.

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

**التعريف:** إصدار منشور محدد من المصحف له خصائص محددة من الناشر والرسم والضبط والتخطيط وغيرها.

**الغرض:** يستخدم لتمييز الإصدارات التي قد تختلف في الصفحات والأسطر والعلامات أو الخصائص الطباعية.

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

**التعريف:** كلام الله المنزل على محمد صلى الله عليه وسلم والمتعبد بتلاوته، ويطلق على مجموعه وعلى بعضه بحسب السياق.

**الغرض:** يمثل المحتوى القرآني نفسه بصورة مستقلة عن مصحف أو تخطيط أو تنسيق أو تمثيل رقمي معين.

- القرآن هو الكلام نفسه، والمصحف وعاؤه المكتوب؛ فما يخص الصفحات والرسم والعلامات يخص المصحف لا القرآن.

**مرتبط به:** <span dir="ltr">[`mushaf`](#mushaf)، [`surah`](#surah)، [`ayah`](#ayah)، [`fadail_al_quran`](#fadail_al_quran)</span>

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

**التعريف:** وحدة من النص القرآني تقع ضمن سورة ولها حدود محددة، وقد يختلف رقمها أو بعض حدودها باختلاف نظام عد الآي.

**الغرض:** تستخدم كوحدة أساسية للإشارة إلى النص القرآني وربط الترجمات والتفاسير والتلاوات والتحليلات والبيانات الأخرى بموضع محدد من القرآن.

- موقعها في صفحة أو سطر يخص المصحف أو تخطيطه، لا هوية الآية نفسها.
- الفاصلة نهاية الآية، وليست الآية.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`fasilah`](#fasilah)، [`ayah_mark`](#ayah_mark)، [`ayah_key`](#ayah_key)، [`word`](#word)، [`asbab_al_nuzul`](#asbab_al_nuzul)، [`ayah_count`](#ayah_count)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir)، [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_timing`](#ayah_timing)، [`equivalent_ayah`](#equivalent_ayah)، [`fadail_al_quran`](#fadail_al_quran)، [`gharib_al_quran`](#gharib_al_quran)، [`maqta_al_ayah`](#maqta_al_ayah)، [`mawdi_al_sajdah`](#mawdi_al_sajdah)، [`mutashabihat`](#mutashabihat)، [`naskh`](#naskh)، [`quran`](#quran)، [`tadabbur`](#tadabbur)، [`tafsir`](#tafsir)، [`tafsir_mathur`](#tafsir_mathur)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`

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

**التعريف:** معرف نصي للآية يجمع رقم سورتها ورقمها فيها مفصولين بنقطتين، على صورة `2:255`، ولا يُقرأ إلا في ضوء نظام عد الآي الذي يستند إليه.

**الغرض:** يستخدم مفتاحًا للربط بين مصادر البيانات ونقل الإشارة إلى الآية بين الواجهات والملفات؛ وتقييده بنظام العد يمنع أن يشير المفتاح الواحد إلى موضعين.

- المفتاح مرجع لا هوية: تغيير نظام العد يغير المفتاح ولا يغير الآية.
- المفتاح غير الرقم المتسلسل للآية في المصحف كله.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`word_key`](#word_key)، [`tartib_al_mushaf`](#tartib_al_mushaf)</span>

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

**التعريف:** صيغة «بسم الله الرحمن الرحيم» التي تفتتح بها السور عدا سورة التوبة، ولها أحكام واختلافات مرتبطة بعد الآي.

**الغرض:** تستخدم لتمييز البسملة وتمثيل موضعها وعلاقتها بالسورة ونظام عد الآي.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`ayah_numbering_system`](#ayah_numbering_system)، [`istiadhah`](#istiadhah)، [`takbir`](#takbir)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/30) — `30`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/145`

<a id="fasilah"></a>

### الفاصلة — Fasilah

<!-- source: standards/terminology/concepts/fasilah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`fasilah`</span> |
| `plural` | <span dir="ltr">`fasilahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفَاصِلَة |
| تهجئات أخرى | <span dir="ltr">`fasila`</span> |
| مقابل إنجليزي | <span dir="ltr">`Verse Ending`</span> |

**التعريف:** خاتمة الآية أو المقطع من جهة النظم، ويعرفها بعض العلماء بأنها الكلمة الأخيرة من الآية.

**الغرض:** تستخدم في الدراسات والبيانات التي تتناول فواصل الآيات والنظم القرآني، ولا تستخدم مرادفًا لـ`ayah`.

- الفاصلة خاتمة الآية من جهة النظم، وعلامة الآية رسم في المصحف يدل عليها.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`ayah_mark`](#ayah_mark)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/153`

<a id="harf_muqatta"></a>

### الحرف المقطع — Harf Muqatta

<!-- source: standards/terminology/concepts/harf_muqatta.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`harf_muqatta`</span> |
| `plural` | <span dir="ltr">`harf_muqattas`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحَرْف المُقَطَّع |
| مقابل إنجليزي | <span dir="ltr">`Disjointed Letters`، `Separated Letters`</span> |

**التعريف:** حروف هجائية افتتحت بها بعض السور، مثل: الم، والر، وحم، وكهيعص.

**الغرض:** تستخدم لتعريف هذه الفواتح وتمييزها وربطها بالسور ومواضعها النصية.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`huruf_muqattaah`](#huruf_muqattaah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/113) — `113`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/361`

<a id="huruf_muqattaah"></a>

### الحروف المقطعة — Huruf Muqattaah

<!-- source: standards/terminology/concepts/huruf_muqattaah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`huruf_muqattaah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحُرُوف المُقَطَّعَة |
| تهجئات أخرى | <span dir="ltr">`muqattaat`، `al_muqattaat`، `huruf_muqattaat`، `huroof_muqattaat`، `fawatih_al_suwar`</span> |
| مقابل إنجليزي | <span dir="ltr">`disjointed letters`، `mysterious letters`</span> |

**التعريف:** مجموعة الحروف الهجائية التي افتُتحت بها 29 سورة، تُقرأ بأسماء الحروف لا بمسمياتها، مثل «الم» و«كهيعص».

**الغرض:** تستخدم لوسم فواتح السور التي تُقرأ بأسماء حروفها، فتُعامل في التلاوة والمد والبحث والترجمة معاملة تخصها.

- الحرف المقطع الواحد `harf_muqatta`، وهذه الفاتحة مجموعةً.
- الفاتحة آية أو جزء آية بحسب نظام العد، وليست اسمًا للسورة.

**مرتبط به:** <span dir="ltr">[`harf_muqatta`](#harf_muqatta)، [`madd_lazim`](#madd_lazim)، [`surah`](#surah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/113) — `113`

<a id="mawdi_al_sajdah"></a>

### موضع السجدة — Mawdi al-Sajdah

<!-- source: standards/terminology/concepts/mawdi_al_sajdah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mawdi_al_sajdah`</span> |
| `plural` | <span dir="ltr">`mawdi_al_sajdahs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَوْضِع السَّجْدَة |
| السجل | <span dir="ltr">[`sajdah`](/guidelines/ar/03-terminology/registries/#sajdah)</span> |
| تهجئات أخرى | <span dir="ltr">`sajdah`، `sajda`، `sajdah_place`</span> |
| مقابل إنجليزي | <span dir="ltr">`Prostration`</span> |

**التعريف:** الموضع من النص الذي يسجد عنده القارئ، وينتهي بآية بعينها، ومواضعه معدودة مختلف في عد بعضها.

**الغرض:** يستخدم لربط السجدة بموضعها من السورة والآية والصفحة، ولتمييز الموضع عن العلامة التي ترسم عنده وعن السجود نفسه.

- الموضع مكان من النص، وعلامة السجدة رسم يدل عليه، وسجود التلاوة هو الفعل.

**مرتبط به:** <span dir="ltr">[`sajdah_mark`](#sajdah_mark)، [`sujud_al_tilawah`](#sujud_al_tilawah)، [`ayah`](#ayah)، [`sajdah_line`](#sajdah_line)</span>

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

**التعريف:** وحدة رئيسية من بنية القرآن، تتكون من آيات مرتبة ولها اسم وموضع معروف في ترتيب المصحف.

**الغرض:** تستخدم كوحدة رئيسية لتنظيم النص وربط الآيات والبيانات المتعلقة بالسورة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`asma_al_surah`](#asma_al_surah)، [`surah_group`](#surah_group)، [`revelation_classification`](#revelation_classification)، [`basmalah`](#basmalah)، [`ayah_count`](#ayah_count)، [`ayah_key`](#ayah_key)، [`fadail_al_quran`](#fadail_al_quran)، [`harf_muqatta`](#harf_muqatta)، [`huruf_muqattaah`](#huruf_muqattaah)، [`maqasid_al_surah`](#maqasid_al_surah)، [`mathani`](#mathani)، [`miun`](#miun)، [`mufassal`](#mufassal)، [`quran`](#quran)، [`revelation_order`](#revelation_order)، [`saba_tiwal`](#saba_tiwal)، [`sabab_al_tasmiyah`](#sabab_al_tasmiyah)، [`tartib_al_mushaf`](#tartib_al_mushaf)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="tartib_al_mushaf"></a>

### ترتيب المصحف — Tartib al-Mushaf

<!-- source: standards/terminology/concepts/tartib_al_mushaf.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tartib_al_mushaf`</span> |
| `kind` | <span dir="ltr">`property`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | تَرْتِيب المُصْحَف |
| تهجئات أخرى | <span dir="ltr">`surah_order`، `uthmani_order`، `tartib_al_suwar`</span> |
| مقابل إنجليزي | <span dir="ltr">`Mushaf order`</span> |

**التعريف:** ترتيب السور كما استقر عليه المصحف العثماني، من الفاتحة إلى الناس، وهو الترتيب الذي تُرقم به السور.

**الغرض:** يستخدم ترتيبًا افتراضيًّا للسور في العرض والتنقل، ورقم السورة فيه هو رقمها في المفتاح؛ ويُذكر باسمه حيث يقابله ترتيب النزول.

- ترتيب المصحف غير ترتيب النزول: للسورة رقم واحد في المصحف، وقد تختلف رتبتها في النزول باختلاف المصدر.

**مرتبط به:** <span dir="ltr">[`revelation_order`](#revelation_order)، [`surah`](#surah)، [`ayah_key`](#ayah_key)</span>

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

**التعريف:** معرف نصي للكلمة يضيف إلى مفتاح الآية موضع الكلمة فيها، على صورة `2:255:5`، وموضع الكلمة يُعد من أول الآية بحسب منهج تقسيم معلن.

**الغرض:** يستخدم مفتاحًا للبيانات المرتبطة بالكلمة: التوقيت والترجمة كلمة بكلمة والتحليل الصرفي والصور.

- الموضع في المفتاح موضع الكلمة لا `token`؛ فتغيير منهج التقسيم الذي يعد الكلمات يغير المفتاح.

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

**التعريف:** وحدة نصية مجردة في نظام تمثيل رقمي، ولا يلزم أن تطابق حرفًا لغويًا واحدًا.

**الغرض:** تستخدم حيث يلزم أن تكون الإزاحة أو الطول أو المقارنة دقيقة: اختبارات مسار النص، وفهارس البحث، وقائمة المحارف المسموح بها.

- المحرف وحدة ترميز، والحرف وحدة لغوية؛ فقد يمثل الحرف الواحد بأكثر من محرف.
- المحرف ليس الشكل المرسوم (`glyph`)؛ فالشكل ينتجه الخط، والمحرف يحمله النص.

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

**التعريف:** قيمة رقمية معرفة في معيار ترميز مثل `Unicode`.

**الغرض:** تستخدم حيث يهم الترميز الدقيق للمحرف أو العلامة: قواعد التطبيع، ومقابلات الخطوط، وقائمة النقاط المسموح بها.

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

**التعريف:** الشكل البصري الذي ينتجه الخط لتمثيل حرف أو محرف أو مجموعة منها.

**الغرض:** يستخدم في الخطوط والرسم والعرض ومواضع الأشكال البصرية.

- الشكل المرسوم ينتجه الخط، وليس الحرف ولا المحرف؛ فالمحرف الواحد قد يرسم بأشكال شتى.

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

**التعريف:** وحدة كتابية يدركها المستخدم كوحدة واحدة، وقد تتكون من أكثر من `codepoint`.

**الغرض:** تستخدم في التقسيم البصري والتحرير واختيار النص عندما لا يكون `codepoint` وحدة مناسبة.

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

**التعريف:** حرف هجائي بوصفه وحدة لغوية من وحدات الكتابة.

**الغرض:** يستخدم للبيانات التي تتعامل مع الحروف اللغوية، دون الخلط بينها وبين التمثيلات الرقمية أو البصرية.

- الحرف وحدة لغوية، والمحرف وحدة ترميز؛ فالحرف الواحد قد يكتب بمحرف أو أكثر.
- الحرف وحدة من الكتابة، وحرف المعنى قسم من أقسام الكلمة.

**مرتبط به:** <span dir="ltr">[`character`](#character)، [`glyph`](#glyph)، [`harf_al_mana`](#harf_al_mana)، [`ijam`](#ijam)، [`makhraj`](#makhraj)، [`word`](#word)</span>

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

**التعريف:** وحدة ينتجها تقسيم النص وفق منهج معلن، وقد تطابق الكلمة، وقد تكون جزءًا منها، وقد تجمع أكثر من كلمة.

**الغرض:** يستخدم لربط التحليل الآلي بالنص حين لا يكون حد الكلمة هو حد التقسيم، وليبقى ما ينتجه المقسم متميزًا عما يعده القارئ كلمة.

- الكلمة وحدة يعرفها القارئ، و`token` وحدة ينتجها منهج تقسيم؛ فاختلاف المنهج يغير عدد `tokens` ولا يغير عدد الكلمات.

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

**التعريف:** وحدة من النص يعرفها القارئ كلمة واحدة، ولا يتغير عدها بتغير منهج تقسيم النص.

**الغرض:** تستخدم لربط البيانات على مستوى الكلمة مثل الجذر والصرف والإعراب والتجويد والمحاذاة الصوتية والموضع البصري.

- الكلمة وحدة يعرفها القارئ، و`token` وحدة ينتجها منهج تقسيم؛ فاختلاف المنهج يغير عدد `tokens` ولا يغير عدد الكلمات.

**مرتبط به:** <span dir="ltr">[`token`](#token)، [`morpheme`](#morpheme)، [`letter`](#letter)، [`word_key`](#word_key)، [`ayah`](#ayah)، [`gharib_al_quran`](#gharib_al_quran)، [`irab`](#irab)، [`mutashabihat`](#mutashabihat)، [`word_by_word_translation`](#word_by_word_translation)، [`word_timing`](#word_timing)</span>

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

**التعريف:** في التقسيم المعاصر نصف جزء، فيكون القرآن ستين حزبًا.

**الغرض:** يستخدم لتمثيل التقسيمات الاصطلاحية والتنقل وخطط القراءة.

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

**التعريف:** واحد من ثلاثين قسمًا في التقسيم المشهور للمصحف لتيسير القراءة والختم.

**الغرض:** يستخدم للتنقل وتنظيم القراءة والجداول والخطط المرتبطة بأجزاء القرآن.

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

**التعريف:** واحد من سبعة أقسام تقليدية للقرآن لتيسير ختمه في أسبوع.

**الغرض:** يستخدم في التطبيقات التي تدعم نظام المنازل وخطط القراءة المبنية عليه.

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

**التعريف:** ربع الحزب في التقسيم المشهور للمصحف.

**الغرض:** يستخدم لتمثيل التقسيم الأدق للحزب ومواضع علاماته في المصحف.

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

**التعريف:** قسم اصطلاحي من القرآن يستخدم لتنظيم القراءة ويظهر في بعض المصاحف.

**الغرض:** يستخدم في التطبيقات والمصاحف التي تعتمد تقسيم الركوع.

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

**التعريف:** ثمن الحزب، وهو تقسيم مستخدم في بعض المصاحف والمدارس.

**الغرض:** يستخدم عند دعم مصادر أو مصاحف تعتمد تقسيم الحزب إلى أثمان.

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

**التعريف:** السور التي تقصر عن المئين وتليها في التقسيم التقليدي، وسميت مثاني لكثرة ما تثنى، أي تكرر قراءتها.

**الغرض:** تستخدم قيمة من قيم تصنيف السور، فتربط بها خطط القراءة وما يعالج المجموعة وحدة واحدة من كتب التفسير.

> لا يعين المعيار أعضاء المجموعة سورة سورة: فالمصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا سجل بعد يحصر أعضاء كل مجموعة بمصدره.

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

**التعريف:** السور التي تقارب آياتها المئة أو تزيد عليها أو تنقص عنها قليلًا.

**الغرض:** تستخدم قيمة من قيم تصنيف السور، فتربط بها خطط القراءة وما يعالج المجموعة وحدة واحدة من كتب التفسير.

> لا يعين المعيار أعضاء المجموعة سورة سورة: فالمصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا سجل بعد يحصر أعضاء كل مجموعة بمصدره.

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

**التعريف:** مجموعة من قصار السور التي تلي المثاني، مع اختلاف العلماء في أولها.

**الغرض:** تستخدم قيمة من قيم تصنيف السور، فتربط بها خطط القراءة وما يعالج المجموعة وحدة واحدة من كتب التفسير.

> لا يعين المعيار أعضاء المجموعة سورة سورة: فالمصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا سجل بعد يحصر أعضاء كل مجموعة بمصدره.

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

**التعريف:** مجموعة من أطول سور القرآن في أوله، مع خلاف معروف في تعيين السورة السابعة.

**الغرض:** تستخدم قيمة من قيم تصنيف السور، فتربط بها خطط القراءة وما يعالج المجموعة وحدة واحدة من كتب التفسير.

> لا يعين المعيار أعضاء المجموعة سورة سورة: فالمصادر تختلف في السابعة من الطوال وفي أول المفصل، ولا سجل بعد يحصر أعضاء كل مجموعة بمصدره.

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

**التعريف:** تصنيف يجمع سورًا وفق تقسيمات اصطلاحية موروثة تعتمد الطول أو موضعها ضمن مجموعات السور.

**الغرض:** يوفر أبًا موحدًا لتصنيفات مثل الطوال والمئين والمثاني والمفصل.

**مرتبط به:** <span dir="ltr">[`saba_tiwal`](#saba_tiwal)، [`miun`](#miun)، [`mathani`](#mathani)، [`mufassal`](#mufassal)، [`surah`](#surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/201`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/221`

## المصحف والتخطيط — `mushaf`

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

**التعريف:** ملف يحمل مجموعة من الأشكال المرسومة (`glyphs`) وقواعد إخراجها، يعرض به نص المصحف.

**الغرض:** يستخدم لتسجيل الخط الذي يعتمد عليه المصحف الرقمي، إذ لا يعرض نصه عرضًا صحيحًا إلا بخط بعينه في كثير من المصاحف، فترتبط به رموز الحروف وأشكالها ومواضع الأسطر.

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

**التعريف:** تنظيم النص والعناصر بصريًا إلى صفحات وأسطر ومواضع ضمن مصحف أو عرض معين.

**الغرض:** يفصل البيانات البصرية عن بنية القرآن النصية الثابتة.

**مرتبط به:** <span dir="ltr">[`mushaf_edition`](#mushaf_edition)، [`page`](#page)، [`line`](#line)، [`font`](#font)، [`maqta_al_ayah`](#maqta_al_ayah)، [`mushaf`](#mushaf)</span>

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

**التعريف:** سطر طباعي داخل صفحة مصحف أو تخطيط معين.

**الغرض:** يستخدم لتمثيل مواقع النص والأشكال داخل التخطيط الطباعي.

**مرتبط به:** <span dir="ltr">[`page`](#page)، [`layout`](#layout)، [`maqta_al_ayah`](#maqta_al_ayah)، [`font`](#font)</span>

<a id="maqta_al_ayah"></a>

### مقطع الآية — Maqta al-Ayah

<!-- source: standards/terminology/concepts/maqta_al_ayah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`maqta_al_ayah`</span> |
| `plural` | <span dir="ltr">`maqta_al_ayahs`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَقْطَع الآيَة |
| الجمع | مقاطع الآيات |
| تهجئات أخرى | <span dir="ltr">`ayah_segment`، `ayah_part`، `line_ayah`، `g_ayah`</span> |
| مقابل إنجليزي | <span dir="ltr">`ayah fragment`</span> |

**التعريف:** ما ظهر من آية واحدة في سطر واحد من صفحة مصحف بعينه؛ فالآية التي تمتد على سطرين مقطعان.

**الغرض:** يستخدم وحدةً للعرض والوسم في تخطيط الصفحة، لأن الآية لا تلزم السطر ولا السطر الآية؛ وعليه تُبنى المحاذاة والإبراز في مصحف مرسوم.

- المقطع صفة في تخطيط مصحف بعينه، وليس جزءًا من هوية الآية.
- المقطع غير الكلمة: قد يكون كلمة أو كلمات، أو جزء كلمة حيث يُقطع داخلها.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`line`](#line)، [`page`](#page)، [`layout`](#layout)</span>

**المصادر:**

- مصحف حفص — كلمة كلمة — `glossary!g.ayah`

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

**التعريف:** وحدة طباعية من تخطيط مصحف معين، وقد يختلف محتواها وحدودها باختلاف المصحف أو الطبعة.

**الغرض:** تستخدم في العرض والتنقل والمحاذاة البصرية بحسب صفحات مصحف معين.

**مرتبط به:** <span dir="ltr">[`mushaf_edition`](#mushaf_edition)، [`layout`](#layout)، [`line`](#line)، [`maqta_al_ayah`](#maqta_al_ayah)، [`mushaf`](#mushaf)</span>

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

**التعريف:** طريقة كتابة ألفاظ القرآن من حيث إثبات الحروف وحذفها وزيادتها وفصلها ووصلها ونحو ذلك.

**الغرض:** يستخدم تصنيفًا يبين على أي رسم كُتب نص أو مصحف أو `dataset`، فيتفرع عليه البحث والمقارنة والعرض؛ ويميز طبقة الرسم عن الخط والتخطيط والمحارف المرسومة.

- الرسم إثبات الحروف وحذفها وفصلها ووصلها، والضبط علامات النطق التي تعلو الحروف.
- الخط صورة الحروف في مصحف بعينه، والرسم ما يثبت في كل مصحف كُتب به.

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

**التعريف:** كتابة ألفاظ القرآن على قواعد الإملاء المعاصرة، بإثبات ما يُحذف في الرسم العثماني وحذف ما يُزاد فيه، لتُقرأ على صورتها المألوفة.

**الغرض:** يستخدم لتحديد أن نصًّا يتبع الإملاء المعاصر، وهو النص الذي تُبنى عليه صيغة البحث والاقتباس والعرض خارج المصحف، مقابل النص العثماني الذي يُعرض به المصحف.

- الرسم الإملائي كتابة لا قراءة: اللفظ واحد، والذي يختلف صورة الكلمة.
- النص الإملائي غير نص البحث المجرد من الضبط، وإن اشتُق الثاني من الأول.

> اشتقاق الاسم بالأداة يعطي `orthographic_rasm`، لأن جدول الكلمات العامة يترجم «إملائي» إلى `orthographic` من أجل «العلامة الإملائية»؛ والاسم المثبت `rasm_imlai`، وهو الذي تستعمله قواعد البيانات والواجهات، والقرار مسجل في سجل القرارات.

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

**التعريف:** طريقة كتابة كلمات المصاحف العثمانية وما يتعلق بها من حذف وزيادة وبدل وفصل ووصل.

**الغرض:** تستخدم لتحديد أن النص يتبع قواعد الرسم العثماني بدل نظم إملائية أخرى.

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

**التعريف:** الدَّارَة الفاصلة بين الآيتين، توضع عند نهاية الآية ويكتب فيها رقمها في أكثر المصاحف.

**الغرض:** تستخدم لتحديد حدود الآية في النص المكتوب، وهي العلامة التي يقرأ منها المحلل والعارض نهاية الآية ورقمها.

- العلامة رسم في المصحف، والفاصلة خاتمة الآية من جهة النظم.
- رقم الآية داخل الدارة يتبع نظام عد الآي، ولا يعد جزءًا من العلامة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`fasilah`](#fasilah)، [`ayah_numbering_system`](#ayah_numbering_system)</span>

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

**التعريف:** الدلالة على حركة الحرف بالضم

**الغرض:** تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على بداية الأجزاء والأحزاب وأنصافها وأرباعها

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

- علامة التقسيم رسم في المصحف، والجزء والحزب وأرباعه أقسام من النص تدل عليها.

> كان `alamat_al_tahzib` مدخلًا مستقلًا يعرف الشيء نفسه، فدمج في هذا المدخل.

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

**التعريف:** نقطة واحدة فوق الحرف أو تحته تميزه عما يشاركه في الرسم، كالباء والنون والجيم والخاء والذال

**الغرض:** تستخدم قيمةً من قيم النقط، ليتميز بها الحرف عما يشاركه في الرسم في التحليل والبحث.

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

**التعريف:** الدلالة على حركة الحرف بالفتح

**الغرض:** تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على همزة القطع المحققة

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** الدلالة على سقوط الهمزة وصلًا

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** علامة تضبط حركة الحرف أو سكونه أو تشديده: الفتحة والضمة والكسرة والسكون والشدة.

**الغرض:** تستخدم أبًا لعلامات الضبط التي تحدد نطق الحرف نفسه.

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

**التعريف:** النقط الذي يميز الحرف عما يشاركه في صورة الرسم.

**الغرض:** تستخدم أبًا لصور النقط، فما يميزها هو عددها وموضعها لا وظيفتها.

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

**التعريف:** الدلالة على الإمالة الكبرى: نطق الفتحة مائلة إلى الكسرة، وهي في رواية حفص في موضع واحد (11:41)

**الغرض:** تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.

**مرتبط به:** <span dir="ltr">[`usul`](#usul)</span>

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

**التعريف:** الدلالة على الإشمام: ضم الشفتين إشارة إلى الضمة المحذوفة من غير صوت

**الغرض:** تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.

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

**التعريف:** الدلالة على حركة الحرف بالكسر

**الغرض:** تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على لزوم مد الحرف مدًّا زائدًا على المد الطبيعي

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** رمز أو علامة غير داخلة في الحروف الأصلية للكلمة، تستخدم في المصحف لأغراض القراءة أو التنظيم أو الإرشاد.

**الغرض:** يوفر أبًا موحدًا للعلامات المختلفة بدل معاملتها كأنواع غير مرتبطة.

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

**التعريف:** الدلالة على ألف محذوفة من الرسم واجبة النطق

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** علامة تضبط رسم الكلمة، كالهمزة والمدة والحروف الصغيرة.

**الغرض:** تستخدم أبًا للعلامات التي تتعلق برسم الكلمة لا بحركتها ولا بالوقف عليها.

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

**التعريف:** علامة ترشد إلى وجه من وجوه الأداء في موضعها، كالسكت والإشمام والتسهيل.

**الغرض:** تستخدم أبًا للعلامات التي تنبه القارئ إلى أداء خاص، لا إلى ضبط الحرف.

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

**التعريف:** الدلالة على زيادة الألف وصلًا لا وقفًا؛ فتنطق عند الوقف عليها

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

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

**التعريف:** الدلالة على زيادة الحرف رسمًا؛ فلا ينطق وصلًا ولا وقفًا

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

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

**التعريف:** الدلالة على الكلمة الموجبة للسجدة

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

**مرتبط به:** <span dir="ltr">[`sajdah_mark`](#sajdah_mark)، [`mawdi_al_sajdah`](#mawdi_al_sajdah)</span>

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

**التعريف:** الدلالة على موضع السجود

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

- علامة السجدة رسم في المصحف، وموضع السجدة مكان من النص، وسجود التلاوة الفعل.

> كان `alamat_mawdi_al_sajdah` مدخلًا مستقلًا يعرف الشيء نفسه، فدمج في هذا المدخل.

**مرتبط به:** <span dir="ltr">[`mawdi_al_sajdah`](#mawdi_al_sajdah)، [`sujud_al_tilawah`](#sujud_al_tilawah)، [`sajdah_line`](#sajdah_line)</span>

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

**التعريف:** الدلالة على السكت: وقفة يسيرة من غير تنفس ثم الوصل بما بعده

**الغرض:** تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.

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

**التعريف:** السين فوق الصاد تدل على القراءة بالسين، والسين تحتها تدل على القراءة بالصاد

**الغرض:** تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.

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

**التعريف:** الدلالة على تشديد الحرف بإدغام الأول الساكن في الثاني المتحرك، فينطقان حرفًا واحدًا مشددًا

**الغرض:** تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على قلب النون الساكنة أو التنوين ميمًا عند الباء

**الغرض:** تستخدم علامةً من علامات المصحف، ليعرف بها موضعها ودلالتها في العرض والتحليل.

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

**التعريف:** الدلالة على نون محذوفة من الرسم واجبة النطق، في موضع واحد (21:88) وحده

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** الدلالة على صلة هاء الضمير المضمومة بواو لفظية في حال الوصل

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** الدلالة على صلة هاء الضمير المكسورة بياء لفظية في حال الوصل

**الغرض:** تستخدم قيمةً من علامات الرسم، ليعرف بها ما خالف فيه الرسم اللفظ في الكلمة.

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

**التعريف:** الدلالة على سكون الحرف وإظهاره

**الغرض:** تستخدم قيمةً من قيم الحركة، ليقرأ منها نطق الحرف في التحليل والعرض والتعليم بدل قراءة صورة الشكل.

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

**التعريف:** نون ساكنة زائدة تلحق آخر الاسم، وترسم بتكرار صورة الحركة.

**الغرض:** تستخدم أبًا لعلامات التنوين الثلاث، فتجمعها بدل تفريقها في قائمة واحدة.

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

**التعريف:** الدلالة على التنوين المرفوع. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد التالي على الإدغام الكامل، ودونه على الإدغام الناقص أو الإخفاء

**الغرض:** تستخدم قيمةً من قيم التنوين، ليقرأ منها نطق آخر الاسم وحكمه بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على التنوين المنصوب. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد التالي على الإدغام الكامل، ودونه على الإدغام الناقص أو الإخفاء

**الغرض:** تستخدم قيمةً من قيم التنوين، ليقرأ منها نطق آخر الاسم وحكمه بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على التنوين المخفوض. وتركيب الحركتين يدل على إظهار التنوين، وتتابعهما مع تشديد التالي على الإدغام الكامل، ودونه على الإدغام الناقص أو الإخفاء

**الغرض:** تستخدم قيمةً من قيم التنوين، ليقرأ منها نطق آخر الاسم وحكمه بدل قراءة صورة الشكل.

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

**التعريف:** الدلالة على تسهيل الهمزة بين بين، أي بينها وبين الألف

**الغرض:** تستخدم قيمةً من علامات القراءة، لينبه بها القارئ إلى أداء خاص في موضعه.

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

**التعريف:** طبقة علامات الضبط الملحقة بحروف النص، من الحركات والتنوين والشدة والسكون وما يتبعها، منظورًا إليها جملةً.

**الغرض:** يستخدم حين يُتعامل مع طبقة الضبط كلها، كإثباتها في العرض أو تجريد النص منها للبحث، لا مع علامة بعينها.

- التشكيل الطبقة، والحركة العلامة الواحدة.
- الضبط العلم وقواعده، والتشكيل ما نتج عنه على الحروف.

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

**التعريف:** ثلاث نقاط فوق الحرف تميزه عما يشاركه في الرسم، كالثاء والشين

**الغرض:** تستخدم قيمةً من قيم النقط، ليتميز بها الحرف عما يشاركه في الرسم في التحليل والبحث.

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

**التعريف:** نقطتان فوق الحرف أو تحته تميزانه عما يشاركه في الرسم، كالتاء والياء والقاف

**الغرض:** تستخدم قيمةً من قيم النقط، ليتميز بها الحرف عما يشاركه في الرسم في التحليل والبحث.

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

**التعريف:** موضعان للوقف، إذا وقف على أحدهما لم يصح الوقف على الآخر

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** الوقف جائز جوازًا مستوي الطرفين، فالوقف والوصل سواء

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** الوقف جائز مع كون الوقف أولى

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** الوقف جائز مع كون الوصل أولى

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** الوقف لازم، لأن وصل ما بعده بما قبله يوهم خلاف المعنى المراد

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** الوقف ممنوع، لأن الوقف على الموضع يفسد المعنى أو يقطع ما لا ينفصل عما بعده

**الغرض:** تستخدم قيمةً من قيم نوع علامة الوقف، ليتفرع عليها العرض والتلقين والتنبيه في التطبيقات بدل قراءة صورة الرمز.

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

**التعريف:** علامة في المصحف ترشد القارئ إلى حكم الوقف أو الوصل في موضع معين.

**الغرض:** تستخدم لتمثيل الرمز وموضعه ونوعه بصورة منظمة.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark_type`](#waqf_mark_type)، [`mushaf_mark`](#mushaf_mark)، [`sabab_al_waqf`](#sabab_al_waqf)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)</span>

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

**التعريف:** عدد آيات السورة في نظام عد بعينه، وقد يختلف من نظام إلى نظام باختلاف الفواصل المعدودة.

**الغرض:** يستخدم للتحقق من المراجع وحدود السور وبناء الفهارس، ويُقرأ من سجل العد لا يُحسب من نص بعينه.

- العدد صفة في السورة تحت نظام عد، لا في المصحف.

> الاسم البرمجي على نسق `ayah_numbering_*` واسم السجل، لا اشتقاق من «عَدَد الآيَات»؛ فالمفهوم من مفاهيم التمثيل وإن كان لعدد الآي أصل في علم العد.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`surah`](#surah)، [`ayah`](#ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_basri"></a>

### العد البصري — Basri Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_basri.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_basri`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ البَصْرِيّ |
| تهجئات أخرى | <span dir="ltr">`basri_numbering`، `basran_numbering`، `basri`</span> |

**التعريف:** عد أهل البصرة، المروي عن عاصم الجحدري عن أسلافه من أهل البصرة.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_dimashqi"></a>

### العد الدمشقي — Dimashqi Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_dimashqi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_dimashqi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ الدِّمَشْقِيّ |
| تهجئات أخرى | <span dir="ltr">`dimashqi_numbering`، `shami`، `shami_numbering`، `damascene_numbering`، `dimashqi`</span> |
| دليل اسم العرض | <span dir="ltr">GitHub phrase search: dimashqi numbering 0 vs shami numbering 0. No form is established, so the display follows the code; `shami` stays an alias.</span> |

**التعريف:** عد أهل الشام، المروي عن يحيى بن الحارث الذماري عن ابن عامر، ويسمى العد الشامي.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/82`

<a id="ayah_numbering_kufi"></a>

### العد الكوفي — Kufi Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_kufi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_kufi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ الكُوفِيّ |
| تهجئات أخرى | <span dir="ltr">`kufi_numbering`، `kufan_numbering`، `kufi`</span> |

**التعريف:** عد أهل الكوفة، المروي عن حمزة الزيات عن ابن أبي ليلى عن أبي عبد الرحمن السلمي عن علي بن أبي طالب، وهو العد الذي يجري عليه أكثر المصاحف المطبوعة اليوم.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/80`

<a id="ayah_numbering_madani_akhir"></a>

### العد المدني الأخير — Madani Akhir Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_madani_akhir.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_madani_akhir`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَدَنِيّ الأَخِير |
| تهجئات أخرى | <span dir="ltr">`madani_akhir`، `last_madani`، `madani_last`</span> |

**التعريف:** عد أهل المدينة في روايته الأخيرة، وهي رواية إسماعيل بن جعفر عن سليمان بن جماز.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_madani_awwal"></a>

### العد المدني الأول — Madani Awwal Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_madani_awwal.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_madani_awwal`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَدَنِيّ الأَوَّل |
| تهجئات أخرى | <span dir="ltr">`madani_awwal`، `first_madani`، `madani_first`</span> |

**التعريف:** عد أهل المدينة في روايته الأولى، وهي رواية أبي جعفر يزيد بن القعقاع وشيبة بن نصاح.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [البيان في عد آي القرآن](https://files.turath.io/books-v3/5542.json) — `1/79`

<a id="ayah_numbering_makki"></a>

### العد المكي — Makki Numbering

<!-- source: standards/terminology/concepts/ayah_numbering_makki.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ayah_numbering_makki`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | العَدّ المَكِّيّ |
| تهجئات أخرى | <span dir="ltr">`makki_numbering`، `meccan_numbering`</span> |

**التعريف:** عد أهل مكة، المروي عن ابن كثير عن مجاهد عن ابن عباس عن أبي بن كعب.

**الغرض:** يستخدم قيمة من قيم نظام عد الآي، فيعرف به ما تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset`، وتقابل به مواضع الآي بين الأنظمة.

> الاسم البرمجي هنا اسم الأصل وما يميز القيمة، لا اشتقاق من الاسم العربي؛ فاشتقاق «العَدّ» يعطي `add` وهو فعل إنجليزي، و`makki` مأخوذ قيمةً من قيم `revelation_classification`. والوجه في ذلك مسجل في سجل القرارات.

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
| القيم | <span dir="ltr">[`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir)، [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal)، [`ayah_numbering_makki`](#ayah_numbering_makki)</span> |
| الأصل | <span dir="ltr">`standard`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | نِظَام عَدّ الآي |
| السجل | <span dir="ltr">[`ayah_numbering`](/guidelines/ar/03-terminology/registries/#ayah_numbering)</span> |
| تهجئات أخرى | <span dir="ltr">`ayah_counting_system`</span> |

**التعريف:** نظام يحدد حدود الآيات وأعدادها وأرقامها وبعض المسائل المتعلقة بالبسملة وفق مدارس عد الآي.

**الغرض:** يستخدم لتحديد النظام الذي تستند إليه أرقام الآيات وحدودها في مصحف أو `dataset` معين.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`equivalent_ayah`](#equivalent_ayah)، [`basmalah`](#basmalah)، [`ayah_count`](#ayah_count)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_makki`](#ayah_numbering_makki)، [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal)، [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir)، [`ayah_key`](#ayah_key)، [`ayah_mark`](#ayah_mark)، [`qiraah`](#qiraah)</span>

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

**التعريف:** الآية في نظام عد تقابل آيةً في نظام آخر، سواء اتفق رقماهما أو اختلفا لاختلاف مواضع الفصل بين الآي.

**الغرض:** تستخدم للربط بين أرقام الآيات عبر أنظمة العد، فلا تقارن البيانات المبنية على نظام ببيانات مبنية على غيره بالرقم وحده.

- المقابلة بين نظامي عد، وليست تشابهًا في اللفظ ولا تكرارًا للنص.

**مرتبط به:** <span dir="ltr">[`ayah_numbering_system`](#ayah_numbering_system)، [`ayah`](#ayah)، [`mutashabihat`](#mutashabihat)، [`ayah_numbering_basri`](#ayah_numbering_basri)، [`ayah_numbering_dimashqi`](#ayah_numbering_dimashqi)، [`ayah_numbering_kufi`](#ayah_numbering_kufi)، [`ayah_numbering_madani_akhir`](#ayah_numbering_madani_akhir)، [`ayah_numbering_madani_awwal`](#ayah_numbering_madani_awwal)، [`ayah_numbering_makki`](#ayah_numbering_makki)</span>

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

**التعريف:** الحوادث أو الأسئلة التي نزلت آية أو آيات متحدثة عنها أو مبينة لحكم يتعلق بها.

**الغرض:** تستخدم لربط الآيات بالمرويات والمعلومات المتعلقة بسبب نزولها.

**مرتبط به:** <span dir="ltr">[`nuzul`](#nuzul)، [`ayah`](#ayah)، [`sabab_al_tasmiyah`](#sabab_al_tasmiyah)، [`naskh`](#naskh)</span>

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

**التعريف:** ما اختلفت المصادر المعتمدة في تصنيفه بين المكي والمدني.

**الغرض:** يمنع إجبار البيانات المختلف فيها على قيمة `makki` أو `madani` دون توثيق الخلاف.

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

**التعريف:** ما نزل من القرآن بعد الهجرة، ولو نزل خارج المدينة.

**الغرض:** يستخدم قيمةً من قيم تصنيف النزول، فتوسم به السورة أو الآية.

- مدني وصف لزمن النزول بعد الهجرة، لا لمكان النزول.

**مرتبط به:** <span dir="ltr">[`makki`](#makki)، [`revelation_classification`](#revelation_classification)، [`nuzul`](#nuzul)، [`disputed`](#disputed)</span>

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

**التعريف:** ما نزل من القرآن قبل الهجرة، ولو نزل خارج مكة.

**الغرض:** يستخدم قيمةً من قيم تصنيف النزول، فتوسم به السورة أو الآية.

- مكي وصف لزمن النزول قبل الهجرة، لا لمكان النزول.

**مرتبط به:** <span dir="ltr">[`madani`](#madani)، [`revelation_classification`](#revelation_classification)، [`nuzul`](#nuzul)، [`disputed`](#disputed)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/60`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/37`

<a id="nuzul"></a>

### النزول — Nuzul

<!-- source: standards/terminology/concepts/nuzul.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`nuzul`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النُّزُول |
| مقابل إنجليزي | <span dir="ltr">`Revelation`</span> |

**التعريف:** إنزال القرآن على النبي صلى الله عليه وسلم منجمًا في مدة الرسالة، على حسب الوقائع والحاجة.

**الغرض:** يستخدم أصلًا تتفرع عنه ترتيب النزول وتصنيفه وأسبابه، فهذه الثلاثة كلها صفات لواقعة النزول، ولا تعرف إلا به.

- النزول واقعة، وترتيب النزول وتصنيفه وسببه صفات لها لا مرادفات لها.

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

**التعريف:** تصنيف للنص القرآني بحسب وقوع نزوله قبل الهجرة أو بعدها وفق الاصطلاح المعتمد.

**الغرض:** يستخدم لتصنيف السور أو الآيات بحسب علاقتها بالهجرة دون الإيحاء بأن التصنيف جغرافي فقط.

**مرتبط به:** <span dir="ltr">[`makki`](#makki)، [`madani`](#madani)، [`disputed`](#disputed)، [`nuzul`](#nuzul)، [`surah`](#surah)</span>

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

**التعريف:** ترتيب السور أو الآيات بحسب زمن نزولها، وقد يختلف بحسب المصدر المعتمد.

**الغرض:** يستخدم لتخزين ترتيب النزول بصورة مستقلة عن ترتيب المصحف.

- ترتيب النزول غير ترتيب المصحف؛ فرقم السورة هو ترتيب المصحف.

**مرتبط به:** <span dir="ltr">[`nuzul`](#nuzul)، [`surah`](#surah)، [`tartib_al_mushaf`](#tartib_al_mushaf)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/140`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/93`

## القراءات — `qiraat`

<a id="farsh"></a>

### الفرش — Farsh

<!-- source: standards/terminology/concepts/farsh.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`farsh`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفَرْش |
| تهجئات أخرى | <span dir="ltr">`farsh_al_huruf`، `farshiyyah`، `farshiyyat`</span> |
| مقابل إنجليزي | <span dir="ltr">`word-specific differences`</span> |

**التعريف:** ما اختلف فيه القراء من الكلمات في مواضع بأعيانها من السور، لا يطرد الخلاف فيه على قاعدة، بل يُذكر كل موضع بنفسه مرتبًا على السور.

**الغرض:** يستخدم لوسم فروق القراءات التي تُخزن كلمةً كلمةً بموضعها، مقابل الأصول التي تُخزن قاعدةً وتُطبق حيث تحقق شرطها.

- الفرش والأصول قسما خلاف القراءات، والوجه ما يجوز داخل الرواية الواحدة.

**مرتبط به:** <span dir="ltr">[`usul`](#usul)، [`qiraah`](#qiraah)، [`wajh`](#wajh)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `2/206`

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

**التعريف:** من تلقى القراءة وأتقنها وينقلها للمتعلمين.

**الغرض:** يستخدم لتمثيل دور التعليم والتلقي والإقراء، ويتميز عن مجرد `reciter`.

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

**التعريف:** وجه من وجوه قراءة القرآن ينسب إلى إمام من أئمة القراءات وتتفرع عنه الروايات والطرق.

**الغرض:** يمثل المستوى الأعلى في نموذج القراءات ويربط الروايات والطرق والنصوص المرتبطة بها.

**مرتبط به:** <span dir="ltr">[`riwayah`](#riwayah)، [`rawi`](#rawi)، [`tariq`](#tariq)، [`muqri`](#muqri)، [`ayah_numbering_system`](#ayah_numbering_system)، [`farsh`](#farsh)، [`qiraah_mark`](#qiraah_mark)، [`usul`](#usul)</span>

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

**التعريف:** من نسبت إليه الرواية عن إمام القراءة.

**الغرض:** يستخدم لتمثيل الشخص المرتبط بـ`riwayah`.

- الراوي من نسبت إليه الرواية عن إمام القراءة، والقارئ مؤدي التسجيل؛ فلا يسمى مؤدي التسجيل راويًا لمجرد أنه يقرأ برواية.

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

**التعريف:** ما ينسب إلى راو عن إمام القراءة؛ مثل رواية حفص عن عاصم.

**الغرض:** تستخدم لتحديد الرواية التي يتبعها نص أو مصحف أو تسجيل أو `dataset`.

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

**التعريف:** وجه النقل المأخوذ عن الراوي بواسطة من دونه في سلسلة نقل القراءة.

**الغرض:** يستخدم عندما تحتاج البيانات إلى مستوى أدق من الرواية لتمييز طرق الأداء والنقل.

> الطرق الأربعة التي تخزنها التطبيقات — الشاطبية وطيبة النشر والدرة والتيسير — في `registries/tariq.tsv`، وحصر طرق النشر كلها، وهي نحو 980 طريقًا، لا يزال مفتوحًا.

**مرتبط به:** <span dir="ltr">[`riwayah`](#riwayah)، [`qiraah`](#qiraah)، [`wajh`](#wajh)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/115`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/146`

<a id="usul"></a>

### الأصول — Usul

<!-- source: standards/terminology/concepts/usul.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`usul`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الأُصُول |
| تهجئات أخرى | <span dir="ltr">`usool`، `usul_al_qiraah`، `usul_al_qiraat`</span> |
| مقابل إنجليزي | <span dir="ltr">`general rules`</span> |

**التعريف:** القواعد المطردة في القراءة التي يجري عليها كل ما تحقق فيه شرطها، كالمد والهمز والإمالة والإدغام وهاء الكناية.

**الغرض:** تستخدم لوسم فروق القراءات التي تُخزن قاعدةً لا موضعًا، فتُطبق على النص حيث تحقق شرطها.

- الأصول قواعد القراءة، والفرش مواضعها المعينة.

**مرتبط به:** <span dir="ltr">[`farsh`](#farsh)، [`qiraah`](#qiraah)، [`madd`](#madd)، [`imalah`](#imalah)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/30`

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

**التعريف:** كيفية من كيفيات الأداء يجوز الأخذ بأي منها في الرواية الواحدة أو الطريق الواحد، كأوجه المد العارض للسكون.

**الغرض:** يستخدم حين يحتاج التسجيل أو التعليم إلى تعيين الوجه المأخوذ به من أوجه جائزة، من غير أن يُنسب الاختلاف إلى رواية أو طريق.

- الوجه لا يغير نسبة القراءة، والطريق يغيرها.

**مرتبط به:** <span dir="ltr">[`tariq`](#tariq)، [`riwayah`](#riwayah)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`lahn`](#lahn)، [`farsh`](#farsh)</span>

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

**التعريف:** مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل آية بعينها.

**الغرض:** يستخدم لربط النص بالصوت، وعليه يقوم التتبع أثناء الاستماع والانتقال إلى آية والتكرار والاقتطاع.

- التوقيت صفة في التسجيل لا في الآية، فيختلف باختلاف التلاوة.
- التوقيت على مستوى الآية غير المحاذاة على مستوى الكلمة.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`ayah`](#ayah)، [`reciter`](#reciter)، [`word_timing`](#word_timing)</span>

<a id="hifz"></a>

### الحفظ — Hifz

<!-- source: standards/terminology/concepts/hifz.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hifz`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الحِفْظ |
| تهجئات أخرى | <span dir="ltr">`hifdh`، `hifz_al_quran`</span> |
| مقابل إنجليزي | <span dir="ltr">`memorising the Quran`، `memorization`، `memorisation`</span> |

**التعريف:** استظهار القرآن كله أو بعضه عن ظهر قلب، على وجه يُتلى به من غير نظر في المصحف.

**الغرض:** يستخدم مجالًا لأدوات الاستظهار والمراجعة، التي تربط بالآية والصفحة والمتشابهات ما تتبعه من خطط وتكرار.

- الحفظ حال القارئ لا صفة في النص، فلا يُوسم به النص، وإنما ما يُبنى له.

**مرتبط به:** <span dir="ltr">[`mutashabihat`](#mutashabihat)، [`instructional_ayah_repetition`](#instructional_ayah_repetition)، [`tilawah`](#tilawah)، [`khatmah`](#khatmah)</span>

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

**التعريف:** طلب العوذ بالله من الشيطان عند إرادة تلاوة القرآن.

**الغرض:** يستخدم لتمثيل الاستعاذة وصيغها وموضعها بالنسبة إلى بداية التلاوة.

**مرتبط به:** <span dir="ltr">[`basmalah`](#basmalah)، [`recitation`](#recitation)، [`takbir`](#takbir)</span>

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

**التعريف:** قراءة القرآن كاملًا من أوله إلى آخره.

**الغرض:** تستخدم لتتبع خطط الختم وإتمام القراءة وربط الجلسات بمسار ختمة.

**مرتبط به:** <span dir="ltr">[`juz`](#juz)، [`manzil`](#manzil)، [`recitation`](#recitation)، [`hifz`](#hifz)، [`takbir`](#takbir)</span>

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

**التعريف:** تسجيل منشور لتلاوة القرآن، منسوب إلى قارئ ورواية ونمط أداء.

**الغرض:** يستخدم لتمثيل التسجيل الذي تُربط به التوقيتات ونمط الأداء ومرتبة السرعة، فيُنسب إلى قارئ ورواية ويُفرد عن فعل التلاوة.

- التسجيل المنشور المنسوب إلى قارئ ورواية ونمط هو `recitation`، والتلاوة الفعل.

**مرتبط به:** <span dir="ltr">[`reciter`](#reciter)، [`riwayah`](#riwayah)، [`recitation_style`](#recitation_style)، [`recitation_pace`](#recitation_pace)، [`ayah_timing`](#ayah_timing)، [`word_timing`](#word_timing)، [`tilawah`](#tilawah)، [`istiadhah`](#istiadhah)، [`khatmah`](#khatmah)، [`spoken_translation`](#spoken_translation)، [`tajwid`](#tajwid)، [`takbir`](#takbir)، [`tartil`](#tartil)</span>

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

**التعريف:** الشخص الذي يؤدي تلاوة القرآن.

**الغرض:** يستخدم لربط التسجيلات الصوتية بمؤديها.

- القارئ مؤدي التلاوة في التسجيل، وليس إمام قراءة ولا راويًا.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`rawi`](#rawi)، [`muqri`](#muqri)، [`ayah_timing`](#ayah_timing)، [`tilawah`](#tilawah)</span>

<a id="sujud_al_tilawah"></a>

### سجود التلاوة — Sujud al-Tilawah

<!-- source: standards/terminology/concepts/sujud_al_tilawah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sujud_al_tilawah`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | سُجُود التِّلَاوَة |
| تهجئات أخرى | <span dir="ltr">`sajdah_al-tilawah`، `sajdat_al-tilawah`</span> |

**التعريف:** سجدة تؤدى عند قراءة أو سماع موضع من مواضع سجود التلاوة.

**الغرض:** يستخدم لربط أحكام السجود وآدابه بموضعه، وليبقى الفعل في البيانات مستقلًا عن العلامة والموضع.

- سجود التلاوة فعل، وعلامة السجدة رسم في المصحف، وموضع السجدة مكان من النص.

**مرتبط به:** <span dir="ltr">[`mawdi_al_sajdah`](#mawdi_al_sajdah)، [`sajdah_mark`](#sajdah_mark)، [`tilawah`](#tilawah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/381`

<a id="takbir"></a>

### التكبير — Takbir

<!-- source: standards/terminology/concepts/takbir.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`takbir`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّكْبِير |
| تهجئات أخرى | <span dir="ltr">`takbeer`، `takbir_al_khatm`، `takbir_al_khatmah`</span> |

**التعريف:** قول «الله أكبر» بين السور، من آخر «الضحى» إلى آخر «الناس»، مرويًّا عن أهل مكة في رواية البزي عن ابن كثير، ويُفعل عند الختم على غيرها.

**الغرض:** يستخدم لوسم ما في التسجيل من التكبير بين السور، حتى لا يُحسب على آية ولا يسقط عند القص.

- التكبير ليس من القرآن ولا من السورة، فلا آية له ولا توقيت آية.

**مرتبط به:** <span dir="ltr">[`khatmah`](#khatmah)، [`recitation`](#recitation)، [`basmalah`](#basmalah)، [`istiadhah`](#istiadhah)</span>

**المصادر:**

- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `2/405`

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

**التعريف:** قراءة القرآن بتؤدة وبيان للحروف والكلمات ومراعاة الوقف والمعنى.

**الغرض:** يستخدم صفةً للأداء في وصف التسجيل والتعليم، لا اسمًا للنمط الذي يُنشر به التسجيل.

- الترتيل صفة الأداء نفسه، والمرتل نمط تسجيل؛ فلا يستعمل أحد الاسمين مكان الآخر.

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

**التعريف:** قراءة القرآن بلفظه أداءً بالصوت على ما تلقاه القارئ، في صلاة كانت أو درس أو تسجيل.

**الغرض:** يستخدم للدلالة على فعل القراءة نفسه حيث يُقصد، كأحكام التلاوة وآدابها وسجدتها وتعلمها؛ ويبقى التسجيل المنشور لها `recitation`.

- التلاوة الفعل، و`recitation` التسجيل المنشور المنسوب إلى قارئ ورواية ونمط أداء.
- الترتيل صفة في التلاوة، لا التلاوة.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`tartil`](#tartil)، [`sujud_al_tilawah`](#sujud_al_tilawah)، [`reciter`](#reciter)، [`hifz`](#hifz)، [`lahn`](#lahn)</span>

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

**التعريف:** مدى زمني في تسجيل تلاوة، محدد ببداية ونهاية، يقابل كلمة بعينها من آية.

**الغرض:** يستخدم لإبراز الكلمة المتلوة أثناء الاستماع، ولمحاذاة النص بالصوت على مستوى أدق من الآية، ولتقطيع التسجيل عند كلمة.

- توقيت الكلمة يقع داخل توقيت آيتها ولا يتجاوزه.
- تسمي واجهات الصوت هذا المفهوم `segment`، والاسم في هذا المعيار `word_timing`، لأن `segment` في مدونات التحليل اللغوي اسم للوحدة الصرفية.

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

**التعريف:** الإسراع في القراءة مع المحافظة على الحروف والحركات وأحكام الأداء دون إخلال.

**الغرض:** تستخدم قيمة من قيم مراتب القراءة، فيوسم بها التسجيل أو جلسة التعليم وتصفى بها.

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

**التعريف:** تصنيف لسرعة أداء القراءة مع المحافظة على أحكامها.

**الغرض:** يفصل مراتب السرعة التقليدية عن أنماط التسجيل مثل `murattal` و`mujawwad`.

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

**التعريف:** القراءة بسرعة متوسطة بين التحقيق والحدر مع المحافظة على الأحكام.

**الغرض:** تستخدم قيمة من قيم مراتب القراءة، فيوسم بها التسجيل أو جلسة التعليم وتصفى بها.

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

**التعريف:** القراءة ببطء وتؤدة مع استيفاء الحروف وأحكامها، وتستخدم كثيرًا في مقام التعليم.

**الغرض:** تستخدم قيمة من قيم مراتب القراءة، فيوسم بها التسجيل أو جلسة التعليم وتصفى بها.

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

**التعريف:** إعادة آية أو جزء منها مرة أو مرات وفق نمط تعليمي يساعد على التلقي والحفظ.

**الغرض:** يستخدم لوصف ميزة مستقلة في التسجيل التعليمي بدل جعلها جزءًا ضمنيًا من `muallim`.

**مرتبط به:** <span dir="ltr">[`muallim`](#muallim)، [`recitation_style`](#recitation_style)، [`hifz`](#hifz)</span>

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

**التعريف:** نمط تلاوة معد للتعليم وقد يتضمن تكرار الآيات أو إتاحة وقت للمتعلم للترديد.

**الغرض:** يستخدم لتصنيف التسجيل بحسب نمطه.

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

**التعريف:** نمط أداء بطيء يمد فيه الصوت وتستوفى أحكام التجويد بتطريب، وهو الوصف الذي تنشر به التسجيلات المؤداة على هذا النحو.

**الغرض:** يستخدم لتصنيف التسجيل بحسب نمطه.

- المجود نمط تسجيل، والتجويد علم يؤدى به كل نمط؛ فلا يستعمل أحد الاسمين مكان الآخر.

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

**التعريف:** نمط أداء متزن دون تطريب، على مرتبة الترتيل، وهو الوصف الذي تنشر به التسجيلات المؤداة على هذا النحو.

**الغرض:** يستخدم لتصنيف التسجيل بحسب نمطه.

- المرتل نمط تسجيل، والترتيل صفة الأداء نفسه؛ فلا يستعمل أحد الاسمين مكان الآخر.

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

**التعريف:** تصنيف للتسجيلات والتلاوات بحسب طريقة أدائها: مرتل أو مجود أو معلم، مستقل عن القراءة والرواية.

**الغرض:** يستخدم لتصنيف التسجيلات الصوتية بحسب طريقة الأداء أو الغرض منها.

**مرتبط به:** <span dir="ltr">[`murattal`](#murattal)، [`mujawwad`](#mujawwad)، [`muallim`](#muallim)، [`recitation`](#recitation)، [`recitation_pace`](#recitation_pace)، [`instructional_ayah_repetition`](#instructional_ayah_repetition)</span>

## التجويد — `tajwid`

<a id="alaqat_al_harfayn"></a>

### علاقة الحرفين — Alaqat al-Harfayn

<!-- source: standards/terminology/concepts/alaqat_al_harfayn.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`alaqat_al_harfayn`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`mutabaidan`](#mutabaidan)، [`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)، [`mutaqariban`](#mutaqariban)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | عَلَاقَة الحَرْفَيْن |
| تهجئات أخرى | <span dir="ltr">`letter_relations`، `alaqat_al_huruf`، `ilaqat_al_harfayn`</span> |
| مقابل إنجليزي | <span dir="ltr">`relation of two letters`</span> |

**التعريف:** نسبة الحرفين المتجاورين أحدهما إلى الآخر في المخرج والصفة: تماثل أو تجانس أو تقارب أو تباعد؛ وعليها يُبنى إدغام الأول في الثاني أو إظهاره.

**الغرض:** تستخدم تصنيفًا يوسم به الموضع الذي يقع فيه إدغام الحرفين أو إظهارهما، فيُعلم سبب الحكم لا الحكم وحده.

- العلاقة سبب، والإدغام والإظهار حكم يترتب عليها.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`izhar`](#izhar)، [`makhraj`](#makhraj)، [`sifat_al_huruf`](#sifat_al_huruf)، [`mutamathilan`](#mutamathilan)، [`mutajanisan`](#mutajanisan)، [`mutaqariban`](#mutaqariban)، [`mutabaidan`](#mutabaidan)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/59) — `59`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/62) — `62`

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

**التعريف:** صوت يخرج من الخيشوم مركب في جسم النون والميم لا عمل للسان فيه، ويختلف مقداره بحسب الحكم: أكمل ما يكون في المشدد والمدغم، ثم في المخفى، ثم في الساكن المظهر.

**الغرض:** تستخدم صفةً تُوسم بها مواضع النص التي تُمد فيها الغنة، كالمشددتين والإدغام بغنة والإخفاء والإقلاب، ليُتبع في التلوين والتعليم، ولأن مقدارها مما يختلف به الطريق.

- الغنة صفة صوت لا حكم في نفسها، فهي تلحق الإدغام والإخفاء والإقلاب ولا تقابلها.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`lahn_khafi`](#lahn_khafi)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/85) — `85`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `noon-mushaddadah`

<a id="hukm_al_tajwid"></a>

### حكم التجويد — Hukm al-Tajwid

<!-- source: standards/terminology/concepts/hukm_al_tajwid.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`hukm_al_tajwid`</span> |
| `plural` | <span dir="ltr">`hukm_al_tajwids`</span> |
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

**التعريف:** ما يجب في أداء الحرف عند حرف يليه أو عند سكون أو همز، من إظهار أو إدغام أو إقلاب أو إخفاء أو مد أو قلقلة أو تفخيم أو ترقيق، مما تقرره قواعد التجويد في موضع بعينه من النص.

**الغرض:** يستخدم أبًا لأحكام التجويد ووعاءً لسجلها، فتُنسب إليه مواضع النص التي يقع فيها حكم، ويُشار إلى الحكم بعينه بصف من السجل بدل اسم حر يختلف من محرك إلى محرك.

- الحكم ما يقع في الموضع، والتجويد العلم الذي يقرره.
- الحكم غير القاعدة: القاعدة شرط الحكم، والحكم أثرها في الموضع.

**مرتبط به:** <span dir="ltr">[`tajwid`](#tajwid)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`iqlab`](#iqlab)، [`ikhfa`](#ikhfa)، [`qalqalah`](#qalqalah)، [`madd`](#madd)، [`ghunnah`](#ghunnah)، [`tafkhim`](#tafkhim)، [`tarqiq`](#tarqiq)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)

<a id="idgham"></a>

### الإدغام — Idgham

<!-- source: standards/terminology/concepts/idgham.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`idgham`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`hukm_al_tajwid`](#hukm_al_tajwid)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِدْغَام |
| تهجئات أخرى | <span dir="ltr">`idghaam`، `idgam`، `edgham`، `idgham_bighunnah`، `idgham_bila_ghunnah`، `idgham_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`assimilation`، `merging`</span> |

**التعريف:** إدخال حرف ساكن في حرف متحرك بعده بحيث يصيران حرفًا واحدًا مشددًا، كاملًا كان الإدغام أو ناقصًا، بغنة أو بغير غنة.

**الغرض:** يستخدم قيمةً من قيم حكم التجويد، فيوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإدغام حكم، والتماثل والتجانس والتقارب علاقة بين الحرفين يقع الإدغام بسببها.

**مرتبط به:** <span dir="ltr">[`izhar`](#izhar)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`ghunnah`](#ghunnah)، [`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`mutamathilan`](#mutamathilan)، [`mutajanisan`](#mutajanisan)، [`mutaqariban`](#mutaqariban)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`meem_sakinah`](#meem_sakinah)، [`mutabaidan`](#mutabaidan)، [`noon_sakinah`](#noon_sakinah)، [`shaddah`](#shaddah)</span>

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
| الأب | <span dir="ltr">[`hukm_al_tajwid`](#hukm_al_tajwid)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِخْفَاء |
| تهجئات أخرى | <span dir="ltr">`ikhfaa`، `ikhfa'`، `ekhfa`، `ikhfa_haqiqi`، `ikhfa_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`concealment`</span> |

**التعريف:** النطق بالحرف الساكن على صفة بين الإظهار والإدغام، عاريًا عن التشديد مع بقاء الغنة؛ حقيقيًّا في النون الساكنة والتنوين عند حروفه الخمسة عشر، وشفويًّا في الميم الساكنة عند الباء.

**الغرض:** يستخدم قيمةً من قيم حكم التجويد، فيوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

**مرتبط به:** <span dir="ltr">[`izhar`](#izhar)، [`idgham`](#idgham)، [`ghunnah`](#ghunnah)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`hukm_al_tajwid`](#hukm_al_tajwid)</span>

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
| الأب | <span dir="ltr">[`hukm_al_tajwid`](#hukm_al_tajwid)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِقْلَاب |
| تهجئات أخرى | <span dir="ltr">`iqlaab`، `qalb`، `iqlab_qalb`، `eqlab`</span> |
| مقابل إنجليزي | <span dir="ltr">`conversion`</span> |

**التعريف:** قلب النون الساكنة أو التنوين ميمًا مخفاة بغنة عند الباء.

**الغرض:** يستخدم قيمةً من قيم حكم التجويد، فيوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإقلاب حكم في النطق، والميم الصغيرة العلامة التي يرسم بها في المصحف.

**مرتبط به:** <span dir="ltr">[`noon_sakinah`](#noon_sakinah)، [`tanwin`](#tanwin)، [`ghunnah`](#ghunnah)، [`small_meem`](#small_meem)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

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
| الأب | <span dir="ltr">[`hukm_al_tajwid`](#hukm_al_tajwid)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الإِظْهَار |
| تهجئات أخرى | <span dir="ltr">`izhaar`، `idhhar`، `idhar`، `ithhar`، `izhar_halqi`، `izhar_shafawi`</span> |
| مقابل إنجليزي | <span dir="ltr">`clear pronunciation`</span> |

**التعريف:** إخراج الحرف الساكن من مخرجه من غير غنة زائدة فيه، كإظهار النون الساكنة والتنوين عند حروف الحلق، وإظهار الميم الساكنة عند غير الباء والميم.

**الغرض:** يستخدم قيمةً من قيم حكم التجويد، فيوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- الإظهار حكم يقابل الإدغام والإخفاء، وليس غياب الحكم: الموضع الموسوم به موضع تحقق فيه سبب ثم لم يقع فيه إدغام ولا إخفاء.

**مرتبط به:** <span dir="ltr">[`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`iqlab`](#iqlab)، [`noon_sakinah`](#noon_sakinah)، [`meem_sakinah`](#meem_sakinah)، [`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`mutabaidan`](#mutabaidan)، [`mutajanisan`](#mutajanisan)، [`mutamathilan`](#mutamathilan)، [`mutaqariban`](#mutaqariban)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/64) — `64`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/65) — `65`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-halqi-noon`

<a id="lahn"></a>

### اللحن — Lahn

<!-- source: standards/terminology/concepts/lahn.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`lahn`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`lahn_jali`](#lahn_jali)، [`lahn_khafi`](#lahn_khafi)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | اللَّحْن |
| تهجئات أخرى | <span dir="ltr">`lahn_error`، `tajwid_error`</span> |
| مقابل إنجليزي | <span dir="ltr">`recitation error`</span> |

**التعريف:** الخطأ في قراءة القرآن والميل بها عن الصواب، جليًّا كان أو خفيًّا.

**الغرض:** يستخدم تصنيفًا لما تبلغ عنه أدوات تقويم التلاوة، فيُفرق بين ما يخل بالمبنى أو المعنى وما يخل بكمال الأداء.

- اللحن خطأ في الأداء، والوجه اختلاف جائز فيه.

**مرتبط به:** <span dir="ltr">[`lahn_jali`](#lahn_jali)، [`lahn_khafi`](#lahn_khafi)، [`tajwid`](#tajwid)، [`tilawah`](#tilawah)، [`wajh`](#wajh)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/8) — `8`

<a id="lahn_jali"></a>

### اللحن الجلي — Lahn Jali

<!-- source: standards/terminology/concepts/lahn_jali.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`lahn_jali`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`lahn`](#lahn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | اللَّحْن الجَلِيّ |
| تهجئات أخرى | <span dir="ltr">`lahn_jaliy`، `lahn_jalee`، `clear_error`</span> |
| مقابل إنجليزي | <span dir="ltr">`plain error`</span> |

**التعريف:** خطأ يطرأ على اللفظ فيخل بالمبنى أو المعنى، كإبدال حرف بحرف أو حركة بحركة، ويدركه العالم وغيره.

**الغرض:** يستخدم قيمةً من قيم اللحن، فيُميز في تقارير التقويم الخطأ الذي يجب تصحيحه على كل قارئ.

**مرتبط به:** <span dir="ltr">[`lahn`](#lahn)، [`lahn_khafi`](#lahn_khafi)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/9) — `9`

<a id="lahn_khafi"></a>

### اللحن الخفي — Lahn Khafi

<!-- source: standards/terminology/concepts/lahn_khafi.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`lahn_khafi`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`lahn`](#lahn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | اللَّحْن الخَفِيّ |
| تهجئات أخرى | <span dir="ltr">`lahn_khafiy`، `lahn_khafee`</span> |
| مقابل إنجليزي | <span dir="ltr">`subtle error`</span> |

**التعريف:** خطأ يطرأ على اللفظ فيخل بكمال الأداء دون المبنى والمعنى، كترك الغنة أو تقصير المد، ولا يدركه إلا أهل الفن.

**الغرض:** يستخدم قيمةً من قيم اللحن، فيُميز في تقارير التقويم ما يخص إتقان التجويد عما يخص صحة اللفظ.

**مرتبط به:** <span dir="ltr">[`lahn`](#lahn)، [`lahn_jali`](#lahn_jali)، [`ghunnah`](#ghunnah)، [`madd`](#madd)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/10) — `10`

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

**التعريف:** إطالة الصوت بحرف من حروف المد الثلاثة: الألف الساكنة بعد فتح، والواو الساكنة بعد ضم، والياء الساكنة بعد كسر؛ أصليًّا كان المد لا يقوم الحرف إلا به، أو فرعيًّا بسبب همز أو سكون.

**الغرض:** يستخدم تصنيفًا تتفرع عليه أنواع المد، فيوسم به موضع النص مع نوعه ومقداره؛ ولأن مقادير المدود مما يختلف به الطريق، فهي مما يُبين في وصف التسجيل والمصحف.

- حروف المد غير حروف اللين وإن اجتمعتا في الواو والياء: حرف المد ساكن بعد حركة تجانسه، وحرف اللين ساكن بعد فتح.
- المد الحكم، والمدة العلامة التي تدل عليه في المصحف.

**مرتبط به:** <span dir="ltr">[`maddah`](#maddah)، [`madd_tabii`](#madd_tabii)، [`madd_muttasil`](#madd_muttasil)، [`madd_munfasil`](#madd_munfasil)، [`madd_lazim`](#madd_lazim)، [`madd_al_badal`](#madd_al_badal)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_silah`](#madd_al_silah)، [`madd_al_lin`](#madd_al_lin)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`lahn_khafi`](#lahn_khafi)، [`usul`](#usul)</span>

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

**التعريف:** مد سببه همزة قبل حرف المد، أُبدل فيه حرف المد من همزة ساكنة، كما في «آمن» و«أوتوا» و«إيمان»؛ ومقداره حركتان عند حفص، ويُزاد عند ورش.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** مد الألف عوضًا عن تنوين الفتح عند الوقف على الكلمة، ومقداره حركتان.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** مد الواو أو الياء الساكنة المفتوح ما قبلها عند الوقف على الكلمة بسكون عارض، كما في «خوف» و«بيت».

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** مد ناشئ عن صلة هاء الضمير بواو أو ياء إذا وقعت بين متحركين؛ صغرى إن لم يقع بعدها همز، وكبرى إن وقع.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** مد سببه سكون عارض في الوقف بعد حرف المد، ويجوز فيه القصر والتوسط والطول.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

> الاشتقاق يعطي `madd_arid_li_al_sukun` بفصل لام الجر عن أداة التعريف، على ما يقرره القسم 8، والصورة الملحومة `lilsukun` محالة في `alternative_spellings`.

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

**التعريف:** مد فرعي سببه سكون أصلي ثابت وصلًا ووقفًا بعد حرف المد، في كلمة أو في حرف من فواتح السور، مثقلًا كان بالإدغام أو مخففًا؛ ومقداره ست حركات.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`huruf_muqattaah`](#huruf_muqattaah)، [`sukun`](#sukun)</span>

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

**التعريف:** مد فرعي سببه همزة في أول الكلمة التالية لحرف المد، وهو جائز: يُقصر ويُمد بحسب الرواية والطريق.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** مد فرعي سببه همزة بعد حرف المد في كلمة واحدة، وهو واجب عند القراء جميعًا، وتختلف مقاديره بحسب الرواية والطريق.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

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

**التعريف:** المد الذي لا تقوم ذات حرف المد إلا به، ولا يتوقف على سبب من همز أو سكون، ومقداره حركتان.

**الغرض:** يستخدم قيمةً من قيم المد، فيوسم به موضع النص مع مقداره، ويُقرأ منه ما يختلف به الطريق في وصف التسجيل والمصحف.

**مرتبط به:** <span dir="ltr">[`madd`](#madd)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_silah`](#madd_al_silah)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/100) — `100`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `madd-tabee-kalimi`

<a id="makhraj"></a>

### المخرج — Makhraj

<!-- source: standards/terminology/concepts/makhraj.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`makhraj`</span> |
| `plural` | <span dir="ltr">`makhrajs`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المَخْرَج |
| الجمع | مخارج |
| تهجئات أخرى | <span dir="ltr">`makhraj_al_harf`، `makharij`، `makhaarij`</span> |
| مقابل إنجليزي | <span dir="ltr">`point of articulation`</span> |

**التعريف:** موضع خروج الحرف الذي يتميز به عن غيره، من الجوف أو الحلق أو اللسان أو الشفتين أو الخيشوم.

**الغرض:** يستخدم في التعليم وتحليل النطق، ولتقرير علاقة الحرفين المتجاورين التي يُبنى عليها الإدغام.

**مرتبط به:** <span dir="ltr">[`sifat_al_huruf`](#sifat_al_huruf)، [`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`letter`](#letter)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/6) — `6`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/40) — `40`

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

**التعريف:** ميم خالية من الحركة، ثابتة لفظًا وخطًّا، تقع في وسط الكلمة أو آخرها.

**الغرض:** تستخدم موضعًا تتفرع عليه الأحكام الشفوية الثلاثة، الإدغام والإخفاء والإظهار، في محركات التجويد.

- الميم الساكنة غير الميم المقلوبة عن النون في الإقلاب وإن اتحد صوتهما.

**مرتبط به:** <span dir="ltr">[`noon_sakinah`](#noon_sakinah)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`ikhfa`](#ikhfa)، [`ghunnah`](#ghunnah)، [`hukm_al_tajwid`](#hukm_al_tajwid)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/63) — `63`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/66) — `66`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/68) — `68`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `izhar-shafawi-meem`

<a id="mutabaidan"></a>

### المتباعدان — Mutabaidan

<!-- source: standards/terminology/concepts/mutabaidan.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutabaidan`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَبَاعِدَان |
| تهجئات أخرى | <span dir="ltr">`mutabaidain`، `mutabaidayn`، `mutaba'idan`</span> |

**التعريف:** حرفان تباعدا مخرجًا واختلفا صفة، ولا إدغام بينهما.

**الغرض:** يستخدم قيمةً من قيم علاقة الحرفين، فيُقرأ منه سبب الإدغام أو الإظهار في الموضع بدل استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

<a id="mutajanisan"></a>

### المتجانسان — Mutajanisan

<!-- source: standards/terminology/concepts/mutajanisan.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutajanisan`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَجَانِسَان |
| تهجئات أخرى | <span dir="ltr">`mutajanisain`، `mutajanisayn`، `mutajanisan_saghir`</span> |

**التعريف:** حرفان اتحدا مخرجًا واختلفا صفة، كالدال والتاء في «قد تبين».

**الغرض:** يستخدم قيمةً من قيم علاقة الحرفين، فيُقرأ منه سبب الإدغام أو الإظهار في الموضع بدل استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

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
| الأب | <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَمَاثِلَان |
| تهجئات أخرى | <span dir="ltr">`mutamathilain`، `mutamathilayn`، `mithlayn`، `mutamathilan_saghir`</span> |

**التعريف:** حرفان اتحدا مخرجًا وصفة، كالباء في «اضرب بعصاك».

**الغرض:** يستخدم قيمةً من قيم علاقة الحرفين، فيُقرأ منه سبب الإدغام أو الإظهار في الموضع بدل استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/58) — `58`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `mutamathilain-idgham-kamil`

<a id="mutaqariban"></a>

### المتقاربان — Mutaqariban

<!-- source: standards/terminology/concepts/mutaqariban.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`mutaqariban`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | المُتَقَارِبَان |
| تهجئات أخرى | <span dir="ltr">`mutaqaribain`، `mutaqaribayn`، `mutaqariban_saghir`</span> |

**التعريف:** حرفان تقاربا مخرجًا أو صفة أو فيهما معًا، كاللام والراء في «قل رب».

**الغرض:** يستخدم قيمةً من قيم علاقة الحرفين، فيُقرأ منه سبب الإدغام أو الإظهار في الموضع بدل استنباطه من الحرفين في كل مرة.

**مرتبط به:** <span dir="ltr">[`alaqat_al_harfayn`](#alaqat_al_harfayn)، [`idgham`](#idgham)، [`izhar`](#izhar)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/62) — `62`

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

**التعريف:** نون خالية من الحركة، تثبت لفظًا وخطًا ووصلًا ووقفًا.

**الغرض:** تستخدم موضعًا تتفرع عليه أحكام الإظهار والإدغام والإقلاب والإخفاء في محركات التجويد.

**مرتبط به:** <span dir="ltr">[`tajwid`](#tajwid)، [`tanwin`](#tanwin)، [`izhar`](#izhar)، [`idgham`](#idgham)، [`iqlab`](#iqlab)، [`ikhfa`](#ikhfa)، [`meem_sakinah`](#meem_sakinah)، [`ghunnah`](#ghunnah)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`small_meem`](#small_meem)، [`sukun`](#sukun)، [`tanwin_al_damm`](#tanwin_al_damm)، [`tanwin_al_fath`](#tanwin_al_fath)، [`tanwin_al_kasr`](#tanwin_al_kasr)</span>

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
| الأب | <span dir="ltr">[`hukm_al_tajwid`](#hukm_al_tajwid)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | القَلْقَلَة |
| تهجئات أخرى | <span dir="ltr">`qalqala`، `qalqalah_sughra`، `qalqalah_kubra`، `qalqalh`</span> |
| مقابل إنجليزي | <span dir="ltr">`echoing`</span> |

**التعريف:** اضطراب في صوت الحرف الساكن عند النطق به حتى تُسمع له نبرة قوية، في حروف «قطب جد»، ويقوى بحسب موضع الحرف من الكلمة والوقف عليه.

**الغرض:** يستخدم قيمةً من قيم حكم التجويد، فيوسم به موضع النص في التحليل والتلوين والتعليم، وتتفرع تحته أنواعه في سجل الأحكام.

- القلقلة صفة من صفات الحروف التي لا ضد لها، وتُعد حكمًا حين يُوسم بها الموضع الذي تظهر فيه.

**مرتبط به:** <span dir="ltr">[`sukun`](#sukun)، [`sifat_al_huruf`](#sifat_al_huruf)، [`hukm_al_tajwid`](#hukm_al_tajwid)</span>

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

**التعريف:** قطع الصوت زمنًا يسيرًا من غير تنفس ثم متابعة القراءة.

**الغرض:** يستخدم لتمثيل مواضع السكت وخصائصها في النص أو التلاوة.

- السكتة الوقفة نفسها، وعلامة السكتة رسم في المصحف يدل عليها.

**مرتبط به:** <span dir="ltr">[`saktah_mark`](#saktah_mark)، [`waqf`](#waqf)، [`tajwid`](#tajwid)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/126) — `126`

<a id="sifat_al_huruf"></a>

### صفات الحروف — Sifat al-Huruf

<!-- source: standards/terminology/concepts/sifat_al_huruf.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sifat_al_huruf`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | صِفَات الحُرُوف |
| تهجئات أخرى | <span dir="ltr">`sifat`، `sifaat`، `sifat_al_hurouf`، `sifaat_al_huroof`</span> |
| مقابل إنجليزي | <span dir="ltr">`attributes of the letters`</span> |

**التعريف:** كيفيات تعرض للحرف عند النطق به فتميزه عن مشاركه في المخرج؛ منها ما له ضد كالهمس والجهر والشدة والرخاوة، ومنها ما لا ضد له كالصفير والقلقلة.

**الغرض:** تستخدم في التعليم وتحليل النطق، ولتقرير التجانس والتقارب بين الحرفين.

- الصفة ما يُعرض للحرف في مخرجه، والتفخيم والترقيق أثر يترتب على بعض الصفات.

**مرتبط به:** <span dir="ltr">[`makhraj`](#makhraj)، [`qalqalah`](#qalqalah)، [`tafkhim`](#tafkhim)، [`tarqiq`](#tarqiq)، [`alaqat_al_harfayn`](#alaqat_al_harfayn)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/7) — `7`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/69) — `69`
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/70) — `70`

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

**التعريف:** سِمَن يدخل على صوت الحرف فيمتلئ الفم بصداه؛ لازم في حروف الاستعلاء، وعارض في الراء ولام لفظ الجلالة والألف تبعًا لما قبلها.

**الغرض:** يستخدم لوسم مواضع الحروف المفخمة تفخيمًا عارضًا في التلوين والتعليم، وإليه تُنسب مراتب التفخيم في سجل الأحكام.

- التفخيم صفة في صوت الحرف، والاستعلاء صفة المخرج التي يلزم منها التفخيم.

**مرتبط به:** <span dir="ltr">[`tarqiq`](#tarqiq)، [`sifat_al_huruf`](#sifat_al_huruf)، [`hukm_al_tajwid`](#hukm_al_tajwid)</span>

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

**التعريف:** علم أداء حروف القرآن من مخارجها وإعطائها حقوقها ومستحقاتها من الصفات والأحكام.

**الغرض:** يمثل العلم الذي تنتمي إليه قواعد التجويد وأحكامه وتلوينات العرض في التطبيقات، فتنسب إليه القاعدة في المحرك أو القاموس.

- التجويد علم، والمجود نمط تسجيل؛ فلا يستعمل أحد الاسمين مكان الآخر.

**مرتبط به:** <span dir="ltr">[`recitation`](#recitation)، [`waqf`](#waqf)، [`mujawwad`](#mujawwad)، [`noon_sakinah`](#noon_sakinah)، [`hukm_al_tajwid`](#hukm_al_tajwid)، [`lahn`](#lahn)، [`saktah`](#saktah)</span>

**المصادر:**

- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine)
- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/4) — `4`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/190`

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

**التعريف:** نحول يدخل على صوت الحرف فلا يمتلئ الفم بصداه؛ لازم في حروف الاستفال، وعارض في الراء ولام لفظ الجلالة.

**الغرض:** يستخدم لوسم مواضع الحروف المرققة ترقيقًا عارضًا في التلوين والتعليم، مقابلًا للتفخيم.

**مرتبط به:** <span dir="ltr">[`tafkhim`](#tafkhim)، [`sifat_al_huruf`](#sifat_al_huruf)، [`hukm_al_tajwid`](#hukm_al_tajwid)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/88) — `88`
- [Rule-driven tajweed engine — rule corpus](https://github.com/quranpedia/tajweed-engine) — `raa-tarqeeq`

## الوقف — `waqf`

<a id="sabab_al_waqf"></a>

### سبب الوقف — Sabab al-Waqf

<!-- source: standards/terminology/concepts/sabab_al_waqf.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sabab_al_waqf`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`waqf_idtirari`](#waqf_idtirari)، [`waqf_ikhtibari`](#waqf_ikhtibari)، [`waqf_ikhtiyari`](#waqf_ikhtiyari)، [`waqf_intizari`](#waqf_intizari)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | سَبَب الوَقْف |
| تهجئات أخرى | <span dir="ltr">`waqf_cause`، `aqsam_al_waqf`، `waqf_by_cause`</span> |
| مقابل إنجليزي | <span dir="ltr">`cause of the stop`</span> |

**التعريف:** تقسيم الوقف باعتبار ما دعا القارئ إليه: اضطرار، أو اختبار، أو انتظار، أو اختيار.

**الغرض:** يستخدم تصنيفًا لموضع الوقف الواقع في تلاوة أو تسجيل، فيُعلم أعن قصد وقع أم عن عارض؛ وهو غير حكم الموضع نفسه وغير علامته.

- سبب الوقف صفة في الوقف الواقع، وحكم الوقف صفة في الموضع، وعلامة الوقف ما رُسم في المصحف.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_ruling`](#waqf_ruling)، [`waqf_mark`](#waqf_mark)، [`waqf_idtirari`](#waqf_idtirari)، [`waqf_ikhtibari`](#waqf_ikhtibari)، [`waqf_intizari`](#waqf_intizari)، [`waqf_ikhtiyari`](#waqf_ikhtiyari)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/115) — `115`

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

**التعريف:** قطع القراءة عند موضع من النص وفق أحكام الوقف والابتداء.

**الغرض:** يمثل المفهوم العام للوقف، بينما تمثل `waqf_mark` العلامات المطبوعة التي ترشد إليه.

**مرتبط به:** <span dir="ltr">[`waqf_mark`](#waqf_mark)، [`waqf_ruling`](#waqf_ruling)، [`waqf_mark_type`](#waqf_mark_type)، [`tajwid`](#tajwid)، [`saktah`](#saktah)، [`madd_al_iwad`](#madd_al_iwad)، [`madd_al_lin`](#madd_al_lin)، [`madd_arid_li_al_sukun`](#madd_arid_li_al_sukun)، [`sabab_al_waqf`](#sabab_al_waqf)، [`waqf_al_muanaqah`](#waqf_al_muanaqah)، [`waqf_hasan`](#waqf_hasan)، [`waqf_idtirari`](#waqf_idtirari)، [`waqf_ikhtibari`](#waqf_ikhtibari)، [`waqf_ikhtiyari`](#waqf_ikhtiyari)، [`waqf_intizari`](#waqf_intizari)، [`waqf_jaiz_mustawi_al_tarafayn`](#waqf_jaiz_mustawi_al_tarafayn)، [`waqf_jaiz_waqf_awla`](#waqf_jaiz_waqf_awla)، [`waqf_jaiz_wasl_awla`](#waqf_jaiz_wasl_awla)، [`waqf_kafi`](#waqf_kafi)، [`waqf_lazim`](#waqf_lazim)، [`waqf_mamnu`](#waqf_mamnu)، [`waqf_qabih`](#waqf_qabih)، [`waqf_tamm`](#waqf_tamm)</span>

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

**التعريف:** ما أفاد معنًى وتعلق بما بعده لفظًا ومعنًى.

**الغرض:** يستخدم قيمةً من قيم حكم الوقف، فيوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/124) — `124`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

<a id="waqf_idtirari"></a>

### الوقف الاضطراري — Waqf Idtirari

<!-- source: standards/terminology/concepts/waqf_idtirari.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_idtirari`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الاِضْطِرَارِيّ |
| تهجئات أخرى | <span dir="ltr">`idtirari`، `waqf_idtirary`، `waqf_idhtirari`</span> |

**التعريف:** ما يعرض للقارئ بسبب يضطره إلى الوقف، من ضيق نفس أو عطاس أو نسيان، فيقف على أي كلمة ثم يبتدئ بما يصح الابتداء به.

**الغرض:** يستخدم قيمةً من قيم سبب الوقف، فيُوسم به الوقف الواقع في التلاوة عند تحليلها أو تعليمها.

**مرتبط به:** <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/117) — `117`

<a id="waqf_ikhtibari"></a>

### الوقف الاختباري — Waqf Ikhtibari

<!-- source: standards/terminology/concepts/waqf_ikhtibari.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_ikhtibari`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الاِخْتِبَارِيّ |
| تهجئات أخرى | <span dir="ltr">`ikhtibari`، `waqf_ikhtibary`</span> |

**التعريف:** ما يقع لبيان المقطوع والموصول والثابت والمحذوف من الرسم، عند سؤال أو تعليم.

**الغرض:** يستخدم قيمةً من قيم سبب الوقف، فيُوسم به الوقف الواقع في التلاوة عند تحليلها أو تعليمها.

**مرتبط به:** <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/119) — `119`

<a id="waqf_ikhtiyari"></a>

### الوقف الاختياري — Waqf Ikhtiyari

<!-- source: standards/terminology/concepts/waqf_ikhtiyari.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_ikhtiyari`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الاِخْتِيَارِيّ |
| تهجئات أخرى | <span dir="ltr">`ikhtiyari`، `waqf_ikhtiyary`</span> |

**التعريف:** ما يقصده القارئ باختياره من غير سبب يعرض، وهو الذي تجري عليه أحكام التام والكافي والحسن والقبيح.

**الغرض:** يستخدم قيمةً من قيم سبب الوقف، فيُوسم به الوقف الواقع في التلاوة عند تحليلها أو تعليمها.

**مرتبط به:** <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)، [`waqf`](#waqf)، [`waqf_ruling`](#waqf_ruling)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/120) — `120`

<a id="waqf_intizari"></a>

### الوقف الانتظاري — Waqf Intizari

<!-- source: standards/terminology/concepts/waqf_intizari.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`waqf_intizari`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَقْف الاِنْتِظَارِيّ |
| تهجئات أخرى | <span dir="ltr">`intizari`، `waqf_intizary`، `waqf_intidhari`</span> |

**التعريف:** ما يقع على الكلمة التي فيها خلاف بين القراءات، ليستوفي القارئ أوجهها عند جمع القراءات.

**الغرض:** يستخدم قيمةً من قيم سبب الوقف، فيُوسم به الوقف الواقع في التلاوة عند تحليلها أو تعليمها.

**مرتبط به:** <span dir="ltr">[`sabab_al_waqf`](#sabab_al_waqf)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/118) — `118`

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

**التعريف:** ما تم معناه وتعلق بما بعده معنًى لا لفظًا.

**الغرض:** يستخدم قيمةً من قيم حكم الوقف، فيوسم به الموضع في التعليم والتحليل.

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

**التعريف:** تصنيف لما ترشد إليه علامة الوقف المرسومة في المصحف من لزوم أو منع أو جواز.

**الغرض:** يوفر مجموعة قيم موحدة تتفرع عليها التطبيقات، بدل قراءة صورة الرمز نفسه.

- نوع العلامة ما ترشد إليه العلامة المرسومة، وحكم الوقف صفة الموضع نفسه ولو لم تُرسم عليه علامة.

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

**التعريف:** ما لم يفد معنًى، أو أفاد معنًى غير مراد.

**الغرض:** يستخدم قيمةً من قيم حكم الوقف، فيوسم به الموضع في التعليم والتحليل.

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

**التعريف:** تصنيف الموضع نفسه من جهة تمام المعنى عنده، لا من جهة العلامة المرسومة عليه.

**الغرض:** يستخدم في التعليم والتحليل النحوي والدلالي للوقف.

- حكم الوقف صفة الموضع، ونوع علامة الوقف ما ترشد إليه العلامة المرسومة؛ وقد يكون للموضع حكم ولا علامة عليه.

**مرتبط به:** <span dir="ltr">[`waqf`](#waqf)، [`waqf_mark_type`](#waqf_mark_type)، [`waqf_tamm`](#waqf_tamm)، [`waqf_kafi`](#waqf_kafi)، [`waqf_hasan`](#waqf_hasan)، [`waqf_qabih`](#waqf_qabih)، [`sabab_al_waqf`](#sabab_al_waqf)، [`waqf_ikhtiyari`](#waqf_ikhtiyari)</span>

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

**التعريف:** ما تم معناه ولم يتعلق بما بعده لفظًا ولا معنًى.

**الغرض:** يستخدم قيمةً من قيم حكم الوقف، فيوسم به الموضع في التعليم والتحليل.

**مرتبط به:** <span dir="ltr">[`waqf_ruling`](#waqf_ruling)، [`waqf`](#waqf)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/121) — `121`
- [النشر في القراءات العشر](https://files.turath.io/books-v3/22642.json) — `1/226`

## اللغة — `linguistics`

<a id="fil"></a>

### الفعل — Fil

<!-- source: standards/terminology/concepts/fil.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`fil`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الفِعْل |
| مقابل إنجليزي | <span dir="ltr">`Verb`</span> |

**التعريف:** ما دل على معنى في نفسه مقترن بزمان، ويتصرف بالماضي والمضارع والأمر.

**الغرض:** يستخدم قيمةً من قيم قسم الكلمة، وعليه تعلق السمات الصرفية الخاصة بالفعل من الزمن والبناء للمعلوم أو المجهول والوزن.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`morphology`](#morphology)</span>

<a id="harf_al_mana"></a>

### حرف المعنى — Harf al-Mana

<!-- source: standards/terminology/concepts/harf_al_mana.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`harf_al_mana`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | حَرْف المَعْنَى |
| مقابل إنجليزي | <span dir="ltr">`Particle`</span> |

**التعريف:** ما دل على معنى في غيره، كحروف الجر والعطف والنفي والاستفهام.

**الغرض:** يستخدم قيمةً من قيم قسم الكلمة، وتحته تندرج وسوم الحروف التفصيلية في مدونات الصرف القرآني.

- حرف المعنى قسم من أقسام الكلمة، وحرف المبنى — وهو `letter` — وحدة من النص المكتوب.

> يسمى بالاسم الكامل لأن `harf` وحده اسم الحرف المبنى، وهو وحدة من وحدات الكتابة لا قسم من أقسام الكلمة؛ والقرار في سجل القرارات.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`letter`](#letter)</span>

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

**التعريف:** بيان الوظائف النحوية للكلمات وعلاماتها وعلاقاتها في التركيب.

**الغرض:** يستخدم لربط كلمات الآيات بالتحليل النحوي والوظائف الإعرابية.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)، [`morphology`](#morphology)، [`word`](#word)</span>

<a id="ism"></a>

### الاسم — Ism

<!-- source: standards/terminology/concepts/ism.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`ism`</span> |
| `kind` | <span dir="ltr">`classification_value`</span> |
| الأب | <span dir="ltr">[`part_of_speech`](#part_of_speech)</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الاِسْم |
| مقابل إنجليزي | <span dir="ltr">`Noun`</span> |

**التعريف:** ما دل على معنى في نفسه غير مقترن بزمان، وتدخل فيه الأسماء والصفات والضمائر وأسماء الإشارة والموصولات.

**الغرض:** يستخدم قيمةً من قيم قسم الكلمة، وتحته تندرج الوسوم التفصيلية التي تستعملها مدونات الصرف القرآني.

**مرتبط به:** <span dir="ltr">[`part_of_speech`](#part_of_speech)</span>

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

**التعريف:** الصيغة المعجمية الأساسية التي ترد إليها صورة الكلمة المصرفة.

**الغرض:** تستخدم لتجميع الصور التصريفية المختلفة تحت مدخل معجمي واحد.

**مرتبط به:** <span dir="ltr">[`root`](#root)، [`stem`](#stem)، [`morphology`](#morphology)، [`wazn`](#wazn)</span>

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

**التعريف:** أصغر وحدة في الكلمة تحمل معنى أو وظيفة صرفية، كالسابقة واللاحقة والجذع.

**الغرض:** تستخدم لتمثيل تقسيم الكلمة القرآنية إلى أجزائها الصرفية، وهو المستوى الذي تنسب إليه السمات الصرفية والوسوم في مدونات التحليل.

- الوحدة الصرفية جزء من الكلمة، و`token` وحدة تقسيم قد تساوي الكلمة أو تزيد عليها.

> الاسم `segment` يعني في مدونات الصرف القرآني الوحدة الصرفية، ويعني في واجهات الصوت توقيت الكلمة؛ فلا يُحَلّ الاسم وحده إلى شيء، و`word_segment` يُحَلّ إلى هذا المدخل، والمعنى الصوتي في `word_timing`.

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

**التعريف:** تحليل بنية الكلمة وصيغتها وما تحمله من خصائص صرفية.

**الغرض:** يستخدم لتمثيل السمات الصرفية للكلمات أو `tokens`.

**مرتبط به:** <span dir="ltr">[`morpheme`](#morpheme)، [`root`](#root)، [`lemma`](#lemma)، [`stem`](#stem)، [`part_of_speech`](#part_of_speech)، [`wazn`](#wazn)، [`fil`](#fil)، [`irab`](#irab)</span>

<a id="part_of_speech"></a>

### قسم الكلمة — Part of Speech

<!-- source: standards/terminology/concepts/part_of_speech.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`part_of_speech`</span> |
| `kind` | <span dir="ltr">`classification`</span> |
| القيم | <span dir="ltr">[`fil`](#fil)، [`harf_al_mana`](#harf_al_mana)، [`ism`](#ism)</span> |
| الأصل | <span dir="ltr">`borrowed`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | قِسْم الكَلِمَة |
| تهجئات أخرى | <span dir="ltr">`pos`</span> |

**التعريف:** تصنيف الكلمة أو الوحدة الصرفية بحسب بابها النحوي، كالاسم والفعل والحرف وما يتفرع عنها.

**الغرض:** يستخدم وسمًا أساسيًا في التحليل الصرفي والنحوي، وعليه يقوم البحث بالوسم والتصفية وبناء التحليل الإعرابي.

> القسمة الثلاثية هي المستوى الذي يثبته المعيار. أما الوسوم التفصيلية التي تستعملها مدونات الصرف القرآني — وهي عشرات — فبيانات تندرج تحت هذه القيم الثلاث، ولا تفرد مداخل في القاموس.

**مرتبط به:** <span dir="ltr">[`morphology`](#morphology)، [`irab`](#irab)، [`morpheme`](#morpheme)، [`fil`](#fil)، [`harf_al_mana`](#harf_al_mana)، [`ism`](#ism)</span>

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

**التعريف:** الأصل الصرفي الذي ترد إليه الكلمة لبيان اشتقاقها وصلتها بالكلمات الأخرى.

**الغرض:** يستخدم للبحث الصرفي والتحليل اللغوي وتجميع الكلمات ذات الأصل المشترك.

**مرتبط به:** <span dir="ltr">[`lemma`](#lemma)، [`stem`](#stem)، [`morphology`](#morphology)، [`wazn`](#wazn)</span>

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

**التعريف:** ما يبقى من الكلمة بعد نزع السوابق واللواحق، وتلحق به الزوائد الصرفية.

**الغرض:** يستخدم في التحليل الصرفي مستوى وسطًا بين صورة الكلمة وجذرها، فبعض المدونات تسجل الجذع ولا تسجل الجذر، وبعضها تسجلهما معًا.

- الجذر أصل اشتقاقي مجرد، والجذع صورة قائمة في الكلمة بعد نزع الزوائد.

**مرتبط به:** <span dir="ltr">[`root`](#root)، [`lemma`](#lemma)، [`morpheme`](#morpheme)، [`morphology`](#morphology)، [`wazn`](#wazn)</span>

<a id="wazn"></a>

### الوزن — Wazn

<!-- source: standards/terminology/concepts/wazn.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`wazn`</span> |
| `plural` | <span dir="ltr">`wazns`</span> |
| `kind` | <span dir="ltr">`unit`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | الوَزْن |
| الجمع | أَوْزَان |
| تهجئات أخرى | <span dir="ltr">`wazan`، `awzan`</span> |
| مقابل إنجليزي | <span dir="ltr">`morphological pattern`، `pattern`</span> |

**التعريف:** صورة الكلمة الصرفية ممثلةً بحروف «فعل» وما يلحقها من زوائد، تبين بناءها بصرف النظر عن جذرها.

**الغرض:** يستخدم في التحليل الصرفي والبحث بالبناء، فتُجمع كلمات على وزن واحد وإن اختلفت جذورها.

- الوزن صورة البناء، والجذر مادته، والجذع الكلمة مجردةً من اللواصق.

**مرتبط به:** <span dir="ltr">[`root`](#root)، [`stem`](#stem)، [`morphology`](#morphology)، [`lemma`](#lemma)</span>

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

**التعريف:** نقل معاني القرآن إلى لغة أخرى في مادة صوتية أو منطوقة.

**الغرض:** يستخدم لتمييز المحتوى الصوتي لترجمة المعاني عن الترجمة النصية وعن التلاوة القرآنية.

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

**التعريف:** نقل معاني القرآن إلى لغة أخرى، وليست الترجمة قرآنًا بلفظه.

**الغرض:** تستخدم لربط نصوص ترجمة المعاني بالآيات واللغات والمترجمين والمصادر.

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

**التعريف:** من نُسبت إليه ترجمة لمعاني القرآن إلى لغة أخرى، فردًا كان أو هيئة.

**الغرض:** يستخدم لنسبة الترجمة إلى صاحبها، وتمييزه عن الناشر والمراجع ومصدر النص.

- المترجم غير المفسر وإن استند في ترجمته إلى تفسير.

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

**التعريف:** تمثيل حروف نظام كتابي بحروف نظام آخر وفق قواعد محددة، دون ترجمة المعنى.

**الغرض:** يستخدم لتوفير تمثيل قابل للقراءة بنظام كتابي آخر أو للتحويل المنهجي بين أنظمة الكتابة.

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

**التعريف:** ترجمة تعطي كل كلمة من كلمات الآية معناها في لغة أخرى على حدة، بترتيب كلمات الأصل.

**الغرض:** تستخدم في العرض التعليمي والتعلم، وتُربط بالكلمة بمفتاحها لا بالآية.

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

**التعريف:** من نسب إليه تفسير للقرآن، تأليفًا أو رواية.

**الغرض:** يستخدم لنسبة التفسير إلى صاحبه، فيتميز صاحب القول عن الكتاب الذي نقل فيه وعن محققه وناشره.

- المفسر صاحب القول، وقد ينقل قوله في كتاب لغيره.

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

**التعريف:** بيان معاني القرآن وشرح ألفاظه وما يرشد إليه من أحكام وهدايات بحسب أصول التفسير.

**الغرض:** يستخدم لتمثيل كتب ومحتوى التفسير وربط مقاطعه بالآيات والسور والمصادر.

**مرتبط به:** <span dir="ltr">[`tafsir_mathur`](#tafsir_mathur)، [`tafsir_al_ray`](#tafsir_al_ray)، [`mufassir`](#mufassir)، [`gharib_al_quran`](#gharib_al_quran)، [`ayah`](#ayah)، [`maqasid_al_surah`](#maqasid_al_surah)، [`tadabbur`](#tadabbur)، [`translation`](#translation)</span>

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

**التعريف:** بيان معاني القرآن بالاجتهاد والنظر بعد معرفة كلام العرب وأساليبه وأصول التفسير، محمودًا كان الاجتهاد أو مذمومًا.

**الغرض:** يستخدم نوعًا للمحتوى المؤلف الذي يُنسب إلى صاحبه قولًا، فيتميز عما يُنقل بإسناد.

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

**التعريف:** ما فسر به القرآن من القرآن نفسه، أو من السنة، أو من قول الصحابة والتابعين، منقولًا بإسناده.

**الغرض:** يستخدم محتوى يربط بالآية ويحمل معه ناقله ودرجة النقل، فلا يعامل معاملة نص التفسير المؤلف الذي ينسب إلى كتاب واحد.

- التفسير المأثور منقول بإسناد، والتفسير المؤلف قول صاحب الكتاب.
- الأثر الواحد ليس مفهومًا في هذا المعيار؛ المفهوم هو نوع المحتوى المرتب على الآية.

> العنوان الأشهر «التَّفْسِير بِالمَأْثُور»، واشتقاقه يلحم حرف الجر بالاسم فيعطي `tafsir_bialmathur`. والاسم المثبت هو الصورة الوصفية، وهي عربية مستعملة، والصورة الأشهر محالة في `alternative_spellings`. وهي العلة التي أفرد لها `naskh` دون «الناسخ والمنسوخ».

**مرتبط به:** <span dir="ltr">[`tafsir`](#tafsir)، [`ayah`](#ayah)، [`tafsir_al_ray`](#tafsir_al_ray)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/358`

## علوم القرآن — `quranic_sciences`

<a id="asma_al_surah"></a>

### أسماء السورة — Asma al-Surah

<!-- source: standards/terminology/concepts/asma_al_surah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`asma_al_surah`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | أَسْمَاء السُّورَة |
| تهجئات أخرى | <span dir="ltr">`asmaa_al_surah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Surah Names`</span> |

**التعريف:** ما سميت به السورة من أسماء، وأكثر السور لها أكثر من اسم، منها ما ثبت بالأثر ومنها ما جرى به الاصطلاح.

**الغرض:** يستخدم لحفظ كل ما تعرف به السورة من أسماء، لأن المصاحف تختلف في الاسم المثبت، والبحث يحتاج أن يجد السورة بأي أسمائها.

- اسم السورة شيء، وسبب تسميتها به شيء آخر.
- أسماء السورة غير أسماء القرآن نفسه.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`sabab_al_tasmiyah`](#sabab_al_tasmiyah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="fadail_al_quran"></a>

### فضائل القرآن — Fadail al-Quran

<!-- source: standards/terminology/concepts/fadail_al_quran.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`fadail_al_quran`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | فَضَائِل القُرْآن |
| تهجئات أخرى | <span dir="ltr">`fadail`، `fadail_al_surah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Merits`</span> |

**التعريف:** ما ورد في فضل القرآن أو فضل سورة منه أو آية، وما يترتب على قراءتها من أجر أو أثر.

**الغرض:** يستخدم محتوى يربط بالقرآن كله أو بسورة أو آية، ويفرد عن التفسير لأنه لا يفسر المعنى، وعن الحديث لأنه مرتب على الموضع لا على الراوي.

- الفضل مرتب على الموضع من القرآن، والحديث الذي ورد فيه أصل ينقل عنه لا يمثل مكانه.
- كثير مما يروى في فضائل السور ضعيف أو موضوع، فيقيد بمصدره ودرجته.

**مرتبط به:** <span dir="ltr">[`quran`](#quran)، [`surah`](#surah)، [`ayah`](#ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `4/136`

<a id="gharib_al_quran"></a>

### غريب القرآن — Gharib al-Quran

<!-- source: standards/terminology/concepts/gharib_al_quran.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`gharib_al_quran`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | غَرِيب القُرْآن |
| تهجئات أخرى | <span dir="ltr">`gharib`، `word_meaning`</span> |
| مقابل إنجليزي | <span dir="ltr">`Word Meanings`</span> |

**التعريف:** بيان معاني الألفاظ القرآنية التي خفي معناها على أكثر القراء، لقلة دورانها في الاستعمال أو لتغير دلالتها.

**الغرض:** يستخدم محتوى يربط بكلمة بعينها من الآية لا بالآية كلها، فيتميز عن التفسير الذي يفسر المعنى الكلي.

- غريب القرآن بيان لفظة، والتفسير بيان معنى الآية.
- المعنى منسوب إلى كتاب بعينه، فقد يختلف بين المصادر.

**مرتبط به:** <span dir="ltr">[`word`](#word)، [`tafsir`](#tafsir)، [`ayah`](#ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `2/3`
- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/8`

<a id="maqasid_al_surah"></a>

### مقاصد السورة — Maqasid al-Surah

<!-- source: standards/terminology/concepts/maqasid_al_surah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`maqasid_al_surah`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | مَقَاصِد السُّورَة |
| تهجئات أخرى | <span dir="ltr">`maqasid`</span> |
| مقابل إنجليزي | <span dir="ltr">`Surah Objectives`</span> |

**التعريف:** المعاني الكلية التي تدور عليها السورة ويجمع بينها موضوعها، وما تنتظم به آياتها من غرض واحد.

**الغرض:** يستخدم محتوى يربط بالسورة كلها لا بآية منها، فيتميز عن التفسير الذي يمضي على الآيات، وعن الموضوعات التي تعدد ما ورد فيها.

- المقصد غرض جامع للسورة، والموضوع واحد مما ورد فيها.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`tafsir`](#tafsir)</span>

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

**التعريف:** المواضع التي يتشابه فيها لفظ الآيات أو أجزاؤها في القرآن، تشابهًا تامًّا أو مع اختلاف يسير في كلمة أو ترتيب.

**الغرض:** تستخدم أساسًا لأدوات الحفظ والمراجعة والبحث، إذ يحتاج الحافظ إلى معرفة المواضع التي يلتبس بعضها ببعض وموضع الفرق بينها.

- التشابه اللفظي المقصود هنا غير المتشابه المقابل للمحكم في علوم القرآن.
- التشابه علاقة بين موضعين أو أكثر، لا صفة في آية واحدة.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`word`](#word)، [`hifz`](#hifz)، [`equivalent_ayah`](#equivalent_ayah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/390`

<a id="naskh"></a>

### النسخ — Naskh

<!-- source: standards/terminology/concepts/naskh.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`naskh`</span> |
| `kind` | <span dir="ltr">`concept`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | النَّسْخ |
| تهجئات أخرى | <span dir="ltr">`nasikh_mansukh`، `nasikh_wa_mansukh`، `nasekh_mansokh`</span> |
| مقابل إنجليزي | <span dir="ltr">`Abrogation`</span> |

**التعريف:** رفع حكم شرعي بدليل شرعي متأخر عنه، ويبحث في القرآن بنسبة الآية الناسخة إلى الآية المنسوخة.

**الغرض:** يستخدم لتمثيل العلاقة بين آيتين إحداهما ناسخة والأخرى منسوخة، وهي علاقة بين موضعين من النص لا صفة في آية واحدة.

- النسخ حكم على الحكم لا على النص، فالآية المنسوخ حكمها ثابتة في المصحف.
- النسبة مختلف فيها في كثير من المواضع، فتقيد بمصدرها ولا تعرض حكمًا مجمعًا عليه.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`asbab_al_nuzul`](#asbab_al_nuzul)</span>

**المصادر:**

- [مباحث في علوم القرآن](https://files.turath.io/books-v3/11368.json) — `1/237`
- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `3/66`

<a id="sabab_al_tasmiyah"></a>

### سبب التسمية — Sabab al-Tasmiyah

<!-- source: standards/terminology/concepts/sabab_al_tasmiyah.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`sabab_al_tasmiyah`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`extended`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | سَبَب التَّسْمِيَة |
| تهجئات أخرى | <span dir="ltr">`sabab_al_tasmiya`</span> |

**التعريف:** بيان العلة التي سميت بها السورة اسمها، وما ورد في ذلك من أثر أو وجه لغوي.

**الغرض:** يستخدم محتوى يربط بالسورة، ويفرد عن سبب النزول لأنه يخص الاسم لا النزول، وكثير من السور لها أكثر من اسم فلها أكثر من سبب.

- سبب التسمية يخص اسم السورة، وسبب النزول يخص نزول الآية.

**مرتبط به:** <span dir="ltr">[`surah`](#surah)، [`asbab_al_nuzul`](#asbab_al_nuzul)، [`asma_al_surah`](#asma_al_surah)</span>

**المصادر:**

- [الإتقان في علوم القرآن](https://files.turath.io/books-v3/11728.json) — `1/178`

<a id="tadabbur"></a>

### التدبر — Tadabbur

<!-- source: standards/terminology/concepts/tadabbur.yml -->

| الحقل | القيمة |
| --- | --- |
| `code` | <span dir="ltr">`tadabbur`</span> |
| `plural` | <span dir="ltr">`tadabburs`</span> |
| `kind` | <span dir="ltr">`content`</span> |
| الأصل | <span dir="ltr">`quranic`</span> |
| المستوى | <span dir="ltr">`core`</span> |
| الحالة | <span dir="ltr">`draft`</span> |
| بالحركات | التَّدَبُّر |
| تهجئات أخرى | <span dir="ltr">`tadabur`، `waqfat_tadabburiyyah`</span> |
| مقابل إنجليزي | <span dir="ltr">`Reflection`</span> |

**التعريف:** التأمل في معاني القرآن وما يقتضيه من عمل، وما يقيده القارئ من وقفة عند آية أو لفظة.

**الغرض:** يستخدم محتوى يربط بآية أو بموضع منها، ويفرد عن التفسير لأنه لا يلتزم بيان المعنى الظاهر، وقائله ليس بالضرورة مفسرًا.

- التفسير بيان لمعنى الآية على منهج، والتدبر أثر المعنى في المتدبر.

**مرتبط به:** <span dir="ltr">[`ayah`](#ayah)، [`tafsir`](#tafsir)</span>

**المصادر:**

- [معجم مصطلحات التجويد](https://tajweed.quranpedia.net/term/show/29) — `29`
