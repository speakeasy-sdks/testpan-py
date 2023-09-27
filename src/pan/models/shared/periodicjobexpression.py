"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils

class PeriodicJobExpressionPeriodicJobType(str, Enum):
    NON_PERIODIC_JOB_EXPRESSION = 'NonPeriodicJobExpression'
    SINGLE_PERIODIC_JOB_EXPRESSION = 'SinglePeriodicJobExpression'
    BY_HOURS_PERIODIC_JOB_EXPRESSION = 'ByHoursPeriodicJobExpression'
    BY_DAYS_PERIODIC_JOB_EXPRESSION = 'ByDaysPeriodicJobExpression'
    WEEKLY_PERIODIC_JOB_EXPRESSION = 'WeeklyPeriodicJobExpression'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PeriodicJobExpression:
    periodic_job_type: PeriodicJobExpressionPeriodicJobType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PeriodicJobType') }})
    

