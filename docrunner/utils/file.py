import os
from io import TextIOWrapper
from typing import List, Optional, Union
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
};

def read_markdown(markdown_path: Optional[str] = None) -> List[str]:
    if not markdown_path:
        markdown_path = './README.md'
    markdown_file = open(markdown_path, mode='r', encoding='utf-8')
    markdown_lines = markdown_file.readlines()
    markdown_file.close()
    return markdown_lines

def get_code_from_markdown(
    language: str,
) -> Union[str, None]:
    code_lines = ''
    markdown_lines = read_markdown()
    markdown_lines = [line.replace('\n', '') for line in markdown_lines]
    found_closing = False
    for i in range(0, len(markdown_lines)):
        if markdown_lines[i] in LANGUAGE_ABBREV_MAPPING[language]:
            for j in range(i + 1, len(markdown_lines)):
                if markdown_lines[j] != '```':
                    code_lines += f'{markdown_lines[j]}\n'
                else:
                    found_closing = True
    if found_closing == False:
        typer.echo('Error: No closing ```')
        return None
    
    return code_lines


def write_file(filepath: str, lines: str) -> None:
    main_file: TextIOWrapper = None
    if os.path.exists(filepath):
        main_file = open(filepath, mode='w+', encoding='utf-8')
    else:
        main_file = open(filepath, mode='x', encoding='utf-8')
    
    main_file.write(lines)
    main_file.close()
    main_file = None
