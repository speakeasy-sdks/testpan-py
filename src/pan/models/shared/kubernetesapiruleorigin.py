"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class KubernetesAPIRuleOrigin(str, Enum):
    USER = 'USER'
    AUTOMATED_POLICY = 'AUTOMATED_POLICY'
    SYSTEM = 'SYSTEM'