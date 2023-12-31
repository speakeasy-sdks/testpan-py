"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .deletedependencyelement import DeleteDependencyElement
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISecurityPolicyDeleteDependencies:
    app_rules: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appRules'), 'exclude': lambda f: f is None }})
    cd_policy: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cdPolicy'), 'exclude': lambda f: f is None }})
    connection_rules: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionRules'), 'exclude': lambda f: f is None }})
    

