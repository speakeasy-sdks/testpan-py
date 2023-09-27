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
    default_rule=shared.ServerlessDefaultRule.BLOCK_ALL,
    unidentified_serverless_rule=shared.UnidentifiedServerlessRule(
        action=shared.UnidentifiedServerlessRuleAction.DETECT,
        name='Jane Shanahan',
    ),
    user_rules=[
        shared.ServerlessRule(
            action=shared.ServerlessRuleAction.DETECT,
            group_name='eligendi',
            id='f7812cb5-12c8-4782-80bf-548f88f8f1bf',
            name='Hannah Schmidt',
            rule=shared.ServerlessRuleType(
                serverless_function_validation=shared.ServerlessFunctionValidation(
                    data_access_risk=shared.ServerlessDataAccessRisk.NO_RISK,
                    function_permission_risk=shared.ServerlessPolicyRisk.CRITICAL,
                    is_unused_function=False,
                    publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.NO_RISK,
                    risk=shared.ServerlessFunctionRiskLevel.NO_RISK,
                    secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
                    vulnerability=shared.VulnerabilitySeverity.CRITICAL,
                ),
                serverless_rule_type=shared.ServerlessRuleTypeServerlessRuleType.FUNCTION_NAME_SERVERLESS_RULE_TYPE,
            ),
            rule_origin=shared.ServerlessRuleOrigin.SYSTEM,
            scope=[
                shared.ServerlessRuleScope(
                    cloud_account='quas',
                    regions=[
                        'sequi',
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

