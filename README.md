<div dir="rtl">

# أدلة Quran.ws

كيف نبني برمجيات تتعامل مع القرآن، من التسمية والتعامل مع النص إلى الإصدارات والتصحيحات والهندسة والمستودعات.

هذه الأدلة للمطورين الذين يبنون تطبيقات قرآنية، ومنهم من لا يقرأ العربية جيدًا. نكتبها بالعربية والإنجليزية من مصدر واحد حتى تبقى النسختان متوافقتين.

كتبناها لأنفسنا أولًا لتتسق قراراتنا في مشاريع [Quran.ws](https://quran.ws)، ولا نكرر النقاش نفسه في كل مستودع جديد. ونشرناها لأن معظمها يفيد غيرنا أيضًا، فكل فريق يبني تطبيقًا قرآنيًا يواجه الأسئلة نفسها: هل نكتب `ayah` أم `verse`؟ ومتى يجوز تعديل نص مصحف منشور؟ وكيف نبلغ المستخدمين بتصحيح النص الذي يعتمدون عليه؟

## الأدلة

5 صفحات قصيرة، نصوغ فيها كل قاعدة في جملة واحدة ونرفق بها مثالًا وفحصًا يكشف مخالفتها.

| الصفحة | المضمون |
| --- | --- |
| [1. التسمية](content/en/naming.md) | نستخدم لكل مفهوم اسمًا واحدًا في النموذج والجدول والمفتاح الأجنبي وواجهة `API`. |
| [2. النص القرآني](content/en/quranic-text.md) | نحفظ النص كما نُقل من مصدره دون تعديل، مع قواعد الترميز والتقسيم والعرض والاختبارات التي تتحقق من سلامتها. |
| [3. الإصدارات والتصحيحات](content/en/versioning.md) | ننشر كل `dataset` في إصدارات دون تعديله مباشرة، مع قواعد الترقيم الدلالي للبيانات وسجل التصحيحات وطريقة إبلاغ القارئ. |
| [4. الهندسة](content/en/engineering.md) | نبني نموذج البيانات على المصحف نفسه بدل الشاشة، مع قواعد الجداول والمعرفات وواجهات `APIs` والتخزين والخطوط والصوت والبحث. |
| [5. المستودعات والترخيص](content/en/repositories.md) | بنية المستودع وتغييرات `commits` والمراجعة والإصدارات و[الوقف والترخيص المفتوح](content/en/licensing.md). |

وتحيل الأدلة إلى مراجع ترجع إليها عند الحاجة دون قراءتها كاملة: [القاموس](content/en/reference/dictionary.md)، و[السجلات](content/en/reference/registries.md)، و[معيار المصطلحات](content/en/reference/standard.md)، و[سجل القرارات](content/en/reference/decisions.md).

نكتب قواعد الصفحات في [`content/pages/`](content/pages/)، ومنها نولّد النسختين العربية والإنجليزية. ويوجد مصدر المصطلحات المقروء آليًا في [`standards/terminology/`](standards/terminology/)، وبنية المستودع كاملة في [STRUCTURE.md](STRUCTURE.md).

## استخدم الأدلة

- اقرأ الأدلة على الموقع: [quran.ws/docs/guidelines](https://quran.ws/docs/guidelines/)، بالعربية والإنجليزية.
- تفحص أداة المصطلحات مستودعك وتذكر كل اسم تختلف صيغته عما يحدده المعيار، دون إعادة تسمية أي شيء:

</div>
<div dir="ltr">

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

</div>
<div dir="rtl">

- يمكنك تثبيت أداة الفحص نفسها إضافةً في Claude Code تربط أي تهجئة بمدخلها:

</div>
<div dir="ltr">

```text
/plugin marketplace add quran-ws/docs
/plugin install quranic-terminology@quran-ws
```

</div>
<div dir="rtl">

- يحتوي [`examples/`](examples/) على أمثلة تستخدم الأسماء المعتمدة، وتشمل مخطط قاعدة بيانات وواجهة `API` وبيانات وترحيلًا واختبارات.
- يعرض [`surveys/`](surveys/) نتائج فحص كود مشاريع حقيقية وفق المعيار، وهذه نتائج وليست قواعد.

## اقترح تعديلًا

ابدأ بـ`Issue` عند اقتراح تعديل قاعدة أو مصطلح، لأن تعديل الأدلة يحتاج إلى نقاش. أما تصحيح فقرة واحدة أو خطأ مطبعي فأرسله في `PR` مباشرة. في المستودع 3 قوالب للمسائل:

- [اقتراح مصطلح](.github/ISSUE_TEMPLATE/term.yml) — مفهوم جديد في القاموس، أو تعديل اسمه أو تعريفه.
- [اقتراح قاعدة](.github/ISSUE_TEMPLATE/proposal.yml) — قاعدة جديدة في الأدلة، أو تعديل قاعدة قائمة.
- [تصحيح فقرة](.github/ISSUE_TEMPLATE/edit.yml) — تعديل فقرة محددة.

لا نعتمد قاعدة دون حالة واقعية تستدعيها، فاذكر في `Issue` اسم المشروع والموضع وما كان غامضًا أو تعذر تنفيذه. وابحث في القاموس قبل اقتراح مصطلح، فأكثر المصطلحات «الجديدة» تهجئات لمداخل موجودة. تجد التفاصيل في [CONTRIBUTING.md](CONTRIBUTING.md).

## حالة الأدلة

لا شيء معتمد بعد، فاعتمد على الصفحة بعد أن تحمل الحالة `adopted` فقط. هذه الأدلة **آراء واجتهادات** وليست فتاوى أو معايير رسمية. يراجع أهل العلم المؤهلون ما يتعلق بالنص القرآني نفسه، أما القواعد الهندسية فهي اختيارات من عدة خيارات صحيحة.

## الرخصة

صفحات الشرح برخصة [CC BY 4.0](LICENSE)، والكود والمخططات والبيانات المقروءة آليًا برخصة MIT. أما النص القرآني نفسه فلا تشمله أي من الرخصتين ولا ندّعي ملكيته.

</div>

---

# Quran.ws Guidelines

How we build software that handles the Quran: naming, text handling, versioning and corrections, engineering, and repositories.

These guidelines are for developers building Quran applications, including those who do not read Arabic well. They are written in Arabic and English from one source, so the two versions cannot drift apart.

We wrote them for ourselves first, so our decisions stay consistent across [Quran.ws](https://quran.ws) projects and we stop having the same argument in every new repository. We published them because most of what is here is not specific to us: any team building a Quran application asks the same questions. Is it `ayah` or `verse`? When may a published mushaf's text be edited? How do you tell users that text they depend on has been corrected?

## The guidelines

Five short pages. Every rule is one sentence, an example, and the check that catches a violation.

| Page | Covers |
| --- | --- |
| [1. Naming](content/en/naming.md) | One concept, one name, the same in the model, the table, the foreign key and the API. |
| [2. Quranic text](content/en/quranic-text.md) | The text is transmitted source data, never edited: encoding, tokenisation, display, and the tests that guard them. |
| [3. Versioning and corrections](content/en/versioning.md) | A dataset is released, never edited: semantic versioning for data, the errata log, and how a reader is told. |
| [4. Engineering](content/en/engineering.md) | Model the mushaf, not the screen: tables, identifiers, APIs, storage, fonts, audio and search. |
| [5. Repositories and licensing](content/en/repositories.md) | Layout, commits, review, releases, and [waqf and open licensing](content/en/licensing.md). |

The reference the guidelines link into, looked up rather than read through: the [dictionary](content/en/reference/dictionary.md), the [registries](content/en/reference/registries.md), the [terminology standard](content/en/reference/standard.md) and the [decision record](content/en/reference/decisions.md).

The pages are written as rules in [`content/pages/`](content/pages/), and both languages are rendered from there. The machine-readable source of the terminology is [`standards/terminology/`](standards/terminology/). The full tree is in [STRUCTURE.md](STRUCTURE.md).

## Using the guidelines

- Read them on the site: [quran.ws/docs/guidelines](https://quran.ws/docs/guidelines/), in English and Arabic.
- The terminology audit reads your repository and reports every name the standard would have written differently. It renames nothing:

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

- The same audit installs into Claude Code as a plugin that resolves any spelling to its entry:

```text
/plugin marketplace add quran-ws/docs
/plugin install quranic-terminology@quran-ws
```

- [`examples/`](examples/) holds samples in canonical names: a database schema, an API, data, a migration and tests.
- [`surveys/`](surveys/) holds real codebases measured against the standard. Findings, not rules.

## Proposing a change

A change to a rule or a term starts with an issue, because the guidelines change through discussion. A correction to one paragraph or a typo goes straight to a PR. There are 3 issue forms:

- [Propose a term](.github/ISSUE_TEMPLATE/term.yml) — a new concept for the dictionary, or a change to a name or a definition.
- [Propose a guideline](.github/ISSUE_TEMPLATE/proposal.yml) — a new rule, or a change to one.
- [Suggest an edit](.github/ISSUE_TEMPLATE/edit.yml) — a change to one paragraph.

A rule with no real case behind it is not adopted, so name the project, the place and what was ambiguous or impossible. Before proposing a term, search the dictionary first: most "new" terms are spellings of an entry that exists. All the detail is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Status

Nothing is adopted yet. Build against a page only once it is marked `adopted`. These are **opinions**, not rulings and not official standards. What concerns the Quranic text itself is reviewed by qualified scholars; what concerns engineering is one defensible choice among several.

## Licence

Prose is [CC BY 4.0](LICENSE); code, schemas and machine-readable data are MIT. The Quranic text itself is covered by neither and carries no claim of ownership.
