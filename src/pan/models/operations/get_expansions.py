"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import expansion as shared_expansion
from enum import Enum
from typing import Optional

class GetExpansionsSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetExpansionsSortKey(str, Enum):
    r"""sort key"""
    NAME = 'name'



@dataclasses.dataclass
class GetExpansionsRequest:
    sort_key: GetExpansionsSortKey = dataclasses.field(metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clusterName', 'style': 'form', 'explode': True }})
    r"""Filter expansions by cluster name"""
    controller_status: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'controllerStatus', 'style': 'form', 'explode': True }})
    r"""Filter the clusters by controller status"""
    controller_version: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'controllerVersion', 'style': 'form', 'explode': True }})
    r"""Filter the clusters by controller version"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    max_results: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter expansions by name"""
    namespace_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'namespaceName', 'style': 'form', 'explode': True }})
    r"""Filter expansions by namespace"""
    no_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'noPagination', 'style': 'form', 'explode': True }})
    r"""When true, the pagination params will be ignored"""
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetExpansionsSortDir] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    




@dataclasses.dataclass
class GetExpansionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    expansions: Optional[list[shared_expansion.Expansion]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

