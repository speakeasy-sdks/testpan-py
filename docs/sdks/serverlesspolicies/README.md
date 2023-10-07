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
        password="",
        username="",
    ),
)


res = s.serverless_policies.get_serverless_policy()

if res.serverless_policy is not None:
    # handle response
```


### Response

**[operations.GetServerlessPolicyResponse](../../models/operations/getserverlesspolicyresponse.md)**


## put_serverless_policy

Set the current serverless policy

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

req = shared.ServerlessPolicy(
    default_rule=shared.ServerlessDefaultRule.DETECT_ALL,
    unidentified_serverless_rule=shared.UnidentifiedServerlessRule(
        action=shared.UnidentifiedServerlessRuleAction.DETECT,
    ),
    user_rules=[
        shared.ServerlessRule(
            action=shared.ServerlessRuleAction.ALLOW,
            name='Northwest granular',
            rule=shared.ServerlessRuleType(
                serverless_function_validation=shared.ServerlessFunctionValidation(),
                serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_ANY_SERVERLESS_RULE_TYPE,
            ),
            scope=[
                shared.ServerlessRuleScope(
                    cloud_account='Tuna brand Legacy',
                    regions=[
                        'Iraq',
                    ],
                ),
            ],
            status=shared.ServerlessRuleStatus.ENABLED,
        ),
    ],
)

res = s.serverless_policies.put_serverless_policy(req)

if res.serverless_policy is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.ServerlessPolicy](../../models/shared/serverlesspolicy.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PutServerlessPolicyResponse](../../models/operations/putserverlesspolicyresponse.md)**

