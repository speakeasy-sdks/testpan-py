"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gatewayclusterinfo as shared_gatewayclusterinfo
from enum import Enum
from typing import List, Optional

class GetGatewaysClustersGatewayType(str, Enum):
    APIGEE_X = 'APIGEE_X'
    KONG_INTERNAL = 'KONG_INTERNAL'
    TYK_INTERNAL = 'TYK_INTERNAL'
    F5_BIG_IP = 'F5_BIG_IP'


@dataclasses.dataclass
class GetGatewaysClustersRequest:
    gateway_type: GetGatewaysClustersGatewayType = dataclasses.field(metadata={'query_param': { 'field_name': 'gatewayType', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetGatewaysClustersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    gateway_cluster_infos: Optional[List[shared_gatewayclusterinfo.GatewayClusterInfo]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

