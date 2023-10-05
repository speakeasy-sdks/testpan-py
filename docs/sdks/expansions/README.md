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
    expansion_id='f85d88d8-8509-415c-acc6-dcdc8448694e',
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
    cluster_name='Agent interface',
    controller_status='Funk Flerovium Road',
    controller_version='Quality',
    download_as_xlsx=False,
    max_results=2748.69,
    name='male payment Kentucky',
    namespace_name='Toyota',
    no_pagination=False,
    offset=4144.14,
    sort_dir=operations.GetExpansionsSortDir.DESC,
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
    expansion_id='f93ee138-484b-4ae8-9598-dc7e98557c98',
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
    cluster_id='ef536384-aae2-4f5a-87a4-cef022a42548',
    controller_last_active=dateutil.parser.isoparse('2023-08-24T22:57:12.780Z'),
    labels=[
        shared.Label(
            key='<key>',
            value='bolívar North Frozen',
        ),
    ],
    name='postmark',
    namespace_id='cab88259-ba11-4df1-9d86-c530fc31b7b3',
    should_send_metrics=False,
    workload_addresses=[
        shared.WorkloadAddress(
            address='23391 Padberg Keys',
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
                key='<key>',
                value='solemnly Money logistical',
            ),
        ],
        name='Kids Program',
        workload_addresses=[
            shared.WorkloadAddress(
                address='628 Will Route',
                network_protocol=shared.NetworkProtocol.TCP,
            ),
        ],
    ),
    expansion_id='4baa7b3c-4b09-4bff-8d17-0310c446aa3a',
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

