"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cdconnectionrule as shared_cdconnectionrule
from typing import Optional



@dataclasses.dataclass
class PutCdRuleIDConnectionsRuleRequest:
    cd_connection_rule: shared_cdconnectionrule.CdConnectionRule = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    rule_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ruleId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class PutCdRuleIDConnectionsRuleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    cd_connection_rule: Optional[shared_cdconnectionrule.CdConnectionRule] = dataclasses.field(default=None)
    r"""updated"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

