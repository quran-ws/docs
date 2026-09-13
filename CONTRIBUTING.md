<div dir="rtl">

# المساهمة

النسخة القصيرة، ولكل مستودعات Quran.ws، في صفحة [كيف تساهم](https://quran.ws/docs/contribute/). وهذا الملف لمن يعدّل هذا المستودع.

افتح `Issue` قبل إرسال `PR`، لأن الأدلة تتغير بالنقاش.

## كيف يُقترح تغيير

1. **افتح `Issue`** لتعديل قاعدة أو مصطلح، يشرح **الحالة الواقعية** التي دفعت إليه: أي مشروع، وأي موضع، وما الذي التبس أو تعذر. القاعدة التي لا حالة وراءها لا تُعتمد.
2. **انتظر الاتفاق.** القاعدة تؤثر في مشاريع كثيرة، وتغييرها بعد اعتمادها أصعب من مناقشتها قبله.
3. **أرسل `PR`** بعد الاتفاق، وأجب فيه عن قائمة المراجعة.

وفي المستودع 3 قوالب: [`term.yml`](.github/ISSUE_TEMPLATE/term.yml) لاقتراح مصطلح، و[`proposal.yml`](.github/ISSUE_TEMPLATE/proposal.yml) لاقتراح قاعدة، و[`edit.yml`](.github/ISSUE_TEMPLATE/edit.yml) لتصحيح فقرة بعينها.

وقبل اقتراح مصطلح ابحث أولًا، فأكثر المصطلحات «الجديدة» تهجئة لمدخل موجود:

</div>
<div dir="ltr">

```bash
python3 skills/quranic-terminology/scripts/lookup.py --search waqf
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"   # يصوغ المسودة
```

</div>
<div dir="rtl">

وإن كان المفهوم جديدًا حقًا، فـ`propose.py` يصوغ مسودة الاقتراح بحقول المدخل، والاسم البرمجي يُشتق من العربية المشكولة. ولفحص مشروع في `CI` شغّل `audit_terminology.py <dir> --strict`، وملف `.terminology.json` في المشروع يُسكت ما يعرف المشروع أنه ليس خطأ (نموذجه في `skills/quranic-terminology/assets/terminology.example.json`).

## المتطلبات

البناء يحتاج إلى Python 3 والحزم في `requirements.txt`:

</div>
<div dir="ltr">

```bash
pip install -r requirements.txt
```

</div>
<div dir="rtl">

## الملفات المولّدة وكيف تُعدَّل

هذه الملفات مولّدة، وأي تعديل فيها يضيع عند إعادة التوليد:

| لا تعدّل | عدّل | ثم شغّل |
| --- | --- | --- |
| `standards/terminology/aliases.json` | `alternative_spellings` في المدخل | `python3 tools/build_aliases.py` |
| `standards/terminology/registry_aliases.json` | الصف في `standards/terminology/registries/*.tsv` | `python3 tools/build_registry_aliases.py` |
| `standards/terminology/registries/ayah_counts.tsv` | لا شيء، يُقرأ من كتاب البيان للداني | `python3 tools/extract_ayah_counts.py` |
| مداخل علامات الضبط | `standards/terminology/data/dabt_marks.tsv` | `python3 tools/generate_dabt.py` |
| كتلة `unicode` في أي مدخل | لا شيء، تُقرأ من قاعدة يونيكود | `python3 tools/generate_dabt.py` |
| تهجئة `code` | `names.arabic.vocalized` | `python3 tools/translit.py`، والبناء يشتقها |
| `content/ar/reference/dictionary.md` و`content/en/…/dictionary.md` | المدخل نفسه، بحقوله العربية والإنجليزية | `python3 tools/generate_dictionary.py` |
| `content/ar/reference/standard.md` | `content/standards/terminology.ar.yml` | `python3 tools/generate_standard.py` |
| `content/{ar,en}/naming.md` وسائر صفحات الأدلة | ملف القواعد `content/pages/<page>.yml` | `python3 tools/generate_pages.py` |
| `content/glossary.json` (قائمة المصطلحات التي يعرضها الموقع) | مدخل المفهوم في `standards/terminology/concepts/` | `python3 tools/generate_glossary.py` |
| `skills/quranic-terminology/` كله، ومنه `data/terminology.json` | المصدر الذي بُني منه | `python3 tools/generate_skill.py` |

## قبل الإرسال

</div>
<div dir="ltr">

```bash
python3 tools/build.py
```

</div>
<div dir="rtl">

يشغّل `build.py` كل خطوات البناء بترتيبها، 14 خطوة اليوم: اختبار قواعد التهجئة، وتوليد مداخل العلامات وسجل أحكام التجويد، وبناء الفهرسين، ومطابقة أعداد الآي، والتحقق من كل مدخل على المخطط وعلى المعيار، وفحص السجلات، وتوليد القاموس وصفحات السجلات بلغتيه، وفحص الأسماء في الصفحات وملفات النماذج، وتوليد المهارة. القائمة الكاملة في [`tools/README.md`](tools/README.md)، و`make build` يشغّل الأمر نفسه. وأدرج الملفات المولّدة في الـ`PR` نفسه.

## حال الصفحة

كل صفحة تحمل `status` في الـ`frontmatter`:

- `draft` — قيد الكتابة ولا يُبنى عليها.
- `proposed` — نوقشت وتنتظر الاعتماد.
- `adopted` — ملزمة لمشاريعنا. ولا يُوسم بها مدخل بلا مصدر يثبت تعريفه.

## العربية والإنجليزية

صفحة الدليل تُكتب مرة واحدة في `content/pages/<page>.yml`: كل قاعدة بالإنجليزية وإلى جانبها حقلها العربي (`rule_ar` و`note_ar` و`checked_by_ar`، وكذلك العنوان والمقدمة وعناوين الأقسام). وتُعدَّل اللغتان في الملف نفسه، ولا تُعدَّل الصفحة المولّدة.

وبعد كتابة العربية أو مراجعتها شغّل `python3 tools/generate_pages.py --stamp <page>`، فيسجل هاش الإنجليزية التي تُرجمت عنها. وإن تغيرت الإنجليزية بعد ذلك فشل `tests/test_pages.py` وسمّى القاعدة التي تأخرت عربيتها. و`--check` يعرض ما لم يُترجم وما تقادم.

المعيار العربي مصدره `content/standards/terminology.ar.yml`. لكل قاعدة `id` نصي من 3 أرقام، و`category` و`name` و`description` وقائمة `examples`. تبقى الأرقام ثابتة عند إعادة الترتيب. يجمع الوصف الحكم وسياق تطبيقه، وتُكتب الأمثلة ككتل Markdown مستقلة: جدول للمقارنة، أو كتلة شفرة للصيغة الحرفية، أو فقرة للتوضيح. تُستخدم صيغة YAML متعددة الأسطر `|` لكل كتلة. يفحص `python3 tools/generate_standard.py --check` المصدر ومطابقة الصفحة المولدة دون تعديل الملفات.

النسخة الإنجليزية من المعيار ما زالت تمثل النسخة السابقة؛ تُراجع ترجمتها بعد اعتماد المسودة العربية. الصفحات النثرية الأخرى (المدخل، والرخصة، وسجل القرارات) ملف في كل لغة.

</div>

---

# Contributing

The short version, for every Quran.ws repository, is [How to contribute](https://quran.ws/docs/contribute/). This file is for changing this repository.

Open an issue before sending a PR, because the guidelines change through discussion.

## How a change is proposed

1. **Open an issue** for a change to a rule or a term, describing the **real case** that prompted the change: which project, which place, what was ambiguous or impossible. A rule with no case behind it is not adopted.
2. **Wait for agreement.** Rules have long reach; changing one after adoption costs more than discussing it before.
3. **Send a PR** once there is agreement, answering the checklist.

There are 3 forms: [`term.yml`](.github/ISSUE_TEMPLATE/term.yml) to propose a term, [`proposal.yml`](.github/ISSUE_TEMPLATE/proposal.yml) to propose a guideline, and [`edit.yml`](.github/ISSUE_TEMPLATE/edit.yml) to correct one paragraph.

Before proposing a term, search first. Most "new" terms are spellings of an entry that exists:

```bash
python3 skills/quranic-terminology/scripts/lookup.py --search waqf
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"   # drafts the proposal
```

If the concept is genuinely new, `propose.py` drafts the proposal with the entry's fields, deriving the code name from the vocalised Arabic. To audit a project in CI run `audit_terminology.py <dir> --strict`; a `.terminology.json` in the project silences known false positives (example in `skills/quranic-terminology/assets/terminology.example.json`).

## Prerequisites

The build needs Python 3 and the packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## What is never edited by hand

These files are generated, and an edit to them is lost on the next build:

| Don't edit | Edit instead | Then run |
| --- | --- | --- |
| `standards/terminology/aliases.json` | `alternative_spellings` in the entry | `python3 tools/build_aliases.py` |
| `standards/terminology/registry_aliases.json` | the row in `standards/terminology/registries/*.tsv` | `python3 tools/build_registry_aliases.py` |
| `standards/terminology/registries/ayah_counts.tsv` | nothing; it is read from al-Dani's al-Bayan | `python3 tools/extract_ayah_counts.py` |
| The mark entries | `standards/terminology/data/dabt_marks.tsv` | `python3 tools/generate_dabt.py` |
| The `unicode` block of any entry | nothing; it is read from the Unicode database | `python3 tools/generate_dabt.py` |
| The `code` spelling | `names.arabic.vocalized` | `python3 tools/translit.py`; the build derives it |
| `content/ar/reference/dictionary.md` and `content/en/…/dictionary.md` | the entry itself, Arabic and English fields | `python3 tools/generate_dictionary.py` |
| `content/ar/reference/standard.md` | `content/standards/terminology.ar.yml` | `python3 tools/generate_standard.py` |
| `content/{ar,en}/naming.md` and the other guideline pages | the rule file `content/pages/<page>.yml` | `python3 tools/generate_pages.py` |
| `content/glossary.json` (the glossary the site renders) | the concept entry in `standards/terminology/concepts/` | `python3 tools/generate_glossary.py` |
| All of `skills/quranic-terminology/`, including `data/terminology.json` | the source it was built from | `python3 tools/generate_skill.py` |

## Before sending

```bash
python3 tools/build.py
```

`build.py` runs every build step in order, 14 today: the spelling tests, the generated mark entries and the tajwid rules registry, the two indexes, the ayah-count reconciliation, every entry against the schema and against the standard, the registries, the dictionary and registry pages in both languages, the names in the prose and the example files, and the skill. The full list is in [`tools/README.md`](tools/README.md); `make build` runs the same command. Include the generated files in the same PR.

## Page status

Every page carries `status` in its frontmatter:

- `draft` — being written; don't build on it.
- `proposed` — discussed, awaiting adoption.
- `adopted` — binding on our projects. An entry with no source for its definition is never marked `adopted`.

## Arabic and English

A guideline page is written once, in `content/pages/<page>.yml`: every rule in English with its Arabic field beside it (`rule_ar`, `note_ar`, `checked_by_ar`, and likewise the title, the intro and the section titles). Both languages are edited in that file, never in the rendered page.

After writing or revising Arabic, run `python3 tools/generate_pages.py --stamp <page>`; it records the hash of the English each field was translated from. If the English changes afterwards, `tests/test_pages.py` fails and names the rule whose Arabic is behind. `--check` lists what is untranslated or stale.

The Arabic standard is authored in `content/standards/terminology.ar.yml`. Each rule has a quoted three-digit `id`, `category`, `name`, `description`, and an `examples` list. IDs stay stable after reordering. Descriptions include the requirement and its scope; each example is a standalone Markdown block: a table for comparisons, a fenced code block for literal syntax, or a paragraph for explanation. Use a YAML literal block (`|`) for each example. Run `python3 tools/generate_standard.py --check` to validate the source and detect stale output without writing.

The English standard still represents the previous edition; its rewrite follows review of the Arabic draft. Other prose pages (start here, licensing, the decision record) remain one file per language.
