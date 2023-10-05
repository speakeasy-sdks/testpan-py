# TrustedSigners
(*trusted_signers*)

## Overview

APIs used to  define and manage trusted signers

### Available Operations

* [delete_trusted_signers_trusted_signer_id_](#delete_trusted_signers_trusted_signer_id_) - Delete a trusted signer
* [get_trusted_signers](#get_trusted_signers) - Get a list of defined trusted signers
* [get_trusted_signers_trusted_signer_id_](#get_trusted_signers_trusted_signer_id_) - get existing trusted signer
* [post_trusted_signers](#post_trusted_signers) - Add new trusted signer
* [put_trusted_signers_trusted_signer_id_](#put_trusted_signers_trusted_signer_id_) - edit existing trusted signer

## delete_trusted_signers_trusted_signer_id_

Delete a trusted signer

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

req = operations.DeleteTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='72a0c357-f09f-4b54-84ce-1c9dc40be52b',
)

res = s.trusted_signers.delete_trusted_signers_trusted_signer_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTrustedSignersTrustedSignerIDRequest](../../models/operations/deletetrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteTrustedSignersTrustedSignerIDResponse](../../models/operations/deletetrustedsignerstrustedsigneridresponse.md)**


## get_trusted_signers

Get a list of defined trusted signers

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

req = operations.GetTrustedSignersRequest(
    sort_dir=operations.GetTrustedSignersSortDir.ASC,
    sort_key=operations.GetTrustedSignersSortKey.NAME,
)

res = s.trusted_signers.get_trusted_signers(req)

if res.trusted_signers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTrustedSignersRequest](../../models/operations/gettrustedsignersrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetTrustedSignersResponse](../../models/operations/gettrustedsignersresponse.md)**


## get_trusted_signers_trusted_signer_id_

get existing trusted signer

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

req = operations.GetTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='3d8f6f9a-2b35-44bb-82c6-f820a67d0e04',
)

res = s.trusted_signers.get_trusted_signers_trusted_signer_id_(req)

if res.trusted_signer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTrustedSignersTrustedSignerIDRequest](../../models/operations/gettrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTrustedSignersTrustedSignerIDResponse](../../models/operations/gettrustedsignerstrustedsigneridresponse.md)**


## post_trusted_signers

Add new trusted signer

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

req = shared.TrustedSignerInput(
    keys=[
        shared.TrustedSignerKey(
            key='<key>',
            name='Northeast Iowa',
        ),
    ],
    name='killer United Agender',
    trusted_signer_cloud_accounts=[
        shared.TrustedSignerCloudAccountInput(
            id='339127fc-1c35-45d9-9677-cf34f19a2406',
            status=shared.TrustedSignerClusterStatus.WARNING,
            validation=shared.TrustedSignerClusterValidation.HASH,
        ),
    ],
    trusted_signer_clusters=[
        shared.TrustedSignerClusterInput(
            id='22272998-72b1-4626-b1e4-e3bd500d0622',
            status=shared.TrustedSignerClusterStatus.WARNING,
            validation=shared.TrustedSignerClusterValidation.NONE,
        ),
    ],
)

res = s.trusted_signers.post_trusted_signers(req)

if res.trusted_signer is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.TrustedSignerInput](../../models/shared/trustedsignerinput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostTrustedSignersResponse](../../models/operations/posttrustedsignersresponse.md)**


## put_trusted_signers_trusted_signer_id_

edit existing trusted signer

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

req = operations.PutTrustedSignersTrustedSignerIDRequest(
    trusted_signer_input=shared.TrustedSignerInput(
        keys=[
            shared.TrustedSignerKey(
                key='<key>',
                name='Chrysler Centers',
            ),
        ],
        name='so static never',
        trusted_signer_cloud_accounts=[
            shared.TrustedSignerCloudAccountInput(
                id='2390f3eb-b00b-4b0b-a50b-1429abb4df87',
                status=shared.TrustedSignerClusterStatus.WARNING,
                validation=shared.TrustedSignerClusterValidation.NONE,
            ),
        ],
        trusted_signer_clusters=[
            shared.TrustedSignerClusterInput(
                id='af5cddc0-6513-44a6-9fd6-1a9bf59409fe',
                status=shared.TrustedSignerClusterStatus.VALID,
                validation=shared.TrustedSignerClusterValidation.SIGNATURE,
            ),
        ],
    ),
    trusted_signer_id='c650d3f6-4267-4f45-b31f-42c8f00b005e',
)

res = s.trusted_signers.put_trusted_signers_trusted_signer_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTrustedSignersTrustedSignerIDRequest](../../models/operations/puttrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PutTrustedSignersTrustedSignerIDResponse](../../models/operations/puttrustedsignerstrustedsigneridresponse.md)**

