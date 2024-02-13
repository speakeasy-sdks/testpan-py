"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import registry as shared_registry


@dataclasses.dataclass
class PutRegistriesRegistryIDRequest:
    registry: shared_registry.RegistryInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    registry_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'registryId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PutRegistriesRegistryIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

