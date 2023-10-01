# GetAPISecurityInternalCatalogRequest


## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `api_policy_profiles`                                                                                                            | list[*str*]                                                                                                                      | :heavy_minus_sign:                                                                                                               | Names of the Api Policy Profiles                                                                                                 |
| `drill_down_score`                                                                                                               | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | Return associated score                                                                                                          |
| `include_service_with_no_spec`                                                                                                   | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | When false, only services with specs wikk be returned                                                                            |
| `max_results`                                                                                                                    | *Optional[float]*                                                                                                                | :heavy_minus_sign:                                                                                                               | The number of entries to return (pagination)                                                                                     |
| `name`                                                                                                                           | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | the Api Catalog name filter                                                                                                      |
| `namespaces_filter`                                                                                                              | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | namespace filter. a base 64 representation of a list of NamespacesFilter definition object                                       |
| `no_pagination`                                                                                                                  | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | When true, the pagination params will be ignored                                                                                 |
| `offset`                                                                                                                         | *Optional[float]*                                                                                                                | :heavy_minus_sign:                                                                                                               | Return entries from this offset (pagination)                                                                                     |
| `sort_dir`                                                                                                                       | [Optional[operations.GetAPISecurityInternalCatalogSortDir]](undefined/models/operations/getapisecurityinternalcatalogsortdir.md) | :heavy_minus_sign:                                                                                                               | sorting direction                                                                                                                |
| `sort_key`                                                                                                                       | [Optional[operations.GetAPISecurityInternalCatalogSortKey]](undefined/models/operations/getapisecurityinternalcatalogsortkey.md) | :heavy_minus_sign:                                                                                                               | the Api Catalog sort key                                                                                                         |
| `updated_after`                                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                             | :heavy_minus_sign:                                                                                                               | Only Apis updated since this date                                                                                                |