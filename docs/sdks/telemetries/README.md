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
        'Crew',
    ],
    app_type=[
        'splendid',
    ],
    end_time=dateutil.parser.isoparse('2021-09-05T15:33:12.217Z'),
    environment_name=[
        'Syrian',
    ],
    executable=[
        'strategy',
    ],
    highest_dockerfile_scan_result=[
        'Concrete',
    ],
    host=[
        'killer',
    ],
    images_id=[
        'af356669-e30a-47df-8a5c-8c97d1dbbd64',
    ],
    result=[
        operations.GetAppTelemetriesResult.ALLOW,
    ],
    sort_key=operations.GetAppTelemetriesSortKey.APP_NAME,
    start_time=dateutil.parser.isoparse('2022-02-10T16:05:06.025Z'),
    status=[
        'auxiliary',
    ],
    vulnerability_levels_filter=[
        'Avon',
    ],
    workload_risks=[
        operations.GetAppTelemetriesWorkloadRisks.HIGH,
    ],
)

res = s.telemetries.get_app_telemetries(req)

if res.app_telemetries is not None:
    # handle response
    pass
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
    app_telemetry_id='6ebde0ec-647c-4eab-b779-88cc0a536506',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_(req)

if res.app_telemetry is not None:
    # handle response
    pass
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
    app_telemetry_id='6f98b895-9ca6-43b1-9526-7f6ebacd6bab',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_api_risk_info(req)

if res.api_risk_infos is not None:
    # handle response
    pass
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
    app_telemetry_id='4668441f-326c-4b1d-9b80-38c3aa5ff203',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_image_packages(req)

if res.images_with_licenses is not None:
    # handle response
    pass
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
    app_telemetry_id='e9382bba-032c-4379-a173-a7671d6d9a49',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_injection_info(req)

if res.token_injection_infos is not None:
    # handle response
    pass
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
    end_time=dateutil.parser.isoparse('2023-12-02T06:47:12.551Z'),
    result=[
        operations.GetConnectionTelemetriesResult.ALLOW,
    ],
    sort_key=operations.GetConnectionTelemetriesSortKey.SOURCE_APP_TYPE,
    source_app_name=[
        'because',
    ],
    source_environment_name=[
        'Cotton',
    ],
    source_executable=[
        'Hybrid',
    ],
    source_host_name=[
        'wireless',
    ],
    source_risk=[
        operations.GetConnectionTelemetriesSourceRisk.HIGH,
    ],
    start_time=dateutil.parser.isoparse('2023-12-19T20:37:58.933Z'),
    target_app_name=[
        'Moscovium',
    ],
    target_environment_name=[
        'Regional',
    ],
    target_executable=[
        'coddle',
    ],
    target_host_name=[
        'Hampshire',
    ],
    target_risk=[
        operations.GetConnectionTelemetriesTargetRisk.MEDIUM,
    ],
)

res = s.telemetries.get_connection_telemetries(req)

if res.connection_telemetries is not None:
    # handle response
    pass
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
    connection_telemetry_id='726acf07-d01e-4a6d-9948-64b67b807f65',
    end_time=dateutil.parser.isoparse('2021-06-17T09:20:57.797Z'),
    start_time=dateutil.parser.isoparse('2023-04-26T13:53:39.546Z'),
)

res = s.telemetries.get_connection_telemetries_connection_telemetry_id_(req)

if res.connection_telemetry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetConnectionTelemetriesConnectionTelemetryIDRequest](../../models/operations/getconnectiontelemetriesconnectiontelemetryidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetConnectionTelemetriesConnectionTelemetryIDResponse](../../models/operations/getconnectiontelemetriesconnectiontelemetryidresponse.md)**

