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
    gateway_id='0059ee9e-2eb4-40ca-97cc-9e2e4879b4b7',
)

res = s.gateways.delete_gateways_gateway_id_(req)

if res.status_code == 200:
    # handle response
    pass
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

req = operations.GetGatewaysRequest()

res = s.gateways.get_gateways(req)

if res.gateways is not None:
    # handle response
    pass
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
    pass
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
    gateway_id='d7df551a-98f0-4f5b-9bdc-d69676cf90f0',
)

res = s.gateways.get_gateways_gateway_id_download_bundle(req)

if res.get_gateways_gateway_id_download_bundle_200_application_json_binary_string is not None:
    # handle response
    pass
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
    cluster_name='string',
    name='string',
    type=shared.GatewayType.APIGEE_X,
)

res = s.gateways.post_gateways(req)

if res.gateway is not None:
    # handle response
    pass
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
        cluster_name='string',
        name='string',
        type=shared.GatewayType.F5_BIG_IP,
    ),
    gateway_id='b1d9c87e-1369-4f02-8e6c-75779c9c8e93',
)

res = s.gateways.put_gateways_gateway_id_(req)

if res.gateway is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutGatewaysGatewayIDRequest](../../models/operations/putgatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutGatewaysGatewayIDResponse](../../models/operations/putgatewaysgatewayidresponse.md)**

