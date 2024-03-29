"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .awsenvironment_input import AwsEnvironmentInput
from .kubernetesenvironment_input import KubernetesEnvironmentInput
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EnvironmentInput:
    r"""Secure Application environment definition. #also must be included for at least one of the env details but Swagger does not support parameter dependencies and mutually exclusive parameters."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Environment name. Must be unique."""
    aws_environments: Optional[List[AwsEnvironmentInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsEnvironments'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The environment description."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    is_system_env: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSystemEnv'), 'exclude': lambda f: f is None }})
    r"""indicates if this environment represents system namespaces that usually will be filtered out from some screens"""
    kubernetes_environments: Optional[List[KubernetesEnvironmentInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kubernetesEnvironments'), 'exclude': lambda f: f is None }})
    

