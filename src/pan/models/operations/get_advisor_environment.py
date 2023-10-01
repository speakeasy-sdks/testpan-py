"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import environmentrecommendationperiod as shared_environmentrecommendationperiod
from typing import Optional



@dataclasses.dataclass
class GetAdvisorEnvironmentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    environment_recommendation_periods: Optional[list[shared_environmentrecommendationperiod.EnvironmentRecommendationPeriod]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
