"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ClusterPodDefinitionSource(str, Enum):
    r"""The source type of the pod definitions of the cluster"""
    KUBERNETES = 'KUBERNETES'
    CD = 'CD'
