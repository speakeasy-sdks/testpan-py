"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiriskinfo as shared_apiriskinfo
from typing import List, Optional


@dataclasses.dataclass
class GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest:
    app_telemetry_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appTelemetryId', 'style': 'simple', 'explode': False }})
    r"""App telemetry ID"""
    



@dataclasses.dataclass
class GetAppTelemetriesAppTelemetryIDAPIRiskInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_apiriskinfo.APIRiskInfo]] = dataclasses.field(default=None)
    r"""Success"""
    

