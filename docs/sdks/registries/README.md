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
        password="<YOUR_PASSWORD_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## get_registries

Get a list of defined registries

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
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
| errors.SDKError | 4x-5xx          | */*             |

## post_registries

Add new registry

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.RegistryInput(
    type=shared.RegistryType.JFROG,
    url='http://serene-hotel.biz',
    cluster_ids=[
        '2a5fe89e-3548-44bf-9b5b-e5f9972484d3',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsType.JFROG_REGISTRY_CREDENTIALS,
    ),
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
| errors.SDKError | 4x-5xx          | */*             |

## post_registries_test_connection

test registry connection

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.RegistryInput(
    type=shared.RegistryType.AWS,
    url='http://imaginative-servitude.name',
    cluster_ids=[
        '7454e65c-1396-4b3e-8e8e-106ebca1e554',
    ],
    credentials=shared.RegistryCredentials(
        registry_credentials_type=shared.RegistryCredentialsType.JFROG_REGISTRY_CREDENTIALS,
    ),
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
| errors.SDKError | 4x-5xx          | */*             |

## post_registries_test_connection_registry_id_

test registry connection

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostRegistriesTestConnectionRegistryIDRequest(
    registry=shared.RegistryInput(
        type=shared.RegistryType.GCP,
        url='http://ordinary-shield.name',
        cluster_ids=[
            '980a8e5d-f00f-47af-9c1e-7dae13c52516',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsType.JFROG_REGISTRY_CREDENTIALS,
        ),
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
| errors.SDKError | 4x-5xx          | */*             |

## put_registries_registry_id_

edit existing registry

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutRegistriesRegistryIDRequest(
    registry=shared.RegistryInput(
        type=shared.RegistryType.JFROG,
        url='https://narrow-encirclement.info',
        cluster_ids=[
            'b9190fe9-27c3-48c5-8c07-f3bb11811d80',
        ],
        credentials=shared.RegistryCredentials(
            registry_credentials_type=shared.RegistryCredentialsType.STANDARD_REGISTRY_CREDENTIALS,
        ),
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
| errors.SDKError | 4x-5xx          | */*             |
