"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import label as shared_label
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NetworkExpansion:
    cluster: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster'), 'exclude': lambda f: f is None }})
    ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ids'), 'exclude': lambda f: f is None }})
    instance_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instanceId'), 'exclude': lambda f: f is None }})
    labels: Optional[List[shared_label.Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    namespace_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceId'), 'exclude': lambda f: f is None }})
    

