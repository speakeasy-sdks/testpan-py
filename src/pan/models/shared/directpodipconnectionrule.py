"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import directpodipconnectionruleaction as shared_directpodipconnectionruleaction
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DirectPodIPConnectionRule:
    action: shared_directpodipconnectionruleaction.DirectPodIPConnectionRuleAction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    is_disabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDisabled'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

