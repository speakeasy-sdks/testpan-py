"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import eventsforwardingdetailslist as shared_eventsforwardingdetailslist
from typing import Optional


@dataclasses.dataclass
class GetSettingsIntegrationsEventForwardingResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    events_forwarding_details_list: Optional[shared_eventsforwardingdetailslist.EventsForwardingDetailsList] = dataclasses.field(default=None)
    r"""Success"""
    

