"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import openapispecscorestatus as shared_openapispecscorestatus
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    open_api_spec_score_status: Optional[shared_openapispecscorestatus.OpenAPISpecScoreStatus] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

