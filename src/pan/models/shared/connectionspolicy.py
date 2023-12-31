"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectionsrule import ConnectionsRule
from .defaultconnectionrule import DefaultConnectionRule
from .directpodipconnectionrule import DirectPodIPConnectionRule
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionsPolicy:
    direct_pod_rule: DirectPodIPConnectionRule = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directPodRule') }})
    default_rule: Optional[DefaultConnectionRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultRule'), 'exclude': lambda f: f is None }})
    user_rules: Optional[List[ConnectionsRule]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRules'), 'exclude': lambda f: f is None }})
    

