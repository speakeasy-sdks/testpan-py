"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiservicemethod as shared_apiservicemethod
from typing import List, Optional


@dataclasses.dataclass
class GetAPISecurityCatalogIDMethodsRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    tags: List[str] = dataclasses.field(metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': False }})
    r"""spec tags names"""
    



@dataclasses.dataclass
class GetAPISecurityCatalogIDMethodsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_apiservicemethod.APIServiceMethod]] = dataclasses.field(default=None)
    r"""Success"""
    

