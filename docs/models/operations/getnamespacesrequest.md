# GetNamespacesRequest


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `cluster_name`                                                                                                     | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | the cluster name to filter by                                                                                      |
| `download_as_xlsx`                                                                                                 | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | When true, the API will return an xlsx file, and pagination will be ignored                                        |
| `max_results`                                                                                                      | *Optional[float]*                                                                                                  | :heavy_minus_sign:                                                                                                 | The number of entries to return (pagination)                                                                       |
| `namespace_name`                                                                                                   | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | the namespace name to filter by                                                                                    |
| `offset`                                                                                                           | *Optional[float]*                                                                                                  | :heavy_minus_sign:                                                                                                 | Return entries from this offset (pagination)                                                                       |
| `protection_status`                                                                                                | [Optional[operations.GetNamespacesProtectionStatus]](undefined/models/operations/getnamespacesprotectionstatus.md) | :heavy_minus_sign:                                                                                                 | When true, the API will return only protected pods                                                                 |
| `sort_dir`                                                                                                         | [Optional[operations.GetNamespacesSortDir]](undefined/models/operations/getnamespacessortdir.md)                   | :heavy_minus_sign:                                                                                                 | sorting direction                                                                                                  |
| `sort_key`                                                                                                         | [Optional[operations.GetNamespacesSortKey]](undefined/models/operations/getnamespacessortkey.md)                   | :heavy_minus_sign:                                                                                                 | the namespaces sort key                                                                                            |