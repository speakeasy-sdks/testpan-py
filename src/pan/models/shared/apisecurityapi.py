"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISecurityAPI:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""API name, usually an FQDN as determined by crankshaft, it can be logical or can correspond to one of the endpoints where the API is reachable, i.e. api.webex.com"""
    

