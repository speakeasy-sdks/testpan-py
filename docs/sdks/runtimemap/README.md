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
        password="",
        username="",
    ),
)

req = operations.DeleteNetworkMapQueueRequestIDRequest(
    request_id='7d2a9c87-ae50-4c16-a61a-1d9136a7e8d5',
)

res = s.runtime_map.delete_network_map_queue_request_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteNetworkMapQueueRequestIDRequest](../../models/operations/deletenetworkmapqueuerequestidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteNetworkMapQueueRequestIDResponse](../../models/operations/deletenetworkmapqueuerequestidresponse.md)**


## get_network_map

Get data for network map

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

req = operations.GetNetworkMapRequest(
    api_risk=operations.GetNetworkMapAPIRisk.MEDIUM,
    apps=[
        'qui',
    ],
    end_time=dateutil.parser.isoparse('2022-10-09T14:23:43.307Z'),
    environments=[
        'tenetur',
    ],
    exclude_apps=[
        'velit',
    ],
    group_apps_on_the_same_environment=False,
    ignore_external_connection=False,
    is_background_job=False,
    labels=[
        'asperiores',
    ],
    namespaces=[
        '658752db-764c-459f-8a56-cebcada29ca7',
    ],
    show_only_apps_with_connections=False,
    show_only_apps_with_violations=False,
    show_only_connections_between_environments=False,
    show_only_connections_with_violations=False,
    start_time=dateutil.parser.isoparse('2022-11-12T06:02:50.943Z'),
)

res = s.runtime_map.get_network_map(req)

if res.network_map is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNetworkMapRequest](../../models/operations/getnetworkmaprequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNetworkMapResponse](../../models/operations/getnetworkmapresponse.md)**


## get_network_map_queue_request_id_

Get status for network map background job

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

req = operations.GetNetworkMapQueueRequestIDRequest(
    request_id='81c95671-663c-4530-b566-5163a3638512',
)

res = s.runtime_map.get_network_map_queue_request_id_(req)

if res.background_job_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetNetworkMapQueueRequestIDRequest](../../models/operations/getnetworkmapqueuerequestidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetNetworkMapQueueRequestIDResponse](../../models/operations/getnetworkmapqueuerequestidresponse.md)**


## get_network_map_results_request_id_

Get result for network map background job

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

req = operations.GetNetworkMapResultsRequestIDRequest(
    request_id='ab2521b9-f2e0-4724-a7b8-a40bc05fab0d',
)

res = s.runtime_map.get_network_map_results_request_id_(req)

if res.network_maps is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetNetworkMapResultsRequestIDRequest](../../models/operations/getnetworkmapresultsrequestidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetNetworkMapResultsRequestIDResponse](../../models/operations/getnetworkmapresultsrequestidresponse.md)**

