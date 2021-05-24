import glob
import os
from io import TextIOWrapper
from pathlib import Path
from typing import List, Optional

from ..constants.language_abbrev import LANGUAGE_ABBREV_MAPPING
from ..exceptions.error import DocrunnerError
from ..exceptions.warning import DocrunnerWarning
from ..models.snippet import Snippet
from ..utils.general import log_exception

# def validate_links(markdown_path: str):
#     # Usage: validate_links(r'C:\path\to\README.md')
#     ignore = 'https://reporoster.com/'

#     if not markdown_path:
#         markdown_path = './README.md'

#     markdown_lines = read_file(
#         filepath=markdown_path
#     )

#     if not markdown_lines:
#         return

#     url_list = []
#     for line in markdown_lines:
#         if 'https://' in line or 'http://' in line or 'ftp://' in line:
#             matches = re.findall(
#                 '(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', line)[0]
#             url = ''
#             url += matches[0] + '://' + matches[1] + matches[2]
#             url_list.append(url)

#     typer.echo('Docrunner Found', len(url_list), 'urls in', markdown_path)
#     typer.echo('Running URL Validation')
#     for url in url_list:
#         try:
#             res = requests.get(url, allow_redirects=True)
#         except Exception:
#             if not url.startswith(ignore):
#                 typer.echo(f'Invalid URL:', url)
#             else:
#                 typer.echo('Valid URL:', url)
#             continue

#         if res.status_code != 200:
#             if not url.startswith(ignore):
#                 typer.echo(f'Invalid URL:', url)
#             else:
#                 typer.echo('Valid URL:', url)
#         else:
#             typer.echo('Valid URL:', url)


def read_file(filepath: str) -> List[str]:
    """Reads a file and returns a list of lines

    Parameters
    ----------
    filepath : str
        Path to the file, by default None

    Returns
    -------
    List[str]
        List of lines from markdown '.md' file
    """

    try:
        file = open(filepath, mode='r', encoding='utf-8')
    except FileNotFoundError as error:
        raise DocrunnerError(
            f'Error: file `{error.filename}` not found'
        )

    markdown_lines = file.readlines()
    file.close()

    markdown_lines = [line.replace('\n', '').strip() for line in markdown_lines]
    return markdown_lines


def get_all_files(
    directory_path: str,
    file_extensions: List[str],
    recursive: bool = False,
) -> List[str]:
    """Returns a list of markdown file paths inside a `directory_path`

    Parameters
    ----------
    directory_path : str
        The path to the directory to search inside
    file_extensions: List[str]
        The file extensions to search for within this directory
    recursive : bool, optional
        Whether to traverse through the directory recursive or not, by default False

    Returns
    -------
    List[str]
        A list of markdown file paths
    """

    if recursive is None:
        recursive = False

    filepaths = []
    for filepath in glob.glob(f'{directory_path}/**', recursive=recursive):
        extension = os.path.splitext(filepath)[1]
        if extension in file_extensions:
            filepaths.append(filepath)
    
    return filepaths


def is_snippet_decorator(string: str) -> bool:

    def is_comment(string: str) -> bool:
        return string[0: 4] == '<!--' and string[-3:] == '-->'
    
    if is_comment(string):
        if 'docrunner.' in string:
            return True

    return False


def _get_complete_snippet(language: str, lines: List[str], line_number: int) -> str:
    code = ''
    for i in range(line_number + 1, len(lines)):
        if len(lines[i]) > 3 and lines[i][0:3] == '```' and lines[i] not in LANGUAGE_ABBREV_MAPPING[language]:
            raise DocrunnerError(
                'Found opening ``` before closing ```'
            )
        elif lines[i] == '```':
            found_closed = True
            break
        else:
            code += f'{lines[i]}\n'

    if not found_closed:
        raise DocrunnerError(
            'No closing ```'
        )
    
    return code


def _is_any_language_opening(string: str) -> bool:
    """Returns whether the `string` is a markdown language opening of any of the supported languages

    Parameters
    ----------
    string : str
        The string to be checked

    Returns
    -------
    bool
        Whether the `string` is a markdown language opening of any of the supported languages
    """
    for language in LANGUAGE_ABBREV_MAPPING.keys():
        if string in LANGUAGE_ABBREV_MAPPING[language]:
            return True

    return False

def get_snippets_from_markdown(
    language: str,
    markdown_path: str,
) -> List[Snippet]:

    markdown_lines = read_file(
        filepath=markdown_path,
    )

    code_snippets: List[Snippet] = []
    last_code_snippet_at = None

    for i in range(0, len(markdown_lines) - 2):
        snippet_decorators = []
        if markdown_lines[i] in LANGUAGE_ABBREV_MAPPING[language]:
            if last_code_snippet_at == i:
                continue

            last_code_snippet_at = i
            code = _get_complete_snippet(
                language=language,
                lines=markdown_lines,
                line_number=i,
            )
            code_snippets.append(
                Snippet.new(
                    code=code,
                    decorators=[]
                )
            )

        elif is_snippet_decorator(markdown_lines[i]):
            last_decorator_line = i
            snippet_decorators: List[str] = [markdown_lines[i]]
            for j in range(i + 1, len(markdown_lines)):
                if markdown_lines[j] in LANGUAGE_ABBREV_MAPPING[language]:
                    if last_code_snippet_at == j:
                        continue
                    
                    if not is_snippet_decorator(markdown_lines[j - 1]):
                        snippet_decorators = []

                    last_code_snippet_at = j
                    code = _get_complete_snippet(
                        language=language,
                        lines=markdown_lines,
                        line_number=j,
                    )

                    code_snippets.append(
                        Snippet.new(
                            code=code,
                            decorators=snippet_decorators,
                        )
                    )

                    break

                elif is_snippet_decorator(markdown_lines[j]):
                    last_decorator_line = j
                    snippet_decorators.append(markdown_lines[j])

                elif not is_snippet_decorator(markdown_lines[j]) and not _is_any_language_opening(markdown_lines[j]):
                    if last_decorator_line == j - 1:
                        comment_warning = DocrunnerWarning(
                            f'Docrunner comment found without code snippet at line {j} in `{markdown_path}`'
                        )
                        log_exception(comment_warning)
    
    code_snippets = [snippet for snippet in code_snippets if not snippet.options.ignore]

    if len(code_snippets) == 0:
        nothing_to_run = DocrunnerWarning(
            f'Nothing to run in `{markdown_path}`'
        )
        log_exception(nothing_to_run)

    return code_snippets


def write_file(
    filepath: str,
    content: str,
    overwrite: Optional[bool] = None,
    append: Optional[bool] = None,
) -> None:
    """Writes `lines` to a file located at `filepath`

    Parameters
    ----------
    filepath : str
        Filepath of file you want to write to
    content : str
        String you want to write into file
    rewrite : Optional[bool]
        Whether the file should be written over if it already exists
    """

    if overwrite is None:
        overwrite = False
    if append is None:
        append = False

    main_file: Optional[TextIOWrapper] = None
    try:
        if os.path.exists(filepath):
            if not overwrite:
                raise DocrunnerError(
                    f'file `{filepath}` already exists'
                )
            if append:
                main_file = open(filepath, mode='a', encoding='utf-8')
            else:
                main_file = open(filepath, mode='w+', encoding='utf-8')
        else:
            main_file = open(filepath, mode='x', encoding='utf-8')
    except FileNotFoundError as error:
        raise DocrunnerError(
            f'folder `{Path(error.filename).parent}` not found'
        )

    main_file.write(content)
    main_file.close()
    main_file = None
