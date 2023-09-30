# PodRuntimeInfo

runtime info of the pod (if is a pod)


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `containers`                                                   | list[[shared.Container](undefined/models/shared/container.md)] | :heavy_minus_sign:                                             | runtime pod containers                                         |
| `init_containers`                                              | list[[shared.Container](undefined/models/shared/container.md)] | :heavy_minus_sign:                                             | runtime pod init containers                                    |
| `labels`                                                       | list[[shared.Label](undefined/models/shared/label.md)]         | :heavy_minus_sign:                                             | runtime pod labels                                             |