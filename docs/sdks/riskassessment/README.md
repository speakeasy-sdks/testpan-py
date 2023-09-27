# RiskAssessment
(*risk_assessment*)

## Overview

APIs used to manage risk assessment on Kubernetes clusters

### Available Operations

* [delete_risk_assessment_ignored_risks_ignored_risk_id_](#delete_risk_assessment_ignored_risks_ignored_risk_id_) - Delete ignored risk
* [delete_risk_assessment_kubernetes_cluster_id_cancel](#delete_risk_assessment_kubernetes_cluster_id_cancel) - Cancel the runtime scan on the given cluster with the given id
* [get_risk_assessment](#get_risk_assessment) - Get risk assessment data for all clusters
* [get_risk_assessment_ignored_risks](#get_risk_assessment_ignored_risks) - Get all the ignored risks
* [get_risk_assessment_permissions](#get_risk_assessment_permissions) - Get list of clusters and their permissions
* [get_risk_assessment_permissions_cluster_id_](#get_risk_assessment_permissions_cluster_id_) - Get all of the users permissions
* [get_risk_assessment_permissions_cluster_id_owner_id_](#get_risk_assessment_permissions_cluster_id_owner_id_) - Get the owner permissions
* [get_risk_assessment_permissions_cluster_id_owner_id_role_id_](#get_risk_assessment_permissions_cluster_id_owner_id_role_id_) - Get the owner permissions
* [get_risk_assessment_poll](#get_risk_assessment_poll) - Poll running scans
* [get_risk_assessment_image_id_vulnerabilities](#get_risk_assessment_image_id_vulnerabilities) - Get all images of given risk assessment pod
* [get_risk_assessment_kubernetes_cluster_id_pods](#get_risk_assessment_kubernetes_cluster_id_pods) - Get all risk assessments of all pods of given cluster
* [post_risk_assessment_ignored_risks](#post_risk_assessment_ignored_risks) - Add ignore risk
* [post_risk_assessment_permissions_owner_id_approve](#post_risk_assessment_permissions_owner_id_approve) - add / remove permissions to /from the approved permissions list
* [post_risk_assessment_kubernetes_cluster_id_scan](#post_risk_assessment_kubernetes_cluster_id_scan) - Execute a new runtime scan on the given cluster with the given configuration
* [post_risk_assessment_kubernetes_cluster_id_settings](#post_risk_assessment_kubernetes_cluster_id_settings) - Save the runtime scan configuration on the given cluster
* [put_risk_assessment_ignored_risks_ignored_risk_id_](#put_risk_assessment_ignored_risks_ignored_risk_id_) - Edit ignore risk

## delete_risk_assessment_ignored_risks_ignored_risk_id_

Delete ignored risk

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

req = operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDRequest(
    ignored_risk_id='1bc74b86-cecc-474f-b7b4-848bd6a6f044',
)

res = s.risk_assessment.delete_risk_assessment_ignored_risks_ignored_risk_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDRequest](../../models/operations/deleteriskassessmentignoredrisksignoredriskidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDResponse](../../models/operations/deleteriskassessmentignoredrisksignoredriskidresponse.md)**


## delete_risk_assessment_kubernetes_cluster_id_cancel

Cancel the runtime scan on the given cluster with the given id

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

req = operations.DeleteRiskAssessmentKubernetesClusterIDCancelRequest(
    kubernetes_cluster_id='1d2c3b80-8094-4373-a060-459bebbad02f',
)

res = s.risk_assessment.delete_risk_assessment_kubernetes_cluster_id_cancel(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteRiskAssessmentKubernetesClusterIDCancelRequest](../../models/operations/deleteriskassessmentkubernetesclusteridcancelrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.DeleteRiskAssessmentKubernetesClusterIDCancelResponse](../../models/operations/deleteriskassessmentkubernetesclusteridcancelresponse.md)**


## get_risk_assessment

Get risk assessment data for all clusters

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


res = s.risk_assessment.get_risk_assessment()

if res.risk_assessment_clusters is not None:
    # handle response
```


### Response

**[operations.GetRiskAssessmentResponse](../../models/operations/getriskassessmentresponse.md)**


## get_risk_assessment_ignored_risks

Get all the ignored risks

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


res = s.risk_assessment.get_risk_assessment_ignored_risks()

if res.ignored_risks is not None:
    # handle response
```


### Response

**[operations.GetRiskAssessmentIgnoredRisksResponse](../../models/operations/getriskassessmentignoredrisksresponse.md)**


## get_risk_assessment_permissions

Get list of clusters and their permissions

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

req = operations.GetRiskAssessmentPermissionsRequest(
    clusters_ids=[
        '2586bcf1-5255-48da-a95b-e6cd02756c35',
    ],
    include_system_owners=False,
    permission_risk=operations.GetRiskAssessmentPermissionsPermissionRisk.MEDIUM,
    sort_dir=operations.GetRiskAssessmentPermissionsSortDir.DESC,
    sort_key=operations.GetRiskAssessmentPermissionsSortKey.PERMISSION_RISK,
)

res = s.risk_assessment.get_risk_assessment_permissions(req)

if res.cluster_permissions is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetRiskAssessmentPermissionsRequest](../../models/operations/getriskassessmentpermissionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetRiskAssessmentPermissionsResponse](../../models/operations/getriskassessmentpermissionsresponse.md)**


## get_risk_assessment_permissions_cluster_id_

Get all of the users permissions

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

req = operations.GetRiskAssessmentPermissionsClusterIDRequest(
    cluster_id='a432b47e-1763-4c52-88c2-3e9802d82f0d',
    include_system_owners=False,
    max_results=3011.88,
    namespace_name='quis',
    no_pagination=False,
    offset=9204.88,
    owner='soluta',
    owner_type=operations.GetRiskAssessmentPermissionsClusterIDOwnerType.SERVICEACCOUNT,
    permission_risk=operations.GetRiskAssessmentPermissionsClusterIDPermissionRisk.HIGH,
    sort_dir=operations.GetRiskAssessmentPermissionsClusterIDSortDir.DESC,
    sort_key=operations.GetRiskAssessmentPermissionsClusterIDSortKey.OWNER_TYPE,
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_(req)

if res.owner_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetRiskAssessmentPermissionsClusterIDRequest](../../models/operations/getriskassessmentpermissionsclusteridrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetRiskAssessmentPermissionsClusterIDResponse](../../models/operations/getriskassessmentpermissionsclusteridresponse.md)**


## get_risk_assessment_permissions_cluster_id_owner_id_

Get the owner permissions

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

req = operations.GetRiskAssessmentPermissionsClusterIDOwnerIDRequest(
    cluster_id='674ee5cf-c18e-4dc7-b787-e32e04b3d3ed',
    is_approved=False,
    owner_id='0c5670ef-42bd-43c9-b1cc-503f6c39bcd0',
    sort_dir=operations.GetRiskAssessmentPermissionsClusterIDOwnerIDSortDir.DESC,
    sort_key=operations.GetRiskAssessmentPermissionsClusterIDOwnerIDSortKey.RISK,
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_owner_id_(req)

if res.permission_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetRiskAssessmentPermissionsClusterIDOwnerIDRequest](../../models/operations/getriskassessmentpermissionsclusteridowneridrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetRiskAssessmentPermissionsClusterIDOwnerIDResponse](../../models/operations/getriskassessmentpermissionsclusteridowneridresponse.md)**


## get_risk_assessment_permissions_cluster_id_owner_id_role_id_

Get the owner permissions

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

req = operations.GetRiskAssessmentPermissionsClusterIDOwnerIDRoleIDRequest(
    cluster_id='6290f957-f385-4189-ad7e-f807aae03f33',
    owner_id='ca79fb9d-e403-42ba-a6fd-368ba9216bcb',
    role_id='415835c7-3641-4723-933e-dc046bc5163b',
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_owner_id_role_id_(req)

if res.permission_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetRiskAssessmentPermissionsClusterIDOwnerIDRoleIDRequest](../../models/operations/getriskassessmentpermissionsclusteridowneridroleidrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetRiskAssessmentPermissionsClusterIDOwnerIDRoleIDResponse](../../models/operations/getriskassessmentpermissionsclusteridowneridroleidresponse.md)**


## get_risk_assessment_poll

Poll running scans

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

req = operations.GetRiskAssessmentPollRequest(
    risk_assessment_poll_key=[
        'bca49227-c42c-422c-9535-0495c5dbb3c5',
    ],
)

res = s.risk_assessment.get_risk_assessment_poll(req)

if res.risk_assessment_clusters is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetRiskAssessmentPollRequest](../../models/operations/getriskassessmentpollrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetRiskAssessmentPollResponse](../../models/operations/getriskassessmentpollresponse.md)**


## get_risk_assessment_image_id_vulnerabilities

Get all images of given risk assessment pod

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

req = operations.GetRiskAssessmentImageIDVulnerabilitiesRequest(
    image_id='7c1e4981-e8aa-4257-9dc1-912ebde64bfc',
    max_results=7713.03,
    offset=3303.58,
    sort_dir=operations.GetRiskAssessmentImageIDVulnerabilitiesSortDir.ASC,
    sort_key=operations.GetRiskAssessmentImageIDVulnerabilitiesSortKey.SEVERITY,
)

res = s.risk_assessment.get_risk_assessment_image_id_vulnerabilities(req)

if res.risk_assessment_vulnerabilities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetRiskAssessmentImageIDVulnerabilitiesRequest](../../models/operations/getriskassessmentimageidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetRiskAssessmentImageIDVulnerabilitiesResponse](../../models/operations/getriskassessmentimageidvulnerabilitiesresponse.md)**


## get_risk_assessment_kubernetes_cluster_id_pods

Get all risk assessments of all pods of given cluster

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

req = operations.GetRiskAssessmentKubernetesClusterIDPodsRequest(
    download_as_xlsx=False,
    kubernetes_cluster_id='69d4015d-fa79-4620-abef-2b0a3e42c1aa',
    max_results=173.42,
    namespaces_names_filter='illo',
    offset=172.89,
    sort_dir=operations.GetRiskAssessmentKubernetesClusterIDPodsSortDir.DESC,
    sort_key=operations.GetRiskAssessmentKubernetesClusterIDPodsSortKey.RISK,
)

res = s.risk_assessment.get_risk_assessment_kubernetes_cluster_id_pods(req)

if res.risk_assessment_pods is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetRiskAssessmentKubernetesClusterIDPodsRequest](../../models/operations/getriskassessmentkubernetesclusteridpodsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.GetRiskAssessmentKubernetesClusterIDPodsResponse](../../models/operations/getriskassessmentkubernetesclusteridpodsresponse.md)**


## post_risk_assessment_ignored_risks

Add ignore risk

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


res = s.risk_assessment.post_risk_assessment_ignored_risks()

if res.ignored_risk is not None:
    # handle response
```


### Response

**[operations.PostRiskAssessmentIgnoredRisksResponse](../../models/operations/postriskassessmentignoredrisksresponse.md)**


## post_risk_assessment_permissions_owner_id_approve

add / remove permissions to /from the approved permissions list

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

req = operations.PostRiskAssessmentPermissionsOwnerIDApproveRequest(
    uuid_list=shared.UUIDList(
        uuid_list=[
            'aac2e913-5586-4d18-b9f9-7a4bfad2bf7d',
        ],
    ),
    action_type=operations.PostRiskAssessmentPermissionsOwnerIDApproveActionType.ADD,
    owner_id='7ca84ad9-9b41-4d61-a435-31870cf68b03',
)

res = s.risk_assessment.post_risk_assessment_permissions_owner_id_approve(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PostRiskAssessmentPermissionsOwnerIDApproveRequest](../../models/operations/postriskassessmentpermissionsowneridapproverequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PostRiskAssessmentPermissionsOwnerIDApproveResponse](../../models/operations/postriskassessmentpermissionsowneridapproveresponse.md)**


## post_risk_assessment_kubernetes_cluster_id_scan

Execute a new runtime scan on the given cluster with the given configuration

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

req = operations.PostRiskAssessmentKubernetesClusterIDScanRequest(
    kubernetes_cluster_id='ad421bd4-3d1f-40cb-8a00-03eb22d9b3a7',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_scan(req)

if res.post_risk_assessment_kubernetes_cluster_id_scan_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PostRiskAssessmentKubernetesClusterIDScanRequest](../../models/operations/postriskassessmentkubernetesclusteridscanrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PostRiskAssessmentKubernetesClusterIDScanResponse](../../models/operations/postriskassessmentkubernetesclusteridscanresponse.md)**


## post_risk_assessment_kubernetes_cluster_id_settings

Save the runtime scan configuration on the given cluster

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

req = operations.PostRiskAssessmentKubernetesClusterIDSettingsRequest(
    risk_assessment_cluster_scan_config=shared.RiskAssessmentClusterScanConfig(
        max_parallelism=47008,
        minimum_severity=shared.VulnerabilitySeverity.CRITICAL,
        namespaces=[
            'excepturi',
        ],
        periodic_job_expression=shared.PeriodicJobExpression(
            periodic_job_type=shared.PeriodicJobExpressionPeriodicJobType.SINGLE_PERIODIC_JOB_EXPRESSION,
        ),
        run_dockerfile_scan=False,
    ),
    kubernetes_cluster_id='faa741c5-7d1f-4edc-a050-d38dc3ce1854',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_settings(req)

if res.post_risk_assessment_kubernetes_cluster_id_settings_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.PostRiskAssessmentKubernetesClusterIDSettingsRequest](../../models/operations/postriskassessmentkubernetesclusteridsettingsrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.PostRiskAssessmentKubernetesClusterIDSettingsResponse](../../models/operations/postriskassessmentkubernetesclusteridsettingsresponse.md)**


## put_risk_assessment_ignored_risks_ignored_risk_id_

Edit ignore risk

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

req = operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDRequest(
    ci_policy_input=shared.CiPolicyInput(
        description='iusto',
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.FATAL,
        ),
        name='Santiago Treutel',
        vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_vulnerability_level=shared.VulnerabilitySeverity.MEDIUM,
        ),
    ),
    ignored_risk_id='6a8be344-4eac-48b3-a287-5c6c1fe606d0',
)

res = s.risk_assessment.put_risk_assessment_ignored_risks_ignored_risk_id_(req)

if res.ignored_risk is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDRequest](../../models/operations/putriskassessmentignoredrisksignoredriskidrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDResponse](../../models/operations/putriskassessmentignoredrisksignoredriskidresponse.md)**

