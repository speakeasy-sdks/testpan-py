# AgentInfo


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `enabled`                                                                    | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |
| `last_active`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_minus_sign:                                                           | The last time that the agent sent telemetries                                |
| `status`                                                                     | [Optional[shared.ControllerStatus]](../../models/shared/controllerstatus.md) | :heavy_minus_sign:                                                           | The current controller state.                                                |
| `version`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |