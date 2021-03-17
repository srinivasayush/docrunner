from utils.file import get_code_from_markdown, write_file
import os
import platform
from pathlib import Path
from typing import List, Optional
import subprocess


def create_python_environment(env_path: Optional[str] = None) -> str:
    if env_path == None:
        directory_path = './docrunner-build-py'
        os.mkdir(directory_path)
    else:
        directory_path = str(Path(env_path).parent)
    
    return directory_path

def run_python(
    env_path: Optional[str] = None,
    run_command: Optional[str] = None,
    markdown_path: Optional[str] = None,
    multi_file: Optional[bool] = None,
):
    code_snippets = get_code_from_markdown(
        language='python',
        markdown_path=markdown_path,
    )
    if not code_snippets:
        return None
    
    directory_path = create_python_environment(
        env_path=env_path
    )
    filepath: str = None
    if multi_file:
        filepaths: List[str] = []
        for i in range(0, len(code_snippets)):
            filepath = f'{directory_path}/file{i + 1}.py'
            write_file(
                filepath=filepath,
                lines=code_snippets[i],
            )
            filepaths.append(filepath)
    else:
        all_lines = ''.join(code_snippets)
        filepath = f'{directory_path}/main.py'
        write_file(
            filepath=filepath,
            lines=all_lines,
        )

    if env_path:
        operating_system = platform.system()
        env_command: str = None
        if operating_system == 'Windows':
            env_command = f'{env_path}\\Scripts\\activate.bat'
            subprocess.call(env_command)
        elif operating_system == 'Linux':
            env_command = f'source {env_path}/bin/activate'
            os.system(env_command)
    
    if run_command:
        run_command = run_command.replace('"', '')
        base = os.getcwd()
        directory_path = str(Path(filepath).parent)
        os.chdir(os.path.join(os.getcwd(), directory_path))
        os.system(run_command)
        os.chdir(base)
    else:
        if multi_file:
            for filepath in filepaths:
                os.system(f'python {filepath}')
        else:
            os.system(f'python {filepath}')
