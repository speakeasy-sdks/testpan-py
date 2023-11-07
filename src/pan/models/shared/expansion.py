"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .label import Label
from .workloadaddress import WorkloadAddress
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Expansion:
    r"""represent expansion object used in put method"""
    cluster_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    namespace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceId') }})
    workload_addresses: List[WorkloadAddress] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workloadAddresses') }})
    account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountName'), 'exclude': lambda f: f is None }})
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterName'), 'exclude': lambda f: f is None }})
    controller_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerEnabled'), 'exclude': lambda f: f is None }})
    controller_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerId'), 'exclude': lambda f: f is None }})
    controller_is_update_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerIsUpdateEnabled'), 'exclude': lambda f: f is None }})
    controller_last_active: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerLastActive'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The last time that the agent sent telemetries"""
    controller_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerStatus'), 'exclude': lambda f: f is None }})
    controller_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerVersion'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""unique Id"""
    instance_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instanceId'), 'exclude': lambda f: f is None }})
    labels: Optional[List[Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    should_send_metrics: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shouldSendMetrics'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExpansionInput:
    r"""represent expansion object used in put method"""
    cluster_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    namespace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceId') }})
    workload_addresses: List[WorkloadAddress] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workloadAddresses') }})
    controller_last_active: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controllerLastActive'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The last time that the agent sent telemetries"""
    labels: Optional[List[Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    should_send_metrics: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shouldSendMetrics'), 'exclude': lambda f: f is None }})
    

