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
    request_id='d744d9fc-99bf-4fa7-bd43-977bd77decee',
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
    api_risk=operations.GetNetworkMapAPIRisk.NEUTRAL,
    apps=[
        'unto',
    ],
    end_time=dateutil.parser.isoparse('2022-07-01T23:29:00.212Z'),
    environments=[
        'Gasoline',
    ],
    exclude_apps=[
        'West',
    ],
    group_apps_on_the_same_environment=False,
    ignore_external_connection=False,
    is_background_job=False,
    labels=[
        'thoughtfully',
    ],
    namespaces=[
        '770727e0-bc8a-4727-a6cf-78080c58f4e0',
    ],
    show_only_apps_with_connections=False,
    show_only_apps_with_violations=False,
    show_only_connections_between_environments=False,
    show_only_connections_with_violations=False,
    start_time=dateutil.parser.isoparse('2021-06-22T19:37:42.851Z'),
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
    request_id='3d22620c-025b-41f7-b070-9e069dc87bfd',
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
    request_id='78c61cf8-31c2-407a-a949-4700ad100770',
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

