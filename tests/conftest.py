"""The tools import each other by bare name from tools/; the skill scripts from
their own directory. Both go on the path once, here."""
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
SKILL = os.path.join(ROOT, "skills", "quranic-terminology")
SKILL_SCRIPTS = os.path.join(SKILL, "scripts")
TEMPLATE_SCRIPTS = os.path.join(ROOT, "tools", "skill_template", "scripts")
for path in (TOOLS, TEMPLATE_SCRIPTS):
    if path not in sys.path:
        sys.path.insert(0, path)


@pytest.fixture(scope="session")
def skill_data():
    """The generated dictionary the skill scripts resolve against."""
    with open(os.path.join(SKILL, "data", "terminology.json"), encoding="utf-8") as fh:
        return json.load(fh)
