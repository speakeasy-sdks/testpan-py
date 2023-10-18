"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apiservicecompliance_simple as shared_apiservicecompliance_simple
from ..shared import ipprotoenum as shared_ipprotoenum
from ..shared import urlschemeenum as shared_urlschemeenum
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIEndpoint:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""IP v4/v6 address of the API endpoint"""
    identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifier') }})
    r"""Unique id of the Endpoint"""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""Port of the API endpoint"""
    proto: shared_ipprotoenum.IPProtoEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('proto') }})
    r"""An enumeration."""
    api_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_id'), 'exclude': lambda f: f is None }})
    r"""API service this endpoint belongs to. Empty if still undetermined."""
    compliance: Optional[shared_apiservicecompliance_simple.APIServiceComplianceSimple] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compliance'), 'exclude': lambda f: f is None }})
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    r"""Hostname of the API endpoint if known"""
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    scheme: Optional[shared_urlschemeenum.URLSchemeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheme'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    

