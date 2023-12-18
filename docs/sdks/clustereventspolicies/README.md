# ClusterEventsPolicies
(*cluster_events_policies*)

## Overview

APIs used to  define and manage cluster events policies

### Available Operations

* [get_kubernetes_api_policy](#get_kubernetes_api_policy) - Get current Kubernetes API policy
* [get_kubernetes_api_policy_history](#get_kubernetes_api_policy_history) - Get the history of the Kubernetes API policies
* [get_kubernetes_api_policy_kubernetes_resources](#get_kubernetes_api_policy_kubernetes_resources) - Get the Kubernetes resource list
* [get_kubernetes_api_policy_kubernetes_users](#get_kubernetes_api_policy_kubernetes_users) - Get the Kubernetes user list
* [get_kubernetes_api_policy_recommended_rules](#get_kubernetes_api_policy_recommended_rules) - Get the recommended Kubernetes API rules
* [put_kubernetes_api_policy](#put_kubernetes_api_policy) - set the current Kubernetes API policy

## get_kubernetes_api_policy

Get current Kubernetes API policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy()

if res.kubernetes_api_policy is not None:
    # handle response
    pass
```


### Response

**[operations.GetKubernetesAPIPolicyResponse](../../models/operations/getkubernetesapipolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_api_policy_history

Get the history of the Kubernetes API policies

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy_history()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetKubernetesAPIPolicyHistoryResponse](../../models/operations/getkubernetesapipolicyhistoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_api_policy_kubernetes_resources

Get the Kubernetes resource list

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy_kubernetes_resources()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetKubernetesAPIPolicyKubernetesResourcesResponse](../../models/operations/getkubernetesapipolicykubernetesresourcesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_api_policy_kubernetes_users

Get the Kubernetes user list

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy_kubernetes_users()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetKubernetesAPIPolicyKubernetesUsersResponse](../../models/operations/getkubernetesapipolicykubernetesusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_api_policy_recommended_rules

Get the recommended Kubernetes API rules

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy_recommended_rules()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetKubernetesAPIPolicyRecommendedRulesResponse](../../models/operations/getkubernetesapipolicyrecommendedrulesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_kubernetes_api_policy

set the current Kubernetes API policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.KubernetesAPIPolicy(
    default_rule=shared.DefaultKubernetesAPIRule(),
    user_rules=[
        shared.KubernetesAPIRule(
            kubernetes_api_rule_type=shared.KubernetesAPIRuleType.KUBERNETES_API_RECOMMENDED_RULE,
        ),
    ],
)

res = s.cluster_events_policies.put_kubernetes_api_policy(req)

if res.kubernetes_api_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.KubernetesAPIPolicy](../../models/shared/kubernetesapipolicy.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PutKubernetesAPIPolicyResponse](../../models/operations/putkubernetesapipolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
