# Repository structure — بنية المستودع

Proposed layout. Content is authored as plain Markdown under `content/` so it stays readable on GitHub, and is rendered later by an Astro Starlight site that maps `content/en` and `content/ar` to its two locales.

المحتوى مكتوب Markdown عاديًا داخل `content/` ليبقى مقروءًا على GitHub مباشرة، ويُبنى لاحقًا بموقع Astro Starlight يربط `content/en` و`content/ar` كلغتين.

```text
guidelines/
├── README.md                      # ما هذا المستودع (عربي + إنجليزي)
├── STRUCTURE.md                   # هذا الملف
├── CONTRIBUTING.md                # كيف تُقترح التغييرات وتُناقش
├── GLOSSARY.md                    # اختصار سريع للمصطلحات، يشير إلى المعيار الكامل
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
│       └── concepts/              # ملف YAML لكل مفهوم
│           ├── ayah.yml        # entity
│           ├── makki.yml       # classification_value مع parent
│           └── tajwid.yml      # discipline
│
├── examples/                      # أمثلة كود قصيرة يشير إليها المحتوى
├── site/                          # موقع Astro Starlight (لاحقًا)
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
- **`standards/` is the source of truth, `content/` explains it.** The terminology tables in prose are generated from `standards/terminology/concepts/*.yml`, never hand-maintained in two places.
