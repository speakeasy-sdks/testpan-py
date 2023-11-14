"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiresponse as shared_apiresponse
from ...models.shared import deletedependencyelementuser as shared_deletedependencyelementuser
from typing import Optional


@dataclasses.dataclass
class GetUsersUserIDDeleteDependenciesRequest:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetUsersUserIDDeleteDependenciesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    delete_dependency_element_user: Optional[shared_deletedependencyelementuser.DeleteDependencyElementUser] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

