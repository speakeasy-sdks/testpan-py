# Deployers
(*deployers*)

## Overview

APIs used to manage deployers on Secure Application

### Available Operations

* [delete_deployers_deployer_id_](#delete_deployers_deployer_id_) - Delete an deployer
* [get_deployers](#get_deployers) - List all the deployers on the system
* [get_deployers_service_accounts](#get_deployers_service_accounts) - List all the service account on the system
* [get_deployers_deployer_id_delete_dependencies](#get_deployers_deployer_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified deployer
* [post_deployers](#post_deployers) - Create a new deployer
* [put_deployers_deployer_id_](#put_deployers_deployer_id_) - Edit deployer definition

## delete_deployers_deployer_id_

Delete an deployer

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

req = operations.DeleteDeployersDeployerIDRequest(
    deployer_id='3dadebf3-f849-4db8-9b45-692d5d0f8f1e',
)

res = s.deployers.delete_deployers_deployer_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteDeployersDeployerIDRequest](../../models/operations/deletedeployersdeployeridrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DeleteDeployersDeployerIDResponse](../../models/operations/deletedeployersdeployeridresponse.md)**


## get_deployers

List all the deployers on the system

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

req = operations.GetDeployersRequest(
    sort_key=operations.GetDeployersSortKey.DEPLOYER,
)

res = s.deployers.get_deployers(req)

if res.deployers is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetDeployersRequest](../../models/operations/getdeployersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetDeployersResponse](../../models/operations/getdeployersresponse.md)**


## get_deployers_service_accounts

List all the service account on the system

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

req = operations.GetDeployersServiceAccountsRequest(
    kubernetes_cluster_id='2cec5765-5bfd-4372-88d6-c69c1df0fe41',
)

res = s.deployers.get_deployers_service_accounts(req)

if res.service_account_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetDeployersServiceAccountsRequest](../../models/operations/getdeployersserviceaccountsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetDeployersServiceAccountsResponse](../../models/operations/getdeployersserviceaccountsresponse.md)**


## get_deployers_deployer_id_delete_dependencies

get dependencies which need to be handled in order to delete specified deployer

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

req = operations.GetDeployersDeployerIDDeleteDependenciesRequest(
    deployer_id='e9516b93-3d3f-40df-8a57-7f05ddcfb304',
)

res = s.deployers.get_deployers_deployer_id_delete_dependencies(req)

if res.deployer_delete_dependencies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.GetDeployersDeployerIDDeleteDependenciesRequest](../../models/operations/getdeployersdeployeriddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.GetDeployersDeployerIDDeleteDependenciesResponse](../../models/operations/getdeployersdeployeriddeletedependenciesresponse.md)**


## post_deployers

Create a new deployer

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

req = shared.DeployerInput(
    deployer_id='589c2d6b-f948-4feb-95d2-afb538f00cdb',
    deployer_type=shared.DeployerDeployerType.SECURE_CN_DEPLOYER,
)

res = s.deployers.post_deployers(req)

if res.deployer is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.DeployerInput](../../models/shared/deployerinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostDeployersResponse](../../models/operations/postdeployersresponse.md)**


## put_deployers_deployer_id_

Edit deployer definition

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

req = operations.PutDeployersDeployerIDRequest(
    deployer_input=shared.DeployerInput(
        deployer_id='bfd0fb57-ae2a-4efa-9ee4-175ba71bdf48',
        deployer_type=shared.DeployerDeployerType.OPERATOR_DEPLOYER,
    ),
    deployer_id='87529aca-1222-401f-98e6-927bec6fe116',
)

res = s.deployers.put_deployers_deployer_id_(req)

if res.deployer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutDeployersDeployerIDRequest](../../models/operations/putdeployersdeployeridrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PutDeployersDeployerIDResponse](../../models/operations/putdeployersdeployeridresponse.md)**

