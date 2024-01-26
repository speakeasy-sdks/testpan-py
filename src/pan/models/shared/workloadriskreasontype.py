"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class WorkloadRiskReasonType(str, Enum):
    K8_S_DASHBOARD = 'K8S_DASHBOARD'
    VULNERABILITY = 'VULNERABILITY'
    RISKY_ROLE = 'RISKY_ROLE'
    PRIVILEGED = 'PRIVILEGED'
    RUN_AS_ROOT = 'RUN_AS_ROOT'
    ALLOWED_HOST_PATH = 'ALLOWED_HOST_PATH'
    ALLOWED_RISKY_CAPABILITIES = 'ALLOWED_RISKY_CAPABILITIES'
    PUBLIC_FACING = 'PUBLIC_FACING'
    UNIDENTIFIED = 'UNIDENTIFIED'
    RUNNING_SSH_SERVER = 'RUNNING_SSH_SERVER'
    HOST_NETWORK = 'HOST_NETWORK'
    HOST_PID = 'HOST_PID'
    HOST_IPC = 'HOST_IPC'
    ALLOW_PRIVILEGE_ESCALATION = 'ALLOW_PRIVILEGE_ESCALATION'
    TEMPLATE_DIFF = 'TEMPLATE_DIFF'
    DOCKERFILE_SCAN = 'DOCKERFILE_SCAN'
    API = 'API'
