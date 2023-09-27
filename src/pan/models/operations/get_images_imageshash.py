"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class GetImagesImagesHashRequest:
    image_hash: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'imageHash', 'style': 'form', 'explode': True }})
    r"""image hash to search for ( as prefix and suffix )"""
    max_results: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    




@dataclasses.dataclass
class GetImagesImagesHashResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_images_images_hash_200_application_json_strings: Optional[list[str]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

