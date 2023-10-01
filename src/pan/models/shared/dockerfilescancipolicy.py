"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dockerfilescanseverity as shared_dockerfilescanseverity
from ..shared import enforcementoption as shared_enforcementoption
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DockerfileScanCiPolicy:
    enforcement_option: shared_enforcementoption.EnforcementOption = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enforcementOption') }})
    permissible_dockerfile_scan_severity: shared_dockerfilescanseverity.DockerfileScanSeverity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permissibleDockerfileScanSeverity') }})
    
