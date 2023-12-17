"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .apiserviceprofilecompliance_simple import APIServiceProfileComplianceSimple
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIServiceComplianceSimple:
    compliant: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compliant') }})
    profilescompliance: List[APIServiceProfileComplianceSimple] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profilescompliance') }})
    

