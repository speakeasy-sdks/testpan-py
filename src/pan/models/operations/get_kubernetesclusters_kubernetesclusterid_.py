"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from ..shared import kubernetescluster as shared_kubernetescluster
from typing import Optional



@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    




@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    kubernetes_cluster: Optional[shared_kubernetescluster.KubernetesCluster] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
