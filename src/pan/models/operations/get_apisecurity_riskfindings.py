"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import riskfindings as shared_riskfindings
from enum import Enum
from typing import List, Optional

class APISecSource(str, Enum):
    r"""source filter. an enum representing the source of the APIs service in scope"""
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'

class Risks(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'
    ALL = 'ALL'

class GetAPISecurityRiskFindingsQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAPISecurityRiskFindingsQueryParamSortKey(str, Enum):
    r"""Risk finding sort key."""
    NAME = 'NAME'
    RISK = 'RISK'


@dataclasses.dataclass
class GetAPISecurityRiskFindingsRequest:
    api_sec_source: APISecSource = dataclasses.field(default=APISecSource.INTERNAL, metadata={'query_param': { 'field_name': 'apiSecSource', 'style': 'form', 'explode': True }})
    r"""source filter. an enum representing the source of the APIs service in scope"""
    category: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'category', 'style': 'form', 'explode': True }})
    r"""Category of the risk finding"""
    detected: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'detected', 'style': 'form', 'explode': True }})
    r"""Show finding with detect elements only"""
    element: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'element', 'style': 'form', 'explode': True }})
    r"""Affected element of the risk finding"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Name of the risk finding name"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    risks: Optional[List[Risks]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'risks', 'style': 'form', 'explode': False }})
    r"""The API risk filter"""
    sort_dir: Optional[GetAPISecurityRiskFindingsQueryParamSortDir] = dataclasses.field(default=GetAPISecurityRiskFindingsQueryParamSortDir.DESC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: GetAPISecurityRiskFindingsQueryParamSortKey = dataclasses.field(default=GetAPISecurityRiskFindingsQueryParamSortKey.RISK, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""Risk finding sort key."""
    source: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'source', 'style': 'form', 'explode': True }})
    r"""Source of the risk finding"""
    



@dataclasses.dataclass
class GetAPISecurityRiskFindingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    risk_findings: Optional[shared_riskfindings.RiskFindings] = dataclasses.field(default=None)
    r"""Success"""
    

