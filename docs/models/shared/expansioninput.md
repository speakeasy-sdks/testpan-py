# ExpansionInput

represent expansion object used in put method


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `cluster_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `controller_last_active`                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The last time that the agent sent telemetries                        |
| `labels`                                                             | list[[Label](../../models/shared/label.md)]                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `namespace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `should_send_metrics`                                                | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | N/A                                                                  |
| `workload_addresses`                                                 | list[[WorkloadAddress](../../models/shared/workloadaddress.md)]      | :heavy_check_mark:                                                   | N/A                                                                  |