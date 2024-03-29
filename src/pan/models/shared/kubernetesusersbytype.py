"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .kubernetesauditlogusertype import KubernetesAuditLogUserType
from .kubernetesuserdetails import KubernetesUserDetails
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KubernetesUsersByType:
    user_type: Optional[KubernetesAuditLogUserType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userType'), 'exclude': lambda f: f is None }})
    users: Optional[List[KubernetesUserDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('users'), 'exclude': lambda f: f is None }})
    

