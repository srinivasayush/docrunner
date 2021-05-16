from typing import List

from pydantic import BaseModel

from ..models.snippet_options import SnippetOptions


class Snippet(BaseModel):
    code: str
    options: SnippetOptions

    @classmethod
    def new(cls, code: str, decorators: List[str]):
        return cls(
            code=code,
            options=SnippetOptions.from_decorators(decorators)
        )
