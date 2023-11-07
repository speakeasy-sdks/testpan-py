"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .cloudaccountsecuritythreats import CloudAccountSecurityThreats
from .cloudprovidertype import CloudProviderType
from .serverlessperiodicjobexpression import ServerlessPeriodicJobExpression
from .vulnerabilitiessummary import VulnerabilitiesSummary
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from pan import utils
from typing import List, Optional

class ValidateFunction(str, Enum):
    HASH_VALIDATION = 'HASH_VALIDATION'
    SIGNATURE_VALIDATION = 'SIGNATURE_VALIDATION'
    NONE = 'NONE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CloudAccountInput:
    r"""represent cloud account object"""
    periodic_job_expression: ServerlessPeriodicJobExpression = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('periodicJobExpression') }})
    cloud_provider: Optional[CloudProviderType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cloudProvider'), 'exclude': lambda f: f is None }})
    install_vulnerability_scanner: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installVulnerabilityScanner'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    regions: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('regions'), 'exclude': lambda f: f is None }})
    security_threats: Optional[CloudAccountSecurityThreats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityThreats'), 'exclude': lambda f: f is None }})
    validate_function: Optional[ValidateFunction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validateFunction'), 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    


class InstallationStatus(str, Enum):
    INSTALLED = 'INSTALLED'
    PENDING_INSTALLATION = 'PENDING_INSTALLATION'
    FAILED = 'FAILED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CloudAccount:
    r"""represent cloud account object"""
    periodic_job_expression: ServerlessPeriodicJobExpression = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('periodicJobExpression') }})
    cloud_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cloudAccountId'), 'exclude': lambda f: f is None }})
    r"""the identifier id from the cloud account provider. account ID for AWS and subscription ID in Azure"""
    cloud_provider: Optional[CloudProviderType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cloudProvider'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    installation_status: Optional[InstallationStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installationStatus'), 'exclude': lambda f: f is None }})
    install_vulnerability_scanner: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installVulnerabilityScanner'), 'exclude': lambda f: f is None }})
    last_scanned: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastScanned'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    regions: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('regions'), 'exclude': lambda f: f is None }})
    security_threats: Optional[CloudAccountSecurityThreats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityThreats'), 'exclude': lambda f: f is None }})
    validate_function: Optional[ValidateFunction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validateFunction'), 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    

