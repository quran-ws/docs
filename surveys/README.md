# Surveys

A survey measures a real codebase against the standard: which of its names resolve to a dictionary entry, which break a rule the standard already fixes, and which name a concept the dictionary does not have yet.

What a survey holds is findings, not rules. A finding that the standard should change becomes a term or guideline proposal with the survey as its case — the "real case" that [CONTRIBUTING.md](../CONTRIBUTING.md) asks for — and the standard changes through that discussion, never through the survey itself. A finding that the surveyed project should change stays here for that project to act on.

| File | What it is |
| --- | --- |
| `quranpedia-net.md` | quranpedia.net (Laravel, 83 tables) measured on 2026-09-06. It produced 29 entries, one domain and 7 decisions. |
| `quranpedia-net-renames.tsv` | The machine-readable list for two of its screens: `surface`, `current`, `canonical`, `rule`, `note`. |
| `OPEN.md` | What the surveys raised that is still undecided. |

A survey is dated and is not kept in step with the dictionary. Where a survey has been overtaken by a decision, the section says so and links to the decision record.
