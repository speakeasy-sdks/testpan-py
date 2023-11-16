"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .singlebar import SingleBar
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkloadVulnerabilitiesWidget:
    bars: Optional[List[SingleBar]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bars'), 'exclude': lambda f: f is None }})
    total_vulnerable_images: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalVulnerableImages'), 'exclude': lambda f: f is None }})
    total_vulnerable_pods: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalVulnerablePods'), 'exclude': lambda f: f is None }})
    

