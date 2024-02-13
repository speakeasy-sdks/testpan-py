# PortshiftAwsSubnet

the interface that represents the node's entity type. Possible types are: PortshiftAwsInstance, PortshiftAwsSecurityGroupViolationInfo, PortshiftAwsSubnet


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `violations_map_node_type`                                                   | [shared.ViolationsMapNodeType](../../models/shared/violationsmapnodetype.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `cidr_block`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `state`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `subnet_id`                                                                  | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `vpc_id`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |