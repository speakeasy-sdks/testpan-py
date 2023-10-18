# AwsEnvironment


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `id`                                                    | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `tags`                                                  | List[[Tag](../../models/shared/tag.md)]                 | :heavy_minus_sign:                                      | N/A                                                     |
| `vpc`                                                   | [VPCDescription](../../models/shared/vpcdescription.md) | :heavy_check_mark:                                      | Like VPC but also includes the name                     |