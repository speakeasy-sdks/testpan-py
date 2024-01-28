"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connectiontelemetry as shared_connectiontelemetry
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class GetConnectionTelemetriesConnectionTelemetryIDRequest:
    connection_telemetry_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionTelemetryId', 'style': 'simple', 'explode': False }})
    r"""connection telemetry ID"""
    end_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'endTime', 'style': 'form', 'explode': True }})
    r"""End date of the query"""
    start_time: datetime = dataclasses.field(metadata={'query_param': { 'field_name': 'startTime', 'style': 'form', 'explode': True }})
    r"""Start date of the query"""
    



@dataclasses.dataclass
class GetConnectionTelemetriesConnectionTelemetryIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connection_telemetry: Optional[shared_connectiontelemetry.ConnectionTelemetry] = dataclasses.field(default=None)
    r"""OK"""
    

