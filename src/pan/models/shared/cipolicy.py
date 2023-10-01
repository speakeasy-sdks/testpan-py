"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dockerfilescancipolicy as shared_dockerfilescancipolicy
from ..shared import vulnerabilitycipolicy as shared_vulnerabilitycipolicy
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CiPolicyInput:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    dockerfile_scan_ci_policy: Optional[shared_dockerfilescancipolicy.DockerfileScanCiPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerfileScanCiPolicy'), 'exclude': lambda f: f is None }})
    vulnerability_ci_policy: Optional[shared_vulnerabilitycipolicy.VulnerabilityCiPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilityCiPolicy'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CiPolicy:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    dockerfile_scan_ci_policy: Optional[shared_dockerfilescancipolicy.DockerfileScanCiPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerfileScanCiPolicy'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    vulnerability_ci_policy: Optional[shared_vulnerabilitycipolicy.VulnerabilityCiPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilityCiPolicy'), 'exclude': lambda f: f is None }})
    
