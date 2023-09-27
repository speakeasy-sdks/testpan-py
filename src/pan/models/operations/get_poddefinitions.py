"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import poddefinition as shared_poddefinition
from typing import Optional



@dataclasses.dataclass
class GetPodDefinitionsRequest:
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clusterName', 'style': 'form', 'explode': True }})
    r"""Filter pod definitions by cluster name"""
    deployment_type: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'deploymentType', 'style': 'form', 'explode': False }})
    r"""Filter pod definitions by deployment type"""
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter pod definitions by name"""
    no_pagination: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'noPagination', 'style': 'form', 'explode': True }})
    r"""When true, the pagination params will be ignored"""
    template_source: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'templateSource', 'style': 'form', 'explode': False }})
    r"""Filter pod definitions by template source"""
    




@dataclasses.dataclass
class GetPodDefinitionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    pod_definitions: Optional[list[shared_poddefinition.PodDefinition]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

