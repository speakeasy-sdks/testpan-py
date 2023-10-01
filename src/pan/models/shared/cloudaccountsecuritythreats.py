"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverlessdataaccessrisk as shared_serverlessdataaccessrisk
from ..shared import serverlesspolicyrisk as shared_serverlesspolicyrisk
from ..shared import serverlesspubliclyaccessiblerisk as shared_serverlesspubliclyaccessiblerisk
from ..shared import serverlesssecretsrisk as shared_serverlesssecretsrisk
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CloudAccountSecurityThreats:
    data_access_risk: Optional[shared_serverlessdataaccessrisk.ServerlessDataAccessRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataAccessRisk'), 'exclude': lambda f: f is None }})
    data_access_risk_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataAccessRiskCount'), 'exclude': lambda f: f is None }})
    is_unused_function: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isUnusedFunction'), 'exclude': lambda f: f is None }})
    policy_risk: Optional[shared_serverlesspolicyrisk.ServerlessPolicyRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyRisk'), 'exclude': lambda f: f is None }})
    policy_risk_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyRiskCount'), 'exclude': lambda f: f is None }})
    publicly_accessible_risk: Optional[shared_serverlesspubliclyaccessiblerisk.ServerlessPubliclyAccessibleRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publiclyAccessibleRisk'), 'exclude': lambda f: f is None }})
    publicly_accessible_risk_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('publiclyAccessibleRiskCount'), 'exclude': lambda f: f is None }})
    secrets_risk: Optional[shared_serverlesssecretsrisk.ServerlessSecretsRisk] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretsRisk'), 'exclude': lambda f: f is None }})
    secrets_risk_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretsRiskCount'), 'exclude': lambda f: f is None }})
    unused_function_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unusedFunctionCount'), 'exclude': lambda f: f is None }})
    
