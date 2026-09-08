# quranic-terminology

An agent skill for naming the concepts of Quranic software by the Quran.ws
Terminology Standard, and for auditing a codebase against it. It carries the
standard, its dictionary (180 concepts, 755 recorded spellings),
the registries of the closed sets, and scripts that resolve any spelling to its
canonical name, derive a name from vocalized Arabic, draft an entry for a new
concept, and report every identifier in a tree that the standard would write
differently. Everything here is generated from
<https://github.com/quran-ws/guidelines> by `tools/generate_skill.py`; snapshot
`08b74f94cde7284d`. Edit the source there, not this directory.

To install it in Claude Code as a plugin, run
`/plugin marketplace add quran-ws/guidelines` and then
`/plugin install quranic-terminology@quran-ws`; `/plugin update` keeps it
current. To install a copy instead, put this directory at
`~/.claude/skills/quranic-terminology/` (every project) or at
`<project>/.claude/skills/quranic-terminology/` (one project) and run
`python3 scripts/update_check.py` now and then to learn when the copy has
fallen behind. The scripts need Python 3 and nothing else. `SKILL.md` is what
the agent reads; start there.
