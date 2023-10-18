"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deployer as shared_deployer
from typing import Optional


@dataclasses.dataclass
class PutDeployersDeployerIDRequest:
    deployer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'deployerId', 'style': 'simple', 'explode': False }})
    deployer_input: shared_deployer.DeployerInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutDeployersDeployerIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    deployer: Optional[shared_deployer.Deployer] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

