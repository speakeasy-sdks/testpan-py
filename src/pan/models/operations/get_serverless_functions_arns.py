"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverlessfunctionarns as shared_serverlessfunctionarns
from typing import List, Optional


@dataclasses.dataclass
class GetServerlessFunctionsArnsRequest:
    cloud_account_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cloudAccountName', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by name"""
    func_arn: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'funcArn', 'style': 'form', 'explode': False }})
    r"""Defined function ARN"""
    region: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'region', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by region"""
    



@dataclasses.dataclass
class GetServerlessFunctionsArnsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_serverlessfunctionarns.ServerlessFunctionArns]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

