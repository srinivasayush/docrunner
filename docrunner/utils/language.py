import glob
import os
from typing import List, Optional

from ..models.options import Options
from ..utils.file import get_code_from_markdown, write_file

LANGUAGE_TO_EXTENSION = {
    'python': 'py',
    'javascript': 'js',
    'typescript': 'ts',
    'dart': 'dart',
}

def create_language_environment(
    language: str,
    markdown_path: str,
    directory_path: Optional[str] = None,
) -> str:
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
        markdown_file_name = os.path.splitext(markdown_path)[0]
        language_extension = LANGUAGE_TO_EXTENSION[language]
        directory_path = f'./docrunner-build-{language_extension}/{markdown_file_name}'
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    return directory_path

def create_language_files(options: Options) -> List[str]:
    """Creates code files for a specified `options.language`

    Parameters
    ----------
    options : Options
        Docrunner options

    Returns
    -------
    List[str]
        A list of file paths to each code file created
    """
    language = options.language
    markdown_paths = options.markdown_paths
    directory_path = options.directory_path
    multi_file = options.multi_file

    code_filepaths = []

    for markdown_path in markdown_paths:
        if os.path.isdir(markdown_path):
            code_filepaths += create_language_files(
                options=Options(
                    language=options.language,
                    markdown_paths=list(glob.glob(f'{markdown_path}/*.md')),
                    directory_path=options.directory_path,
                    startup_command=options.startup_command,
                    multi_file=options.multi_file,
                )
            )
            return code_filepaths

        code_snippets = get_code_from_markdown(
            language=language,
            markdown_path=markdown_path,
        )

        directory_path = create_language_environment(
            language=language,
            markdown_path=markdown_path,
            directory_path=directory_path
        )

        filepath: str = None
        if multi_file:
            for i in range(0, len(code_snippets)):
                filepath = f'{directory_path}/file{i + 1}.{LANGUAGE_TO_EXTENSION[language]}'
                write_file(
                    filepath=filepath,
                    lines=code_snippets[i],
                    overwrite=True,
                )
                code_filepaths.append(filepath)
        else:
            all_lines = ''.join(code_snippets)
            filepath = f'{directory_path}/main.{LANGUAGE_TO_EXTENSION[language]}'
            write_file(
                filepath=filepath,
                lines=all_lines,
                overwrite=True,
            )
            code_filepaths.append(filepath)
    
    return code_filepaths
