"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import apiresponse as errors_apiresponse
from ...models.shared import cloudaccountdeletedependencies as shared_cloudaccountdeletedependencies
from pan import utils
from typing import Optional


@dataclasses.dataclass
class GetCloudAccountsCloudAccountIDDeleteDependenciesRequest:
    cloud_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'cloudAccountId', 'style': 'simple', 'explode': False }})
    r"""cloud account ID"""
    



@dataclasses.dataclass
class GetCloudAccountsCloudAccountIDDeleteDependenciesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[errors_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    cloud_account_delete_dependencies: Optional[shared_cloudaccountdeletedependencies.CloudAccountDeleteDependencies] = dataclasses.field(default=None)
    r"""Success"""
    

