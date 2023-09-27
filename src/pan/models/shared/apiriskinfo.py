"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apiservicetype as shared_apiservicetype
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import Optional

class APIRiskInfoServiceRisk(str, Enum):
    CRITICAL = 'CRITICAL'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIRiskInfo:
    service_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceId'), 'exclude': lambda f: f is None }})
    service_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceName'), 'exclude': lambda f: f is None }})
    service_risk: Optional[APIRiskInfoServiceRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceRisk'), 'exclude': lambda f: f is None }})
    service_type: Optional[shared_apiservicetype.APIServiceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serviceType'), 'exclude': lambda f: f is None }})
    r"""An `enum`eration."""
    

