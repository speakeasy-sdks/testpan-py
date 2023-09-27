"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import workloadrisklevel as shared_workloadrisklevel
from ..shared import workloadriskreason as shared_workloadriskreason
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WorkloadRisk:
    level: Optional[shared_workloadrisklevel.WorkloadRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    reasons: Optional[list[shared_workloadriskreason.WorkloadRiskReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reasons'), 'exclude': lambda f: f is None }})
    

