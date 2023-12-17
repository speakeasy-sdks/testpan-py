"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import agents as shared_agents
from enum import Enum
from typing import List, Optional

class Risk(str, Enum):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    UNDEFINED = 'UNDEFINED'

class GetAgentsQueryParamSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'

class GetAgentsQueryParamSortKey(str, Enum):
    r"""sort key"""
    HOST_NAME = 'hostName'
    ENVIRONMENT_NAME = 'environmentName'
    RISK = 'risk'
    STATUS = 'status'
    LAST_ACTIVE = 'lastActive'

class Status(str, Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STOPPED = 'STOPPED'
    TERMINATED = 'TERMINATED'


@dataclasses.dataclass
class GetAgentsRequest:
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    environment_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'environmentName', 'style': 'form', 'explode': False }})
    r"""Empty string means no filtering. \\"UNDEFINED\\" means telemetries with no App type"""
    host_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'hostName', 'style': 'form', 'explode': False }})
    r"""The name of the host"""
    risk: Optional[List[Risk]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'risk', 'style': 'form', 'explode': False }})
    r"""The risk of the environment for attack"""
    sort_dir: Optional[GetAgentsQueryParamSortDir] = dataclasses.field(default=GetAgentsQueryParamSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    sort_key: Optional[GetAgentsQueryParamSortKey] = dataclasses.field(default=GetAgentsQueryParamSortKey.HOST_NAME, metadata={'query_param': { 'field_name': 'sortKey', 'style': 'form', 'explode': True }})
    r"""sort key"""
    status: Optional[List[Status]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': False }})
    r"""Agent status"""
    



@dataclasses.dataclass
class GetAgentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    agents: Optional[shared_agents.Agents] = dataclasses.field(default=None)
    r"""Success"""
    

