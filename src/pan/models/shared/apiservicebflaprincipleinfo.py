"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIServiceBflaPrincipleInfo:
    ip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    principle_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('principleType') }})
    

