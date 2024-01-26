"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .mitretechniqueaffectedelement import MitreTechniqueAffectedElement
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MitreTechniqueInfo:
    affected_elements: Optional[List[MitreTechniqueAffectedElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('affectedElements'), 'exclude': lambda f: f is None }})
    affected_techniques: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('affectedTechniques'), 'exclude': lambda f: f is None }})
    explanation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('explanation'), 'exclude': lambda f: f is None }})
    fix_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fixDescription'), 'exclude': lambda f: f is None }})
    how_to_fix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('howToFix'), 'exclude': lambda f: f is None }})
    is_fix_avilable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isFixAvilable'), 'exclude': lambda f: f is None }})
    

