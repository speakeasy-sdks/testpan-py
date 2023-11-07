# TelemetryAvailabilityState


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `status`                                                                             | [Optional[shared.TelemetryStateStatus]](../../models/shared/telemetrystatestatus.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `status_reason`                                                                      | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | will be populate only when status is unhealthy                                       |