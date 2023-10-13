# Advisor
(*advisor*)

## Overview

APIs used to get policy recommendations

### Available Operations

* [get_advisor_cluster_event_rules](#get_advisor_cluster_event_rules) - Returns a list of suggested cluster event rules
* [get_advisor_connection_rules](#get_advisor_connection_rules) - Returns a list of suggested connection rules
* [get_advisor_environment](#get_advisor_environment) - Returns a list of suggested kubernetes environments
* [get_advisor_environment_rules](#get_advisor_environment_rules) - Returns a list of suggested environment rules
* [get_advisor_pod_security_policy](#get_advisor_pod_security_policy) - Returns a list of suggested kubernetes Pod Security Standards
* [get_advisor_queue_advisor_type_](#get_advisor_queue_advisor_type_) - Get status for policy advisor background job
* [post_advisor_run](#post_advisor_run) - Runs the policy advisor

## get_advisor_cluster_event_rules

Returns a list of suggested cluster event rules

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


res = s.advisor.get_advisor_cluster_event_rules()

if res.cluster_event_rule_recommendation_periods is not None:
    # handle response
    pass
```


### Response

**[operations.GetAdvisorClusterEventRulesResponse](../../models/operations/getadvisorclustereventrulesresponse.md)**


## get_advisor_connection_rules

Returns a list of suggested connection rules

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


res = s.advisor.get_advisor_connection_rules()

if res.connections_rule_recommendation_periods is not None:
    # handle response
    pass
```


### Response

**[operations.GetAdvisorConnectionRulesResponse](../../models/operations/getadvisorconnectionrulesresponse.md)**


## get_advisor_environment

Returns a list of suggested kubernetes environments

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


res = s.advisor.get_advisor_environment()

if res.environment_recommendation_periods is not None:
    # handle response
    pass
```


### Response

**[operations.GetAdvisorEnvironmentResponse](../../models/operations/getadvisorenvironmentresponse.md)**


## get_advisor_environment_rules

Returns a list of suggested environment rules

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


res = s.advisor.get_advisor_environment_rules()

if res.environment_rules_recommendation_periods is not None:
    # handle response
    pass
```


### Response

**[operations.GetAdvisorEnvironmentRulesResponse](../../models/operations/getadvisorenvironmentrulesresponse.md)**


## get_advisor_pod_security_policy

Returns a list of suggested kubernetes Pod Security Standards

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


res = s.advisor.get_advisor_pod_security_policy()

if res.pod_security_policy_recommendation_periods is not None:
    # handle response
    pass
```


### Response

**[operations.GetAdvisorPodSecurityPolicyResponse](../../models/operations/getadvisorpodsecuritypolicyresponse.md)**


## get_advisor_queue_advisor_type_

Get status for policy advisor background job

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

req = operations.GetAdvisorQueueAdvisorTypeRequest(
    advisor_type=operations.GetAdvisorQueueAdvisorTypeAdvisorType.DEPLOYMENT_RULES,
)

res = s.advisor.get_advisor_queue_advisor_type_(req)

if res.policy_advisor_state is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAdvisorQueueAdvisorTypeRequest](../../models/operations/getadvisorqueueadvisortyperequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetAdvisorQueueAdvisorTypeResponse](../../models/operations/getadvisorqueueadvisortyperesponse.md)**


## post_advisor_run

Runs the policy advisor

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

req = operations.PostAdvisorRunRequest(
    policy_advisor_type=operations.PostAdvisorRunPolicyAdvisorType.API_RULES,
)

res = s.advisor.post_advisor_run(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PostAdvisorRunRequest](../../models/operations/postadvisorrunrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PostAdvisorRunResponse](../../models/operations/postadvisorrunresponse.md)**

