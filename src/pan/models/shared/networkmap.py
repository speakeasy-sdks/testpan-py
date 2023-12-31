"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .networkapp import NetworkApp
from .networkconnection import NetworkConnection
from .networkenvironment import NetworkEnvironment
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NetworkMap:
    apps: Optional[List[NetworkApp]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apps'), 'exclude': lambda f: f is None }})
    connections: Optional[List[NetworkConnection]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connections'), 'exclude': lambda f: f is None }})
    environments: Optional[List[NetworkEnvironment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environments'), 'exclude': lambda f: f is None }})
    

