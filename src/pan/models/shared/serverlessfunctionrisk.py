"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverlessfunctionreason as shared_serverlessfunctionreason
from ..shared import serverlessfunctionrisklevel as shared_serverlessfunctionrisklevel
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerlessFunctionRisk:
    function_risk: Optional[shared_serverlessfunctionrisklevel.ServerlessFunctionRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('functionRisk'), 'exclude': lambda f: f is None }})
    reasons: Optional[List[shared_serverlessfunctionreason.ServerlessFunctionReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reasons'), 'exclude': lambda f: f is None }})
    

