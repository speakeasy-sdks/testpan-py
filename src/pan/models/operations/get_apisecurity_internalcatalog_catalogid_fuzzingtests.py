"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiservicefuzzingtest as shared_apiservicefuzzingtest
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDFuzzingTestsRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDFuzzingTestsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_service_fuzzing_tests: Optional[list[shared_apiservicefuzzingtest.APIServiceFuzzingTest]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

