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
        password="",
        username="",
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
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMitreDashboardRequest](../../models/operations/getmitredashboardrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetMitreDashboardResponse](../../models/operations/getmitredashboardresponse.md)**


## get_mitre_report_download

Download Mitre security report

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


res = s.mitre.get_mitre_report_download()

if res.get_mitre_report_download_200_application_json_binary_string is not None:
    # handle response
```


### Response

**[operations.GetMitreReportDownloadResponse](../../models/operations/getmitrereportdownloadresponse.md)**


## get_mitre_report_status

Get Mitre report status

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


res = s.mitre.get_mitre_report_status()

if res.report_status is not None:
    # handle response
```


### Response

**[operations.GetMitreReportStatusResponse](../../models/operations/getmitrereportstatusresponse.md)**


## get_mitre_technique

Get data for MITRE technique of the given mitreTechniqueType

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

req = operations.GetMitreTechniqueRequest(
    clusters_ids=[
        '15c243dc-adda-4d62-b64a-acf9b6fc450a',
    ],
    mitre_technique_type=operations.GetMitreTechniqueMitreTechniqueType.DEPLOY_CONTAINER,
)

res = s.mitre.get_mitre_technique(req)

if res.mitre_technique_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMitreTechniqueRequest](../../models/operations/getmitretechniquerequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetMitreTechniqueResponse](../../models/operations/getmitretechniqueresponse.md)**


## post_mitre_report_generate

Generate Mitre report

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


res = s.mitre.post_mitre_report_generate()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostMitreReportGenerateResponse](../../models/operations/postmitrereportgenerateresponse.md)**


## post_mitre_technique_fix

Post fix for MITRE technique of the given mitreTechniqueType

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

req = operations.PostMitreTechniqueFixRequest(
    mitre_technique_fix_info=shared.MitreTechniqueFixInfo(
        affected_elements=[
            shared.MitreTechniqueAffectedElement(
                mitre_technique_affected_element_type=shared.MitreTechniqueAffectedElementMitreTechniqueAffectedElementType.MITRE_TECHNIQUE_AFFECTED_WORKLOAD,
            ),
        ],
    ),
    clusters_ids=[
        '84b4b2c6-3c2f-47d9-8968-3947da0e326b',
    ],
    mitre_technique_type=operations.PostMitreTechniqueFixMitreTechniqueType.ACCESS_CLUSTER_RESOURCES,
)

res = s.mitre.post_mitre_technique_fix(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PostMitreTechniqueFixRequest](../../models/operations/postmitretechniquefixrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PostMitreTechniqueFixResponse](../../models/operations/postmitretechniquefixresponse.md)**

