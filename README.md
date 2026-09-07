<div dir="rtl">

# أدلة Quran.ws

كيف نبني برمجيات تتعامل مع القرآن: التسمية، والتعامل مع النص، والإصدارات والتصحيحات.

هذه الأدلة موجهة إلى المطورين الذين يبنون تطبيقات قرآنية، ومنهم من لا يقرأ العربية جيدًا. وهي مكتوبة بالعربية والإنجليزية، والنسختان متقابلتان صفحة بصفحة.

- اقرأ الأدلة على الموقع: <https://quran-ws.github.io/guidelines/ar/>
- English: <https://quran-ws.github.io/guidelines/en/>

كتبناها لأنفسنا أولًا حتى تبقى قراراتنا متسقة عبر مشاريع [Quran.ws](https://quran.ws)، ولا نعيد النقاش نفسه في كل مستودع جديد. ونشرناها لأن أكثر ما فيها لا يخصنا وحدنا، فكل فريق يبني تطبيقًا قرآنيًا يسأل الأسئلة نفسها: هل نكتب `ayah` أم `verse`؟ ومتى يجوز تعديل نص مصحف منشور؟ وكيف نُعلم المستخدمين بتصحيح في النص؟

> هذه الأدلة **آراء واجتهادات**، وليست فتاوى ولا معايير رسمية. ما يتعلق منها بالنص القرآني نفسه مبني على مراجعة أهل الاختصاص، وما يتعلق بالهندسة اختيار من بين بدائل صحيحة.

## ما في المستودع

| المحور | الحال | المضمون |
| --- | --- | --- |
| [المدخل](content/ar/01-intro/index.md) | `draft` | أسلوب الكتابة، وما يجب أن تحتويه صفحة في هذه الأدلة. |
| [أدبيات التعامل مع النص القرآني](content/ar/02-quranic-text/index.md) | `draft` | النص أصل منقول ولا يُحرر: التخزين والترميز والتقسيم والعرض، والاختبارات التي تحرسها. |
| [معيار المصطلحات](content/ar/03-terminology/standard.md) و[القاموس](content/ar/03-terminology/dictionary.md) | `draft` | اسم واحد لكل مفهوم، وتهجئة تُشتق بدالة ولا تُختار. المصدر المقروء آليًا في [`standards/terminology/`](standards/terminology/)، وأسباب القرارات في [سجل القرارات](content/ar/03-terminology/decisions.md)، و[مهارة وكيل](skills/quranic-terminology/) تفحص بها كودًا قائمًا. |
| [الإصدارات والتصحيحات](content/ar/04-versioning/index.md) | `draft` | إصدار البيانات وليس الكود وحده، وسجل التصحيحات، وكيف نُعلم المستخدمين بتغيّر النص. |
| [المصدر المفتوح و`version control`](content/ar/05-open-source/index.md) | `draft` | الرخص، وبنية المستودعات، وقواعد الـ`commits` والـ`PRs` والمراجعة. |
| [الهندسة](content/ar/06-engineering/index.md) | `draft` | تصميم الـ`APIs`، ونمذجة البيانات، وعرض المصحف والخطوط، والصوت. |

لا شيء معتمد بعد، ولا يُبنى على صفحة قبل أن تُوسم `adopted`.

## البدء

</div>
<div dir="ltr">

```bash
# Read the dictionary (Arabic; the English one is under content/en/)
open content/ar/03-terminology/dictionary.md

# Build and check everything, in order
pip install -r requirements.txt
python3 tools/build.py

# Look a name up: any spelling resolves to its entry
python3 skills/quranic-terminology/scripts/lookup.py aya verse "Waqf Lazim"

# Install the agent skill: as a plugin, inside Claude Code
#   /plugin marketplace add quran-ws/guidelines
#   /plugin install quranic-terminology@quran-ws
# or by hand
cp -r skills/quranic-terminology ~/.claude/skills/

# Audit a codebase in CI; a .terminology.json in the project silences known false positives
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
#   example config: skills/quranic-terminology/assets/terminology.example.json

# Draft a term proposal from the vocalized Arabic
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"

# Build the site
cd site && npm install && npm run build
```

</div>
<div dir="rtl">

يحتاج البناء إلى Python 3 والحزم المذكورة في `requirements.txt`، ويحتاج الموقع إلى Node.

## خريطة المستودع

- `content/{ar,en}/` — صفحات الأدلة، ملفًا بملف في اللغتين.
- `standards/terminology/` — المصدر المقروء آليًا: `schema.json`، و`concepts/` (ملف لكل مفهوم)، و`registries/` (المجموعات المغلقة: السور، والقراءات، وأنظمة عدّ الآي، ومواضع السجدة)، و`aliases.json`.
- `tools/` — ما يشتق الأسماء ويفحصها ويولّد الصفحات. [`tools/README.md`](tools/README.md) يشرح كل أداة.
- `skills/quranic-terminology/` — مهارة الوكيل، مولّدة كاملة في كل بناء.
- `surveys/` — فحص مستودعات حقيقية على المعيار. وما فيها نتائج وليس قواعد.
- `examples/` — نماذج مفحوصة بالأسماء المعتمدة: مخطط قاعدة بيانات، و`API`، وبيانات، وترحيل، واختبارات.
- `site/` — موقع Astro Starlight الذي يعرض `content/`.
- [`STRUCTURE.md`](STRUCTURE.md) — الشجرة كاملة وقواعد التنظيم.

## المساهمة

افتح `Issue` قبل إرسال `PR`، لأن الأدلة تتغير بالنقاش. القوالب ثلاثة:

- [اقتراح مصطلح](.github/ISSUE_TEMPLATE/term.yml) — مفهوم جديد في القاموس، أو تعديل اسمه أو تعريفه.
- [اقتراح قاعدة](.github/ISSUE_TEMPLATE/proposal.yml) — قاعدة جديدة في الأدلة، أو تعديل قاعدة قائمة.
- [تصحيح فقرة](.github/ISSUE_TEMPLATE/edit.yml) — تعديل على فقرة بعينها. يُفتح من كل فقرة في الموقع.

وقبل اقتراح مصطلح ابحث أولًا: `python3 skills/quranic-terminology/scripts/lookup.py --search <كلمة>`، فأكثر المصطلحات «الجديدة» تهجئة لمدخل موجود. فإن لم تجده، فـ`scripts/propose.py NAME "الاسم مشكولًا"` يصوغ لك مسودة الاقتراح بحقولها. التفصيل في [CONTRIBUTING.md](CONTRIBUTING.md).

## الرخصة

النصوص برخصة [CC BY 4.0](LICENSE)، والكود والمخططات والبيانات المقروءة آليًا برخصة MIT. والنص القرآني نفسه لا تشمله رخصة ولا دعوى ملكية.

</div>

---

# Quran.ws Guidelines

How we build software that handles the Quran: naming, text handling, versioning and corrections.

These guidelines are for developers building Quran applications, including those who do not read Arabic well. They are written in Arabic and English, and the two versions mirror each other page for page.

- Read the guidelines: <https://quran-ws.github.io/guidelines/en/>
- العربية: <https://quran-ws.github.io/guidelines/ar/>

We wrote them for ourselves first, so our decisions stay consistent across [Quran.ws](https://quran.ws) projects and we stop having the same argument in every new repository. We published them because most of what is here is not specific to us: any team building a Quran application asks the same questions. Is it `ayah` or `verse`? When may a published mushaf's text be edited? How do you tell users that text they depend on has been corrected?

> These are **opinions**, not rulings and not official standards. What concerns the Quranic text itself is reviewed by qualified scholars; what concerns engineering is one defensible choice among several.

## What is here

| Area | Status | Covers |
| --- | --- | --- |
| [Introduction](content/en/01-intro/index.md) | `draft` | Writing style, and what a page in these guidelines must contain. |
| [Handling Quranic text](content/en/02-quranic-text/index.md) | `draft` | The text is transmitted source data, never edited: storage, encoding, tokenisation, display, and the tests that guard them. |
| [Terminology standard](content/en/03-terminology/standard.md) and [dictionary](content/en/03-terminology/dictionary.md) | `draft` | One name per concept, and a spelling derived by a function rather than chosen. The machine-readable source is in [`standards/terminology/`](standards/terminology/), the arguments are in the [decision record](content/en/03-terminology/decisions.md), and an [agent skill](skills/quranic-terminology/) audits a codebase against it. |
| [Versioning and corrections](content/en/04-versioning/index.md) | `draft` | Versioning data, not only code; errata logs; how users are told the text changed. |
| [Open source and version control](content/en/05-open-source/index.md) | `draft` | Licensing, repository layout, and the rules for commits, PRs and review. |
| [Engineering](content/en/06-engineering/index.md) | `draft` | API design, data modelling, mushaf rendering and fonts, and audio. |

Nothing is adopted yet. Build against a page only once it is marked `adopted`.

## Quickstart

```bash
# Read the dictionary (English; the Arabic one is under content/ar/)
open content/en/03-terminology/dictionary.md

# Build and check everything, in order
pip install -r requirements.txt
python3 tools/build.py

# Look a name up: any spelling resolves to its entry
python3 skills/quranic-terminology/scripts/lookup.py aya verse "Waqf Lazim"

# Install the agent skill: as a plugin, inside Claude Code
#   /plugin marketplace add quran-ws/guidelines
#   /plugin install quranic-terminology@quran-ws
# or by hand
cp -r skills/quranic-terminology ~/.claude/skills/

# Audit a codebase in CI; a .terminology.json in the project silences known false positives
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
#   example config: skills/quranic-terminology/assets/terminology.example.json

# Draft a term proposal from the vocalised Arabic
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"

# Build the site
cd site && npm install && npm run build
```

The build needs Python 3 and the packages in `requirements.txt`; the site needs Node.

## Map of the repository

- `content/{ar,en}/` — the guideline pages, file for file in both languages.
- `standards/terminology/` — the machine-readable source: `schema.json`, `concepts/` (one file per concept), `registries/` (the closed sets: surahs, qiraat, ayah numbering systems, sajdahs), and `aliases.json`.
- `tools/` — what derives the names, checks them and generates the pages. [`tools/README.md`](tools/README.md) describes each tool.
- `skills/quranic-terminology/` — the agent skill, generated in full on every build.
- `surveys/` — real codebases measured against the standard. Findings, not rules.
- `examples/` — checked samples in canonical names: a database schema, an API, data, a migration and tests.
- `site/` — the Astro Starlight site that renders `content/`.
- [`STRUCTURE.md`](STRUCTURE.md) — the full tree and the layout conventions.

## Contributing

Open an issue before sending a PR, because the guidelines change through discussion. There are 3 issue forms:

- [Propose a term](.github/ISSUE_TEMPLATE/term.yml) — a new concept for the dictionary, or a change to a name or a definition.
- [Propose a guideline](.github/ISSUE_TEMPLATE/proposal.yml) — a new rule, or a change to one.
- [Suggest an edit](.github/ISSUE_TEMPLATE/edit.yml) — a change to one paragraph. Every paragraph on the site links to it.

Before proposing a term, search first: `python3 skills/quranic-terminology/scripts/lookup.py --search <word>`. Most "new" terms are spellings of an entry that exists. If it is genuinely new, `scripts/propose.py NAME "vocalized arabic"` drafts the proposal with its fields filled in. Details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Prose is [CC BY 4.0](LICENSE); code, schemas and machine-readable data are MIT. The Quranic text itself is covered by neither and carries no claim of ownership.
