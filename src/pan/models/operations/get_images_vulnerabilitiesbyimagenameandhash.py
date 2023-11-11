"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import vulnerability as shared_vulnerability
from enum import Enum
from typing import List, Optional

class GetImagesVulnerabilitiesByImageNameAndHashQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetImagesVulnerabilitiesByImageNameAndHashRequest:
    image_hash: str = dataclasses.field(metadata={'query_param': { 'field_name': 'imageHash', 'style': 'form', 'explode': True }})
    r"""the image sha256"""
    image_name: str = dataclasses.field(metadata={'query_param': { 'field_name': 'imageName', 'style': 'form', 'explode': True }})
    r"""the image name without tag"""
    is_ignored: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'isIgnored', 'style': 'form', 'explode': True }})
    r"""Return ignored / not ignored entries"""
    layer_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'layerId', 'style': 'form', 'explode': True }})
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    show_only_vulnerabilities_with_fix: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'showOnlyVulnerabilitiesWithFix', 'style': 'form', 'explode': True }})
    sort_dir: Optional[GetImagesVulnerabilitiesByImageNameAndHashQueryParamSortDir] = dataclasses.field(default=GetImagesVulnerabilitiesByImageNameAndHashQueryParamSortDir.DESC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    



@dataclasses.dataclass
class GetImagesVulnerabilitiesByImageNameAndHashResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_vulnerability.Vulnerability]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

