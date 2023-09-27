# Gateways
(*gateways*)

### Available Operations

* [delete_gateways_gateway_id_](#delete_gateways_gateway_id_) - Delete gateway
* [get_gateways](#get_gateways) - Get gateways
* [get_gateways_clusters](#get_gateways_clusters) - Get clusters info
* [get_gateways_gateway_id_download_bundle](#get_gateways_gateway_id_download_bundle) - Get a GW installation script
* [post_gateways](#post_gateways) - Add new gateway
* [put_gateways_gateway_id_](#put_gateways_gateway_id_) - Edit gateway

## delete_gateways_gateway_id_

Delete gateway

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

req = operations.DeleteGatewaysGatewayIDRequest(
    gateway_id='f443b425-7b99-42c8-9bda-6a61efa21982',
)

res = s.gateways.delete_gateways_gateway_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteGatewaysGatewayIDRequest](../../models/operations/deletegatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteGatewaysGatewayIDResponse](../../models/operations/deletegatewaysgatewayidresponse.md)**


## get_gateways

Get gateways

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

req = operations.GetGatewaysRequest(
    max_results=3560.07,
    name='Miss Santos Stroman',
    no_pagination=False,
    offset=9085.87,
    sort_dir=operations.GetGatewaysSortDir.DESC,
)

res = s.gateways.get_gateways(req)

if res.gateways is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetGatewaysRequest](../../models/operations/getgatewaysrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetGatewaysResponse](../../models/operations/getgatewaysresponse.md)**


## get_gateways_clusters

Get clusters info

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

req = operations.GetGatewaysClustersRequest(
    gateway_type=operations.GetGatewaysClustersGatewayType.TYK_INTERNAL,
)

res = s.gateways.get_gateways_clusters(req)

if res.gateway_cluster_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGatewaysClustersRequest](../../models/operations/getgatewaysclustersrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetGatewaysClustersResponse](../../models/operations/getgatewaysclustersresponse.md)**


## get_gateways_gateway_id_download_bundle

In order to install,  extract and run "./install_bundle.sh"

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

req = operations.GetGatewaysGatewayIDDownloadBundleRequest(
    gateway_id='47f7d3ef-0496-440d-aa18-31c87adf596f',
)

res = s.gateways.get_gateways_gateway_id_download_bundle(req)

if res.get_gateways_gateway_id_download_bundle_200_application_json_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetGatewaysGatewayIDDownloadBundleRequest](../../models/operations/getgatewaysgatewayiddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetGatewaysGatewayIDDownloadBundleResponse](../../models/operations/getgatewaysgatewayiddownloadbundleresponse.md)**


## post_gateways

Add new gateway

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

req = shared.Gateway(
    cluster_name='repellendus',
    description='delectus',
    id='1ad837ae-80c1-4c19-895b-a998678fa3f6',
    name='Milton Morar MD',
    type=shared.GatewayType.F5_BIG_IP,
)

res = s.gateways.post_gateways(req)

if res.gateway is not None:
    # handle response
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [shared.Gateway](../../models/shared/gateway.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.PostGatewaysResponse](../../models/operations/postgatewaysresponse.md)**


## put_gateways_gateway_id_

Edit gateway

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

req = operations.PutGatewaysGatewayIDRequest(
    gateway=shared.Gateway(
        cluster_name='dolor',
        description='voluptatum',
        id='8ce03614-448c-4797-ba0e-f2f536028efe',
        name='Edmond McDermott',
        type=shared.GatewayType.APIGEE_X,
    ),
    gateway_id='52ed7e25-3f4c-4157-9eaa-7170f445accf',
)

res = s.gateways.put_gateways_gateway_id_(req)

if res.gateway is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutGatewaysGatewayIDRequest](../../models/operations/putgatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutGatewaysGatewayIDResponse](../../models/operations/putgatewaysgatewayidresponse.md)**

