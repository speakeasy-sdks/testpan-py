"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from ..shared import deletedependencyelementenvironments as shared_deletedependencyelementenvironments
from typing import Optional


@dataclasses.dataclass
class GetEnvironmentsEnvIDDeleteDependenciesRequest:
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetEnvironmentsEnvIDDeleteDependenciesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    delete_dependency_element_environments: Optional[shared_deletedependencyelementenvironments.DeleteDependencyElementEnvironments] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

