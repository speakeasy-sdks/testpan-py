"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import enforcementoption as shared_enforcementoption
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISecurityCdPolicyElement:
    api_security_profile: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiSecurityProfile') }})
    r"""The allowed api security profile for the pipeline"""
    enforcement_option: shared_enforcementoption.EnforcementOption = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enforcementOption') }})
    

