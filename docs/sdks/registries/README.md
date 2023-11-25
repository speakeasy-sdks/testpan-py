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
    registry_id='e5f28387-13f7-45c6-911a-2f9bf926c17f',
)

res = s.registries.delete_registries_registry_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteRegistriesRegistryIDRequest](../../models/operations/deleteregistriesregistryidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.DeleteRegistriesRegistryIDResponse](../../models/operations/deleteregistriesregistryidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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

req = operations.GetRegistriesRequest()

res = s.registries.get_registries(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetRegistriesRequest](../../models/operations/getregistriesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetRegistriesResponse](../../models/operations/getregistriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
        '95b632a5-fe89-4e35-884b-fdb5be5f9972',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsType.AWS_REGISTRY_CREDENTIALS,
    ),
    type=shared.RegistryType.AZURE,
    url='http://svelte-curio.org',
)

res = s.registries.post_registries(req)

if res.registry is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RegistryInput](../../models/shared/registryinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostRegistriesResponse](../../models/operations/postregistriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
        '146c9745-4e65-4c13-96b3-e4e8e106ebca',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsType.AWS_REGISTRY_CREDENTIALS,
    ),
    type=shared.RegistryType.OTHER,
    url='http://handy-energy.net',
)

res = s.registries.post_registries_test_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RegistryInput](../../models/shared/registryinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostRegistriesTestConnectionResponse](../../models/operations/postregistriestestconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
    registry=shared.RegistryInput(
        cluster_ids=[
            '309c9980-a8e5-4df0-8f7a-f1c1e7dae13c',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsType.STANDARD_REGISTRY_CREDENTIALS,
        ),
        type=shared.RegistryType.AWS,
        url='http://blond-horror.org',
    ),
    registry_id='99bd4248-5508-4257-836a-3d0e30be4155',
)

res = s.registries.post_registries_test_connection_registry_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PostRegistriesTestConnectionRegistryIDRequest](../../models/operations/postregistriestestconnectionregistryidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PostRegistriesTestConnectionRegistryIDResponse](../../models/operations/postregistriestestconnectionregistryidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
    registry=shared.RegistryInput(
        cluster_ids=[
            'bb846b91-90fe-4927-838c-5cc07f3bb118',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsType.AWS_REGISTRY_CREDENTIALS,
        ),
        type=shared.RegistryType.AWS,
        url='https://mixed-affiliate.info',
    ),
    registry_id='a8f4138b-1ba6-41a9-bb5f-375f1e0e9ee0',
)

res = s.registries.put_registries_registry_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PutRegistriesRegistryIDRequest](../../models/operations/putregistriesregistryidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PutRegistriesRegistryIDResponse](../../models/operations/putregistriesregistryidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
