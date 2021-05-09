from docrunner.utils.language import create_language_environment
import os
from typing import List, Optional

from ..utils.file import get_code_from_markdown, write_file


def run_javascript(
    directory_path: Optional[str] = None,
    startup_command: Optional[str] = None,
    markdown_path: Optional[str] = None,
    multi_file: Optional[bool] = None,
):
    """Runs all javascript code within a markdown '.md' file

    Parameters
    ----------
    directory_path : Optional[str], optional
        Path to directory where javascript code should be stored and ran, by default None
    startup_command : Optional[str], optional
        Command that is run which starts code, by default None
    markdown_path : Optional[str], optional
        Path to markdown '.md' file, by default None
    multi_file : Optional[bool], optional
        Whether each code snippet should be stored and run in another file or not, by default None
    """

    code_snippets = get_code_from_markdown(
        language='javascript',
        markdown_path=markdown_path,
    )
    if not code_snippets:
        return None

    directory_path = create_language_environment(
        language='js',
        directory_path=directory_path,
    )

    filepath: str = None
    if multi_file:
        filepaths: List[str] = []
        for i in range(0, len(code_snippets)):
            filepath = f'{directory_path}/file{i + 1}.js'
            write_file(
                filepath=filepath,
                lines=code_snippets[i],
            )
            filepaths.append(filepath)
    else:
        all_lines = ''.join(code_snippets)
        filepath = f'{directory_path}/main.js'
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
            os.system(f'node {filepath}')
    else:
        os.system(f'node {filepath}')
