"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import policyfiltersearchresponsepod as shared_policyfiltersearchresponsepod
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PolicyFilterSearchResponse:
    envs: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('envs'), 'exclude': lambda f: f is None }})
    pods: Optional[List[shared_policyfiltersearchresponsepod.PolicyFilterSearchResponsePod]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pods'), 'exclude': lambda f: f is None }})
    

