"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ImageSourceType(str, Enum):
    JENKINS_PLUGIN_CI = 'JENKINS_PLUGIN_CI'
    DOCKER_PLUGIN_CI = 'DOCKER_PLUGIN_CI'
    RISK_ASSESSMENT = 'RISK_ASSESSMENT'
    JFROG_XRAY = 'JFROG_XRAY'
    RUNTIME = 'RUNTIME'
