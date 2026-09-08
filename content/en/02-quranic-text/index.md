---
title: Handling Quranic text
description: Quranic text is transmitted source data, not content we edit. Practical rules for storage, tokenisation, display and testing.
status: draft
sidebar:
  order: 1
---

**The governing rule:** Quranic text is immutable source data. Store it, record its
identity, verify it, and build everything else — search, analysis, display — as
derived layers around it rather than as edits to it.

The reason is not technical. The Quran is the word of God, and He undertook its
preservation: ﴿إِنَّا نَحْنُ نَزَّلْنَا ٱلذِّكْرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ﴾ (15:9).
Honouring what He made sacred is itself an act of piety: ﴿وَمَن يُعَظِّمْ شَعَٰٓئِرَ
ٱللَّهِ فَإِنَّهَا مِن تَقْوَى ٱلْقُلُوبِ﴾ (22:32). A reader who opens your app is
reading the mushaf, so anything wrong on the screen is charged to the mushaf, not
to your code.

Every rule below is written to become a test or a constraint in code. The test
table is at the end, and `examples/` holds a schema, an API, data records and
tests that carry these rules in canonical names. The figures come from an audit
of a published Uthmani text; see [Source of the figures](#source-of-the-figures).

## 1. The source text

- Quranic text is transmitted, not authored. You are not its editor.
- Identify a text before you import it: edition, riwayah (the transmission the
  text follows, such as Hafs from Asim), ayah numbering system, version, and a
  hash of the file. `examples/data/mushaf_edition.json` is that record.
- Never edit the source in place. Any processing produces a new copy or a new layer.
- Keep the source reproducible from the published original. Your production database
  is not the only copy of it.
- Anything derivable is re-derived. Anything transmitted from the mushaf is stored
  as transmitted.
- Record where every fact came from. An import job must not drop provenance.

## 2. Encoding and characters

- Use one declared Unicode encoding end to end: source file, database, API,
  frontend.
- Don't assume that two strings that look alike are the same digitally; compare
  codepoints rather than shapes.
- Never swap one Quranic character for another that looks like it.
- Don't run generic cleanup on the text — `trim`, stripping "weird characters",
  collapsing whitespace — until you have proven it safe on this specific text.
- Never run `normalize` on the source, to `NFC`, `NFD`, `NFKC` or `NFKD`. Running
  `NFC` over a full mushaf changed **5,771 ayahs out of 6,236**, in two different ways:

```text
reorders:  ل + ّ (U+0651) + َ (U+064E)   →   ل + َ (U+064E) + ّ (U+0651)
composes:  ا (U+0627) + ٓ (U+0653)       →   آ (U+0622)   in ٱلضَّآلِّينَ (1:7)
```

- `NFKC` is worse: it substitutes a character with whatever Unicode treats as
  equivalent in use, and the original is gone:

```text
ﷲ  (U+FDF2)  →  الله
ﷺ  (U+FDFA)  →  صلى الله عليه وسلم
```

- Never strip vowels or other marks from the source. Generate a separate copy when
  search or analysis needs one.
- A string's length is not the number of visible letters. The audited text is
  **1,360,018 bytes** and **721,236 codepoints**, and it has fewer visible
  letters than either figure.
- Build an allowlist of the characters your text actually uses and fail the build on
  anything outside it. That entire text is built from 70 distinct characters — and
  ayah `1:1` still begins with a `U+FEFF` picked up during export, invisible on
  screen. `tools/audit_text.py` computes the allowlist, and every figure in this
  section, from any text file.

## 3. Rasm, marks and fonts

- Keep three things apart: the consonantal skeleton (rasm), the marks that vowel it
  (dabt), and the font that draws it. What you see is not the text.
- A glyph is not a character. Neither the font nor the shaping engine is a source of
  truth.
- A character with no glyph in the font either disappears or renders as a box, and
  the reader won't notice. Check your character set against the font's `cmap` before
  adopting it.
- Never inject display markup or HTML into the source.
- Edition marks are not part of an ayah: end of ayah ۝ (`U+06DD`), rubu al-hizb ۞
  (`U+06DE`), sajdah ۩ (`U+06E9`). In the audited text **199 ayahs** start with ۞
  and **15** contain ۩ inside the text field itself. Anyone building on that field
  counts these marks as words, searches them, and measures with them.

## 4. Tokenisation, identifiers and offsets

- Give surahs, ayahs and words stable identifiers. The text itself is never the key.
- Define your tokenisation explicitly. A programmatic word does not always match a
  word in the mushaf:

```text
يَٰٓأَيُّهَا   (2:21)   one whitespace token, two words linguistically
مَالِ هَٰذَا  (25:7)   two whitespace tokens, one word linguistically
```

- Splitting the audited text on whitespace yields **82,456** tokens — not the word
  count of the mushaf, and 199 of them are rubu al-hizb marks.
- Every offset carries three things: which text it was computed on, in which
  encoding, and in which unit.
- An ayah number alone is not a location. Bind it to its surah and its numbering
  system.
- Separate the ayah as text from its boundaries, its position and its number.

## 5. Riwayahs, editions and numbering systems

- Never mix data from different riwayahs or editions, however identical the text
  looks.
- Numbering systems are not interchangeable, and ayah boundaries do not line up
  across them.
- The basmalah is its own field: whether it counts as an ayah depends on the
  numbering system, and surah al-Tawbah has none.
- Test counts against the edition and numbering system you actually ship, not
  against remembered constants. 6,236 is the total of the Kufi numbering system
  (`kufi`), not a universal fact. Reference:
  `standards/terminology/registries/ayah_numbering.tsv`, one row per system with
  its total.

## 6. Derived layers

- Every derived layer — tajwid, word segmentation, morphology, translation, tafsir,
  coordinates, search indexes — stores the hash of the text it was derived from, so
  running it against a different copy is detectable.
- Tajwid, waqf, sajdah and colouring are annotations anchored to positions in the
  text, not edits to it — unless they were already part of the source edition.
- Model translations, tafsir and commentary as separate entities from the text.
- Every transformation is deterministic and rebuildable from the source.
- The search field (`search_key`) is derived: strip vowels and tatweel there, unify
  the forms of hamzah, alif, yaa and taa there. Never show it to the reader, never
  store it in place of the text.
- Don't put untested regex anywhere near this text.

## 7. Display

- Never trim the text to fit the layout. Change the layout.
- An ellipsis is never part of Quranic text.
- If you show a fragment, present it as a fragment, with its reference and a link.
  Never let it read as the complete ayah.
- When you must cut the string itself — `og:description`, a notification — cut on
  grapheme cluster boundaries with `Intl.Segmenter`. `slice` separates a letter from
  its marks.
- A word boundary is not a legitimate stopping place. Stopping at the end of (107:4)
  without (107:5) reverses the meaning.
- Never render an ayah that hasn't finished loading. Show a loading state or an
  error.
- Keep the text out of `placeholder`s, test fixtures, error logs, filenames and
  URLs. `114:1` is enough.

## 8. Errors, corrections and releases

- Never silently fix the source by hand. Raise the suspected error with the
  publisher, and document the correction.
- Distinguish a source error, a transmission error and a display error. Each is
  fixed in a different place.
- Make text changes reviewable character by character, not line by line.
- Treat any migration touching a text column as a high-risk change.
- A mushaf data update is never silent. A new version is a new dataset with a known
  origin and a known diff, announced in
  [Versioning and corrections](/guidelines/en/04-versioning/).
  `examples/data/errata.json` shows one erratum in that shape.
- When the text is not what you expected, fail loudly. Never auto-repair.
- Never guess at missing text or missing metadata.

## 9. Tests

A failing text test blocks the release. It never fixes the text.
`examples/tests/test_text_invariants.py` runs the rows below over a real record.

| What it tests | How |
| --- | --- |
| The text did not change | An expected `checksum` per approved release; the build fails when it moves |
| The whole text, not a sample | Every ayah of the full mushaf |
| Round-trip | read → store → retrieve returns the same characters |
| Every stage | Verify after the database, the API, the JSON layer and the frontend — the file alone proves nothing |
| No normalisation | A `lint` rule banning `normalize` in the text path |
| No foreign characters | Character set checked against the allowlist generated from the source |
| The text field holds text only | No digits, no Latin letters, no HTML, no edition marks (۝ ۞ ۩) |
| Counts | Surah and ayah counts per the shipped edition and numbering system |
| The database preserves marks | In MySQL, `SELECT 'مُحَمَّد' = 'محمد';` must return `0`; otherwise use `utf8mb4_bin` |
| Derived layers match their source | The source hash recorded in each layer matches the current source |
| Font coverage | `cmap` check plus a snapshot of an ayah with shaddah, a vowel and a small waqf mark |
| Truncation | Cut an ayah at every length and assert no letter is split from its marks |
| Every location is bound | Every text-bearing row and endpoint carries surah, ayah number and numbering system; a schema check, as in `examples/schema/` |
| Offsets name their text | Every stored offset records the text hash, the encoding and the unit; a missing one fails the build |
| No mixing of riwayahs or editions | A foreign key to the edition on every text table; a query across editions is a deliberate join, never a default |
| The basmalah is its own field | A schema check that the basmalah is not inside the first ayah's text field |
| No text where text does not belong | A lint over fixtures, logs, filenames and URLs for Quranic characters beyond a reference like `114:1` |
| A fragment reads as a fragment | A snapshot test that a cut string carries its reference and a marker, and never equals the full ayah |
| Text migrations are reviewed | CI flags any migration that touches a text column and requires a codepoint diff and a second reviewer |
| No auto-repair | An import fed corrupt input fails and changes nothing |

## Source of the figures

The figures in sections 2–4 — 5,771 of 6,236 ayahs changed by `NFC`; 1,360,018
bytes; 721,236 codepoints; 70 distinct characters; `U+FEFF` at 1:1; 199 ayahs
starting with ۞; 15 containing ۩; 82,456 whitespace tokens — come from one audit
of a published Uthmani text in the riwayah of Hafs from Asim with Kufi numbering,
run for this guide. The audited file is not in this repository.
`python3 tools/audit_text.py <file> --format tanzil` recomputes every one of
these figures from a text file, so the page is checked against the file rather
than remembered.

**To fill in (maintainer):** the audited file's edition or name, source URL,
version, SHA-256 and retrieval date, followed by a rerun of `tools/audit_text.py`
to confirm the figures above. Until then they stand as first measured.
