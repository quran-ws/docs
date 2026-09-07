---
title: المصطلحات
description: اسم واحد لكل مفهوم، وتهجئة مشتقة، ومصدر مقروء آليًا.
status: draft
sidebar:
  order: 0
---

- [معيار المصطلحات](/guidelines/ar/03-terminology/standard/) — كيف يسمى المفهوم: اسم Canonical واحد، وتهجئة تُشتق بدالة موثقة ولا تُختار، والحقول التي يوضع فيها كل اسم.
- [سجل القرارات](/guidelines/ar/03-terminology/decisions/) — القرارات التي كان فيها خلاف، كل منها مؤرخ، بقراره وسببه ودليله.
- [قاموس المصطلحات](/guidelines/ar/03-terminology/dictionary/) — المفاهيم بتعريفاتها وأسمائها، مولدة من `standards/terminology/concepts/`. وكل مدخل مكتوب باللغتين، وكل صفحة تولد من جانب لغتها في المدخل.
- [السجلات](/guidelines/ar/03-terminology/registries/) — أفراد المجموعات المغلقة التي يشير إليها القاموس: السور، والقراءات ورواتها ورواياتها، وأنظمة عد الآي وأعدادها، ومواضع السجدة.

والمصدر نفسه معبأ مهارة للوكلاء في
[`skills/quranic-terminology/`](https://github.com/quran-ws/guidelines/tree/main/skills/quranic-terminology)،
وفيها المعيار والقاموس والسجلات وسكربتات تحل التهجئة إلى مفهومها وتشتق الاسم وتفحص كودًا قائمًا على المعيار. انسخ المجلد إلى مجلد مهارات وكيلك. والمهارة تولد في كل بناء وتحمل بصمة (`hash`) مدخلاتها، فلا تختلف عن المداخل أبدًا.

والمصدر المقروء آليًا مستقل عن اللغة، ويمكن استعماله وحده:

| الملف | ما فيه |
| --- | --- |
| `standards/terminology/concepts/*.yml` | ملف لكل مفهوم |
| `standards/terminology/schema.json` | مخطط المدخل |
| `standards/terminology/registries/*.tsv` | أفراد كل مجموعة مغلقة، سطر لكل فرد |
| `standards/terminology/data/*.tsv` | جداول التهجئة التي يقرؤها الاشتقاق: أسماء الحروف، والكلمات العامة، وحروف الربط، والتهجئات المستقرة |
| `standards/terminology/aliases.json` | كل تهجئة معروفة لمفهوم، محلولة إليه |
| `standards/terminology/registry_aliases.json` | كل تهجئة معروفة لفرد، محلولة إليه، مفهرسة بالـ`kind` |
| `standards/terminology/sources.yml` | المصادر التي تحيل إليها المداخل وسطور السجلات |
