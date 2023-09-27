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
        password="",
        username="",
    ),
)

req = operations.DeleteExpansionsExpansionIDRequest(
    expansion_id='42b78f15-6263-498a-8dc7-66324ccb06c8',
)

res = s.expansions.delete_expansions_expansion_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeleteExpansionsExpansionIDRequest](../../models/operations/deleteexpansionsexpansionidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeleteExpansionsExpansionIDResponse](../../models/operations/deleteexpansionsexpansionidresponse.md)**


## get_expansions

List all the expansions on the system

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

req = operations.GetExpansionsRequest(
    cluster_name='optio',
    controller_status='est',
    controller_version='inventore',
    download_as_xlsx=False,
    max_results=1648.05,
    name='Mark D'Amore',
    namespace_name='perspiciatis',
    no_pagination=False,
    offset=1664.01,
    sort_dir=operations.GetExpansionsSortDir.ASC,
    sort_key=operations.GetExpansionsSortKey.NAME,
)

res = s.expansions.get_expansions(req)

if res.expansions is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetExpansionsRequest](../../models/operations/getexpansionsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetExpansionsResponse](../../models/operations/getexpansionsresponse.md)**


## get_expansions_expansion_id_install_expansion_tar_gz

Get the expansion installation

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

req = operations.GetExpansionsExpansionIDInstallExpansionTarGzRequest(
    expansion_id='0b8d5722-dd89-45b8-bcf2-4db959693352',
)

res = s.expansions.get_expansions_expansion_id_install_expansion_tar_gz(req)

if res.get_expansions_expansion_id_install_expansion_tar_gz_200_application_json_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetExpansionsExpansionIDInstallExpansionTarGzRequest](../../models/operations/getexpansionsexpansionidinstallexpansiontargzrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetExpansionsExpansionIDInstallExpansionTarGzResponse](../../models/operations/getexpansionsexpansionidinstallexpansiontargzresponse.md)**


## post_expansions

Create a new expansion

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.ExpansionInput(
    cluster_id='f7453399-4d78-4de3-b6e9-389f5abb7f66',
    controller_last_active=dateutil.parser.isoparse('2022-08-24T06:52:21.437Z'),
    labels=[
        shared.Label(
            key='ullam',
            value='doloremque',
        ),
    ],
    name='Clarence Lang',
    namespace_id='2ac483af-d231-45bb-a650-164e06f5bf6a',
    should_send_metrics=False,
    workload_addresses=[
        shared.WorkloadAddress(
            address='351 Schaefer Loop',
            network_protocol=shared.NetworkProtocol.HTTP,
        ),
    ],
)

res = s.expansions.post_expansions(req)

if res.expansion is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.ExpansionInput](../../models/shared/expansioninput.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostExpansionsResponse](../../models/operations/postexpansionsresponse.md)**


## put_expansions_expansion_id_

Edit expansion definition

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

req = operations.PutExpansionsExpansionIDRequest(
    expansion_put=shared.ExpansionPut(
        labels=[
            shared.Label(
                key='assumenda',
                value='repudiandae',
            ),
        ],
        name='Mr. Dale Jenkins',
        workload_addresses=[
            shared.WorkloadAddress(
                address='2710 Vena Square',
                network_protocol=shared.NetworkProtocol.HTTP,
            ),
        ],
    ),
    expansion_id='840774a6-8a9a-435d-886b-6f66fef020e9',
)

res = s.expansions.put_expansions_expansion_id_(req)

if res.expansion is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PutExpansionsExpansionIDRequest](../../models/operations/putexpansionsexpansionidrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PutExpansionsExpansionIDResponse](../../models/operations/putexpansionsexpansionidresponse.md)**

