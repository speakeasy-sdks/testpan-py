"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiservicedrilldowninternal as shared_apiservicedrilldowninternal
from typing import List, Optional


@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalogId', 'style': 'simple', 'explode': False }})
    api_policy_profiles: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'apiPolicyProfiles', 'style': 'form', 'explode': False }})
    r"""Names of the Api Policy Profiles"""
    download_as_json: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsJson', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an json file, and pagination will be ignored"""
    



@dataclasses.dataclass
class GetAPISecurityInternalCatalogCatalogIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_service_drill_down_internal: Optional[shared_apiservicedrilldowninternal.APIServiceDrillDownInternal] = dataclasses.field(default=None)
    r"""Success"""
    

