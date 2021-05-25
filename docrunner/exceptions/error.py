from typing import Literal

import typer

from ..exceptions.base_exception import DocrunnerBaseException


class DocrunnerError(DocrunnerBaseException):
    def get_message(self) -> str:
        return f"ERROR: {self.args[0]}"

    def get_output_color(self) -> Literal["red"]:
        return typer.colors.RED
