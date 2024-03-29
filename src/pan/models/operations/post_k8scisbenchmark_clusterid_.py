"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import k8scisbenchmarkclusterssummary as shared_k8scisbenchmarkclusterssummary
from typing import Optional


@dataclasses.dataclass
class PostK8sCISBenchmarkClusterIDRequest:
    cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clusterId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PostK8sCISBenchmarkClusterIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    k8s_cis_benchmark_clusters_summary: Optional[shared_k8scisbenchmarkclusterssummary.K8sCISBenchmarkClustersSummary] = dataclasses.field(default=None)
    r"""Accepted"""
    

