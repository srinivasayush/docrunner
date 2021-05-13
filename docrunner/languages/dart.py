import os

import typer

from ..models.options import Options
from ..utils.language import create_language_files


def run_dart(
    options: Options
):
    """Runs all dart code within a markdown '.md' file

    Parameters
    ----------
    options : Options
        Docrunner options
    """

    try:
        code_filepaths = create_language_files(
            options=options,
        )

        for filepath in code_filepaths:
            os.system(f'dart run {filepath}')

    except FileNotFoundError as error:
        typer.echo(
            typer.style(
                f'Error: file `{error.filename}` not found',
                fg=typer.colors.RED,
            ),
            err=True
        )
