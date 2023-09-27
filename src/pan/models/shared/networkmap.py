"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import networkapp as shared_networkapp
from ..shared import networkconnection as shared_networkconnection
from ..shared import networkenvironment as shared_networkenvironment
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class NetworkMap:
    apps: Optional[list[shared_networkapp.NetworkApp]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apps'), 'exclude': lambda f: f is None }})
    connections: Optional[list[shared_networkconnection.NetworkConnection]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connections'), 'exclude': lambda f: f is None }})
    environments: Optional[list[shared_networkenvironment.NetworkEnvironment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environments'), 'exclude': lambda f: f is None }})
    

