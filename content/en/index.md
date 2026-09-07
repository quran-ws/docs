---
title: Quran.ws Guidelines
description: Internal guidelines and open standards for the Quran.ws infrastructure.
status: draft
template: splash
hero:
  tagline: How we write code, handle Quranic text, name concepts, and manage releases and corrections.
  actions:
    - text: Terminology standard
      link: /guidelines/en/03-terminology/standard/
      icon: right-arrow
    - text: Repository
      link: https://github.com/quran-ws/guidelines
      icon: external
      variant: minimal
---

<dl class="qw-meta">
  <div>
    <dt>STATUS</dt>
    <dd>Draft — nothing adopted yet</dd>
  </div>
  <div>
    <dt>LICENSE</dt>
    <dd class="mono">CC BY 4.0 · MIT</dd>
  </div>
  <div>
    <dt>SOURCE</dt>
    <dd class="mono">quran-ws/guidelines</dd>
  </div>
  <div>
    <dt>LANG</dt>
    <dd>العربية · English</dd>
  </div>
</dl>

## Areas

<div class="qw-index">

  <div class="qw-index-row">
    <span class="qw-index-num">§01</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/01-intro/">Introduction</a>
      <p>Writing style, and how the guides themselves are written.</p>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">§02</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/02-quranic-text/">Handling Quranic text</a>
      <p>Immutable source text, encoding and normalisation, tokenisation and offsets, display, and the tests that guard them.</p>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

  <div class="qw-index-row is-current">
    <span class="qw-index-num">§03</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/03-terminology/">Terminology</a>
      <p>One canonical name per concept, and a spelling derived by a documented function rather than chosen.</p>
      <span class="qw-index-links">
        <a href="/guidelines/en/03-terminology/standard/">standard</a>
        <a href="/guidelines/en/03-terminology/decisions/">decisions</a>
        <a href="/guidelines/en/03-terminology/dictionary/">dictionary</a>
        <a href="/guidelines/en/03-terminology/registries/">registries</a>
        <a href="https://github.com/quran-ws/guidelines/tree/main/skills/quranic-terminology">agent skill</a>
      </span>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">§04</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/04-versioning/">Versioning and corrections</a>
      <p>Semantic versioning for data and not only code, errata logs, and how users are told the text changed.</p>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">§05</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/05-open-source/">Open source and version control</a>
      <p>Licensing, repository layout, and the rules for commits, PRs and review.</p>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

  <div class="qw-index-row">
    <span class="qw-index-num">§06</span>
    <div class="qw-index-body">
      <a href="/guidelines/en/06-engineering/">Engineering</a>
      <p>API design, data modelling, mushaf rendering and fonts, and audio.</p>
    </div>
    <span class="qw-index-state status-draft">draft</span>
  </div>

</div>

:::caution[These are drafts]
Nothing here is adopted yet. Don't build against a page until it's marked `adopted`. These are opinions and judgement calls, not rulings or formal standards.
:::
