## ما الذي يغيره هذا؟ — What does this change?

<!-- سطر أو سطران. ما القاعدة أو المدخل الذي تغير؟
     One or two lines. Which rule or entry changed? -->

## الحالة التي دفعت إليه — The case behind it

<!-- الأدلة تتغير بحالة واقعية واجهناها، لا بتفضيل عام. اذكر المشروع والموضع، أو رقم الـ`Issue` الذي نوقش فيه.
     The guidelines change through a real case, not a preference. Name the project and the place, or the issue where it was discussed. -->

## قبل المراجعة — Before review

- [ ] نوقش في `Issue` قبل هذا الـ`PR`. — Discussed in an issue before this PR.
- [ ] `python3 tools/build.py` يمر، والملفات المولّدة مضمنة في الـ`PR`: `dictionary.md` بلغتيه، و`aliases.json`، و`registry_aliases.json`، و`skills/quranic-terminology/`. — `python3 tools/build.py` passes, and the generated files are in the PR.
- [ ] إن أضاف مدخلًا: أُجيب عن أسئلة قسم «قاعدة قبول أي مصطلح جديد» في المعيار، وله مصدر في `sources.yml`. — If it adds an entry: the questions of "The rule for accepting a new term" are answered, and it cites a source from `sources.yml`.
- [ ] إن غيّر اسمًا: الاسم القديم مسجل في `alternative_spellings` أو `deprecated`. — If it renames: the old name is recorded in `alternative_spellings` or `deprecated`.
- [ ] إن مس قواعد التهجئة: الحالات المتغيرة في `tools/test_translit.py` مذكورة. — If it touches the spelling rules: the golden cases that changed are listed.
- [ ] إن أضاف قاعدة: كُتب معها ما يتحقق منها. — If it adds a rule: what checks it is written with it.
- [ ] `status` صحيح، ولا يُوسم `adopted` ما ليس له مصدر. — `status` is right, and nothing is `adopted` without a source.
- [ ] النسخة العربية والإنجليزية لم تتباعدا، أو التباعد مذكور صراحة. — The Arabic and English versions still match, or the gap is stated.
