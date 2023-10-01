"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class APIReconstructionStatus(str, Enum):
    r"""Status of an ongoing API reconstruction phase."""
    NONE = 'NONE'
    IN_PROGRESS = 'IN_PROGRESS'
    ERROR = 'ERROR'
    DONE = 'DONE'
    ABORTING = 'ABORTING'