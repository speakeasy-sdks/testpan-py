"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import environment as shared_environment
from typing import List, Optional


@dataclasses.dataclass
class GetEnvironmentsEnvIDRequest:
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetEnvironmentsEnvIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_environment.Environment]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

