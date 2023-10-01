# GetGatewaysRequest


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `max_results`                                                                                | *Optional[float]*                                                                            | :heavy_minus_sign:                                                                           | The number of entries to return (pagination)                                                 |
| `name`                                                                                       | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | Filter gateways by name                                                                      |
| `no_pagination`                                                                              | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | When true, the pagination params will be ignored                                             |
| `offset`                                                                                     | *Optional[float]*                                                                            | :heavy_minus_sign:                                                                           | Return entries from this offset (pagination)                                                 |
| `sort_dir`                                                                                   | [Optional[operations.GetGatewaysSortDir]](undefined/models/operations/getgatewayssortdir.md) | :heavy_minus_sign:                                                                           | sorting direction                                                                            |