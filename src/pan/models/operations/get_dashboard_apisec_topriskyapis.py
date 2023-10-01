"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apisectopriskyapiswidget as shared_apisectopriskyapiswidget
from enum import Enum
from typing import Optional

class GetDashboardApisecTopRiskyApisAPISecSource(str, Enum):
    r"""source filter. an enum representing the source of the APIs service in scope"""
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'



@dataclasses.dataclass
class GetDashboardApisecTopRiskyApisRequest:
    api_sec_source: GetDashboardApisecTopRiskyApisAPISecSource = dataclasses.field(default=GetDashboardApisecTopRiskyApisAPISecSource.INTERNAL, metadata={'query_param': { 'field_name': 'apiSecSource', 'style': 'form', 'explode': True }})
    r"""source filter. an enum representing the source of the APIs service in scope"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    




@dataclasses.dataclass
class GetDashboardApisecTopRiskyApisResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_sec_top_risky_apis_widget: Optional[shared_apisectopriskyapiswidget.APISecTopRiskyApisWidget] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
