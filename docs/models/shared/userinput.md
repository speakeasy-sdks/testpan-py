# UserInput


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `email`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The email of the user.                                               |
| `full_name`                                                          | *Optional[str]*                                                      | :heavy_check_mark:                                                   | N/A                                                                  |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | ID of the user as created by Secure Application management.          |
| `role`                                                               | [Optional[shared.Role]](undefined/models/shared/role.md)             | :heavy_minus_sign:                                                   | The role of the user                                                 |
| `status`                                                             | [Optional[shared.UserStatus]](undefined/models/shared/userstatus.md) | :heavy_check_mark:                                                   | N/A                                                                  |