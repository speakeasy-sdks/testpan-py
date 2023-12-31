"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .scorefinding import ScoreFinding
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScoreFindingGroup:
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    findings: List[ScoreFinding] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('findings') }})
    

