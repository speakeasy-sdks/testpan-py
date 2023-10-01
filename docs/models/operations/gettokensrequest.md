# GetTokensRequest


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `max_results`                                                                            | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | The number of entries to return (pagination)                                             |
| `no_pagination`                                                                          | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | When true, the pagination params will be ignored                                         |
| `offset`                                                                                 | *Optional[float]*                                                                        | :heavy_minus_sign:                                                                       | Return entries from this offset (pagination)                                             |
| `sort_dir`                                                                               | [Optional[operations.GetTokensSortDir]](undefined/models/operations/gettokenssortdir.md) | :heavy_minus_sign:                                                                       | sorting direction                                                                        |
| `sort_key`                                                                               | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | the token sort key                                                                       |
| `token_name`                                                                             | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Defined token name                                                                       |