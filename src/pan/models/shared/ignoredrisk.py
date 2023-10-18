"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import workloadriskreasontype as shared_workloadriskreasontype
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import List, Optional

class IgnoredRiskIgnoredRiskType(str, Enum):
    CLUSTER_IGNORED_RISK = 'ClusterIgnoredRisk'
    ANY_CLUSTER_IGNORED_RISK = 'AnyClusterIgnoredRisk'
    ANY_ENVIRONMENT_IGNORED_RISK = 'AnyEnvironmentIgnoredRisk'
    ENVIRONMENT_IGNORED_RISK = 'EnvironmentIgnoredRisk'
    WORKLOAD_IGNORED_RISK = 'WorkloadIgnoredRisk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IgnoredRisk:
    r"""represent ignore risk object"""
    ignored_risk_type: IgnoredRiskIgnoredRiskType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignoredRiskType') }})
    workload_risks_type: List[shared_workloadriskreasontype.WorkloadRiskReasonType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workloadRisksType') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    

