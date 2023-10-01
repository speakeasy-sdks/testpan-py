"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import edituser as shared_edituser
from ..shared import user as shared_user
from typing import Optional



@dataclasses.dataclass
class PutUsersUserIDRequest:
    edit_user_input: shared_edituser.EditUserInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class PutUsersUserIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    r"""Success"""
    
