"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import cloudaccountbase as shared_cloudaccountbase
from ..shared import serverlessdataaccessrisk as shared_serverlessdataaccessrisk
from ..shared import serverlessfunctionrisk as shared_serverlessfunctionrisk
from ..shared import serverlesspolicyrisk as shared_serverlesspolicyrisk
from ..shared import serverlesspubliclyaccessiblerisk as shared_serverlesspubliclyaccessiblerisk
from ..shared import serverlessroledetails as shared_serverlessroledetails
from ..shared import serverlesssecretsrisk as shared_serverlesssecretsrisk
from ..shared import serverlessviolationinfo as shared_serverlessviolationinfo
from ..shared import vulnerabilitiessummary as shared_vulnerabilitiessummary
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ServerlessFunction:
    r"""Single serverless function"""
    arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('arn'), 'exclude': lambda f: f is None }})
    cloud_account: Optional[shared_cloudaccountbase.CloudAccountBase] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cloudAccount'), 'exclude': lambda f: f is None }})
    r"""represent cloud account object"""
    data_access_risk: Optional[shared_serverlessdataaccessrisk.ServerlessDataAccessRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataAccessRisk'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    is_unused_function: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isUnusedFunction'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""name with version"""
    policy_risk: Optional[shared_serverlesspolicyrisk.ServerlessPolicyRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyRisk'), 'exclude': lambda f: f is None }})
    publicly_accessible_risk: Optional[shared_serverlesspubliclyaccessiblerisk.ServerlessPubliclyAccessibleRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publiclyAccessibleRisk'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    risk: Optional[shared_serverlessfunctionrisk.ServerlessFunctionRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('risk'), 'exclude': lambda f: f is None }})
    role_details: Optional[shared_serverlessroledetails.ServerlessRoleDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roleDetails'), 'exclude': lambda f: f is None }})
    runtime: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runtime'), 'exclude': lambda f: f is None }})
    secrets_risk: Optional[shared_serverlesssecretsrisk.ServerlessSecretsRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretsRisk'), 'exclude': lambda f: f is None }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    violation: Optional[shared_serverlessviolationinfo.ServerlessViolationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('violation'), 'exclude': lambda f: f is None }})
    vulnerabilities_summary: Optional[shared_vulnerabilitiessummary.VulnerabilitiesSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vulnerabilitiesSummary'), 'exclude': lambda f: f is None }})
    r"""Vulnerabilities summary by severity"""
    
