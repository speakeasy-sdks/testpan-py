# Envs
(*envs*)

## Overview

APIs used to define environments

### Available Operations

* [delete_environments_env_id_](#delete_environments_env_id_)
* [get_environments](#get_environments) - List all defined Secure Application environments
* [get_environments_env_id_](#get_environments_env_id_) - get a Secure Application environment
* [get_environments_env_id_delete_dependencies](#get_environments_env_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified environment
* [post_environments](#post_environments) - Add a new environment
* [post_environments_batch](#post_environments_batch) - Add a number of  Secure Application environments
* [post_environments_delete](#post_environments_delete) - Delete multiple Secure Application environments
* [put_environments_env_id_](#put_environments_env_id_) - Edit an existing Secure Application environment

## delete_environments_env_id_

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteEnvironmentsEnvIDRequest(
    env_id='b0aabb9f-e7ee-44ba-ba12-8ad45974b0df',
)

res = s.envs.delete_environments_env_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteEnvironmentsEnvIDRequest](../../models/operations/deleteenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteEnvironmentsEnvIDResponse](../../models/operations/deleteenvironmentsenvidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_environments

List all defined Secure Application environments

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetEnvironmentsRequest()

res = s.envs.get_environments(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetEnvironmentsRequest](../../models/operations/getenvironmentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetEnvironmentsResponse](../../models/operations/getenvironmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_environments_env_id_

get a Secure Application environment

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetEnvironmentsEnvIDRequest(
    env_id='559017e3-f060-4096-aa0f-bf777791d889',
)

res = s.envs.get_environments_env_id_(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetEnvironmentsEnvIDRequest](../../models/operations/getenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetEnvironmentsEnvIDResponse](../../models/operations/getenvironmentsenvidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_environments_env_id_delete_dependencies

get dependencies which need to be handled in order to delete specified environment

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetEnvironmentsEnvIDDeleteDependenciesRequest(
    env_id='28b60297-9556-4e6f-93e6-0cc1c215a603',
)

res = s.envs.get_environments_env_id_delete_dependencies(req)

if res.delete_dependency_element_environments is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetEnvironmentsEnvIDDeleteDependenciesRequest](../../models/operations/getenvironmentsenviddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetEnvironmentsEnvIDDeleteDependenciesResponse](../../models/operations/getenvironmentsenviddeletedependenciesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_environments

Add a  Secure Application environment. An instance should be contained in a single environment. The environment is defined by a VPC and an optional tag. If a tag is supplied, only instances in the specified VPC with the given tag will belong to the new environment.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.EnvironmentInput(
    name='Prod',
)

res = s.envs.post_environments(req)

if res.environment is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.EnvironmentInput](../../models/shared/environmentinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostEnvironmentsResponse](../../models/operations/postenvironmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_environments_batch

Add a number of new Secure Application environments. This is similar to the 'Add environment' method, but for multiple environments.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = [
    shared.EnvironmentInput(
        name='Prod',
    ),
]

res = s.envs.post_environments_batch(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                         | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `request`                                         | [List[shared.EnvironmentInput]](../../models/.md) | :heavy_check_mark:                                | The request object to use for the request.        |


### Response

**[operations.PostEnvironmentsBatchResponse](../../models/operations/postenvironmentsbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_environments_delete

Delete multiple Secure Application environments.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.envs.post_environments_delete()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.PostEnvironmentsDeleteResponse](../../models/operations/postenvironmentsdeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_environments_env_id_

Edit an existing Secure Application environment.


### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutEnvironmentsEnvIDRequest(
    environment=shared.EnvironmentInput(
        name='Prod',
    ),
    env_id='57cf89fe-5e65-409c-b415-d6003566df6f',
)

res = s.envs.put_environments_env_id_(req)

if res.environment is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutEnvironmentsEnvIDRequest](../../models/operations/putenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutEnvironmentsEnvIDResponse](../../models/operations/putenvironmentsenvidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
