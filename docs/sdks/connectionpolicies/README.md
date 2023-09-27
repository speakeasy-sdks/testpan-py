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

req = operations.GetConnectionsPolicyRequest(
    policy_filter='quibusdam',
)

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
    kubernetes_cluster_id='905a972e-0567-4282-a7b2-d309470bf7a4',
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
    kubernetes_cluster_id='fa87cf53-5a6f-4ae5-8ebf-60c321f023b7',
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

req = operations.GetConnectionsPolicySearchOptionsRequest(
    name_filter='nostrum',
)

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
    default_rule=shared.DefaultConnectionRule(
        action=shared.ConnectionRuleAction.ENCRYPT_DIRECT,
        type=shared.DefaultConnectionRuleType.ALLOW_ALL,
    ),
    direct_pod_rule=shared.DirectPodIPConnectionRule(
        action=shared.DirectPodIPConnectionRuleAction.DETECT,
        is_disabled=False,
        name='Stella Witting MD',
    ),
    user_rules=[
        shared.ConnectionsRule(
            action=shared.ConnectionRuleAction.DETECT,
            destination=shared.ConnectionRulePart(
                connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.EXPANSION_LABELS_CONNECTION_RULE_PART,
            ),
            group_name='minus',
            id='8df79f0a-396d-490c-b64b-7c15dfbace18',
            is_rule_active=False,
            layer7_settings=shared.Layer7SettingsPart(
                layer7_protocol=shared.Layer7SettingsPartLayer7Protocol.KAFKA_LAYER_PART,
            ),
            name='Samuel Russel',
            rule_origin=shared.ConnectionRuleOrigin.SYSTEM,
            rule_type=shared.NetworkConnectionRuleType.USER_RULE,
            source=shared.ConnectionRulePart(
                connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.EXPANSION_NAME_CONNECTION_RULE_PART,
            ),
            status=shared.ConnectionsRuleStatus.DISABLED,
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

