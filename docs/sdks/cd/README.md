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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteCdRuleIDConnectionsRuleRequest(
    rule_id='192323ea-9230-406f-b63c-3a2786be61ed',
)

res = s.cd.delete_cd_rule_id_connections_rule(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteCdRuleIDConnectionsRuleRequest](../../models/operations/deletecdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteCdRuleIDConnectionsRuleResponse](../../models/operations/deletecdruleidconnectionsruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_cd_rule_id_serverless_rule

delete a cd serverless rule.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteCdRuleIDServerlessRuleRequest(
    rule_id='3a210f22-fa8a-464b-89de-71407e1ae662',
)

res = s.cd.delete_cd_rule_id_serverless_rule(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.DeleteCdRuleIDServerlessRuleRequest](../../models/operations/deletecdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.DeleteCdRuleIDServerlessRuleResponse](../../models/operations/deletecdruleidserverlessruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_cd

Get all the CD pipelines results

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetCdRequest(
    end_time=dateutil.parser.isoparse('2023-11-14T04:42:16.390Z'),
    start_time=dateutil.parser.isoparse('2024-12-05T23:05:32.860Z'),
)

res = s.cd.get_cd(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [operations.GetCdRequest](../../models/operations/getcdrequest.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetCdResponse](../../models/operations/getcdresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_cd_resource_id_

Get A single CD pipeline results

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetCdResourceIDRequest(
    resource_id='dbdc0e78-4707-4528-b885-f251b95127b5',
)

res = s.cd.get_cd_resource_id_(req)

if res.cd_pipeline_resource_result is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetCdResourceIDRequest](../../models/operations/getcdresourceidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetCdResourceIDResponse](../../models/operations/getcdresourceidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_cd_rule_id_connections_rule

get a cd connection rule.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetCdRuleIDConnectionsRuleRequest(
    rule_id='d826ec74-f98b-4a09-b982-a21b9e98807d',
)

res = s.cd.get_cd_rule_id_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetCdRuleIDConnectionsRuleRequest](../../models/operations/getcdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetCdRuleIDConnectionsRuleResponse](../../models/operations/getcdruleidconnectionsruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_cd_rule_id_serverless_rule

get a cd serverless rule.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetCdRuleIDServerlessRuleRequest(
    rule_id='fd218fe5-1dd3-4b03-aead-515501fcd459',
)

res = s.cd.get_cd_rule_id_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCdRuleIDServerlessRuleRequest](../../models/operations/getcdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetCdRuleIDServerlessRuleResponse](../../models/operations/getcdruleidserverlessruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_cd_connections_rule

Adds cd connection rule.

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.CdConnectionRule()

res = s.cd.post_cd_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.CdConnectionRule](../../models/shared/cdconnectionrule.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostCdConnectionsRuleResponse](../../models/operations/postcdconnectionsruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_cd_serverless_rule

Adds cd serverless rule.

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.CdServerlessRule(
    action=shared.ServerlessRuleAction.DETECT,
    name='string',
    rule=shared.ServerlessRuleType(
        serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_ARN_SERVERLESS_RULE_TYPE,
    ),
    status=shared.ServerlessRuleStatus.DISABLED,
)

res = s.cd.post_cd_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.CdServerlessRule](../../models/shared/cdserverlessrule.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostCdServerlessRuleResponse](../../models/operations/postcdserverlessruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_cd_rule_id_connections_rule

update a cd connection rule.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutCdRuleIDConnectionsRuleRequest(
    cd_connection_rule=shared.CdConnectionRule(),
    rule_id='0d3491c8-3a5a-4dc3-9212-eed6713c4812',
)

res = s.cd.put_cd_rule_id_connections_rule(req)

if res.cd_connection_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutCdRuleIDConnectionsRuleRequest](../../models/operations/putcdruleidconnectionsrulerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutCdRuleIDConnectionsRuleResponse](../../models/operations/putcdruleidconnectionsruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_cd_rule_id_serverless_rule

update a cd serverless rule.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutCdRuleIDServerlessRuleRequest(
    cd_serverless_rule=shared.CdServerlessRule(
        action=shared.ServerlessRuleAction.DETECT,
        name='string',
        rule=shared.ServerlessRuleType(
            serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_ARN_SERVERLESS_RULE_TYPE,
        ),
        status=shared.ServerlessRuleStatus.DISABLED,
    ),
    rule_id='4bb3d5f9-13b9-454c-81f6-ceb379119c49',
)

res = s.cd.put_cd_rule_id_serverless_rule(req)

if res.cd_serverless_rule is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PutCdRuleIDServerlessRuleRequest](../../models/operations/putcdruleidserverlessrulerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PutCdRuleIDServerlessRuleResponse](../../models/operations/putcdruleidserverlessruleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
