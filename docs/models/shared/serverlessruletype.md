# ServerlessRuleType

identify the serverless functions matching type. Only one of the below should be not null, and  used.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `serverless_rule_type`                                                                                     | [shared.ServerlessRuleTypeServerlessRuleType](../../models/shared/serverlessruletypeserverlessruletype.md) | :heavy_check_mark:                                                                                         | N/A                                                                                                        |
| `serverless_function_validation`                                                                           | [Optional[shared.ServerlessFunctionValidation]](../../models/shared/serverlessfunctionvalidation.md)       | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |