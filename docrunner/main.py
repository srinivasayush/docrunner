import typer

from .constants.help import (DART_DIRECTORY_HELP, JAVASCRIPT_DIRECTORY_HELP,
                             MARKDOWN_PATH_HELP, PYTHON_DIRECTORY_HELP,
                             STARTUP_COMMAND_HELP, TYPESCRIPT_DIRECTORY_HELP)
from .languages.dart import run_dart
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
    directory_path: str = typer.Option(
        None,
        help=PYTHON_DIRECTORY_HELP,
    ),
    startup_command: str = typer.Option(
        None,
        help=STARTUP_COMMAND_HELP
    ),
    multi_file: bool = False,
):
    typer.echo(typer.style("Running python", fg=typer.colors.GREEN))
    run_python(
        directory_path=directory_path,
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
        help=STARTUP_COMMAND_HELP
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
        help=STARTUP_COMMAND_HELP
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

@app.command()
def dart(
    markdown_path: str = typer.Option(
        None,
        help=MARKDOWN_PATH_HELP
    ),
    directory_path: str = typer.Option(
        None,
        help=DART_DIRECTORY_HELP,
    ),
    multi_file: bool = False,
):
    typer.echo(typer.style("Running dart", fg=typer.colors.BRIGHT_CYAN))
    run_dart(
        directory_path=directory_path,
        markdown_path=markdown_path,
        multi_file=multi_file,
    )

if __name__ == '__main__':
    app()
