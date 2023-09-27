"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import Optional

class PostAdvisorRunPolicyAdvisorType(str, Enum):
    r"""policy advisor type"""
    ENVIRONMENT = 'ENVIRONMENT'
    POD_SECURITY_STANDARD = 'POD_SECURITY_STANDARD'
    CONNECTION_RULES = 'CONNECTION_RULES'
    DEPLOYMENT_RULES = 'DEPLOYMENT_RULES'
    API_RULES = 'API_RULES'



@dataclasses.dataclass
class PostAdvisorRunRequest:
    policy_advisor_type: PostAdvisorRunPolicyAdvisorType = dataclasses.field(metadata={'query_param': { 'field_name': 'policyAdvisorType', 'style': 'form', 'explode': True }})
    r"""policy advisor type"""
    




@dataclasses.dataclass
class PostAdvisorRunResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

