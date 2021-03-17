import typer

from constants import (JAVASCRIPT_DIRECTORY_HELP, PY_ENVIRONMENT_HELP,
                       PY_RUN_HELP)
from languages.javascript import run_javascript
from languages.python import run_python

app = typer.Typer()

@app.command()
def python(
    env_path: str = typer.Option(
        None,
        help=PY_ENVIRONMENT_HELP
    ),
    run_command: str = typer.Option(
        None,
        help=PY_RUN_HELP
    )
):  
    typer.echo(f'Running python code')
    run_python(
        env_path=env_path,
        run_command=run_command,
    )

@app.command()
def javascript(
    directory_path: str = typer.Option(
        None,
        help=JAVASCRIPT_DIRECTORY_HELP,
    )
):
    run_javascript(
        directory_path=directory_path,
    )



if __name__ == '__main__':
    app()
