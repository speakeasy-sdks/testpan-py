"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .deletedependencyelement import DeleteDependencyElement
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDependencyDeployerElement:
    cd_policies: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cdPolicies'), 'exclude': lambda f: f is None }})
    deployers: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployers'), 'exclude': lambda f: f is None }})
    

