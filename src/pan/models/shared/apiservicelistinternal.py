"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apiserviceinternal as shared_apiserviceinternal
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIServiceListInternal:
    items: list[shared_apiserviceinternal.APIServiceInternal] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    
