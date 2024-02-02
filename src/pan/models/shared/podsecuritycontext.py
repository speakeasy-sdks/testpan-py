"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PodSecurityContext:
    fs_group: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fsGroup'), 'exclude': lambda f: f is None }})
    run_as_group: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runAsGroup'), 'exclude': lambda f: f is None }})
    run_as_non_root: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runAsNonRoot'), 'exclude': lambda f: f is None }})
    run_as_user: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runAsUser'), 'exclude': lambda f: f is None }})
    supplemental_groups: Optional[List[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplementalGroups'), 'exclude': lambda f: f is None }})
    

