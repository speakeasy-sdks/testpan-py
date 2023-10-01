"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deletedependencyelement as shared_deletedependencyelement
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TokenDeleteDependencies:
    deployment_rules: Optional[list[shared_deletedependencyelement.DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentRules'), 'exclude': lambda f: f is None }})
    
