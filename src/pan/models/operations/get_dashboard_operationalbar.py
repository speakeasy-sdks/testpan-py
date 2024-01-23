"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import operationalbar as shared_operationalbar
from typing import List, Optional


@dataclasses.dataclass
class GetDashboardOperationalBarRequest:
    clusters_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clustersIds', 'style': 'form', 'explode': True }})
    r"""the clusters ids to filter by"""
    



@dataclasses.dataclass
class GetDashboardOperationalBarResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    operational_bar: Optional[shared_operationalbar.OperationalBar] = dataclasses.field(default=None)
    r"""OK"""
    

