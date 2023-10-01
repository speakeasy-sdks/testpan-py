# EnvironmentRecommendation


## Fields

| Field                                                                                                                                                                                        | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `environemnt`                                                                                                                                                                                | [Optional[shared.Environment]](undefined/models/shared/environment.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                           | Secure Application environment definition. #also must be included for at least one of the env details but Swagger does not support parameter dependencies and mutually exclusive parameters. |
| `id`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `number_of_affected_workloads`                                                                                                                                                               | *Optional[int]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                           | N/A                                                                                                                                                                                          |