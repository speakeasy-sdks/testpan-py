"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import environment as shared_environment
from enum import Enum
from typing import Optional

class GetEnvironmentsSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetEnvironmentsSortKey(str, Enum):
    r"""Environment sort key"""
    NAME = 'name'



@dataclasses.dataclass
class GetEnvironmentsRequest:
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    include_system_envs: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeSystemEnvs', 'style': 'form', 'explode': True }})
    r"""include systems environments"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter environments by name"""
    sort_dir: Optional[GetEnvironmentsSortDir] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetEnvironmentsSortKey] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""Environment sort key"""
    




@dataclasses.dataclass
class GetEnvironmentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    environments: Optional[list[shared_environment.Environment]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

