# UserInput


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `full_name`                                                 | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `status`                                                    | [shared.UserStatus](../../models/shared/userstatus.md)      | :heavy_check_mark:                                          | N/A                                                         |
| `description`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `email`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The email of the user.                                      |
| `id`                                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | ID of the user as created by Secure Application management. |
| `role`                                                      | [Optional[shared.Role]](../../models/shared/role.md)        | :heavy_minus_sign:                                          | The role of the user                                        |