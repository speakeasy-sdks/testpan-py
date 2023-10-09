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
        password="",
        username="",
    ),
)


res = s.cluster_events_policies.get_kubernetes_api_policy()

if res.kubernetes_api_policy is not None:
    # handle response
```


### Response

**[operations.GetKubernetesAPIPolicyResponse](../../models/operations/getkubernetesapipolicyresponse.md)**


## get_kubernetes_api_policy_history

Get the history of the Kubernetes API policies

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


res = s.cluster_events_policies.get_kubernetes_api_policy_history()

if res.kubernetes_api_policy_histories is not None:
    # handle response
```


### Response

**[operations.GetKubernetesAPIPolicyHistoryResponse](../../models/operations/getkubernetesapipolicyhistoryresponse.md)**


## get_kubernetes_api_policy_kubernetes_resources

Get the Kubernetes resource list

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


res = s.cluster_events_policies.get_kubernetes_api_policy_kubernetes_resources()

if res.kubernetes_resources is not None:
    # handle response
```


### Response

**[operations.GetKubernetesAPIPolicyKubernetesResourcesResponse](../../models/operations/getkubernetesapipolicykubernetesresourcesresponse.md)**


## get_kubernetes_api_policy_kubernetes_users

Get the Kubernetes user list

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


res = s.cluster_events_policies.get_kubernetes_api_policy_kubernetes_users()

if res.kubernetes_users_by_types is not None:
    # handle response
```


### Response

**[operations.GetKubernetesAPIPolicyKubernetesUsersResponse](../../models/operations/getkubernetesapipolicykubernetesusersresponse.md)**


## get_kubernetes_api_policy_recommended_rules

Get the recommended Kubernetes API rules

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


res = s.cluster_events_policies.get_kubernetes_api_policy_recommended_rules()

if res.recommended_kubernetes_api_rules is not None:
    # handle response
```


### Response

**[operations.GetKubernetesAPIPolicyRecommendedRulesResponse](../../models/operations/getkubernetesapipolicyrecommendedrulesresponse.md)**


## put_kubernetes_api_policy

set the current Kubernetes API policy

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

req = shared.KubernetesAPIPolicy(
    default_rule=shared.DefaultKubernetesAPIRule(),
    user_rules=[
        shared.KubernetesAPIRule(
            kubernetes_api_rule_type=shared.KubernetesAPIRuleKubernetesAPIRuleType.KUBERNETES_API_RECOMMENDED_RULE,
        ),
    ],
)

res = s.cluster_events_policies.put_kubernetes_api_policy(req)

if res.kubernetes_api_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.KubernetesAPIPolicy](../../models/shared/kubernetesapipolicy.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PutKubernetesAPIPolicyResponse](../../models/operations/putkubernetesapipolicyresponse.md)**

