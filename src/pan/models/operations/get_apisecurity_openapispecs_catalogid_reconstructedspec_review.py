"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apireconstructedspec as shared_apireconstructedspec
from typing import Optional


@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_reconstructed_spec: Optional[shared_apireconstructedspec.APIReconstructedSpec] = dataclasses.field(default=None)
    r"""Success"""
    

