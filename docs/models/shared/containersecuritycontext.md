# ContainerSecurityContext


## Fields

| Field                        | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `allow_privilege_escalation` | *Optional[bool]*             | :heavy_minus_sign:           | N/A                          |
| `capabilities_add`           | list[*str*]                  | :heavy_minus_sign:           | N/A                          |
| `capabilities_drop`          | list[*str*]                  | :heavy_minus_sign:           | N/A                          |
| `name`                       | *Optional[str]*              | :heavy_minus_sign:           | N/A                          |
| `privileged`                 | *Optional[bool]*             | :heavy_minus_sign:           | N/A                          |
| `proc_mount`                 | *Optional[str]*              | :heavy_minus_sign:           | N/A                          |
| `read_only_root_filesystem`  | *Optional[bool]*             | :heavy_minus_sign:           | N/A                          |
| `run_as_group`               | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `run_as_non_root`            | *Optional[bool]*             | :heavy_minus_sign:           | N/A                          |
| `run_as_user`                | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |