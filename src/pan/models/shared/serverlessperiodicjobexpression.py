"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils

class ServerlessPeriodicJobExpressionPeriodicJobType(str, Enum):
    SERVERLESS_BY_HOURS_PERIODIC_JOB_EXPRESSION = 'ServerlessByHoursPeriodicJobExpression'
    SERVERLESS_BY_DAYS_PERIODIC_JOB_EXPRESSION = 'ServerlessByDaysPeriodicJobExpression'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ServerlessPeriodicJobExpression:
    periodic_job_type: ServerlessPeriodicJobExpressionPeriodicJobType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PeriodicJobType') }})
    
