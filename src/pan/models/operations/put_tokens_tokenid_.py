"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import token as shared_token
from typing import Optional


@dataclasses.dataclass
class PutTokensTokenIDRequest:
    token: shared_token.Token = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    token_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tokenId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutTokensTokenIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    token: Optional[shared_token.Token] = dataclasses.field(default=None)
    r"""Token was edited."""
    

