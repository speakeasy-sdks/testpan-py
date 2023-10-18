"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import graphnumberpoint as shared_graphnumberpoint
from ..shared import pricingdetails as shared_pricingdetails
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UsageAndPricing:
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    pods_usage_graph: Optional[List[shared_graphnumberpoint.GraphNumberPoint]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podsUsageGraph'), 'exclude': lambda f: f is None }})
    pricing_details: Optional[shared_pricingdetails.PricingDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pricingDetails'), 'exclude': lambda f: f is None }})
    vcpus_usage_graph: Optional[List[shared_graphnumberpoint.GraphNumberPoint]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vcpusUsageGraph'), 'exclude': lambda f: f is None }})
    

