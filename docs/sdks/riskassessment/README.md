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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDRequest(
    ignored_risk_id='591339a8-adc9-48b1-82f6-1d3cce316b8d',
)

res = s.risk_assessment.delete_risk_assessment_ignored_risks_ignored_risk_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDRequest](../../models/operations/deleteriskassessmentignoredrisksignoredriskidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.DeleteRiskAssessmentIgnoredRisksIgnoredRiskIDResponse](../../models/operations/deleteriskassessmentignoredrisksignoredriskidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_risk_assessment_kubernetes_cluster_id_cancel

Cancel the runtime scan on the given cluster with the given id

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteRiskAssessmentKubernetesClusterIDCancelRequest(
    kubernetes_cluster_id='0086ba38-7819-4a93-be05-2abfdf0aef92',
)

res = s.risk_assessment.delete_risk_assessment_kubernetes_cluster_id_cancel(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.DeleteRiskAssessmentKubernetesClusterIDCancelRequest](../../models/operations/deleteriskassessmentkubernetesclusteridcancelrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.DeleteRiskAssessmentKubernetesClusterIDCancelResponse](../../models/operations/deleteriskassessmentkubernetesclusteridcancelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment

Get risk assessment data for all clusters

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.risk_assessment.get_risk_assessment()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetRiskAssessmentResponse](../../models/operations/getriskassessmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_ignored_risks

Get all the ignored risks

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.risk_assessment.get_risk_assessment_ignored_risks()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetRiskAssessmentIgnoredRisksResponse](../../models/operations/getriskassessmentignoredrisksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_permissions

Get list of clusters and their permissions

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetRiskAssessmentPermissionsRequest()

res = s.risk_assessment.get_risk_assessment_permissions(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetRiskAssessmentPermissionsRequest](../../models/operations/getriskassessmentpermissionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetRiskAssessmentPermissionsResponse](../../models/operations/getriskassessmentpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_permissions_cluster_id_

Get all of the users permissions

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_permissions_cluster_id_owner_id_

Get the owner permissions

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_permissions_cluster_id_owner_id_role_id_

Get the owner permissions

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_poll

Poll running scans

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetRiskAssessmentPollRequest(
    risk_assessment_poll_key=[
        '813cbccb-b94b-4a50-afbd-d7c394a6030d',
    ],
)

res = s.risk_assessment.get_risk_assessment_poll(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetRiskAssessmentPollRequest](../../models/operations/getriskassessmentpollrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetRiskAssessmentPollResponse](../../models/operations/getriskassessmentpollresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_image_id_vulnerabilities

Get all images of given risk assessment pod

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetRiskAssessmentImageIDVulnerabilitiesRequest(
    image_id='6cbcdb90-f642-47ed-b640-ae8227deac5c',
    sort_key=operations.GetRiskAssessmentImageIDVulnerabilitiesQueryParamSortKey.SEVERITY,
)

res = s.risk_assessment.get_risk_assessment_image_id_vulnerabilities(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetRiskAssessmentImageIDVulnerabilitiesRequest](../../models/operations/getriskassessmentimageidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetRiskAssessmentImageIDVulnerabilitiesResponse](../../models/operations/getriskassessmentimageidvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_risk_assessment_kubernetes_cluster_id_pods

Get all risk assessments of all pods of given cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetRiskAssessmentKubernetesClusterIDPodsRequest(
    kubernetes_cluster_id='764514eb-01d8-4d87-972e-7065c0075222',
    sort_key=operations.GetRiskAssessmentKubernetesClusterIDPodsQueryParamSortKey.RISK,
)

res = s.risk_assessment.get_risk_assessment_kubernetes_cluster_id_pods(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetRiskAssessmentKubernetesClusterIDPodsRequest](../../models/operations/getriskassessmentkubernetesclusteridpodsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.GetRiskAssessmentKubernetesClusterIDPodsResponse](../../models/operations/getriskassessmentkubernetesclusteridpodsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_risk_assessment_ignored_risks

Add ignore risk

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.risk_assessment.post_risk_assessment_ignored_risks()

if res.ignored_risk is not None:
    # handle response
    pass

```


### Response

**[operations.PostRiskAssessmentIgnoredRisksResponse](../../models/operations/postriskassessmentignoredrisksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_risk_assessment_permissions_owner_id_approve

add / remove permissions to /from the approved permissions list

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostRiskAssessmentPermissionsOwnerIDApproveRequest(
    uuid_list=shared.UUIDList(),
    action_type=operations.PostRiskAssessmentPermissionsOwnerIDApproveQueryParamActionType.REMOVE,
    owner_id='da4268f7-c786-4d34-be27-82993d8ba4dd',
)

res = s.risk_assessment.post_risk_assessment_permissions_owner_id_approve(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PostRiskAssessmentPermissionsOwnerIDApproveRequest](../../models/operations/postriskassessmentpermissionsowneridapproverequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PostRiskAssessmentPermissionsOwnerIDApproveResponse](../../models/operations/postriskassessmentpermissionsowneridapproveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_risk_assessment_kubernetes_cluster_id_scan

Execute a new runtime scan on the given cluster with the given configuration

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostRiskAssessmentKubernetesClusterIDScanRequest(
    kubernetes_cluster_id='967e4e2b-c728-4357-980a-727b8f594aad',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_scan(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PostRiskAssessmentKubernetesClusterIDScanRequest](../../models/operations/postriskassessmentkubernetesclusteridscanrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PostRiskAssessmentKubernetesClusterIDScanResponse](../../models/operations/postriskassessmentkubernetesclusteridscanresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_risk_assessment_kubernetes_cluster_id_settings

Save the runtime scan configuration on the given cluster

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostRiskAssessmentKubernetesClusterIDSettingsRequest(
    risk_assessment_cluster_scan_config=shared.RiskAssessmentClusterScanConfig(
        max_parallelism=752536,
        minimum_severity=shared.VulnerabilitySeverity.LOW,
    ),
    kubernetes_cluster_id='8c1a0c98-84de-4f8c-97bd-4845665df2f7',
)

res = s.risk_assessment.post_risk_assessment_kubernetes_cluster_id_settings(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.PostRiskAssessmentKubernetesClusterIDSettingsRequest](../../models/operations/postriskassessmentkubernetesclusteridsettingsrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.PostRiskAssessmentKubernetesClusterIDSettingsResponse](../../models/operations/postriskassessmentkubernetesclusteridsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_risk_assessment_ignored_risks_ignored_risk_id_

Edit ignore risk

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutRiskAssessmentIgnoredRisksIgnoredRiskIDRequest(
    ci_policy=shared.CiPolicyInput(
        name='<value>',
    ),
    ignored_risk_id='44ed1978-a3a5-42b6-af16-d35fdf8529c3',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
