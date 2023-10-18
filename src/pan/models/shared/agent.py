"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import agentenvironment as shared_agentenvironment
from ..shared import agentinfo as shared_agentinfo
from ..shared import agentinstance as shared_agentinstance
from ..shared import agenttype as shared_agenttype
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import List, Optional

class AgentGatherInformationState(str, Enum):
    NEW = 'NEW'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    FAILED = 'FAILED'
    NONE = 'NONE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Agent:
    environments: Optional[List[shared_agentenvironment.AgentEnvironment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environments'), 'exclude': lambda f: f is None }})
    gather_information_state: Optional[AgentGatherInformationState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gatherInformationState'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""sha2 of the content of the public key pem. The fingerprint format is xx:xx:xx..."""
    info: Optional[shared_agentinfo.AgentInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info'), 'exclude': lambda f: f is None }})
    instance: Optional[shared_agentinstance.AgentInstance] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance'), 'exclude': lambda f: f is None }})
    is_update_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isUpdateEnabled'), 'exclude': lambda f: f is None }})
    kubernetes_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kubernetesVersion'), 'exclude': lambda f: f is None }})
    nodes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nodes'), 'exclude': lambda f: f is None }})
    shared_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sharedSecret'), 'exclude': lambda f: f is None }})
    status_codes: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCodes'), 'exclude': lambda f: f is None }})
    type: Optional[shared_agenttype.AgentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of agent. Possible values are instance agent or k8s agent."""
    vcpus: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vcpus'), 'exclude': lambda f: f is None }})
    

