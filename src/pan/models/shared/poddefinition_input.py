"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .container import Container
from .label import Label
from .poddefinitionsource import PodDefinitionSource
from .podtemplatekind import PodTemplateKind
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PodDefinitionInput:
    cluster_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterId') }})
    containers: List[Container] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('containers') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""in pod template, this is the normalized name (for example, get it from pod -> replicaset -> deployment)."""
    init_containers: Optional[List[Container]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initContainers'), 'exclude': lambda f: f is None }})
    kind: Optional[PodTemplateKind] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind'), 'exclude': lambda f: f is None }})
    labels: Optional[List[Label]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    pod_definition_source: Optional[PodDefinitionSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('podDefinitionSource'), 'exclude': lambda f: f is None }})
    r"""The source type of the pod definition"""
    
