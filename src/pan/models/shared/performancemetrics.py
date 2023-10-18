"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import performancemetricsgraphpoint as shared_performancemetricsgraphpoint
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import List, Optional

class PerformanceMetricsConnectionProtocol(str, Enum):
    TCP_PERFORMANCE_METRICS = 'TcpPerformanceMetrics'
    HTTP_PERFORMANCE_METRICS = 'HttpPerformanceMetrics'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PerformanceMetrics:
    connection_protocol: Optional[PerformanceMetricsConnectionProtocol] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionProtocol'), 'exclude': lambda f: f is None }})
    total_received_bytes: Optional[List[shared_performancemetricsgraphpoint.PerformanceMetricsGraphPoint]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalReceivedBytes'), 'exclude': lambda f: f is None }})
    r"""Return a list of total received bytes per connection"""
    total_sent_bytes: Optional[List[shared_performancemetricsgraphpoint.PerformanceMetricsGraphPoint]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalSentBytes'), 'exclude': lambda f: f is None }})
    r"""Return a list of total sent bytes per connection"""
    

