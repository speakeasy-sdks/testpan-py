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
    rule_id='192323ea-9230-406f-b63c-3a2786be61ed',
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
    rule_id='3a210f22-fa8a-464b-89de-71407e1ae662',
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
    end_time=dateutil.parser.isoparse('2022-11-13T13:45:57.433Z'),
    start_time=dateutil.parser.isoparse('2023-12-05T23:39:45.476Z'),
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
    resource_id='dbdc0e78-4707-4528-b885-f251b95127b5',
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
    rule_id='d826ec74-f98b-4a09-b982-a21b9e98807d',
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
    rule_id='fd218fe5-1dd3-4b03-aead-515501fcd459',
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
    destination=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.POD_NAME_CONNECTION_RULE_PART,
    ),
    source=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_TYPE_CONNECTION_RULE_PART,
    ),
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
    action=shared.ServerlessRuleAction.DETECT,
    name='orchestration Account navigate',
    rule=shared.ServerlessRuleType(
        serverless_function_validation=shared.ServerlessFunctionValidation(),
        serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
    ),
    scope=[
        shared.ServerlessRuleScope(
            cloud_account='that',
            regions=[
                'tenetur',
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
        destination=shared.ConnectionRulePart(
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_NAME_CONNECTION_RULE_PART,
        ),
        source=shared.ConnectionRulePart(
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.EXPANSION_ANY_CONNECTION_RULE_PART,
        ),
    ),
    rule_id='3491c83a-5adc-4392-92ee-d6713c48128c',
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
        name='dedicated Developer Sports',
        rule=shared.ServerlessRuleType(
            serverless_function_validation=shared.ServerlessFunctionValidation(),
            serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
        ),
        scope=[
            shared.ServerlessRuleScope(
                cloud_account='Cisgender tesla incentivize',
                regions=[
                    'ivory',
                ],
            ),
        ],
        status=shared.ServerlessRuleStatus.ENABLED,
    ),
    rule_id='f6ceb379-119c-449c-aa96-4c43ac563e54',
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

