"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import permissionroleresponse as shared_permissionroleresponse
from typing import Optional


@dataclasses.dataclass
class GetRiskAssessmentPermissionsClusterIDOwnerIDRoleIDRequest:
    cluster_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clusterId', 'style': 'simple', 'explode': False }})
    owner_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ownerId', 'style': 'simple', 'explode': False }})
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'roleId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetRiskAssessmentPermissionsClusterIDOwnerIDRoleIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    permission_role_response: Optional[shared_permissionroleresponse.PermissionRoleResponse] = dataclasses.field(default=None)
    r"""Success"""
    

