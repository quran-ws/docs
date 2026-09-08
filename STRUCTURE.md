<div dir="rtl">

# بنية المستودع

المحتوى مكتوب بـ`Markdown` عادي داخل `content/` ليبقى مقروءًا على GitHub مباشرة، ويُبنى بموقع Astro Starlight في `site/` يربط `content/ar` و`content/en` لغتين. و`standards/` هو المصدر المقروء آليًا، و`tools/` يشتق منه ويفحصه ويولّد الصفحات والمهارة.

</div>

# Repository layout

Content is authored as plain Markdown under `content/`, so it stays readable on GitHub, and is rendered by the Astro Starlight site in `site/`, which maps `content/ar` and `content/en` to its two locales. `standards/` is the machine-readable source; `tools/` derives from it, checks it, and generates the pages and the skill.

```text
guidelines/
├── README.md                          # what this repository is (Arabic + English) — ما هذا المستودع
├── STRUCTURE.md                       # this file — هذا الملف
├── CONTRIBUTING.md                    # how a change is proposed and reviewed — كيف يُقترح التغيير
├── LICENSE                            # CC BY 4.0 for prose, MIT for code and data — الرخصتان
├── requirements.txt                   # Python packages the build needs
├── Makefile                           # install / build / test / site / clean
│
├── content/                           # the guideline pages — الصفحات
│   ├── ar/                            # Arabic: the source for text and terminology pages
│   │   ├── index.md                   # landing page
│   │   ├── 01-intro/                  # writing-style.md, writing-guides.md
│   │   ├── 02-quranic-text/           # handling Quranic text
│   │   ├── 03-terminology/            # standard.md, decisions.md, and the generated
│   │   │                              #   dictionary.md and registries.md
│   │   ├── 04-versioning/             # versioning and corrections
│   │   ├── 05-repositories/           # repositories, review, releases, and the licensing policy
│   │   └── 06-engineering/            # APIs, data, rendering, audio
│   └── en/                            # English mirror, file for file; the source for engineering pages
│
├── standards/                         # machine-readable source — المصدر المقروء آليًا
│   └── terminology/
│       ├── schema.json                # the shape of an entry
│       ├── sources.yml                # the sources entries cite, and how to cite each
│       ├── aliases.json               # generated: every attested spelling → its concept
│       ├── registry_aliases.json      # generated: every member spelling → its member, by kind
│       ├── concepts/                  # one YAML file per concept — ملف لكل مفهوم
│       ├── registries/                # closed sets, one row per member — المجموعات المغلقة
│       │   ├── surahs.tsv             # 114 surahs
│       │   ├── qiraat.tsv             # 10 qiraat, 19 rawis, 20 riwayahs
│       │   ├── tariq.tsv              # the tariqs below the riwayahs
│       │   ├── ayah_numbering.tsv     # the 6 numbering systems and their totals
│       │   ├── ayah_counts.tsv        # generated: ayahs per surah in each system, from al-Bayan
│       │   ├── sajdah.tsv             # the 15 sajdahs
│       │   └── tajwid_rules.tsv       # generated: the tajwid rulings, from tajweed_engine_rules.json
│       └── data/                      # what the derivation and the generators read
│           ├── dabt_marks.tsv         # 35 marks with their names
│           ├── letter_names.tsv       # letter names as they are said
│           ├── established_spellings.tsv, general_words.tsv, connectives.tsv
│           ├── hafs_svg_*.tsv         # a project's glossary and structure, as surveyed
│           └── tajweed_engine_rules.json
│
├── tools/                             # derive, check, generate — see tools/README.md
│   ├── build.py                       # the build: every step, in order
│   ├── translit.py                    # Canonical Code Spelling from vocalised Arabic
│   ├── check_*.py                     # checks: schema, conformance, registries, prose names,
│   │                                  #   example files, issue templates
│   ├── generate_*.py                  # generators: marks, tajwid registry, dictionary,
│   │                                  #   registry pages, skill
│   ├── audit_text.py                  # recomputes the figures the text page cites
│   └── skill_template/                # the skill's text, scripts and assets, filled at build
├── tests/                             # pytest over the tools and generators
│
├── skills/
│   └── quranic-terminology/           # the agent skill, generated whole on every build
├── .claude-plugin/                    # plugin manifest: /plugin marketplace add quran-ws/guidelines
│
├── surveys/                           # real codebases measured against the standard — نتائج لا قواعد
│   ├── README.md, OPEN.md             # what a survey is; what the surveys left undecided
│   └── quranpedia-net.md, quranpedia-net-renames.tsv
├── examples/                          # checked samples in canonical names — نماذج مفحوصة
│   ├── schema/                        # quran_text.sql, quran_text.prisma
│   ├── api/                           # ayah.openapi.yml
│   ├── data/                          # mushaf_edition.json, ayah.json, errata.json
│   ├── migrations/                    # 0001_rawi_to_riwayah.sql
│   └── tests/                         # test_text_invariants.py, truncation.js
│
├── site/                              # Astro Starlight; src/content.config.ts reads ../content
│   └── src/plugins/suggest-edit.mjs   # the "suggest an edit" link on every paragraph
└── .github/
    ├── ISSUE_TEMPLATE/                # term.yml, proposal.yml, edit.yml
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/                     # build.yml (the build and tests), pages.yml (the site)
```

<div dir="rtl">

## قواعد التنظيم

- **أرقام المجلدات** (`01-`، `02-`) تثبّت ترتيب القراءة على GitHub وفي شريط الموقع. الأرقام للترتيب فقط، ولا يُشار إلى قسم برقم مجلده في النثر.
- **`ar` و`en` متقابلان ملفًا بملف.** الصفحة الموجودة في لغة واحدة نقص معروف، وليست بنية مختلفة. العربية أصل لصفحات النص القرآني والمصطلحات، والإنجليزية أصل لصفحات الهندسة.
- **كل صفحة تذكر حالها في الـ`frontmatter`**: `draft` أو `proposed` أو `adopted`. ولا يلزم مشاريعنا إلا ما وُسم `adopted`.
- **المفهوم يُعرف في مدخل، والفرد يُذكر في صف من سجل.** `concepts/` لما يحتاج إلى تعريف، و`registries/` للمجموعات المغلقة التي لا يحمل أفرادها إلا أسماءهم ومواضعهم في المجموعة: 10 قراءات، و114 سورة. ومدخل المفهوم يسمي سجله، و`tools/check_registries.py` يفحص الصفوف.
- **`skills/` مولّد ولا يُعدَّل.** `tools/generate_skill.py` يكتبه كاملًا في كل بناء من `standards/` و`content/en`، فلا تذكر المهارة قاعدة لا يذكرها المعيار.
- **`standards/` هو المصدر، و`content/` يشرحه.** جداول المصطلحات في النثر تُولَّد من `standards/terminology/concepts/*.yml`، ولا تُكتب باليد في موضعين.
- **`surveys/` نتائج، و`examples/` نماذج مفحوصة.** الفحص لا يغيّر المعيار، وإنما يصير حالة يستند إليها اقتراح. والنماذج يفحصها البناء، فما فيها يطابق ما يقوله المعيار اليوم.

</div>

## Conventions

- **Numbered section directories** (`01-`, `02-`) fix reading order on GitHub and in the site sidebar. Numbers fix order only; never cite a section by its directory number in prose.
- **`ar` and `en` mirror each other file for file.** A page that exists in one locale and not the other is a known gap, not a different structure. Arabic is the source for the Quranic-text and terminology pages; English is the source for the engineering pages.
- **Every page states its status in frontmatter**: `draft`, `proposed`, or `adopted`. Only `adopted` pages bind our projects.
- **A concept gets an entry, a member gets a row.** `concepts/` holds what needs a definition; `registries/` holds closed sets whose members have nothing to say beyond their name and their place in the set: the 10 qiraat, the 114 surahs. The concept entry names its registry, and `tools/check_registries.py` checks the rows.
- **`skills/` is generated, never edited.** `tools/generate_skill.py` writes it whole on every build, from `standards/` and `content/en`, so the skill an agent runs cannot state a rule the standard does not.
- **`standards/` is the source of truth; `content/` explains it.** The terminology tables in prose are generated from `standards/terminology/concepts/*.yml`, never hand-maintained in two places.
- **`surveys/` holds findings; `examples/` holds checked samples.** A survey never changes the standard by itself; it becomes the case behind a proposal. The examples are checked by the build, so what they show is what the standard says today.
