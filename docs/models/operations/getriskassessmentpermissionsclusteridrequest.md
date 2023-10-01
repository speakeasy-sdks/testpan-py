# GetRiskAssessmentPermissionsClusterIDRequest


## Fields

| Field                                                                                                                                                          | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cluster_id`                                                                                                                                                   | *Optional[str]*                                                                                                                                                | :heavy_check_mark:                                                                                                                                             | N/A                                                                                                                                                            |
| `include_system_owners`                                                                                                                                        | *Optional[bool]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                             | include systems default owners                                                                                                                                 |
| `max_results`                                                                                                                                                  | *Optional[float]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                             | The number of entries to return (pagination)                                                                                                                   |
| `namespace_name`                                                                                                                                               | *Optional[str]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                             | the namespace name to filter by                                                                                                                                |
| `no_pagination`                                                                                                                                                | *Optional[bool]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                             | When true, the pagination params will be ignored                                                                                                               |
| `offset`                                                                                                                                                       | *Optional[float]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                             | Return entries from this offset (pagination)                                                                                                                   |
| `owner`                                                                                                                                                        | *Optional[str]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                             | owner name                                                                                                                                                     |
| `owner_type`                                                                                                                                                   | [Optional[operations.GetRiskAssessmentPermissionsClusterIDOwnerType]](undefined/models/operations/getriskassessmentpermissionsclusteridownertype.md)           | :heavy_minus_sign:                                                                                                                                             | owner type                                                                                                                                                     |
| `permission_risk`                                                                                                                                              | [Optional[operations.GetRiskAssessmentPermissionsClusterIDPermissionRisk]](undefined/models/operations/getriskassessmentpermissionsclusteridpermissionrisk.md) | :heavy_minus_sign:                                                                                                                                             | the risk to filter by                                                                                                                                          |
| `sort_dir`                                                                                                                                                     | [Optional[operations.GetRiskAssessmentPermissionsClusterIDSortDir]](undefined/models/operations/getriskassessmentpermissionsclusteridsortdir.md)               | :heavy_minus_sign:                                                                                                                                             | sorting direction                                                                                                                                              |
| `sort_key`                                                                                                                                                     | [Optional[operations.GetRiskAssessmentPermissionsClusterIDSortKey]](undefined/models/operations/getriskassessmentpermissionsclusteridsortkey.md)               | :heavy_minus_sign:                                                                                                                                             | sort key                                                                                                                                                       |