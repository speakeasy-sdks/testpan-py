"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ConnectionRuleAction(str, Enum):
    r"""ENCRYPT is not allowed in default rule"""
    DETECT = 'DETECT'
    BLOCK = 'BLOCK'
    ALLOW = 'ALLOW'
    ENCRYPT = 'ENCRYPT'
    ENCRYPT_DIRECT = 'ENCRYPT_DIRECT'
