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
    pod_id='1d7b59d4-9a1e-473b-8e2e-c8a463501aa8',
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
    cluster_id='6d4f5b01-1e67-437c-a42b-e9becce491b4',
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
    cluster_name='handle',
    controller_status='Metical withdrawal unless',
    controller_version='Northeast Northeast',
    download_as_xlsx=False,
    kubernetes_version='SMTP PCI soulful',
    max_results=5309.6,
    offset=6721.13,
    only_spec_reconstruction_enabled_filter=False,
    sort_dir=operations.GetKubernetesClustersSortDir.ASC,
    sort_key='background mmm',
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
    kubernetes_cluster_id='6ad413ce-670c-4973-bf8a-5a66b7855734',
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
    kubernetes_cluster_id='b06f6c06-c4ec-44f8-ba3a-a7d63215e690',
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
    kubernetes_cluster_id='204aba8f-ddfd-4080-9f3c-89482d02fb76',
    send_telemetries_interval_sec=908942,
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
    kubernetes_cluster_id='f7710c3a-4d45-43f9-898d-e19416c2b527',
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
    kubernetes_cluster_id='b18474d1-b95c-48d9-af1c-951ce15b0be6',
    sort_dir=operations.GetKubernetesClustersKubernetesClusterIDNamespacesSortDir.DESC,
    sort_key=operations.GetKubernetesClustersKubernetesClusterIDNamespacesSortKey.NAME,
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
    kubernetes_cluster_id='1b08f941-6d25-44a9-8a5a-94e46b69d5cc',
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
    cluster_name='sensor Granite',
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
    cluster_name='Thorium',
    download_as_xlsx=False,
    max_results=6640.03,
    namespace_name='mindshare',
    offset=617.97,
    protection_status=operations.GetNamespacesProtectionStatus.DISABLED,
    sort_dir=operations.GetNamespacesSortDir.DESC,
    sort_key=operations.GetNamespacesSortKey.PROTECTION_STATUS,
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
    cluster_name='Illinois Savings',
    deployment_type=[
        'disclaimer',
    ],
    download_as_xlsx=False,
    name='Multigender M2F',
    no_pagination=False,
    template_source=[
        'Boulder',
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
    account_name='withdrawal',
    agent_fail_close=False,
    api_intelligence_dast=False,
    auto_label_enabled=False,
    auto_upgrade_controller_version=False,
    automated_policy_requires_deployer=False,
    ci_image_signature_validation=False,
    ci_image_validation=False,
    cluster_pod_definition_source=shared.ClusterPodDefinitionSource.KUBERNETES,
    controller_data_response=shared.ControllerDataResponse(
        agent_id='81eb935a-67c1-4676-82ab-92109ab1c541',
        shared_key='Movies',
    ),
    controller_status=shared.ControllerStatus.UNKNOWN,
    enable_connections_control=False,
    helm_commands_installation=shared.HelmCommandsInstallation(
        istio_helm_command='wherever Bedfordshire',
        panoptica_helm_command='Personal generation Small',
        vault_helm_command='Generic than',
    ),
    id='6e76a9b0-598f-49f4-b42b-b8cf86555cd8',
    install_envoy_tracing_support=False,
    install_tracing_support=False,
    installation_source=shared.InstallationSource.HELM,
    internal_registry_parameters=shared.InternalRegistryParameters(
        internal_registry='Pines Trial',
        internal_registry_enabled=False,
    ),
    is_hold_application_until_proxy_starts=False,
    is_istio_ingress_enabled=False,
    is_multi_cluster=False,
    is_persistent=False,
    istio_ingress_annotations=[
        shared.KubernetesAnnotation(
            key='<key>',
            value='upright maximize verbally',
        ),
    ],
    istio_installation_parameters=shared.IstioInstallationParameters(
        is_istio_already_installed=False,
        istio_version='ladybug',
    ),
    k8s_events_enabled=False,
    kubernetes_security=False,
    minimal_number_of_controller_replicas=225610,
    name='female Branding Architect',
    orchestration_type=shared.KubernetesClusterOrchestrationType.RANCHER,
    preserve_original_source_ip=False,
    proxy_configuration=shared.ProxyConfiguration(
        enable_proxy=False,
        https_proxy='Customer befriend',
    ),
    restrict_registires=False,
    scan_configuration=shared.ScanConfiguration(
        number_of_scanners=127892,
        scan_types=[
            shared.ScanType.VULNERABILITIES,
        ],
    ),
    service_discovery_isolation_enabled=False,
    sidecars_resources=shared.SidecarsResource(
        proxy_init_limits_cpu='meter deposit South',
        proxy_init_limits_memory='compress Lake',
        proxy_init_requests_cpu='as Tactics mobile',
        proxy_init_requests_memory='blue Manager Program',
        proxy_limits_cpu='achievement Optimization',
        proxy_limits_memory='Zirconium',
        proxy_request_cpu='fuchsia Texas Ergonomic',
        proxy_request_memory='Longview',
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
    cluster_id='caf647ad-b35e-4462-baa4-a61d2b4e2410',
    containers=[
        shared.Container(
            image=shared.Image(
                dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
                hash='Folk',
                repository='Smart Trigender',
                tag='Analyst',
                vulnerability_severity_level=shared.VulnerabilitySeverity.HIGH,
            ),
        ),
    ],
    init_containers=[
        shared.Container(
            image=shared.Image(
                dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
                hash='yellow Solutions geez',
                repository='resound mobile applications',
                tag='meh',
                vulnerability_severity_level=shared.VulnerabilitySeverity.LOW,
            ),
        ),
    ],
    kind=shared.PodTemplateKind.REPLICA_SET,
    labels=[
        shared.Label(
            key='<key>',
            value='unless',
        ),
    ],
    name='payment Michigan',
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
        account_name='savior normalization absentmindedly',
        agent_fail_close=False,
        api_intelligence_dast=False,
        auto_label_enabled=False,
        auto_upgrade_controller_version=False,
        automated_policy_requires_deployer=False,
        ci_image_signature_validation=False,
        ci_image_validation=False,
        cluster_pod_definition_source=shared.ClusterPodDefinitionSource.CD,
        controller_data_response=shared.ControllerDataResponse(
            agent_id='d957958a-0796-4a5f-ad9d-7f9c73b14840',
            shared_key='Fantastic Berkshire',
        ),
        controller_status=shared.ControllerStatus.PENDING_INSTALL,
        enable_connections_control=False,
        helm_commands_installation=shared.HelmCommandsInstallation(
            istio_helm_command='orange Central invoice',
            panoptica_helm_command='pascal to squeegee',
            vault_helm_command='parsing blissfully pine',
        ),
        id='f781f7b5-14b5-45e8-9b88-a92334e6deac',
        install_envoy_tracing_support=False,
        install_tracing_support=False,
        installation_source=shared.InstallationSource.HELM,
        internal_registry_parameters=shared.InternalRegistryParameters(
            internal_registry='North Highlands',
            internal_registry_enabled=False,
        ),
        is_hold_application_until_proxy_starts=False,
        is_istio_ingress_enabled=False,
        is_multi_cluster=False,
        is_persistent=False,
        istio_ingress_annotations=[
            shared.KubernetesAnnotation(
                key='<key>',
                value='ADP Seamless',
            ),
        ],
        istio_installation_parameters=shared.IstioInstallationParameters(
            is_istio_already_installed=False,
            istio_version='Southeast',
        ),
        k8s_events_enabled=False,
        kubernetes_security=False,
        minimal_number_of_controller_replicas=890421,
        name='delectus Rap Awesome',
        orchestration_type=shared.KubernetesClusterOrchestrationType.IKS,
        preserve_original_source_ip=False,
        proxy_configuration=shared.ProxyConfiguration(
            enable_proxy=False,
            https_proxy='Directives spar Handcrafted',
        ),
        restrict_registires=False,
        scan_configuration=shared.ScanConfiguration(
            number_of_scanners=663885,
            scan_types=[
                shared.ScanType.VULNERABILITIES,
            ],
        ),
        service_discovery_isolation_enabled=False,
        sidecars_resources=shared.SidecarsResource(
            proxy_init_limits_cpu='tan comic tan',
            proxy_init_limits_memory='Rubber',
            proxy_init_requests_cpu='Sleek drain sensor',
            proxy_init_requests_memory='indexing Hackensack',
            proxy_limits_cpu='superstructure',
            proxy_limits_memory='generating',
            proxy_request_cpu='micronutrient',
            proxy_request_memory='pro Cambridgeshire',
        ),
        ssh_monitor_disabled=False,
        support_external_trace_source=False,
        tls_inspection_enabled=False,
        token_injection_enabled=False,
        use_external_ca=False,
    ),
    kubernetes_cluster_id='96a74b13-6974-4b67-a067-bd753e149f7b',
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
        name='transmitter innocently',
    ),
    kubernetes_cluster_id='ff47cf23-f7b6-483e-bd0b-e8fe575edb2f',
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
        cluster_id='8813d860-716a-4bd1-be6a-f36d0732a688',
        containers=[
            shared.Container(
                image=shared.Image(
                    dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
                    hash='female West',
                    repository='Cyclocross female jubilant',
                    tag='Rubber Tamiami',
                    vulnerability_severity_level=shared.VulnerabilitySeverity.LOW,
                ),
            ),
        ],
        init_containers=[
            shared.Container(
                image=shared.Image(
                    dockerfile_scan_severity=shared.DockerfileScanSeverity.WARN,
                    hash='Southeast custody',
                    repository='Music Unbranded Visionary',
                    tag='Squares towards',
                    vulnerability_severity_level=shared.VulnerabilitySeverity.LOW,
                ),
            ),
        ],
        kind=shared.PodTemplateKind.STATEFUL_SET,
        labels=[
            shared.Label(
                key='<key>',
                value='actualize Dollar',
            ),
        ],
        name='opt virtual copying',
        pod_definition_source=shared.PodDefinitionSource.HELM,
    ),
    pod_id='d7ad7bdf-9c15-4917-b40e-79415cfed383',
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

