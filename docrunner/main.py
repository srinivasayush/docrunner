import typer

from .constants.help import (DART_DIRECTORY_HELP, JAVASCRIPT_DIRECTORY_HELP,
                             MARKDOWN_PATH_HELP, PYTHON_DIRECTORY_HELP,
                             STARTUP_COMMAND_HELP, TYPESCRIPT_DIRECTORY_HELP)
from .languages.dart import run_dart
from .languages.javascript import run_javascript
from .languages.python import run_python
from .languages.typescript import run_typescript
from .models.options import Options

app = typer.Typer()


LANGUAGE_TO_COLOR = {
    'python': typer.colors.GREEN,
    'javascript': typer.colors.YELLOW,
    'typescript': typer.colors.BLUE,
    'dart': typer.colors.BRIGHT_CYAN,
}

LANGUAGE_TO_FUNCTION = {
    'python': run_python,
    'javascript': run_javascript,
    'typescript': run_typescript,
    'dart': run_dart,
}

@app.command()
def run():
    """
    The docrunner run command
    """

    options = Options.from_config_file()
    if not options:
        typer.echo(
            typer.style(
                'No `docrunner.toml` file found, please create one', fg=typer.colors.RED
            ),
            err=True
        )
        return
    if not options.language:
        typer.echo(
            typer.style(
                '`language` field not specified in docrunner.toml, please add it', fg=typer.colors.RED
            ),
            err=True
        )
        return
    
    typer.echo(
        typer.style(
            f'Running {options.language}',
            fg=LANGUAGE_TO_COLOR[options.language]
        )
    )
    LANGUAGE_TO_FUNCTION[options.language](
        options=options,
    )


@app.command()
def init():
    typer.echo(
        typer.style(
            'Creating configuration file',
            fg=typer.colors.GREEN,
        )
    )
    Options.create_config_file()

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
    """
    The python language command
    """

    typer.echo(
        typer.style(
            'Running python',
            fg=LANGUAGE_TO_COLOR['python']
        )
    )

    options = Options.override_with_cli_arguments(
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
    """
    The javascript language command
    """

    typer.echo(
        typer.style(
            'Running javascript',
            fg=LANGUAGE_TO_COLOR['javascript']
        )
    )

    options = Options.override_with_cli_arguments(
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
    """
    The typescript language command
    """
    typer.echo(
        typer.style(
            'Running typescript',
            fg=LANGUAGE_TO_COLOR['typescript']
        )
    )

    options = Options.override_with_cli_arguments(
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
    """
    The dart language command
    """

    typer.echo(
        typer.style(
            'Running dart',
            fg=LANGUAGE_TO_COLOR['dart']
        )
    )
    
    options = Options.override_with_cli_arguments(
        markdown_path=markdown_path,
        directory_path=directory_path,
        multi_file=multi_file,
    )
    run_dart(
        options=options,
    )

if __name__ == '__main__':
    app()
