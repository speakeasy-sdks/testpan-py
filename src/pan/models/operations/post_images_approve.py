"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import uuidlist as shared_uuidlist
from typing import Optional


@dataclasses.dataclass
class PostImagesApproveRequest:
    is_image_approved: bool = dataclasses.field(metadata={'query_param': { 'field_name': 'isImageApproved', 'style': 'form', 'explode': True }})
    r"""Is image approved"""
    uuid_list: shared_uuidlist.UUIDList = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PostImagesApproveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

