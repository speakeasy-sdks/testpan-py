# APISecurityPolicies
(*api_security_policies*)

## Overview

APIs used to  define and manage api security policies

### Available Operations

* [delete_api_security_policy_policy_id_](#delete_api_security_policy_policy_id_) - Delete api security policy
* [get_api_security_policy](#get_api_security_policy) - Get a list of API security policies
* [get_api_security_policy_policy_id_delete_dependencies](#get_api_security_policy_policy_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified api security service
* [post_api_security_policy](#post_api_security_policy) - Add new API security policy
* [put_api_security_policy_policy_id_](#put_api_security_policy_policy_id_) - Edit Api security policy.

## delete_api_security_policy_policy_id_

Delete api security policy

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

req = operations.DeleteAPISecurityPolicyPolicyIDRequest(
    policy_id='04ae1a0e-dcb7-4d2b-b7a6-f7ca105f8c92',
)

res = s.api_security_policies.delete_api_security_policy_policy_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.DeleteAPISecurityPolicyPolicyIDRequest](../../models/operations/deleteapisecuritypolicypolicyidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.DeleteAPISecurityPolicyPolicyIDResponse](../../models/operations/deleteapisecuritypolicypolicyidresponse.md)**


## get_api_security_policy

Get a list of API security policies

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


res = s.api_security_policies.get_api_security_policy()

if res.api_security_policies is not None:
    # handle response
    pass
```


### Response

**[operations.GetAPISecurityPolicyResponse](../../models/operations/getapisecuritypolicyresponse.md)**


## get_api_security_policy_policy_id_delete_dependencies

get dependencies which need to be handled in order to delete specified api security service

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

req = operations.GetAPISecurityPolicyPolicyIDDeleteDependenciesRequest(
    policy_id='d3b9d79d-ed4f-4420-a583-071cdb02c3fd',
)

res = s.api_security_policies.get_api_security_policy_policy_id_delete_dependencies(req)

if res.api_security_policy_delete_dependencies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.GetAPISecurityPolicyPolicyIDDeleteDependenciesRequest](../../models/operations/getapisecuritypolicypolicyiddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |


### Response

**[operations.GetAPISecurityPolicyPolicyIDDeleteDependenciesResponse](../../models/operations/getapisecuritypolicypolicyiddeletedependenciesresponse.md)**


## post_api_security_policy

Add new API security policy

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

req = shared.APISecurityPolicyInput(
    category_conditions=shared.APISecurityPolicyCategoryConditions(
        conditions=[
            shared.APISecurityPolicyCategoryCondition(
                category='solid',
                highest_accepted_severity=shared.APISecurityPolicyRiskSeverity.NO_RISK,
            ),
        ],
    ),
    global_condition=shared.APISecurityPolicyGlobalCondition(
        highest_accepted_severity=shared.APISecurityPolicyRiskSeverity.MEDIUM,
    ),
    name='to',
)

res = s.api_security_policies.post_api_security_policy(req)

if res.api_security_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.APISecurityPolicyInput](../../models/shared/apisecuritypolicyinput.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PostAPISecurityPolicyResponse](../../models/operations/postapisecuritypolicyresponse.md)**


## put_api_security_policy_policy_id_

Edit Api security policy.

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

req = operations.PutAPISecurityPolicyPolicyIDRequest(
    api_security_policy_input=shared.APISecurityPolicyInput(
        category_conditions=shared.APISecurityPolicyCategoryConditions(
            conditions=[
                shared.APISecurityPolicyCategoryCondition(
                    category='deposit',
                    highest_accepted_severity=shared.APISecurityPolicyRiskSeverity.LOW,
                ),
            ],
        ),
        global_condition=shared.APISecurityPolicyGlobalCondition(
            highest_accepted_severity=shared.APISecurityPolicyRiskSeverity.HIGH,
        ),
        name='Buckinghamshire',
    ),
    policy_id='ef90a301-7448-4558-8280-7a30fd0b43b1',
)

res = s.api_security_policies.put_api_security_policy_policy_id_(req)

if res.api_security_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PutAPISecurityPolicyPolicyIDRequest](../../models/operations/putapisecuritypolicypolicyidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PutAPISecurityPolicyPolicyIDResponse](../../models/operations/putapisecuritypolicypolicyidresponse.md)**

