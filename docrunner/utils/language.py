import os
from typing import Optional


def create_language_environment(language: str, directory_path: Optional[str] = None) -> str:
    if not directory_path:
        directory_path = f'./docrunner-build-{language}'
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    return directory_path
