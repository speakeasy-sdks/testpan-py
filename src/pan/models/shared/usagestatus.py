"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UsageStatus:
    r"""Account resource usage status"""
    current_clusters_usage: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentClustersUsage'), 'exclude': lambda f: f is None }})
    current_nodes_usage: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentNodesUsage'), 'exclude': lambda f: f is None }})
    max_clusters: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxClusters'), 'exclude': lambda f: f is None }})
    max_nodes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxNodes'), 'exclude': lambda f: f is None }})
    
