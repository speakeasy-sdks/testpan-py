"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gateway as shared_gateway
from typing import Optional


@dataclasses.dataclass
class PutGatewaysGatewayIDRequest:
    gateway: shared_gateway.Gateway = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    gateway_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'gatewayId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutGatewaysGatewayIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    gateway: Optional[shared_gateway.Gateway] = dataclasses.field(default=None)
    r"""Token was gateway."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

