"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import label as shared_label
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class App:
    executable: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executable') }})
    r"""The name of the executable."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The unique name of the App (as it will appear in the Secure Application UI)."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the App."""
    args: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('args'), 'exclude': lambda f: f is None }})
    r"""The command line arguments of the executable."""
    cwd: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cwd'), 'exclude': lambda f: f is None }})
    r"""The working directory of the executable."""
    executable_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executablePath'), 'exclude': lambda f: f is None }})
    r"""The directory of the executable."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    labels: Optional[List[shared_label.Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    r"""pods that match one of the given labels"""
    process_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processName'), 'exclude': lambda f: f is None }})
    r"""The process name."""
    

