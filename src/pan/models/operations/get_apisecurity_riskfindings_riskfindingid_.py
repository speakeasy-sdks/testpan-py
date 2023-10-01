"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import riskfinding as shared_riskfinding
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityRiskFindingsRiskFindingIDRequest:
    risk_finding_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'riskFindingId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetAPISecurityRiskFindingsRiskFindingIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    risk_finding: Optional[shared_riskfinding.RiskFinding] = dataclasses.field(default=None)
    r"""Success"""
    
