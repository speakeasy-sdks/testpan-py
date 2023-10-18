"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import agent as shared_agent
from ..shared import kubernetescluster as shared_kubernetescluster
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KubernetesClusterController:
    agent: Optional[shared_agent.Agent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Agent'), 'exclude': lambda f: f is None }})
    kubernetes_cluster: Optional[shared_kubernetescluster.KubernetesCluster] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('KubernetesCluster'), 'exclude': lambda f: f is None }})
    should_send_metrics: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shouldSendMetrics'), 'exclude': lambda f: f is None }})
    

