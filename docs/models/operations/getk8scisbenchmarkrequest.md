# GetK8sCISBenchmarkRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `cluster_ids`                                    | list[*str*]                                      | :heavy_minus_sign:                               | cluster ids to filter                            |
| `max_results`                                    | *Optional[float]*                                | :heavy_minus_sign:                               | The number of entries to return (pagination)     |
| `no_pagination`                                  | *Optional[bool]*                                 | :heavy_minus_sign:                               | When true, the pagination params will be ignored |
| `offset`                                         | *Optional[float]*                                | :heavy_minus_sign:                               | Return entries from this offset (pagination)     |