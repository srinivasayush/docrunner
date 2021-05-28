from typing import List

from docrunner.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_language_commands(
    languages: List[str], language_commands: List[str]
) -> None:

    for language_command in language_commands:
        result = runner.invoke(app, [language_command])
        assert result.exit_code == 0
        if language_command in languages:
            assert f"Running {language_command}" in result.stdout
