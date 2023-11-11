"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverlesszip as shared_serverlesszip
from typing import Optional


@dataclasses.dataclass
class GetServerlessZipFilesZipIDRequest:
    zip_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'zipId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetServerlessZipFilesZipIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    serverless_zip: Optional[shared_serverlesszip.ServerlessZip] = dataclasses.field(default=None)
    r"""Success"""
    

