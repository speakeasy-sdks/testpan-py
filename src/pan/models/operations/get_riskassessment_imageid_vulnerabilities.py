"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import riskassessmentvulnerability as shared_riskassessmentvulnerability
from enum import Enum
from typing import Final, Optional

class GetRiskAssessmentImageIDVulnerabilitiesSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'



@dataclasses.dataclass
class GetRiskAssessmentImageIDVulnerabilitiesRequest:
    image_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'imageId', 'style': 'simple', 'explode': False }})
    r"""The id of the risk assessment image"""
    SORT_KEY: Final[str] = dataclasses.field(default='SEVERITY', metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""risk assessment image sort key."""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetRiskAssessmentImageIDVulnerabilitiesSortDir] = dataclasses.field(default=GetRiskAssessmentImageIDVulnerabilitiesSortDir.DESC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    




@dataclasses.dataclass
class GetRiskAssessmentImageIDVulnerabilitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    risk_assessment_vulnerabilities: Optional[list[shared_riskassessmentvulnerability.RiskAssessmentVulnerability]] = dataclasses.field(default=None)
    r"""Success"""
    

