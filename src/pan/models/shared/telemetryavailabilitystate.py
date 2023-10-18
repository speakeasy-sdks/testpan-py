"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import telemetrystatestatus as shared_telemetrystatestatus
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TelemetryAvailabilityState:
    status: Optional[shared_telemetrystatestatus.TelemetryStateStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    status_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusReason'), 'exclude': lambda f: f is None }})
    r"""will be populate only when status is unhealthy"""
    

