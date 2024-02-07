"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverlessfunctionnames as shared_serverlessfunctionnames
from typing import List, Optional


@dataclasses.dataclass
class GetServerlessFunctionsNamesRequest:
    cloud_account_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cloudAccountName', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by name"""
    func_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'funcName', 'style': 'form', 'explode': False }})
    r"""Defined function name"""
    region: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'region', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by region"""
    



@dataclasses.dataclass
class GetServerlessFunctionsNamesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_serverlessfunctionnames.ServerlessFunctionNames]] = dataclasses.field(default=None)
    r"""Success"""
    

