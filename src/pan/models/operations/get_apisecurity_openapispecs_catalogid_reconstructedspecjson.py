"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    download_as_json: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsJson', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an json file, and pagination will be ignored"""
    




@dataclasses.dataclass
class GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_api_security_open_api_specs_catalog_id_reconstructed_spec_json_200_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

