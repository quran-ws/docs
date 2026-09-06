---
title: المصطلحات
description: اسم واحد لكل مفهوم، وتهجئة مشتقة، ومصدر مقروء آليًا.
status: draft
sidebar:
  order: 1
---

- [معيار المصطلحات](/guidelines/ar/03-terminology/standard/) — كيف يسمى المفهوم: اسم Canonical واحد، وتهجئة تشتق بدالة موثقة لا تختار، والحقول التي يسكنها كل اسم.
- [سجل القرارات](/guidelines/ar/03-terminology/decisions/) — القرارات التي كان فيها خلاف، بقرارها وسببها ودليلها.
- [قاموس المصطلحات](/guidelines/ar/03-terminology/dictionary/) — 117 مفهومًا، مولدة من `standards/terminology/concepts/`.

والمصدر المقروء آليًا مستقل عن اللغة، ويستعمل الآن:

| الملف | ما فيه |
| --- | --- |
| `standards/terminology/concepts/*.yml` | ملف لكل مفهوم |
| `standards/terminology/schema.json` | مخطط المدخل |
| `standards/terminology/aliases.json` | كل تهجئة معروفة، محلولة إلى مفهومها |
| `standards/terminology/sources.yml` | المصادر التي تحيل إليها المداخل |
