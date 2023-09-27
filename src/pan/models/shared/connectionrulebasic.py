"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connectionruleaction as shared_connectionruleaction
from ..shared import connectionruleorigin as shared_connectionruleorigin
from ..shared import networkconnectionruletype as shared_networkconnectionruletype
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ConnectionRuleBasic:
    action: shared_connectionruleaction.ConnectionRuleAction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""ENCRYPT is not allowed in default rule"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    group_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupName'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    is_rule_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRuleActive'), 'exclude': lambda f: f is None }})
    rule_origin: Optional[shared_connectionruleorigin.ConnectionRuleOrigin] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleOrigin'), 'exclude': lambda f: f is None }})
    rule_type: Optional[shared_networkconnectionruletype.NetworkConnectionRuleType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleType'), 'exclude': lambda f: f is None }})
    

