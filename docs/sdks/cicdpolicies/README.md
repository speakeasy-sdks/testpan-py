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
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_ci_policy_policy_id_

Delete CI policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_cd_policy

Get the current CD policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.ci_cd_policies.get_cd_policy()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetCdPolicyResponse](../../models/operations/getcdpolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_ci_policy

Get the current CI policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.ci_cd_policies.get_ci_policy()

if res.ci_policy is not None:
    # handle response
    pass
```


### Response

**[operations.GetCiPolicyResponse](../../models/operations/getcipolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_cd_policy

Set the current CD policy. At least one CdPolicyElement should be present

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.CdPolicyInput(
    deployers=[
        'e20e4f6e-3e04-4f9f-8904-433d8246a999',
    ],
    name='string',
    api_security_cd_policy=shared.APISecurityCdPolicyElement(
        api_security_profile='4aede075-c316-4444-be1e-6c4ecee9d904',
        enforcement_option=shared.EnforcementOption.FAIL,
    ),
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_ci_policy

Set the current CI policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.CiPolicyInput(
    name='string',
    dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
        enforcement_option=shared.EnforcementOption.FAIL,
        permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
    ),
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_cd_policy_policy_id_

Edit CD policy. At least one CdPolicyElement should be present

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutCdPolicyPolicyIDRequest(
    cd_policy=shared.CdPolicyInput(
        deployers=[
            '75218fad-dbdc-48d5-b27f-e1d8ecd9e791',
        ],
        name='string',
        api_security_cd_policy=shared.APISecurityCdPolicyElement(
            api_security_profile='545666e4-dfb7-44ef-ada8-1a0d950f62fe',
            enforcement_option=shared.EnforcementOption.IGNORE,
        ),
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_ci_policy_policy_id_

Edit CI policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutCiPolicyPolicyIDRequest(
    ci_policy=shared.CiPolicyInput(
        name='string',
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.IGNORE,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
        ),
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
