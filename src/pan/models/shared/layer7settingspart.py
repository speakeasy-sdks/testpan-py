"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pan import utils
from typing import Optional

class Layer7SettingsPartLayer7Protocol(str, Enum):
    HTTP_LAYER7_PART = 'HttpLayer7Part'
    KAFKA_LAYER_PART = 'KafkaLayerPart'
    API_SERVICE_LAYER_PART = 'ApiServiceLayerPart'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Layer7SettingsPart:
    layer7_protocol: Optional[Layer7SettingsPartLayer7Protocol] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layer7Protocol'), 'exclude': lambda f: f is None }})
    

