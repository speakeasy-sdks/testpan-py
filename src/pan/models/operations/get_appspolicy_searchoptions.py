"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import policyfiltersearchresponse as shared_policyfiltersearchresponse
from typing import Optional


@dataclasses.dataclass
class GetAppsPolicySearchOptionsRequest:
    name_filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'nameFilter', 'style': 'form', 'explode': True }})
    r"""the pod/env name to filter by."""
    



@dataclasses.dataclass
class GetAppsPolicySearchOptionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    policy_filter_search_response: Optional[shared_policyfiltersearchresponse.PolicyFilterSearchResponse] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

