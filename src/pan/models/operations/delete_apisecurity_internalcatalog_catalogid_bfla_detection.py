"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_api_security_internal_catalog_catalog_id_bfla_detection_204_application_json_uuid_string: Optional[str] = dataclasses.field(default=None)
    r"""Stopped"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

