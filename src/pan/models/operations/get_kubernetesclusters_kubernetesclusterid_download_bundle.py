"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from typing import Optional



@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    send_telemetries_interval_sec: Optional[int] = dataclasses.field(default=30, metadata={'query_param': { 'field_name': 'sendTelemetriesIntervalSec', 'style': 'form', 'explode': True }})
    r"""The time interval for sending telemetries"""
    




@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDDownloadBundleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    get_kubernetes_clusters_kubernetes_cluster_id_download_bundle_200_application_json_binary_string: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
