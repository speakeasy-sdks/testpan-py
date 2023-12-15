# Mitre
(*mitre*)

### Available Operations

* [get_mitre_dashboard](#get_mitre_dashboard) - Get data for MITRE dashboard for all clusters
* [get_mitre_report_download](#get_mitre_report_download) - Download Mitre security report
* [get_mitre_report_status](#get_mitre_report_status) - Get Mitre report status
* [get_mitre_technique](#get_mitre_technique) - Get data for MITRE technique of the given mitreTechniqueType
* [post_mitre_report_generate](#post_mitre_report_generate) - Generate Mitre report
* [post_mitre_technique_fix](#post_mitre_technique_fix) - Post fix for MITRE technique of the given mitreTechniqueType

## get_mitre_dashboard

Get data for MITRE dashboard for all clusters

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetMitreDashboardRequest(
    clusters_ids=[
        'a91a8587-5ae9-468d-bcc5-575f0642f99f',
    ],
)

res = s.mitre.get_mitre_dashboard(req)

if res.mitre_dashboard is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMitreDashboardRequest](../../models/operations/getmitredashboardrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetMitreDashboardResponse](../../models/operations/getmitredashboardresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_mitre_report_download

Download Mitre security report

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.mitre.get_mitre_report_download()

if res.stream is not None:
    # handle response
    pass
```


### Response

**[operations.GetMitreReportDownloadResponse](../../models/operations/getmitrereportdownloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_mitre_report_status

Get Mitre report status

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.mitre.get_mitre_report_status()

if res.report_status is not None:
    # handle response
    pass
```


### Response

**[operations.GetMitreReportStatusResponse](../../models/operations/getmitrereportstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_mitre_technique

Get data for MITRE technique of the given mitreTechniqueType

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetMitreTechniqueRequest(
    clusters_ids=[
        '15c243dc-adda-4d62-b64a-acf9b6fc450a',
    ],
    mitre_technique_type=operations.MitreTechniqueType.DEPLOY_CONTAINER,
)

res = s.mitre.get_mitre_technique(req)

if res.mitre_technique_info is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMitreTechniqueRequest](../../models/operations/getmitretechniquerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetMitreTechniqueResponse](../../models/operations/getmitretechniqueresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_mitre_report_generate

Generate Mitre report

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.mitre.post_mitre_report_generate()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostMitreReportGenerateResponse](../../models/operations/postmitrereportgenerateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_mitre_technique_fix

Post fix for MITRE technique of the given mitreTechniqueType

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostMitreTechniqueFixRequest(
    mitre_technique_fix_info=shared.MitreTechniqueFixInfo(
        affected_elements=[
            shared.MitreTechniqueAffectedElement(),
        ],
    ),
    clusters_ids=[
        '684b4b2c-63c2-4f7d-9896-83947da0e326',
    ],
    mitre_technique_type=operations.QueryParamMitreTechniqueType.CLEAR_K8_S_EVENTS,
)

res = s.mitre.post_mitre_technique_fix(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PostMitreTechniqueFixRequest](../../models/operations/postmitretechniquefixrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PostMitreTechniqueFixResponse](../../models/operations/postmitretechniquefixresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
