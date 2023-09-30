"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import clusterpoddefinitionsource as shared_clusterpoddefinitionsource
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LeanKubernetesCluster:
    cluster_pod_definition_source: Optional[shared_clusterpoddefinitionsource.ClusterPodDefinitionSource] = dataclasses.field(default=shared_clusterpoddefinitionsource.ClusterPodDefinitionSource.KUBERNETES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterPodDefinitionSource'), 'exclude': lambda f: f is None }})
    r"""The source type of the pod definitions of the cluster"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Id of the cluster."""
    install_tracing_support: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installTracingSupport'), 'exclude': lambda f: f is None }})
    r"""indicates whether to install tracing support, enable for apiSecurity accounts"""
    kubernetes_security: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kubernetesSecurity'), 'exclude': lambda f: f is None }})
    r"""indicates whether kubernetes security is enabled"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    use_external_ca: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('useExternalCA'), 'exclude': lambda f: f is None }})
    r"""indicates whether kubernetes should use external CA"""
    

