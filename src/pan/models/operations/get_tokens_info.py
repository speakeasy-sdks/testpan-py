"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apitokeninfo as shared_apitokeninfo
from typing import Optional



@dataclasses.dataclass
class GetTokensInfoRequest:
    tokens_ids: list[str] = dataclasses.field(metadata={'query_param': { 'field_name': 'tokensIds', 'style': 'form', 'explode': False }})
    




@dataclasses.dataclass
class GetTokensInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_token_infos: Optional[list[shared_apitokeninfo.APITokenInfo]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

