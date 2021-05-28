from typing import List

import pytest
from docrunner.constants.language_abbrev import LANGUAGE_ABBREV_MAPPING


@pytest.fixture()
def language_commands() -> List[str]:
    commands = list(LANGUAGE_ABBREV_MAPPING.keys()) + ["run"]
    return commands


@pytest.fixture()
def languages() -> List[str]:
    return list(LANGUAGE_ABBREV_MAPPING.keys())
