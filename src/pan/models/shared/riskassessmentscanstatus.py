"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class RiskAssessmentScanStatus(str, Enum):
    r"""Status of a risk assessment scan"""
    AGENT_NOT_READY = 'AGENT_NOT_READY'
    NOT_SCANNED = 'NOT_SCANNED'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
