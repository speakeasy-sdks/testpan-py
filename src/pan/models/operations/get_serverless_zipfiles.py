"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverlesszip as shared_serverlesszip
from enum import Enum
from typing import List, Optional

class GetServerlessZipFilesQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetServerlessZipFilesQueryParamSortKey(str, Enum):
    r"""sort key"""
    TIME = 'TIME'
    VULNERABILITIES = 'VULNERABILITIES'


@dataclasses.dataclass
class GetServerlessZipFilesRequest:
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetServerlessZipFilesQueryParamSortDir] = dataclasses.field(default=GetServerlessZipFilesQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetServerlessZipFilesQueryParamSortKey] = dataclasses.field(default=GetServerlessZipFilesQueryParamSortKey.VULNERABILITIES, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    zip_name_filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'zipNameFilter', 'style': 'form', 'explode': True }})
    zip_sha256_filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'zipSha256Filter', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetServerlessZipFilesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_serverlesszip.ServerlessZip]] = dataclasses.field(default=None)
    r"""Success"""
    

