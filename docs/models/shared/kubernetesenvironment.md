# KubernetesEnvironment


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `kubernetes_cluster`                               | *str*                                              | :heavy_check_mark:                                 | N/A                                                |
| `id`                                               | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `kubernetes_cluster_name`                          | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |
| `namespace_labels`                                 | List[[shared.Label](../../models/shared/label.md)] | :heavy_minus_sign:                                 | N/A                                                |
| `namespaces`                                       | List[*str*]                                        | :heavy_minus_sign:                                 | N/A                                                |
| `preserve_original_source_ip`                      | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |