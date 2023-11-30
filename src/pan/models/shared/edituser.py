"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .role import Role
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import Optional

class EditUserStatus(str, Enum):
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EditUser:
    full_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullName') }})
    status: EditUserStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""ID of the user as created by Secure Application management."""
    role: Optional[Role] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    r"""The role of the user"""
    

