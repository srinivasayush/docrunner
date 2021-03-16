from utils.utils import VALID_LANGUAGES, is_valid_language
import typer
from languages.python import run_python

app = typer.Typer()

def main(
    language: str = typer.Option(
        ...,
        prompt=True,
        help='The language you want to identify and execute in your markdown file'
    ),
):
    language = language.lower()
    if not is_valid_language(language):
        print(f"The language {language} either isn't a valid language, or we just don't support it right now")
        print("Right now we support: ")
        for i in range(0, len(VALID_LANGUAGES)):
            print(f'{i + 1}. {VALID_LANGUAGES[i]}')
        return None

    print(f'Running {language} code')
    if language == 'python':
        run_python()

if __name__ == '__main__':
    typer.run(main)
