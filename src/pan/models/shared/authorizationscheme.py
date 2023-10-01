"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils

class AuthorizationSchemeAuthorizationSchemeType(str, Enum):
    AUTHORIZATION_SCHEME_BASIC_AUTH = 'AuthorizationSchemeBasicAuth'
    AUTHORIZATION_SCHEME_API_TOKEN = 'AuthorizationSchemeApiToken'
    AUTHORIZATION_SCHEME_BEARER_TOKEN = 'AuthorizationSchemeBearerToken'
    AUTHORIZATION_SCHEME_NONE = 'AuthorizationSchemeNone'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AuthorizationScheme:
    authorization_scheme_type: AuthorizationSchemeAuthorizationSchemeType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorizationSchemeType') }})
    
