# المساهمة — Contributing

<div dir="rtl">

الأدلة تتغير بالنقاش لا بالـcommit المباشر.

## كيف يقترح تغيير

1. **افتح Issue** يشرح **الحالة الواقعية** التي دفعت إليه: أي مشروع، وأي موضع، وما الذي التبس أو تعذر. القاعدة التي لا حالة وراءها لا تعتمد.
2. **انتظر الاتفاق.** القواعد أثرها ممتد، وتغييرها بعد اعتمادها أغلى من مناقشتها قبله.
3. **أرسل PR** بعد الاتفاق، وأجب فيه عن قائمة المراجعة.

لاقتراح مصطلح استعمل قالب [`term.yml`](.github/ISSUE_TEMPLATE/term.yml)، ولاقتراح قاعدة [`proposal.yml`](.github/ISSUE_TEMPLATE/proposal.yml).

## ما لا يعدل باليد

هذه الملفات مولّدة، وأي تعديل فيها يضيع عند إعادة التوليد:

| لا تعدل | عدل | ثم |
| --- | --- | --- |
| `standards/terminology/aliases.json` | `alternative_spellings` في المدخل | `python3 tools/build_aliases.py` |
| مداخل علامات الضبط | `standards/terminology/data/dabt_marks.tsv` | `python3 tools/generate_dabt.py` |
| كتلة `unicode` في أي مدخل | لا شيء، تقرأ من قاعدة يونيكود | `python3 tools/generate_dabt.py` |
| تهجئة `code` | `names.arabic.vocalized` | تشتق تلقائيًا |
| `content/ar/03-terminology/dictionary.md` و`content/en/…/dictionary.md` | المدخل نفسه، بحقوله العربية والإنجليزية | `python3 tools/generate_dictionary.py` |
| `skills/quranic-terminology/` كله | المصدر الذي بنيت منه | `python3 tools/generate_skill.py` |

## قبل الإرسال

```bash
python3 tools/build.py            # يولّد كل شيء ويفحصه بترتيبه
```

وهو يشمل `test_translit.py` و`validate.py` و`build_aliases.py`
و`check_conformance.py` و`check_examples.py`، وينتهي بتوليد المهارة.

## حال الصفحة

كل صفحة تحمل `status` في الـfrontmatter:

- `draft` — قيد الكتابة ولا يبنى عليها.
- `proposed` — نوقشت وتنتظر الاعتماد.
- `adopted` — ملزمة لمشاريعنا. ولا يوسم بها مدخل بلا مصدر يثبت تعريفه.

## العربية والإنجليزية

`content/ar` و`content/en` متقابلان ملفًا بملف، والصفحة الموجودة في لغة واحدة
تعتبر نقصًا معروفًا يستكمل لاحقًا. العربية أصل لصفحات النص والمصطلحات،
والإنجليزية أصل لصفحات الهندسة.

</div>

---

Guidelines change through discussion, not direct commits.

1. **Open an issue** describing the **real case** that prompted the change — which project, which place, what was ambiguous or impossible. A rule with no case behind it doesn't get adopted.
2. **Wait for agreement.** Rules have long reach; changing one after adoption costs more than discussing it before.
3. **Send a PR** once there's agreement, answering the checklist.

Run `python3 tools/build.py` before sending: it generates and checks everything, in order, and ends by rebuilding the agent skill. Never hand-edit generated output — the table above says what regenerates what.
