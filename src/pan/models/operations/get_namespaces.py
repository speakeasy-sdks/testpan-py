"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from ..shared import namespace as shared_namespace
from enum import Enum
from typing import List, Optional

class GetNamespacesProtectionStatus(str, Enum):
    r"""When true, the API will return only protected pods"""
    FULL = 'FULL'
    DEPLOYMENT_ONLY = 'DEPLOYMENT_ONLY'
    CONNECTION_ONLY = 'CONNECTION_ONLY'
    DISABLED = 'DISABLED'
    ALL = 'ALL'

class GetNamespacesSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetNamespacesSortKey(str, Enum):
    r"""the namespaces sort key"""
    NAMESPACE_NAME = 'namespaceName'
    CLUSTER_NAME = 'clusterName'
    RUNNING_PODS = 'runningPods'
    PROTECTION_STATUS = 'protectionStatus'


@dataclasses.dataclass
class GetNamespacesRequest:
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clusterName', 'style': 'form', 'explode': True }})
    r"""the cluster name to filter by"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    namespace_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespaceName', 'style': 'form', 'explode': True }})
    r"""the namespace name to filter by"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    protection_status: Optional[GetNamespacesProtectionStatus] = dataclasses.field(default=GetNamespacesProtectionStatus.ALL, metadata={'query_param': { 'field_name': 'protectionStatus', 'style': 'form', 'explode': True }})
    r"""When true, the API will return only protected pods"""
    sort_dir: Optional[GetNamespacesSortDir] = dataclasses.field(default=GetNamespacesSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetNamespacesSortKey] = dataclasses.field(default=GetNamespacesSortKey.NAMESPACE_NAME, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""the namespaces sort key"""
    



@dataclasses.dataclass
class GetNamespacesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    namespaces: Optional[List[shared_namespace.Namespace]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

