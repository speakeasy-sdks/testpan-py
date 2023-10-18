"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import serverlessfunction as shared_serverlessfunction
from enum import Enum
from typing import List, Optional

class GetServerlessFunctionsPolicyRisk(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'

class GetServerlessFunctionsResult(str, Enum):
    ALLOW = 'ALLOW'
    DETECT = 'DETECT'
    BLOCK = 'BLOCK'

class GetServerlessFunctionsRisk(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'

class GetServerlessFunctionsSecretsRisk(str, Enum):
    NO_KNOWN_RISK = 'NO_KNOWN_RISK'
    RISK_IDENTIFIED = 'RISK_IDENTIFIED'

class GetServerlessFunctionsSortDir(str, Enum):
    r"""sorting direction"""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetServerlessFunctionsRequest:
    cloud_account_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cloudAccountName', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by name"""
    cloud_accounts_ids_filter: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cloudAccountsIdsFilter', 'style': 'form', 'explode': False }})
    download_as_xlsx: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'downloadAsXlsx', 'style': 'form', 'explode': True }})
    r"""When true, the API will return an xlsx file, and pagination will be ignored"""
    func_name: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'funcName', 'style': 'form', 'explode': False }})
    r"""Defined function name"""
    max_results: Optional[float] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'maxResults', 'style': 'form', 'explode': True }})
    r"""The number of entries to return (pagination)"""
    offset: Optional[float] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Return entries from this offset (pagination)"""
    policy_risk: Optional[List[GetServerlessFunctionsPolicyRisk]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'policyRisk', 'style': 'form', 'explode': False }})
    r"""The risk of the serverless functioriskFindingsn policy"""
    region: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'region', 'style': 'form', 'explode': True }})
    r"""Filter cloud accounts by region"""
    result: Optional[List[GetServerlessFunctionsResult]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'result', 'style': 'form', 'explode': False }})
    r"""serverless function result filter"""
    risk: Optional[List[GetServerlessFunctionsRisk]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'risk', 'style': 'form', 'explode': False }})
    r"""The risk of the serverless function"""
    secrets_risk: Optional[List[GetServerlessFunctionsSecretsRisk]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'secretsRisk', 'style': 'form', 'explode': False }})
    r"""The risk of the serverless function secrets"""
    sort_dir: Optional[GetServerlessFunctionsSortDir] = dataclasses.field(default=GetServerlessFunctionsSortDir.ASC, metadata={'query_param': { 'field_name': 'sortDir', 'style': 'form', 'explode': True }})
    r"""sorting direction"""
    



@dataclasses.dataclass
class GetServerlessFunctionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    serverless_functions: Optional[List[shared_serverlessfunction.ServerlessFunction]] = dataclasses.field(default=None)
    r"""Success"""
    

