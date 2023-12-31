"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import uuidlist as shared_uuidlist
from enum import Enum
from typing import Optional

class PostRiskAssessmentPermissionsOwnerIDApproveQueryParamActionType(str, Enum):
    r"""The approve action type (ADD/REMOVE)"""
    ADD = 'ADD'
    REMOVE = 'REMOVE'


@dataclasses.dataclass
class PostRiskAssessmentPermissionsOwnerIDApproveRequest:
    action_type: PostRiskAssessmentPermissionsOwnerIDApproveQueryParamActionType = dataclasses.field(metadata={'query_param': { 'field_name': 'actionType', 'style': 'form', 'explode': True }})
    r"""The approve action type (ADD/REMOVE)"""
    owner_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ownerId', 'style': 'simple', 'explode': False }})
    uuid_list: shared_uuidlist.UUIDList = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PostRiskAssessmentPermissionsOwnerIDApproveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

