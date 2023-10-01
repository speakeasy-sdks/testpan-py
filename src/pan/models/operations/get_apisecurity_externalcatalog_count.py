"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from datetime import datetime
from typing import Optional



@dataclasses.dataclass
class GetAPISecurityExternalCatalogCountRequest:
    include_service_with_no_spec: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'includeServiceWithNoSpec', 'style': 'form', 'explode': True }})
    r"""When false, only services with specs wikk be returned"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""the Api Catalog name filter"""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updatedAfter', 'style': 'form', 'explode': True }})
    r"""Only Apis updated since this date"""
    




@dataclasses.dataclass
class GetAPISecurityExternalCatalogCountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_api_security_external_catalog_count_200_application_json_integer: Optional[int] = dataclasses.field(default=None)
    r"""Number of APIs in the inventory"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
