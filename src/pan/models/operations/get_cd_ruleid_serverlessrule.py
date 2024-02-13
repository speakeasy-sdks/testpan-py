"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import cdserverlessrule as shared_cdserverlessrule
from typing import Optional


@dataclasses.dataclass
class GetCdRuleIDServerlessRuleRequest:
    rule_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ruleId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetCdRuleIDServerlessRuleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    cd_serverless_rule: Optional[shared_cdserverlessrule.CdServerlessRule] = dataclasses.field(default=None)
    r"""OK"""
    

