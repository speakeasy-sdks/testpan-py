"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .deletedependencyelement import DeleteDependencyElement
from .deletedependencyelementenvironments import DeleteDependencyElementEnvironments
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KubernetesClusterDeleteDependencies:
    cluster_event_rules: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterEventRules'), 'exclude': lambda f: f is None }})
    connection_rules: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionRules'), 'exclude': lambda f: f is None }})
    deployers: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployers'), 'exclude': lambda f: f is None }})
    deployment_rules: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploymentRules'), 'exclude': lambda f: f is None }})
    environments: Optional[DeleteDependencyElementEnvironments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environments'), 'exclude': lambda f: f is None }})
    expansions: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expansions'), 'exclude': lambda f: f is None }})
    gateways: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gateways'), 'exclude': lambda f: f is None }})
    registries: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('registries'), 'exclude': lambda f: f is None }})
    trusted_signers: Optional[List[DeleteDependencyElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trustedSigners'), 'exclude': lambda f: f is None }})
    

