import typer
from ..exceptions.base_exception import DocrunnerBaseException


def log_exception(exception: DocrunnerBaseException) -> None:
    typer.echo(
        typer.style(
            exception.get_message(),
            fg=exception.get_output_color()
        )
    )
