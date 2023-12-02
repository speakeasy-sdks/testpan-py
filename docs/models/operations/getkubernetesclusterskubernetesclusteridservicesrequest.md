# GetKubernetesClustersKubernetesClusterIDServicesRequest


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `kubernetes_cluster_id`                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | Secure Application Kubernetes cluster ID                                               |
| `show_istio_only`                                                                      | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | if true, return only services deployed on namespace with label istio-injection=enabled |