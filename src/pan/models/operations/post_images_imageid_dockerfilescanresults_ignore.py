"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import uuidlist as shared_uuidlist
from enum import Enum
from typing import Optional

class PostImagesImageIDDockerfileScanResultsIgnoreActionType(str, Enum):
    r"""The ignore action type (ADD/REMOVE)"""
    ADD = 'ADD'
    REMOVE = 'REMOVE'



@dataclasses.dataclass
class PostImagesImageIDDockerfileScanResultsIgnoreRequest:
    action_type: PostImagesImageIDDockerfileScanResultsIgnoreActionType = dataclasses.field(metadata={'query_param': { 'field_name': 'actionType', 'style': 'form', 'explode': True }})
    r"""The ignore action type (ADD/REMOVE)"""
    image_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'imageId', 'style': 'simple', 'explode': False }})
    uuid_list: shared_uuidlist.UUIDList = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PostImagesImageIDDockerfileScanResultsIgnoreResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

