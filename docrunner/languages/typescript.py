import os
from pathlib import Path

import typer

from ..exceptions.base_exception import DocrunnerBaseException
from ..models.options import Options
from ..utils.general import log_exception
from ..utils.language import create_language_files


def compile_typescript(filepath: str) -> int:
    directory_path = str(Path(filepath).parent)
    compile_command = f"tsc {filepath}"
    compile_exit_code = 0

    if os.path.exists(f"{directory_path}/tsconfig.json"):
        compile_command = f"tsc -p ."
        base = os.getcwd()
        os.chdir(os.path.join(base, directory_path))
        compile_exit_code = os.system(compile_command)
        os.chdir(base)
    else:
        compile_exit_code = os.system(compile_command)

    return compile_exit_code


def run_typescript(options: Options):
    """Runs all typescript code within a markdown '.md' file

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
            compile_exit_code = compile_typescript(filepath=filepath)
            if compile_exit_code != 0:
                final_exit_code = compile_exit_code

            filepath = filepath[0:-3]
            filepath += ".js"
            run_exit_code = os.system(f"node {filepath}")
            if run_exit_code != 0:
                final_exit_code = run_exit_code

        if final_exit_code != 0:
            raise typer.Exit(code=final_exit_code)

    except DocrunnerBaseException as error:
        log_exception(error)
