"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .additionalinfo import AdditionalInfo
from .apisecurityriskseverity import APISecurityRiskSeverity
from .countershistory import CountersHistory
from .riskconfidenceenum import RiskConfidenceEnum
from .risktrendenum import RiskTrendEnum
from .scorefindinggroup import ScoreFindingGroup
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CategoryScoreGrade:
    critical: ScoreFindingGroup = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('critical') }})
    high: ScoreFindingGroup = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('high') }})
    low: ScoreFindingGroup = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('low') }})
    medium: ScoreFindingGroup = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('medium') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    risk: APISecurityRiskSeverity = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk') }})
    r"""An `enum`eration."""
    scorer_version: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scorer_version') }})
    unclassified: ScoreFindingGroup = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unclassified') }})
    additional_info: Optional[List[AdditionalInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_info'), 'exclude': lambda f: f is None }})
    confidence: Optional[RiskConfidenceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    counters_history: Optional[CountersHistory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('counters_history'), 'exclude': lambda f: f is None }})
    trend: Optional[RiskTrendEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trend'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    

