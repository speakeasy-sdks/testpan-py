# APIServiceFuzzingProgress


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `fuzzing_progress`                                                                                     | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `fuzzing_start_time`                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                   | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `fuzzing_status`                                                                                       | [Optional[shared.FuzzingStatus]](undefined/models/shared/fuzzingstatus.md)                             | :heavy_minus_sign:                                                                                     | An enumeration.                                                                                        |
| `fuzzing_status_message`                                                                               | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `test_configuration`                                                                                   | [Optional[shared.APIFuzzingTestConfiguration]](undefined/models/shared/apifuzzingtestconfiguration.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `test_id`                                                                                              | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |