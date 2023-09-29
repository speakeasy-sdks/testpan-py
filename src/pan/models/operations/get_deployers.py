"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deployer as shared_deployer
from enum import Enum
from typing import Optional

class GetDeployersSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetDeployersSortKey(str, Enum):
    r"""sort key"""
    DEPLOYER = 'deployer'
    TYPE = 'type'



@dataclasses.dataclass
class GetDeployersRequest:
    sort_key: GetDeployersSortKey = dataclasses.field(metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter deployers by name"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    rule_creation: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ruleCreation', 'style': 'form', 'explode': True }})
    r"""Filter deployers by rule creation"""
    security_check: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'securityCheck', 'style': 'form', 'explode': True }})
    r"""Filter deployers by security checks"""
    sort_dir: Optional[GetDeployersSortDir] = dataclasses.field(default=GetDeployersSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    




@dataclasses.dataclass
class GetDeployersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    deployers: Optional[list[shared_deployer.Deployer]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

