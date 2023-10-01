# GetAppTelemetriesRequest


## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `app_name`                                                                                                                 | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Defined App name                                                                                                           |
| `app_type`                                                                                                                 | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Empty string means no filtering. "UNDEFINED" means telemetries with no App type                                            |
| `download_as_xlsx`                                                                                                         | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true, the API will return an xlsx file, and pagination will be ignored                                                |
| `end_time`                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                       | :heavy_check_mark:                                                                                                         | End date of the query                                                                                                      |
| `environment_name`                                                                                                         | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Empty string means no filtering. "UNDEFINED" means telemetries with no App type                                            |
| `executable`                                                                                                               | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |
| `hide_internals`                                                                                                           | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true, the API will filter out "OS Internal" and "User OS Internal" App types                                          |
| `highest_dockerfile_scan_result`                                                                                           | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Highest DockerfileScan Result                                                                                              |
| `host`                                                                                                                     | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Defined host name                                                                                                          |
| `images_id`                                                                                                                | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Array of images id                                                                                                         |
| `is_identified`                                                                                                            | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | app is identified filter                                                                                                   |
| `max_results`                                                                                                              | *Optional[float]*                                                                                                          | :heavy_minus_sign:                                                                                                         | The number of entries to return (pagination)                                                                               |
| `namespaces_filter`                                                                                                        | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | namespace filter. a base 64 representation of a list of NamespacesFilter definition object                                 |
| `offset`                                                                                                                   | *Optional[float]*                                                                                                          | :heavy_minus_sign:                                                                                                         | Return entries from this offset (pagination)                                                                               |
| `protection_status`                                                                                                        | [Optional[operations.GetAppTelemetriesProtectionStatus]](undefined/models/operations/getapptelemetriesprotectionstatus.md) | :heavy_minus_sign:                                                                                                         | When true, the API will return only protected pods                                                                         |
| `result`                                                                                                                   | list[[operations.GetAppTelemetriesResult](undefined/models/operations/getapptelemetriesresult.md)]                         | :heavy_minus_sign:                                                                                                         | app result filter                                                                                                          |
| `show_only_entries_with_app_name`                                                                                          | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true, the telemetries API will only return entries with the App name                                                  |
| `show_only_violations`                                                                                                     | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true, the API will only return entries that violate the active policy                                                 |
| `show_system_pods`                                                                                                         | *Optional[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                         | When true, the telemetries API will also return workloads that are part of the Kubernetes system                           |
| `sort_dir`                                                                                                                 | [Optional[operations.GetAppTelemetriesSortDir]](undefined/models/operations/getapptelemetriessortdir.md)                   | :heavy_minus_sign:                                                                                                         | sorting direction                                                                                                          |
| `sort_key`                                                                                                                 | [Optional[operations.GetAppTelemetriesSortKey]](undefined/models/operations/getapptelemetriessortkey.md)                   | :heavy_check_mark:                                                                                                         | sort key                                                                                                                   |
| `start_time`                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                       | :heavy_check_mark:                                                                                                         | Start date of the query                                                                                                    |
| `status`                                                                                                                   | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | App status                                                                                                                 |
| `vulnerability_levels_filter`                                                                                              | list[*str*]                                                                                                                | :heavy_minus_sign:                                                                                                         | Highest vulnerability                                                                                                      |
| `workload_risks`                                                                                                           | list[[operations.GetAppTelemetriesWorkloadRisks](undefined/models/operations/getapptelemetriesworkloadrisks.md)]           | :heavy_minus_sign:                                                                                                         | workloadRisk filter                                                                                                        |