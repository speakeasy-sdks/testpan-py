"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import apiresponse as errors_apiresponse
from ...models.shared import deployerdeletedependencies as shared_deployerdeletedependencies
from typing import Optional


@dataclasses.dataclass
class GetDeployersDeployerIDDeleteDependenciesRequest:
    deployer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'deployerId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetDeployersDeployerIDDeleteDependenciesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[errors_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    deployer_delete_dependencies: Optional[shared_deployerdeletedependencies.DeployerDeleteDependencies] = dataclasses.field(default=None)
    r"""Success"""
    

