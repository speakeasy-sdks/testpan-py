"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import podsecuritypolicy as shared_podsecuritypolicy
from typing import List, Optional


@dataclasses.dataclass
class PostPodSecurityPolicyProfilesBatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_podsecuritypolicy.PodSecurityPolicy]] = dataclasses.field(default=None)
    r"""Added"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

