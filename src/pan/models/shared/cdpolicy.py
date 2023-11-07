"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .apisecuritycdpolicyelement import APISecurityCdPolicyElement
from .cdpolicyelement import CdPolicyElement
from .secretscdpolicyelement import SecretsCdPolicyElement
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CdPolicyInput:
    deployers: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployers') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    api_security_cd_policy: Optional[APISecurityCdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiSecurityCdPolicy'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    permission_cd_policy: Optional[CdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permissionCDPolicy'), 'exclude': lambda f: f is None }})
    secret_cd_policy: Optional[SecretsCdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretCDPolicy'), 'exclude': lambda f: f is None }})
    security_context_cd_policy: Optional[CdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityContextCDPolicy'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CdPolicy:
    deployers: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployers') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    api_security_cd_policy: Optional[APISecurityCdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiSecurityCdPolicy'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    permission_cd_policy: Optional[CdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permissionCDPolicy'), 'exclude': lambda f: f is None }})
    secret_cd_policy: Optional[SecretsCdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretCDPolicy'), 'exclude': lambda f: f is None }})
    security_context_cd_policy: Optional[CdPolicyElement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityContextCDPolicy'), 'exclude': lambda f: f is None }})
    

