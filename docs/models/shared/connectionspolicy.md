# ConnectionsPolicy


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `default_rule`                                                                         | [Optional[shared.DefaultConnectionRule]](../../models/shared/defaultconnectionrule.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `direct_pod_rule`                                                                      | [shared.DirectPodIPConnectionRule](../../models/shared/directpodipconnectionrule.md)   | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `user_rules`                                                                           | List[[shared.ConnectionsRule](../../models/shared/connectionsrule.md)]                 | :heavy_minus_sign:                                                                     | N/A                                                                                    |