"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import app as shared_app
from enum import Enum
from typing import List, Optional

class GetAppsQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAppsQueryParamSortKey(str, Enum):
    r"""App sort key"""
    NAME = 'name'
    TYPE = 'type'


@dataclasses.dataclass
class GetAppsRequest:
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter Apps by name"""
    no_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'noPagination', 'style': 'form', 'explode': True }})
    r"""When true, the pagination params will be ignored"""
    sort_dir: Optional[GetAppsQueryParamSortDir] = dataclasses.field(default=GetAppsQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetAppsQueryParamSortKey] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""App sort key"""
    type: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': False }})
    r"""Filter Apps by type"""
    



@dataclasses.dataclass
class GetAppsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_app.App]] = dataclasses.field(default=None)
    r"""Created"""
    

