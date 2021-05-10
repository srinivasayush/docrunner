import os
import re
from io import TextIOWrapper
from pathlib import Path
from typing import List, Optional

import requests
import typer

LANGUAGE_ABBREV_MAPPING = {
    'python': [
        '```py',
        '```python',
    ],
    'javascript': [
        '```js',
        '```javascript',
    ],
    'typescript': [
        '```ts',
        '```typescript'
    ],
    'dart': [
        '```dart'
    ]
}


def validate_links(markdown_path: Optional[str] = None):
    # Usage: validate_links(r'C:\path\to\README.md')
    ignore = 'https://reporoster.com/'

    if not markdown_path:
        markdown_path = './README.md'

    markdown_lines = read_markdown(
        markdown_path=markdown_path
    )

    if not markdown_lines:
        return

    url_list = []
    for line in markdown_lines:
        if 'https://' in line or 'http://' in line or 'ftp://' in line:
            matches = re.findall(
                '(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', line)[0]
            url = ''
            url += matches[0] + '://' + matches[1] + matches[2]
            url_list.append(url)

    typer.echo('Docrunner Found', len(url_list), 'urls in', markdown_path)
    typer.echo('Running URL Validation')
    for url in url_list:
        try:
            res = requests.get(url, allow_redirects=True)
        except Exception:
            if not url.startswith(ignore):
                typer.echo(f'Invalid URL:', url)
            else:
                typer.echo('Valid URL:', url)
            continue

        if res.status_code != 200:
            if not url.startswith(ignore):
                typer.echo(f'Invalid URL:', url)
            else:
                typer.echo('Valid URL:', url)
        else:
            typer.echo('Valid URL:', url)


def read_markdown(markdown_path: Optional[str] = None) -> Optional[List[str]]:
    """Reads a markdown file and returns a list of lines

    Parameters
    ----------
    markdown_path : Optional[str], optional
        Path to the markdown '.md' file, by default None

    Returns
    -------
    Optional[List[str]]
        List of lines from markdown '.md' file
    """
    if not markdown_path:
        markdown_path = './README.md'
    
    markdown_file = None
    markdown_lines = None

    try:
        markdown_file = open(markdown_path, mode='r', encoding='utf-8')
        markdown_lines = markdown_file.readlines()
        markdown_file.close()
    except FileNotFoundError as error:
        typer.echo(
            typer.style(
                f'Error: file `{error.filename}` not found', fg=typer.colors.RED
            ),
            err=True
        )
        return None
    return markdown_lines


def get_code_from_markdown(
    language: str,
    markdown_path: Optional[str] = None,
) -> Optional[List[str]]:
    """Returns a list of code snippets of a certain `language`

    Parameters
    ----------
    language : str
        Name of the language
    markdown_path : Optional[str], optional
        Path to the markdown '.md' file, by default None

    Returns
    -------
    Optional[List[str]]
        List of string code snippets from markdown '.md' file
    """

    markdown_lines = read_markdown(
        markdown_path=markdown_path,
    )
    if not markdown_lines:
        return

    markdown_lines = [line.replace('\n', '').strip() for line in markdown_lines]
    language_openings = [i for i, line in enumerate(
        markdown_lines) if line in LANGUAGE_ABBREV_MAPPING[language]]

    if len(language_openings) == 0:
        typer.echo(
            typer.style(
                "WARNING: Language not found in markdown file",
                fg=typer.colors.YELLOW,
            )
        )
    code_snippets: List[str] = []
    for i in language_openings:
        found_closed = False
        code_lines = ''
        if markdown_lines[i] in LANGUAGE_ABBREV_MAPPING[language]:
            for j in range(i + 1, len(markdown_lines)):
                if len(markdown_lines[j]) > 3 and markdown_lines[j][0:3] == '```' and markdown_lines[j] not in LANGUAGE_ABBREV_MAPPING[language]:
                    typer.echo(
                        typer.style(
                            'Error: Found opening ``` before closing ```', fg=typer.colors.RED
                        ),
                        err=True
                    )
                    return None
                elif markdown_lines[j] == '```':
                    code_snippets.append(code_lines)
                    found_closed = True
                    break
                else:
                    code_lines += f'{markdown_lines[j]}\n'
            if not found_closed:
                typer.echo(
                    typer.style(
                        'Error: No closing ```', fg=typer.colors.RED
                    ),
                    err=True,
                )

    return code_snippets


def write_file(filepath: str, lines: str) -> None:
    """Writes `lines` to a file located at `filepath`

    Parameters
    ----------
    filepath : str
        Filepath of file you want to write to
    lines : str
        String you want to write into file
    """
    main_file: TextIOWrapper = None
    try:
        if os.path.exists(filepath):
            main_file = open(filepath, mode='w+', encoding='utf-8')
        else:
            main_file = open(filepath, mode='x', encoding='utf-8')
    except FileNotFoundError as error:
        typer.echo(
            typer.style(
                f'Error: folder `{Path(error.filename).parent}` not found', fg=typer.colors.RED
            ),
            err=True
        )
        return None

    main_file.write(lines)
    main_file.close()
    main_file = None
