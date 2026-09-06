# Open items from the surveys

What the surveys raised that the standard has not yet settled. Each item names the survey section it came from. An item leaves this list when it becomes an entry, a decision, or a recorded refusal.

## Undecided

- **`nahw` and `irab`** (quranpedia §5.2): one concept or two? quranpedia serves both. Until this is answered the treebank layer — `syntax`, `constituent`, `syntactic_relation` — has no name, and one of the two entries would be a duplicate (§6.3).
- **The three forms of one text** (quranpedia §3.6): `text`, `clean_text` (the normalised copy for search) and `coded_text` (glyph codes for one font). The text page names the first as the source and the second as `search_key`; the dictionary names neither result. The evidence is one application, which the survey judged not enough to name a concept.
- **`language`** (quranpedia §3.8): declined as out of scope, but `translation` needs it and no rule says how a project names it.
- **`quran_qa`** (quranpedia §5.4): a distinct content concept, or a fatwa under another name? The data has separate sources, so probably distinct; not decided.
- **A migration path** (quranpedia §5.5): the standard binds names in code, and every finding in §2 is a rename in a production database whose data cannot be rebuilt. `aliases.json` is most of the machinery for a mapping; a deprecation window and a rule for views or aliases are not written.
- **Sources for the entries the survey produced** (quranpedia §6.2): the 29 entries added on 2026-09-06 are `status: draft`. The standard keeps an entry out of `adopted` until a source establishes its definition.

## Answered since the survey

- *Are the ten qiraat and their rawis concepts or data?* (§5.1) — Data: they are rows in `standards/terminology/registries/qiraat.tsv`, and a concept with a closed set of members names its registry instead of giving each member an entry.
- *Where does the boundary of the standard fall?* (§5.3) — A concept belongs when it cannot be defined without referring to the Quran or the mushaf. It heads the standard's "rule for accepting a new term", and the decision record argues it.
- *Five new domains* (§4) — Rejected. See the decision *The standard names the Quran's sciences and stops there*.
- *The tajwid rulings* (§3.7, §6.1) — A registry: `standards/terminology/registries/tajwid_rules.tsv`, generated from `standards/terminology/data/tajweed_engine_rules.json`, with `hukm_al_tajwid` as the classification over it. See the decision *The rules of tajwid are a registry, not entries*.
