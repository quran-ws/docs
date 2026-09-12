## ما الذي يغيره هذا؟ — What does this change?

<!-- سطر أو سطران. ما القاعدة أو المدخل الذي تغير؟
     One or two lines. Which rule or entry changed? -->

## الحالة التي دفعت إليه — The case behind it

<!-- تعديل قاعدة أو مصطلح يذكر المشروع والموضع، أو رقم الـ`Issue` الذي نوقش فيه. وتصحيح فقرة لا يحتاج إلى `Issue`.
     A change to a rule or a term names the project and the place, or the issue where it was discussed. A one-paragraph fix needs no issue. -->

## قبل المراجعة — Before review

- [ ] `python3 tools/build.py` و`python3 -m pytest -q` يمران، والملفات المولّدة مضمنة. — `python3 tools/build.py` and `python3 -m pytest -q` pass, and the generated files are in the PR.
- [ ] إن مس قاعدة: عُدّلت في `content/pages/`، والعربية معها أو مذكور أنها تنتظر. — If it touches a rule: it was edited in `content/pages/`, with its Arabic, or the gap is stated.
- [ ] إن أضاف مدخلًا أو غيّر اسمًا: له مصدر في `sources.yml`، والاسم القديم في `alternative_spellings` أو `deprecated`. — If it adds an entry or renames: it cites a source from `sources.yml`, and the old name is kept in `alternative_spellings` or `deprecated`.
