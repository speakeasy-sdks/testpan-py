"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiservicefuzzingprogress as shared_apiservicefuzzingprogress
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDFuzzingStatusRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDFuzzingStatusResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_service_fuzzing_progress: Optional[shared_apiservicefuzzingprogress.APIServiceFuzzingProgress] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

