"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .imagelayer import ImageLayer
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ImageLayers:
    r"""image layers"""
    safe_layers: Optional[List[ImageLayer]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('safeLayers'), 'exclude': lambda f: f is None }})
    vulnerable_layers: Optional[List[ImageLayer]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerableLayers'), 'exclude': lambda f: f is None }})
    

