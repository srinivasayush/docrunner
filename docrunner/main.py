import typer

from constants import (JAVASCRIPT_DIRECTORY_HELP, MARKDOWN_PATH_HELP,
                       PY_ENVIRONMENT_HELP, PY_RUN_HELP,
                       TYPESCRIPT_DIRECTORY_HELP)
from languages.javascript import run_javascript
from languages.python import run_python
from languages.typescript import run_typescript

app = typer.Typer()

@app.command()
def python(
    markdown_path: str = typer.Option(
        None,
        help=MARKDOWN_PATH_HELP
    ),
    env_path: str = typer.Option(
        None,
        help=PY_ENVIRONMENT_HELP
    ),
    run_command: str = typer.Option(
        None,
        help=PY_RUN_HELP
    ),
    multi_file: bool = False,
):  
    run_python(
        env_path=env_path,
        run_command=run_command,
        markdown_path=markdown_path,
        multi_file=multi_file,
    )

@app.command()
def javascript(
    markdown_path: str = typer.Option(
        None,
        help=MARKDOWN_PATH_HELP
    ),
    directory_path: str = typer.Option(
        None,
        help=JAVASCRIPT_DIRECTORY_HELP,
    ),
    multi_file: bool = False,
):
    run_javascript(
        directory_path=directory_path,
        markdown_path=markdown_path,
    )

@app.command()
def typescript(
    markdown_path: str = typer.Option(
        None,
        help=MARKDOWN_PATH_HELP
    ),
    directory_path: str = typer.Option(
        None,
        help=TYPESCRIPT_DIRECTORY_HELP,
    ),
    multi_file: bool = False,
):
    run_typescript(
        directory_path=directory_path,
        markdown_path=markdown_path,
    )



if __name__ == '__main__':
    app()
