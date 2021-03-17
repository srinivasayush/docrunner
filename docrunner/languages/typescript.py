import os
from pathlib import Path
from typing import List, Optional

from utils.file import get_code_from_markdown, write_file


def create_typescript_environment(directory_path: Optional[str] = None) -> str:
    if directory_path == None:
        directory_path = './docrunner-build-ts'
        os.mkdir(directory_path)
    
    return directory_path

def compile_typescript(filepath: str) -> int:
    directory_path = str(Path(filepath).parent)
    compile_command = f'tsc {filepath}'
    if os.path.exists(f'{directory_path}/tsconfig.json'):
        compile_command = f'tsc -p .'
    
    base = os.getcwd()
    os.chdir(os.path.join(base, directory_path))
    compile_exit_code = os.system(compile_command)
    os.chdir(base)

    return compile_exit_code

def run_typescript(
    directory_path: Optional[str] = None,
    markdown_path: Optional[str] = None,
):
    code_snippets = get_code_from_markdown(
        language='typescript',
        markdown_path=markdown_path,
    )
    if not code_snippets:
        return None

    directory_path = create_typescript_environment(
        directory_path=directory_path,
    )
    filepaths: List[str] = []
    for i in range(0, len(code_snippets)):
        filepath = f'{directory_path}/file{i + 1}.ts'
        write_file(
            filepath=filepath,
            lines=code_snippets[i],
        )
        filepaths.append(filepath)

    for filepath in filepaths:
        compile_exit_code = compile_typescript(filepath=filepath)
        if compile_exit_code != 0:
            return None

        filepath = filepath[0 : len(filepath) - 3]
        filepath += '.js'
        os.system(f'node {filepath}')
