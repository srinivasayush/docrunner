from typing import Any, Dict, List
import typer
from ..exceptions.base_exception import DocrunnerBaseException


def log_exception(exception: DocrunnerBaseException) -> None:
    typer.echo(
        typer.style(
            exception.get_message(),
            fg=exception.get_output_color()
        )
    )

def merge_dict_with_additions(dicts: List[Dict[Any, int]]) -> Dict[Any, int]:
    final_dict = {}
    for dictionary in dicts:
        for key in dictionary.keys():
            if key not in final_dict:
                final_dict[key] = dictionary[key]
            else:
                final_dict[key] += dictionary[key]

    return final_dict
