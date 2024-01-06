"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIProviderBase:
    identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifier') }})
    r"""Unique id of the subject API as assigned by Crankshaft"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the provider, typically an FQDN"""
    industry: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('industry'), 'exclude': lambda f: f is None }})
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    

