---
title: Quranic text
description: The text is transmitted source data, never edited. The rules for storing, encoding, tokenising, displaying and testing it.
status: proposed
generated: content/pages/quranic-text.yml
sidebar:
  order: 2
---

**The governing rule:** Quranic text is immutable source data. Store it,
record its identity, verify it, and build everything else as derived layers
around it, never as edits to it.

The reason is not technical. The Quran is the word of God, and He undertook
its preservation: ﴿إِنَّا نَحۡنُ نَزَّلۡنَا ٱلذِّكۡرَ وَإِنَّا لَهُۥ لَحَٰفِظُونَ﴾
(15:9). A reader who opens your app is reading the mushaf, so anything wrong
on the screen is charged to the mushaf, not to your code.

The figures on this page come from one audit of a published Uthmani text in
the riwayah of Hafs from Asim with Kufi numbering. `tools/audit_text.py`
recomputes every one of them from any text file. `examples/` holds a schema,
an API, data records and tests that carry these rules in canonical names.

## 1. The source

The text is transmitted, not authored. You are not its editor.

**1.1** Identify a text before you import it: edition, riwayah, ayah numbering system, version, and a hash of the file.

`examples/data/mushaf_edition.json` is that record.

*Checked by:* A schema check that every text-bearing table carries a foreign key to the edition it was built from (`examples/schema/`).

**1.2** Never edit the source in place; any processing produces a new copy or a new layer, and the source stays reproducible from the published original.

*Checked by:* An expected checksum per approved release, and a build that fails when it moves.

**1.3** Anything derivable is re-derived, and anything transmitted from the mushaf is stored as transmitted, with where it came from.

*Checked by:* Every derived layer records the hash of the text it was built from, and a build step compares it with the current source.

**1.4** Never type Quranic text by hand, in code, prose, tests or documentation; quote it by reference, or copy it from a released dataset and name the release.

Placeholder Arabic reads as Quran to whoever sees it, and a typed ayah carries no identity to verify against.

*Checked by:* The lint of rule 7.5, run over source files and documentation as well; and review.

## 2. Encoding and characters

Compare codepoints, never shapes, and never let a library "clean" the text.

**2.1** Use one declared Unicode encoding end to end, in the source file, the database, the API and the frontend.

*Checked by:* A round-trip test that reading, storing and retrieving returns the same codepoints at every stage.

**2.2** Never run `normalize` on the source, to `NFC`, `NFD`, `NFKC` or `NFKD`.

Running `NFC` over a full mushaf changed **5,771 ayahs out of 6,236**, in two ways:

```text
reorders:  ل + ّ (U+0651) + َ (U+064E)   →   ل + َ (U+064E) + ّ (U+0651)
composes:  ا (U+0627) + ٓ (U+0653)       →   آ (U+0622)   in ٱلضَّآلِّينَ (1:7)
```

`NFKC` is worse, because it replaces a character with what Unicode treats as equivalent and the original is gone:

```text
ﷲ  (U+FDF2)  →  الله
ﷺ  (U+FDFA)  →  صلى الله عليه وسلم
```

*Checked by:* A lint rule that bans `normalize` in the text path, from file to reader.

**2.3** Don't trim, strip "weird characters", collapse whitespace, swap look-alike characters or remove marks from the source; generate a separate copy when search needs one.

*Checked by:* The checksum test, and a test that the text field holds no digits, Latin letters or HTML.

**2.4** Build an allowlist of the characters your text uses and fail the build on anything outside it.

The audited text is built from 70 distinct characters, and ayah `1:1` still began with a `U+FEFF` picked up during export, invisible on screen.

```bash
python3 tools/audit_text.py <file> --format tanzil    # computes the allowlist and every figure on this page
```

*Checked by:* The allowlist, enforced at ingestion; a character outside it fails the import.

**2.5** A string's length is not the number of visible letters, so never size, cut or count by it.

The audited text is **1,360,018 bytes** and **721,236 codepoints**, and has fewer visible letters than either.

*Checked by:* A truncation test that cuts an ayah at every length and asserts no letter is split from its marks.

## 3. Rasm, marks and fonts

The skeleton, the marks and the font are three layers, and only the first two are the text.

**3.1** Keep the consonantal skeleton (rasm), the marks that vowel it (dabt) and the font that draws it apart; what you see is not the text.

*Checked by:* A schema in which a font, a layout and a glyph-coded text are separate datasets keyed to the edition.

**3.2** A glyph is not a character, and neither the font nor the shaping engine is a source of truth.

*Checked by:* The codepoint round-trip test.

**3.3** Check your character set against the font's `cmap` before adopting it, because a character with no glyph disappears or renders as a box and the reader won't notice.

*Checked by:* A `cmap` coverage test per font release, and a snapshot of an ayah with a shaddah, a vowel and a small waqf mark.

**3.4** Edition marks are not part of an ayah: end of ayah ۝ (`U+06DD`), rubu al-hizb ۞ (`U+06DE`), sajdah ۩ (`U+06E9`).

In the audited text **199 ayahs** start with ۞ and **15** contain ۩ inside the text field. Anyone building on that field counts them as words and searches them.

*Checked by:* A test that the text field holds no edition mark.

**3.5** Never inject display markup or HTML into the source.

*Checked by:* The text-only test on the text field.

## 4. Locations, tokens and offsets

The text is never the key.

**4.1** Give surahs, ayahs and words stable identifiers; the text itself is never the key.

*Checked by:* A schema check that every text-bearing row has an identifier that is not derived from the text.

**4.2** An ayah number alone is not a location; bind it to its surah and its numbering system.

*Checked by:* A schema check that every text-bearing row and endpoint carries the surah, the ayah number and the numbering system (`examples/schema/`).

**4.3** Define your tokenisation explicitly, because a programmatic word does not always match a word in the mushaf.

```text
يَٰٓأَيُّهَا   (2:21)   one whitespace token, two words linguistically
مَالِ هَٰذَا  (25:7)   two whitespace tokens, one word linguistically
```

Splitting the audited text on whitespace yields **82,456** tokens, which is not the word count of the mushaf, and 199 of them are rubu al-hizb marks.

*Checked by:* The tokenisation is versioned with the dataset, and a golden test holds the token count of each release.

**4.4** Every offset carries three things: which text it was computed on, in which encoding, and in which unit.

*Checked by:* A schema check on every stored offset; a missing field fails the build.

## 5. Riwayahs, editions and numbering systems

However alike two texts look, they are not interchangeable.

**5.1** Never mix data from different riwayahs or editions, however identical the text looks.

*Checked by:* A foreign key to the edition on every text table; a query across editions is a deliberate join, never a default.

**5.2** Numbering systems are not interchangeable, and ayah boundaries do not line up across them.

6,236 is the total of the Kufi system (`kufi`), not a universal fact. `standards/terminology/registries/ayah_numbering.tsv` has one row per system with its total.

*Checked by:* Surah and ayah counts tested against the edition and numbering system you ship, never against remembered constants.

**5.3** The basmalah is its own field, because whether it counts as an ayah depends on the numbering system, and surah al-Tawbah has none.

*Checked by:* A schema check that the basmalah is not inside the first ayah's text field.

## 6. Derived layers

Everything built on the text names the text it was built on.

**6.1** Every derived layer, from tajwid and segmentation to translation, tafsir and search indexes, stores the hash of the text it was derived from.

*Checked by:* A build step that compares each layer's recorded hash with the current source.

**6.2** Tajwid, waqf, sajdah and colouring are annotations anchored to positions in the text, not edits to it, unless they were part of the source edition.

*Checked by:* The checksum test on the text field, which an annotation must not move.

**6.3** The search field is derived, by a deterministic function that strips vowels and tatweel and unifies letter forms; never show it to the reader and never store it in place of the text.

*Checked by:* Golden cases for the derivation, and a test that the index was built by the current function version.

**6.4** Don't put an untested regular expression anywhere near this text.

*Checked by:* The checksum and round-trip tests, run after every transformation.

## 7. Display

Change the layout, never the text.

**7.1** Never trim the text to fit the layout, and never let an ellipsis stand in Quranic text.

*Checked by:* A snapshot test that a rendered ayah equals the stored text.

**7.2** A fragment is presented as a fragment, with its reference and a link, and never reads as the complete ayah.

Stopping at the end of (107:4) without (107:5) reverses the meaning. A word boundary is not a legitimate stopping place.

*Checked by:* A snapshot test that a cut string carries its reference and a marker, and never equals the full ayah.

**7.3** When you must cut the string itself, for a notification or an `og:description`, cut on grapheme cluster boundaries with `Intl.Segmenter`, never with `slice`.

`examples/tests/truncation.js` cuts an ayah at every length and asserts no letter is separated from its marks.

*Checked by:* The truncation test.

**7.4** Never render an ayah that hasn't finished loading; show a loading state or an error.

*Checked by:* A component test with a delayed and a failed fetch.

**7.5** Keep the text out of placeholders, fixtures, error logs, filenames and URLs; a reference like `114:1` is enough.

*Checked by:* A lint over fixtures, logs, filenames and URLs for Quranic characters.

## 8. Errors and corrections

Fail loudly, fix nothing by hand, and write every correction down.

**8.1** Never silently fix the source by hand; raise the suspected error with the publisher and document the correction.

`examples/data/errata.json` shows one erratum in the shape the [versioning page](/guidelines/en/versioning/) defines.

*Checked by:* The errata log, and a review rule that a text diff with no erratum is rejected.

**8.2** Distinguish a source error, a transmission error and a display error, because each is fixed in a different place.

*Checked by:* The `kind` field of every erratum, which takes one of the three values.

**8.3** Make text changes reviewable character by character, and treat any migration that touches a text column as a high-risk change.

*Checked by:* CI flags a migration on a text column and requires a codepoint diff and a second reviewer.

**8.4** When the text is not what you expected, fail loudly; never auto-repair and never guess at missing text or metadata.

*Checked by:* An import fed corrupt input fails and changes nothing.

**8.5** A mushaf data update is never silent; a new version is a new dataset with a known origin and a known diff, announced to the reader.

*Checked by:* The release tests on the [versioning page](/guidelines/en/versioning/).
