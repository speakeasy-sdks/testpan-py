"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import timebasedwidget as shared_timebasedwidget
from typing import Optional



@dataclasses.dataclass
class GetDashboardKubernetesClusterIDConnectionTelemetriesRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    




@dataclasses.dataclass
class GetDashboardKubernetesClusterIDConnectionTelemetriesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    time_based_widget: Optional[shared_timebasedwidget.TimeBasedWidget] = dataclasses.field(default=None)
    r"""OK"""
    

