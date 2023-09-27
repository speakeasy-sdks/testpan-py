"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import expansion as shared_expansion
from ..shared import expansionput as shared_expansionput
from typing import Optional



@dataclasses.dataclass
class PutExpansionsExpansionIDRequest:
    expansion_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'expansionId', 'style': 'simple', 'explode': False }})
    expansion_put: shared_expansionput.ExpansionPut = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PutExpansionsExpansionIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    expansion: Optional[shared_expansion.Expansion] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

