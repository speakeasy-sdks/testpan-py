"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import apiresponse as errors_apiresponse
from ...models.shared import kubernetesclusterdeletedependencies as shared_kubernetesclusterdeletedependencies
from typing import Optional


@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    



@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDDeleteDependenciesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    api_response: Optional[errors_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    kubernetes_cluster_delete_dependencies: Optional[shared_kubernetesclusterdeletedependencies.KubernetesClusterDeleteDependencies] = dataclasses.field(default=None)
    r"""Success"""
    

