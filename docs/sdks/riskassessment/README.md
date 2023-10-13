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
    ignored_risk_id='591339a8-adc9-48b1-82f6-1d3cce316b8d',
)

res = s.risk_assessment.delete_risk_assessment_ignored_risks_ignored_risk_id_(req)

if res.status_code == 200:
    # handle response
    pass
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
    kubernetes_cluster_id='0086ba38-7819-4a93-be05-2abfdf0aef92',
)

res = s.risk_assessment.delete_risk_assessment_kubernetes_cluster_id_cancel(req)

if res.status_code == 200:
    # handle response
    pass
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
    pass
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
    pass
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
        'a89898f1-37f8-4c09-8113-2e54dc492339',
    ],
)

res = s.risk_assessment.get_risk_assessment_permissions(req)

if res.cluster_permissions is not None:
    # handle response
    pass
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
    cluster_id='af306627-d7b5-4fd9-a554-cf5effac095b',
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_(req)

if res.owner_response is not None:
    # handle response
    pass
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
    cluster_id='e6c26498-20da-481b-bc16-7b830d3456dd',
    owner_id='79a8a441-40ea-4cdf-8584-73da2c62b846',
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_owner_id_(req)

if res.permission_response is not None:
    # handle response
    pass
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
    cluster_id='419337aa-84cc-4a55-afba-5a213e1dbdfd',
    owner_id='4e00792b-c0ad-4551-9794-d6bafdbc8352',
    role_id='ad0304b4-bb83-44d6-bf7f-174c17202a1e',
)

res = s.risk_assessment.get_risk_assessment_permissions_cluster_id_owner_id_role_id_(req)

if res.permission_role_response is not None:
    # handle response
    pass
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
        '813cbccb-b94b-4a50-afbd-d7c394a6030d',
    ],
)

res = s.risk_assessment.get_risk_assessment_poll(req)

if res.risk_assessment_clusters is not None:
    # handle response
    pass
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
    image_id='6cbcdb90-f642-47ed-b640-ae8227deac5c',
    sort_key=operations.GetRiskAssessmentImageIDVulnerabilitiesSortKey.SEVERITY,
)

res = s.risk_assessment.get_risk_assessment_image_id_vulnerabilities(req)

if res.risk_assessment_vulnerabilities is not None:
    # handle response
    pass
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
    kubernetes_cluster_id='764514eb-01d8-4d87-972e-7065c0075222',
    sort_key=operations.GetRiskAssessmentKubernetesClusterIDPodsSortKey.NAME,
)

res = s.risk_assessment.get_risk_assessment_kubernetes_cluster_id_pods(req)

if res.risk_assessment_pods is not None:
    # handle response
    pass
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
    pass
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
            'fda4268f-7c78-46d3-87e2-782993d8ba4d',
        ],
    ),
    action_type=operations.PostRiskAssessmentPermissionsOwnerIDApproveActionType.REMOVE,
    owner_id='c3b8ad34-72d2-4f81-a59b-f81c3cc9c10e',
)

res = s.risk_assessment.post_risk_assessment_permissions_owner_id_approve(req)

if res.status_code == 200:
    # handle response
    pass
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
    kubernetes_cluster_id='967e4e2b-c728-4357-980a-727b8f594aad',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_scan(req)

if res.post_risk_assessment_kubernetes_cluster_id_scan_201_application_json_uuid_string is not None:
    # handle response
    pass
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
        max_parallelism=752536,
        minimum_severity=shared.VulnerabilitySeverity.LOW,
        namespaces=[
            'synthesizing',
        ],
        periodic_job_expression=shared.PeriodicJobExpression(
            periodic_job_type=shared.PeriodicJobExpressionPeriodicJobType.NON_PERIODIC_JOB_EXPRESSION,
        ),
    ),
    kubernetes_cluster_id='a0c9884d-ef8c-417b-9484-5665df2f730e',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_settings(req)

if res.post_risk_assessment_kubernetes_cluster_id_settings_201_application_json_uuid_string is not None:
    # handle response
    pass
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
        dockerfile_scan_ci_policy=shared.DockerfileScanCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_dockerfile_scan_severity=shared.DockerfileScanSeverity.INFO,
        ),
        name='Bentley Intersex feed',
        vulnerability_ci_policy=shared.VulnerabilityCiPolicy(
            enforcement_option=shared.EnforcementOption.FAIL,
            permissible_vulnerability_level=shared.VulnerabilitySeverity.HIGH,
        ),
    ),
    ignored_risk_id='52b6ef16-d35f-4df8-929c-311ad619343e',
)

res = s.risk_assessment.put_risk_assessment_ignored_risks_ignored_risk_id_(req)

if res.ignored_risk is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDRequest](../../models/operations/putriskassessmentignoredrisksignoredriskidrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDResponse](../../models/operations/putriskassessmentignoredrisksignoredriskidresponse.md)**

