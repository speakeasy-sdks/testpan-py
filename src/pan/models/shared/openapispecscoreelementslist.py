"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .apisecurityriskseverity import APISecurityRiskSeverity
from .openapispecscoreelement import OpenAPISpecScoreElement
from .vulnerabilitiessummary import VulnerabilitiesSummary
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpenAPISpecScoreElementsList:
    elements: Optional[List[OpenAPISpecScoreElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('elements'), 'exclude': lambda f: f is None }})
    severity: Optional[APISecurityRiskSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""An `enum`eration."""
    vulnerabilities_summary: Optional[VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    

