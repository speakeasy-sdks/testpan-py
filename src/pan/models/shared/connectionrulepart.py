"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils

class ConnectionRulePartType(str, Enum):
    APP_NAME_CONNECTION_RULE_PART = 'AppNameConnectionRulePart'
    APP_TYPE_CONNECTION_RULE_PART = 'AppTypeConnectionRulePart'
    APP_LABEL_CONNECTION_RULE_PART = 'AppLabelConnectionRulePart'
    APP_ANY_CONNECTION_RULE_PART = 'AppAnyConnectionRulePart'
    POD_NAME_CONNECTION_RULE_PART = 'PodNameConnectionRulePart'
    POD_LABLES_CONNECTION_RULE_PART = 'PodLablesConnectionRulePart'
    POD_ANY_CONNECTION_RULE_PART = 'PodAnyConnectionRulePart'
    ENVIRONMENT_NAME_CONNECTION_RULE_PART = 'EnvironmentNameConnectionRulePart'
    ENVIRONMENT_ANY_CONNECTION_RULE_PART = 'EnvironmentAnyConnectionRulePart'
    IP_RANGE_CONNECTION_RULE_PART = 'IpRangeConnectionRulePart'
    EXTERNAL_CONNECTION_RULE_PART = 'ExternalConnectionRulePart'
    FQDN_CONNECTION_RULE_PART = 'FqdnConnectionRulePart'
    SERVICE_NAME_CONNECTION_RULE_PART = 'ServiceNameConnectionRulePart'
    ANY_CONNECTION_RULE_PART = 'AnyConnectionRulePart'
    EXPANSION_NAME_CONNECTION_RULE_PART = 'ExpansionNameConnectionRulePart'
    EXPANSION_LABELS_CONNECTION_RULE_PART = 'ExpansionLabelsConnectionRulePart'
    EXPANSION_ANY_CONNECTION_RULE_PART = 'ExpansionAnyConnectionRulePart'
    KAFKA_CONNECTION_RULE_PART = 'KafkaConnectionRulePart'
    API_SERVICE_CONNECTION_RULE_PART = 'ApiServiceConnectionRulePart'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionRulePart:
    connection_rule_part_type: ConnectionRulePartType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionRulePartType') }})
    

