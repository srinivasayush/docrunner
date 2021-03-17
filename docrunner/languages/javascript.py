import os
from typing import Optional
from utils.file import get_code_from_markdown, write_file



def create_javascript_environment(directory_path: Optional[str] = None) -> str:
    if directory_path == None:
        directory_path = './docrunner-build-js'
        os.mkdir(directory_path)

    return f'{directory_path}/index.js'

def run_javascript(
    directory_path: Optional[str] = None,
):
    code_lines = get_code_from_markdown(
        language='javascript',
    )
    if not code_lines:
        return None

    filepath = create_javascript_environment(
        directory_path=directory_path,
    )
    write_file(
        filepath=filepath,
        lines=code_lines,
    )

    os.system(f'node {filepath}')
