"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiresponse as shared_apiresponse
from ...models.shared import kubernetesclustercontroller as shared_kubernetesclustercontroller
from enum import Enum
from typing import List, Optional

class GetKubernetesClustersQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetKubernetesClustersRequest:
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clusterName', 'style': 'form', 'explode': True }})
    r"""the cluster name to filter by"""
    controller_status: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'controllerStatus', 'style': 'form', 'explode': True }})
    r"""Filter the clusters by controller status"""
    controller_version: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'controllerVersion', 'style': 'form', 'explode': True }})
    r"""Filter the clusters by controller version"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    kubernetes_version: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'kubernetesVersion', 'style': 'form', 'explode': True }})
    r"""Filter the clusters by k8s version"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    only_spec_reconstruction_enabled_filter: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'onlySpecReconstructionEnabledFilter', 'style': 'form', 'explode': True }})
    r"""retrive only clusters that configured as spec reconstruction enabled."""
    sort_dir: Optional[GetKubernetesClustersQueryParamSortDir] = dataclasses.field(default=GetKubernetesClustersQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    



@dataclasses.dataclass
class GetKubernetesClustersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_response: Optional[shared_apiresponse.APIResponse] = dataclasses.field(default=None)
    r"""unknown error"""
    classes: Optional[List[shared_kubernetesclustercontroller.KubernetesClusterController]] = dataclasses.field(default=None)
    r"""Success"""
    

