# Examples

Concrete files in canonical names, for copying: a database schema, an API, data records, a migration and tests. Every file here is checked on each build by `tools/check_example_files.py`, so what it shows is what the standard says today.

| File | What it shows |
| --- | --- |
| `schema/quran_text.sql` | The core tables — `mushaf_editions`, `surahs`, `ayahs`, `words` — keyed by the standard's textual `ayah_key` and `word_key`, with the numbering system and the riwayah as columns, and a binary collation on the text. |
| `schema/quran_text.prisma` | The same model for an ORM. |
| `api/ayah.openapi.yml` | One endpoint: an ayah by location, with the numbering system and riwayah explicit and the source hash in the response. |
| `data/mushaf_edition.json` | The dataset manifest the versioning page defines: `dataset`, `mushaf_edition`, `riwayah`, `ayah_numbering_system`, `version`, `source_hash`, `derived_from`, `license`, `errata`, `released`. |
| `data/ayah.json` | One ayah record, text exactly as transmitted, basmalah in its own field, words segmented. |
| `data/errata.json` | One erratum in the shape the versioning page defines: `id`, `location`, `offset`, `before`/`after` as codepoints, `kind`, `confirmed_by`, `confirmed_on`, `fixed_in`. |
| `migrations/0001_rawi_to_riwayah.sql` | A rename the standard requires — a mushaf follows a riwayah, not a person — done with a deprecation view. |
| `tests/test_text_invariants.py` | The text page's test table as runnable assertions over `data/ayah.json`. |
| `tests/truncation.js` | Cutting an ayah at every length on grapheme boundaries, and asserting no letter is split from its marks. |

What the check enforces:

1. Every domain name in these files resolves to a dictionary entry **and is that entry's canonical `code` or plural** — an alias such as `sura` or `verse` fails here, unlike in prose. Generic words (`id`, `text`, `version`, `hash`) are allowed by name in the checker.
2. Every value of a classification field is a member of its registry, written as its member code.
3. The text in `data/ayah.json` holds no edition marks, no BOM, no digits, no Latin, no HTML, and matches its recorded hash.
4. The tests run and pass.
5. Every `examples/…` path mentioned in a page or a README exists.

The ayah in `data/ayah.json` is 112:1 in the riwayah of Hafs from Asim, copied from the Tanzil Uthmani text as served by `api.alquran.cloud` (edition `quran-uthmani`, retrieved 2026-09-06). The API returns the basmalah joined to the first ayah of the surah; the record stores the ayah without it and the basmalah in its own field, as the text page requires.
