"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import periodicjobexpression as shared_periodicjobexpression
from ..shared import vulnerabilityseverity as shared_vulnerabilityseverity
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RiskAssessmentClusterScanConfig:
    r"""Single cluster risk assessment scan config"""
    max_parallelism: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxParallelism') }})
    minimum_severity: shared_vulnerabilityseverity.VulnerabilitySeverity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minimumSeverity') }})
    namespaces: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaces'), 'exclude': lambda f: f is None }})
    periodic_job_expression: Optional[shared_periodicjobexpression.PeriodicJobExpression] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('periodicJobExpression'), 'exclude': lambda f: f is None }})
    run_dockerfile_scan: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runDockerfileScan'), 'exclude': lambda f: f is None }})
    
