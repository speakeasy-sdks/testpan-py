"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apisecurityriskseverity as shared_apisecurityriskseverity
from ..shared import httpmethod as shared_httpmethod
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIServiceMethod:
    method: shared_httpmethod.HTTPMethod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path') }})
    risk: shared_apisecurityriskseverity.APISecurityRiskSeverity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk') }})
    r"""An `enum`eration."""
    tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag') }})
    
