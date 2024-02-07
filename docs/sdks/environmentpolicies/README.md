# EnvironmentPolicies
(*environment_policies*)

## Overview

APIs used to  define and manage environment policies

### Available Operations

* [get_apps_policy](#get_apps_policy) - Get the current Apps policy
* [get_apps_policy_history](#get_apps_policy_history) - Get the history of Apps policies
* [get_apps_policy_search_options](#get_apps_policy_search_options) - Get the current Apps policy filter option
* [put_apps_policy](#put_apps_policy) - Set the current Apps policy

## get_apps_policy

Get the current Apps policy

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppsPolicyRequest()

res = s.environment_policies.get_apps_policy(req)

if res.app_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAppsPolicyRequest](../../models/operations/getappspolicyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetAppsPolicyResponse](../../models/operations/getappspolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_apps_policy_history

Get the history of Apps policies

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.environment_policies.get_apps_policy_history()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetAppsPolicyHistoryResponse](../../models/operations/getappspolicyhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_apps_policy_search_options

Get the current Apps policy filter option

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppsPolicySearchOptionsRequest()

res = s.environment_policies.get_apps_policy_search_options(req)

if res.policy_filter_search_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAppsPolicySearchOptionsRequest](../../models/operations/getappspolicysearchoptionsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetAppsPolicySearchOptionsResponse](../../models/operations/getappspolicysearchoptionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_apps_policy

Set the current Apps policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.AppPolicy(
    unidentified_pods_rule=shared.UnidentifiedPodsRule(
        action=shared.UnidentifiedPodsRuleAction.BLOCK,
    ),
    user_rules=[
        shared.AppRule(
            name='string',
            rule_type_properties=shared.AppRuleType(
                rule_type=shared.RuleType.VIOLATION_RULE_TYPE,
            ),
            status=shared.AppRuleStatus.DELETED,
            app=shared.WorkloadRuleType(
                workload_rule_type=shared.WorkloadRuleTypeWorkloadRuleType.APP_NAME_WORKLOAD_RULE_TYPE,
            ),
            scope=shared.WorkloadRuleScopeType(
                workload_rule_scope_type=shared.WorkloadRuleScopeTypeEnum.ANY_RULE_TYPE,
            ),
        ),
    ],
)

res = s.environment_policies.put_apps_policy(req)

if res.app_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.AppPolicy](../../models/shared/apppolicy.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PutAppsPolicyResponse](../../models/operations/putappspolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
