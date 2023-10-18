# RiskAssessmentClusterScanConfig

Single cluster risk assessment scan config


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `max_parallelism`                                                               | *int*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `minimum_severity`                                                              | [VulnerabilitySeverity](../../models/shared/vulnerabilityseverity.md)           | :heavy_check_mark:                                                              | N/A                                                                             |
| `namespaces`                                                                    | List[*str*]                                                                     | :heavy_minus_sign:                                                              | N/A                                                                             |
| `periodic_job_expression`                                                       | [Optional[PeriodicJobExpression]](../../models/shared/periodicjobexpression.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `run_dockerfile_scan`                                                           | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | N/A                                                                             |