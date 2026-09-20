<a id="reading-entries"></a>

## Reading an entry

Start with the [lookup table](#dictionary-lookup) to find a name or meaning. Each entry brings together a concept's definition, purpose and names. The [naming standard](../standard/) explains how those names are chosen.

For example, the hamzah entry records these forms together:

```yaml
names:
  code: hamzah
  display: Hamzah
  arabic:
    vocalized: الهَمْزَة
    singular: الهمزة
  dabt: الهَمْزَة — رَأْس العَيْن
  by_shape: رَأْس عَيْن
  mushaf_introduction: null
  unicode: ARABIC LETTER HAMZA
alternative_spellings:
  - hamza
```

### Naming fields

These fields are inside `names`, except for top-level `alternative_spellings`. Not every field applies to every concept.

| Field | Contents |
| --- | --- |
| `code` | The stable identifier for code, APIs and databases. |
| `display` | The English name readers see in interfaces and documentation. |
| `display_evidence` | Evidence for the display choice, completed before adoption. |
| `transliteration` | Optional scholarly rendering, such as ALA-LC or DIN 31635. |
| `arabic.vocalized` | Vocalised Arabic for derivation and Arabic display. |
| `arabic.singular` and `arabic.plural` | Unvocalised singular and plural for linguistic information and search. |
| `dabt` | The name in the science of mushaf marks, as the source gives it. |
| `by_shape` | The source's description of the mark's shape. |
| `mushaf_introduction` | The name in the mushaf introduction; `null` means the introduction does not name it, not that the entry is incomplete. |
| `unicode` | The official character name, separate from the code identifier. |
| `alternative_spellings` | Other spellings of the same name for search. |

### Meaning and relationships

`definition` explains what the concept is; `purpose` explains why software models it. `boundaries` identifies exclusions where confusion is possible, while `related` points to neighbouring concepts.

`kind` identifies the entry's form: `entity`, `concept`, `classification`, `classification_value`, `property`, `role`, `process`, `content`, `analysis`, `mark` or `unit`. `category` identifies the domain under which the entry appears on this page. Every entry has one kind and one category; `process` is reserved and ordinary operation names do not use it.

`parent` names what the concept is a type of, such as `makki` under `revelation_classification`. `part_of` names what it belongs within, such as `rubu_al_hizb` within `hizb`. A mark with a family records that family in `parent`, while `mark_family` preserves the source's grouping; the groupings may differ.

The entry identifier `concept` is the target of dictionary references. It may differ from `names.code`: `ayah_numbering_makki` has the code value `makki`, which also occurs in another classification. Use the value within its classification's context.

`english_glosses` holds English equivalents for search; `deprecated` holds former names. `Verse` is not an alternative spelling of `ayah`, and a deprecated name is not the recommended name for a new project.

### Concepts and registry members

A concept needs a definition, purpose and boundaries. A member of a closed set gets a row in the [registries](../registries/) recording its name, position and source. `makki` is a value with a meaning; Hafs is a named registry member. `registry` identifies the concept's member registry. A row's `verified` states what was checked against a source; `no` is an allowed value.

A member and concept may share a name: `hamzah` for the mark and `qiraah:hamzah` for the reciter. A bare name resolves to the concept; members are looked up within their kind's namespace. Letter names live in the spelling table because derivation reads them directly; see the naming standard's letter-name rules.

Tajwid rulings as concepts have entries; engine application cases have registry rows; occurrences in the text are spans labelled with the ruling's name. These describe different levels of information.

### Origin and status

`origin` records `quranic` for a specialised term, `borrowed` for a general borrowed concept, or `standard` for a modelling concept defined by the standard. `tier` records `core` for concepts applications store today or `extended` for those rarely represented or with varying boundaries.

`status` records the review stage: `draft`, `proposed`, `adopted`, or `deprecated` for a withdrawn entry retained for reference. `sources` supports the concept's meaning; choosing its code spelling is a standard convention. `note` records entry notes and name changes.

To add or correct an entry, follow [Contributing to the dictionary](#contributing).

<a id="contributing"></a>

## Contributing to the dictionary

Search the [dictionary](#reading-entries) first, then propose the change with a real project case that explains the need. The [naming standard](../standard/) explains naming choices; the dictionary guide explains the fields. This page is for entry authors and reviewers.

### Propose the change

Open an [issue](https://github.com/quran-ws/docs/issues/new/choose) for a new term or a rule change. Describe the project, location and problem, and discuss the change before sending a PR. A typo correction can go directly to a PR. The [repository instructions](https://github.com/quran-ws/docs/blob/main/CONTRIBUTING.md) explain setup and checks.

### Check scope and need

A concept belongs here if it cannot be defined without reference to the Quran or mushaf and has a clear software purpose. For example, `ayah_timing` belongs; `user` and `subscription` are general concepts. Search meanings and spellings before creating an entry: the proposal may be another name for an existing concept.

Projects can keep local concepts in a separate directory using the same structure, `origin: standard`, their own categories, and the same tools. Do not redefine a dictionary concept or reuse its name for another meaning. Propose an in-scope local concept here for inclusion after acceptance.

### Choose an entry or a registry row

Create an entry for something needing a definition, purpose and boundaries, such as the classification value `makki`. Put a named member identified by its name, position and source, such as a reciter or surah, in its group's registry. Every meaningful classification value has an entry even when software represents it as an `enum`; a classification must have values.

Registry rows cite sources and use `verified` to state what was checked; `no` is acceptable when verification is incomplete. Letter names belong in the spelling table. Mark entries and the registry of engine rulings have generated sources identified in the repository instructions; edit the source, not the output.

### Write the definition, purpose and boundaries

`definition` answers “What is this concept?” Write a precise, concise definition without circular wording or implementation details. “An ayah is a Quranic ayah” defines nothing.

`purpose` answers “Why does software model this?” Explain what software stores, connects or distinguishes. Do not repeat the definition: linking tafsir and recitation to a location in the text explains an ayah's software purpose.

Where confusion is plausible, state exclusions in `boundaries` and name neighbouring concepts in `related`. Explain whether a column stores a word in the text or a token produced by segmentation; “differs from `word`” is insufficient.

These require human review. Passing automated checks does not establish a good definition or a need for an entry.

### Complete the entry

Each concept has a YAML file in `standards/terminology/concepts/` whose filename matches `concept`. The [schema](https://github.com/quran-ws/docs/blob/main/standards/terminology/schema.json) defines fields and allowed values; the [entry guide](#reading-entries) explains their meaning.

The basic fields are `concept`, `kind`, `category`, `origin`, `tier`, `status`, `names.code`, `names.display`, and both languages of the definition and purpose: `definition`, `definition_en`, `purpose`, `purpose_en`.

- Choose one `kind` from the closed list and one existing `category`. Do not mix shape and domain in a kind such as `textual_concept`, or add an empty category.
- Supply `parent` for classification values and marks with a family. Use `part_of` for containment, referring to an entity. Relationships must reference existing entries.
- Supply `plural` when the concept is used as a collection: the complete code name plus `s`, including compound names.
- Vocalised Arabic is required for `origin: quranic`. For a borrowed concept, record an established Arabic name when one exists without inventing one.
- `symbol`, `unicode` and `mark_family` belong to marks and drawn `waqf_mark_type` values. The `unicode` block is generated from Unicode data, never edited by hand.
- Keep `alternative_spellings`, `english_glosses` and `deprecated` separate. A name for a different concept is not an alias; explain the confusion in `boundaries`.

### Cite suitable evidence

Sources establish a concept's meaning and definition; the standard chooses its code name. Register sources in `standards/terminology/sources.yml`, then cite their IDs and locations, such as a page or term number, in `sources`. Registry rows use the same source catalogue.

Entries start as `draft`, become `proposed` after discussion and `adopted` after approval. Adoption requires a source for the definition and display-name evidence in `names.display_evidence`. Drafts may carry a display name before its evidence is complete.

### Keep both languages aligned

An entry has Arabic and English text. `definition_en`, `purpose_en`, `boundaries_en` and `note_en` translate the Arabic fields without adding or removing conditions. Translate boundaries line by line.

Use canonical terms such as `ayah` in English prose and put identifiers in backticks. Translate repeated Arabic wording consistently. Leave Arabic in English fields only when discussing that name, enclosed in «…». This explains a concept in another language; it is not an authorised translation of scripture.

### Preserve old names

When renaming or merging entries for the same concept, put the former name in `deprecated` on the surviving entry. Record the date and reason in `note` with a decision-record link. Deprecated names remain in that field; `aliases.json` indexes alternative spellings.

When withdrawing an entire entry, retain it with `status: deprecated` so its name is never reused for another meaning. An incorrect name for a different concept is not a former name for this one.

### Before sending

- The real case, purpose, boundaries and sources are explained.
- Names follow the standard and relationships resolve to existing entries.
- Both languages agree and the entry status reflects its review.
- Former names, dates and reasons are preserved where needed.
- The build and tests pass, and generated files are included in the PR.

```bash
python3 tools/build.py
python3 -m pytest -q
```

See the [maintenance guide](https://github.com/quran-ws/docs/blob/main/tools/README.md) for generation, versioning and checks.
