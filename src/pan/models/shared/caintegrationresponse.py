"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CaIntegrationResponse:
    certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificate') }})
    issuer_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issuerName') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    issuer_namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issuerNamespace'), 'exclude': lambda f: f is None }})
    

