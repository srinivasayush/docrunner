import os

from ..exceptions.base_exception import DocrunnerBaseException
from ..models.options import Options
from ..utils.general import log_exception
from ..utils.language import create_language_files


def run_dart(
    options: Options
):
    """Runs all dart code within a markdown '.md' file

    Parameters
    ----------
    options : Options
        Docrunner options
    """

    try:
        code_filepaths = create_language_files(
            options=options,
        )

        for filepath in code_filepaths:
            os.system(f'dart run {filepath}')

    except DocrunnerBaseException as error:
        log_exception(error)
