import os

import typer

from ..exceptions.base_exception import DocrunnerBaseException
from ..models.options import Options
from ..utils.general import log_exception
from ..utils.language import create_language_files


def run_python(options: Options):
    """Runs all python code within a markdown '.md' file

    Parameters
    ----------
    options : Options
        Docrunner options
    """

    startup_command = options.startup_command
    final_exit_code = 0

    try:
        code_filepaths = create_language_files(
            options=options,
        )

        if startup_command:
            startup_command = startup_command.replace('"', "")
            exit_code = os.system(startup_command)
            if exit_code != 0:
                raise typer.Exit(code=exit_code)

            return

        for filepath in list(code_filepaths.keys()):
            exit_code = os.system(f"python {filepath}")
            if exit_code != 0:
                final_exit_code = exit_code

        if final_exit_code != 0:
            raise typer.Exit(code=final_exit_code)

    except DocrunnerBaseException as error:
        log_exception(error)
