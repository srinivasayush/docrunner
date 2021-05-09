import os
from typing import List, Optional

from ..utils.file import get_code_from_markdown, write_file
from ..utils.language import create_language_environment


def run_dart(
    directory_path: Optional[str] = None,
    markdown_path: Optional[str] = None,
    multi_file: Optional[bool] = None,
):
    """Runs all dart code within a markdown '.md' file

    Parameters
    ----------
    directory_path : Optional[str], optional
        Path to directory where dart code should be stored and ran, by default None
    markdown_path : Optional[str], optional
        Path to markdown '.md' file, by default None
    multi_file : Optional[bool], optional
        Whether each code snippet should be stored and run in another file or not, by default None
    """

    code_snippets = get_code_from_markdown(
        language='dart',
        markdown_path=markdown_path
    )
    if not code_snippets:
        return

    directory_path = create_language_environment(
        language='dart',
        directory_path=directory_path
    )

    filepath: str = None
    if multi_file:
        filepaths: List[str] = []
        for i in range(0, len(code_snippets)):
            filepath = f'{directory_path}/file{i + 1}.dart'
            write_file(
                filepath=filepath,
                lines=code_snippets[i],
            )
            filepaths.append(filepath)
    else:
        all_lines = ''.join(code_snippets)
        filepath = f'{directory_path}/main.dart'
        write_file(
            filepath=filepath,
            lines=all_lines,
        )

    if multi_file:
        for filepath in filepaths:
            os.system(f'dart run {filepath}')
    else:
        os.system(f'dart run {filepath}')
