"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import trustedsigner as shared_trustedsigner
from typing import Optional


@dataclasses.dataclass
class PutTrustedSignersTrustedSignerIDRequest:
    trusted_signer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'trustedSignerId', 'style': 'simple', 'explode': False }})
    trusted_signer_input: shared_trustedsigner.TrustedSignerInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutTrustedSignersTrustedSignerIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

