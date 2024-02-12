# GetAPISecurityExternalCatalogCatalogIDRequest


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `catalog_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `api_policy_profiles`                                                       | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Names of the Api Policy Profiles                                            |
| `download_as_json`                                                          | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | When true, the API will return an json file, and pagination will be ignored |