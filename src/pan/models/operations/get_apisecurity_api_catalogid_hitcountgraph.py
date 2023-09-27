"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiservicespecpathhitcountgraphpoint as shared_apiservicespecpathhitcountgraphpoint
from enum import Enum
from typing import Optional

class GetAPISecurityAPICatalogIDHitCountGraphSpecPathMethod(str, Enum):
    r"""spec path method"""
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    HEAD = 'HEAD'
    CONNECT = 'CONNECT'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'
    PATCH = 'PATCH'



@dataclasses.dataclass
class GetAPISecurityAPICatalogIDHitCountGraphRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    spec_path: str = dataclasses.field(metadata={'query_param': { 'field_name': 'specPath', 'style': 'form', 'explode': True }})
    r"""spec path"""
    spec_path_method: GetAPISecurityAPICatalogIDHitCountGraphSpecPathMethod = dataclasses.field(metadata={'query_param': { 'field_name': 'specPathMethod', 'style': 'form', 'explode': True }})
    r"""spec path method"""
    hours_interval: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'hoursInterval', 'style': 'form', 'explode': True }})
    r"""hours interval"""
    




@dataclasses.dataclass
class GetAPISecurityAPICatalogIDHitCountGraphResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_service_spec_path_hit_count_graph: Optional[list[shared_apiservicespecpathhitcountgraphpoint.APIServiceSpecPathHitCountGraphPoint]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

