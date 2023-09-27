# UserInput


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `description`                                               | *Optional[str]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `email`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The email of the user.                                      |
| `full_name`                                                 | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `id`                                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | ID of the user as created by Secure Application management. |
| `role`                                                      | [Optional[Role]](../../models/shared/role.md)               | :heavy_minus_sign:                                          | The role of the user                                        |
| `status`                                                    | [UserStatus](../../models/shared/userstatus.md)             | :heavy_check_mark:                                          | N/A                                                         |