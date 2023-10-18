"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attackvector as shared_attackvector
from ..shared import cvssrisklevel as shared_cvssrisklevel
from ..shared import scope as shared_scope
from ..shared import userinteraction as shared_userinteraction
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cvss:
    attack_complexity: Optional[shared_cvssrisklevel.CvssRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attackComplexity'), 'exclude': lambda f: f is None }})
    attack_vector: Optional[shared_attackvector.AttackVector] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attackVector'), 'exclude': lambda f: f is None }})
    availability_impact: Optional[shared_cvssrisklevel.CvssRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availabilityImpact'), 'exclude': lambda f: f is None }})
    confidentiality_impact: Optional[shared_cvssrisklevel.CvssRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidentialityImpact'), 'exclude': lambda f: f is None }})
    integrity_impact: Optional[shared_cvssrisklevel.CvssRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrityImpact'), 'exclude': lambda f: f is None }})
    privileges_required: Optional[shared_cvssrisklevel.CvssRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('privilegesRequired'), 'exclude': lambda f: f is None }})
    scope: Optional[shared_scope.Scope] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope'), 'exclude': lambda f: f is None }})
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    user_interaction: Optional[shared_userinteraction.UserInteraction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userInteraction'), 'exclude': lambda f: f is None }})
    

