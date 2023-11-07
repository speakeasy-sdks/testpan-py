"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import cloudaccount as shared_cloudaccount
from typing import Optional


@dataclasses.dataclass
class PutCloudAccountsCloudAccountIDRequest:
    cloud_account: shared_cloudaccount.CloudAccountInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    cloud_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'cloudAccountId', 'style': 'simple', 'explode': False }})
    r"""cloud account ID"""
    



@dataclasses.dataclass
class PutCloudAccountsCloudAccountIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    cloud_account: Optional[shared_cloudaccount.CloudAccount] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

