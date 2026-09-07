// Cut an ayah at every length on grapheme cluster boundaries, and assert no
// letter is separated from its marks. `slice` cannot do this; Intl.Segmenter can.
//
//     node examples/tests/truncation.js
//
// Exits non-zero on the first bad cut.

const fs = require('node:fs');
const path = require('node:path');

const record = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'ayah.json'), 'utf8'));
const text = record.text;

const segmenter = new Intl.Segmenter('ar', { granularity: 'grapheme' });
const graphemes = Array.from(segmenter.segment(text), s => s.segment);

// A combining mark (harakah, shaddah, sukun, small letters…) is any code point
// in the Arabic block with general category Mn. Intl has no category lookup;
// the ranges below are the Arabic combining marks.
const isMark = ch => /[ؐ-ًؚ-ٰٟۖ-ۜ۟-۪ۤۧۨ-ۭ]/u.test(ch);

let bad = 0;

// 1. The naive cut is unsafe: somewhere `slice` orphans a mark.
const naiveBad = [];
for (let i = 1; i < text.length; i++) if (isMark(text[i])) naiveBad.push(i);
if (naiveBad.length === 0) { console.error('expected slice to be unsafe on a vocalised text'); bad++; }

// 2. The grapheme cut is safe at every length.
for (let n = 1; n < graphemes.length; n++) {
  const head = graphemes.slice(0, n).join('');
  const tail = graphemes.slice(n).join('');
  if (isMark(tail[0])) { console.error(`cut after ${n} graphemes orphans a mark`); bad++; }
  if (head + tail !== text) { console.error(`cut after ${n} graphemes lost characters`); bad++; }
}

// 3. No cut produces a string that reads as the whole ayah: a fragment is a fragment.
const cutMarker = '…';
for (let n = 1; n < graphemes.length; n++) {
  const shown = graphemes.slice(0, n).join('') + cutMarker;
  if (shown === text) { console.error('a fragment must never equal the full ayah'); bad++; }
}

if (bad) { console.error(`${bad} problems`); process.exit(1); }
console.log(`ok — ${graphemes.length} graphemes, ${text.length} code units; slice would break at ${naiveBad.length} positions, the grapheme cut at none`);
