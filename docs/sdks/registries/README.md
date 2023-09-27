# Registries
(*registries*)

## Overview

APIs used to  define and manage registries

### Available Operations

* [delete_registries_registry_id_](#delete_registries_registry_id_) - Delete a registry
* [get_registries](#get_registries) - Get a list of defined registries
* [post_registries](#post_registries) - Add new registry
* [post_registries_test_connection](#post_registries_test_connection) - test registry connection
* [post_registries_test_connection_registry_id_](#post_registries_test_connection_registry_id_) - test registry connection
* [put_registries_registry_id_](#put_registries_registry_id_) - edit existing registry

## delete_registries_registry_id_

Delete a registry

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

req = operations.DeleteRegistriesRegistryIDRequest(
    registry_id='b7021a52-046b-464e-99fb-0e67e094fdfe',
)

res = s.registries.delete_registries_registry_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteRegistriesRegistryIDRequest](../../models/operations/deleteregistriesregistryidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.DeleteRegistriesRegistryIDResponse](../../models/operations/deleteregistriesregistryidresponse.md)**


## get_registries

Get a list of defined registries

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

req = operations.GetRegistriesRequest(
    sort_dir=operations.GetRegistriesSortDir.DESC,
    sort_key=operations.GetRegistriesSortKey.URL,
)

res = s.registries.get_registries(req)

if res.registries is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetRegistriesRequest](../../models/operations/getregistriesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetRegistriesResponse](../../models/operations/getregistriesresponse.md)**


## post_registries

Add new registry

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

req = shared.RegistryInput(
    cluster_ids=[
        '5540ef53-a34a-41b8-be99-731adc05d85a',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsRegistryCredentialsType.JFROG_REGISTRY_CREDENTIALS,
    ),
    type=shared.RegistryType.AWS,
    url='illum',
)

res = s.registries.post_registries(req)

if res.registry is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RegistryInput](../../models/shared/registryinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostRegistriesResponse](../../models/operations/postregistriesresponse.md)**


## post_registries_test_connection

test registry connection

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

req = shared.RegistryInput(
    cluster_ids=[
        'fb70fb38-7429-40d3-b656-1eca16ef8945',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsRegistryCredentialsType.AWS_REGISTRY_CREDENTIALS,
    ),
    type=shared.RegistryType.JFROG,
    url='facere',
)

res = s.registries.post_registries_test_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RegistryInput](../../models/shared/registryinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostRegistriesTestConnectionResponse](../../models/operations/postregistriestestconnectionresponse.md)**


## post_registries_test_connection_registry_id_

test registry connection

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

req = operations.PostRegistriesTestConnectionRegistryIDRequest(
    registry_input=shared.RegistryInput(
        cluster_ids=[
            '76eeeb51-8c4d-4a1f-ad35-512f06d4e5b7',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsRegistryCredentialsType.AWS_REGISTRY_CREDENTIALS,
        ),
        type=shared.RegistryType.OTHER,
        url='alias',
    ),
    registry_id='f548568a-0424-4e00-a1d6-eb9434645d03',
)

res = s.registries.post_registries_test_connection_registry_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PostRegistriesTestConnectionRegistryIDRequest](../../models/operations/postregistriestestconnectionregistryidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PostRegistriesTestConnectionRegistryIDResponse](../../models/operations/postregistriestestconnectionregistryidresponse.md)**


## put_registries_registry_id_

edit existing registry

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

req = operations.PutRegistriesRegistryIDRequest(
    registry_input=shared.RegistryInput(
        cluster_ids=[
            '084fbba5-ccef-4f5c-b01f-e51e528a45ac',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsRegistryCredentialsType.STANDARD_REGISTRY_CREDENTIALS,
        ),
        type=shared.RegistryType.AWS,
        url='distinctio',
    ),
    registry_id='85f8bc2c-aba8-4da4-927d-d597ff4711aa',
)

res = s.registries.put_registries_registry_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PutRegistriesRegistryIDRequest](../../models/operations/putregistriesregistryidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PutRegistriesRegistryIDResponse](../../models/operations/putregistriesregistryidresponse.md)**

