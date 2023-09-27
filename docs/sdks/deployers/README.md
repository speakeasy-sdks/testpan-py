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
    deployer_id='f334cddf-857a-49e6-9876-c6ab21d29dfc',
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
    max_results=6018.03,
    name='Mable Hodkiewicz',
    offset=7874.52,
    rule_creation=False,
    security_check=False,
    sort_dir=operations.GetDeployersSortDir.DESC,
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
    kubernetes_cluster_id='99390066-a6d2-4d00-8355-338cec086fa2',
    namespace_name='veritatis',
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
    deployer_id='e9152cb3-1191-467b-8e3c-8db03408d6d3',
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
    deployer='voluptas',
    deployer_id='4ffd4559-06d1-4263-948e-935c2c9e81f3',
    deployer_type=shared.DeployerDeployerType.OPERATOR_DEPLOYER,
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
        deployer='soluta',
        deployer_id='e3e43202-d721-4657-a506-641870d9d21f',
        deployer_type=shared.DeployerDeployerType.SECURE_CN_DEPLOYER,
    ),
    deployer_id='ad030c4e-cc11-4a08-b642-9068b8502a55',
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

