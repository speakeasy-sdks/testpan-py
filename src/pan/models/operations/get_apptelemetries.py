"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apptelemetry as shared_apptelemetry
from datetime import datetime
from enum import Enum
from typing import List, Optional

class QueryParamProtectionStatus(str, Enum):
    r"""When true, the API will return only protected pods"""
    FULL = 'FULL'
    DEPLOYMENT_ONLY = 'DEPLOYMENT_ONLY'
    CONNECTION_ONLY = 'CONNECTION_ONLY'
    DISABLED = 'DISABLED'
    ALL = 'ALL'

class GetAppTelemetriesQueryParamResult(str, Enum):
    ALLOW = 'ALLOW'
    DETECT = 'DETECT'
    BLOCK = 'BLOCK'

class GetAppTelemetriesQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAppTelemetriesQueryParamSortKey(str, Enum):
    r"""sort key"""
    APP_NAME = 'appName'
    APP_TYPE = 'appType'
    EXECUTABLE = 'executable'
    ENVIRONMENT_NAME = 'environmentName'
    RISK = 'risk'
    STATUS = 'status'
    START_TIME = 'startTime'
    FINISH_TIME = 'finishTime'
    WORKLOAD_RISK = 'workloadRisk'

class WorkloadRisks(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'


@dataclasses.dataclass
class GetAppTelemetriesRequest:
    end_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'endTime', 'style': 'form', 'explode': True }})
    r"""End date of the query"""
    sort_key: GetAppTelemetriesQueryParamSortKey = dataclasses.field(metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    start_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'startTime', 'style': 'form', 'explode': True }})
    r"""Start date of the query"""
    app_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'appName', 'style': 'form', 'explode': False }})
    r"""Defined App name"""
    app_type: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'appType', 'style': 'form', 'explode': False }})
    r"""Empty string means no filtering. \\"UNDEFINED\\" means telemetries with no App type"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    environment_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'environmentName', 'style': 'form', 'explode': False }})
    r"""Empty string means no filtering. \\"UNDEFINED\\" means telemetries with no App type"""
    executable: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'executable', 'style': 'form', 'explode': False }})
    hide_internals: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'hideInternals', 'style': 'form', 'explode': True }})
    r"""When true, the API will filter out \\"OS Internal\\" and \\"User OS Internal\\" App types"""
    highest_dockerfile_scan_result: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'highestDockerfileScanResult', 'style': 'form', 'explode': False }})
    r"""Highest DockerfileScan Result"""
    host: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'host', 'style': 'form', 'explode': False }})
    r"""Defined host name"""
    images_id: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'imagesId', 'style': 'form', 'explode': False }})
    r"""Array of images id"""
    is_identified: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'isIdentified', 'style': 'form', 'explode': True }})
    r"""app is identified filter"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    namespaces_filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespacesFilter', 'style': 'form', 'explode': True }})
    r"""namespace filter. a base 64 representation of a list of NamespacesFilter definition object"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    protection_status: Optional[QueryParamProtectionStatus] = dataclasses.field(default=QueryParamProtectionStatus.ALL, metadata={'query_param': { 'field_name': 'protectionStatus', 'style': 'form', 'explode': True }})
    r"""When true, the API will return only protected pods"""
    result: Optional[List[GetAppTelemetriesQueryParamResult]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'result', 'style': 'form', 'explode': False }})
    r"""app result filter"""
    show_only_entries_with_app_name: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'showOnlyEntriesWithAppName', 'style': 'form', 'explode': True }})
    r"""When true, the telemetries API will only return entries with the App name"""
    show_only_violations: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'showOnlyViolations', 'style': 'form', 'explode': True }})
    r"""When true, the API will only return entries that violate the active policy"""
    show_system_pods: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'showSystemPods', 'style': 'form', 'explode': True }})
    r"""When true, the telemetries API will also return workloads that are part of the Kubernetes system"""
    sort_dir: Optional[GetAppTelemetriesQueryParamSortDir] = dataclasses.field(default=GetAppTelemetriesQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    status: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': False }})
    r"""App status"""
    vulnerability_levels_filter: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'vulnerabilityLevelsFilter', 'style': 'form', 'explode': False }})
    r"""Highest vulnerability"""
    workload_risks: Optional[List[WorkloadRisks]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workloadRisks', 'style': 'form', 'explode': False }})
    r"""workloadRisk filter"""
    



@dataclasses.dataclass
class GetAppTelemetriesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_apptelemetry.AppTelemetry]] = dataclasses.field(default=None)
    r"""Success"""
    

