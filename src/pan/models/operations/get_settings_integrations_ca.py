"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import caintegrationresponsewithclusters as shared_caintegrationresponsewithclusters
from typing import Optional



@dataclasses.dataclass
class GetSettingsIntegrationsCaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    ca_integration_response_with_clusters: Optional[list[shared_caintegrationresponsewithclusters.CaIntegrationResponseWithClusters]] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

