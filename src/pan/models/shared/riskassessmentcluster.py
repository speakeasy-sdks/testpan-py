"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import dockerfilescanresultssummary as shared_dockerfilescanresultssummary
from ..shared import riskassessmentclusterscanconfig as shared_riskassessmentclusterscanconfig
from ..shared import riskassessmentscanstatus as shared_riskassessmentscanstatus
from ..shared import vulnerabilitiessummary as shared_vulnerabilitiessummary
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RiskAssessmentCluster:
    r"""Single cluster risk assessment"""
    cluster_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterId'), 'exclude': lambda f: f is None }})
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterName'), 'exclude': lambda f: f is None }})
    dockerfile_scan_results_summary: Optional[shared_dockerfilescanresultssummary.DockerfileScanResultsSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerfileScanResultsSummary'), 'exclude': lambda f: f is None }})
    r"""dockerfile scan results summary by severity"""
    has_failed: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasFailed'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    scan_config: Optional[shared_riskassessmentclusterscanconfig.RiskAssessmentClusterScanConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scanConfig'), 'exclude': lambda f: f is None }})
    r"""Single cluster risk assessment scan config"""
    scanned: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scanned'), 'exclude': lambda f: f is None }})
    status: Optional[shared_riskassessmentscanstatus.RiskAssessmentScanStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of a risk assessment scan"""
    time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total'), 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[shared_vulnerabilitiessummary.VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    
