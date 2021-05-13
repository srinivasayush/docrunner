import os

import typer

from ..models.options import Options
from ..utils.language import create_language_files


def run_javascript(
    options: Options
):
    """Runs all javascript code within a markdown '.md' file

    Parameters
    ----------
    options : Options
        Docrunner options
    """
    startup_command = options.startup_command

    code_filepaths = None
    try:
        code_filepaths = create_language_files(
            options=options,
        )

        if startup_command:
            startup_command = startup_command.replace('"', '')
            os.system(startup_command)
            return

        for filepath in code_filepaths:
            os.system(f'node {filepath}')

    except FileNotFoundError as error:
        typer.echo(
            typer.style(
                f'Error: file `{error.filename}` not found',
                fg=typer.colors.RED,
            ),
            err=True
        )
