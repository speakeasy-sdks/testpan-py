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
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppTelemetriesRequest(
    end_time=dateutil.parser.isoparse('2024-07-22T12:37:40.720Z'),
    sort_key=operations.GetAppTelemetriesQueryParamSortKey.ENVIRONMENT_NAME,
    start_time=dateutil.parser.isoparse('2022-02-25T06:07:38.033Z'),
)

res = s.telemetries.get_app_telemetries(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAppTelemetriesRequest](../../models/operations/getapptelemetriesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetAppTelemetriesResponse](../../models/operations/getapptelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_app_telemetries_app_telemetry_id_

Get App telemetry by ID

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_app_telemetries_app_telemetry_id_api_risk_info

Get API risks info of given app telemetry

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest(
    app_telemetry_id='6f98b895-9ca6-43b1-9526-7f6ebacd6bab',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_api_risk_info(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest](../../models/operations/getapptelemetriesapptelemetryidapiriskinforequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoResponse](../../models/operations/getapptelemetriesapptelemetryidapiriskinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_app_telemetries_app_telemetry_id_image_packages

list packages with licenses runnin on a pod

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest(
    app_telemetry_id='4668441f-326c-4b1d-9b80-38c3aa5ff203',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_image_packages(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest](../../models/operations/getapptelemetriesapptelemetryidimagepackagesrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDImagePackagesResponse](../../models/operations/getapptelemetriesapptelemetryidimagepackagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_app_telemetries_app_telemetry_id_injection_info

Get token injection info of given app telemetry

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest(
    app_telemetry_id='e9382bba-032c-4379-a173-a7671d6d9a49',
)

res = s.telemetries.get_app_telemetries_app_telemetry_id_injection_info(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest](../../models/operations/getapptelemetriesapptelemetryidinjectioninforequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetAppTelemetriesAppTelemetryIDInjectionInfoResponse](../../models/operations/getapptelemetriesapptelemetryidinjectioninforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_connection_telemetries

Get connection telemetries

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetConnectionTelemetriesRequest(
    end_time=dateutil.parser.isoparse('2024-12-02T06:08:07.741Z'),
    sort_key=operations.GetConnectionTelemetriesQueryParamSortKey.TARGET_RISK,
    start_time=dateutil.parser.isoparse('2022-04-30T20:32:05.208Z'),
)

res = s.telemetries.get_connection_telemetries(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetConnectionTelemetriesRequest](../../models/operations/getconnectiontelemetriesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetConnectionTelemetriesResponse](../../models/operations/getconnectiontelemetriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_connection_telemetries_connection_telemetry_id_

get details for a single connection telemetry

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetConnectionTelemetriesConnectionTelemetryIDRequest(
    connection_telemetry_id='726acf07-d01e-4a6d-9948-64b67b807f65',
    end_time=dateutil.parser.isoparse('2022-06-17T13:01:05.521Z'),
    start_time=dateutil.parser.isoparse('2024-04-26T08:25:39.198Z'),
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
