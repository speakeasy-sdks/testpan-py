"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apisecurityriskseverity as shared_apisecurityriskseverity
from ..shared import fuzzingmethod as shared_fuzzingmethod
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FuzzingTestTag:
    methods: Optional[list[shared_fuzzingmethod.FuzzingMethod]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('methods'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    severity: Optional[shared_apisecurityriskseverity.APISecurityRiskSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""An `enum`eration."""
    
