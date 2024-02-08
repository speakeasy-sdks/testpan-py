"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiservicelistinternal as shared_apiservicelistinternal
from datetime import datetime
from enum import Enum
from typing import List, Optional

class GetAPISecurityInternalCatalogQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAPISecurityInternalCatalogQueryParamSortKey(str, Enum):
    r"""the Api Catalog sort key"""
    NAME = 'name'
    RISK = 'risk'


@dataclasses.dataclass
class GetAPISecurityInternalCatalogRequest:
    api_policy_profiles: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'apiPolicyProfiles', 'style': 'form', 'explode': False }})
    r"""Names of the Api Policy Profiles"""
    drill_down_score: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'drillDownScore', 'style': 'form', 'explode': True }})
    r"""Return associated score"""
    include_service_with_no_spec: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'includeServiceWithNoSpec', 'style': 'form', 'explode': True }})
    r"""When false, only services with specs wikk be returned"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""the Api Catalog name filter"""
    namespaces_filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespacesFilter', 'style': 'form', 'explode': True }})
    r"""namespace filter. a base 64 representation of a list of NamespacesFilter definition object"""
    no_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'noPagination', 'style': 'form', 'explode': True }})
    r"""When true, the pagination params will be ignored"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetAPISecurityInternalCatalogQueryParamSortDir] = dataclasses.field(default=GetAPISecurityInternalCatalogQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetAPISecurityInternalCatalogQueryParamSortKey] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""the Api Catalog sort key"""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updatedAfter', 'style': 'form', 'explode': True }})
    r"""Only Apis updated since this date"""
    



@dataclasses.dataclass
class GetAPISecurityInternalCatalogResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_service_list_internal: Optional[shared_apiservicelistinternal.APIServiceListInternal] = dataclasses.field(default=None)
    r"""Success"""
    

