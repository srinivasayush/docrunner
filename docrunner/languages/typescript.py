import os
from pathlib import Path
from typing import List

from docrunner.utils.language import create_language_environment

from ..models.options import Options
from ..utils.file import get_code_from_markdown, write_file


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

    markdown_paths = options.markdown
    directory_path = options.directory_path
    startup_command = options.startup_command
    multi_file = options.multi_file

    for markdown_path in markdown_paths:
    
        code_snippets = get_code_from_markdown(
            language='typescript',
            markdown_path=markdown_path,
        )
        if not code_snippets:
            return None

        directory_path = create_language_environment(
            language='ts',
            markdown_path=markdown_path,
            directory_path=directory_path,
        )

        filepath: str = None
        if multi_file:
            filepaths: List[str] = []
            for i in range(0, len(code_snippets)):
                filepath = f'{directory_path}/file{i + 1}.ts'
                write_file(
                    filepath=filepath,
                    lines=code_snippets[i],
                    overwrite=True,
                )
                filepaths.append(filepath)
        else:
            all_lines = ''.join(code_snippets)
            filepath = f'{directory_path}/main.ts'
            write_file(
                filepath=filepath,
                lines=all_lines,
                overwrite=True,
            )
        
        if startup_command:
            startup_command = startup_command.replace('"', '')
            os.system(startup_command)
            return


        if multi_file:
            for filepath in filepaths:
                compile_exit_code = compile_typescript(filepath=filepath)
                if compile_exit_code != 0:
                    return None

                filepath = filepath[0: len(filepath) - 3]
                filepath += '.js'
                os.system(f'node {filepath}')
        else:
            compile_exit_code = compile_typescript(filepath=filepath)
            if compile_exit_code != 0:
                return None
            filepath = filepath[0: len(filepath) - 3]
            filepath += '.js'
            os.system(f'node {filepath}')
