import os
from pathlib import Path

import typer

from ..models.options import Options
from ..utils.language import create_language_files


def compile_typescript(filepath: str) -> int:
    directory_path = str(Path(filepath).parent)
    compile_command = f'tsc {filepath}'
    compile_exit_code = 0

    if os.path.exists(f'{directory_path}/tsconfig.json'):
        compile_command = f'tsc -p .'
        base = os.getcwd()
        os.chdir(os.path.join(base, directory_path))
        compile_exit_code = os.system(compile_command)
        os.chdir(base)
    else:
        compile_exit_code = os.system(compile_command)

    return compile_exit_code


def run_typescript(
    options: Options
):
    """Runs all typescript code within a markdown '.md' file

    Parameters
    ----------
    options : Options
        Docrunner options
    """
    
    startup_command = options.startup_command
    try:
        code_filepaths = create_language_files(
            options=options,
        )

        if startup_command:
            startup_command = startup_command.replace('"', '')
            os.system(startup_command)
            return
        
        for filepath in code_filepaths:
            compile_exit_code = compile_typescript(filepath=filepath)
            if compile_exit_code != 0:
                return

            filepath = filepath[0: -3]
            filepath += '.js'
            os.system(f'node {filepath}')
    except FileNotFoundError as error:
        typer.echo(
            typer.style(
                f'Error: file `{error.filename}` not found',
                fg=typer.colors.RED,
            ),
            err=True
        )
