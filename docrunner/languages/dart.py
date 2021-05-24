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

    startup_command = options.startup_command

    try:
        code_filepaths = create_language_files(
            options=options,
        )

        if startup_command:
            startup_command = startup_command.replace('"', '')
            os.system(startup_command)
            return

        for filepath in list(code_filepaths.keys()):
            os.system(f'dart run {filepath}')

    except DocrunnerBaseException as error:
        log_exception(error)
