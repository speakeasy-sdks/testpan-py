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
    kubernetes_cluster_id='c3450841-f176-4445-a379-f3fb27e21f86',
)

res = s.kubernetes.delete_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.DeleteKubernetesClustersKubernetesClusterIDRequest](../../models/operations/deletekubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.DeleteKubernetesClustersKubernetesClusterIDResponse](../../models/operations/deletekubernetesclusterskubernetesclusteridresponse.md)**


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
    pod_id='2657b36f-c6b9-4f58-bce5-25c67641a831',
)

res = s.kubernetes.delete_pod_definitions_pod_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeletePodDefinitionsPodIDRequest](../../models/operations/deletepoddefinitionspodidrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DeletePodDefinitionsPodIDResponse](../../models/operations/deletepoddefinitionspodidresponse.md)**


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
    cluster_id='2e5047b4-c21c-4cb4-a3ab-cdc91faabdd8',
)

res = s.kubernetes.get_get_controller_data_cluster_id_(req)

if res.controller_data_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetGetControllerDataClusterIDRequest](../../models/operations/getgetcontrollerdataclusteridrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetGetControllerDataClusterIDResponse](../../models/operations/getgetcontrollerdataclusteridresponse.md)**


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

if res.get_istio_supported_versions_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetIstioSupportedVersionsResponse](../../models/operations/getistiosupportedversionsresponse.md)**


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

req = operations.GetKubernetesClustersRequest(
    cluster_name='praesentium',
    controller_status='officiis',
    controller_version='esse',
    download_as_xlsx=False,
    kubernetes_version='vitae',
    max_results=9651.17,
    offset=3864.01,
    only_spec_reconstruction_enabled_filter=False,
    sort_dir=operations.GetKubernetesClustersSortDir.DESC,
    sort_key='labore',
)

res = s.kubernetes.get_kubernetes_clusters(req)

if res.kubernetes_cluster_controllers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetKubernetesClustersRequest](../../models/operations/getkubernetesclustersrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetKubernetesClustersResponse](../../models/operations/getkubernetesclustersresponse.md)**


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
    kubernetes_cluster_id='8252d777-1e7f-4d07-8009-ef8d29de1dd7',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.kubernetes_cluster is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetKubernetesClustersKubernetesClusterIDRequest](../../models/operations/getkubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDResponse](../../models/operations/getkubernetesclusterskubernetesclusteridresponse.md)**


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
    kubernetes_cluster_id='097b5da0-8c57-4fa6-878a-216e19bafeca',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies(req)

if res.kubernetes_cluster_delete_dependencies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest](../../models/operations/getkubernetesclusterskubernetesclusteriddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesResponse](../../models/operations/getkubernetesclusterskubernetesclusteriddeletedependenciesresponse.md)**


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
    kubernetes_cluster_id='61914981-40b6-44ff-8ae1-70ef03b5f37e',
    send_telemetries_interval_sec=253855,
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_download_bundle(req)

if res.get_kubernetes_clusters_kubernetes_cluster_id_download_bundle_200_application_json_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest](../../models/operations/getkubernetesclusterskubernetesclusteriddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleResponse](../../models/operations/getkubernetesclusterskubernetesclusteriddownloadbundleresponse.md)**


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
    kubernetes_cluster_id='aa868555-9667-432a-a5dc-b6682cb70f8c',
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands(req)

if res.helm_commands_installation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsRequest](../../models/operations/getkubernetesclusterskubernetesclusteridgethelmcommandsrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsResponse](../../models/operations/getkubernetesclusterskubernetesclusteridgethelmcommandsresponse.md)**


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
    include_scannable=False,
    kubernetes_cluster_id='fd5fb6e9-1b9a-49f7-8846-e2c3309db053',
    sort_dir=operations.GetKubernetesClustersKubernetesClusterIDNamespacesSortDir.ASC,
    sort_key=operations.GetKubernetesClustersKubernetesClusterIDNamespacesSortKey.STATUS,
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_namespaces(req)

if res.kubernetes_namespace_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest](../../models/operations/getkubernetesclusterskubernetesclusteridnamespacesrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDNamespacesResponse](../../models/operations/getkubernetesclusterskubernetesclusteridnamespacesresponse.md)**


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
    kubernetes_cluster_id='9e75ca00-6f53-492c-91a2-5a8bf92f9742',
    show_istio_only=False,
)

res = s.kubernetes.get_kubernetes_clusters_kubernetes_cluster_id_services(req)

if res.kubernetes_services is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.GetKubernetesClustersKubernetesClusterIDServicesRequest](../../models/operations/getkubernetesclusterskubernetesclusteridservicesrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.GetKubernetesClustersKubernetesClusterIDServicesResponse](../../models/operations/getkubernetesclusterskubernetesclusteridservicesresponse.md)**


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

req = operations.GetLeanKubernetesClustersRequest(
    cluster_name='molestias',
)

res = s.kubernetes.get_lean_kubernetes_clusters(req)

if res.lean_kubernetes_clusters is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetLeanKubernetesClustersRequest](../../models/operations/getleankubernetesclustersrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetLeanKubernetesClustersResponse](../../models/operations/getleankubernetesclustersresponse.md)**


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

req = operations.GetNamespacesRequest(
    cluster_name='fuga',
    download_as_xlsx=False,
    max_results=8697.18,
    namespace_name='unde',
    offset=6734,
    protection_status=operations.GetNamespacesProtectionStatus.CONNECTION_ONLY,
    sort_dir=operations.GetNamespacesSortDir.DESC,
    sort_key=operations.GetNamespacesSortKey.RUNNING_PODS,
)

res = s.kubernetes.get_namespaces(req)

if res.namespaces is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNamespacesRequest](../../models/operations/getnamespacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNamespacesResponse](../../models/operations/getnamespacesresponse.md)**


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
    cluster_name='soluta',
    deployment_type=[
        'earum',
    ],
    download_as_xlsx=False,
    name='Mr. Roy Conn',
    no_pagination=False,
    template_source=[
        'ad',
    ],
)

res = s.kubernetes.get_pod_definitions(req)

if res.pod_definitions is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetPodDefinitionsRequest](../../models/operations/getpoddefinitionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetPodDefinitionsResponse](../../models/operations/getpoddefinitionsresponse.md)**


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
    account_name='velit',
    agent_fail_close=False,
    api_intelligence_dast=False,
    auto_label_enabled=False,
    auto_upgrade_controller_version=False,
    automated_policy_requires_deployer=False,
    ci_image_signature_validation=False,
    ci_image_validation=False,
    cluster_pod_definition_source=shared.ClusterPodDefinitionSource.KUBERNETES,
    controller_data_response=shared.ControllerDataResponse(
        agent_id='9d98387f-7a79-4cd7-acd2-484da21729f2',
        shared_key='similique',
    ),
    controller_status=shared.ControllerStatus.WAITING_FOR_USER_UPDATE,
    enable_connections_control=False,
    helm_commands_installation=shared.HelmCommandsInstallation(
        istio_helm_command='numquam',
        panoptica_helm_command='inventore',
        vault_helm_command='necessitatibus',
    ),
    id='f5725f11-69ac-41e4-9d8a-23c23e34f2df',
    install_envoy_tracing_support=False,
    install_tracing_support=False,
    installation_source=shared.InstallationSource.HELM,
    internal_registry_parameters=shared.InternalRegistryParameters(
        internal_registry='quaerat',
        internal_registry_enabled=False,
    ),
    is_hold_application_until_proxy_starts=False,
    is_istio_ingress_enabled=False,
    is_multi_cluster=False,
    is_persistent=False,
    istio_ingress_annotations=[
        shared.KubernetesAnnotation(
            key='officia',
            value='sunt',
        ),
    ],
    istio_installation_parameters=shared.IstioInstallationParameters(
        is_istio_already_installed=False,
        istio_version='perspiciatis',
    ),
    k8s_events_enabled=False,
    kubernetes_security=False,
    minimal_number_of_controller_replicas=461758,
    name='Elmer Stokes',
    orchestration_type=shared.KubernetesClusterOrchestrationType.GKE,
    preserve_original_source_ip=False,
    proxy_configuration=shared.ProxyConfiguration(
        enable_proxy=False,
        https_proxy='aspernatur',
    ),
    restrict_registires=False,
    scan_configuration=shared.ScanConfiguration(
        number_of_scanners=91136,
        scan_types=[
            shared.ScanType.VULNERABILITIES,
        ],
    ),
    service_discovery_isolation_enabled=False,
    sidecars_resources=shared.SidecarsResource(
        proxy_init_limits_cpu='et',
        proxy_init_limits_memory='delectus',
        proxy_init_requests_cpu='saepe',
        proxy_init_requests_memory='sunt',
        proxy_limits_cpu='in',
        proxy_limits_memory='architecto',
        proxy_request_cpu='sed',
        proxy_request_memory='voluptatem',
    ),
    ssh_monitor_disabled=False,
    support_external_trace_source=False,
    tls_inspection_enabled=False,
    token_injection_enabled=False,
    use_external_ca=False,
)

res = s.kubernetes.post_kubernetes_clusters(req)

if res.kubernetes_cluster is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.KubernetesCluster](../../models/shared/kubernetescluster.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostKubernetesClustersResponse](../../models/operations/postkubernetesclustersresponse.md)**


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
    cluster_id='99853e9f-543d-4854-839e-e224460443bc',
    containers=[
        shared.Container(
            image=shared.Image(
                dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
                hash='minima',
                repository='magnam',
                tag='vitae',
                vulnerability_severity_level=shared.VulnerabilitySeverity.MEDIUM,
            ),
        ),
    ],
    init_containers=[
        shared.Container(
            image=shared.Image(
                dockerfile_scan_severity=shared.DockerfileScanSeverity.WARN,
                hash='quisquam',
                repository='sunt',
                tag='asperiores',
                vulnerability_severity_level=shared.VulnerabilitySeverity.LOW,
            ),
        ),
    ],
    kind=shared.PodTemplateKind.CRON_JOB,
    labels=[
        shared.Label(
            key='accusamus',
            value='totam',
        ),
    ],
    name='Cristina Nader',
    pod_definition_source=shared.PodDefinitionSource.KUBERNETES,
)

res = s.kubernetes.post_pod_definitions(req)

if res.pod_definition is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PodDefinitionInput](../../models/shared/poddefinitioninput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostPodDefinitionsResponse](../../models/operations/postpoddefinitionsresponse.md)**


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
        account_name='odit',
        agent_fail_close=False,
        api_intelligence_dast=False,
        auto_label_enabled=False,
        auto_upgrade_controller_version=False,
        automated_policy_requires_deployer=False,
        ci_image_signature_validation=False,
        ci_image_validation=False,
        cluster_pod_definition_source=shared.ClusterPodDefinitionSource.CD,
        controller_data_response=shared.ControllerDataResponse(
            agent_id='abd617c3-b0d5-41a4-8bf0-1bad8706d460',
            shared_key='laudantium',
        ),
        controller_status=shared.ControllerStatus.ACTIVE,
        enable_connections_control=False,
        helm_commands_installation=shared.HelmCommandsInstallation(
            istio_helm_command='libero',
            panoptica_helm_command='maiores',
            vault_helm_command='nam',
        ),
        id='dc41ff5d-4e2a-4e4f-b5cb-35d17638f1ed',
        install_envoy_tracing_support=False,
        install_tracing_support=False,
        installation_source=shared.InstallationSource.HELM,
        internal_registry_parameters=shared.InternalRegistryParameters(
            internal_registry='ducimus',
            internal_registry_enabled=False,
        ),
        is_hold_application_until_proxy_starts=False,
        is_istio_ingress_enabled=False,
        is_multi_cluster=False,
        is_persistent=False,
        istio_ingress_annotations=[
            shared.KubernetesAnnotation(
                key='atque',
                value='consectetur',
            ),
        ],
        istio_installation_parameters=shared.IstioInstallationParameters(
            is_istio_already_installed=False,
            istio_version='nemo',
        ),
        k8s_events_enabled=False,
        kubernetes_security=False,
        minimal_number_of_controller_replicas=592760,
        name='Kim Rutherford',
        orchestration_type=shared.KubernetesClusterOrchestrationType.EKS,
        preserve_original_source_ip=False,
        proxy_configuration=shared.ProxyConfiguration(
            enable_proxy=False,
            https_proxy='praesentium',
        ),
        restrict_registires=False,
        scan_configuration=shared.ScanConfiguration(
            number_of_scanners=427859,
            scan_types=[
                shared.ScanType.VULNERABILITIES,
            ],
        ),
        service_discovery_isolation_enabled=False,
        sidecars_resources=shared.SidecarsResource(
            proxy_init_limits_cpu='delectus',
            proxy_init_limits_memory='quas',
            proxy_init_requests_cpu='impedit',
            proxy_init_requests_memory='illum',
            proxy_limits_cpu='ullam',
            proxy_limits_memory='praesentium',
            proxy_request_cpu='perferendis',
            proxy_request_memory='soluta',
        ),
        ssh_monitor_disabled=False,
        support_external_trace_source=False,
        tls_inspection_enabled=False,
        token_injection_enabled=False,
        use_external_ca=False,
    ),
    kubernetes_cluster_id='a73810e4-fe44-4472-97cd-3b1dd3bbce24',
)

res = s.kubernetes.put_kubernetes_clusters_kubernetes_cluster_id_(req)

if res.kubernetes_cluster is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PutKubernetesClustersKubernetesClusterIDRequest](../../models/operations/putkubernetesclusterskubernetesclusteridrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.PutKubernetesClustersKubernetesClusterIDResponse](../../models/operations/putkubernetesclusterskubernetesclusteridresponse.md)**


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
    edit_kubernetes_cluster_managed_by_helm=shared.EditKubernetesClusterManagedByHelm(
        name='Opal Klocko',
    ),
    kubernetes_cluster_id='4eff5012-6d71-4cff-bd0e-b74b8421953b',
)

res = s.kubernetes.put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm(req)

if res.kubernetes_cluster is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmRequest](../../models/operations/putkubernetesclusterskubernetesclusteridmanagedbyhelmrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmResponse](../../models/operations/putkubernetesclusterskubernetesclusteridmanagedbyhelmresponse.md)**


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
    pod_definition_input=shared.PodDefinitionInput(
        cluster_id='44bd3c43-159d-433e-9953-c001139863aa',
        containers=[
            shared.Container(
                image=shared.Image(
                    dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
                    hash='et',
                    repository='eveniet',
                    tag='aliquid',
                    vulnerability_severity_level=shared.VulnerabilitySeverity.HIGH,
                ),
            ),
        ],
        init_containers=[
            shared.Container(
                image=shared.Image(
                    dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
                    hash='ab',
                    repository='maxime',
                    tag='porro',
                    vulnerability_severity_level=shared.VulnerabilitySeverity.UNKNOWN,
                ),
            ),
        ],
        kind=shared.PodTemplateKind.OTHER,
        labels=[
            shared.Label(
                key='dicta',
                value='hic',
            ),
        ],
        name='Miss Geoffrey Herman',
        pod_definition_source=shared.PodDefinitionSource.MANUAL,
    ),
    pod_id='41ffbe9c-bd79-45ee-a5e0-76cc7abf616e',
)

res = s.kubernetes.put_pod_definitions_pod_id_(req)

if res.pod_definition is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutPodDefinitionsPodIDRequest](../../models/operations/putpoddefinitionspodidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PutPodDefinitionsPodIDResponse](../../models/operations/putpoddefinitionspodidresponse.md)**

