# ServerlessPolicies
(*serverless_policies*)

### Available Operations

* [get_serverless_policy](#get_serverless_policy) - Get current serverless policy
* [put_serverless_policy](#put_serverless_policy) - Set the current serverless policy

## get_serverless_policy

Get current serverless policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.serverless_policies.get_serverless_policy()

if res.serverless_policy is not None:
    # handle response
    pass
```


### Response

**[operations.GetServerlessPolicyResponse](../../models/operations/getserverlesspolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_serverless_policy

Set the current serverless policy

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.ServerlessPolicy(
    default_rule=shared.ServerlessDefaultRule.DETECT_ALL,
    unidentified_serverless_rule=shared.UnidentifiedServerlessRule(
        action=shared.UnidentifiedServerlessRuleAction.DETECT,
    ),
)

res = s.serverless_policies.put_serverless_policy(req)

if res.serverless_policy is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.ServerlessPolicy](../../models/shared/serverlesspolicy.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PutServerlessPolicyResponse](../../models/operations/putserverlesspolicyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
