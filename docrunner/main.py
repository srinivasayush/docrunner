from constants import ENVIRONMENT_HELP, RUN_HELP
import typer
from languages.python import run_python

app = typer.Typer()

@app.command()
def python(
    env_path: str = typer.Option(
        None,
        help=ENVIRONMENT_HELP
    ),
    run_command: str = typer.Option(
        None,
        help=RUN_HELP
    )
):  
    typer.echo(f'Running python code')
    run_python(env_path=env_path, run_command=run_command)

@app.command()
def javascript(
):
    typer.echo('javascript command')



if __name__ == '__main__':
    app()
