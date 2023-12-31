"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .cddeploymentinfo import CDDeploymentInfo
from .cddeploymentresource import CDDeploymentResource
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CdPipelineResourceResult:
    r"""CD resource results"""
    deployment_info: Optional[CDDeploymentInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentInfo'), 'exclude': lambda f: f is None }})
    resources: Optional[List[CDDeploymentResource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resources'), 'exclude': lambda f: f is None }})
    

