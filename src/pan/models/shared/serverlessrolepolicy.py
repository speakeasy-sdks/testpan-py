"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverlesspolicyrisk as shared_serverlesspolicyrisk
from ..shared import serverlesspolicyriskreasons as shared_serverlesspolicyriskreasons
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerlessRolePolicy:
    policy_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyArn'), 'exclude': lambda f: f is None }})
    policy_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyName'), 'exclude': lambda f: f is None }})
    policy_risk: Optional[shared_serverlesspolicyrisk.ServerlessPolicyRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyRisk'), 'exclude': lambda f: f is None }})
    risk_reasons: Optional[List[shared_serverlesspolicyriskreasons.ServerlessPolicyRiskReasons]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('riskReasons'), 'exclude': lambda f: f is None }})
    

