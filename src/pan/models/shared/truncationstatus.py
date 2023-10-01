"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TruncationStatus:
    is_truncation_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isTruncationEnabled') }})
    r"""is truncation enabled."""
    truncate_time_in_days: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('truncateTimeInDays') }})
    r"""truncation interval, in days."""
    
