"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverlessdefaultrule as shared_serverlessdefaultrule
from ..shared import serverlessruleaction as shared_serverlessruleaction
from ..shared import serverlessuserrule as shared_serverlessuserrule
from ..shared import serverlessviolationreason as shared_serverlessviolationreason
from ..shared import unidentifiedserverlessrule as shared_unidentifiedserverlessrule
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerlessViolationInfo:
    default_rule: Optional[shared_serverlessdefaultrule.ServerlessDefaultRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultRule'), 'exclude': lambda f: f is None }})
    rule_action: Optional[shared_serverlessruleaction.ServerlessRuleAction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleAction'), 'exclude': lambda f: f is None }})
    r"""serverless rule action"""
    unidentified_serverless_rule: Optional[shared_unidentifiedserverlessrule.UnidentifiedServerlessRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unidentifiedServerlessRule'), 'exclude': lambda f: f is None }})
    user_rule: Optional[shared_serverlessuserrule.ServerlessUserRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRule'), 'exclude': lambda f: f is None }})
    r"""used for violation in ServerlessFunction"""
    violation_reasons: Optional[List[shared_serverlessviolationreason.ServerlessViolationReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violationReasons'), 'exclude': lambda f: f is None }})
    

