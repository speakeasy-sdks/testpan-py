# PodRuntimeInfo

runtime info of the pod (if is a pod)


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `containers`                                               | List[[shared.Container](../../models/shared/container.md)] | :heavy_minus_sign:                                         | runtime pod containers                                     |
| `init_containers`                                          | List[[shared.Container](../../models/shared/container.md)] | :heavy_minus_sign:                                         | runtime pod init containers                                |
| `labels`                                                   | List[[shared.Label](../../models/shared/label.md)]         | :heavy_minus_sign:                                         | runtime pod labels                                         |