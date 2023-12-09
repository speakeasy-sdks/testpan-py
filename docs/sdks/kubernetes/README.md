# Kubernetes
(*kubernetes*)

## Overview

APIs used to manage Kubernetes clusters on Secure Application

### Available Operations

* [delete_kubernetes_clusters_kubernetes_cluster_id_](#delete_kubernetes_clusters_kubernetes_cluster_id_) - Delete a Kubernetes cluster
* [delete_pod_definitions_pod_id_](#delete_pod_definitions_pod_id_) - Delete a pod definition
* [get_get_controller_data_cluster_id_](#get_get_controller_data_cluster_id_) - get controller data using clusterId
* [get_istio_supported_versions](#get_istio_supported_versions) - Get a list of istio releases that are supported by Secure Application agent. sorted from latest to oldest
* [get_kubernetes_clusters](#get_kubernetes_clusters) - get a list of current Kubernetes clusters
* [get_kubernetes_clusters_kubernetes_cluster_id_](#get_kubernetes_clusters_kubernetes_cluster_id_) - get the Kubernetes cluster with the given id
* [get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies](#get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified Kubernetes cluster
* [get_kubernetes_clusters_kubernetes_cluster_id_download_bundle](#get_kubernetes_clusters_kubernetes_cluster_id_download_bundle) - Get Secure Application installation script
* [get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands](#get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands) - Get Panoptica Aug release Helm command
* [get_kubernetes_clusters_kubernetes_cluster_id_namespaces](#get_kubernetes_clusters_kubernetes_cluster_id_namespaces) - List namespaces on a specific Kubernetes cluster
* [get_kubernetes_clusters_kubernetes_cluster_id_services](#get_kubernetes_clusters_kubernetes_cluster_id_services) - List services on a specific Kubernetes cluster
* [get_lean_kubernetes_clusters](#get_lean_kubernetes_clusters) - get a list of current Kubernetes clusters
* [get_namespaces](#get_namespaces) - Get a list of current Kubernetes namespaces
* [get_pod_definitions](#get_pod_definitions) - Get all pod definitions on the system
* [post_kubernetes_clusters](#post_kubernetes_clusters) - Add a new Kubernetes cluster to Secure Application
* [post_pod_definitions](#post_pod_definitions) - Create a new pod definition
* [put_kubernetes_clusters_kubernetes_cluster_id_](#put_kubernetes_clusters_kubernetes_cluster_id_) - Update the Kubernetes cluster
* [put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm](#put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm) - Update the Kubernetes cluster which managed by HELM
* [put_pod_definitions_pod_id_](#put_pod_definitions_pod_id_) - Change pod definition

## delete_kubernetes_clusters_kubernetes_cluster_id_

Delete a Kubernetes cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.DeleteKubernetesClustersKubernetesClusterIDRequest(
    kubernetes_cluster_id='a8fff1fd-16f4-41cf-ba2f-6b7d60168e00',
)

res = s.kubernetes.delete_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.DeleteKubernetesClustersKubernetesClusterIDRequest](../../models/operations/deletekubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.DeleteKubernetesClustersKubernetesClusterIDResponse](../../models/operations/deletekubernetesclusterskubernetesclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_pod_definitions_pod_id_

Delete a pod definition

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.DeletePodDefinitionsPodIDRequest(
    pod_id='1d7b59d4-9a1e-473b-8e2e-c8a463501aa8',
)

res = s.kubernetes.delete_pod_definitions_pod_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeletePodDefinitionsPodIDRequest](../../models/operations/deletepoddefinitionspodidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DeletePodDefinitionsPodIDResponse](../../models/operations/deletepoddefinitionspodidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_get_controller_data_cluster_id_

get controller data using clusterId

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetGetControllerDataClusterIDRequest(
    cluster_id='6d4f5b01-1e67-437c-a42b-e9becce491b4',
)

res = s.kubernetes.get_get_controller_data_cluster_id_(req)

if res.controller_data_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetGetControllerDataClusterIDRequest](../../models/operations/getgetcontrollerdataclusteridrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetGetControllerDataClusterIDResponse](../../models/operations/getgetcontrollerdataclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_istio_supported_versions

Get a list of istio releases that are supported by Secure Application agent. sorted from latest to oldest

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)


res = s.kubernetes.get_istio_supported_versions()

if res.strings is not None:
    # handle response
    pass
```


### Response

**[operations.GetIstioSupportedVersionsResponse](../../models/operations/getistiosupportedversionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters

get a list of current Kubernetes clusters

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersRequest()

res = s.kubernetes.get_kubernetes_clusters(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetKubernetesClustersRequest](../../models/operations/getkubernetesclustersrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetKubernetesClustersResponse](../../models/operations/getkubernetesclustersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_

get the Kubernetes cluster with the given id

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDRequest(
    kubernetes_cluster_id='6ad413ce-670c-4973-bf8a-5a66b7855734',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.kubernetes_cluster is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetKubernetesClustersKubernetesClusterIDRequest](../../models/operations/getkubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDResponse](../../models/operations/getkubernetesclusterskubernetesclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies

get dependencies which need to be handled in order to delete specified Kubernetes cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest(
    kubernetes_cluster_id='b06f6c06-c4ec-44f8-ba3a-a7d63215e690',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies(req)

if res.kubernetes_cluster_delete_dependencies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest](../../models/operations/getkubernetesclusterskubernetesclusteriddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesResponse](../../models/operations/getkubernetesclusterskubernetesclusteriddeletedependenciesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_download_bundle

In order to install,  extract and run "./install_bundle.sh"

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest(
    kubernetes_cluster_id='204aba8f-ddfd-4080-9f3c-89482d02fb76',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_download_bundle(req)

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest](../../models/operations/getkubernetesclusterskubernetesclusteriddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleResponse](../../models/operations/getkubernetesclusterskubernetesclusteriddownloadbundleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands

Get Panoptica Aug release Helm command

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsRequest(
    kubernetes_cluster_id='f7710c3a-4d45-43f9-898d-e19416c2b527',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands(req)

if res.helm_commands_installation is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsRequest](../../models/operations/getkubernetesclusterskubernetesclusteridgethelmcommandsrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsResponse](../../models/operations/getkubernetesclusterskubernetesclusteridgethelmcommandsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_namespaces

List namespaces on a specific Kubernetes cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest(
    kubernetes_cluster_id='b18474d1-b95c-48d9-af1c-951ce15b0be6',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_namespaces(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest](../../models/operations/getkubernetesclusterskubernetesclusteridnamespacesrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDNamespacesResponse](../../models/operations/getkubernetesclusterskubernetesclusteridnamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_kubernetes_clusters_kubernetes_cluster_id_services

List services on a specific Kubernetes cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetKubernetesClustersKubernetesClusterIDServicesRequest(
    kubernetes_cluster_id='1b08f941-6d25-44a9-8a5a-94e46b69d5cc',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_services(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.GetKubernetesClustersKubernetesClusterIDServicesRequest](../../models/operations/getkubernetesclusterskubernetesclusteridservicesrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDServicesResponse](../../models/operations/getkubernetesclusterskubernetesclusteridservicesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_lean_kubernetes_clusters

get a list of current Kubernetes clusters

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetLeanKubernetesClustersRequest()

res = s.kubernetes.get_lean_kubernetes_clusters(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetLeanKubernetesClustersRequest](../../models/operations/getleankubernetesclustersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetLeanKubernetesClustersResponse](../../models/operations/getleankubernetesclustersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_namespaces

Get a list of current Kubernetes namespaces

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetNamespacesRequest()

res = s.kubernetes.get_namespaces(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNamespacesRequest](../../models/operations/getnamespacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNamespacesResponse](../../models/operations/getnamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_pod_definitions

Get all pod definitions on the system

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetPodDefinitionsRequest(
    deployment_type=[
        'string',
    ],
    template_source=[
        'string',
    ],
)

res = s.kubernetes.get_pod_definitions(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPodDefinitionsRequest](../../models/operations/getpoddefinitionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetPodDefinitionsResponse](../../models/operations/getpoddefinitionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_kubernetes_clusters

Add a new Kubernetes cluster to Secure Application

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.KubernetesCluster(
    controller_data_response=shared.ControllerDataResponse(),
    helm_commands_installation=shared.HelmCommandsInstallation(),
    internal_registry_parameters=shared.InternalRegistryParameters(),
    istio_ingress_annotations=[
        shared.KubernetesAnnotation(
            key='<key>',
            value='string',
        ),
    ],
    istio_installation_parameters=shared.IstioInstallationParameters(),
    name='string',
    proxy_configuration=shared.ProxyConfiguration(),
    scan_configuration=shared.ScanConfiguration(
        scan_types=[
            shared.ScanType.VULNERABILITIES,
        ],
    ),
    sidecars_resources=shared.SidecarsResource(),
)

res = s.kubernetes.post_kubernetes_clusters(req)

if res.kubernetes_cluster is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.KubernetesCluster](../../models/shared/kubernetescluster.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostKubernetesClustersResponse](../../models/operations/postkubernetesclustersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_pod_definitions

Create a new pod definition

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.PodDefinitionInput(
    cluster_id='caf647ad-b35e-4462-baa4-a61d2b4e2410',
    containers=[
        shared.Container(
            image=shared.Image(),
        ),
    ],
    init_containers=[
        shared.Container(
            image=shared.Image(),
        ),
    ],
    labels=[
        shared.Label(
            key='<key>',
            value='string',
        ),
    ],
    name='string',
)

res = s.kubernetes.post_pod_definitions(req)

if res.pod_definition is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PodDefinitionInput](../../models/shared/poddefinitioninput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostPodDefinitionsResponse](../../models/operations/postpoddefinitionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_kubernetes_clusters_kubernetes_cluster_id_

Update the Kubernetes cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutKubernetesClustersKubernetesClusterIDRequest(
    kubernetes_cluster=shared.KubernetesCluster(
        controller_data_response=shared.ControllerDataResponse(),
        helm_commands_installation=shared.HelmCommandsInstallation(),
        internal_registry_parameters=shared.InternalRegistryParameters(),
        istio_ingress_annotations=[
            shared.KubernetesAnnotation(
                key='<key>',
                value='string',
            ),
        ],
        istio_installation_parameters=shared.IstioInstallationParameters(),
        name='string',
        proxy_configuration=shared.ProxyConfiguration(),
        scan_configuration=shared.ScanConfiguration(
            scan_types=[
                shared.ScanType.DOCKER_CIS_BENCHMARK,
            ],
        ),
        sidecars_resources=shared.SidecarsResource(),
    ),
    kubernetes_cluster_id='fc49f9e0-fd95-4795-8a07-96a5f2d9d7f9',
)

res = s.kubernetes.put_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.kubernetes_cluster is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PutKubernetesClustersKubernetesClusterIDRequest](../../models/operations/putkubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.PutKubernetesClustersKubernetesClusterIDResponse](../../models/operations/putkubernetesclusterskubernetesclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm

Update the Kubernetes cluster which managed by HELM

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmRequest(
    edit_kubernetes_cluster_managed_by_helm=shared.EditKubernetesClusterManagedByHelm(),
    kubernetes_cluster_id='98ce5ff4-7cf2-43f7-b683-e7d0be8fe575',
)

res = s.kubernetes.put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm(req)

if res.kubernetes_cluster is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmRequest](../../models/operations/putkubernetesclusterskubernetesclusteridmanagedbyhelmrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmResponse](../../models/operations/putkubernetesclusterskubernetesclusteridmanagedbyhelmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_pod_definitions_pod_id_

Change pod definition

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutPodDefinitionsPodIDRequest(
    pod_definition=shared.PodDefinitionInput(
        cluster_id='8813d860-716a-4bd1-be6a-f36d0732a688',
        containers=[
            shared.Container(
                image=shared.Image(),
            ),
        ],
        init_containers=[
            shared.Container(
                image=shared.Image(),
            ),
        ],
        labels=[
            shared.Label(
                key='<key>',
                value='string',
            ),
        ],
        name='string',
    ),
    pod_id='d5b40efc-46b3-4d79-9349-9390e36a1df3',
)

res = s.kubernetes.put_pod_definitions_pod_id_(req)

if res.pod_definition is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutPodDefinitionsPodIDRequest](../../models/operations/putpoddefinitionspodidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PutPodDefinitionsPodIDResponse](../../models/operations/putpoddefinitionspodidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
