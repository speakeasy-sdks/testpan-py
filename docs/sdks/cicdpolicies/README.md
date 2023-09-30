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
    policy_id='113917a9-a33e-48f7-8502-0a3844f10696',
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
    policy_id='04ff3f56-c960-40ce-85e7-ad7f8b628cd7',
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
        api_security_profile='e20e4f6e-3e04-4f9f-8904-433d8246a999',
        enforcement_option=shared.EnforcementOption.FAIL,
    ),
    deployers=[
        'aede075c-3164-444b-a1e6-c4ecee9d9042',
    ],
    description='User-friendly composite Graphic Interface',
    name='Concrete',
    permission_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.IGNORE,
        permissible_vulnerability_level=shared.CDPipelineFindingRisk.HIGH,
    ),
    secret_cd_policy=shared.SecretsCdPolicyElement(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.NO_KNOWN_RISK,
    ),
    security_context_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.IGNORE,
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
    description='Adaptive scalable portal',
    dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
    ),
    name='local Tom',
    vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.VulnerabilitySeverity.LOW,
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
            api_security_profile='75218fad-dbdc-48d5-b27f-e1d8ecd9e791',
            enforcement_option=shared.EnforcementOption.FAIL,
        ),
        deployers=[
            '45666e4d-fb74-4ef6-9a81-a0d950f62fec',
        ],
        description='Enterprise-wide 4th generation process improvement',
        name='Berkshire quantifying',
        permission_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.HIGH,
        ),
        secret_cd_policy=shared.SecretsCdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.RISK_IDENTIFIED,
        ),
        security_context_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.HIGH,
        ),
    ),
    policy_id='0d219b4a-2fde-47a8-9370-33a3f0a96f23',
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
        description='Public-key 24 hour pricing structure',
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
        ),
        name='primary transform drive',
        vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.VulnerabilitySeverity.CRITICAL,
        ),
    ),
    policy_id='e24f5dcf-d347-4fd8-8ec5-8c84ce879afb',
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

