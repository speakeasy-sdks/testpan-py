# RegistryInput

image registry


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`                                                                             | [shared.RegistryType](../../models/shared/registrytype.md)                         | :heavy_check_mark:                                                                 | N/A                                                                                |
| `url`                                                                              | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `cluster_ids`                                                                      | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `credentials`                                                                      | [Optional[shared.RegistryCredentials]](../../models/shared/registrycredentials.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |