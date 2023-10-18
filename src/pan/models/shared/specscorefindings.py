"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import specscorefindingslist as shared_specscorefindingslist
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SpecScoreFindings:
    critical: Optional[shared_specscorefindingslist.SpecScoreFindingsList] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('critical'), 'exclude': lambda f: f is None }})
    high: Optional[shared_specscorefindingslist.SpecScoreFindingsList] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('high'), 'exclude': lambda f: f is None }})
    low: Optional[shared_specscorefindingslist.SpecScoreFindingsList] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('low'), 'exclude': lambda f: f is None }})
    medium: Optional[shared_specscorefindingslist.SpecScoreFindingsList] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('medium'), 'exclude': lambda f: f is None }})
    unclassified: Optional[shared_specscorefindingslist.SpecScoreFindingsList] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unclassified'), 'exclude': lambda f: f is None }})
    

