# Expansions
(*expansions*)

## Overview

APIs used to manage expansions on Secure Application

### Available Operations

* [delete_expansions_expansion_id_](#delete_expansions_expansion_id_) - Delete an expansion
* [get_expansions](#get_expansions) - List all the expansions on the system
* [get_expansions_expansion_id_install_expansion_tar_gz](#get_expansions_expansion_id_install_expansion_tar_gz) - Get the expansion installation
* [post_expansions](#post_expansions) - Create a new expansion
* [put_expansions_expansion_id_](#put_expansions_expansion_id_) - Edit expansion definition

## delete_expansions_expansion_id_

Delete an expansion

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteExpansionsExpansionIDRequest(
    expansion_id='f85d88d8-8509-415c-acc6-dcdc8448694e',
)

res = s.expansions.delete_expansions_expansion_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteExpansionsExpansionIDRequest](../../models/operations/deleteexpansionsexpansionidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteExpansionsExpansionIDResponse](../../models/operations/deleteexpansionsexpansionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_expansions

List all the expansions on the system

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetExpansionsRequest(
    sort_key=operations.GetExpansionsQueryParamSortKey.NAME,
)

res = s.expansions.get_expansions(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetExpansionsRequest](../../models/operations/getexpansionsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetExpansionsResponse](../../models/operations/getexpansionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_expansions_expansion_id_install_expansion_tar_gz

Get the expansion installation

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetExpansionsExpansionIDInstallExpansionTarGzRequest(
    expansion_id='f93ee138-484b-4ae8-9598-dc7e98557c98',
)

res = s.expansions.get_expansions_expansion_id_install_expansion_tar_gz(req)

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetExpansionsExpansionIDInstallExpansionTarGzRequest](../../models/operations/getexpansionsexpansionidinstallexpansiontargzrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetExpansionsExpansionIDInstallExpansionTarGzResponse](../../models/operations/getexpansionsexpansionidinstallexpansiontargzresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_expansions

Create a new expansion

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.ExpansionInput(
    cluster_id='ef536384-aae2-4f5a-87a4-cef022a42548',
    labels=[
        shared.Label(
            key='<key>',
            value='string',
        ),
    ],
    name='string',
    namespace_id='ea7db024-5fda-41fa-8ab8-8259ba11df19',
    workload_addresses=[
        shared.WorkloadAddress(
            address='547 Dean Brook',
        ),
    ],
)

res = s.expansions.post_expansions(req)

if res.expansion is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.ExpansionInput](../../models/shared/expansioninput.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostExpansionsResponse](../../models/operations/postexpansionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_expansions_expansion_id_

Edit expansion definition

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutExpansionsExpansionIDRequest(
    expansion_put=shared.ExpansionPut(
        labels=[
            shared.Label(
                key='<key>',
                value='string',
            ),
        ],
        name='string',
        workload_addresses=[
            shared.WorkloadAddress(
                address='218 Jenkins Gateway',
            ),
        ],
    ),
    expansion_id='159739a0-b94d-4cfc-a4ba-a7b3c4b09bff',
)

res = s.expansions.put_expansions_expansion_id_(req)

if res.expansion is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutExpansionsExpansionIDRequest](../../models/operations/putexpansionsexpansionidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutExpansionsExpansionIDResponse](../../models/operations/putexpansionsexpansionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
