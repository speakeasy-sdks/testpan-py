"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import kubernetesauditlog as shared_kubernetesauditlog
from datetime import datetime
from enum import Enum
from typing import List, Optional

class Result(str, Enum):
    ALLOW = 'ALLOW'
    DETECT = 'DETECT'
    BLOCK = 'BLOCK'
    RISKY = 'RISKY'

class GetAuditLogsKubernetesQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAuditLogsKubernetesQueryParamSortKey(str, Enum):
    r"""sort key"""
    FIRST_SEEN = 'firstSeen'
    LAST_SEEN = 'lastSeen'
    ACTION = 'action'
    USER = 'user'
    TOTAL = 'total'


@dataclasses.dataclass
class GetAuditLogsKubernetesRequest:
    end_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'endTime', 'style': 'form', 'explode': True }})
    r"""End date of the query"""
    start_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'startTime', 'style': 'form', 'explode': True }})
    r"""Start date of the query"""
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clusterName', 'style': 'form', 'explode': True }})
    r"""the cluster name to filter by"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    kubernetes_audit_action: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'kubernetesAuditAction', 'style': 'form', 'explode': False }})
    r"""Kubernetes audit action"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    namespace_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespaceName', 'style': 'form', 'explode': True }})
    r"""the namespace name to filter by"""
    no_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'noPagination', 'style': 'form', 'explode': True }})
    r"""When true, the pagination params will be ignored"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    resource_kind: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'resourceKind', 'style': 'form', 'explode': True }})
    r"""Resource kind"""
    resource_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'resourceName', 'style': 'form', 'explode': True }})
    r"""Resource name"""
    result: Optional[List[Result]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'result', 'style': 'form', 'explode': False }})
    r"""event result filter"""
    sort_dir: Optional[GetAuditLogsKubernetesQueryParamSortDir] = dataclasses.field(default=GetAuditLogsKubernetesQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetAuditLogsKubernetesQueryParamSortKey] = dataclasses.field(default=GetAuditLogsKubernetesQueryParamSortKey.LAST_SEEN, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    user: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    r"""User name"""
    



@dataclasses.dataclass
class GetAuditLogsKubernetesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_kubernetesauditlog.KubernetesAuditLog]] = dataclasses.field(default=None)
    r"""Success"""
    

