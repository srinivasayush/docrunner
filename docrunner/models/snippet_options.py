import re
from typing import List, Optional

from pydantic import BaseModel


class SnippetOptions(BaseModel):
    ignore: Optional[bool] = False
    file_name: Optional[str]

    @classmethod
    def from_decorators(cls, decorators: List[str]):
        options = cls()

        if len(decorators) == 0:
            return options

        for decorator in decorators:
            decorator = decorator[4: len(decorator) - 3].strip()
            if decorator == 'docrunner.ignore':
                options.ignore = True

            if 'docrunner.file_name' in decorator:
                file_name = [str(result.replace('"', '')) for result in re.findall('".*"', decorator)][0]
                options.file_name = file_name
        
        return options
