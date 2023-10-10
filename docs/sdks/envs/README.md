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
        password="",
        username="",
    ),
)

req = operations.DeleteEnvironmentsEnvIDRequest(
    env_id='b0aabb9f-e7ee-44ba-ba12-8ad45974b0df',
)

res = s.envs.delete_environments_env_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteEnvironmentsEnvIDRequest](../../models/operations/deleteenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteEnvironmentsEnvIDResponse](../../models/operations/deleteenvironmentsenvidresponse.md)**


## get_environments

List all defined Secure Application environments

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

req = operations.GetEnvironmentsRequest()

res = s.envs.get_environments(req)

if res.environments is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetEnvironmentsRequest](../../models/operations/getenvironmentsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetEnvironmentsResponse](../../models/operations/getenvironmentsresponse.md)**


## get_environments_env_id_

get a Secure Application environment

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

req = operations.GetEnvironmentsEnvIDRequest(
    env_id='559017e3-f060-4096-aa0f-bf777791d889',
)

res = s.envs.get_environments_env_id_(req)

if res.environments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetEnvironmentsEnvIDRequest](../../models/operations/getenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetEnvironmentsEnvIDResponse](../../models/operations/getenvironmentsenvidresponse.md)**


## get_environments_env_id_delete_dependencies

get dependencies which need to be handled in order to delete specified environment

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

req = operations.GetEnvironmentsEnvIDDeleteDependenciesRequest(
    env_id='28b60297-9556-4e6f-93e6-0cc1c215a603',
)

res = s.envs.get_environments_env_id_delete_dependencies(req)

if res.delete_dependency_element_environments is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetEnvironmentsEnvIDDeleteDependenciesRequest](../../models/operations/getenvironmentsenviddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetEnvironmentsEnvIDDeleteDependenciesResponse](../../models/operations/getenvironmentsenviddeletedependenciesresponse.md)**


## post_environments

Add a  Secure Application environment. An instance should be contained in a single environment. The environment is defined by a VPC and an optional tag. If a tag is supplied, only instances in the specified VPC with the given tag will belong to the new environment.


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

req = shared.EnvironmentInput(
    aws_environments=[
        shared.AwsEnvironmentInput(
            tags=[
                shared.Tag(
                    key='<key>',
                    value='South',
                ),
            ],
            vpc=shared.VPCDescriptionInput(
                aws_account_id='Seaborgium',
                region_id='Northeast',
                vpc_id='invoice Honduras',
            ),
        ),
    ],
    kubernetes_environments=[
        shared.KubernetesEnvironmentInput(
            kubernetes_cluster='5a8916a0-e622-4811-bd3c-8c7fc23dd96f',
            namespace_labels=[
                shared.Label(
                    key='<key>',
                    value='Southwest group',
                ),
            ],
            namespaces=[
                'sievert',
            ],
        ),
    ],
    name='Prod',
)

res = s.envs.post_environments(req)

if res.environment is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.EnvironmentInput](../../models/shared/environmentinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostEnvironmentsResponse](../../models/operations/postenvironmentsresponse.md)**


## post_environments_batch

Add a number of new Secure Application environments. This is similar to the 'Add environment' method, but for multiple environments.


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

req = [
    shared.EnvironmentInput(
        aws_environments=[
            shared.AwsEnvironmentInput(
                tags=[
                    shared.Tag(
                        key='<key>',
                        value='Maine ampere',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='support round',
                    region_id='East',
                    vpc_id='Coast Facilitator bypassing',
                ),
            ),
        ],
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                kubernetes_cluster='198d741c-5bdf-45a6-87e9-5a1cd6d26b83',
                namespace_labels=[
                    shared.Label(
                        key='<key>',
                        value='West Customer',
                    ),
                ],
                namespaces=[
                    'except',
                ],
            ),
        ],
        name='Prod',
    ),
]

res = s.envs.post_environments_batch(req)

if res.environments is not None:
    # handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [list[shared.EnvironmentInput]](../../models//.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.PostEnvironmentsBatchResponse](../../models/operations/postenvironmentsbatchresponse.md)**


## post_environments_delete

Delete multiple Secure Application environments.


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


res = s.envs.post_environments_delete()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostEnvironmentsDeleteResponse](../../models/operations/postenvironmentsdeleteresponse.md)**


## put_environments_env_id_

Edit an existing Secure Application environment.


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

req = operations.PutEnvironmentsEnvIDRequest(
    environment_input=shared.EnvironmentInput(
        aws_environments=[
            shared.AwsEnvironmentInput(
                tags=[
                    shared.Tag(
                        key='<key>',
                        value='1080p into',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='tromp Upgradable',
                    region_id='paradigms eligendi',
                    vpc_id='Steel revolutionize Checking',
                ),
            ),
        ],
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                kubernetes_cluster='3566df6f-010d-4e05-b98d-e3a9acad0419',
                namespace_labels=[
                    shared.Label(
                        key='<key>',
                        value='portals Lakes West',
                    ),
                ],
                namespaces=[
                    'zero',
                ],
            ),
        ],
        name='Prod',
    ),
    env_id='efb650de-9801-4dae-8e96-7d9d0297331b',
)

res = s.envs.put_environments_env_id_(req)

if res.environment is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutEnvironmentsEnvIDRequest](../../models/operations/putenvironmentsenvidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutEnvironmentsEnvIDResponse](../../models/operations/putenvironmentsenvidresponse.md)**

