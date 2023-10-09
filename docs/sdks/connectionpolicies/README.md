# ConnectionPolicies
(*connection_policies*)

## Overview

APIs used to  define and manage connection policies

### Available Operations

* [get_connections_policy](#get_connections_policy) - Get current connection policy
* [get_connections_policy_history](#get_connections_policy_history) - Get the history of the connection policies
* [get_connections_policy_kafka_actions](#get_connections_policy_kafka_actions) - Get the a list of kafka actions
* [get_connections_policy_kafka_kubernetes_cluster_id_brokers](#get_connections_policy_kafka_kubernetes_cluster_id_brokers) - Get the a list of kafka brokers
* [get_connections_policy_kafka_kubernetes_cluster_id_topics](#get_connections_policy_kafka_kubernetes_cluster_id_topics) - Get the a list of kafka topics
* [get_connections_policy_search_options](#get_connections_policy_search_options) - Get the current connection policy filter option
* [get_serverless_policy_history](#get_serverless_policy_history) - Get the history of the serverless policies
* [put_connections_policy](#put_connections_policy) - Set the current connection policy

## get_connections_policy

Get current connection policy

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

req = operations.GetConnectionsPolicyRequest()

res = s.connection_policies.get_connections_policy(req)

if res.connections_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetConnectionsPolicyRequest](../../models/operations/getconnectionspolicyrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetConnectionsPolicyResponse](../../models/operations/getconnectionspolicyresponse.md)**


## get_connections_policy_history

Get the history of the connection policies

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


res = s.connection_policies.get_connections_policy_history()

if res.connection_policy_histories is not None:
    # handle response
```


### Response

**[operations.GetConnectionsPolicyHistoryResponse](../../models/operations/getconnectionspolicyhistoryresponse.md)**


## get_connections_policy_kafka_actions

Get the a list of kafka actions

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


res = s.connection_policies.get_connections_policy_kafka_actions()

if res.get_connections_policy_kafka_actions_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetConnectionsPolicyKafkaActionsResponse](../../models/operations/getconnectionspolicykafkaactionsresponse.md)**


## get_connections_policy_kafka_kubernetes_cluster_id_brokers

Get the a list of kafka brokers

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

req = operations.GetConnectionsPolicyKafkaKubernetesClusterIDBrokersRequest(
    kubernetes_cluster_id='adf9ba62-2ac1-4d6f-9118-9c1b46212731',
)

res = s.connection_policies.get_connections_policy_kafka_kubernetes_cluster_id_brokers(req)

if res.get_connections_policy_kafka_kubernetes_cluster_id_brokers_200_application_json_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetConnectionsPolicyKafkaKubernetesClusterIDBrokersRequest](../../models/operations/getconnectionspolicykafkakubernetesclusteridbrokersrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetConnectionsPolicyKafkaKubernetesClusterIDBrokersResponse](../../models/operations/getconnectionspolicykafkakubernetesclusteridbrokersresponse.md)**


## get_connections_policy_kafka_kubernetes_cluster_id_topics

Get the a list of kafka topics

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

req = operations.GetConnectionsPolicyKafkaKubernetesClusterIDTopicsRequest(
    kubernetes_cluster_id='fa0332c3-3e86-408a-93f6-0cc1de785419',
)

res = s.connection_policies.get_connections_policy_kafka_kubernetes_cluster_id_topics(req)

if res.get_connections_policy_kafka_kubernetes_cluster_id_topics_200_application_json_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetConnectionsPolicyKafkaKubernetesClusterIDTopicsRequest](../../models/operations/getconnectionspolicykafkakubernetesclusteridtopicsrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetConnectionsPolicyKafkaKubernetesClusterIDTopicsResponse](../../models/operations/getconnectionspolicykafkakubernetesclusteridtopicsresponse.md)**


## get_connections_policy_search_options

Get the current connection policy filter option

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

req = operations.GetConnectionsPolicySearchOptionsRequest()

res = s.connection_policies.get_connections_policy_search_options(req)

if res.policy_filter_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetConnectionsPolicySearchOptionsRequest](../../models/operations/getconnectionspolicysearchoptionsrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.GetConnectionsPolicySearchOptionsResponse](../../models/operations/getconnectionspolicysearchoptionsresponse.md)**


## get_serverless_policy_history

Get the history of the serverless policies

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


res = s.connection_policies.get_serverless_policy_history()

if res.connection_policy_histories is not None:
    # handle response
```


### Response

**[operations.GetServerlessPolicyHistoryResponse](../../models/operations/getserverlesspolicyhistoryresponse.md)**


## put_connections_policy

Set the current connection policy

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

req = shared.ConnectionsPolicy(
    default_rule=shared.DefaultConnectionRule(),
    direct_pod_rule=shared.DirectPodIPConnectionRule(
        action=shared.DirectPodIPConnectionRuleAction.DETECT,
    ),
    user_rules=[
        shared.ConnectionsRule(
            action=shared.ConnectionRuleAction.ENCRYPT_DIRECT,
            destination=shared.ConnectionRulePart(
                connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.KAFKA_CONNECTION_RULE_PART,
            ),
            layer7_settings=shared.Layer7SettingsPart(),
            name='violet yet honestly',
            source=shared.ConnectionRulePart(
                connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_NAME_CONNECTION_RULE_PART,
            ),
        ),
    ],
)

res = s.connection_policies.put_connections_policy(req)

if res.connections_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.ConnectionsPolicy](../../models/shared/connectionspolicy.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PutConnectionsPolicyResponse](../../models/operations/putconnectionspolicyresponse.md)**

