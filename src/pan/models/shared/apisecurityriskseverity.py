"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class APISecurityRiskSeverity(str, Enum):
    r"""An `enum`eration."""
    NO_RISK = 'NO_RISK'
    UNKNOWN = 'UNKNOWN'
    NEUTRAL = 'NEUTRAL'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'