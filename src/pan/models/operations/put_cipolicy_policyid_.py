"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import cipolicy as shared_cipolicy
from typing import Optional


@dataclasses.dataclass
class PutCiPolicyPolicyIDRequest:
    ci_policy: shared_cipolicy.CiPolicyInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    policy_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'policyId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutCiPolicyPolicyIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ci_policy: Optional[shared_cipolicy.CiPolicy] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

