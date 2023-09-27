# Cd
(*cd*)

## Overview

APIs used to query for CD pipelines results

### Available Operations

* [delete_cd_rule_id_connections_rule](#delete_cd_rule_id_connections_rule) - delete a cd connection rule.
* [delete_cd_rule_id_serverless_rule](#delete_cd_rule_id_serverless_rule) - delete a cd serverless rule.
* [get_cd](#get_cd) - Get all the CD pipelines results
* [get_cd_resource_id_](#get_cd_resource_id_) - Get A single CD pipeline results
* [get_cd_rule_id_connections_rule](#get_cd_rule_id_connections_rule) - get a cd connection rule.
* [get_cd_rule_id_serverless_rule](#get_cd_rule_id_serverless_rule) - get a cd serverless rule.
* [post_cd_connections_rule](#post_cd_connections_rule) - Adds cd connection rule.
* [post_cd_serverless_rule](#post_cd_serverless_rule) - Adds cd serverless rule.
* [put_cd_rule_id_connections_rule](#put_cd_rule_id_connections_rule) - update a cd connection rule.
* [put_cd_rule_id_serverless_rule](#put_cd_rule_id_serverless_rule) - update a cd serverless rule.

## delete_cd_rule_id_connections_rule

delete a cd connection rule.

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

req = operations.DeleteCdRuleIDConnectionsRuleRequest(
    rule_id='e1e91e45-0ad2-4abd-8426-9802d502a94b',
)

res = s.cd.delete_cd_rule_id_connections_rule(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteCdRuleIDConnectionsRuleRequest](../../models/operations/deletecdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteCdRuleIDConnectionsRuleResponse](../../models/operations/deletecdruleidconnectionsruleresponse.md)**


## delete_cd_rule_id_serverless_rule

delete a cd serverless rule.

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

req = operations.DeleteCdRuleIDServerlessRuleRequest(
    rule_id='b4f63c96-9e9a-43ef-a77d-fb14cd66ae39',
)

res = s.cd.delete_cd_rule_id_serverless_rule(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCdRuleIDServerlessRuleRequest](../../models/operations/deletecdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.DeleteCdRuleIDServerlessRuleResponse](../../models/operations/deletecdruleidserverlessruleresponse.md)**


## get_cd

Get all the CD pipelines results

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetCdRequest(
    end_time=dateutil.parser.isoparse('2022-02-13T03:59:53.583Z'),
    max_results=9654.17,
    offset=6925.32,
    resource_name='provident',
    sort_dir=operations.GetCdSortDir.DESC,
    sort_key=operations.GetCdSortKey.STATUS,
    start_time=dateutil.parser.isoparse('2021-12-07T18:13:34.827Z'),
)

res = s.cd.get_cd(req)

if res.cd_pipeline_results is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [operations.GetCdRequest](../../models/operations/getcdrequest.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetCdResponse](../../models/operations/getcdresponse.md)**


## get_cd_resource_id_

Get A single CD pipeline results

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

req = operations.GetCdResourceIDRequest(
    resource_id='f3a66997-074b-4a44-a9b6-e2141959890a',
    sort_dir=operations.GetCdResourceIDSortDir.DESC,
    sort_key=operations.GetCdResourceIDSortKey.RISK,
)

res = s.cd.get_cd_resource_id_(req)

if res.cd_pipeline_resource_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCdResourceIDRequest](../../models/operations/getcdresourceidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetCdResourceIDResponse](../../models/operations/getcdresourceidresponse.md)**


## get_cd_rule_id_connections_rule

get a cd connection rule.

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

req = operations.GetCdRuleIDConnectionsRuleRequest(
    rule_id='a563e251-6fe4-4c8b-b11e-5b7fd2ed0289',
)

res = s.cd.get_cd_rule_id_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCdRuleIDConnectionsRuleRequest](../../models/operations/getcdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetCdRuleIDConnectionsRuleResponse](../../models/operations/getcdruleidconnectionsruleresponse.md)**


## get_cd_rule_id_serverless_rule

get a cd serverless rule.

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

req = operations.GetCdRuleIDServerlessRuleRequest(
    rule_id='21cddc69-2601-4fb5-b6b0-d5f0d30c5fbb',
)

res = s.cd.get_cd_rule_id_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCdRuleIDServerlessRuleRequest](../../models/operations/getcdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCdRuleIDServerlessRuleResponse](../../models/operations/getcdruleidserverlessruleresponse.md)**


## post_cd_connections_rule

Adds cd connection rule.

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

req = shared.CdConnectionRule(
    action=shared.ConnectionRuleAction.DETECT,
    destination=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.POD_ANY_CONNECTION_RULE_PART,
    ),
    group_name='totam',
    id='7053202c-73d5-4fe9-b90c-28909b3fe49a',
    name='Ervin McLaughlin',
    source=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.API_SERVICE_CONNECTION_RULE_PART,
    ),
    status=shared.CdConnectionRuleStatus.ENABLED,
)

res = s.cd.post_cd_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.CdConnectionRule](../../models/shared/cdconnectionrule.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostCdConnectionsRuleResponse](../../models/operations/postcdconnectionsruleresponse.md)**


## post_cd_serverless_rule

Adds cd serverless rule.

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

req = shared.CdServerlessRule(
    action=shared.ServerlessRuleAction.ALLOW,
    group_name='aliquid',
    id='33323f9b-77f3-4a41-8067-4ebf69280d1b',
    name='Ted Kling',
    rule=shared.ServerlessRuleType(
        serverless_function_validation=shared.ServerlessFunctionValidation(
            data_access_risk=shared.ServerlessDataAccessRisk.LOW,
            function_permission_risk=shared.ServerlessPolicyRisk.CRITICAL,
            is_unused_function=False,
            publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.MEDIUM,
            risk=shared.ServerlessFunctionRiskLevel.CRITICAL,
            secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
            vulnerability=shared.VulnerabilitySeverity.LOW,
        ),
        serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
    ),
    scope=[
        shared.ServerlessRuleScope(
            cloud_account='id',
            regions=[
                'saepe',
            ],
        ),
    ],
    status=shared.ServerlessRuleStatus.ENABLED,
)

res = s.cd.post_cd_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.CdServerlessRule](../../models/shared/cdserverlessrule.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostCdServerlessRuleResponse](../../models/operations/postcdserverlessruleresponse.md)**


## put_cd_rule_id_connections_rule

update a cd connection rule.

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

req = operations.PutCdRuleIDConnectionsRuleRequest(
    cd_connection_rule=shared.CdConnectionRule(
        action=shared.ConnectionRuleAction.DETECT,
        destination=shared.ConnectionRulePart(
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_NAME_CONNECTION_RULE_PART,
        ),
        group_name='amet',
        id='ce5e6a95-d8a0-4d44-ace2-af7a73cf3be4',
        name='Florence Will',
        source=shared.ConnectionRulePart(
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_NAME_CONNECTION_RULE_PART,
        ),
        status=shared.CdConnectionRuleStatus.DELETED,
    ),
    rule_id='326b5a73-429c-4db1-a842-2bb679d23227',
)

res = s.cd.put_cd_rule_id_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutCdRuleIDConnectionsRuleRequest](../../models/operations/putcdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutCdRuleIDConnectionsRuleResponse](../../models/operations/putcdruleidconnectionsruleresponse.md)**


## put_cd_rule_id_serverless_rule

update a cd serverless rule.

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

req = operations.PutCdRuleIDServerlessRuleRequest(
    cd_serverless_rule=shared.CdServerlessRule(
        action=shared.ServerlessRuleAction.DETECT,
        group_name='ullam',
        id='bf0cbb1e-31b8-4b90-b344-3a1108e0adcf',
        name='Olivia McGlynn IV',
        rule=shared.ServerlessRuleType(
            serverless_function_validation=shared.ServerlessFunctionValidation(
                data_access_risk=shared.ServerlessDataAccessRisk.LOW,
                function_permission_risk=shared.ServerlessPolicyRisk.MEDIUM,
                is_unused_function=False,
                publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.MEDIUM,
                risk=shared.ServerlessFunctionRiskLevel.HIGH,
                secrets_risk=shared.ServerlessSecretsRisk.RISK_IDENTIFIED,
                vulnerability=shared.VulnerabilitySeverity.HIGH,
            ),
            serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
        ),
        scope=[
            shared.ServerlessRuleScope(
                cloud_account='ipsum',
                regions=[
                    'delectus',
                ],
            ),
        ],
        status=shared.ServerlessRuleStatus.DISABLED,
    ),
    rule_id='3ef7fbc7-abd7-44dd-b9c0-f5d2cff7c70a',
)

res = s.cd.put_cd_rule_id_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCdRuleIDServerlessRuleRequest](../../models/operations/putcdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PutCdRuleIDServerlessRuleResponse](../../models/operations/putcdruleidserverlessruleresponse.md)**

