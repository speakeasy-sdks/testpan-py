"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .apireconstructionstatus import APIReconstructionStatus
from .apireconstructiontype import APIReconstructionType
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Response:
    learning_duration_left: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('learningDurationLeft'), 'exclude': lambda f: f is None }})
    messages: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('messages'), 'exclude': lambda f: f is None }})
    status: Optional[APIReconstructionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of an ongoing API reconstruction phase."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIReconstructionResponse:
    response: Optional[Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response'), 'exclude': lambda f: f is None }})
    type: Optional[APIReconstructionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Status of an ongoing API reconstruction."""
    

