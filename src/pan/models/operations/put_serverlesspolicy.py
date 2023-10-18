"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import serverlesspolicy as shared_serverlesspolicy
from typing import Optional


@dataclasses.dataclass
class PutServerlessPolicyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    serverless_policy: Optional[shared_serverlesspolicy.ServerlessPolicy] = dataclasses.field(default=None)
    r"""Success"""
    

