"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import cdpipelineresultstatus as shared_cdpipelineresultstatus
from ..shared import cdpipelinesecurityfinding as shared_cdpipelinesecurityfinding
from ..shared import cdresult as shared_cdresult
from ..shared import deploymentsource as shared_deploymentsource
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CDDeploymentInfo:
    deployment_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentName'), 'exclude': lambda f: f is None }})
    deployment_source: Optional[shared_deploymentsource.DeploymentSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentSource'), 'exclude': lambda f: f is None }})
    deployment_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentVersion'), 'exclude': lambda f: f is None }})
    policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyId'), 'exclude': lambda f: f is None }})
    policy_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyName'), 'exclude': lambda f: f is None }})
    result: Optional[shared_cdresult.CDResult] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    security_finding: Optional[list[shared_cdpipelinesecurityfinding.CDPipelineSecurityFinding]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityFinding'), 'exclude': lambda f: f is None }})
    status: Optional[shared_cdpipelineresultstatus.CDPipelineResultStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

