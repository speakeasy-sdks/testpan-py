"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import backgroundjobresponse as shared_backgroundjobresponse
from typing import Optional


@dataclasses.dataclass
class GetNetworkMapQueueRequestIDRequest:
    request_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'requestId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetNetworkMapQueueRequestIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    background_job_response: Optional[shared_backgroundjobresponse.BackgroundJobResponse] = dataclasses.field(default=None)
    r"""Success"""
    

