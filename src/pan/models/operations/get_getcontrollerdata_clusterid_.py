"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import apiresponse as errors_apiresponse
from ...models.shared import controllerdataresponse as shared_controllerdataresponse
from pan import utils
from typing import Optional


@dataclasses.dataclass
class GetGetControllerDataClusterIDRequest:
    cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clusterId', 'style': 'simple', 'explode': False }})
    r"""Portshift cluster ID"""
    



@dataclasses.dataclass
class GetGetControllerDataClusterIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[errors_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    controller_data_response: Optional[shared_controllerdataresponse.ControllerDataResponse] = dataclasses.field(default=None)
    r"""Success"""
    

