"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .k8scisbenchmarkscanstate import K8sCisBenchmarkScanState
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class K8sCISBenchmarkClustersSummary:
    agent_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agentActive'), 'exclude': lambda f: f is None }})
    compliance: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compliance'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    number_of_action_items: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfActionItems'), 'exclude': lambda f: f is None }})
    number_of_info_items: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfInfoItems'), 'exclude': lambda f: f is None }})
    number_of_items_failed: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfItemsFailed'), 'exclude': lambda f: f is None }})
    number_of_items_passed: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfItemsPassed'), 'exclude': lambda f: f is None }})
    number_of_nodes: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfNodes'), 'exclude': lambda f: f is None }})
    number_of_scanned_nodes: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfScannedNodes'), 'exclude': lambda f: f is None }})
    orchestration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orchestration'), 'exclude': lambda f: f is None }})
    scan_state: Optional[K8sCisBenchmarkScanState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scanState'), 'exclude': lambda f: f is None }})
    scan_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scanTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

