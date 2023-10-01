"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import apisecurityapistatus as shared_apisecurityapistatus
from ..shared import apisecurityriskseverity as shared_apisecurityriskseverity
from ..shared import apiserviceclientworkload as shared_apiserviceclientworkload
from ..shared import apiservicecompliance_simple as shared_apiservicecompliance_simple
from ..shared import apiservicescore as shared_apiservicescore
from ..shared import fuzzingstatus as shared_fuzzingstatus
from ..shared import gateway as shared_gateway
from ..shared import openapispecavailability as shared_openapispecavailability
from ..shared import vulnerabilitiessummary as shared_vulnerabilitiessummary
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIServiceInternal:
    identifier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifier') }})
    r"""Unique identifier of the subject API as assigned by Crankshaft"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""API name (for external) or destination workload (for internal)"""
    client_workloads: Optional[list[shared_apiserviceclientworkload.APIServiceClientWorkload]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientWorkloads'), 'exclude': lambda f: f is None }})
    cluster: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster'), 'exclude': lambda f: f is None }})
    compliance: Optional[shared_apiservicecompliance_simple.APIServiceComplianceSimple] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compliance'), 'exclude': lambda f: f is None }})
    creation_timestamp: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creation_timestamp'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Textual description of the Service"""
    fuzzing_end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingEndTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    fuzzing_start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStartTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    fuzzing_status: Optional[shared_fuzzingstatus.FuzzingStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStatus'), 'exclude': lambda f: f is None }})
    r"""An enumeration."""
    fuzzing_status_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fuzzingStatusMessage'), 'exclude': lambda f: f is None }})
    gateway_info: Optional[shared_gateway.Gateway] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gatewayInfo'), 'exclude': lambda f: f is None }})
    last_update: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_update'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    link_doc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_doc'), 'exclude': lambda f: f is None }})
    r"""Location of the documentation. This can be an URL for example"""
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    openapi_spec_availablity: Optional[shared_openapispecavailability.OpenAPISpecAvailability] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openapi_spec_availablity'), 'exclude': lambda f: f is None }})
    port: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    risk: Optional[shared_apisecurityriskseverity.APISecurityRiskSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk'), 'exclude': lambda f: f is None }})
    r"""An `enum`eration."""
    score: Optional[shared_apiservicescore.APIServiceScore] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    status: Optional[shared_apisecurityapistatus.APISecurityAPIStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Api status enumeration."""
    status_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_description'), 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[shared_vulnerabilitiessummary.VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    
