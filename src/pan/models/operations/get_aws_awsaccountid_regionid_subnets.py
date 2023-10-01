"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import portshiftawssubnet as shared_portshiftawssubnet
from typing import Optional



@dataclasses.dataclass
class GetAwsAwsAccountIDRegionIDSubnetsRequest:
    aws_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'awsAccountId', 'style': 'simple', 'explode': False }})
    r"""AWS account Id"""
    region_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'regionId', 'style': 'simple', 'explode': False }})
    r"""AWS region Id"""
    




@dataclasses.dataclass
class GetAwsAwsAccountIDRegionIDSubnetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    portshift_aws_subnets: Optional[list[shared_portshiftawssubnet.PortshiftAwsSubnet]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
