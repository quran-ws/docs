-- A mushaf follows a riwayah, not a person.
--
-- The case: `mushafs.rawi_id` pointed at a table of transmitters, so "all
-- mushafs in Warsh" meant "all mushafs by the man Warsh", and the two stop
-- agreeing the moment a second riwayah of the same rawi is loaded
-- (surveys/quranpedia-net.md, section 2.1). Three concepts were in one table:
--
--   rawi      the transmitter        a person
--   riwayah   what he transmitted    a text tradition, keyed to a qiraah
--   tariq     the route to him       a chain below the riwayah
--
-- The migration separates them, moves the foreign key, and leaves a view under
-- the old column's meaning for one deprecation window so nothing breaks the
-- day it runs. The data in a production text database cannot be rebuilt, so
-- every step is additive until the last, and the last is its own release.
--
-- MySQL 8 syntax.

-- 1. The concepts the old table collapsed. Members come from the qiraat registry.
CREATE TABLE qiraahs (
  qiraah_id  INTEGER     NOT NULL AUTO_INCREMENT PRIMARY KEY,
  code       VARCHAR(64) NOT NULL UNIQUE                      -- registry member: asim
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE riwayahs (
  riwayah_id INTEGER     NOT NULL AUTO_INCREMENT PRIMARY KEY,
  code       VARCHAR(64) NOT NULL UNIQUE,                     -- registry member: hafs_an_asim
  qiraah_id  INTEGER     NOT NULL,
  rawi_id    INTEGER     NOT NULL,                            -- the person, still a row in rawis
  CONSTRAINT fk_riwayahs_qiraah FOREIGN KEY (qiraah_id) REFERENCES qiraahs (qiraah_id),
  CONSTRAINT fk_riwayahs_rawi   FOREIGN KEY (rawi_id)   REFERENCES rawis (rawi_id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

-- 2. Backfill: every rawi row that was really naming a riwayah becomes one.
--    The old rows carried the riwayah name in `translated_name`; the mapping
--    to registry codes is reviewed by hand before this runs, never guessed.
INSERT INTO qiraahs (code) VALUES ('asim'), ('nafi');
INSERT INTO riwayahs (code, qiraah_id, rawi_id)
SELECT 'hafs_an_asim', q.qiraah_id, r.rawi_id FROM rawis r JOIN qiraahs q ON q.code = 'asim' WHERE r.code = 'hafs';
INSERT INTO riwayahs (code, qiraah_id, rawi_id)
SELECT 'warsh_an_nafi', q.qiraah_id, r.rawi_id FROM rawis r JOIN qiraahs q ON q.code = 'nafi' WHERE r.code = 'warsh';

-- 3. The new foreign key, filled from the old one. Both exist for the window.
ALTER TABLE mushafs ADD COLUMN riwayah_id INTEGER NULL AFTER rawi_id;
UPDATE mushafs m JOIN riwayahs w ON w.rawi_id = m.rawi_id SET m.riwayah_id = w.riwayah_id;
ALTER TABLE mushafs MODIFY COLUMN riwayah_id INTEGER NOT NULL,
  ADD CONSTRAINT fk_mushafs_riwayah FOREIGN KEY (riwayah_id) REFERENCES riwayahs (riwayah_id);

ALTER TABLE recitations ADD COLUMN riwayah_id INTEGER NULL AFTER rawi_id;
UPDATE recitations c JOIN riwayahs w ON w.rawi_id = c.rawi_id SET c.riwayah_id = w.riwayah_id;
ALTER TABLE recitations MODIFY COLUMN riwayah_id INTEGER NOT NULL,
  ADD CONSTRAINT fk_recitations_riwayah FOREIGN KEY (riwayah_id) REFERENCES riwayahs (riwayah_id);

-- 4. The deprecation window: readers of the old column get it through a view,
--    and the column itself is marked. Removed in the next major release.
CREATE VIEW mushafs_deprecated_rawi AS
SELECT m.mushaf_id, w.rawi_id
FROM mushafs m JOIN riwayahs w ON w.riwayah_id = m.riwayah_id;

ALTER TABLE mushafs     MODIFY COLUMN rawi_id INTEGER NULL COMMENT 'deprecated: use riwayah_id; removed in 3.0.0';
ALTER TABLE recitations MODIFY COLUMN rawi_id INTEGER NULL COMMENT 'deprecated: use riwayah_id; removed in 3.0.0';

-- 5. In release 3.0.0, a separate migration:
--    ALTER TABLE mushafs DROP COLUMN rawi_id;
--    ALTER TABLE recitations DROP COLUMN rawi_id;
--    DROP VIEW mushafs_deprecated_rawi;
