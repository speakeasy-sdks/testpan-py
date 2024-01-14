"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .podtemplatedifftype import PodTemplateDiffType
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PodTemplateDiff:
    diff_type: Optional[PodTemplateDiffType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('diffType'), 'exclude': lambda f: f is None }})
    old_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oldValue'), 'exclude': lambda f: f is None }})
    r"""The old value in the path. Will only be populated with MODIFIED type"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""The path of the added/deleted/modified object in the pod (example: spec.volumes.0.name)"""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    r"""The current value in the path"""
    

