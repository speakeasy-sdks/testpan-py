"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import apiresponse as errors_apiresponse
from ...models.shared import trialuser as shared_trialuser
from ...models.shared import user as shared_user
from pan import utils
from typing import Optional


@dataclasses.dataclass
class PostUsersTrialRequest:
    g_recaptcha_response: str = dataclasses.field(metadata={'header': { 'field_name': 'g-recaptcha-response', 'style': 'simple', 'explode': False }})
    r"""google recaptcha response"""
    trial_user: shared_trialuser.TrialUser = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PostUsersTrialResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[errors_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    r"""The new trial user that was created"""
    

