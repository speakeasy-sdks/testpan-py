"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DashboardTimeBasedGraphInfo:
    policy_update_times: Optional[list[datetime]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyUpdateTimes'), 'encoder': utils.list_encoder(True, utils.datetimeisoformat(False)), 'decoder': utils.list_decoder(dateutil.parser.isoparse), 'exclude': lambda f: f is None }})
    
