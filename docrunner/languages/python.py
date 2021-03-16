from typing import Optional
from utils.file import write_code_file
import os

def create_python_environment(directory_path: Optional[str] = None) -> str:
    if directory_path == None:
        directory_path = './runreadme'
    os.mkdir(directory_path)
    home = os.getcwd()

    os.chdir(os.path.join(os.getcwd(), directory_path))
    os.system('python -m venv env')
    os.chdir(home)

    return f'{directory_path}/main.py'

def run_python(
    directory_path: Optional[str] = None
):
    filepath = create_python_environment(
        directory_path=directory_path
    )
    write_code_file(
        language='python',
        filepath=filepath,
    )
    os.system(f'python {filepath}')
