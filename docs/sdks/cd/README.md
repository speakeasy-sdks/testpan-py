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
    max_results=9762.43,
    offset=9342.32,
    resource_name='kale Northeast Bicycle',
    sort_dir=operations.GetCdSortDir.DESC,
    sort_key=operations.GetCdSortKey.TIME,
    start_time=dateutil.parser.isoparse('2023-10-03T17:16:38.452Z'),
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
    sort_dir=operations.GetCdResourceIDSortDir.ASC,
    sort_key='apropos doom',
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
    action=shared.ConnectionRuleAction.BLOCK,
    destination=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.APP_TYPE_CONNECTION_RULE_PART,
    ),
    group_name='North',
    id='b91e56e8-5c5e-4dba-b536-b99e2dee788b',
    name='Account programming quos',
    source=shared.ConnectionRulePart(
        connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.EXPANSION_LABELS_CONNECTION_RULE_PART,
    ),
    status=shared.CdConnectionRuleStatus.DISABLED,
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
    group_name='orchestration Account navigate',
    id='81ea9f29-4b56-4171-9abd-233ecb84ab91',
    name='Arizona South',
    rule=shared.ServerlessRuleType(
        serverless_function_validation=shared.ServerlessFunctionValidation(
            data_access_risk=shared.ServerlessDataAccessRisk.LOW,
            function_permission_risk=shared.ServerlessPolicyRisk.CRITICAL,
            is_unused_function=False,
            publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.NO_RISK,
            risk=shared.ServerlessFunctionRiskLevel.LOW,
            secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
            vulnerability=shared.VulnerabilitySeverity.HIGH,
        ),
        serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
    ),
    scope=[
        shared.ServerlessRuleScope(
            cloud_account='Loan redundant',
            regions=[
                'orchid',
            ],
        ),
    ],
    status=shared.ServerlessRuleStatus.DELETED,
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
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.EXPANSION_ANY_CONNECTION_RULE_PART,
        ),
        group_name='Rubber',
        id='1c83a5ad-c392-412e-ad67-13c48128c295',
        name='Philippines male Philippine',
        source=shared.ConnectionRulePart(
            connection_rule_part_type=shared.ConnectionRulePartConnectionRulePartType.ANY_CONNECTION_RULE_PART,
        ),
        status=shared.CdConnectionRuleStatus.ENABLED,
    ),
    rule_id='352316c2-4f37-43ef-9bcd-45b8a926d9e0',
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
        group_name='dedicated Developer Sports',
        id='5f913b95-4cc1-4f6c-ab37-9119c49c2a96',
        name='Electric',
        rule=shared.ServerlessRuleType(
            serverless_function_validation=shared.ServerlessFunctionValidation(
                data_access_risk=shared.ServerlessDataAccessRisk.NO_RISK,
                function_permission_risk=shared.ServerlessPolicyRisk.HIGH,
                is_unused_function=False,
                publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.MEDIUM,
                risk=shared.ServerlessFunctionRiskLevel.LOW,
                secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
                vulnerability=shared.VulnerabilitySeverity.LOW,
            ),
            serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_ARN_SERVERLESS_RULE_TYPE,
        ),
        scope=[
            shared.ServerlessRuleScope(
                cloud_account='Rubber',
                regions=[
                    'utilisation',
                ],
            ),
        ],
        status=shared.ServerlessRuleStatus.ENABLED,
    ),
    rule_id='688963e3-0212-4786-89a2-e3b6d79445cb',
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

