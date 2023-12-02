# Dashboard
(*dashboard*)

## Overview

APIs to get dashboard statistics

### Available Operations

* [get_dashboard_apisec_risk_findings](#get_dashboard_apisec_risk_findings) - Get API sec risk findings widget
* [get_dashboard_apisec_risk_findings_trend](#get_dashboard_apisec_risk_findings_trend) - Get API sec risk findings trend graph widget for the last 30 days
* [get_dashboard_apisec_specs_and_operations_diffs](#get_dashboard_apisec_specs_and_operations_diffs) - Get API sec specs and operations diffs widget
* [get_dashboard_apisec_top_risky_apis](#get_dashboard_apisec_top_risky_apis) - Get API sec top risky APIs widget
* [get_dashboard_apisec_top_risky_findings](#get_dashboard_apisec_top_risky_findings) - Get API sec top risky findings widget
* [get_dashboard_clusters](#get_dashboard_clusters) - Get the active clusters
* [get_dashboard_connection_telemetries](#get_dashboard_connection_telemetries) - Get pod connection dashboard data for all clusters
* [get_dashboard_kubernetes_audit_logs](#get_dashboard_kubernetes_audit_logs) - Get kubernetes audit logs dashboard data for all clusters
* [get_dashboard_operational_bar](#get_dashboard_operational_bar) - Get the operation data dashboard for the given kubernetesClusterId
* [get_dashboard_permissions](#get_dashboard_permissions) - Get permissions dashboard data for the given kubernetesClusterIds
* [get_dashboard_pod_telemetries](#get_dashboard_pod_telemetries) - Get pod telemetries dashboard data for all clusters
* [get_dashboard_report_download](#get_dashboard_report_download) - Download Secure Application security report
* [get_dashboard_report_status](#get_dashboard_report_status) - Get Secure Application report security status
* [get_dashboard_security_context](#get_dashboard_security_context) - Get security context dashboard data for all clusters
* [get_dashboard_top_security_risks](#get_dashboard_top_security_risks) - Get the top risky deployments dashboard data for the given kubernetesClusterIds
* [get_dashboard_vulnerabilities](#get_dashboard_vulnerabilities) - Get vulnerabilities dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_connection_telemetries](#get_dashboard_kubernetes_cluster_id_connection_telemetries) - Get connection telemetries dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs](#get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs) - Get kubernetes audit logs dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_pod_telemetries](#get_dashboard_kubernetes_cluster_id_pod_telemetries) - Get pod telemetries dashboard data for the given kubernetesClusterId
* [get_licensing_dashboard](#get_licensing_dashboard) - Get licensing dashboard data
* [post_dashboard_report_generate](#post_dashboard_report_generate) - Generate Secure Application security report

## get_dashboard_apisec_risk_findings

Get API sec risk findings widget

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

req = operations.GetDashboardApisecRiskFindingsRequest(
    api_sec_source=operations.QueryParamAPISecSource.INTERNAL,
)

res = s.dashboard.get_dashboard_apisec_risk_findings(req)

if res.api_sec_risk_findings_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecRiskFindingsRequest](../../models/operations/getdashboardapisecriskfindingsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecRiskFindingsResponse](../../models/operations/getdashboardapisecriskfindingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_apisec_risk_findings_trend

Get API sec risk findings trend graph widget for the last 30 days

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

req = operations.GetDashboardApisecRiskFindingsTrendRequest(
    api_sec_source=operations.GetDashboardApisecRiskFindingsTrendQueryParamAPISecSource.INTERNAL,
)

res = s.dashboard.get_dashboard_apisec_risk_findings_trend(req)

if res.api_sec_risk_findings_trend_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetDashboardApisecRiskFindingsTrendRequest](../../models/operations/getdashboardapisecriskfindingstrendrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetDashboardApisecRiskFindingsTrendResponse](../../models/operations/getdashboardapisecriskfindingstrendresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_apisec_specs_and_operations_diffs

Get API sec specs and operations diffs widget

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

req = operations.GetDashboardApisecSpecsAndOperationsDiffsRequest(
    api_sec_source=operations.GetDashboardApisecSpecsAndOperationsDiffsQueryParamAPISecSource.EXTERNAL,
)

res = s.dashboard.get_dashboard_apisec_specs_and_operations_diffs(req)

if res.specs_and_operations_diffs_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetDashboardApisecSpecsAndOperationsDiffsRequest](../../models/operations/getdashboardapisecspecsandoperationsdiffsrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetDashboardApisecSpecsAndOperationsDiffsResponse](../../models/operations/getdashboardapisecspecsandoperationsdiffsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_apisec_top_risky_apis

Get API sec top risky APIs widget

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

req = operations.GetDashboardApisecTopRiskyApisRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyApisQueryParamAPISecSource.EXTERNAL,
)

res = s.dashboard.get_dashboard_apisec_top_risky_apis(req)

if res.api_sec_top_risky_apis_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecTopRiskyApisRequest](../../models/operations/getdashboardapisectopriskyapisrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecTopRiskyApisResponse](../../models/operations/getdashboardapisectopriskyapisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_apisec_top_risky_findings

Get API sec top risky findings widget

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

req = operations.GetDashboardApisecTopRiskyFindingsRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyFindingsQueryParamAPISecSource.INTERNAL,
)

res = s.dashboard.get_dashboard_apisec_top_risky_findings(req)

if res.api_sec_top_risky_findings_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetDashboardApisecTopRiskyFindingsRequest](../../models/operations/getdashboardapisectopriskyfindingsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetDashboardApisecTopRiskyFindingsResponse](../../models/operations/getdashboardapisectopriskyfindingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_clusters

Get the active clusters

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


res = s.dashboard.get_dashboard_clusters()

if res.clusters_details is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardClustersResponse](../../models/operations/getdashboardclustersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_connection_telemetries

Get pod connection dashboard data for all clusters

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


res = s.dashboard.get_dashboard_connection_telemetries()

if res.time_based_widget is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardConnectionTelemetriesResponse](../../models/operations/getdashboardconnectiontelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_kubernetes_audit_logs

Get kubernetes audit logs dashboard data for all clusters

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


res = s.dashboard.get_dashboard_kubernetes_audit_logs()

if res.time_based_widget is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardKubernetesAuditLogsResponse](../../models/operations/getdashboardkubernetesauditlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_operational_bar

Get the operation data dashboard for the given kubernetesClusterId

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

req = operations.GetDashboardOperationalBarRequest(
    clusters_ids=[
        '22554b3a-d14f-42dc-b8d0-c3530e8f8d65',
    ],
)

res = s.dashboard.get_dashboard_operational_bar(req)

if res.operational_bar is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetDashboardOperationalBarRequest](../../models/operations/getdashboardoperationalbarrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetDashboardOperationalBarResponse](../../models/operations/getdashboardoperationalbarresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_permissions

Get permissions dashboard data for the given kubernetesClusterIds

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

req = operations.GetDashboardPermissionsRequest(
    clusters_ids=[
        '5a331cfa-e207-49d9-a176-e260318ece7d',
    ],
)

res = s.dashboard.get_dashboard_permissions(req)

if res.permissions_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetDashboardPermissionsRequest](../../models/operations/getdashboardpermissionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetDashboardPermissionsResponse](../../models/operations/getdashboardpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_pod_telemetries

Get pod telemetries dashboard data for all clusters

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


res = s.dashboard.get_dashboard_pod_telemetries()

if res.time_based_widget is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardPodTelemetriesResponse](../../models/operations/getdashboardpodtelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_report_download

Download Secure Application security report

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


res = s.dashboard.get_dashboard_report_download()

if res.stream is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardReportDownloadResponse](../../models/operations/getdashboardreportdownloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_report_status

Get Secure Application report security status

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


res = s.dashboard.get_dashboard_report_status()

if res.report_status is not None:
    # handle response
    pass
```


### Response

**[operations.GetDashboardReportStatusResponse](../../models/operations/getdashboardreportstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_security_context

Get security context dashboard data for all clusters

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

req = operations.GetDashboardSecurityContextRequest(
    clusters_ids=[
        '238f2259-a31a-4eed-8f78-79faf6121c42',
    ],
)

res = s.dashboard.get_dashboard_security_context(req)

if res.security_context_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetDashboardSecurityContextRequest](../../models/operations/getdashboardsecuritycontextrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetDashboardSecurityContextResponse](../../models/operations/getdashboardsecuritycontextresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_top_security_risks

Get the top risky deployments dashboard data for the given kubernetesClusterIds

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

req = operations.GetDashboardTopSecurityRisksRequest(
    clusters_ids=[
        'e552767e-0350-4925-b7e4-39731700805c',
    ],
)

res = s.dashboard.get_dashboard_top_security_risks(req)

if res.top_security_risks_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetDashboardTopSecurityRisksRequest](../../models/operations/getdashboardtopsecurityrisksrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetDashboardTopSecurityRisksResponse](../../models/operations/getdashboardtopsecurityrisksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_vulnerabilities

Get vulnerabilities dashboard data for the given kubernetesClusterId

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

req = operations.GetDashboardVulnerabilitiesRequest(
    clusters_ids=[
        'f32607b3-fc0f-4f77-9432-186ec778c011',
    ],
)

res = s.dashboard.get_dashboard_vulnerabilities(req)

if res.vulnerabilities_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetDashboardVulnerabilitiesRequest](../../models/operations/getdashboardvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetDashboardVulnerabilitiesResponse](../../models/operations/getdashboardvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_kubernetes_cluster_id_connection_telemetries

Get connection telemetries dashboard data for the given kubernetesClusterId

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

req = operations.GetDashboardKubernetesClusterIDConnectionTelemetriesRequest(
    kubernetes_cluster_id='fcc6ab38-d1d9-486d-93c4-52d73dc4b7aa',
)

res = s.dashboard.get_dashboard_kubernetes_cluster_id_connection_telemetries(req)

if res.time_based_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.GetDashboardKubernetesClusterIDConnectionTelemetriesRequest](../../models/operations/getdashboardkubernetesclusteridconnectiontelemetriesrequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |


### Response

**[operations.GetDashboardKubernetesClusterIDConnectionTelemetriesResponse](../../models/operations/getdashboardkubernetesclusteridconnectiontelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs

Get kubernetes audit logs dashboard data for the given kubernetesClusterId

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

req = operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsRequest(
    kubernetes_cluster_id='6f0ce2c1-9ce6-424f-84d6-ad78557fec29',
)

res = s.dashboard.get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs(req)

if res.time_based_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsRequest](../../models/operations/getdashboardkubernetesclusteridkubernetesauditlogsrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsResponse](../../models/operations/getdashboardkubernetesclusteridkubernetesauditlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_dashboard_kubernetes_cluster_id_pod_telemetries

Get pod telemetries dashboard data for the given kubernetesClusterId

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

req = operations.GetDashboardKubernetesClusterIDPodTelemetriesRequest(
    kubernetes_cluster_id='6c0046f1-672f-410e-9032-dde3c7f70879',
)

res = s.dashboard.get_dashboard_kubernetes_cluster_id_pod_telemetries(req)

if res.time_based_widget is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetDashboardKubernetesClusterIDPodTelemetriesRequest](../../models/operations/getdashboardkubernetesclusteridpodtelemetriesrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetDashboardKubernetesClusterIDPodTelemetriesResponse](../../models/operations/getdashboardkubernetesclusteridpodtelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_licensing_dashboard

Get licensing dashboard data

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


res = s.dashboard.get_licensing_dashboard()

if res.licensing_dashboard is not None:
    # handle response
    pass
```


### Response

**[operations.GetLicensingDashboardResponse](../../models/operations/getlicensingdashboardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_dashboard_report_generate

Generate Secure Application security report

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


res = s.dashboard.post_dashboard_report_generate()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostDashboardReportGenerateResponse](../../models/operations/postdashboardreportgenerateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
