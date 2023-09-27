"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverlessruleaction as shared_serverlessruleaction
from ..shared import serverlessruleorigin as shared_serverlessruleorigin
from ..shared import serverlessrulescope as shared_serverlessrulescope
from ..shared import serverlessrulestatus as shared_serverlessrulestatus
from ..shared import serverlessruletype as shared_serverlessruletype
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ServerlessRule:
    r"""A rule that states what serverless function are allowed and where."""
    action: shared_serverlessruleaction.ServerlessRuleAction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""serverless rule action"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    rule: shared_serverlessruletype.ServerlessRuleType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rule') }})
    r"""identify the serverless functions matching type. Only one of the below should be not null, and  used."""
    status: shared_serverlessrulestatus.ServerlessRuleStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    group_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groupName'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    rule_origin: Optional[shared_serverlessruleorigin.ServerlessRuleOrigin] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleOrigin'), 'exclude': lambda f: f is None }})
    scope: Optional[list[shared_serverlessrulescope.ServerlessRuleScope]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope'), 'exclude': lambda f: f is None }})
    

