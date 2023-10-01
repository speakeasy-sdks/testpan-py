"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apireconstructedspec as shared_apireconstructedspec
from typing import Optional



@dataclasses.dataclass
class PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveRequest:
    api_reconstructed_spec_input: shared_apireconstructedspec.APIReconstructedSpecInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
