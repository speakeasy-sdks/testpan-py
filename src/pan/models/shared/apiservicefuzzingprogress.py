"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import apifuzzingtestconfiguration as shared_apifuzzingtestconfiguration
from ..shared import fuzzingstatus as shared_fuzzingstatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIServiceFuzzingProgress:
    fuzzing_progress: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingProgress'), 'exclude': lambda f: f is None }})
    fuzzing_start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStartTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    fuzzing_status: Optional[shared_fuzzingstatus.FuzzingStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStatus'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    fuzzing_status_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStatusMessage'), 'exclude': lambda f: f is None }})
    test_configuration: Optional[shared_apifuzzingtestconfiguration.APIFuzzingTestConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('testConfiguration'), 'exclude': lambda f: f is None }})
    test_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('testId'), 'exclude': lambda f: f is None }})
    

