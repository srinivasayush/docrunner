from utils.file import get_code_from_markdown, write_file
import os
import platform
from pathlib import Path
from typing import Optional
import subprocess


def create_python_environment(env_path: Optional[str] = None) -> str:
    if env_path == None:
        directory_path = './docrunner-build-py'
        os.mkdir(directory_path)
    else:
        directory_path = str(Path(env_path).parent)

    return f'{directory_path}/main.py'

def run_python(
    env_path: Optional[str] = None,
    run_command: Optional[str] = None,
    markdown_path: Optional[str] = None,
):
    code_lines = get_code_from_markdown(
        language='python',
        markdown_path=markdown_path,
    )
    if not code_lines:
        return None
    
    filepath = create_python_environment(
        env_path=env_path
    )
    write_file(
        filepath=filepath,
        lines=code_lines
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
        os.system(f'python {filepath}')
