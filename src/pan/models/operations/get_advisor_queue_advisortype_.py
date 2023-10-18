"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import policyadvisorstate as shared_policyadvisorstate
from enum import Enum
from typing import Optional

class GetAdvisorQueueAdvisorTypeAdvisorType(str, Enum):
    ENVIRONMENT = 'ENVIRONMENT'
    POD_SECURITY_STANDARD = 'POD_SECURITY_STANDARD'
    CONNECTION_RULES = 'CONNECTION_RULES'
    DEPLOYMENT_RULES = 'DEPLOYMENT_RULES'
    API_RULES = 'API_RULES'


@dataclasses.dataclass
class GetAdvisorQueueAdvisorTypeRequest:
    advisor_type: GetAdvisorQueueAdvisorTypeAdvisorType = dataclasses.field(metadata={'path_param': { 'field_name': 'advisorType', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetAdvisorQueueAdvisorTypeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    policy_advisor_state: Optional[shared_policyadvisorstate.PolicyAdvisorState] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

