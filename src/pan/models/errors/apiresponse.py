"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIResponse(Exception):
    r"""An object that is return in all cases of failures."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
