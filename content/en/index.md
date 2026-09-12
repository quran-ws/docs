---
title: Quran.ws Guidelines
description: How we build software that handles the Quran. Naming, text handling, versioning, engineering and repositories, each rule with the check behind it.
status: draft
template: splash
hero:
  tagline: How we build software that handles the Quran. Five short pages of rules, each with the check that enforces it.
  actions:
    - text: Start with naming
      link: /guidelines/en/naming/
      icon: right-arrow
    - text: Repository
      link: https://github.com/quran-ws/docs
      icon: external
      variant: minimal
---

<dl class="qw-meta">
  <div>
    <dt>STATUS</dt>
    <dd>Proposed — nothing adopted yet</dd>
  </div>
  <div>
    <dt>LICENSE</dt>
    <dd class="mono">CC BY 4.0 · MIT</dd>
  </div>
  <div>
    <dt>SOURCE</dt>
    <dd class="mono">quran-ws/docs</dd>
  </div>
  <div>
    <dt>LANG</dt>
    <dd>العربية · English</dd>
  </div>
</dl>

## Guidelines

Every rule is one sentence, an example, and the check that catches a violation.
Read them in order the first time; after that, each page stands on its own.

<div class="qw-index">

  <div class="qw-index-row">
    <span class="qw-index-num">1</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/naming/">Naming</a>
      <p>One concept, one name, the same in the model, the table, the foreign key and the API. Is it <code>ayah</code> or <code>verse</code>? It is <code>ayah</code>, and here is why.</p>
    </div>
    <span class="qw-index-state status-proposed">proposed</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">2</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/quranic-text/">Quranic text</a>
      <p>The text is transmitted source data, never edited. Encoding, normalisation, tokenisation, display, and the tests that guard them.</p>
    </div>
    <span class="qw-index-state status-proposed">proposed</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">3</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/versioning/">Versioning and corrections</a>
      <p>A dataset is released, never edited. Semantic versioning for data, the errata log, and how a reader is told the text changed.</p>
    </div>
    <span class="qw-index-state status-proposed">proposed</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">4</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/engineering/">Engineering</a>
      <p>Model the mushaf, not the screen. Tables, identifiers, APIs, storage, fonts, audio, search and caching.</p>
    </div>
    <span class="qw-index-state status-proposed">proposed</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">5</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/repositories/">Repositories and licensing</a>
      <p>Layout, commits, review, releases, what a dependant may rely on, and the licences everything is published under.</p>
      <span class="qw-index-links">
        <a href="/guidelines/en/licensing/">waqf and open licensing</a>
      </span>
    </div>
    <span class="qw-index-state status-proposed">proposed</span>
  </div>

</div>

## Reference

Looked up, not read through. The guidelines link into these where a rule needs them.

<div class="qw-index">

  <div class="qw-index-row">
    <div class="qw-index-body">
      <a href="/guidelines/en/reference/dictionary/">Dictionary</a>
      <p>Every concept with its canonical name, its definition, its spellings and its source.</p>
      <span class="qw-index-links">
        <a href="/guidelines/en/reference/registries/">registries</a>
        <a href="/guidelines/en/reference/standard/">terminology standard</a>
        <a href="/guidelines/en/reference/decisions/">decision record</a>
      </span>
    </div>
  </div>

</div>

## Use it in your repository

The terminology audit reads a codebase and reports every name the standard would have written differently. It renames nothing.

```bash
python3 skills/quranic-terminology/scripts/audit_terminology.py src --strict
```

Run it in CI on every pull request, and keep what your project already knows in `.terminology.json`. The [naming page](/guidelines/en/naming/) says how.

:::caution[Nothing is adopted yet]
Build against a page only once it is marked `adopted`. Until then these are proposals: what concerns the Quranic text itself is reviewed by qualified scholars, and what concerns engineering is one defensible choice among several.
:::
