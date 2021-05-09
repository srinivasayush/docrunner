import os
from typing import Optional


def create_language_environment(language: str, directory_path: Optional[str] = None) -> str:
    """Creates a folder for storing code if one does not exist already

    Parameters
    ----------
    language : str
        Name of the language
    directory_path : Optional[str], optional
        Path to the directory where the code should be stored, by default None

    Returns
    -------
    str
        Path to the directory where the code is stored
    """
    if not directory_path:
        directory_path = f'./docrunner-build-{language}'
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    return directory_path
