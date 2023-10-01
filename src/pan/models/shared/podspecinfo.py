"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import containersecuritycontext as shared_containersecuritycontext
from ..shared import podsecuritycontext as shared_podsecuritycontext
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PodSpecInfo:
    r"""pod spec attributes which are potentially risky"""
    containers: Optional[list[shared_containersecuritycontext.ContainerSecurityContext]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('containers'), 'exclude': lambda f: f is None }})
    host_ipc: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostIPC'), 'exclude': lambda f: f is None }})
    host_network: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostNetwork'), 'exclude': lambda f: f is None }})
    host_pid: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostPID'), 'exclude': lambda f: f is None }})
    init_containers: Optional[list[shared_containersecuritycontext.ContainerSecurityContext]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initContainers'), 'exclude': lambda f: f is None }})
    pod_security_context: Optional[shared_podsecuritycontext.PodSecurityContext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podSecurityContext'), 'exclude': lambda f: f is None }})
    share_process_namespace: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shareProcessNamespace'), 'exclude': lambda f: f is None }})
    volumes: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('volumes'), 'exclude': lambda f: f is None }})
    
