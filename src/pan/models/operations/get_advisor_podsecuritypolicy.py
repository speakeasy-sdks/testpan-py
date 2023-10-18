"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import podsecuritypolicyrecommendationperiod as shared_podsecuritypolicyrecommendationperiod
from typing import List, Optional


@dataclasses.dataclass
class GetAdvisorPodSecurityPolicyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    pod_security_policy_recommendation_periods: Optional[List[shared_podsecuritypolicyrecommendationperiod.PodSecurityPolicyRecommendationPeriod]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

