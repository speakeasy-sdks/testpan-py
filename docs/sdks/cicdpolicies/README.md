# CICDPolicies
(*ci_cd_policies*)

## Overview

APIs used to  define and manage CI/CD policies

### Available Operations

* [delete_cd_policy_policy_id_](#delete_cd_policy_policy_id_) - Delete CD policy
* [delete_ci_policy_policy_id_](#delete_ci_policy_policy_id_) - Delete CI policy
* [get_cd_policy](#get_cd_policy) - Get the current CD policy
* [get_ci_policy](#get_ci_policy) - Get the current CI policy
* [post_cd_policy](#post_cd_policy) - Set the current CD policy. At least one CdPolicyElement should be present
* [post_ci_policy](#post_ci_policy) - Set the current CI policy
* [put_cd_policy_policy_id_](#put_cd_policy_policy_id_) - Edit CD policy. At least one CdPolicyElement should be present
* [put_ci_policy_policy_id_](#put_ci_policy_policy_id_) - Edit CI policy

## delete_cd_policy_policy_id_

Delete CD policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.DeleteCdPolicyPolicyIDRequest(
    policy_id='45626d43-6813-4f16-99f5-fce6c556146c',
)

res = s.ci_cd_policies.delete_cd_policy_policy_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteCdPolicyPolicyIDRequest](../../models/operations/deletecdpolicypolicyidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteCdPolicyPolicyIDResponse](../../models/operations/deletecdpolicypolicyidresponse.md)**


## delete_ci_policy_policy_id_

Delete CI policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.DeleteCiPolicyPolicyIDRequest(
    policy_id='3e250fb0-08c4-42e1-81aa-c366c8dd6b14',
)

res = s.ci_cd_policies.delete_ci_policy_policy_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteCiPolicyPolicyIDRequest](../../models/operations/deletecipolicypolicyidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteCiPolicyPolicyIDResponse](../../models/operations/deletecipolicypolicyidresponse.md)**


## get_cd_policy

Get the current CD policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)


res = s.ci_cd_policies.get_cd_policy()

if res.cd_policies is not None:
    # handle response
```


### Response

**[operations.GetCdPolicyResponse](../../models/operations/getcdpolicyresponse.md)**


## get_ci_policy

Get the current CI policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)


res = s.ci_cd_policies.get_ci_policy()

if res.ci_policy is not None:
    # handle response
```


### Response

**[operations.GetCiPolicyResponse](../../models/operations/getcipolicyresponse.md)**


## post_cd_policy

Set the current CD policy. At least one CdPolicyElement should be present

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.CdPolicyInput(
    api_security_cd_policy=shared.APISecurityCdPolicyElement(
        api_security_profile='42907474-778a-47bd-866d-28c10ab3cdca',
        enforcement_option=shared.EnforcementOption.FAIL,
    ),
    deployers=[
        '251904e5-23c7-4e0b-8717-8e4796f2a70c',
    ],
    description='eum',
    name='Dwayne Cronin',
    permission_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.IGNORE,
        permissible_vulnerability_level=shared.CDPipelineFindingRisk.MEDIUM,
    ),
    secret_cd_policy=shared.SecretsCdPolicyElement(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.RISK_IDENTIFIED,
    ),
    security_context_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.CDPipelineFindingRisk.NO_RISK,
    ),
)

res = s.ci_cd_policies.post_cd_policy(req)

if res.cd_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.CdPolicyInput](../../models/shared/cdpolicyinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostCdPolicyResponse](../../models/operations/postcdpolicyresponse.md)**


## post_ci_policy

Set the current CI policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.CiPolicyInput(
    description='nisi',
    dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
    ),
    name='Norma Christiansen',
    vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
        enforcement_option=shared.EnforcementOption.IGNORE,
        permissible_vulnerability_level=shared.VulnerabilitySeverity.UNKNOWN,
    ),
)

res = s.ci_cd_policies.post_ci_policy(req)

if res.ci_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.CiPolicyInput](../../models/shared/cipolicyinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostCiPolicyResponse](../../models/operations/postcipolicyresponse.md)**


## put_cd_policy_policy_id_

Edit CD policy. At least one CdPolicyElement should be present

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutCdPolicyPolicyIDRequest(
    cd_policy_input=shared.CdPolicyInput(
        api_security_cd_policy=shared.APISecurityCdPolicyElement(
            api_security_profile='7ee17cbe-61e6-4b7b-95bc-0ab3c20c4f37',
            enforcement_option=shared.EnforcementOption.IGNORE,
        ),
        deployers=[
            '9fd871f9-9dd2-4efd-921a-a6f1e674bdb0',
        ],
        description='aliquam',
        name='Samuel Hermiston',
        permission_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.NO_RISK,
        ),
        secret_cd_policy=shared.SecretsCdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.NO_KNOWN_RISK,
        ),
        security_context_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.MEDIUM,
        ),
    ),
    policy_id='8ea19f1d-1705-4133-9d08-086a1840394c',
)

res = s.ci_cd_policies.put_cd_policy_policy_id_(req)

if res.cd_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PutCdPolicyPolicyIDRequest](../../models/operations/putcdpolicypolicyidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PutCdPolicyPolicyIDResponse](../../models/operations/putcdpolicypolicyidresponse.md)**


## put_ci_policy_policy_id_

Edit CI policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutCiPolicyPolicyIDRequest(
    ci_policy_input=shared.CiPolicyInput(
        description='explicabo',
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
        ),
        name='Jean Wunsch',
        vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.VulnerabilitySeverity.LOW,
        ),
    ),
    policy_id='f0642dac-7af5-415c-8413-aa63aae8d678',
)

res = s.ci_cd_policies.put_ci_policy_policy_id_(req)

if res.ci_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PutCiPolicyPolicyIDRequest](../../models/operations/putcipolicypolicyidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PutCiPolicyPolicyIDResponse](../../models/operations/putcipolicypolicyidresponse.md)**

