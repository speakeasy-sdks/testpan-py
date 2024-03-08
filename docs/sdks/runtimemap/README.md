# RuntimeMap
(*runtime_map*)

## Overview

APIs used to  query for network map

### Available Operations

* [delete_network_map_queue_request_id_](#delete_network_map_queue_request_id_) - Cancel the network map background job
* [get_network_map](#get_network_map) - Get data for network map
* [get_network_map_queue_request_id_](#get_network_map_queue_request_id_) - Get status for network map background job
* [get_network_map_results_request_id_](#get_network_map_results_request_id_) - Get result for network map background job

## delete_network_map_queue_request_id_

Cancel the network map background job

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteNetworkMapQueueRequestIDRequest(
    request_id='d744d9fc-99bf-4fa7-bd43-977bd77decee',
)

res = s.runtime_map.delete_network_map_queue_request_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteNetworkMapQueueRequestIDRequest](../../models/operations/deletenetworkmapqueuerequestidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteNetworkMapQueueRequestIDResponse](../../models/operations/deletenetworkmapqueuerequestidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_network_map

Get data for network map

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

req = operations.GetNetworkMapRequest(
    end_time=dateutil.parser.isoparse('2024-01-08T06:16:22.888Z'),
    start_time=dateutil.parser.isoparse('2024-11-30T21:38:21.961Z'),
)

res = s.runtime_map.get_network_map(req)

if res.network_map is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNetworkMapRequest](../../models/operations/getnetworkmaprequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNetworkMapResponse](../../models/operations/getnetworkmapresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_network_map_queue_request_id_

Get status for network map background job

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetNetworkMapQueueRequestIDRequest(
    request_id='3d22620c-025b-41f7-b070-9e069dc87bfd',
)

res = s.runtime_map.get_network_map_queue_request_id_(req)

if res.background_job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetNetworkMapQueueRequestIDRequest](../../models/operations/getnetworkmapqueuerequestidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetNetworkMapQueueRequestIDResponse](../../models/operations/getnetworkmapqueuerequestidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_network_map_results_request_id_

Get result for network map background job

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetNetworkMapResultsRequestIDRequest(
    request_id='78c61cf8-31c2-407a-a949-4700ad100770',
)

res = s.runtime_map.get_network_map_results_request_id_(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetNetworkMapResultsRequestIDRequest](../../models/operations/getnetworkmapresultsrequestidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetNetworkMapResultsRequestIDResponse](../../models/operations/getnetworkmapresultsrequestidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
