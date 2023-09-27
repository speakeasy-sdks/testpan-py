"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponse as shared_apiresponse
from ..shared import kubernetesnamespace as shared_kubernetesnamespace
from enum import Enum
from typing import Optional

class GetKubernetesClustersKubernetesClusterIDNamespacesSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetKubernetesClustersKubernetesClusterIDNamespacesSortKey(str, Enum):
    r"""sort key"""
    NAME = 'name'
    STATUS = 'status'



@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDNamespacesRequest:
    kubernetes_cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'kubernetesClusterId', 'style': 'simple', 'explode': False }})
    r"""Secure Application Kubernetes cluster ID"""
    include_scannable: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeScannable', 'style': 'form', 'explode': True }})
    r"""If true - return all scannable namespaces"""
    sort_dir: Optional[GetKubernetesClustersKubernetesClusterIDNamespacesSortDir] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetKubernetesClustersKubernetesClusterIDNamespacesSortKey] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    




@dataclasses.dataclass
class GetKubernetesClustersKubernetesClusterIDNamespacesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    kubernetes_namespace_responses: Optional[list[shared_kubernetesnamespace.KubernetesNamespace]] = dataclasses.field(default=None)
    r"""success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

