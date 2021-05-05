import typer

from .constants import (JAVASCRIPT_DIRECTORY_HELP, MARKDOWN_PATH_HELP,
                        PY_ENVIRONMENT_HELP, PY_RUN_HELP,
                        TYPESCRIPT_DIRECTORY_HELP)
from .languages.javascript import run_javascript
from .languages.python import run_python
from .languages.typescript import run_typescript

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
    startup_command: str = typer.Option(
        None,
        help=PY_RUN_HELP
    ),
    multi_file: bool = False,
):
    typer.echo(typer.style("Running python", fg=typer.colors.GREEN))
    run_python(
        env_path=env_path,
        startup_command=startup_command,
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
    startup_command: str = typer.Option(
        None,
        help=PY_RUN_HELP
    ),
    multi_file: bool = False,
):
    typer.echo(typer.style("Running javascript", fg=typer.colors.YELLOW))
    run_javascript(
        directory_path=directory_path,
        markdown_path=markdown_path,
        multi_file=multi_file,
        startup_command=startup_command
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
    startup_command: str = typer.Option(
        None,
        help=PY_RUN_HELP
    ),
    multi_file: bool = False,
):
    typer.echo(typer.style("Running typescript", fg=typer.colors.BLUE))
    run_typescript(
        directory_path=directory_path,
        markdown_path=markdown_path,
        multi_file=multi_file,
        startup_command=startup_command
    )


if __name__ == '__main__':
    app()
