"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import app as shared_app
from typing import Optional


@dataclasses.dataclass
class PutAppsAppIDRequest:
    app: shared_app.App = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutAppsAppIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    app: Optional[shared_app.App] = dataclasses.field(default=None)
    r"""App was edited."""
    

