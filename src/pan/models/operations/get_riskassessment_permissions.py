"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clusterpermission as shared_clusterpermission
from enum import Enum
from typing import List, Optional

class QueryParamPermissionRisk(str, Enum):
    r"""the risk to filter by"""
    NO_RISK = 'NO_RISK'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    APPROVED = 'APPROVED'

class GetRiskAssessmentPermissionsQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetRiskAssessmentPermissionsQueryParamSortKey(str, Enum):
    r"""sort key"""
    PERMISSION_RISK = 'permissionRisk'


@dataclasses.dataclass
class GetRiskAssessmentPermissionsRequest:
    clusters_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'clustersIds', 'style': 'form', 'explode': True }})
    r"""the clusters ids to filter by"""
    include_system_owners: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'includeSystemOwners', 'style': 'form', 'explode': True }})
    r"""include systems default owners"""
    permission_risk: Optional[QueryParamPermissionRisk] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'permissionRisk', 'style': 'form', 'explode': True }})
    r"""the risk to filter by"""
    sort_dir: Optional[GetRiskAssessmentPermissionsQueryParamSortDir] = dataclasses.field(default=GetRiskAssessmentPermissionsQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetRiskAssessmentPermissionsQueryParamSortKey] = dataclasses.field(default=GetRiskAssessmentPermissionsQueryParamSortKey.PERMISSION_RISK, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    



@dataclasses.dataclass
class GetRiskAssessmentPermissionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_clusterpermission.ClusterPermission]] = dataclasses.field(default=None)
    r"""Success"""
    

