from docrunner.utils.language import create_language_environment
import os
from pathlib import Path
from typing import List, Optional

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
    directory_path: Optional[str] = None,
    startup_command: Optional[str] = None,
    markdown_path: Optional[str] = None,
    multi_file: Optional[bool] = None,
):
    """Runs all typescript code within a markdown '.md' file

    Parameters
    ----------
    directory_path : Optional[str], optional
        Path to directory where typescript code should be stored and ran, by default None
    startup_command : Optional[str], optional
        Command that is run which starts code, by default None
    markdown_path : Optional[str], optional
        Path to markdown '.md' file, by default None
    multi_file : Optional[bool], optional
        Whether each code snippet should be stored and run in another file or not, by default None
    """
    
    code_snippets = get_code_from_markdown(
        language='typescript',
        markdown_path=markdown_path,
    )
    if not code_snippets:
        return None

    directory_path = create_language_environment(
        language='ts',
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
            )
            filepaths.append(filepath)
    else:
        all_lines = ''.join(code_snippets)
        filepath = f'{directory_path}/main.ts'
        write_file(
            filepath=filepath,
            lines=all_lines,
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
