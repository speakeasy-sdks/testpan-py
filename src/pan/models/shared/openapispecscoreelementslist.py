"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import apisecurityriskseverity as shared_apisecurityriskseverity
from ..shared import openapispecscoreelement as shared_openapispecscoreelement
from ..shared import vulnerabilitiessummary as shared_vulnerabilitiessummary
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpenAPISpecScoreElementsList:
    elements: Optional[List[shared_openapispecscoreelement.OpenAPISpecScoreElement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('elements'), 'exclude': lambda f: f is None }})
    severity: Optional[shared_apisecurityriskseverity.APISecurityRiskSeverity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('severity'), 'exclude': lambda f: f is None }})
    r"""An `enum`eration."""
    vulnerabilities_summary: Optional[shared_vulnerabilitiessummary.VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    

