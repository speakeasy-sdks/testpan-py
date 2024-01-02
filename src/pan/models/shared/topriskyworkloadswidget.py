"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .topriskyworkload import TopRiskyWorkload
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TopRiskyWorkloadsWidget:
    top_risky_workloads: Optional[List[TopRiskyWorkload]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topRiskyWorkloads'), 'exclude': lambda f: f is None }})
    

