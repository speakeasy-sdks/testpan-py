"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import scantype as shared_scantype
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ScanConfiguration:
    r"""scan configuration information"""
    number_of_scanners: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfScanners'), 'exclude': lambda f: f is None }})
    r"""Number of available scanners in cluster"""
    scan_types: Optional[list[shared_scantype.ScanType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scanTypes'), 'exclude': lambda f: f is None }})
    r"""Cluster scan types"""
    

