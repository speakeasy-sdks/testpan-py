"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .appprocessinfo import AppProcessInfo
from .appruntimeinfo import AppRuntimeInfo
from .dockerfilescanseverity import DockerfileScanSeverity
from .expansiontelemetryinfo import ExpansionTelemetryInfo
from .podidentification import PodIdentification
from .podruntimeinfo import PodRuntimeInfo
from .podspecinfo import PodSpecInfo
from .podtelemetryinfo import PodTelemetryInfo
from .telemetrystate import TelemetryState
from .tokeninjectionstatus import TokenInjectionStatus
from .unprotectedpodreason import UnprotectedPodReason
from .violationinfo import ViolationInfo
from .vulnerabilityseverity import VulnerabilitySeverity
from .workloadrisk import WorkloadRisk
from .workloadrisklevel import WorkloadRiskLevel
from .workloadtype import WorkloadType
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cluster:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppTelemetryEnvironment:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppTelemetryInstance:
    agent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agentId'), 'exclude': lambda f: f is None }})
    cloud_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cloudAccountId'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppTelemetryNamespace:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    labels: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Network:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppTelemetry:
    r"""Single telemetry entry"""
    app: Optional[AppProcessInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app'), 'exclude': lambda f: f is None }})
    r"""app info and process info for connection and App telemetries"""
    app_runtime_info: Optional[AppRuntimeInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appRuntimeInfo'), 'exclude': lambda f: f is None }})
    r"""runtime info of the App (if it is an App)"""
    cluster: Optional[Cluster] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster'), 'exclude': lambda f: f is None }})
    environment: Optional[AppTelemetryEnvironment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    expansion: Optional[ExpansionTelemetryInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expansion'), 'exclude': lambda f: f is None }})
    highest_dockerfile_scan_result: Optional[DockerfileScanSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highestDockerfileScanResult'), 'exclude': lambda f: f is None }})
    highest_security_context_risk: Optional[WorkloadRiskLevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highestSecurityContextRisk'), 'exclude': lambda f: f is None }})
    highest_vulnerability: Optional[VulnerabilitySeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highestVulnerability'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    instance: Optional[AppTelemetryInstance] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance'), 'exclude': lambda f: f is None }})
    is_pod_protected: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isPodProtected'), 'exclude': lambda f: f is None }})
    is_public_facing: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isPublicFacing'), 'exclude': lambda f: f is None }})
    namespace: Optional[AppTelemetryNamespace] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    network: Optional[Network] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('network'), 'exclude': lambda f: f is None }})
    pod: Optional[PodTelemetryInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pod'), 'exclude': lambda f: f is None }})
    pod_identification: Optional[PodIdentification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podIdentification'), 'exclude': lambda f: f is None }})
    pod_runtime_info: Optional[PodRuntimeInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podRuntimeInfo'), 'exclude': lambda f: f is None }})
    r"""runtime info of the pod (if is a pod)"""
    pod_spec_info: Optional[PodSpecInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podSpecInfo'), 'exclude': lambda f: f is None }})
    r"""pod spec attributes which are potentially risky"""
    pods_licenses: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podsLicenses'), 'exclude': lambda f: f is None }})
    r"""Licenses in use by the docker images. this field will be populated only in the drill down api"""
    risk: Optional[WorkloadRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk'), 'exclude': lambda f: f is None }})
    securecn_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securecnId'), 'exclude': lambda f: f is None }})
    state: Optional[TelemetryState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""Status of a telemetry entry"""
    telemetry_uid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telemetryUid'), 'exclude': lambda f: f is None }})
    r"""the kubernetes uid"""
    telemetry_uids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('telemetryUids'), 'exclude': lambda f: f is None }})
    token_injection_status: Optional[TokenInjectionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokenInjectionStatus'), 'exclude': lambda f: f is None }})
    unprotected_reasons: Optional[List[UnprotectedPodReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unprotectedReasons'), 'exclude': lambda f: f is None }})
    violation: Optional[ViolationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violation'), 'exclude': lambda f: f is None }})
    r"""If the the App is running on an environment on which it is not allowed to run, this object contains the rule it violated."""
    workload_type: Optional[WorkloadType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workloadType'), 'exclude': lambda f: f is None }})
    

