"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .topriskyserverlessfunction import TopRiskyServerlessFunction
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TopRiskyServerlessFunctionsWidget:
    top_risky_serverless_functions: Optional[List[TopRiskyServerlessFunction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topRiskyServerlessFunctions'), 'exclude': lambda f: f is None }})
    

