"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cdpipelineresourceresult as shared_cdpipelineresourceresult
from enum import Enum
from typing import Optional

class GetCdResourceIDSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetCdResourceIDSortKey(str, Enum):
    r"""sort key"""
    RISK = 'risk'



@dataclasses.dataclass
class GetCdResourceIDRequest:
    resource_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'resourceId', 'style': 'simple', 'explode': False }})
    sort_dir: Optional[GetCdResourceIDSortDir] = dataclasses.field(default=GetCdResourceIDSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetCdResourceIDSortKey] = dataclasses.field(default=GetCdResourceIDSortKey.RISK, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    




@dataclasses.dataclass
class GetCdResourceIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    cd_pipeline_resource_result: Optional[shared_cdpipelineresourceresult.CdPipelineResourceResult] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

