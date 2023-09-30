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

req = operations.GetEnvironmentsRequest(
    download_as_xlsx=False,
    include_system_envs=False,
    name='Pangender',
    sort_dir=operations.GetEnvironmentsSortDir.ASC,
    sort_key='Waltham if',
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
            id='3143be01-277d-4065-a891-6a0e622811bd',
            tags=[
                shared.Tag(
                    key='<key>',
                    value='blue',
                ),
            ],
            vpc=shared.VPCDescriptionInput(
                aws_account_id='sequestrate Square',
                name='keyboarding Southwest',
                region_id='sievert Nepalese',
                vpc_id='Card Electronic',
            ),
        ),
    ],
    description='Managed cohesive conglomeration',
    id='8b0df411-a017-4fec-b7c0-652306ac0dd6',
    is_system_env=False,
    kubernetes_environments=[
        shared.KubernetesEnvironmentInput(
            id='2ded15fb-507e-428f-8658-431e3d4048f3',
            kubernetes_cluster='1327f0e5-119e-46a7-bae1-a8564c416b7d',
            kubernetes_cluster_name='female Hat',
            namespace_labels=[
                shared.Label(
                    key='<key>',
                    value='Bedfordshire Northeast',
                ),
            ],
            namespaces=[
                'Tracy',
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
                id='925b166e-fc31-42c0-aebd-81198d741c5b',
                tags=[
                    shared.Tag(
                        key='<key>',
                        value='epithelium Architect transsexual',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='Touring',
                    name='maroon Designer Rubber',
                    region_id='Van',
                    vpc_id='Ouguiya Practical Sausages',
                ),
            ),
        ],
        description='Reactive multimedia open system',
        id='a8d71159-31ea-4cc0-a751-fa912e0c2e77',
        is_system_env=False,
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                id='81de4db5-179e-49e8-a850-eef1ac7cc5cf',
                kubernetes_cluster='7cd38ac9-5b1f-4cd3-b4df-81a2f60b1759',
                kubernetes_cluster_name='Avon male East',
                namespace_labels=[
                    shared.Label(
                        key='<key>',
                        value='Missouri magenta',
                    ),
                ],
                namespaces=[
                    'preface',
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
                id='57cf89fe-5e65-409c-b415-d6003566df6f',
                tags=[
                    shared.Tag(
                        key='<key>',
                        value='Avon',
                    ),
                ],
                vpc=shared.VPCDescriptionInput(
                    aws_account_id='actually communities Soul',
                    name='fatally Customer Accounts',
                    region_id='Cargo Mexico',
                    vpc_id='Fiat executive',
                ),
            ),
        ],
        description='Pre-emptive bifurcated access',
        id='4790c5f1-efb6-450d-a980-1dae0e967d9d',
        is_system_env=False,
        kubernetes_environments=[
            shared.KubernetesEnvironmentInput(
                id='0297331b-d38c-454f-9f13-9d5f8956b63c',
                kubernetes_cluster='b013e34e-0fd3-4e76-a959-cf530e5cf52d',
                kubernetes_cluster_name='Carolina Integration',
                namespace_labels=[
                    shared.Label(
                        key='<key>',
                        value='including Recumbent International',
                    ),
                ],
                namespaces=[
                    'Loan',
                ],
            ),
        ],
        name='Prod',
    ),
    env_id='fd1e02d4-5afd-490e-8b66-39364458cb01',
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

