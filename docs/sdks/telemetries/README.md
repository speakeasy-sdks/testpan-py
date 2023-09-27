# Telemetries
(*telemetries*)

## Overview

APIs used to query for telemetries

### Available Operations

* [get_app_telemetries](#get_app_telemetries) - Get App telemetries
* [get_app_telemetries_app_telemetry_id_](#get_app_telemetries_app_telemetry_id_) - Get App telemetry by ID
* [get_app_telemetries_app_telemetry_id_api_risk_info](#get_app_telemetries_app_telemetry_id_api_risk_info) - Get API risks info of given app telemetry
* [get_app_telemetries_app_telemetry_id_image_packages](#get_app_telemetries_app_telemetry_id_image_packages) - list packages with licenses runnin on a pod
* [get_app_telemetries_app_telemetry_id_injection_info](#get_app_telemetries_app_telemetry_id_injection_info) - Get token injection info of given app telemetry
* [get_connection_telemetries](#get_connection_telemetries) - Get connection telemetries
* [get_connection_telemetries_connection_telemetry_id_](#get_connection_telemetries_connection_telemetry_id_) - get details for a single connection telemetry

## get_app_telemetries

Get App telemetries

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAppTelemetriesRequest(
    app_name=[
        'unde',
    ],
    app_type=[
        'impedit',
    ],
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2022-10-29T03:20:48.266Z'),
    environment_name=[
        'commodi',
    ],
    executable=[
        'neque',
    ],
    hide_internals=False,
    highest_dockerfile_scan_result=[
        'enim',
    ],
    host=[
        'eaque',
    ],
    images_id=[
        'a4671437-89ce-40e9-9159-4d93a74c0252',
    ],
    is_identified=False,
    max_results=9545.42,
    namespaces_filter='saepe',
    offset=2245.48,
    protection_status=operations.GetAppTelemetriesProtectionStatus.DISABLED,
    result=[
        operations.GetAppTelemetriesResult.ALLOW,
    ],
    show_only_entries_with_app_name=False,
    show_only_violations=False,
    show_system_pods=False,
    sort_dir=operations.GetAppTelemetriesSortDir.DESC,
    sort_key=operations.GetAppTelemetriesSortKey.EXECUTABLE,
    start_time=dateutil.parser.isoparse('2020-11-24T00:05:53.510Z'),
    status=[
        'atque',
    ],
    vulnerability_levels_filter=[
        'tempore',
    ],
    workload_risks=[
        operations.GetAppTelemetriesWorkloadRisks.MEDIUM,
    ],
)

res = s.telemetries.get_app_telemetries(req)

if res.app_telemetries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAppTelemetriesRequest](../../models/operations/getapptelemetriesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetAppTelemetriesResponse](../../models/operations/getapptelemetriesresponse.md)**


## get_app_telemetries_app_telemetry_id_

Get App telemetry by ID

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

req = operations.GetAppTelemetriesAppTelemetryIDRequest(
    app_telemetry_id='78ebb6e1-d2cf-4502-bafb-2cbc4635d5e6',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_(req)

if res.app_telemetry is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetAppTelemetriesAppTelemetryIDRequest](../../models/operations/getapptelemetriesapptelemetryidrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDResponse](../../models/operations/getapptelemetriesapptelemetryidresponse.md)**


## get_app_telemetries_app_telemetry_id_api_risk_info

Get API risks info of given app telemetry

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

req = operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest(
    app_telemetry_id='5da028c3-e951-4a1e-b0fd-a966489d7b78',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_api_risk_info(req)

if res.api_risk_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest](../../models/operations/getapptelemetriesapptelemetryidapiriskinforequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoResponse](../../models/operations/getapptelemetriesapptelemetryidapiriskinforesponse.md)**


## get_app_telemetries_app_telemetry_id_image_packages

list packages with licenses runnin on a pod

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

req = operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest(
    app_telemetry_id='673e13a1-2a6b-4992-8945-94487f5c8438',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_image_packages(req)

if res.images_with_licenses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest](../../models/operations/getapptelemetriesapptelemetryidimagepackagesrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDImagePackagesResponse](../../models/operations/getapptelemetriesapptelemetryidimagepackagesresponse.md)**


## get_app_telemetries_app_telemetry_id_injection_info

Get token injection info of given app telemetry

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

req = operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest(
    app_telemetry_id='36b86b3c-df64-415b-8449-f9df13f4eedb',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_injection_info(req)

if res.token_injection_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest](../../models/operations/getapptelemetriesapptelemetryidinjectioninforequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDInjectionInfoResponse](../../models/operations/getapptelemetriesapptelemetryidinjectioninforesponse.md)**


## get_connection_telemetries

Get connection telemetries

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetConnectionTelemetriesRequest(
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2021-08-26T23:34:52.732Z'),
    logical_operator=operations.GetConnectionTelemetriesLogicalOperator.OR,
    max_results=7347.74,
    offset=9709.57,
    result=[
        operations.GetConnectionTelemetriesResult.BLOCK,
    ],
    show_only_violations=False,
    sort_dir=operations.GetConnectionTelemetriesSortDir.ASC,
    sort_key=operations.GetConnectionTelemetriesSortKey.TARGET_APP_NAME,
    source_app_name=[
        'molestias',
    ],
    source_environment_name=[
        'quia',
    ],
    source_executable=[
        'ipsam',
    ],
    source_host_name=[
        'rem',
    ],
    source_namespaces_filter='molestias',
    source_risk=[
        operations.GetConnectionTelemetriesSourceRisk.HIGH,
    ],
    start_time=dateutil.parser.isoparse('2021-02-06T05:09:51.787Z'),
    target_app_name=[
        'in',
    ],
    target_environment_name=[
        'aliquid',
    ],
    target_executable=[
        'amet',
    ],
    target_host_name=[
        'fugiat',
    ],
    target_namespaces_filter='corporis',
    target_risk=[
        operations.GetConnectionTelemetriesTargetRisk.LOW,
    ],
)

res = s.telemetries.get_connection_telemetries(req)

if res.connection_telemetries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetConnectionTelemetriesRequest](../../models/operations/getconnectiontelemetriesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetConnectionTelemetriesResponse](../../models/operations/getconnectiontelemetriesresponse.md)**


## get_connection_telemetries_connection_telemetry_id_

get details for a single connection telemetry

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetConnectionTelemetriesConnectionTelemetryIDRequest(
    connection_telemetry_id='72795b78-5148-4d6d-949e-5635b33bc0f9',
    end_time=dateutil.parser.isoparse('2022-12-21T18:54:05.127Z'),
    start_time=dateutil.parser.isoparse('2022-02-14T21:38:08.583Z'),
)

res = s.telemetries.get_connection_telemetries_connection_telemetry_id_(req)

if res.connection_telemetry is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetConnectionTelemetriesConnectionTelemetryIDRequest](../../models/operations/getconnectiontelemetriesconnectiontelemetryidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetConnectionTelemetriesConnectionTelemetryIDResponse](../../models/operations/getconnectiontelemetriesconnectiontelemetryidresponse.md)**

