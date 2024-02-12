"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import dockerfilescanresult as shared_dockerfilescanresult
from enum import Enum
from typing import List, Optional

class GetImagesImageIDDockerfileScanResultsQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetImagesImageIDDockerfileScanResultsRequest:
    image_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'imageId', 'style': 'simple', 'explode': False }})
    is_ignored: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'isIgnored', 'style': 'form', 'explode': True }})
    r"""Return ignored / not ignored entries"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetImagesImageIDDockerfileScanResultsQueryParamSortDir] = dataclasses.field(default=GetImagesImageIDDockerfileScanResultsQueryParamSortDir.DESC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    



@dataclasses.dataclass
class GetImagesImageIDDockerfileScanResultsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_dockerfilescanresult.DockerfileScanResult]] = dataclasses.field(default=None)
    r"""OK"""
    

