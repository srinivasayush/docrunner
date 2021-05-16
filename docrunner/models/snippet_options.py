from typing import List, Optional

from pydantic import BaseModel


class SnippetOptions(BaseModel):
    ignore: Optional[bool] = False

    @classmethod
    def from_decorators(cls, decorators: List[str]):
        if len(decorators) == 0:
            return cls()
        
        options = cls()
        for decorator in decorators:
            if decorator == '<!--docrunner.ignore-->':
                options.ignore = True
        
        return options
