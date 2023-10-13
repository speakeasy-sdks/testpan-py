# AwsEnvironmentInput


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *Optional[str]*                                                   | :heavy_minus_sign:                                                | N/A                                                               |
| `tags`                                                            | list[[Tag](../../models/shared/tag.md)]                           | :heavy_minus_sign:                                                | N/A                                                               |
| `vpc`                                                             | [VPCDescriptionInput](../../models/shared/vpcdescriptioninput.md) | :heavy_check_mark:                                                | Like VPC but also includes the name                               |