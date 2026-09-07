-- The core tables for storing Quranic text, in canonical names.
--
-- Rules this schema carries (see content/en/02-quranic-text/):
--   * The text is transmitted source data. Nothing here edits it; every derived
--     form (search_key) lives in its own column and names the hash it came from.
--   * Every text-bearing row knows its mushaf edition, its riwayah and its ayah
--     numbering system. An ayah number alone is not a location, and the keys
--     are the standard's textual ayah_key (`112:1`) and word_key (`112:1:3`).
--   * The basmalah is its own field, not part of the first ayah.
--   * Text columns use a binary collation, so 'مُحَمَّد' <> 'محمد'.
--
-- MySQL 8 syntax. Table names are the canonical plural; columns that point at
-- another table are <canonical>_id.

CREATE TABLE mushaf_editions (
  mushaf_edition_id      INTEGER      NOT NULL AUTO_INCREMENT PRIMARY KEY,
  code                   VARCHAR(64)  NOT NULL UNIQUE,      -- e.g. tanzil_uthmani
  name                   VARCHAR(255) NOT NULL,
  publisher              VARCHAR(255) NOT NULL,
  riwayah                VARCHAR(64)  NOT NULL,             -- registry member: hafs_an_asim
  ayah_numbering_system  VARCHAR(64)  NOT NULL,             -- registry member: kufi
  version                VARCHAR(64)  NOT NULL,
  text_hash              CHAR(64)     NOT NULL,             -- sha256 of the published file
  retrieved              DATE         NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE surahs (
  surah_number               INTEGER      NOT NULL PRIMARY KEY,  -- the established order, 1..114
  code                       VARCHAR(64)  NOT NULL UNIQUE,       -- registry member: fatihah
  revelation_classification  VARCHAR(16)  NOT NULL,              -- makki | madani | disputed
  revelation_order           INTEGER      NULL,
  ayah_count                 INTEGER      NOT NULL               -- per the edition's numbering system
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE ayahs (
  ayah_key               VARCHAR(16)  NOT NULL,             -- textual key `112:1`, read in the light of the numbering system
  mushaf_edition_id      INTEGER      NOT NULL,
  surah_number           INTEGER      NOT NULL,
  ayah_number            INTEGER      NOT NULL,
  ayah_numbering_system  VARCHAR(64)  NOT NULL,             -- repeated here so a row is a location on its own
  text                   TEXT         NOT NULL,             -- exactly as transmitted, never normalised
  text_hash              CHAR(64)     NOT NULL,             -- sha256 of `text`
  basmalah_present       BOOLEAN      NOT NULL DEFAULT FALSE,
  basmalah_text          TEXT         NULL,                 -- its own field; whether it counts is the numbering system's call
  search_key             TEXT         NULL,                 -- derived: no dabt, no tatweel, unified hamzah/alif/yaa/taa forms
  search_key_source_hash CHAR(64)     NULL,                 -- the text_hash the search_key was derived from
  CONSTRAINT fk_ayahs_mushaf_edition FOREIGN KEY (mushaf_edition_id) REFERENCES mushaf_editions (mushaf_edition_id),
  CONSTRAINT fk_ayahs_surah          FOREIGN KEY (surah_number)      REFERENCES surahs (surah_number),
  CONSTRAINT pk_ayahs PRIMARY KEY (mushaf_edition_id, ayah_numbering_system, ayah_key),
  CONSTRAINT uq_ayahs_location UNIQUE (mushaf_edition_id, surah_number, ayah_number, ayah_numbering_system)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE words (
  word_key               VARCHAR(24)  NOT NULL,             -- textual key `112:1:3`: the ayah key plus the position
  mushaf_edition_id      INTEGER      NOT NULL,
  ayah_numbering_system  VARCHAR(64)  NOT NULL,
  ayah_key               VARCHAR(16)  NOT NULL,
  word_position          INTEGER      NOT NULL,             -- 1-based, under the declared tokenization
  tokenization           VARCHAR(32)  NOT NULL,             -- e.g. whitespace; a different method is a different row set
  text                   TEXT         NOT NULL,
  CONSTRAINT pk_words PRIMARY KEY (mushaf_edition_id, ayah_numbering_system, tokenization, word_key),
  CONSTRAINT fk_words_ayah FOREIGN KEY (mushaf_edition_id, ayah_numbering_system, ayah_key)
    REFERENCES ayahs (mushaf_edition_id, ayah_numbering_system, ayah_key),
  CONSTRAINT uq_words_position UNIQUE (mushaf_edition_id, ayah_numbering_system, ayah_key, tokenization, word_position)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

-- The collation test from the text page. This must return 0.
-- SELECT 'مُحَمَّد' = 'محمد';
