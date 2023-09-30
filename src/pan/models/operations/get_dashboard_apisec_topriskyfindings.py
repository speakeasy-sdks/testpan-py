"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apisectopriskyfindingswidget as shared_apisectopriskyfindingswidget
from enum import Enum
from typing import Optional

class GetDashboardApisecTopRiskyFindingsAPISecSource(str, Enum):
    r"""source filter. an enum representing the source of the APIs service in scope"""
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'



@dataclasses.dataclass
class GetDashboardApisecTopRiskyFindingsRequest:
    api_sec_source: GetDashboardApisecTopRiskyFindingsAPISecSource = dataclasses.field(default=GetDashboardApisecTopRiskyFindingsAPISecSource.INTERNAL, metadata={'query_param': { 'field_name': 'apiSecSource', 'style': 'form', 'explode': True }})
    r"""source filter. an enum representing the source of the APIs service in scope"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    




@dataclasses.dataclass
class GetDashboardApisecTopRiskyFindingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_sec_top_risky_findings_widget: Optional[shared_apisectopriskyfindingswidget.APISecTopRiskyFindingsWidget] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

