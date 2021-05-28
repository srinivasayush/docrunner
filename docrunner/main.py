from typing import Optional

import typer

from docrunner import __version__
from docrunner.constants.help import (
    DART_DIRECTORY_HELP,
    JAVASCRIPT_DIRECTORY_HELP,
    MARKDOWN_PATH_HELP,
    PYTHON_DIRECTORY_HELP,
    STARTUP_COMMAND_HELP,
    TYPESCRIPT_DIRECTORY_HELP,
)
from docrunner.constants.language_color import LANGUAGE_TO_COLOR
from docrunner.exceptions.error import DocrunnerError
from docrunner.languages.dart import run_dart
from docrunner.languages.javascript import run_javascript
from docrunner.languages.python import run_python
from docrunner.languages.typescript import run_typescript
from docrunner.models.options import Options
from docrunner.utils.general import log_exception

app = typer.Typer()


@app.command(name="version")
def version_command():
    """Gets the version of docrunner that you are running"""
    typer.echo(f"Docrunner version {__version__}")


@app.callback(invoke_without_command=True)
def version_callback(version: bool = False):
    """Gets the version of docrunner that you are running"""
    if version:
        version_command()
    raise typer.Exit(code=0)


@app.command()
def run():
    """
    Runs docrunner with your `docrunner.toml` configuration file
    """

    options = Options.from_config_file()
    if not options:
        typer.echo(
            typer.style(
                "No `docrunner.toml` file found, please create one",
                fg=typer.colors.RED,
            ),
            err=True,
        )
        return
    if not options.language:
        typer.echo(
            typer.style(
                "`language` field not specified in docrunner.toml, please add it",
                fg=typer.colors.RED,
            ),
            err=True,
        )
        return

    typer.echo(
        typer.style(
            f"Running {options.language}",
            fg=LANGUAGE_TO_COLOR[options.language],
        )
    )

    LANGUAGE_TO_FUNCTION = {
        "python": run_python,
        "javascript": run_javascript,
        "typescript": run_typescript,
        "dart": run_dart,
    }

    LANGUAGE_TO_FUNCTION[options.language](
        options=options,
    )


@app.command()
def init():
    """Creates a `docrunner.toml` configuration file in the root directory"""
    typer.echo(
        typer.style(
            "Creating configuration file",
            fg=typer.colors.GREEN,
        )
    )

    try:
        Options.create_config_file()
    except DocrunnerError as error:
        log_exception(error)


@app.command()
def python(
    markdown_path: str = typer.Option(None, help=MARKDOWN_PATH_HELP),
    directory_path: str = typer.Option(
        None,
        help=PYTHON_DIRECTORY_HELP,
    ),
    startup_command: str = typer.Option(None, help=STARTUP_COMMAND_HELP),
    multi_file: Optional[bool] = None,
):
    """
    Runs all python code within a markdown '.md' file
    """

    typer.echo(typer.style("Running python", fg=LANGUAGE_TO_COLOR["python"]))

    options = Options.override_with_cli_arguments(
        language="python",
        markdown_path=markdown_path,
        directory_path=directory_path,
        startup_command=startup_command,
        multi_file=multi_file,
    )
    run_python(
        options=options,
    )


@app.command()
def javascript(
    markdown_path: str = typer.Option(None, help=MARKDOWN_PATH_HELP),
    directory_path: str = typer.Option(
        None,
        help=JAVASCRIPT_DIRECTORY_HELP,
    ),
    startup_command: str = typer.Option(None, help=STARTUP_COMMAND_HELP),
    multi_file: Optional[bool] = None,
):
    """
    Runs all javascript code within a markdown '.md' file
    """

    typer.echo(
        typer.style("Running javascript", fg=LANGUAGE_TO_COLOR["javascript"])
    )

    options = Options.override_with_cli_arguments(
        language="javascript",
        markdown_path=markdown_path,
        directory_path=directory_path,
        startup_command=startup_command,
        multi_file=multi_file,
    )
    run_javascript(
        options=options,
    )


@app.command()
def typescript(
    markdown_path: str = typer.Option(None, help=MARKDOWN_PATH_HELP),
    directory_path: str = typer.Option(
        None,
        help=TYPESCRIPT_DIRECTORY_HELP,
    ),
    startup_command: str = typer.Option(None, help=STARTUP_COMMAND_HELP),
    multi_file: Optional[bool] = None,
):
    """
    Runs all typescript code within a markdown '.md' file
    """
    typer.echo(
        typer.style("Running typescript", fg=LANGUAGE_TO_COLOR["typescript"])
    )

    options = Options.override_with_cli_arguments(
        language="typescript",
        markdown_path=markdown_path,
        directory_path=directory_path,
        startup_command=startup_command,
        multi_file=multi_file,
    )
    run_typescript(
        options=options,
    )


@app.command()
def dart(
    markdown_path: str = typer.Option(None, help=MARKDOWN_PATH_HELP),
    directory_path: str = typer.Option(
        None,
        help=DART_DIRECTORY_HELP,
    ),
    startup_command: str = typer.Option(None, help=STARTUP_COMMAND_HELP),
    multi_file: Optional[bool] = None,
):
    """
    Runs all dart code within a markdown '.md' file
    """

    typer.echo(typer.style("Running dart", fg=LANGUAGE_TO_COLOR["dart"]))

    options = Options.override_with_cli_arguments(
        language="dart",
        markdown_path=markdown_path,
        directory_path=directory_path,
        startup_command=startup_command,
        multi_file=multi_file,
    )
    run_dart(
        options=options,
    )


if __name__ == "__main__":
    app()
