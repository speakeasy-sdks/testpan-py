"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .container import Container
from .label import Label
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PodRuntimeInfo:
    r"""runtime info of the pod (if is a pod)"""
    containers: Optional[List[Container]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('containers'), 'exclude': lambda f: f is None }})
    r"""runtime pod containers"""
    init_containers: Optional[List[Container]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initContainers'), 'exclude': lambda f: f is None }})
    r"""runtime pod init containers"""
    labels: Optional[List[Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    r"""runtime pod labels"""
    

