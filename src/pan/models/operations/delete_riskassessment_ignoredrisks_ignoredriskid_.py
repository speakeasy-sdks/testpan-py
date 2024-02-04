"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http


@dataclasses.dataclass
class DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDRequest:
    ignored_risk_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ignoredRiskId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

