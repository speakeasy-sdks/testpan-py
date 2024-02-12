# GetAPISecurityExternalCatalogCountRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `include_service_with_no_spec`                                       | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | When false, only services with specs wikk be returned                |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | the Api Catalog name filter                                          |
| `updated_after`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Only Apis updated since this date                                    |