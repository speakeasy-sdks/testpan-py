"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverlessfunctionsecretissue as shared_serverlessfunctionsecretissue
from typing import List, Optional


@dataclasses.dataclass
class GetServerlessFunctionsFunctionIDSecretsRequest:
    function_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'functionId', 'style': 'simple', 'explode': False }})
    r"""Function ID"""
    



@dataclasses.dataclass
class GetServerlessFunctionsFunctionIDSecretsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_serverlessfunctionsecretissue.ServerlessFunctionSecretIssue]] = dataclasses.field(default=None)
    r"""Success"""
    

