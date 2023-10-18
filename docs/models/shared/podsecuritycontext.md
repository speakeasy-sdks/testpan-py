# PodSecurityContext


## Fields

| Field                 | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `fs_group`            | *Optional[int]*       | :heavy_minus_sign:    | N/A                   |
| `run_as_group`        | *Optional[int]*       | :heavy_minus_sign:    | N/A                   |
| `run_as_non_root`     | *Optional[bool]*      | :heavy_minus_sign:    | N/A                   |
| `run_as_user`         | *Optional[int]*       | :heavy_minus_sign:    | N/A                   |
| `supplemental_groups` | List[*int*]           | :heavy_minus_sign:    | N/A                   |