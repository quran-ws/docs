<div align="right" dir="rtl">

# أدلة Quran.ws

**الأدلة الداخلية والمعايير المفتوحة لبنية Quran.ws التحتية.**

هذا المستودع هو المرجع المعتمد للطريقة التي نكتب بها الكود، ونتعامل بها مع النص القرآني، ونسمي بها المفاهيم، وندير بها الإصدارات والتصحيحات في مشاريع [Quran.ws](https://quran.ws).

كتبناه لأنفسنا أولًا حتى تكون قراراتنا متسقة عبر المشاريع، وحتى لا نعيد الجدال نفسه في كل مستودع جديد. ونشرناه للعموم لأن أكثر ما فيه غير خاص بنا، فأي فريق يبني تطبيقًا قرآنيًا يواجه الأسئلة نفسها: هل نكتب `Ayah` أم `Verse`؟ ومتى يجوز تعديل نص مصحف منشور؟ وكيف نُعلم المستخدمين بتصحيح في النص؟

> هذه الأدلة **آراء واجتهادات**، وليست فتاوى ولا معايير رسمية. ما يتعلق منها بالنص القرآني نفسه مبني على مراجعة أهل الاختصاص، وما يتعلق بالهندسة فهو اختيارٌ من بين بدائل صحيحة.

## المحاور

| المحور | المضمون |
| --- | --- |
| **أدبيات التعامل مع النص القرآني** | الأدب الواجب في عرض النص وتخزينه ونقله، وحدود التطبيع (normalization)، والتعامل مع النص الناقص أو المقطوع، والاختبارات الآلية على النص. |
| **دليل المصطلحات** | [المعيار](content/ar/03-terminology/standard.md) و[القاموس](content/ar/03-terminology/dictionary.md): اسم واحد لكل مفهوم، وتهجئة تشتق بدالة لا تختار، ومصدر يقرأ آليًا في [`standards/`](standards/terminology/). |
| **إدارة الإصدارات والإعلام عن التصحيحات** | الإصدار الدلالي للبيانات لا للكود فقط، وسجل التصحيحات (errata)، وكيف ومتى نُعلم المستخدمين بتغيّر النص. |
| **المصدر المفتوح وVersion control** | الرخص، وبنية المستودعات، وقواعد الـcommits والـPRs والمراجعة، وسياسة الاعتماد على مشاريعنا. |
| **الهندسة** | تصميم الـAPIs، ونمذجة البيانات، وعرض المصحف والخطوط، والصوت والتلاوات. |

## الحالة

المستودع في مرحلة التأسيس. **معيار المصطلحات** مسودة قيد الكتابة وهو أكثر المحاور نضجًا حتى الآن، وبقية المحاور هيكل لم يُكتب بعد. لا شيء هنا معتمد، ولا يُبنى عليه في مشروع قبل أن يُوسم `adopted`.

## المساهمة

الأدلة تتغير بالنقاش وليس بالـcommit المباشر. افتح Issue يشرح الحالة التي دفعتك لاقتراح التغيير، ثم أرسل PR بعد الاتفاق. راجع [CONTRIBUTING.md](CONTRIBUTING.md) و[STRUCTURE.md](STRUCTURE.md).

</div>

---

# Quran.ws Guidelines

**Internal guidelines and open standards for the Quran.ws infrastructure.**

This repository is the reference for how we write code, handle Quranic text, name concepts, and manage releases and corrections across [Quran.ws](https://quran.ws) projects.

We wrote it for ourselves first, so our decisions stay consistent across projects and we stop relitigating the same argument in every new repository. We published it because most of it isn't specific to us. Any team building a Quran application hits the same questions: is it `Ayah` or `Verse`? When may a published Mushaf's text be edited? How do you notify users that text they depend on has been corrected?

> These are **opinions**, not rulings and not official standards. What concerns the Quranic text itself is reviewed by qualified scholars; what concerns engineering is one defensible choice among several.

## Areas

| Area | Covers |
| --- | --- |
| **Handling Quranic text** | Adab of displaying, storing, and transmitting the text; the limits of normalization; partial and truncated text; automated tests over sacred text. |
| **Terminology** | The [standard](content/ar/03-terminology/standard.md) and [dictionary](content/ar/03-terminology/dictionary.md): one name per concept, spellings derived by a function rather than chosen, and a machine-readable source in [`standards/`](standards/terminology/). |
| **Versioning & corrections** | Versioning data, not just code; errata logs; how and when users are told the text changed. |
| **Open source & version control** | Licensing, repository layout, commit/PR/review conventions, and what downstream users can rely on. |
| **Engineering** | API design, data modeling, Mushaf rendering and fonts, audio and recitation. |

## Status

Early. The **terminology standard** is a working draft and the most developed piece so far; the other areas are scaffolding. Nothing here is adopted yet — don't build against a page until it's marked `adopted`.

## Contributing

Guidelines change through discussion, not direct commits. Open an issue describing the case that prompted the change, then send a PR once there's agreement. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Prose is [CC BY 4.0](LICENSE); code samples and the machine-readable standard are MIT.
