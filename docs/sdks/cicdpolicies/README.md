# CICDPolicies
(*.ci_cd_policies*)

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
    pass
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
    pass
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

if res.classes is not None:
    # handle response
    pass
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
    pass
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
    name='string',
    permission_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.IGNORE,
        permissible_vulnerability_level=shared.CDPipelineFindingRisk.NO_RISK,
    ),
    secret_cd_policy=shared.SecretsCdPolicyElement(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.NO_KNOWN_RISK,
    ),
    security_context_cd_policy=shared.CdPolicyElement(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_vulnerability_level=shared.CDPipelineFindingRisk.NO_RISK,
    ),
)

res = s.ci_cd_policies.post_cd_policy(req)

if res.cd_policy is not None:
    # handle response
    pass
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
    dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
    ),
    name='string',
    vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
        enforcement_option=shared.EnforcementOption.IGNORE,
        permissible_vulnerability_level=shared.VulnerabilitySeverity.LOW,
    ),
)

res = s.ci_cd_policies.post_ci_policy(req)

if res.ci_policy is not None:
    # handle response
    pass
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
    cd_policy=shared.CdPolicyInput(
        api_security_cd_policy=shared.APISecurityCdPolicyElement(
            api_security_profile='75218fad-dbdc-48d5-b27f-e1d8ecd9e791',
            enforcement_option=shared.EnforcementOption.FAIL,
        ),
        deployers=[
            '45666e4d-fb74-4ef6-9a81-a0d950f62fec',
        ],
        name='string',
        permission_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.NO_RISK,
        ),
        secret_cd_policy=shared.SecretsCdPolicyElement(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.CDPipelineSecretsFindingRisk.RISK_IDENTIFIED,
        ),
        security_context_cd_policy=shared.CdPolicyElement(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_vulnerability_level=shared.CDPipelineFindingRisk.MEDIUM,
        ),
    ),
    policy_id='8aed8fba-0d21-49b4-a2fd-e7a8937033a3',
)

res = s.ci_cd_policies.put_cd_policy_policy_id_(req)

if res.cd_policy is not None:
    # handle response
    pass
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
    ci_policy=shared.CiPolicyInput(
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
        ),
        name='string',
        vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_vulnerability_level=shared.VulnerabilitySeverity.UNKNOWN,
        ),
    ),
    policy_id='0c597151-5cdf-4e24-b5dc-fd347fd80ec5',
)

res = s.ci_cd_policies.put_ci_policy_policy_id_(req)

if res.ci_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PutCiPolicyPolicyIDRequest](../../models/operations/putcipolicypolicyidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PutCiPolicyPolicyIDResponse](../../models/operations/putcipolicypolicyidresponse.md)**

