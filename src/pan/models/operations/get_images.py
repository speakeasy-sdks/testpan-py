"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import imagedefget as shared_imagedefget
from enum import Enum
from typing import Optional

class GetImagesSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetImagesSortKey(str, Enum):
    r"""image sort key. enum description in image sort key definition"""
    IMAGE_NAME = 'IMAGE_NAME'
    TIME = 'TIME'
    RISK = 'RISK'



@dataclasses.dataclass
class GetImagesRequest:
    sort_key: GetImagesSortKey = dataclasses.field(metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""image sort key. enum description in image sort key definition"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    image_hash: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'IMAGE_HASH', 'style': 'form', 'explode': False }})
    r"""Filter images by HASH"""
    image_name: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'IMAGE_NAME', 'style': 'form', 'explode': False }})
    r"""Filter images by name"""
    image_tag: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'IMAGE_TAG', 'style': 'form', 'explode': False }})
    r"""Filter images by tags"""
    max_results: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    sort_dir: Optional[GetImagesSortDir] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    vulnerability_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'vulnerabilityName', 'style': 'form', 'explode': True }})
    r"""Filter images by vulnerability name"""
    




@dataclasses.dataclass
class GetImagesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    image_def_gets: Optional[list[shared_imagedefget.ImageDefGet]] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

