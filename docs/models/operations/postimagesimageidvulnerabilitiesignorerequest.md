# PostImagesImageIDVulnerabilitiesIgnoreRequest


## Fields

| Field                                                                                                                                                    | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uuid_list`                                                                                                                                              | [Optional[shared.UUIDList]](undefined/models/shared/uuidlist.md)                                                                                         | :heavy_check_mark:                                                                                                                                       | N/A                                                                                                                                                      |
| `action_type`                                                                                                                                            | [Optional[operations.PostImagesImageIDVulnerabilitiesIgnoreActionType]](undefined/models/operations/postimagesimageidvulnerabilitiesignoreactiontype.md) | :heavy_check_mark:                                                                                                                                       | The ignore action type (ADD/REMOVE)                                                                                                                      |
| `image_id`                                                                                                                                               | *Optional[str]*                                                                                                                                          | :heavy_check_mark:                                                                                                                                       | N/A                                                                                                                                                      |
| `snooze_time`                                                                                                                                            | [Optional[operations.PostImagesImageIDVulnerabilitiesIgnoreSnoozeTime]](undefined/models/operations/postimagesimageidvulnerabilitiesignoresnoozetime.md) | :heavy_minus_sign:                                                                                                                                       | The time to snooze the vulnerability                                                                                                                     |