import os
from typing import Optional
from pathlib import Path
from utils.file import get_code_from_markdown, write_file



def create_typescript_environment(directory_path: Optional[str] = None) -> str:
    if directory_path == None:
        directory_path = './docrunner-build-ts'
        os.mkdir(directory_path)

    return f'{directory_path}/index.ts'

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
):
    code_lines = get_code_from_markdown(
        language='typescript',
    )
    if not code_lines:
        return None

    filepath = create_typescript_environment(
        directory_path=directory_path,
    )
    write_file(
        filepath=filepath,
        lines=code_lines,
    )

    compile_exit_code = compile_typescript(filepath=filepath)
    if compile_exit_code != 0:
        return None

    filepath = filepath[0 : len(filepath) - 3]
    filepath += '.js'
    os.system(f'node {filepath}')
