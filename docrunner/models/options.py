from __future__ import annotations

import os
from typing import Optional

import toml
from pydantic import BaseModel

from ..utils.file import write_file


class Options(BaseModel):
    """Base model for docrunner options"""
    language: Optional[str] = None
    markdown_path: Optional[str] = None
    directory_path: Optional[str] = None
    startup_command: Optional[str] = None
    multi_file: Optional[bool] = False

    @classmethod
    def override_with_cli_arguments(
        cls,
        markdown_path: Optional[str] = None,
        directory_path: Optional[str] = None,
        startup_command: Optional[str] = None,
        multi_file: Optional[bool] = False,
    ) -> Options:
        options = cls.from_config_file()
        if options:
            if markdown_path:
                options.markdown_path = markdown_path
            if directory_path:
                options.directory_path = directory_path
            if startup_command:
                options.startup_command = startup_command
            if options.multi_file != multi_file:
                options.multi_file = multi_file
        else:
            options = cls(
                markdown_path=markdown_path,
                directory_path=directory_path,
                startup_command=startup_command,
                multi_file=multi_file
            )
        
        return options
        

    @classmethod
    def from_config_file(cls) -> Optional[Options]:
        """Gets options from `docrunner.toml` file if file exists

        Returns
        -------
        Optional[Options]
            Docrunner options if found in file
        """
        filepath = './docrunner.toml'
        if not os.path.exists(filepath):
            return
        else:
            configuration_file = open(filepath)
            configuration_lines = configuration_file.read()
            configuration_file.close()
            options_dict = toml.loads(configuration_lines)
            options_dict = options_dict['docrunner']
            options = cls(**options_dict)
            return options
    
    
    @staticmethod
    def create_config_file():
        options = Options(
            markdown_path='README.md',
            multi_file=False,
        )
        configuration_lines = toml.dumps({
            'docrunner': options.dict()
        })
        write_file(
            filepath='docrunner.toml',
            lines=configuration_lines,
            overwrite=False
        )
