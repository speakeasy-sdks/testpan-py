"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .apisecuritypolicycategoryconditions import APISecurityPolicyCategoryConditions
from .apisecuritypolicyglobalcondition import APISecurityPolicyGlobalCondition
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISecurityPolicyInput:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    category_conditions: Optional[APISecurityPolicyCategoryConditions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryConditions'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    global_condition: Optional[APISecurityPolicyGlobalCondition] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('globalCondition'), 'exclude': lambda f: f is None }})
    

