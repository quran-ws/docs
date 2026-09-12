---
title: أدلة Quran.ws
description: كيف نبني برمجيات تتعامل مع القرآن، وتشمل التسمية والتعامل مع النص والإصدارات والهندسة والمستودعات، مع وسيلة للتحقق من كل قاعدة.
status: draft
template: splash
hero:
  tagline: كيف نبني برمجيات تتعامل مع القرآن، في 5 صفحات قصيرة، مع وسيلة للتحقق من الالتزام بكل قاعدة.
  actions:
    - text: ابدأ بالتسمية
      link: /guidelines/ar/naming/
      icon: right-arrow
    - text: المستودع
      link: https://github.com/quran-ws/docs
      icon: external
      variant: minimal
---

<dl class="qw-meta">
  <div>
    <dt>الحالة</dt>
    <dd>مقترح — لا شيء معتمد بعد</dd>
  </div>
  <div>
    <dt>الرخصة</dt>
    <dd class="mono">CC BY 4.0 · MIT</dd>
  </div>
  <div>
    <dt>المصدر</dt>
    <dd class="mono">quran-ws/docs</dd>
  </div>
  <div>
    <dt>اللغة</dt>
    <dd>العربية · English</dd>
  </div>
</dl>

## الأدلة

نصوغ كل قاعدة في جملة واحدة ونرفق بها مثالًا وفحصًا يكشف مخالفتها.
اقرأ الصفحات بالترتيب في المرة الأولى، وبعدها يمكنك قراءة كل صفحة وحدها.

<div class="qw-index">

  <div class="qw-index-row">
    <span class="qw-index-num">1</span>
    <div class="qw-index-body">
      <a href="/guidelines/ar/naming/">التسمية</a>
      <p>نستخدم لكل مفهوم اسمًا واحدًا في النموذج والجدول والمفتاح الأجنبي وواجهة <code>API</code>. هل نكتب <code>ayah</code> أم <code>verse</code>؟ نكتب <code>ayah</code>، وهنا نبيّن السبب.</p>
    </div>
    <span class="qw-index-state status-proposed">مقترح</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">2</span>
    <div class="qw-index-body">
      <a href="/guidelines/ar/quranic-text/">النص القرآني</a>
      <p>نحفظ النص كما نُقل من مصدره دون تعديل، وهذه قواعد الترميز والتطبيع والتقسيم والعرض والاختبارات التي تتحقق من سلامتها.</p>
    </div>
    <span class="qw-index-state status-proposed">مقترح</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">3</span>
    <div class="qw-index-body">
      <a href="/guidelines/ar/versioning/">الإصدارات والتصحيحات</a>
      <p>ننشر كل <code>dataset</code> في إصدارات دون تعديله مباشرة، وهذه قواعد الترقيم الدلالي للبيانات وسجل التصحيحات وطريقة إبلاغ القارئ بتغيّر النص.</p>
    </div>
    <span class="qw-index-state status-proposed">مقترح</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">4</span>
    <div class="qw-index-body">
      <a href="/guidelines/ar/engineering/">الهندسة</a>
      <p>ابنِ نموذج البيانات على المصحف نفسه بدل ما يظهر على الشاشة، وهذه قواعد الجداول والمعرفات وواجهات <code>API</code> والتخزين والخطوط والصوت والبحث والتخزين المؤقت.</p>
    </div>
    <span class="qw-index-state status-proposed">مقترح</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">5</span>
    <div class="qw-index-body">
      <a href="/guidelines/ar/repositories/">المستودعات والترخيص</a>
      <p>بنية المستودع وتغييرات <code>commit</code> والمراجعة والإصدارات، وما يمكن للمشاريع التي تعتمد علينا توقعه، والرخص التي ننشر كل ذلك بموجبها.</p>
      <span class="qw-index-links">
        <a href="/guidelines/ar/licensing/">الوقف والترخيص المفتوح</a>
      </span>
    </div>
    <span class="qw-index-state status-proposed">مقترح</span>
  </div>

</div>

## المراجع

ارجع إلى هذه الصفحات عند الحاجة دون قراءتها كاملة، وستجد روابطها في القواعد التي تحتاج إليها.

<div class="qw-index">

  <div class="qw-index-row">
    <div class="qw-index-body">
      <a href="/guidelines/ar/reference/dictionary/">القاموس</a>
      <p>كل مفهوم باسمه المعتمد وتعريفه وتهجئاته ومصدره.</p>
      <span class="qw-index-links">
        <a href="/guidelines/ar/reference/registries/">السجلات</a>
        <a href="/guidelines/ar/reference/standard/">معيار المصطلحات</a>
        <a href="/guidelines/ar/reference/decisions/">سجل القرارات</a>
      </span>
    </div>
  </div>

</div>

## شغّل الفحص في مستودعك

تفحص أداة المصطلحات الكود وتذكر كل اسم تختلف صيغته عما يحدده المعيار، دون إعادة تسمية أي شيء.

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

شغّل الفحص في `CI` مع كل طلب دمج، وسجّل معلومات مشروعك التي يحتاجها الفحص في `.terminology.json`، وتشرح [صفحة التسمية](/guidelines/ar/naming/) الطريقة.

:::caution[لا شيء معتمد بعد]
اعتمد على الصفحة بعد أن تحمل الحالة `adopted` فقط، وإلى ذلك الحين تبقى هذه القواعد مقترحات. يراجع أهل العلم المؤهلون ما يتعلق بالنص القرآني نفسه، أما القواعد الهندسية فهي اختيارات من عدة خيارات صحيحة.
:::
