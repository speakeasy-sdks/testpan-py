"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import caintegrationrequest as shared_caintegrationrequest
from ...models.shared import caintegrationresponse as shared_caintegrationresponse
from typing import Optional


@dataclasses.dataclass
class PutSettingsIntegrationsCaIDRequest:
    ca_integration_request: shared_caintegrationrequest.CaIntegrationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutSettingsIntegrationsCaIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ca_integration_response: Optional[shared_caintegrationresponse.CaIntegrationResponse] = dataclasses.field(default=None)
    r"""Success"""
    

