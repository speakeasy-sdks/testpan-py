"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import seccompprofile as shared_seccompprofile
from ...models.shared import seccompprofile_input as shared_seccompprofile_input
from typing import Optional


@dataclasses.dataclass
class PutSeccompProfilesProfileIDRequest:
    seccomp_profile: shared_seccompprofile_input.SeccompProfileInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    profile_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'profileId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutSeccompProfilesProfileIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    seccomp_profile: Optional[shared_seccompprofile.SeccompProfile] = dataclasses.field(default=None)
    r"""Success"""
    

