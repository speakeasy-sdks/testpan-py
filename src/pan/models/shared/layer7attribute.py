"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Layer7Attribute:
    r"""Collection of layer 7 attributes"""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    values: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values') }})
    

