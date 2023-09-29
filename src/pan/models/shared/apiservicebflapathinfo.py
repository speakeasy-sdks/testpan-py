"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apiservicebflaclientinfo as shared_apiservicebflaclientinfo
from ..shared import httpmethod as shared_httpmethod
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIServiceBflaPathInfo:
    method: shared_httpmethod.HTTPMethod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path') }})
    clients: Optional[list[shared_apiservicebflaclientinfo.APIServiceBflaClientInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clients'), 'exclude': lambda f: f is None }})
    is_legitimate: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isLegitimate'), 'exclude': lambda f: f is None }})
    

