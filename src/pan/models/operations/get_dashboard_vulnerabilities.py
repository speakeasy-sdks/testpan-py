"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import vulnerabilitieswidget as shared_vulnerabilitieswidget
from typing import List, Optional


@dataclasses.dataclass
class GetDashboardVulnerabilitiesRequest:
    clusters_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clustersIds', 'style': 'form', 'explode': True }})
    r"""the clusters ids to filter by"""
    



@dataclasses.dataclass
class GetDashboardVulnerabilitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    vulnerabilities_widget: Optional[shared_vulnerabilitieswidget.VulnerabilitiesWidget] = dataclasses.field(default=None)
    r"""OK"""
    

