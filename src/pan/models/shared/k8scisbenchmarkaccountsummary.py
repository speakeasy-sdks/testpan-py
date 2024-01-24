"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class K8sCISBenchmarkAccountSummary:
    compliance: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compliance'), 'exclude': lambda f: f is None }})
    number_of_clusters: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfClusters'), 'exclude': lambda f: f is None }})
    number_of_clusters_with_action_items: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfClustersWithActionItems'), 'exclude': lambda f: f is None }})
    number_of_scanned_clusters: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfScannedClusters'), 'exclude': lambda f: f is None }})
    

