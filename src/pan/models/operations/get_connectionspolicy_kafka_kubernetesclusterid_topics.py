"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import List, Optional


@dataclasses.dataclass
class GetConnectionsPolicyKafkaKubernetesClusterIDTopicsRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    



@dataclasses.dataclass
class GetConnectionsPolicyKafkaKubernetesClusterIDTopicsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    strings: Optional[List[str]] = dataclasses.field(default=None)
    r"""Success"""
    

