"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .kubernetesapiruleorigin import KubernetesAPIRuleOrigin
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import Optional

class KubernetesAPIRuleType(str, Enum):
    KUBERNETES_API_CUSTOM_RULE = 'KubernetesApiCustomRule'
    KUBERNETES_API_RECOMMENDED_RULE = 'KubernetesApiRecommendedRule'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class KubernetesAPIRule:
    kubernetes_api_rule_type: KubernetesAPIRuleType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kubernetesApiRuleType') }})
    rule_origin: Optional[KubernetesAPIRuleOrigin] = dataclasses.field(default=KubernetesAPIRuleOrigin.USER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleOrigin'), 'exclude': lambda f: f is None }})
    

