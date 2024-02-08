"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import userdisplay as shared_userdisplay
from enum import Enum
from typing import List, Optional

class Roles(str, Enum):
    LIGHTSPIN_ADMIN = 'LIGHTSPIN_ADMIN'
    SELF_PROVISIONING = 'SELF_PROVISIONING'
    CI_CD_SCANNER = 'CI_CD_SCANNER'
    PORTSHIFT_ADMIN = 'PORTSHIFT_ADMIN'
    PORTSHIFT_AUDITOR = 'PORTSHIFT_AUDITOR'
    ACCOUNT_ADMIN = 'ACCOUNT_ADMIN'
    SERVICE = 'SERVICE'
    ACCOUNT_AUDITOR = 'ACCOUNT_AUDITOR'


@dataclasses.dataclass
class GetUsersRequest:
    email: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    r"""the email to filter by"""
    roles: Optional[List[Roles]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'roles', 'style': 'form', 'explode': True }})
    r"""the roles to filter by"""
    username: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'username', 'style': 'form', 'explode': True }})
    r"""the user name to filter by"""
    



@dataclasses.dataclass
class GetUsersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_userdisplay.UserDisplay]] = dataclasses.field(default=None)
    r"""Success"""
    

