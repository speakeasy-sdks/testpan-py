"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .operationsdiffsdonutpiechart import OperationsDiffsDonutPieChart
from .specsdonutpiechart import SpecsDonutPieChart
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SpecsAndOperationsDiffsWidget:
    operations_diffs: Optional[OperationsDiffsDonutPieChart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operationsDiffs'), 'exclude': lambda f: f is None }})
    specs: Optional[SpecsDonutPieChart] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('specs'), 'exclude': lambda f: f is None }})
    

