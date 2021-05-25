from __future__ import annotations

import os
from typing import List, Optional

import toml
from pydantic import BaseModel

from ..utils.file import write_file


class Options(BaseModel):
    """Base model for docrunner options"""

    language: Optional[str]
    markdown_paths: Optional[List[str]] = ["README.md"]
    directory_path: Optional[str] = None
    startup_command: Optional[str] = None
    multi_file: Optional[bool] = False
    recursive: Optional[bool] = False

    @classmethod
    def override_with_cli_arguments(
        cls,
        language: str,
        markdown_path: Optional[str] = None,
        directory_path: Optional[str] = None,
        startup_command: Optional[str] = None,
        multi_file: Optional[bool] = None,
        recursive: Optional[bool] = None,
    ) -> Options:
        options = cls.from_config_file()
        if options:
            options.language = language
            if markdown_path:
                options.markdown_paths = [markdown_path]
            if directory_path:
                options.directory_path = directory_path
            if startup_command:
                options.startup_command = startup_command
            if multi_file is not None:
                options.multi_file = multi_file
            if recursive is not None:
                options.recursive = recursive

        else:
            # No config `docrunner.toml` file found
            options = cls(
                language=language,
                markdown_paths=[markdown_path] if markdown_path else ["README.md"],
                directory_path=directory_path,
                startup_command=startup_command,
                multi_file=multi_file if multi_file is not None else False,
                recursive=recursive if recursive is not None else False,
            )
        return options

    @classmethod
    def from_config_file(cls) -> Optional[Options]:
        """Gets options from `docrunner.toml` file if it exists

        Returns
        -------
        Optional[Options]
            Docrunner options if found in file
        """
        filepath = "./docrunner.toml"
        if not os.path.exists(filepath):
            return
        else:
            configuration_file = open(filepath)
            configuration_lines = configuration_file.read()
            configuration_file.close()
            options_dict = toml.loads(configuration_lines)
            options_dict = options_dict["docrunner"]
            options = cls(**options_dict)
            return options

    @classmethod
    def create_config_file(cls):
        """Creates a config `docrunner.toml` file with some default options"""
        options = cls(
            markdown_paths=["README.md"],
            multi_file=False,
        )
        configuration_lines = toml.dumps({"docrunner": options.dict()})
        write_file(
            filepath="docrunner.toml", content=configuration_lines, overwrite=False
        )
