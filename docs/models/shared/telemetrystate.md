# TelemetryState

Status of a telemetry entry


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `last_seen`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `start_time`                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `status`                                                                                 | [Optional[shared.TelemetryStateStatus]](undefined/models/shared/telemetrystatestatus.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `status_reason`                                                                          | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | will be populate only when status is unhealthy                                           |