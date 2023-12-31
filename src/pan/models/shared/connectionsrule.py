"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectionruleaction import ConnectionRuleAction
from .connectionruleorigin import ConnectionRuleOrigin
from .connectionrulepart import ConnectionRulePart
from .layer7settingspart import Layer7SettingsPart
from .networkconnectionruletype import NetworkConnectionRuleType
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import Optional

class ConnectionsRuleStatus(str, Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'
    DELETED = 'DELETED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionsRule:
    r"""A rule that states what Apps are allowed to communicate with each other."""
    action: ConnectionRuleAction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""ENCRYPT is not allowed in default rule"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    destination: Optional[ConnectionRulePart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination'), 'exclude': lambda f: f is None }})
    group_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupName'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    is_rule_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRuleActive'), 'exclude': lambda f: f is None }})
    layer7_settings: Optional[Layer7SettingsPart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layer7Settings'), 'exclude': lambda f: f is None }})
    rule_origin: Optional[ConnectionRuleOrigin] = dataclasses.field(default=ConnectionRuleOrigin.USER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleOrigin'), 'exclude': lambda f: f is None }})
    rule_type: Optional[NetworkConnectionRuleType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleType'), 'exclude': lambda f: f is None }})
    source: Optional[ConnectionRulePart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    status: Optional[ConnectionsRuleStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

