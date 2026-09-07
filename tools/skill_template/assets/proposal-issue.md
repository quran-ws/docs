## Proposal checklist for `{{CODE}}`

Section 30 of the standard: a term is accepted when these are answered, and
not adopted until the need is clear. Copy this into the pull request or issue
and answer each line in a sentence; "yes" is not an answer.

**First, is the concept ours to name?** It belongs in this standard only when
it cannot be defined without referring to the Quran or the mushaf. A book, a
tag, a user, a stream, a fatwa, a hadith are real and are not ours.

- [ ] 1. What is the concept?
- [ ] 2. What is its definition? (what it is — no implementation detail, no circularity)
- [ ] 3. Why does software need to model it? (not a restatement of the definition)
- [ ] 4. What are its boundaries, and what might it be confused with?
- [ ] 5. What is its `kind`?
- [ ] 6. Which `category` does it belong to?
- [ ] 7. Does it have a `parent`? (is-a only; containment is `part_of`)
- [ ] 8. Is it a Quranic concept or a general technical one? (`origin`)
- [ ] 9. What is the most suitable canonical name, and does it say what the concept is?
- [ ] 10. If it is Arabic in origin, does the name follow the Canonical Code Spelling? (`scripts/spell.py` says so)
- [ ] 11. What are its singular and plural in code? (the code plus `s`)
- [ ] 12. What are its alternative spellings? (every one seen in the wild)
- [ ] 13. What are its translations or English glosses?
- [ ] 14. Are there deprecated names?
- [ ] 15. Does the name work naturally in code, in an API and in a database? (write the column, the field and the class)
- [ ] 16. What source establishes the concept's definition?

Before sending: `scripts/lookup.py --search` found no entry for it under any
spelling; the Arabic `definition` and `purpose` are written or marked TODO for
a maintainer; `status` is `draft`.
