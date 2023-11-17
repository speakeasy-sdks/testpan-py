"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperationsDiffsDonutPieChart:
    general_diffs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generalDiffs'), 'exclude': lambda f: f is None }})
    operations_without_diffs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operationsWithoutDiffs'), 'exclude': lambda f: f is None }})
    shadow_diffs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shadowDiffs'), 'exclude': lambda f: f is None }})
    total_operations: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalOperations'), 'exclude': lambda f: f is None }})
    zombie_diffs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zombieDiffs'), 'exclude': lambda f: f is None }})
    

