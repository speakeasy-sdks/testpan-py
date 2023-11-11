"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import cdpolicy as shared_cdpolicy
from ...models.shared import cdpolicy_input as shared_cdpolicy_input
from typing import Optional


@dataclasses.dataclass
class PutCdPolicyPolicyIDRequest:
    cd_policy: shared_cdpolicy_input.CdPolicyInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    policy_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'policyId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutCdPolicyPolicyIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    cd_policy: Optional[shared_cdpolicy.CdPolicy] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

