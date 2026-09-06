# Repository structure — بنية المستودع

Proposed layout. Content is authored as plain Markdown under `content/` so it stays readable on GitHub, and is rendered later by an Astro Starlight site that maps `content/en` and `content/ar` to its two locales.

المحتوى مكتوب Markdown عاديًا داخل `content/` ليبقى مقروءًا على GitHub مباشرة، ويُبنى لاحقًا بموقع Astro Starlight يربط `content/en` و`content/ar` كلغتين.

```text
guidelines/
├── README.md                      # ما هذا المستودع (عربي + إنجليزي)
├── STRUCTURE.md                   # هذا الملف
├── CONTRIBUTING.md                # كيف تُقترح التغييرات وتُناقش
├── LICENSE                        # CC BY 4.0 للنصوص، MIT للكود
│
├── content/
│   ├── ar/                        # النسخة العربية (المصدر لأكثر المحتوى)
│   │   ├── 01-intro/              # لماذا هذه الأدلة، كيف تُقرأ، كيف نتخذ القرار
│   │   ├── 02-quranic-text/       # أدبيات التعامل مع النص القرآني
│   │   ├── 03-terminology/        # دليل المصطلحات
│   │   │   ├── standard.md        # Quranic Software Terminology Standard
│   │   │   └── dictionary.md      # Quranic Software Terminology Dictionary
│   │   ├── 04-versioning/         # الإصدارات والتصحيحات والإعلام عنها
│   │   ├── 05-open-source/        # الرخص، Git، المراجعة، الإصدار
│   │   └── 06-engineering/        # APIs، البيانات، عرض المصحف، الصوت
│   └── en/                        # English mirror, same section numbering
│       ├── 01-intro/
│       ├── 02-quranic-text/
│       ├── 03-terminology/
│       ├── 04-versioning/
│       ├── 05-open-source/
│       └── 06-engineering/
│
├── standards/                     # المصادر Machine-readable
│   └── terminology/
│       ├── schema.json            # بنية الـEntry حسب القسم 27
│       ├── sources.yml            # سجل المصادر وصيغة الإحالة لكل مصدر
│       ├── aliases.json           # مولد: كل تهجئة معروفة تحل إلى مفهومها
│       ├── data/                  # السجلات كما وردت من المشاريع
│       │   ├── dabt_marks.tsv     # 35 علامة بأسمائها الخمسة
│       │   ├── hafs_svg_*.tsv     # مسرد المشروع وبنيته ونموذج الكلمة
│       │   └── tajweed_engine_rules.json
│       ├── registries/            # المجموعات المغلقة: سطر لكل فرد
│       │   ├── qiraat.tsv         # ١٠ قراءات، ١٩ راوياً، ٢٠ رواية
│       │   ├── surahs.tsv         # ١١٤ سورة
│       │   ├── ayah_numbering.tsv # مذاهب العد الستة وجملها
│       │   ├── ayah_counts.tsv    # عدد آي كل سورة في المذاهب الستة
│       │   └── sajdah.tsv         # ١٥ موضع سجدة
│       └── concepts/              # ملف YAML لكل مفهوم
│           ├── ayah.yml
│           ├── waqf_lazim.yml     # مولد من dabt_marks.tsv
│           └── ...
│
├── tools/                         # ما يشتق الأسماء ويقيسها ويتحقق منها
│   ├── build.py                   # البناء: كل خطوة بترتيبها
│   └── skill_template/            # نص المهارة وسكربتاتها، تملأ عند البناء
├── skills/
│   └── quranic-terminology/       # مهارة الوكيل، مولدة كاملة في كل بناء
├── examples/                      # أمثلة كود قصيرة يشير إليها المحتوى
├── site/                          # موقع Astro Starlight
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── proposal.yml           # اقتراح قاعدة جديدة أو تعديل قاعدة
    │   └── term.yml               # اقتراح مصطلح أو تهجئة
    └── PULL_REQUEST_TEMPLATE.md
```

## Conventions — قواعد التنظيم

- **Numbered section directories** (`01-`, `02-`) fix reading order in both plain GitHub browsing and the generated site sidebar. Numbers are for ordering only; never reference them in links from prose.
- **`ar` and `en` mirror each other file-for-file.** A page that exists in one locale and not the other is a known gap, not a different structure. Arabic is the authoring source for text-adab and terminology; English is the source for engineering pages.
- **Every page states its status in frontmatter**: `draft`, `proposed`, or `adopted`. Only `adopted` pages are binding on our projects.
- **A concept gets an entry, a member gets a row.** `concepts/` holds what needs a definition; `registries/` holds closed sets whose members have nothing to say beyond their name and their place in the set — the ten qiraat, the 114 surahs. The concept entry names its registry, and `tools/check_registries.py` checks the rows.
- **`skills/` is generated, never edited.** `tools/generate_skill.py` writes it whole on every build, from `standards/` and `content/en`, so the skill an agent runs cannot state a rule the standard does not.
- **`standards/` is the source of truth, `content/` explains it.** The terminology tables in prose are generated from `standards/terminology/concepts/*.yml`, never hand-maintained in two places.
