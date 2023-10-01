"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import userlogininfo as shared_userlogininfo
from typing import Optional



@dataclasses.dataclass
class PostMeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    user_login_info: Optional[shared_userlogininfo.UserLoginInfo] = dataclasses.field(default=None)
    r"""Success"""
    
