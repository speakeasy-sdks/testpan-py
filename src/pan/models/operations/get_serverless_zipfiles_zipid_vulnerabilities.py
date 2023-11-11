"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import vulnerability as shared_vulnerability
from enum import Enum
from typing import List, Optional

class GetServerlessZipFilesZipIDVulnerabilitiesQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetServerlessZipFilesZipIDVulnerabilitiesRequest:
    zip_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'zipId', 'style': 'simple', 'explode': False }})
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetServerlessZipFilesZipIDVulnerabilitiesQueryParamSortDir] = dataclasses.field(default=GetServerlessZipFilesZipIDVulnerabilitiesQueryParamSortDir.DESC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    



@dataclasses.dataclass
class GetServerlessZipFilesZipIDVulnerabilitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_vulnerability.Vulnerability]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

