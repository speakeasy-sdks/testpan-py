"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import topsecurityriskswidget as shared_topsecurityriskswidget
from typing import List, Optional


@dataclasses.dataclass
class GetDashboardTopSecurityRisksRequest:
    clusters_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clustersIds', 'style': 'form', 'explode': True }})
    r"""the clusters ids to filter by"""
    size: Optional[int] = dataclasses.field(default=5, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    r"""Amount of top risky workloads to return"""
    



@dataclasses.dataclass
class GetDashboardTopSecurityRisksResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    top_security_risks_widget: Optional[shared_topsecurityriskswidget.TopSecurityRisksWidget] = dataclasses.field(default=None)
    r"""OK"""
    

