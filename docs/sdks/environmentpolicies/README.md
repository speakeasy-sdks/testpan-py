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
        password="",
        username="",
    ),
)

req = operations.GetAppsPolicyRequest(
    policy_filter='Secured Hybrid',
)

res = s.environment_policies.get_apps_policy(req)

if res.app_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAppsPolicyRequest](../../models/operations/getappspolicyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetAppsPolicyResponse](../../models/operations/getappspolicyresponse.md)**


## get_apps_policy_history

Get the history of Apps policies

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


res = s.environment_policies.get_apps_policy_history()

if res.app_policy_histories is not None:
    # handle response
```


### Response

**[operations.GetAppsPolicyHistoryResponse](../../models/operations/getappspolicyhistoryresponse.md)**


## get_apps_policy_search_options

Get the current Apps policy filter option

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

req = operations.GetAppsPolicySearchOptionsRequest(
    name_filter='Ball Clothing Classical',
)

res = s.environment_policies.get_apps_policy_search_options(req)

if res.policy_filter_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAppsPolicySearchOptionsRequest](../../models/operations/getappspolicysearchoptionsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetAppsPolicySearchOptionsResponse](../../models/operations/getappspolicysearchoptionsresponse.md)**


## put_apps_policy

Set the current Apps policy

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

req = shared.AppPolicy(
    default_rule=shared.DefaultRule.DETECT_ALL,
    unidentified_pods_rule=shared.UnidentifiedPodsRule(
        action=shared.UnidentifiedPodsRuleAction.BLOCK,
        name='Bolivia Peso Gasoline',
    ),
    user_rules=[
        shared.AppRule(
            app=shared.WorkloadRuleType(
                workload_rule_type=shared.WorkloadRuleTypeWorkloadRuleType.APP_NAME_WORKLOAD_RULE_TYPE,
            ),
            group_name='Elegant mole Bronze',
            id='c913f708-35e4-4a31-9380-1bc9778ebe02',
            name='Delaware cultivate',
            rule_origin=shared.AppRuleOrigin.SYSTEM,
            rule_type_properties=shared.AppRuleType(
                rule_type=shared.AppRuleTypeRuleType.VIOLATION_RULE_TYPE,
            ),
            scope=shared.WorkloadRuleScopeType(
                workload_rule_scope_type=shared.WorkloadRuleScopeTypeEnum.ANY_RULE_TYPE,
            ),
            status=shared.AppRuleStatus.DELETED,
        ),
    ],
)

res = s.environment_policies.put_apps_policy(req)

if res.app_policy is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.AppPolicy](../../models/shared/apppolicy.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PutAppsPolicyResponse](../../models/operations/putappspolicyresponse.md)**
