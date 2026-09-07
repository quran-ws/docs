<div dir="rtl">

# المساهمة

افتح `Issue` قبل إرسال `PR`، لأن الأدلة تتغير بالنقاش.

## كيف يُقترح تغيير

1. **افتح `Issue`** يشرح **الحالة الواقعية** التي دفعت إليه: أي مشروع، وأي موضع، وما الذي التبس أو تعذر. القاعدة التي لا حالة وراءها لا تُعتمد.
2. **انتظر الاتفاق.** القاعدة تؤثر في مشاريع كثيرة، وتغييرها بعد اعتمادها أصعب من مناقشتها قبله.
3. **أرسل `PR`** بعد الاتفاق، وأجب فيه عن قائمة المراجعة.

القوالب ثلاثة: [`term.yml`](.github/ISSUE_TEMPLATE/term.yml) لاقتراح مصطلح، و[`proposal.yml`](.github/ISSUE_TEMPLATE/proposal.yml) لاقتراح قاعدة، و[`edit.yml`](.github/ISSUE_TEMPLATE/edit.yml) لتصحيح فقرة بعينها، ويُفتح من كل فقرة في الموقع.

وقبل اقتراح مصطلح ابحث أولًا، فأكثر المصطلحات «الجديدة» تهجئة لمدخل موجود:

</div>
<div dir="ltr">

```bash
python3 skills/quranic-terminology/scripts/lookup.py --search waqf
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"   # يصوغ المسودة
```

</div>
<div dir="rtl">

وإن كان المفهوم جديدًا حقًا، فـ`propose.py` يصوغ مسودة الاقتراح بحقول المدخل، والاسم البرمجي يُشتق من العربية المشكولة. ولفحص مشروع في `CI` شغّل `audit_terminology.py <dir> --strict`، وملف `.terminology.json` في المشروع يُسكت الإنذارات الكاذبة المعروفة (نموذجه في `skills/quranic-terminology/assets/terminology.example.json`).

## المتطلبات

البناء يحتاج إلى Python 3 والحزم في `requirements.txt`، والموقع يحتاج إلى Node:

</div>
<div dir="ltr">

```bash
pip install -r requirements.txt
cd site && npm install
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
| `content/ar/03-terminology/dictionary.md` و`content/en/…/dictionary.md` | المدخل نفسه، بحقوله العربية والإنجليزية | `python3 tools/generate_dictionary.py` |
| `skills/quranic-terminology/` كله، ومنه `data/terminology.json` | المصدر الذي بُني منه | `python3 tools/generate_skill.py` |

## قبل الإرسال

</div>
<div dir="ltr">

```bash
python3 tools/build.py
```

</div>
<div dir="rtl">

يشغّل `build.py` كل خطوات البناء بترتيبها، 14 خطوة اليوم: اختبار قواعد التهجئة، وتوليد مداخل العلامات وسجل أحكام التجويد، وبناء الفهرسين، ومطابقة أعداد الآي، والتحقق من كل مدخل على المخطط وعلى المعيار، وفحص السجلات، وتوليد القاموس وصفحات السجلات بلغتيه، وفحص الأسماء في النثر وملفات النماذج، وتوليد المهارة. القائمة الكاملة في [`tools/README.md`](tools/README.md)، و`make build` يشغّل الأمر نفسه. وأدرج الملفات المولّدة في الـ`PR` نفسه.

## حال الصفحة

كل صفحة تحمل `status` في الـ`frontmatter`:

- `draft` — قيد الكتابة ولا يُبنى عليها.
- `proposed` — نوقشت وتنتظر الاعتماد.
- `adopted` — ملزمة لمشاريعنا. ولا يُوسم بها مدخل بلا مصدر يثبت تعريفه.

## العربية والإنجليزية

`content/ar` و`content/en` متقابلان ملفًا بملف، والصفحة الموجودة في لغة واحدة تُعَدّ نقصًا معروفًا يُستكمل لاحقًا. العربية أصل لصفحات النص والمصطلحات، والإنجليزية أصل لصفحات الهندسة.

</div>

---

# Contributing

Open an issue before sending a PR, because the guidelines change through discussion.

## How a change is proposed

1. **Open an issue** describing the **real case** that prompted the change: which project, which place, what was ambiguous or impossible. A rule with no case behind it is not adopted.
2. **Wait for agreement.** Rules have long reach; changing one after adoption costs more than discussing it before.
3. **Send a PR** once there is agreement, answering the checklist.

There are 3 forms: [`term.yml`](.github/ISSUE_TEMPLATE/term.yml) to propose a term, [`proposal.yml`](.github/ISSUE_TEMPLATE/proposal.yml) to propose a guideline, and [`edit.yml`](.github/ISSUE_TEMPLATE/edit.yml) to correct one paragraph; every paragraph on the site links to it.

Before proposing a term, search first. Most "new" terms are spellings of an entry that exists:

```bash
python3 skills/quranic-terminology/scripts/lookup.py --search waqf
python3 skills/quranic-terminology/scripts/propose.py waqf_lazim "الوَقْف اللَّازِم"   # drafts the proposal
```

If the concept is genuinely new, `propose.py` drafts the proposal with the entry's fields, deriving the code name from the vocalised Arabic. To audit a project in CI run `audit_terminology.py <dir> --strict`; a `.terminology.json` in the project silences known false positives (example in `skills/quranic-terminology/assets/terminology.example.json`).

## Prerequisites

The build needs Python 3 and the packages in `requirements.txt`; the site needs Node:

```bash
pip install -r requirements.txt
cd site && npm install
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
| `content/ar/03-terminology/dictionary.md` and `content/en/…/dictionary.md` | the entry itself, Arabic and English fields | `python3 tools/generate_dictionary.py` |
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

`content/ar` and `content/en` mirror each other file for file. A page that exists in one language only is a known gap to be filled later. Arabic is the source for the text and terminology pages; English is the source for the engineering pages.
