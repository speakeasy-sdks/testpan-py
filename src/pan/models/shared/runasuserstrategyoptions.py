"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .idrange import IDRange
from .runasuserstrategy import RunAsUserStrategy
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RunAsUserStrategyOptions:
    ranges: Optional[List[IDRange]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ranges'), 'exclude': lambda f: f is None }})
    rule: Optional[RunAsUserStrategy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule'), 'exclude': lambda f: f is None }})
    

