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
    env_id='ef51fcb4-c593-4ec1-acda-ad0ec7afedbd',
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

req = operations.GetEnvironmentsRequest(
    download_as_xlsx=False,
    include_system_envs=False,
    name='Richard Smith',
    sort_dir=operations.GetEnvironmentsSortDir.ASC,
    sort_key=operations.GetEnvironmentsSortKey.NAME,
)

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
    env_id='8a47f939-0c58-4880-983d-abf9ef3ffdd9',
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
    env_id='f7f079af-4d35-4724-8db0-f4d281187d56',
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
            id='844eded8-5a90-465e-a28b-dfc2032b6c87',
            tags=[
                shared.Tag(
                    key='omnis',
                    value='omnis',
                ),
            ],
            vpc=shared.VPCDescriptionInput(
                aws_account_id='fugit',
                name='Melody Kreiger I',
                region_id='ad',
                vpc_id='atque',
            ),
        ),
    ],
    description='ut',
    id='f7ae12c6-891f-482c-a115-7172305377dc',
    is_system_env=False,
    kubernetes_environments=[
        shared.KubernetesEnvironmentInput(
            id='fa89df97-5e35-4668-a092-e9c3ddc5f111',
            kubernetes_cluster='dea1026d-541a-44d1-90fe-b21780bccc0d',
            kubernetes_cluster_name='distinctio',
            namespace_labels=[
                shared.Label(
                    key='distinctio',
                    value='assumenda',
                ),
            ],
            namespaces=[
                'illum',
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
                id='b484708f-b4e3-491e-abc1-58c4c4e54599',
                tags=[
                    shared.Tag(
                        key='itaque',
                        value='fuga',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='consectetur',
                    name='Nicole Christiansen DVM',
                    region_id='sint',
                    vpc_id='nobis',
                ),
            ),
        ],
        description='qui',
        id='00ce78a1-bd8f-4b7a-8a11-6ce723d4097f',
        is_system_env=False,
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                id='a30e9af7-25b2-4912-a030-d83f5aeb7799',
                kubernetes_cluster='d22e8c1f-8493-4825-bdc4-2c876c2c2dfb',
                kubernetes_cluster_name='aliquam',
                namespace_labels=[
                    shared.Label(
                        key='eligendi',
                        value='hic',
                    ),
                ],
                namespaces=[
                    'quo',
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
                id='1c76230f-841f-4b1b-923f-db14db6be5a6',
                tags=[
                    shared.Tag(
                        key='laudantium',
                        value='corporis',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='excepturi',
                    name='Alfredo Tromp',
                    region_id='laborum',
                    vpc_id='vero',
                ),
            ),
        ],
        description='eos',
        id='0da16fc2-b271-4a28-9c57-e854e90439d2',
        is_system_env=False,
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                id='22465694-6240-4708-8f7a-b37cef022251',
                kubernetes_cluster='94db5541-0adc-4669-af90-a26c7cdc981f',
                kubernetes_cluster_name='voluptatem',
                namespace_labels=[
                    shared.Label(
                        key='aliquid',
                        value='laudantium',
                    ),
                ],
                namespaces=[
                    'unde',
                ],
            ),
        ],
        name='Prod',
    ),
    env_id='81d6bb33-cfaa-4348-831b-f407ee4fcf0c',
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

