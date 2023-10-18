"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import dockerfilescanresultssummary as shared_dockerfilescanresultssummary
from ..shared import imagesourcetype as shared_imagesourcetype
from ..shared import vulnerabilitiessummary as shared_vulnerabilitiessummary
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from pan import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ImageDefGet:
    r"""Authorized image hash"""
    dockerfile_scan_results_summary: Optional[shared_dockerfilescanresultssummary.DockerfileScanResultsSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerfileScanResultsSummary'), 'exclude': lambda f: f is None }})
    r"""dockerfile scan results summary by severity"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    image_hash: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageHash'), 'exclude': lambda f: f is None }})
    r"""Valid hash for the image. * will authorize image name without validating hash"""
    image_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageName'), 'exclude': lambda f: f is None }})
    image_source_type: Optional[shared_imagesourcetype.ImageSourceType] = dataclasses.field(default=shared_imagesourcetype.ImageSourceType.DOCKER_PLUGIN_CI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageSourceType'), 'exclude': lambda f: f is None }})
    image_tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageTags'), 'exclude': lambda f: f is None }})
    is_identified: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isIdentified'), 'exclude': lambda f: f is None }})
    r"""Specify if the image is identified"""
    is_scanned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isScanned'), 'exclude': lambda f: f is None }})
    r"""Specify if the image has been scanned during CI"""
    licenses: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('licenses'), 'exclude': lambda f: f is None }})
    time_added: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeAdded'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[shared_vulnerabilitiessummary.VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    

