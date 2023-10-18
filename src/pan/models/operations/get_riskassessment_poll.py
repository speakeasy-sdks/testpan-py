"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import riskassessmentcluster as shared_riskassessmentcluster
from typing import List, Optional


@dataclasses.dataclass
class GetRiskAssessmentPollRequest:
    risk_assessment_poll_key: List[str] = dataclasses.field(metadata={'query_param': { 'field_name': 'riskAssessmentPollKey', 'style': 'form', 'explode': False }})
    r"""The ids of the clusters whose scans to poll"""
    



@dataclasses.dataclass
class GetRiskAssessmentPollResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    risk_assessment_clusters: Optional[List[shared_riskassessmentcluster.RiskAssessmentCluster]] = dataclasses.field(default=None)
    r"""Success"""
    

