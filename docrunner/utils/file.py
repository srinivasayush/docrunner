import os
from io import TextIOWrapper
from typing import List, Optional, Union
import typer
import re
import requests

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
}


def validate_links(markdown_path: Optional[str] = None):
    # Usage: validate_links(r'C:\path\to\README.md')
    ignore = 'https://reporoster.com/'

    if not markdown_path:
        markdown_path = './README.md'
    markdown_file = open(markdown_path, mode='r', encoding='utf-8')
    markdown_lines = markdown_file.readlines()
    markdown_file.close()

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


def read_markdown(markdown_path: Optional[str] = None) -> List[str]:
    if not markdown_path:
        markdown_path = './README.md'
    markdown_file = open(markdown_path, mode='r', encoding='utf-8')
    markdown_lines = markdown_file.readlines()
    markdown_file.close()
    return markdown_lines


def get_code_from_markdown(
    language: str,
    markdown_path: Optional[str] = None,
) -> Union[List[str], None]:
    markdown_lines = read_markdown(
        markdown_path=markdown_path,
    )

    markdown_lines = [line.replace('\n', '') for line in markdown_lines]
    language_openings = [i for i, line in enumerate(
        markdown_lines) if line in LANGUAGE_ABBREV_MAPPING[language]]

    if len(language_openings) == 0:
        typer.echo(
            typer.style(
                "WARNING: Language not found in markdown file",
                fg=typer.colors.MAGENTA,
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
    main_file: TextIOWrapper = None
    if os.path.exists(filepath):
        main_file = open(filepath, mode='w+', encoding='utf-8')
    else:
        main_file = open(filepath, mode='x', encoding='utf-8')

    main_file.write(lines)
    main_file.close()
    main_file = None
