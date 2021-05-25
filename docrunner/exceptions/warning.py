from typing import Literal

import typer

from ..exceptions.base_exception import DocrunnerBaseException


class DocrunnerWarning(DocrunnerBaseException):
    def get_message(self) -> str:
        return f"WARNING: {self.args[0]}"

    def get_output_color(self) -> Literal["yellow"]:
        return typer.colors.YELLOW
