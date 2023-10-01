# NetworkPod


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `cluster`                                                                                                 | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `cluster_id`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `containers`                                                                                              | list[[shared.NetworkContainer](undefined/models/shared/networkcontainer.md)]                              | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `highest_vulnerability_severity_level`                                                                    | [Optional[shared.VulnerabilitySeverity]](undefined/models/shared/vulnerabilityseverity.md)                | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `hosts`                                                                                                   | list[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `id`                                                                                                      | list[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `is_identified`                                                                                           | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `kind`                                                                                                    | [Optional[shared.PodTemplateKind]](undefined/models/shared/podtemplatekind.md)                            | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `labels`                                                                                                  | list[[shared.Label](undefined/models/shared/label.md)]                                                    | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `name`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | in pod template, this is the normalized name (for example, get it from pod -> replicaset -> deployment).<br/> |
| `namespace`                                                                                               | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `namespace_id`                                                                                            | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `pod_template_id`                                                                                         | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |